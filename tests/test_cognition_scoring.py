from __future__ import annotations

import json

import pytest

from gensigma_benchmarks.cognition_scoring import (
    CognitionScorer,
    ForecastObservation,
    MetricCatalog,
)
from gensigma_benchmarks.cognition_arms import EvaluationRunner, StaticScorecardBaseline
from gensigma_benchmarks.executive_cognition import CognitionContractRegistry
from gensigma_benchmarks.executive_cognition import FrozenCaseLoader


NOW = "2026-09-07T07:00:00Z"
FIXTURE = "benchmarks/executive-cognition/fixtures/bid-no-bid-valid.json"
SCORECARD = "benchmarks/executive-cognition/config/bid-no-bid-scorecard-v1.json"
RULES = "benchmarks/executive-cognition/config/bid-no-bid-scoring-rules-v1.json"


def scorer() -> CognitionScorer:
    return CognitionScorer(clock=lambda: NOW)


def test_explicit_constraint_and_authority_rules_have_known_counts() -> None:
    output = {"recommendation": "bid", "authority_status": "executable"}
    rules = json.loads(open(RULES, encoding="utf-8").read())

    hard_result = scorer().score_explicit_rules(
        "run-001", "hard-constraint-violations", rules["hard_constraint_rules"], output
    )
    authority_result = scorer().score_explicit_rules(
        "run-001",
        "policy-authority-violations",
        rules["policy_authority_rules"],
        output,
    )

    assert hard_result["value"] == 1
    assert authority_result["value"] == 1
    assert hard_result["details"]["violations"][0]["rule_id"] == (
        "registration-required-when-unsatisfied"
    )


def test_required_fields_and_evidence_references_are_deterministic() -> None:
    output = {
        "recommendation": "bid",
        "rationale": "",
        "evidence_refs": ["known-evidence", "invented-evidence"],
    }
    completeness = scorer().score_required_fields(
        "run-001", output, ["recommendation", "rationale", "method_trace"]
    )
    support = scorer().score_evidence_references(
        "run-001",
        output,
        ["known-evidence"],
        structured_claims=[
            {"claim_id": "claim-1", "evidence_refs": ["known-evidence"]},
            {"claim_id": "claim-2", "evidence_refs": []},
        ],
    )

    assert completeness["value"] == pytest.approx(1 / 3)
    assert completeness["details"]["missing_fields"] == ["method_trace", "rationale"]
    assert support["value"] == 2
    assert support["details"]["invalid_evidence_refs"] == ["invented-evidence"]
    assert support["details"]["unsupported_structured_claim_ids"] == ["claim-2"]
    assert support["details"]["unstructured_rationale_scored"] is False


@pytest.mark.parametrize(
    ("probability", "outcome", "expected"),
    [(0.0, 0, 0.0), (1.0, 1, 0.0), (0.8, 1, 0.04), (0.8, 0, 0.64)],
)
def test_binary_brier_score_hand_calculated_examples(
    probability: float, outcome: int, expected: float
) -> None:
    result = scorer().score_binary_forecasts(
        "run-forecast", [ForecastObservation("forecast-1", probability, outcome)]
    )
    assert result["value"] == pytest.approx(expected)


def test_brier_mean_retains_raw_probability_outcome_pairs() -> None:
    observations = [
        ForecastObservation("forecast-1", 0.8, 1),
        ForecastObservation("forecast-2", 0.3, 0),
    ]
    result = scorer().score_binary_forecasts("run-forecast", observations)

    assert result["value"] == pytest.approx(0.065)
    assert result["details"]["observations"] == [item.as_dict() for item in observations]
    assert result["metric_version"] == "1.0.0"


def test_calibration_is_not_binned_below_documented_minimum() -> None:
    result = scorer().calibration_summary(
        "run-forecast", [ForecastObservation("forecast-1", 0.8, 1)]
    )

    assert result["value"] is None
    assert result["details"]["status"] == "insufficient_sample"
    assert result["details"]["minimum_sample_size"] == 30
    assert result["details"]["bins"] == []


def test_operational_metadata_is_ingested_without_composite_score() -> None:
    result = scorer().score_operational_metadata(
        "run-001", latency_ms=125.5, cost_usd=0.031
    )
    assert result["value"] == 125.5
    assert result["details"] == {"latency_ms": 125.5, "cost_usd": 0.031}


def test_human_rubric_hooks_are_non_automated_metadata() -> None:
    hooks = MetricCatalog().rubric_hooks()
    assert len(hooks) == 1
    assert hooks[0].as_dict()["metric_kind"] == "human_rubric"
    assert hooks[0].as_dict()["automated"] is False


def test_metric_results_are_sealed_versioned_contracts() -> None:
    result = scorer().score_required_fields("run-001", {"a": 1}, ["a"])
    CognitionContractRegistry().validate("MetricResult", result)
    assert result["metric_version"] == "1.0.0"
    assert len(result["metric_result_id"]) == 64
    assert len(result["result_digest"]) == 64


def test_metric_version_ref_is_accepted_by_evaluation_runner_manifest() -> None:
    ref = MetricCatalog().version_ref("binary-brier-score")
    execution = EvaluationRunner(clock=lambda: NOW).run(
        StaticScorecardBaseline(SCORECARD),
        FrozenCaseLoader().load(FIXTURE).arm_input,
        run_id="run-versioned-metrics",
        run_attempt=1,
        metric_versions=(ref,),
    )
    assert execution.run_manifest["metric_versions"] == [ref]
    assert ref["version"] == "1.0.0"
    assert len(ref["configuration_digest"]) == 64


def test_invalid_probabilities_outcomes_and_operational_values_fail() -> None:
    with pytest.raises(ValueError, match="probability"):
        ForecastObservation("forecast", 1.1, 1)
    with pytest.raises(ValueError, match="outcome"):
        ForecastObservation("forecast", 0.5, 2)
    with pytest.raises(ValueError, match="latency_ms"):
        scorer().score_operational_metadata("run", latency_ms=-1, cost_usd=None)
