from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest

from gensigma_benchmarks.executive_cognition import (
    BenchmarkContractViolation,
    CognitionContractRegistry,
    canonical_json,
    immutable_result_identity,
    seal_result,
    stable_digest,
)


FIXTURES = Path("benchmarks/executive-cognition/fixtures")
NOW = "2026-09-06T20:00:00Z"
DIGEST_A = "a" * 64
DIGEST_B = "b" * 64


def load_fixture(relative_path: str) -> dict:
    return json.loads((FIXTURES / relative_path).read_text(encoding="utf-8"))


@pytest.fixture
def contracts() -> CognitionContractRegistry:
    return CognitionContractRegistry()


def component(component_id: str, version: str = "1.0.0") -> dict:
    return {"id": component_id, "version": version, "configuration_digest": None}


def run_manifest(run_id: str, attempt: int) -> dict:
    return {
        "contract_version": "evaluation-run/0.1",
        "run_id": run_id,
        "run_version": "1.0.0",
        "run_attempt": attempt,
        "case_ref": {"id": "synthetic-bid-001", "version": "1.0.0", "digest": DIGEST_A},
        "arm_ref": {"id": "scorecard-baseline", "version": "1.0.0", "digest": DIGEST_B},
        "configuration_versions": [component("bid-scorecard-config")],
        "model_versions": [],
        "prompt_versions": [],
        "tool_versions": [component("gensigma-benchmarks", "0.1.0")],
        "metric_versions": [component("hard-constraint-violations")],
        "random_seed": None,
        "started_at": NOW,
        "completed_at": NOW,
        "input_digest": DIGEST_A,
    }


def test_valid_bid_no_bid_case_and_held_out_outcome_validate(
    contracts: CognitionContractRegistry,
) -> None:
    contracts.validate("DecisionCase", load_fixture("bid-no-bid-valid.json"))
    contracts.validate(
        "HeldOutOutcome", load_fixture("bid-no-bid-outcome-valid.json")
    )


@pytest.mark.parametrize(
    ("contract_name", "fixture_path", "location"),
    [
        ("DecisionCase", "invalid/missing-as-of.json", "<root>"),
        ("DecisionCase", "invalid/mixed-outcome-input.json", "decision_input"),
        ("DecisionCase", "invalid/invalid-reference.json", "evidence_refs"),
        ("EvaluationRun", "invalid/incomplete-run-manifest.json", "<root>"),
    ],
)
def test_invalid_fixtures_fail_deterministically(
    contracts: CognitionContractRegistry,
    contract_name: str,
    fixture_path: str,
    location: str,
) -> None:
    with pytest.raises(BenchmarkContractViolation, match=location):
        contracts.validate(contract_name, load_fixture(fixture_path))


def test_normal_arm_input_excludes_outcome_and_is_immutable(
    contracts: CognitionContractRegistry,
) -> None:
    arm_input = contracts.arm_input(load_fixture("bid-no-bid-valid.json"))

    assert not hasattr(arm_input, "outcome")
    assert "outcome" not in arm_input.decision_input
    with pytest.raises(TypeError):
        arm_input.decision_input["outcome"] = {"award_result": "loss"}


def test_repeated_runs_have_distinct_immutable_identities(
    contracts: CognitionContractRegistry,
) -> None:
    first = run_manifest("run-synthetic-001", 1)
    second = run_manifest("run-synthetic-002", 2)

    contracts.validate("EvaluationRun", first)
    contracts.validate("EvaluationRun", second)
    assert stable_digest(first) != stable_digest(second)
    assert immutable_result_identity(first["run_id"], {}) != immutable_result_identity(
        second["run_id"], {}
    )


def test_serialization_and_result_digests_are_stable(
    contracts: CognitionContractRegistry,
) -> None:
    assert canonical_json({"b": 2, "a": 1}) == '{"a":1,"b":2}'
    assert stable_digest({"b": 2, "a": 1}) == stable_digest({"a": 1, "b": 2})

    output = {
        "contract_version": "arm-output/0.1",
        "result_id": "result-synthetic-001",
        "result_version": "1.0.0",
        "run_id": "run-synthetic-001",
        "created_at": NOW,
        "recommendation": "gather_evidence",
        "rationale": "Partner availability is material and unresolved.",
        "alternatives_considered": ["bid", "decline"],
        "assumptions": ["The deadline remains unchanged"],
        "uncertainties": [],
        "reversal_conditions": ["A qualified partner commits before the deadline"],
        "method_trace": [
            {
                "method_id": "hard-constraint-gate",
                "method_version": "0.1.0",
                "role": "gate",
                "material_contribution": "Confirmed mandatory registration is satisfied.",
            }
        ],
        "evidence_refs": ["evidence-solicitation-001"],
        "authority_status": "approval_required",
    }
    sealed = seal_result(output)
    contracts.validate("ArmOutput", sealed)

    tampered = copy.deepcopy(sealed)
    tampered["recommendation"] = "bid"
    with pytest.raises(BenchmarkContractViolation, match="result_digest"):
        contracts.validate("ArmOutput", tampered)


def test_all_remaining_contract_surfaces_validate(
    contracts: CognitionContractRegistry,
) -> None:
    evidence = load_fixture("bid-no-bid-valid.json")["evidence"][0]
    contracts.validate("DecisionTimeEvidenceRef", evidence)

    arm = {
        "contract_version": "evaluation-arm/0.1",
        "arm_id": "scorecard-baseline",
        "arm_version": "1.0.0",
        "arm_type": "scorecard",
        "configuration_versions": [component("bid-scorecard-config")],
        "model_versions": [],
        "prompt_versions": [],
        "tool_versions": [component("gensigma-benchmarks", "0.1.0")],
    }
    contracts.validate("EvaluationArm", arm)

    metric = seal_result(
        {
            "contract_version": "metric-result/0.1",
            "metric_result_id": "metric-result-001",
            "metric_id": "hard-constraint-violations",
            "metric_version": "1.0.0",
            "run_id": "run-synthetic-001",
            "metric_kind": "deterministic",
            "value": 0,
            "details": {},
            "computed_at": NOW,
        }
    )
    contracts.validate("MetricResult", metric)

    review = {
        "contract_version": "human-review-packet/0.1",
        "packet_id": "packet-001",
        "packet_version": "1.0.0",
        "case_ref": {"id": "synthetic-bid-001", "version": "1.0.0", "digest": DIGEST_A},
        "rubric_version": "1.0.0",
        "blind_result_refs": [{"id": "result-A", "version": "1.0.0", "digest": DIGEST_B}],
        "randomization_seed_digest": DIGEST_A,
        "generated_at": NOW,
    }
    contracts.validate("HumanReviewPacket", review)

    report = seal_result(
        {
            "contract_version": "benchmark-report/0.1",
            "report_id": "report-001",
            "report_version": "1.0.0",
            "case_refs": [{"id": "synthetic-bid-001", "version": "1.0.0", "digest": DIGEST_A}],
            "run_refs": [{"id": "run-synthetic-001", "version": "1.0.0", "digest": DIGEST_B}],
            "metric_versions": [component("hard-constraint-violations")],
            "review_packet_refs": [],
            "artifact_refs": ["artifact://report-001/results.json"],
            "generated_at": NOW,
        }
    )
    contracts.validate("BenchmarkReport", report)
