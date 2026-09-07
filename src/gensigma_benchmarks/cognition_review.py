"""Blinded human review and dimension-preserving benchmark reporting."""

from __future__ import annotations

import copy
import math
import random
from dataclasses import dataclass
from statistics import fmean
from typing import Any, Callable, Mapping, Sequence

from .executive_cognition import CognitionContractRegistry, seal_result, stable_digest


class ReviewConfigurationError(ValueError):
    """Raised when review artifacts cannot preserve benchmark invariants."""


@dataclass(frozen=True)
class ReviewPacketBundle:
    """Reviewer-facing material plus the separately held reconciliation map."""

    packet_metadata: Mapping[str, Any]
    reviewer_packet: Mapping[str, Any]
    reconciliation: Mapping[str, Any]


@dataclass(frozen=True)
class ReviewResponse:
    review_id: str
    blind_result_id: str
    reviewer_id: str
    reviewer_version: str
    rubric_version: str
    ratings: Mapping[str, float]
    comments: Mapping[str, str]
    submitted_at: str

    def __post_init__(self) -> None:
        identifiers = (
            self.review_id,
            self.blind_result_id,
            self.reviewer_id,
            self.reviewer_version,
            self.rubric_version,
            self.submitted_at,
        )
        if any(not value for value in identifiers):
            raise ValueError("review response identifiers and versions are required")
        for dimension, value in self.ratings.items():
            if (
                not dimension
                or isinstance(value, bool)
                or not isinstance(value, (int, float))
                or not math.isfinite(value)
            ):
                raise ValueError("ratings require named, finite numeric values")

    def as_dict(self) -> dict[str, Any]:
        return {
            "review_id": self.review_id,
            "blind_result_id": self.blind_result_id,
            "reviewer_id": self.reviewer_id,
            "reviewer_version": self.reviewer_version,
            "rubric_version": self.rubric_version,
            "ratings": dict(self.ratings),
            "comments": dict(self.comments),
            "submitted_at": self.submitted_at,
        }


def _ref(identifier: str, version: str, digest: str) -> dict[str, str]:
    return {"id": identifier, "version": version, "digest": digest}


def _candidate_label(index: int) -> str:
    """Return labels A..Z, AA..AZ, BA.. for any practical arm count."""
    if index < 0:
        raise ValueError("candidate index must be non-negative")
    value = index + 1
    letters = []
    while value:
        value, remainder = divmod(value - 1, 26)
        letters.append(chr(ord("A") + remainder))
    return "candidate-" + "".join(reversed(letters))


def _blind_output(output: Mapping[str, Any], blind_result_id: str) -> dict[str, Any]:
    """Project comparable decision content without arm- or run-identifying fields."""
    allowed = (
        "recommendation",
        "rationale",
        "alternatives_considered",
        "assumptions",
        "uncertainties",
        "reversal_conditions",
        "evidence_refs",
        "authority_status",
    )
    return {
        "blind_result_id": blind_result_id,
        **{key: copy.deepcopy(output[key]) for key in allowed if key in output},
    }


