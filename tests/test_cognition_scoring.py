from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest

from gensigma_benchmarks.cognition_scoring import (
    CognitionScorer,
    ForecastObservation,
    MetricCatalog,
    ScoringConfigurationError,
    brier_score,
    calibration_summary,
    hard_constraint_violations,
    policy_authority_violations,
    trace_completeness,
    unsupported_evidence_references,
)
from gensigma_benchmarks.executive_cognition import seal_result, stable_digest


FIXTURES = Path("benchmarks/executive-cognition/fixtures")
METRICS = Path("benchmarks/executive-cognition/config/cognition-metrics-v1.json")
NOW = "2026-09-07T06:10:00Z"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def case() -> dict:
    return load_json(FIXTURES / "bid-no-bid-valid.json")


def rules() -> dict:
    return load_json(FIXTURES / "bid-no-bid-scoring-rules-v1.json")


def arm_output(**overrides) -> dict:
    value = {
        "contract_version": "arm-output/0.1",
        "result_id": "result-score-001",
        "result_version": "1.0.0",
        "run_id": "run-score-001",
        "created_at": NOW,
        "recommendation": "gather_evidence",
        "rationale": "Partner availability is unresolved.",
        "alternatives_considered": ["bid", "decline"],
        "assumptions": ["The deadline is unchanged."],
        "uncertainties": [],
        "reversal_conditions": ["A qualified partner commits."],
        "method_trace": [
            {
                "method_id": "test-method",
                "method_version": "1.0.0",
                "role": "analysis",
                "material_contribution": "Produced a test recommendation.",
            }
        ],
        "evidence_refs": ["evidence-solicitation-001"],
        "authority_status": "approval_required",
    }
    value.update(overrides)
    return seal_result(value)


def run_manifest(decision_case: dict) -> dict:
    return {
        "contract_version": "evaluation-run/0.1",
        "run_id": "run-score-001",
        "run_version": "1.0.0",
        "run_attempt": 1,
        "case_ref": {
            "id": decision_case["case_id"],
            "version": decision_case["case_version"],
            "digest": stable_digest(decision_case),
        },
        "arm_ref": {
            "id": "test-arm",
            "version": "1.0.0",
            "digest": "a" * 64,
        },
        "configuration_versions": [],
        "model_versions": [],
        "prompt_versions": [],
        "tool_versions": [],
        "metric_versions": list(MetricCatalog(METRICS).component_versions()),
        "random_seed": None,
        "started_at": NOW,
        "completed_at": NOW,
        "input_digest": "b" * 64,
    }


def test_brier_score_matches_hand_calculated_examples() -> None:
    assert brier_score([ForecastObservation("f1", 0.8, 1)]) == pytest.approx(0.04)
    assert brier_score(
        [ForecastObservation("f1", 0.8, 1), ForecastObservation("f2", 0.3, 0)]
    ) == pytest.approx(0.065)


@pytest.mark.parametrize(
    "probability,outcome",
    [(-0.01, 0), (1.01, 1), (0.5, 2), (True, 1)],
)
def test_forecast_observations_reject_invalid_values(probability, outcome) -> None:
    with pytest.raises(ValueError):
        ForecastObservation("bad", probability, outcome)


def test_calibration_requires_explicit_bins_and_minimum_sample() -> None:
    small = [ForecastObservation(f"f-{index}", 0.5, index % 2) for index in range(4)]
    assert calibration_summary(small, minimum_sample_size=20)["status"] == (
        "not_requested"
    )
    insufficient = calibration_summary(
        small, minimum_sample_size=20, bin_edges=(0, 0.5, 1)
    )
    assert insufficient == {
        "status": "insufficient_sample",
        "sample_size": 4,
        "minimum_sample_size": 20,
    }
    assert "bins" not in insufficient


def test_calibration_bins_only_when_configured_and_sufficient() -> None:
    observations = [
        ForecastObservation(f"f-{index}", 0.25 if index < 10 else 0.75, index % 2)
        for index in range(20)
    ]
    summary = calibration_summary(
        observations, minimum_sample_size=20, bin_edges=(0, 0.5, 1)
    )
    assert summary["status"] == "computed"
    assert [item["count"] for item in summary["bins"]] == [10, 10]


