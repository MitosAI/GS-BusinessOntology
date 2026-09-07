from __future__ import annotations

from typing import Any, Mapping

from gensigma_benchmarks.cognition_arms import (
    EvaluationRunner,
    LLMOnlyBaseline,
    StaticScorecardBaseline,
)
from gensigma_benchmarks.executive_cognition import (
    CognitionContractRegistry,
    FrozenCaseLoader,
)


FIXTURE = "benchmarks/executive-cognition/fixtures/bid-no-bid-valid.json"
SCORECARD = "benchmarks/executive-cognition/config/bid-no-bid-scorecard-v1.json"
NOW = "2026-09-07T06:00:00Z"


class ScriptedModel:
    model_id = "scripted-model"
    model_version = "test-1.0.0"

    def __init__(self) -> None:
        self.prompts: list[str] = []

    def complete(self, prompt: str) -> Mapping[str, Any]:
        self.prompts.append(prompt)
        return {
            "recommendation": "gather_evidence",
            "rationale": "Partner availability is material and unresolved.",
            "alternatives_considered": ["bid", "decline"],
            "assumptions": ["The deadline remains unchanged"],
            "uncertainties": [],
            "reversal_conditions": ["A qualified partner commits"],
            "evidence_refs": ["evidence-solicitation-001"],
            "authority_status": "approval_required",
        }


def arm_input():
    return FrozenCaseLoader().load(FIXTURE).arm_input


def llm_arm(model: ScriptedModel) -> LLMOnlyBaseline:
    return LLMOnlyBaseline(
        model,
        prompt_id="bid-no-bid-llm-only",
        prompt_version="1.0.0",
        prompt_template="Decide only from this frozen case: {decision_case}",
    )


def test_both_baselines_run_on_identical_frozen_input() -> None:
    frozen = arm_input()
    model = ScriptedModel()
    runner = EvaluationRunner(clock=lambda: NOW)

    llm = runner.run(llm_arm(model), frozen, run_id="run-llm-001", run_attempt=1)
    scorecard = runner.run(
        StaticScorecardBaseline(SCORECARD),
        frozen,
        run_id="run-scorecard-001",
        run_attempt=1,
    )

    assert llm.run_manifest["case_ref"] == scorecard.run_manifest["case_ref"]
    assert llm.run_manifest["input_digest"] == scorecard.run_manifest["input_digest"]
    assert llm.arm_output["recommendation"] == "gather_evidence"
    assert scorecard.arm_output["recommendation"] == "gather_evidence"
    assert "Weighted score 0.640" in scorecard.arm_output["rationale"]


def test_llm_receives_no_held_out_outcome_and_versions_are_recorded() -> None:
    model = ScriptedModel()
    execution = EvaluationRunner(clock=lambda: NOW).run(
        llm_arm(model), arm_input(), run_id="run-llm-001", run_attempt=1
    )

    assert "held_out_outcome" not in model.prompts[0]
    assert "award_result" not in model.prompts[0]
    assert execution.run_manifest["model_versions"][0]["id"] == "scripted-model"
    assert execution.run_manifest["prompt_versions"][0]["version"] == "1.0.0"
    assert execution.run_manifest["configuration_versions"] == []
    assert execution.run_manifest["tool_versions"] == []


def test_scorecard_criteria_and_configuration_are_explicitly_versioned() -> None:
    arm = StaticScorecardBaseline(SCORECARD)
    metadata = arm.metadata()

    assert metadata["configuration_versions"][0]["id"] == (
        "bid-no-bid-static-scorecard"
    )
    assert metadata["configuration_versions"][0]["version"] == "1.0.0"
    assert metadata["configuration_versions"][0]["configuration_digest"]
    assert len(arm.configuration["criteria"]) == 3


def test_repeated_llm_runs_create_distinct_immutable_results() -> None:
    frozen = arm_input()
    model = ScriptedModel()
    runner = EvaluationRunner(clock=lambda: NOW)

    first = runner.run(llm_arm(model), frozen, run_id="run-llm-001", run_attempt=1)
    second = runner.run(llm_arm(model), frozen, run_id="run-llm-002", run_attempt=2)

    assert first.arm_output["result_id"] != second.arm_output["result_id"]
    assert first.arm_output["result_digest"] != second.arm_output["result_digest"]
    assert first.run_manifest["run_id"] != second.run_manifest["run_id"]


def test_baseline_outputs_and_manifests_conform_to_common_contracts() -> None:
    contracts = CognitionContractRegistry()
    execution = EvaluationRunner(contracts, clock=lambda: NOW).run(
        StaticScorecardBaseline(SCORECARD),
        arm_input(),
        run_id="run-scorecard-001",
        run_attempt=1,
    )

    contracts.validate("EvaluationRun", execution.run_manifest)
    contracts.validate("ArmOutput", execution.arm_output)