class ReviewPacketBuilder:
    """Create deterministic blind packets and recoverable internal mappings."""

    def __init__(
        self,
        contracts: CognitionContractRegistry | None = None,
        clock: Callable[[], str] | None = None,
    ) -> None:
        self.contracts = contracts or CognitionContractRegistry()
        self.clock = clock or (lambda: "1970-01-01T00:00:00Z")

    def build(
        self,
        *,
        case_ref: Mapping[str, str],
        run_manifests: Sequence[Mapping[str, Any]],
        arm_outputs: Sequence[Mapping[str, Any]],
        rubric: Mapping[str, Any],
        randomization_seed: int,
        case_material: Mapping[str, Any] | None = None,
    ) -> ReviewPacketBundle:
        if not run_manifests or len(run_manifests) != len(arm_outputs):
            raise ReviewConfigurationError(
                "review packets require one arm output per non-empty run list"
            )
        required_rubric = {"rubric_id", "rubric_version", "dimensions"}
        if not required_rubric.issubset(rubric) or not rubric["dimensions"]:
            raise ReviewConfigurationError("rubric id, version, and dimensions are required")

        manifests = {}
        for manifest in run_manifests:
            self.contracts.validate("EvaluationRun", manifest)
            if manifest["case_ref"] != dict(case_ref):
                raise ReviewConfigurationError("all runs must reference the packet case")
            if manifest["run_id"] in manifests:
                raise ReviewConfigurationError("run ids must be unique within a packet")
            manifests[manifest["run_id"]] = manifest

        paired = []
        for output in arm_outputs:
            self.contracts.validate("ArmOutput", output)
            run_id = output["run_id"]
            if run_id not in manifests:
                raise ReviewConfigurationError("every output must reference a packet run")
            paired.append((manifests[run_id], output))
        if len({output["run_id"] for _, output in paired}) != len(paired):
            raise ReviewConfigurationError("each run may appear only once in a packet")

        paired.sort(key=lambda item: item[0]["run_id"])
        random.Random(randomization_seed).shuffle(paired)
        seed_digest = stable_digest(
            {"randomization_seed": randomization_seed, "case_ref": dict(case_ref)}
        )

        blind_refs = []
        candidates = []
        mapping = {}
        for index, (manifest, output) in enumerate(paired):
            blind_id = _candidate_label(index)
            blind_refs.append(
                _ref(blind_id, output["result_version"], output["result_digest"])
            )
            candidates.append(_blind_output(output, blind_id))
            mapping[blind_id] = {
                "run_ref": _ref(
                    manifest["run_id"],
                    manifest["run_version"],
                    stable_digest(manifest),
                ),
                "arm_ref": copy.deepcopy(manifest["arm_ref"]),
                "result_ref": _ref(
                    output["result_id"],
                    output["result_version"],
                    output["result_digest"],
                ),
            }

        packet_identity = {
            "case_ref": dict(case_ref),
            "rubric_version": rubric["rubric_version"],
            "blind_result_refs": blind_refs,
            "randomization_seed_digest": seed_digest,
        }
        packet_id = "review-packet-" + stable_digest(packet_identity)[:16]
        metadata = {
            "contract_version": "human-review-packet/0.1",
            "packet_id": packet_id,
            "packet_version": "1.0.0",
            **packet_identity,
            "generated_at": self.clock(),
        }
        self.contracts.validate("HumanReviewPacket", metadata)

        reviewer_packet = {
            "format_version": "blind-review-presentation/1.0.0",
            "packet_id": packet_id,
            "case_ref": copy.deepcopy(dict(case_ref)),
            "case_material": copy.deepcopy(dict(case_material or {})),
            "rubric": copy.deepcopy(dict(rubric)),
            "candidates": candidates,
        }
        reconciliation = {
            "format_version": "blind-review-reconciliation/1.0.0",
            "packet_id": packet_id,
            "randomization_seed": randomization_seed,
            "randomization_seed_digest": seed_digest,
            "mapping": mapping,
            "mapping_digest": stable_digest(mapping),
        }
        return ReviewPacketBundle(metadata, reviewer_packet, reconciliation)