def test_deterministic_checks_only_use_explicit_structured_rules() -> None:
    decision_case = case()
    fixture_rules = rules()
    output = arm_output()
    assert hard_constraint_violations(decision_case, output, fixture_rules) == []
    assert policy_authority_violations(output, fixture_rules) == []
    assert trace_completeness(output, fixture_rules) == (1.0, [])
    assert unsupported_evidence_references(decision_case, output) == []

    decision_case["decision_input"]["context"]["policy_authority"][
        "hard_constraints"
    ][0]["satisfied"] = False
    violating = arm_output(
        recommendation="bid",
        authority_status="executable",
        assumptions=[],
        evidence_refs=["unsupported-evidence"],
    )
    assert hard_constraint_violations(decision_case, violating, fixture_rules) == [
        "registration-required"
    ]
    assert len(policy_authority_violations(violating, fixture_rules)) == 1
    completeness, missing = trace_completeness(violating, fixture_rules)
    assert completeness == pytest.approx(0.875)
    assert missing == ["assumptions"]
    assert unsupported_evidence_references(decision_case, violating) == [
        "unsupported-evidence"
    ]


def test_unknown_fixture_constraint_fails_instead_of_guessing() -> None:
    fixture_rules = copy.deepcopy(rules())
    fixture_rules["hard_constraint_rules"][0]["rule_id"] = "not-in-case"
    with pytest.raises(ScoringConfigurationError, match="unknown hard constraint"):
        hard_constraint_violations(case(), arm_output(), fixture_rules)


def test_scoring_engine_emits_separate_versioned_contract_results() -> None:
    decision_case = case()
    observations = (
        ForecastObservation("award-forecast", 0.3, 0),
        ForecastObservation("submission-forecast", 0.9, 1),
    )
    results = CognitionScorer(
        MetricCatalog(METRICS), clock=lambda: NOW
    ).score(
        decision_case=decision_case,
        run_manifest=run_manifest(decision_case),
        arm_output=arm_output(),
        fixture_rules=rules(),
        operational_metadata={
            "latency_ms": 1250,
            "cost_usd": 0.04,
            "retry_count": 0,
        },
        forecasts=observations,
        calibration_bin_edges=(0, 0.5, 1),
    )
    by_id = {item["metric_id"]: item for item in results}

    assert by_id["hard-constraint-violations"]["value"] == 0
    assert by_id["hard-constraint-violations"]["details"][
        "fixture_rules_ref"
    ]["rules_version"] == "1.0.0"
    assert by_id["latency-ms"]["value"] == 1250
    assert by_id["cost-usd"]["value"] == pytest.approx(0.04)
    forecast = by_id["binary-brier-score"]
    assert forecast["value"] == pytest.approx(0.05)
    assert len(forecast["details"]["observations"]) == 2
    assert forecast["details"]["calibration"]["status"] == "insufficient_sample"
    rubric = by_id["executive-quality-rubric"]
    assert rubric["metric_kind"] == "human_rubric"
    assert rubric["value"] is None
    assert rubric["details"]["status"] == "awaiting_human_review"
    assert all(item["metric_version"] == "1.0.0" for item in results)
    assert all(item["result_digest"] for item in results)
    assert "composite-score" not in by_id


def test_scoring_rejects_run_identity_mismatch() -> None:
    decision_case = case()
    output = arm_output(run_id="different-run")
    with pytest.raises(ValueError, match="same run"):
        CognitionScorer(MetricCatalog(METRICS)).score(
            decision_case=decision_case,
            run_manifest=run_manifest(decision_case),
            arm_output=output,
            fixture_rules=rules(),
        )


def test_scoring_rejects_rules_for_a_different_case_version() -> None:
    decision_case = case()
    fixture_rules = rules()
    fixture_rules["case_version"] = "2.0.0"
    with pytest.raises(ScoringConfigurationError, match="same case version"):
        CognitionScorer(MetricCatalog(METRICS)).score(
            decision_case=decision_case,
            run_manifest=run_manifest(decision_case),
            arm_output=arm_output(),
            fixture_rules=fixture_rules,
        )
