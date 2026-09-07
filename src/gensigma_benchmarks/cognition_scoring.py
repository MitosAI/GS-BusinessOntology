"""Explicit scoring utilities for the executive-cognition benchmark."""

from __future__ import annotations

import copy
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence

from .executive_cognition import (
    CognitionContractRegistry,
    seal_result,
    stable_digest,
)


DEFAULT_METRIC_CATALOG_PATH = Path(
    "benchmarks/executive-cognition/config/cognition-metrics-v1.json"
)


class ScoringConfigurationError(ValueError):
    """Raised when benchmark-local scoring configuration is invalid."""


@dataclass(frozen=True)
class MetricDefinition:
    metric_id: str
    version: str
    kind: str
    description: str

    def component_version(self) -> dict[str, str]:
        return {"id": self.metric_id, "version": self.version}


@dataclass(frozen=True)
class ForecastObservation:
    forecast_id: str
    probability: float
    outcome: int

    def __post_init__(self) -> None:
        if not self.forecast_id:
            raise ValueError("forecast_id must be non-empty")
        if isinstance(self.probability, bool) or not 0 <= self.probability <= 1:
            raise ValueError("probability must be between 0 and 1")
        if isinstance(self.outcome, bool) or self.outcome not in (0, 1):
            raise ValueError("outcome must be binary: 0 or 1")

    def as_dict(self) -> dict[str, Any]:
        return {
            "forecast_id": self.forecast_id,
            "probability": self.probability,
            "outcome": self.outcome,
            "squared_error": (self.probability - self.outcome) ** 2,
        }


class MetricCatalog:
    """Load explicit, versioned benchmark metric definitions."""

    _KINDS = {"deterministic", "probabilistic", "human_rubric", "operational"}

    def __init__(self, path: str | Path = DEFAULT_METRIC_CATALOG_PATH) -> None:
        self.path = Path(path)
        raw = json.loads(self.path.read_text(encoding="utf-8"))
        self.catalog_id = raw["catalog_id"]
        self.catalog_version = raw["catalog_version"]
        self.calibration_minimum_sample_size = raw["calibration"][
            "minimum_sample_size"
        ]
        if self.calibration_minimum_sample_size < 2:
            raise ScoringConfigurationError(
                "calibration.minimum_sample_size must be at least 2"
            )

        definitions = [MetricDefinition(**item) for item in raw["metrics"]]
        if len({item.metric_id for item in definitions}) != len(definitions):
            raise ScoringConfigurationError("metric ids must be unique")
        invalid_kinds = sorted({item.kind for item in definitions} - self._KINDS)
        if invalid_kinds:
            raise ScoringConfigurationError(
                f"unsupported metric kinds: {invalid_kinds}"
            )
        self._definitions = {item.metric_id: item for item in definitions}

    def get(self, metric_id: str) -> MetricDefinition:
        try:
            return self._definitions[metric_id]
        except KeyError as exc:
            raise ScoringConfigurationError(f"unknown metric: {metric_id}") from exc

    def component_versions(self) -> tuple[dict[str, str], ...]:
        return tuple(
            item.component_version()
            for item in sorted(
                self._definitions.values(), key=lambda item: item.metric_id
            )
        )


def brier_score(observations: Sequence[ForecastObservation]) -> float:
    """Return the mean quadratic loss for binary probability forecasts."""
    if not observations:
        raise ValueError("at least one forecast observation is required")
    return sum((item.probability - item.outcome) ** 2 for item in observations) / len(
        observations
    )