def reconcile_reviews(
    responses: Sequence[ReviewResponse],
    reconciliation: Mapping[str, Any],
    rubric: Mapping[str, Any],
) -> tuple[dict[str, Any], ...]:
    mapping = reconciliation.get("mapping", {})
    if reconciliation.get("mapping_digest") != stable_digest(mapping):
        raise ReviewConfigurationError("reconciliation mapping digest does not match")
    dimensions = set(rubric["dimensions"])
    reconciled = []
    seen_reviews = set()
    seen_assignments = set()
    for response in responses:
        if response.review_id in seen_reviews:
            raise ReviewConfigurationError("review ids must be unique")
        seen_reviews.add(response.review_id)
        assignment = (
            response.blind_result_id,
            response.reviewer_id,
            response.reviewer_version,
            response.rubric_version,
        )
        if assignment in seen_assignments:
            raise ReviewConfigurationError("reviewer assignment was submitted more than once")
        seen_assignments.add(assignment)
        if response.blind_result_id not in mapping:
            raise ReviewConfigurationError("review references an unknown blind result")
        if response.rubric_version != rubric["rubric_version"]:
            raise ReviewConfigurationError("review and packet rubric versions differ")
        if set(response.ratings) != dimensions:
            raise ReviewConfigurationError("review must rate every rubric dimension exactly once")
        minimum, maximum = rubric["scale"]["minimum"], rubric["scale"]["maximum"]
        if any(value < minimum or value > maximum for value in response.ratings.values()):
            raise ReviewConfigurationError("rating falls outside the rubric scale")
        reconciled.append(
            {
                **response.as_dict(),
                **copy.deepcopy(mapping[response.blind_result_id]),
            }
        )
    return tuple(reconciled)


def reviewer_disagreement(
    reconciled_reviews: Sequence[Mapping[str, Any]],
) -> tuple[dict[str, Any], ...]:
    grouped: dict[tuple[str, str], list[tuple[str, float]]] = {}
    for review in reconciled_reviews:
        run_id = review["run_ref"]["id"]
        for dimension, rating in review["ratings"].items():
            grouped.setdefault((run_id, dimension), []).append(
                (review["reviewer_id"], rating)
            )
    rows = []
    for (run_id, dimension), values in sorted(grouped.items()):
        ratings = [value for _, value in values]
        rows.append(
            {
                "run_id": run_id,
                "dimension": dimension,
                "reviewer_ratings": [
                    {"reviewer_id": reviewer, "rating": rating}
                    for reviewer, rating in sorted(values)
                ],
                "reviewer_count": len(ratings),
                "mean": fmean(ratings),
                "range": max(ratings) - min(ratings),
                "resolution_status": "unresolved" if len(set(ratings)) > 1 else "agreement",
            }
        )
    return tuple(rows)


@dataclass(frozen=True)
class BenchmarkReportBundle:
    report_metadata: Mapping[str, Any]
    report: Mapping[str, Any]
    raw_export: Mapping[str, Any]


