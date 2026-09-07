"""Executable baseline arms for the executive-cognition benchmark."""

from __future__ import annotations

import copy
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Mapping, Protocol

from .executive_cognition import (
    ArmInput,
    CognitionContractRegistry,
    canonical_json,
    immutable_result_identity,
    seal_result,
    stable_digest,
)


class ModelAdapter(Protocol):
    model_id: str
    model_version: str

    def complete(self, prompt: str) -> Mapping[str, Any]: ...


@dataclass(frozen=True)
class ArmDecision:
    recommendation: str
    rationale: str
    alternatives_considered: tuple[str, ...]
    assumptions: tuple[str, ...]
    uncertainties: tuple[Mapping[str, Any], ...]
    reversal_conditions: tuple[str, ...]
    method_trace: tuple[Mapping[str, Any], ...]
    evidence_refs: tuple[str, ...]
    authority_status: str


class BenchmarkArm(Protocol):
    def metadata(self) -> Mapping[str, Any]: ...

    def evaluate(self, arm_input: ArmInput) -> ArmDecision: ...


@dataclass(frozen=True)
class ArmExecution:
    run_manifest: Mapping[str, Any]
    arm_output: Mapping[str, Any]


def _thaw(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {key: _thaw(item) for key, item in value.items()}
    if isinstance(value, tuple):
        return [_thaw(item) for item in value]
    return value


def arm_input_document(arm_input: ArmInput) -> dict[str, Any]:
    return {
        "case_id": arm_input.case_id,
        "case_version": arm_input.case_version,
        "decision_class": arm_input.decision_class,
        "question": arm_input.question,
        "as_of": arm_input.as_of,
        "decision_input": _thaw(arm_input.decision_input),
        "evidence": _thaw(arm_input.evidence),
        "case_digest": arm_input.case_digest,
    }


class EvaluationRunner:
    def __init__(
        self,
        contracts: CognitionContractRegistry | None = None,
        clock: Callable[[], str] | None = None,
    ) -> None:
        self.contracts = contracts or CognitionContractRegistry()
        self.clock = clock or (lambda: "1970-01-01T00:00:00Z")

    def run(
        self,
        arm: BenchmarkArm,
        arm_input: ArmInput,
        *,
        run_id: str,
        run_attempt: int,
        random_seed: int | None = None,
        metric_versions: tuple[Mapping[str, Any], ...] = (),
    ) -> ArmExecution:
        metadata = copy.deepcopy(dict(arm.metadata()))
        self.contracts.validate("EvaluationArm", metadata)
        started_at = self.clock()
        decision = arm.evaluate(arm_input)
        created_at = self.clock()
        decision_payload = {
            "recommendation": decision.recommendation,
            "rationale": decision.rationale,
            "alternatives_considered": list(decision.alternatives_considered),
            "assumptions": list(decision.assumptions),
            "uncertainties": _thaw(decision.uncertainties),
            "reversal_conditions": list(decision.reversal_conditions),
            "method_trace": _thaw(decision.method_trace),
            "evidence_refs": list(decision.evidence_refs),
            "authority_status": decision.authority_status,
        }
        output = {
            "contract_version": "arm-output/0.1",
            "result_id": immutable_result_identity(run_id, decision_payload),
            "result_version": "1.0.0",
            "run_id": run_id,
            "created_at": created_at,
            **decision_payload,
        }
        sealed_output = seal_result(output)
        self.contracts.validate("ArmOutput", sealed_output)

        manifest = {
            "contract_version": "evaluation-run/0.1",
            "run_id": run_id,
            "run_version": "1.0.0",
            "run_attempt": run_attempt,
            "case_ref": {
                "id": arm_input.case_id,
                "version": arm_input.case_version,
                "digest": arm_input.case_digest,
            },
            "arm_ref": {
                "id": metadata["arm_id"],
                "version": metadata["arm_version"],
                "digest": stable_digest(metadata),
            },
            "configuration_versions": metadata["configuration_versions"],
            "model_versions": metadata["model_versions"],
            "prompt_versions": metadata["prompt_versions"],
            "tool_versions": metadata["tool_versions"],
            "metric_versions": _thaw(metric_versions),
            "random_seed": random_seed,
            "started_at": started_at,
            "completed_at": self.clock(),
            "input_digest": stable_digest(arm_input_document(arm_input)),
        }
        self.contracts.validate("EvaluationRun", manifest)
        return ArmExecution(run_manifest=manifest, arm_output=sealed_output)


class LLMOnlyBaseline:
    """A provider-neutral benchmark baseline with no tools or formal modules."""

    def __init__(
        self,
        model: ModelAdapter,
        *,
        prompt_id: str,
        prompt_version: str,
        prompt_template: str,
    ) -> None:
        self.model = model
        self.prompt_id = prompt_id
        self.prompt_version = prompt_version
        self.prompt_template = prompt_template

    def metadata(self) -> Mapping[str, Any]:
        return {
            "contract_version": "evaluation-arm/0.1",
            "arm_id": "llm-only-baseline",
            "arm_version": "1.0.0",
            "arm_type": "llm_only",
            "configuration_versions": [],
            "model_versions": [
                {"id": self.model.model_id, "version": self.model.model_version}
            ],
            "prompt_versions": [
                {
                    "id": self.prompt_id,
                    "version": self.prompt_version,
                    "configuration_digest": stable_digest(self.prompt_template),
                }
            ],
            "tool_versions": [],
        }

    def evaluate(self, arm_input: ArmInput) -> ArmDecision:
        prompt = self.prompt_template.format(
            decision_case=canonical_json(arm_input_document(arm_input))
        )
        response = self.model.complete(prompt)
        return ArmDecision(
            recommendation=response["recommendation"],
            rationale=response["rationale"],
            alternatives_considered=tuple(response.get("alternatives_considered", ())),
            assumptions=tuple(response.get("assumptions", ())),
            uncertainties=tuple(response.get("uncertainties", ())),
            reversal_conditions=tuple(response.get("reversal_conditions", ())),
            method_trace=(
                {
                    "method_id": self.model.model_id,
                    "method_version": self.model.model_version,
                    "role": "synthesis",
                    "material_contribution": "Produced the LLM-only baseline recommendation.",
                },
            ),
            evidence_refs=tuple(response.get("evidence_refs", ())),
            authority_status=response.get("authority_status", "authority_unknown"),
        )


class StaticScorecardBaseline:
    """Explicit weighted-scorecard benchmark baseline; not production decision logic."""

    def __init__(self, configuration_path: str | Path) -> None:
        self.path = Path(configuration_path)
        self.configuration = json.loads(self.path.read_text(encoding="utf-8"))

    def metadata(self) -> Mapping[str, Any]:
        return {
            "contract_version": "evaluation-arm/0.1",
            "arm_id": "static-scorecard-baseline",
            "arm_version": "1.0.0",
            "arm_type": "scorecard",
            "configuration_versions": [
                {
                    "id": self.configuration["configuration_id"],
                    "version": self.configuration["configuration_version"],
                    "configuration_digest": stable_digest(self.configuration),
                }
            ],
            "model_versions": [],
            "prompt_versions": [],
            "tool_versions": [
                {"id": "gensigma-scorecard", "version": "1.0.0"}
            ],
        }

    @staticmethod
    def _lookup(document: Any, path: str) -> Any:
        value = document
        for part in path.split("."):
            value = value[int(part)] if isinstance(value, list) else value[part]
        return value

    def evaluate(self, arm_input: ArmInput) -> ArmDecision:
        document = arm_input_document(arm_input)
        weighted_total = 0.0
        weight_total = 0.0
        contributions: list[str] = []
        for criterion in self.configuration["criteria"]:
            raw = self._lookup(document, criterion["path"])
            score = criterion["values"][str(raw).lower()]
            weight = criterion["weight"]
            weighted_total += score * weight
            weight_total += weight
            contributions.append(f"{criterion['id']}={score:g} x {weight:g}")
        score = weighted_total / weight_total

        recommendation = "decline"
        for threshold in sorted(
            self.configuration["thresholds"],
            key=lambda item: item["minimum"],
            reverse=True,
        ):
            if score >= threshold["minimum"]:
                recommendation = threshold["recommendation"]
                break

        policy = document["decision_input"]["context"].get("policy_authority", {})
        authority_status = (
            "approval_required"
            if policy.get("required_approvals")
            else "authority_unknown"
        )
        evidence_refs = tuple(document["decision_input"]["evidence_refs"])
        return ArmDecision(
            recommendation=recommendation,
            rationale=f"Weighted score {score:.3f}: " + "; ".join(contributions),
            alternatives_considered=tuple(
                item["recommendation"] for item in self.configuration["thresholds"]
            ),
            assumptions=("Configured criteria are compensatory and complete.",),
            uncertainties=(),
            reversal_conditions=("A criterion change crosses a configured threshold.",),
            method_trace=(
                {
                    "method_id": self.configuration["configuration_id"],
                    "method_version": self.configuration["configuration_version"],
                    "role": "analysis",
                    "material_contribution": "Computed the explicit weighted baseline score.",
                },
            ),
            evidence_refs=evidence_refs,
            authority_status=authority_status,
        )