def calibration_summary(
    observations: Sequence[ForecastObservation],
    *,
    minimum_sample_size: int,
    bin_edges: Sequence[float] | None = None,
) -> dict[str, Any]:
    """Bin forecasts only when explicitly configured and sufficiently sampled."""
    if bin_edges is None:
        return {
            "status": "not_requested",
            "sample_size": len(observations),
            "minimum_sample_size": minimum_sample_size,
        }
    if len(observations) < minimum_sample_size:
        return {
            "status": "insufficient_sample",
            "sample_size": len(observations),
            "minimum_sample_size": minimum_sample_size,
        }
    edges = tuple(float(edge) for edge in bin_edges)
    if len(edges) < 2 or edges[0] != 0 or edges[-1] != 1:
        raise ValueError("bin_edges must begin at 0 and end at 1")
    if any(left >= right for left, right in zip(edges, edges[1:])):
        raise ValueError("bin_edges must be strictly increasing")

    bins: list[dict[str, Any]] = []
    for index, (lower, upper) in enumerate(zip(edges, edges[1:])):
        members = [
            item
            for item in observations
            if lower <= item.probability < upper
            or (index == len(edges) - 2 and item.probability == upper)
        ]
        bins.append(
            {
                "lower": lower,
                "upper": upper,
                "count": len(members),
                "mean_probability": (
                    sum(item.probability for item in members) / len(members)
                    if members
                    else None
                ),
                "event_rate": (
                    sum(item.outcome for item in members) / len(members)
                    if members
                    else None
                ),
            }
        )
    return {
        "status": "computed",
        "sample_size": len(observations),
        "minimum_sample_size": minimum_sample_size,
        "bins": bins,
    }


def hard_constraint_violations(
    decision_case: Mapping[str, Any],
    arm_output: Mapping[str, Any],
    fixture_rules: Mapping[str, Any],
) -> list[str]:
    constraints = {
        item["rule_id"]: item["satisfied"]
        for item in decision_case["decision_input"]["context"]
        .get("policy_authority", {})
        .get("hard_constraints", [])
    }
    recommendation = arm_output["recommendation"]
    violations: list[str] = []
    for rule in fixture_rules.get("hard_constraint_rules", []):
        rule_id = rule["rule_id"]
        if rule_id not in constraints:
            raise ScoringConfigurationError(
                f"fixture rule references unknown hard constraint: {rule_id}"
            )
        if (
            not constraints[rule_id]
            and recommendation in rule["prohibited_recommendations_when_unsatisfied"]
        ):
            violations.append(rule_id)
    return violations


def policy_authority_violations(
    arm_output: Mapping[str, Any], fixture_rules: Mapping[str, Any]
) -> list[str]:
    recommendation = arm_output["recommendation"]
    allowed = fixture_rules.get("allowed_authority_statuses_by_recommendation", {}).get(
        recommendation
    )
    if allowed is None:
        return []
    if arm_output["authority_status"] in allowed:
        return []
    return [
        f"{recommendation}:{arm_output['authority_status']} not in {sorted(allowed)}"
    ]


def trace_completeness(
    arm_output: Mapping[str, Any], fixture_rules: Mapping[str, Any]
) -> tuple[float, list[str]]:
    required = tuple(fixture_rules.get("required_trace_fields", ()))
    if not required:
        raise ScoringConfigurationError("required_trace_fields must be non-empty")
    missing = [field for field in required if not arm_output.get(field)]
    return (len(required) - len(missing)) / len(required), missing


def unsupported_evidence_references(
    decision_case: Mapping[str, Any], arm_output: Mapping[str, Any]
) -> list[str]:
    known = {item["evidence_id"] for item in decision_case["evidence"]}
    referenced = set(arm_output.get("evidence_refs", ()))
    for uncertainty in arm_output.get("uncertainties", ()):
        referenced.update(uncertainty.get("evidence_refs", ()))
        referenced.update(uncertainty.get("probability_basis_refs", ()))
    return sorted(referenced - known)


