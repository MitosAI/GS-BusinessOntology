from __future__ import annotations

import copy

import pytest

from gensigma_benchmarks.cognition_review import (
    BenchmarkReporter,
    ReviewConfigurationError,
    ReviewPacketBuilder,
    ReviewResponse,
    reconcile_reviews,
)
from gensigma_benchmarks.executive_cognition import seal_result, stable_digest


NOW = "2026-09-07T07:00:00Z"
CASE_REF = {"id": "case-1", "version": "1.0.0", "digest": "a" * 64}
RUBRIC = {
    "rubric_id": "executive-cognition-review",
    "rubric_version": "1.0.0",
    "dimensions": ["decision_framing", "uncertainty_treatment"],
    "scale": {"minimum": 1, "maximum": 5},
}


def manifest(run_id: str, arm_id: str) -> dict:
    return {
        "contract_version": "evaluation-run/0.1",
        "run_id": run_id,
        "run_version": "1.0.0",
        "run_attempt": 1,
        "case_ref": copy.deepcopy(CASE_REF),
        "arm_ref": {"id": arm_id, "version": "1.0.0", "digest": "b" * 64},
        "configuration_versions": [],
        "model_versions": [],
        "prompt_versions": [],
        "tool_versions": [],
        "metric_versions": [],
        "random_seed": 42,
        "started_at": NOW,
        "completed_at": NOW,
        "input_digest": "c" * 64,
    }


def output(run_id: str, suffix: str) -> dict:
    return seal_result(
        {
            "contract_version": "arm-output/0.1",
            "result_id": f"result-{suffix}",
            "result_version": "1.0.0",
            "run_id": run_id,
            "created_at": NOW,
            "recommendation": "gather_evidence",
            "rationale": f"Rationale {suffix}",
            "alternatives_considered": ["bid", "decline"],
            "assumptions": ["Deadline unchanged"],
            "uncertainties": [],
            "reversal_conditions": ["Partner commits"],
            "method_trace": [{
                "method_id": f"revealing-method-{suffix}",
                "method_version": "1.0.0",
                "role": "analysis",
                "material_contribution": "Produced a recommendation.",
            }],
            "evidence_refs": ["evidence-1"],
            "authority_status": "approval_required",
        }
    )


def bundle(seed: int = 17):
    return ReviewPacketBuilder(clock=lambda: NOW).build(
        case_ref=CASE_REF,
        run_manifests=[manifest("run-a", "llm-only"), manifest("run-b", "scorecard")],
        arm_outputs=[output("run-a", "a"), output("run-b", "b")],
        rubric=RUBRIC,
        randomization_seed=seed,
        case_material={"question": "Bid?"},
    )


def test_blinding_is_deterministic_and_reviewer_packet_leaks_no_arm_identity():
    first = bundle(17)
    second = bundle(17)
    assert first.reviewer_packet == second.reviewer_packet
    serialized = repr(first.reviewer_packet)
    for secret in ("run-a", "run-b", "llm-only", "scorecard", "revealing-method"):
        assert secret not in serialized
    assert [item["blind_result_id"] for item in first.reviewer_packet["candidates"]] == [
        "candidate-A", "candidate-B"
    ]
    assert set(first.reconciliation["mapping"]) == {"candidate-A", "candidate-B"}


def test_reconciliation_maps_independent_reviews_and_retains_disagreement():
    packet = bundle()
    responses = [
        ReviewResponse("review-1", "candidate-A", "reviewer-1", "1.0", "1.0.0", {"decision_framing": 5, "uncertainty_treatment": 4}, {}, NOW),
        ReviewResponse("review-2", "candidate-A", "reviewer-2", "1.0", "1.0.0", {"decision_framing": 3, "uncertainty_treatment": 4}, {"decision_framing": "Missing framing."}, NOW),
    ]
    reconciled = reconcile_reviews(responses, packet.reconciliation, RUBRIC)
    assert len(reconciled) == 2
    assert reconciled[0]["run_ref"] == reconciled[1]["run_ref"]

    metric = seal_result({
        "contract_version": "metric-result/0.1", "metric_result_id": "metric-1",
        "metric_id": "required-field-completeness", "metric_version": "1.0.0",
        "run_id": reconciled[0]["run_ref"]["id"], "metric_kind": "deterministic",
        "value": 1.0, "computed_at": NOW,
    })
    report = BenchmarkReporter(clock=lambda: NOW).build(
        case_refs=[CASE_REF],
        run_manifests=[manifest("run-a", "llm-only"), manifest("run-b", "scorecard")],
        metric_results=[metric],
        reconciled_reviews=reconciled,
        review_packet_refs=[{"id": packet.packet_metadata["packet_id"], "version": "1.0.0", "digest": stable_digest(packet.packet_metadata)}],
        artifact_refs=["artifacts/raw-results.json"],
        failure_examples=[{"case_id": "case-1", "run_id": "run-a", "failure": "unsupported claim"}],
    )
    disagreement = report.report["aggregate_human_review_table"]
    framing = next(row for row in disagreement if row["dimension"] == "decision_framing")
    assert framing["reviewer_ratings"] == [
        {"reviewer_id": "reviewer-1", "rating": 5},
        {"reviewer_id": "reviewer-2", "rating": 3},
    ]
    assert framing["range"] == 2
    assert framing["resolution_status"] == "unresolved"
    assert report.report["composite_score"] is None
    assert report.report["raw_export_refs"] == ["artifacts/raw-results.json"]
    assert report.raw_export["failure_examples"][0]["failure"] == "unsupported claim"


def test_reconciliation_rejects_tampering_unknown_labels_and_partial_ratings():
    packet = bundle()
    response = ReviewResponse("review-1", "candidate-A", "reviewer-1", "1.0", "1.0.0", {"decision_framing": 5, "uncertainty_treatment": 4}, {}, NOW)
    tampered = copy.deepcopy(packet.reconciliation)
    tampered["mapping"]["candidate-A"]["run_ref"]["id"] = "changed"
    with pytest.raises(ReviewConfigurationError, match="digest"):
        reconcile_reviews([response], tampered, RUBRIC)
    with pytest.raises(ReviewConfigurationError, match="every rubric dimension"):
        reconcile_reviews([
            ReviewResponse("review-2", "candidate-A", "reviewer-1", "1.0", "1.0.0", {"decision_framing": 5}, {}, NOW)
        ], packet.reconciliation, RUBRIC)
