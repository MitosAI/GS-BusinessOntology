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


class TemporalQueryError(ValueError):
    pass


class UnsupportedTemporalPrecision(TemporalQueryError):
    pass


class TemporalStateNotFound(TemporalQueryError):
    pass


class AmbiguousTemporalState(TemporalQueryError):
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


_TEMPORAL_MODES = frozenset(
    {"effective_using_current_knowledge", "accepted_as_recorded_at_time"}
)


def _parse_temporal_timestamp(value: str, *, field: str) -> datetime:
    if not isinstance(value, str):
        raise TemporalQueryError(f"{field} must be a timezone-aware RFC 3339 string")
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise TemporalQueryError(
            f"{field} must be a timezone-aware RFC 3339 string"
        ) from exc
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise TemporalQueryError(f"{field} must include a UTC offset")
    return parsed.astimezone(UTC)


def _is_effective_at(resource: dict[str, Any], as_of: datetime) -> bool:
    effective_time = resource.get("effective_time", {})
    precision = effective_time.get("precision")
    if precision != "exact":
        raise UnsupportedTemporalPrecision(
            f"Temporal reads require exact precision; got {precision!r}"
        )
    valid_from_raw = effective_time.get("valid_from")
    valid_to_raw = effective_time.get("valid_to")
    valid_from = None if valid_from_raw is None else _parse_temporal_timestamp(
        valid_from_raw, field="valid_from"
    )
    valid_to = None if valid_to_raw is None else _parse_temporal_timestamp(
        valid_to_raw, field="valid_to"
    )
    if valid_from is not None and valid_to is not None and valid_from >= valid_to:
        raise TemporalQueryError("effective_time requires valid_from < valid_to")
    return (valid_from is None or valid_from <= as_of) and (
        valid_to is None or as_of < valid_to
    )


class BusinessRealityKernel:
    """Executable reference kernel for evidence -> candidate -> canonical promotion.

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
        """Promote a governed candidate into canonical Business Reality.

        There is intentionally no public direct `put_canonical` method. Canonical state
        can enter through a promotion path so evidence and decision lineage are retained.
        """
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
        self._canonical_history.setdefault(resource_id, []).append(copy.deepcopy(resource))
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

        semantic_type = replacement.get("type")
        if not semantic_type:
            raise ValueError("Corrected resource requires a semantic type")
        self.contracts.validate_semantic_resource(semantic_type, replacement)

        self._canonical_history[resource_id].append(copy.deepcopy(replacement))
        record = CorrectionRecord(
            resource_id=resource_id,
            actor=actor,
            reason=reason,
            recorded_at=_utc_now(),
        )
        self._corrections.append(record)
        return record

    def get_state(
        self,
        resource_id: str,
        *,
        as_of: str,
        temporal_mode: str = "effective_using_current_knowledge",
    ) -> dict[str, Any]:
        """Return exact point-in-time state under the contracted temporal mode."""
        if temporal_mode not in _TEMPORAL_MODES:
            raise TemporalQueryError(
                f"Unknown temporal mode {temporal_mode!r}; "
                f"choose one of {sorted(_TEMPORAL_MODES)}"
            )
        query_time = _parse_temporal_timestamp(as_of, field="as_of")
        try:
            history = self._canonical_history[resource_id]
        except KeyError as exc:
            raise KeyError(f"Unknown canonical resource: {resource_id}") from exc
        applicable: list[tuple[datetime, dict[str, Any]]] = []
        for resource in history:
            if not _is_effective_at(resource, query_time):
                continue
            recorded_at = _parse_temporal_timestamp(
                resource["recorded_at"], field="recorded_at"
            )
            if temporal_mode == "accepted_as_recorded_at_time" and recorded_at > query_time:
                continue
            applicable.append((recorded_at, resource))
        if not applicable:
            raise TemporalStateNotFound(
                f"No state for {resource_id!r} applies at {as_of!r} "
                f"under mode {temporal_mode!r}"
            )
        latest_recorded_at = max(recorded_at for recorded_at, _ in applicable)
        winners = [
            resource
            for recorded_at, resource in applicable
            if recorded_at == latest_recorded_at
        ]
        if len(winners) > 1 and any(resource != winners[0] for resource in winners[1:]):
            raise AmbiguousTemporalState(
                f"Multiple states for {resource_id!r} are equally current at {as_of!r}"
            )
        return copy.deepcopy(winners[0])

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

    def get_promotion_records(self, resource_id: str | None = None) -> list[PromotionRecord]:
        if resource_id is None:
            return list(self._promotions)
        return [record for record in self._promotions if record.resource_id == resource_id]

    def get_correction_records(self, resource_id: str | None = None) -> list[CorrectionRecord]:
        if resource_id is None:
            return list(self._corrections)
        return [record for record in self._corrections if record.resource_id == resource_id]
