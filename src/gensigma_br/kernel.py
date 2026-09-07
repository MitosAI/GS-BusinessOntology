from __future__ import annotations

import copy
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Any

from .contracts import ContractRegistry


class EvidenceConflict(ValueError):
    pass


class UnknownEvidence(KeyError):
    pass


class UnknownCandidate(KeyError):
    pass


class CandidateConflict(ValueError):
    pass


class CandidateSemanticTypeMismatch(ValueError):
    pass


class CanonicalResourceConflict(ValueError):
    pass


class RelationshipInvariantViolation(ValueError):
    pass


@dataclass(frozen=True)
class PromotionRecord:
    resource_id: str
    candidate_id: str
    evidence_ids: tuple[str, ...]
    actor: str
    reason: str
    recorded_at: str


@dataclass(frozen=True)
class CorrectionRecord:
    resource_id: str
    actor: str
    reason: str
    recorded_at: str


def _utc_now() -> str:
    return datetime.now(UTC).isoformat().replace("+00:00", "Z")


class BusinessRealityKernel:
    """Executable reference kernel for governed Business Reality semantics.

    This implementation is deliberately in-memory. It proves semantic and behavioral
    invariants before the program selects production persistence technology.
    """

    def __init__(self, contracts_root: str = "contracts") -> None:
        self.contracts = ContractRegistry(contracts_root)
        self._raw_evidence: dict[str, dict[str, Any]] = {}
        self._candidates: dict[str, dict[str, Any]] = {}
        self._canonical_history: dict[str, list[dict[str, Any]]] = {}
        self._promotions: list[PromotionRecord] = []
        self._corrections: list[CorrectionRecord] = []

    # ---------------------------- Evidence ----------------------------
    def append_raw_evidence(self, evidence: dict[str, Any]) -> bool:
        """Append raw evidence.

        Returns True on first insert and False on an exact replay. Reusing the same
        evidence_id for different content is rejected rather than silently overwritten.
        """
        self.contracts.validate("schemas/evidence/raw-evidence.schema.json", evidence)
        evidence_id = evidence["evidence_id"]
        existing = self._raw_evidence.get(evidence_id)
        if existing is None:
            self._raw_evidence[evidence_id] = copy.deepcopy(evidence)
            return True
        if existing == evidence:
            return False
        raise EvidenceConflict(
            f"Raw evidence is immutable: {evidence_id} already exists with different content"
        )

    def get_raw_evidence(self, evidence_id: str) -> dict[str, Any]:
        try:
            return copy.deepcopy(self._raw_evidence[evidence_id])
        except KeyError as exc:
            raise UnknownEvidence(evidence_id) from exc

    # ---------------------------- Candidates ----------------------------
    def propose_candidate(self, candidate: dict[str, Any]) -> bool:
        self.contracts.validate("schemas/evidence/candidate.schema.json", candidate)
        missing = [
            evidence_id
            for evidence_id in candidate["source_evidence_ids"]
            if evidence_id not in self._raw_evidence
        ]
        if missing:
            raise UnknownEvidence(
                f"Candidate references evidence not present in the evidence store: {missing}"
            )

        candidate_id = candidate["candidate_id"]
        existing = self._candidates.get(candidate_id)
        if existing is None:
            self._candidates[candidate_id] = copy.deepcopy(candidate)
            return True
        if existing == candidate:
            return False
        raise CandidateConflict(f"Candidate {candidate_id} already exists with different content")

    def get_candidate(self, candidate_id: str) -> dict[str, Any]:
        try:
            return copy.deepcopy(self._candidates[candidate_id])
        except KeyError as exc:
            raise UnknownCandidate(candidate_id) from exc

    # ---------------------------- Canonical state ----------------------------
    def promote_candidate(
        self,
        candidate_id: str,
        resource: dict[str, Any],
        *,
        actor: str,
        reason: str,
    ) -> PromotionRecord:
        """Promote a governed candidate into canonical Business Reality."""
        candidate = self.get_candidate(candidate_id)
        if candidate.get("resolution_status") in {"rejected", "superseded"}:
            raise ValueError(f"Candidate {candidate_id} cannot be promoted from its current state")

        semantic_type = resource.get("type")
        if not semantic_type:
            raise ValueError("Canonical resource requires a semantic type")

        proposed_semantic_type = candidate.get("proposed_semantic_type")
        if proposed_semantic_type is not None and proposed_semantic_type != semantic_type:
            raise CandidateSemanticTypeMismatch(
                f"Candidate {candidate_id} proposes {proposed_semantic_type!r} "
                f"but resource type is {semantic_type!r}"
            )

        self.contracts.validate_semantic_resource(semantic_type, resource)
        resource_id = resource["id"]
        if resource_id in self._canonical_history:
            raise CanonicalResourceConflict(
                f"Canonical resource {resource_id} already exists; use the correction path"
            )

        if semantic_type == "BusinessRelationship":
            self._validate_business_relationship(resource, candidate=candidate)

        self._canonical_history[resource_id] = [copy.deepcopy(resource)]
        record = PromotionRecord(
            resource_id=resource_id,
            candidate_id=candidate_id,
            evidence_ids=tuple(candidate["source_evidence_ids"]),
            actor=actor,
            reason=reason,
            recorded_at=_utc_now(),
        )
        self._promotions.append(record)
        return record

    def correct_canonical_state(
        self,
        resource_id: str,
        replacement: dict[str, Any],
        *,
        actor: str,
        reason: str,
    ) -> CorrectionRecord:
        """Append a corrected interpretation while preserving prior canonical history."""
        if resource_id not in self._canonical_history:
            raise KeyError(f"Unknown canonical resource: {resource_id}")
        if replacement.get("id") != resource_id:
            raise ValueError("Correction must preserve canonical resource identity")

        current_type = self._canonical_history[resource_id][-1].get("type")
        semantic_type = replacement.get("type")
        if not semantic_type:
            raise ValueError("Corrected resource requires a semantic type")
        if semantic_type != current_type:
            raise ValueError("Correction must preserve canonical semantic type")

        self.contracts.validate_semantic_resource(semantic_type, replacement)
        if semantic_type == "BusinessRelationship":
            self._validate_business_relationship(replacement)

        self._canonical_history[resource_id].append(copy.deepcopy(replacement))
        record = CorrectionRecord(
            resource_id=resource_id,
            actor=actor,
            reason=reason,
            recorded_at=_utc_now(),
        )
        self._corrections.append(record)
        return record

    def get_object(self, resource_id: str) -> dict[str, Any]:
        try:
            return copy.deepcopy(self._canonical_history[resource_id][-1])
        except KeyError as exc:
            raise KeyError(f"Unknown canonical resource: {resource_id}") from exc

    def get_history(self, resource_id: str) -> list[dict[str, Any]]:
        try:
            return copy.deepcopy(self._canonical_history[resource_id])
        except KeyError as exc:
            raise KeyError(f"Unknown canonical resource: {resource_id}") from exc

    def get_relationships(
        self,
        resource_id: str,
        *,
        relationship_type: str | None = None,
        scope_id: str | None = None,
    ) -> list[dict[str, Any]]:
        """Return current relationships for a participant, traversable from either side.

        Effective-time and security filtering are intentionally deferred to the next
        bounded runtime increments. Callers cannot infer those guarantees from this API.
        """
        self.get_object(resource_id)
        matches: list[dict[str, Any]] = []
        for history in self._canonical_history.values():
            relationship = history[-1]
            if relationship.get("type") != "BusinessRelationship":
                continue
            participant_ids = {
                participant["participant_ref"]["id"]
                for participant in relationship["participants"]
            }
            if resource_id not in participant_ids:
                continue
            if (
                relationship_type is not None
                and relationship["relationship_type"] != relationship_type
            ):
                continue
            if scope_id is not None and scope_id not in {
                scope_ref["id"] for scope_ref in relationship["scope_refs"]
            }:
                continue
            matches.append(copy.deepcopy(relationship))
        return sorted(matches, key=lambda item: item["id"])

    def get_promotion_records(self, resource_id: str | None = None) -> list[PromotionRecord]:
        if resource_id is None:
            return list(self._promotions)
        return [record for record in self._promotions if record.resource_id == resource_id]

    def get_correction_records(self, resource_id: str | None = None) -> list[CorrectionRecord]:
        if resource_id is None:
            return list(self._corrections)
        return [record for record in self._corrections if record.resource_id == resource_id]

    def _validate_business_relationship(
        self,
        relationship: dict[str, Any],
        *,
        candidate: dict[str, Any] | None = None,
    ) -> None:
        if candidate is not None and candidate.get("candidate_type") != "relationship":
            raise RelationshipInvariantViolation(
                "BusinessRelationship promotion requires a relationship candidate"
            )

        participant_keys: set[tuple[str, str, str | None]] = set()
        for participant in relationship["participants"]:
            reference = participant["participant_ref"]
            key = (
                reference["id"],
                participant["contextual_role"],
                participant.get("role_qualifier"),
            )
            if key in participant_keys:
                raise RelationshipInvariantViolation(
                    "A relationship cannot repeat the same participant, role, and qualifier"
                )
            participant_keys.add(key)
            self._validate_canonical_ref(reference, purpose="participant")

        for reference in relationship["scope_refs"]:
            self._validate_canonical_ref(reference, purpose="scope")

    def _validate_canonical_ref(
        self, reference: dict[str, Any], *, purpose: str
    ) -> None:
        try:
            target = self._canonical_history[reference["id"]][-1]
        except KeyError as exc:
            raise RelationshipInvariantViolation(
                f"Relationship {purpose} {reference['id']!r} is not canonical"
            ) from exc

        for field in ("type", "model_owner", "contract_version"):
            if reference[field] != target.get(field):
                raise RelationshipInvariantViolation(
                    f"Relationship {purpose} reference {reference['id']!r} "
                    f"has incompatible {field}"
                )