class BenchmarkReporter:
    """Render auditable tables while keeping metric dimensions separate."""

    def __init__(
        self,
        contracts: CognitionContractRegistry | None = None,
        clock: Callable[[], str] | None = None,
    ) -> None:
        self.contracts = contracts or CognitionContractRegistry()
        self.clock = clock or (lambda: "1970-01-01T00:00:00Z")

    def build(
        self,
        *,
        case_refs: Sequence[Mapping[str, str]],
        run_manifests: Sequence[Mapping[str, Any]],
        metric_results: Sequence[Mapping[str, Any]],
        reconciled_reviews: Sequence[Mapping[str, Any]],
        review_packet_refs: Sequence[Mapping[str, str]],
        artifact_refs: Sequence[str],
        failure_examples: Sequence[Mapping[str, Any]] = (),
    ) -> BenchmarkReportBundle:
        if not case_refs or not run_manifests:
            raise ReviewConfigurationError("reports require cases and runs")
        runs = {}
        for manifest in run_manifests:
            self.contracts.validate("EvaluationRun", manifest)
            if manifest["run_id"] in runs:
                raise ReviewConfigurationError("report run ids must be unique")
            runs[manifest["run_id"]] = manifest
        known_case_refs = {stable_digest(item) for item in case_refs}
        if any(stable_digest(run["case_ref"]) not in known_case_refs for run in runs.values()):
            raise ReviewConfigurationError("every report run must reference a report case")
        metric_rows = []
        metric_versions = {}
        for result in metric_results:
            self.contracts.validate("MetricResult", result)
            if result["run_id"] not in runs:
                raise ReviewConfigurationError("metric result references an unknown run")
            manifest = runs[result["run_id"]]
            metric_rows.append(
                {
                    "case_id": manifest["case_ref"]["id"],
                    "run_id": result["run_id"],
                    "arm_id": manifest["arm_ref"]["id"],
                    "metric_id": result["metric_id"],
                    "metric_version": result["metric_version"],
                    "metric_kind": result["metric_kind"],
                    "value": result["value"],
                    "details": copy.deepcopy(result.get("details", {})),
                }
            )
            metric_versions[(result["metric_id"], result["metric_version"])] = {
                "id": result["metric_id"], "version": result["metric_version"]
            }

        run_refs = [
            _ref(run["run_id"], run["run_version"], stable_digest(run))
            for run in sorted(run_manifests, key=lambda value: value["run_id"])
        ]
        sorted_case_refs = sorted(
            (copy.deepcopy(dict(item)) for item in case_refs),
            key=lambda item: (item["id"], item["version"], item["digest"]),
        )
        sorted_metric_versions = [
            metric_versions[key] for key in sorted(metric_versions)
        ]
        sorted_packet_refs = sorted(
            (copy.deepcopy(dict(item)) for item in review_packet_refs),
            key=lambda item: (item["id"], item["version"], item["digest"]),
        )
        identity = {
            "case_refs": sorted_case_refs,
            "run_refs": run_refs,
            "metric_versions": sorted_metric_versions,
            "review_packet_refs": sorted_packet_refs,
            "artifact_refs": sorted(artifact_refs),
        }
        metadata = seal_result(
            {
                "contract_version": "benchmark-report/0.1",
                "report_id": "benchmark-report-" + stable_digest(identity)[:16],
                "report_version": "1.0.0",
                **identity,
                "generated_at": self.clock(),
            }
        )
        self.contracts.validate("BenchmarkReport", metadata)

        disagreement = reviewer_disagreement(reconciled_reviews)
        report = {
            "format_version": "cognition-benchmark-report/1.0.0",
            "report_metadata": metadata,
            "per_case": [
                {
                    "case_ref": copy.deepcopy(dict(case_ref)),
                    "metric_rows": [
                        row for row in metric_rows if row["case_id"] == case_ref["id"]
                    ],
                    "review_rows": [
                        copy.deepcopy(dict(review))
                        for review in reconciled_reviews
                        if runs[review["run_ref"]["id"]]["case_ref"]["id"]
                        == case_ref["id"]
                    ],
                    "disagreement": [
                        row
                        for row in disagreement
                        if runs[row["run_id"]]["case_ref"]["id"] == case_ref["id"]
                    ],
                    "failure_examples": [
                        copy.deepcopy(dict(item))
                        for item in failure_examples
                        if item.get("case_id") == case_ref["id"]
                    ],
                }
                for case_ref in sorted_case_refs
            ],
            "aggregate_metric_table": sorted(
                metric_rows,
                key=lambda row: (row["metric_id"], row["case_id"], row["arm_id"]),
            ),
            "aggregate_human_review_table": list(disagreement),
            "failure_examples": [copy.deepcopy(dict(item)) for item in failure_examples],
            "composite_score": None,
            "raw_export_refs": sorted(artifact_refs),
        }
        raw_export = {
            "format_version": "cognition-benchmark-raw-export/1.0.0",
            "cases": sorted_case_refs,
            "run_manifests": [copy.deepcopy(runs[key]) for key in sorted(runs)],
            "metric_results": sorted(
                (copy.deepcopy(dict(item)) for item in metric_results),
                key=lambda item: (item["run_id"], item["metric_id"]),
            ),
            "human_reviews": sorted(
                (copy.deepcopy(dict(item)) for item in reconciled_reviews),
                key=lambda item: (item["run_ref"]["id"], item["review_id"]),
            ),
            "failure_examples": [copy.deepcopy(dict(item)) for item in failure_examples],
        }
        return BenchmarkReportBundle(metadata, report, raw_export)