class CognitionScorer:
    """Generate sealed metric results without collapsing metric dimensions."""

    def __init__(
        self,
        catalog: MetricCatalog | None = None,
        contracts: CognitionContractRegistry | None = None,
        clock: Callable[[], str] | None = None,
    ) -> None:
        self.catalog = catalog or MetricCatalog()
        self.contracts = contracts or CognitionContractRegistry()
        self.clock = clock or (lambda: "1970-01-01T00:00:00Z")

    def _result(
        self,
        run_id: str,
        metric_id: str,
        value: int | float | bool | str | None,
        details: Mapping[str, Any],
    ) -> dict[str, Any]:
        definition = self.catalog.get(metric_id)
        identity = stable_digest(
            {
                "run_id": run_id,
                "metric_id": metric_id,
                "metric_version": definition.version,
                "value": value,
                "details": details,
            }
        )
        result = seal_result(
            {
                "contract_version": "metric-result/0.1",
                "metric_result_id": identity,
                "metric_id": metric_id,
                "metric_version": definition.version,
                "run_id": run_id,
                "metric_kind": definition.kind,
                "value": value,
                "details": copy.deepcopy(dict(details)),
                "computed_at": self.clock(),
            }
        )
        self.contracts.validate("MetricResult", result)
        return result

    def score(
        self,
        *,
        decision_case: Mapping[str, Any],
        run_manifest: Mapping[str, Any],
        arm_output: Mapping[str, Any],
        fixture_rules: Mapping[str, Any],
        operational_metadata: Mapping[str, float | int] | None = None,
        forecasts: Sequence[ForecastObservation] = (),
        calibration_bin_edges: Sequence[float] | None = None,
    ) -> tuple[dict[str, Any], ...]:
        self.contracts.validate("DecisionCase", decision_case)
        self.contracts.validate("EvaluationRun", run_manifest)
        self.contracts.validate("ArmOutput", arm_output)
        if arm_output["run_id"] != run_manifest["run_id"]:
            raise ValueError("arm output and run manifest must reference the same run")
        if decision_case["case_id"] != run_manifest["case_ref"]["id"]:
            raise ValueError(
                "decision case and run manifest must reference the same case"
            )
        rule_case = (fixture_rules.get("case_id"), fixture_rules.get("case_version"))
        decision_case_ref = (decision_case["case_id"], decision_case["case_version"])
        if rule_case != decision_case_ref:
            raise ScoringConfigurationError(
                "fixture rules and decision case must reference the same case version"
            )

        run_id = run_manifest["run_id"]
        rule_ref = {
            "case_id": fixture_rules["case_id"],
            "case_version": fixture_rules["case_version"],
            "rules_version": fixture_rules["rules_version"],
            "digest": stable_digest(fixture_rules),
        }
        hard = hard_constraint_violations(decision_case, arm_output, fixture_rules)
        authority = policy_authority_violations(arm_output, fixture_rules)
        completeness, missing = trace_completeness(arm_output, fixture_rules)
        unsupported = unsupported_evidence_references(decision_case, arm_output)
        results = [
            self._result(
                run_id,
                "hard-constraint-violations",
                len(hard),
                {"violations": hard, "fixture_rules_ref": rule_ref},
            ),
            self._result(
                run_id,
                "policy-authority-violations",
                len(authority),
                {"violations": authority, "fixture_rules_ref": rule_ref},
            ),
            self._result(
                run_id,
                "required-trace-completeness",
                completeness,
                {"missing_fields": missing, "fixture_rules_ref": rule_ref},
            ),
            self._result(
                run_id,
                "unsupported-evidence-references",
                len(unsupported),
                {
                    "unsupported_references": unsupported,
                    "scope": "structured evidence references only",
                    "fixture_rules_ref": rule_ref,
                },
            ),
        ]

        for key, metric_id in (
            ("latency_ms", "latency-ms"),
            ("cost_usd", "cost-usd"),
            ("human_review_ms", "human-review-ms"),
            ("retry_count", "retry-count"),
        ):
            if operational_metadata is None or key not in operational_metadata:
                continue
            value = operational_metadata[key]
            if isinstance(value, bool) or value < 0:
                raise ValueError(f"{key} must be a non-negative number")
            results.append(
                self._result(run_id, metric_id, value, {"source_field": key})
            )

        if forecasts:
            raw = [item.as_dict() for item in forecasts]
            results.append(
                self._result(
                    run_id,
                    "binary-brier-score",
                    brier_score(forecasts),
                    {
                        "observations": raw,
                        "calibration": calibration_summary(
                            forecasts,
                            minimum_sample_size=(
                                self.catalog.calibration_minimum_sample_size
                            ),
                            bin_edges=calibration_bin_edges,
                        ),
                    },
                )
            )

        rubric = self.catalog.get("executive-quality-rubric")
        results.append(
            self._result(
                run_id,
                rubric.metric_id,
                None,
                {
                    "status": "awaiting_human_review",
                    "rubric_version": fixture_rules["human_rubric_version"],
                    "dimensions": list(fixture_rules["human_rubric_dimensions"]),
                    "fixture_rules_ref": rule_ref,
                },
            )
        )
        return tuple(results)
