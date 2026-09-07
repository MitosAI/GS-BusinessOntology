"""Deterministic and probabilistic scoring for cognition benchmark results."""

from __future__ import annotations

import copy
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence

from .executive_cognition import (
    CognitionContractRegistry,
    immutable_result_identity,
    seal_result,
    stable_digest,
)


DEFAULT_METRIC_CATALOG_PATH = Path(
    "benchmarks/executive-cognition/config/metric-definitions-v1.json"
)


@dataclass(frozen=True)
class ForecastObservation:
    """One binary probability and its realized outcome, retained without binning."""

    forecast_id: str
    probability: float
    outcome: int

    def __post_init__(self) -> None:
        if not self.forecast_id:
            raise ValueError("forecast_id must be non-empty")
        if (
            isinstance(self.probability, bool)
            or not math.isfinite(self.probability)
            or not 0.0 <= self.probability <= 1.0
        ):
            raise ValueError("probability must be between 0 and 1")
        if type(self.outcome) is not int or self.outcome not in (0, 1):
            raise ValueError("outcome must be binary: 0 or 1")

    def as_dict(self) -> dict[str, Any]:
        return {
            "forecast_id": self.forecast_id,
            "probability": self.probability,
            "outcome": self.outcome,
        }


@dataclass(frozen=True)
class HumanRubricHook:
    """Versioned handoff metadata; this type deliberately performs no scoring."""

    metric_id: str
    metric_version: str
    rubric_id: str
    rubric_version: str
    dimensions: tuple[str, ...]

    def __post_init__(self) -> None:
        values = (
            self.metric_id,
            self.metric_version,
            self.rubric_id,
            self.rubric_version,
            *self.dimensions,
        )
        if not self.dimensions or any(not value for value in values):
            raise ValueError("rubric identifiers, versions, and dimensions are required")

    def as_dict(self) -> dict[str, Any]:
        return {
            "metric_id": self.metric_id,
            "metric_version": self.metric_version,
            "metric_kind": "human_rubric",
            "automated": False,
            "rubric_id": self.rubric_id,
            "rubric_version": self.rubric_version,
            "dimensions": list(self.dimensions),
        }


class MetricCatalog:
    """Load explicit benchmark-local metric identities and configuration rules."""

    def __init__(self, path: str | Path = DEFAULT_METRIC_CATALOG_PATH) -> None:
        self.path = Path(path)
        self.document = json.loads(self.path.read_text(encoding="utf-8"))
        if self.document.get("catalog_version") != "cognition-metrics/1.0.0":
            raise ValueError("unsupported metric catalog_version")
        metrics = self.document.get("metrics")
        if not isinstance(metrics, list) or not metrics:
            raise ValueError("metric catalog must contain metrics")
        self._metrics: dict[str, Mapping[str, Any]] = {}
        for metric in metrics:
            metric_id = metric.get("metric_id")
            if not metric_id or not metric.get("metric_version"):
                raise ValueError("every metric requires metric_id and metric_version")
            if metric_id in self._metrics:
                raise ValueError(f"duplicate metric_id: {metric_id}")
            self._metrics[metric_id] = copy.deepcopy(metric)

    @property
    def digest(self) -> str:
        return stable_digest(self.document)

    def definition(self, metric_id: str) -> Mapping[str, Any]:
        try:
            return copy.deepcopy(self._metrics[metric_id])
        except KeyError as exc:
            raise KeyError(f"unknown metric_id: {metric_id}") from exc

    def version_ref(self, metric_id: str) -> dict[str, Any]:
        metric = self.definition(metric_id)
        return {
            "id": metric["metric_id"],
            "version": metric["metric_version"],
            "configuration_digest": self.digest,
        }

    def rubric_hooks(self) -> tuple[HumanRubricHook, ...]:
        hooks = []
        for metric in self._metrics.values():
            if metric["metric_kind"] == "human_rubric":
                hooks.append(
                    HumanRubricHook(
                        metric_id=metric["metric_id"],
                        metric_version=metric["metric_version"],
                        rubric_id=metric["rubric_id"],
                        rubric_version=metric["rubric_version"],
                        dimensions=tuple(metric["dimensions"]),
                    )
                )
        return tuple(hooks)


