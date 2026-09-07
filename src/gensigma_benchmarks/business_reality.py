"""Persistence-neutral Business Reality workload benchmark."""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Protocol


SCALE_FACTORS = {"tiny": 1, "small": 5, "medium": 25}
PENDING_WORKLOADS = {
    "historical_as_of_read": "temporal runtime is not implemented",
    "security_scoped_traversal": "security enforcement runtime is not implemented",
}


@dataclass(frozen=True)
class Fixture:
    version: str
    scale: str
    identities: tuple[dict[str, Any], ...]
    relationships: tuple[dict[str, str], ...]
    evidence: tuple[dict[str, str], ...]


@dataclass(frozen=True)
class WorkloadResult:
    name: str
    status: str
    operation_count: int
    result_count: int
    digest: str | None
    reason: str | None = None


class BenchmarkAdapter(Protocol):
    def resolve_identity(self, alias: str) -> list[str]: ...

    def get_neighbors(self, resource_id: str, depth: int) -> list[str]: ...

    def get_evidence(self, resource_id: str) -> list[str]: ...

    def promote(self, candidate_id: str, resource_id: str) -> str: ...

    def correct(self, resource_id: str, revision: str) -> list[str]: ...


def build_fixture(scale: str) -> Fixture:
    try:
        factor = SCALE_FACTORS[scale]
    except KeyError as exc:
        raise ValueError(f"unknown scale {scale!r}; choose {sorted(SCALE_FACTORS)}") from exc

    identities: list[dict[str, Any]] = []
    relationships: list[dict[str, str]] = []
    evidence: list[dict[str, str]] = []
    for index in range(factor):
        org = f"org-{index:03d}"
        opportunity = f"opportunity-{index:03d}"
        partner = f"partner-{index:03d}"
        identities.extend(
            [
                {"id": org, "aliases": [f"Customer {index}", f"C{index}"]},
                {"id": opportunity, "aliases": [f"Pursuit {index}"]},
                {"id": partner, "aliases": [f"Partner {index}"]},
            ]
        )
        relationships.extend(
            [
                {"from": org, "to": opportunity, "type": "customer_of"},
                {"from": opportunity, "to": partner, "type": "partner_in"},
            ]
        )
        evidence.extend(
            [
                {"id": f"evidence-{index:03d}-a", "target": opportunity},
                {"id": f"evidence-{index:03d}-b", "target": opportunity},
            ]
        )
    return Fixture("0.1", scale, tuple(identities), tuple(relationships), tuple(evidence))


class ReferenceAdapter:
    """In-memory reference adapter; it is not a persistence recommendation."""

    def __init__(self, fixture: Fixture) -> None:
        self.fixture = fixture
        self._aliases = {
            alias: item["id"]
            for item in fixture.identities
            for alias in item["aliases"]
        }
        self._edges = [(edge["from"], edge["to"]) for edge in fixture.relationships]
        self._evidence = fixture.evidence
        self._canonical: dict[str, list[str]] = {}

    def resolve_identity(self, alias: str) -> list[str]:
        value = self._aliases.get(alias)
        return [] if value is None else [value]

    def get_neighbors(self, resource_id: str, depth: int) -> list[str]:
        visited = {resource_id}
        frontier = {resource_id}
        for _ in range(depth):
            next_frontier: set[str] = set()
            for left, right in self._edges:
                if left in frontier and right not in visited:
                    next_frontier.add(right)
                if right in frontier and left not in visited:
                    next_frontier.add(left)
            visited.update(next_frontier)
            frontier = next_frontier
        return sorted(visited - {resource_id})

    def get_evidence(self, resource_id: str) -> list[str]:
        return sorted(item["id"] for item in self._evidence if item["target"] == resource_id)

    def promote(self, candidate_id: str, resource_id: str) -> str:
        self._canonical.setdefault(resource_id, []).append(candidate_id)
        return resource_id

    def correct(self, resource_id: str, revision: str) -> list[str]:
        history = self._canonical.setdefault(resource_id, [])
        history.append(revision)
        return list(history)


def _digest(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode()).hexdigest()


class BenchmarkRunner:
    def __init__(self, adapter: BenchmarkAdapter, fixture: Fixture) -> None:
        self.adapter = adapter
        self.fixture = fixture

    def run(self) -> dict[str, Any]:
        factor = SCALE_FACTORS[self.fixture.scale]
        workloads: list[WorkloadResult] = []

        identity_results = [self.adapter.resolve_identity(f"C{i}") for i in range(factor)]
        workloads.append(self._complete("canonical_identity_lookup", factor, identity_results))

        traversal_results = [
            self.adapter.get_neighbors(f"org-{i:03d}", 2) for i in range(factor)
        ]
        workloads.append(self._complete("typed_relationship_neighborhood", factor, traversal_results))

        evidence_results = [
            self.adapter.get_evidence(f"opportunity-{i:03d}") for i in range(factor)
        ]
        workloads.append(self._complete("evidence_lineage", factor, evidence_results))

        promotions = [
            self.adapter.promote(f"candidate-{i:03d}", f"canonical-{i:03d}")
            for i in range(factor)
        ]
        workloads.append(self._complete("canonical_promotion", factor, promotions))

        corrections = [
            self.adapter.correct(f"canonical-{i:03d}", f"revision-{i:03d}")
            for i in range(factor)
        ]
        workloads.append(self._complete("canonical_correction", factor, corrections))

        workloads.extend(
            WorkloadResult(name, "pending", 0, 0, None, reason)
            for name, reason in sorted(PENDING_WORKLOADS.items())
        )
        result = {
            "benchmark_version": "0.1",
            "fixture_version": self.fixture.version,
            "scale": self.fixture.scale,
            "cardinality": {
                "identities": len(self.fixture.identities),
                "relationships": len(self.fixture.relationships),
                "evidence": len(self.fixture.evidence),
            },
            "workloads": [asdict(item) for item in workloads],
        }
        result["result_digest"] = _digest(result)
        return result

    @staticmethod
    def _complete(name: str, operations: int, values: list[Any]) -> WorkloadResult:
        return WorkloadResult(
            name=name,
            status="complete",
            operation_count=operations,
            result_count=sum(len(value) if isinstance(value, list) else 1 for value in values),
            digest=_digest(values),
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scale", choices=sorted(SCALE_FACTORS), default="small")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    fixture = build_fixture(args.scale)
    result = BenchmarkRunner(ReferenceAdapter(fixture), fixture).run()
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
