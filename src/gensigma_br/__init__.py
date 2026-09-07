"""GenSigma Business Reality reference kernel."""

from .contracts import ContractRegistry, ContractViolation, UnknownSemanticType
from .kernel import (
    AmbiguousTemporalState,
    BusinessRealityKernel,
    CandidateSemanticTypeMismatch,
    CanonicalResourceConflict,
    EvidenceConflict,
    RelationshipInvariantViolation,
    TemporalQueryError,
    TemporalStateNotFound,
    UnknownCandidate,
    UnknownEvidence,
    UnsupportedTemporalPrecision,
)

__all__ = [
    "AmbiguousTemporalState",
    "BusinessRealityKernel",
    "CandidateSemanticTypeMismatch",
    "CanonicalResourceConflict",
    "ContractRegistry",
    "ContractViolation",
    "EvidenceConflict",
    "RelationshipInvariantViolation",
    "TemporalQueryError",
    "TemporalStateNotFound",
    "UnknownCandidate",
    "UnknownEvidence",
    "UnknownSemanticType",
    "UnsupportedTemporalPrecision",
]