class CognitionScorer:
    """Create sealed MetricResult records from machine-verifiable inputs."""

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
        value: float | int | bool | str | None,
        details: Mapping[str, Any],
    ) -> dict[str, Any]:
        metric = self.catalog.definition(metric_id)
        payload = {
            "metric_id": metric_id,
            "metric_version": metric["metric_version"],
            "value": value,
            "details": copy.deepcopy(dict(details)),
        }
        result = {
            "contract_version": "metric-result/0.1",
            "metric_result_id": immutable_result_identity(run_id, payload),
            **payload,
            "run_id": run_id,
            "metric_kind": metric["metric_kind"],
            "computed_at": self.clock(),
        }
        sealed = seal_result(result)
        self.contracts.validate("MetricResult", sealed)
        return sealed

    def score_explicit_rules(
        self,
        run_id: str,
        metric_id: str,
        rules: Sequence[Mapping[str, Any]],
        output: Mapping[str, Any],
    ) -> dict[str, Any]:
        """Count violations only for explicit, mechanically evaluable output rules."""
        metric = self.catalog.definition(metric_id)
        if metric["metric_kind"] != "deterministic":
            raise ValueError("explicit rules require a deterministic metric")
        violations = []
        evaluated = []
        for rule in rules:
            rule_id = rule.get("rule_id")
            field = rule.get("output_field")
            operator = rule.get("operator")
            if not rule_id or not field or operator not in {"equals", "in", "not_in"}:
                raise ValueError("rules require rule_id, output_field, and a supported operator")
            expected = rule.get("expected")
            if operator in {"in", "not_in"} and not isinstance(expected, list):
                raise ValueError("in and not_in rules require an expected list")
            if field not in output:
                violated = True
                observed = None
            else:
                observed = output[field]
                if operator == "equals":
                    violated = observed != expected
                elif operator == "in":
                    violated = observed not in expected
                else:
                    violated = observed in expected
            evaluated.append(rule_id)
            if violated:
                violations.append(
                    {"rule_id": rule_id, "output_field": field, "observed": observed}
                )
        return self._result(
            run_id,
            metric_id,
            len(violations),
            {"evaluated_rule_ids": evaluated, "violations": violations},
        )

    def score_required_fields(
        self,
        run_id: str,
        output: Mapping[str, Any],
        required_fields: Sequence[str],
    ) -> dict[str, Any]:
        missing = sorted(
            field
            for field in required_fields
            if field not in output or output[field] in (None, "", [], {})
        )
        total = len(required_fields)
        value = 1.0 if total == 0 else (total - len(missing)) / total
        return self._result(
            run_id,
            "required-field-completeness",
            value,
            {"required_fields": sorted(required_fields), "missing_fields": missing},
        )

    def score_evidence_references(
        self,
        run_id: str,
        output: Mapping[str, Any],
        available_evidence_ids: Sequence[str],
        structured_claims: Sequence[Mapping[str, Any]] = (),
    ) -> dict[str, Any]:
        available = set(available_evidence_ids)
        invalid_refs = sorted(set(output.get("evidence_refs", ())) - available)
        unsupported_claims = []
        for claim in structured_claims:
            refs = set(claim.get("evidence_refs", ()))
            if not refs or not refs.issubset(available):
                unsupported_claims.append(claim.get("claim_id", "unknown"))
        violations = len(invalid_refs) + len(unsupported_claims)
        return self._result(
            run_id,
            "evidence-reference-validity",
            violations,
            {
                "invalid_evidence_refs": invalid_refs,
                "unsupported_structured_claim_ids": sorted(unsupported_claims),
                "unstructured_rationale_scored": False,
            },
        )

    def score_operational_metadata(
        self,
        run_id: str,
        *,
        latency_ms: float,
        cost_usd: float | None,
    ) -> dict[str, Any]:
        if (
            isinstance(latency_ms, bool)
            or not math.isfinite(latency_ms)
            or latency_ms < 0
        ):
            raise ValueError("latency_ms must be non-negative")
        if cost_usd is not None and (
            isinstance(cost_usd, bool)
            or not math.isfinite(cost_usd)
            or cost_usd < 0
        ):
            raise ValueError("cost_usd must be non-negative or null")
        return self._result(
            run_id,
            "operational-metadata",
            latency_ms,
            {"latency_ms": latency_ms, "cost_usd": cost_usd},
        )

    def score_binary_forecasts(
        self,
        run_id: str,
        observations: Sequence[ForecastObservation],
    ) -> dict[str, Any]:
        if not observations:
            raise ValueError("at least one forecast observation is required")
        forecast_ids = [observation.forecast_id for observation in observations]
        if len(forecast_ids) != len(set(forecast_ids)):
            raise ValueError("forecast_id values must be unique within a metric result")
        raw_pairs = [observation.as_dict() for observation in observations]
        components = [
            (observation.probability - observation.outcome) ** 2
            for observation in observations
        ]
        return self._result(
            run_id,
            "binary-brier-score",
            sum(components) / len(components),
            {"observations": raw_pairs, "squared_errors": components},
        )

    def calibration_summary(
        self,
        run_id: str,
        observations: Sequence[ForecastObservation],
    ) -> dict[str, Any]:
        metric = self.catalog.definition("binary-calibration-summary")
        minimum = metric["minimum_sample_size"]
        if len(observations) < minimum:
            return self._result(
                run_id,
                "binary-calibration-summary",
                None,
                {
                    "status": "insufficient_sample",
                    "sample_size": len(observations),
                    "minimum_sample_size": minimum,
                    "bins": [],
                },
            )
        return self._result(
            run_id,
            "binary-calibration-summary",
            None,
            {
                "status": "eligible_for_configured_analysis",
                "sample_size": len(observations),
                "minimum_sample_size": minimum,
                "bins": [],
                "note": "Binning is an explicit reporting step, not automatic scoring.",
            },
        )
