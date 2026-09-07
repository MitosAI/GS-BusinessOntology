"""GenSigma Business Reality reference kernel."""

from .contracts import ContractRegistry, ContractViolation, UnknownSemanticType
from .kernel import (
    AmbiguousTemporalState,
    BusinessRealityKernel,
    CandidateSemanticTypeMismatch,
    EvidenceConflict,
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
    "ContractRegistry",
    "ContractViolation",
    "EvidenceConflict",
    "TemporalQueryError",
    "TemporalStateNotFound",
    "UnknownCandidate",
    "UnknownEvidence",
    "UnknownSemanticType",
    "UnsupportedTemporalPrecision",
]
