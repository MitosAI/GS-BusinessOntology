"""Benchmark-local contracts for reproducible executive-cognition evaluation."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import ValidationError
from referencing import Registry, Resource


DEFAULT_CONTRACT_PATH = Path(
    "benchmarks/executive-cognition/contracts.schema.json"
)

CONTRACT_DEFINITIONS = {
    "DecisionCase": "decisionCase",
    "DecisionTimeEvidenceRef": "evidenceRef",
    "HeldOutOutcome": "heldOutOutcome",
    "EvaluationArm": "evaluationArm",
    "EvaluationRun": "evaluationRun",
    "ArmOutput": "armOutput",
    "MetricResult": "metricResult",
    "HumanReviewPacket": "humanReviewPacket",
    "BenchmarkReport": "benchmarkReport",
}

DIGESTED_CONTRACTS = frozenset(
    {"ArmOutput", "MetricResult", "BenchmarkReport"}
)


class BenchmarkContractViolation(ValueError):
    """Raised when a benchmark artifact violates its local evaluation contract."""


def canonical_json(value: Any) -> str:
    """Serialize JSON data stably using the convention established by PR #24."""
    return json.dumps(
        value,
        allow_nan=False,
        ensure_ascii=True,
        separators=(",", ":"),
        sort_keys=True,
    )


def stable_digest(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def result_digest(value: Mapping[str, Any]) -> str:
    """Digest a result without its self-describing ``result_digest`` field."""
    unsigned = dict(value)
    unsigned.pop("result_digest", None)
    return stable_digest(unsigned)


def seal_result(value: Mapping[str, Any]) -> dict[str, Any]:
    sealed = copy.deepcopy(dict(value))
    sealed["result_digest"] = result_digest(sealed)
    return sealed


def immutable_result_identity(run_id: str, value: Mapping[str, Any]) -> str:
    """Bind an immutable result identity to a distinct evaluation run."""
    if not run_id:
        raise ValueError("run_id must be non-empty")
    return stable_digest({"run_id": run_id, "result_digest": result_digest(value)})


def _freeze(value: Any) -> Any:
    if isinstance(value, dict):
        return MappingProxyType({key: _freeze(item) for key, item in value.items()})
    if isinstance(value, list):
        return tuple(_freeze(item) for item in value)
    return value


@dataclass(frozen=True)
class ArmInput:
    """The normal evaluation-arm input surface; outcomes are absent by construction."""

    case_id: str
    case_version: str
    decision_class: str
    question: str
    as_of: str
    decision_input: Mapping[str, Any]
    evidence: tuple[Mapping[str, Any], ...]
    case_digest: str


class CognitionContractRegistry:
    """Load and deterministically validate the Issue #11 contract bundle."""

    def __init__(self, contract_path: str | Path = DEFAULT_CONTRACT_PATH) -> None:
        self.path = Path(contract_path)
        if not self.path.exists():
            raise FileNotFoundError(f"Cognition benchmark contract not found: {self.path}")
        self.schema = json.loads(self.path.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(self.schema)
        self.schema_id = self.schema["$id"]
        self.registry = Registry().with_resource(
            self.schema_id, Resource.from_contents(self.schema)
        )

    def validate(self, contract_name: str, value: Mapping[str, Any]) -> None:
        try:
            definition = CONTRACT_DEFINITIONS[contract_name]
        except KeyError as exc:
            known = ", ".join(CONTRACT_DEFINITIONS)
            raise KeyError(
                f"Unknown cognition benchmark contract {contract_name!r}; expected: {known}"
            ) from exc

        validator = Draft202012Validator(
            {
                "$schema": "https://json-schema.org/draft/2020-12/schema",
                "$ref": f"{self.schema_id}#/$defs/{definition}",
            },
            registry=self.registry,
            format_checker=FormatChecker(),
        )
        errors = sorted(
            validator.iter_errors(value),
            key=lambda error: tuple(str(part) for part in error.absolute_path),
        )
        if errors:
            raise BenchmarkContractViolation(
                self._format_error(contract_name, errors[0])
            )

        if contract_name == "DecisionCase":
            self._validate_decision_case_references(value)
        if contract_name in DIGESTED_CONTRACTS:
            self._validate_result_digest(contract_name, value)

    @staticmethod
    def _format_error(contract_name: str, error: ValidationError) -> str:
        location = ".".join(str(part) for part in error.absolute_path) or "<root>"
        return f"{contract_name} violation at {location}: {error.message}"

    @staticmethod
    def _validate_decision_case_references(value: Mapping[str, Any]) -> None:
        forbidden_keys = {"held_out_outcome", "realized_outcome", "ground_truth"}

        def find_forbidden(item: Any, path: tuple[str, ...] = ()) -> str | None:
            if isinstance(item, Mapping):
                for key, nested in item.items():
                    if key in forbidden_keys:
                        return ".".join((*path, key))
                    if found := find_forbidden(nested, (*path, key)):
                        return found
            elif isinstance(item, list):
                for index, nested in enumerate(item):
                    if found := find_forbidden(nested, (*path, str(index))):
                        return found
            return None

        if forbidden_path := find_forbidden(value["decision_input"]):
            raise BenchmarkContractViolation(
                "DecisionCase violation at decision_input."
                f"{forbidden_path}: held-out outcome data is forbidden"
            )

        evidence_ids = [item["evidence_id"] for item in value["evidence"]]
        if len(evidence_ids) != len(set(evidence_ids)):
            raise BenchmarkContractViolation(
                "DecisionCase violation at evidence: duplicate evidence_id"
            )

        available = set(evidence_ids)
        referenced = set(value["decision_input"]["evidence_refs"])
        for uncertainty in value["decision_input"]["uncertainties"]:
            referenced.update(uncertainty["evidence_refs"])
        missing = sorted(referenced - available)
        if missing:
            raise BenchmarkContractViolation(
                "DecisionCase violation at decision_input.evidence_refs: "
                f"unknown evidence references: {missing}"
            )

    @staticmethod
    def _validate_result_digest(
        contract_name: str, value: Mapping[str, Any]
    ) -> None:
        expected = result_digest(value)
        if value["result_digest"] != expected:
            raise BenchmarkContractViolation(
                f"{contract_name} violation at result_digest: expected {expected}"
            )

    def arm_input(self, decision_case: Mapping[str, Any]) -> ArmInput:
        self.validate("DecisionCase", decision_case)
        return ArmInput(
            case_id=decision_case["case_id"],
            case_version=decision_case["case_version"],
            decision_class=decision_case["decision_class"],
            question=decision_case["question"],
            as_of=decision_case["as_of"],
            decision_input=_freeze(copy.deepcopy(decision_case["decision_input"])),
            evidence=tuple(_freeze(copy.deepcopy(item)) for item in decision_case["evidence"]),
            case_digest=stable_digest(decision_case),
        )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate one executive-cognition benchmark artifact."
    )
    parser.add_argument("contract", choices=tuple(CONTRACT_DEFINITIONS))
    parser.add_argument("artifact", type=Path)
    parser.add_argument("--contracts", type=Path, default=DEFAULT_CONTRACT_PATH)
    args = parser.parse_args()

    value = json.loads(args.artifact.read_text(encoding="utf-8"))
    CognitionContractRegistry(args.contracts).validate(args.contract, value)
    print(stable_digest(value))


if __name__ == "__main__":
    main()
