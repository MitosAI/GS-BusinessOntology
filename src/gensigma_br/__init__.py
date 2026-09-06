"""GenSigma Business Reality reference kernel."""

from .contracts import ContractRegistry, ContractViolation, UnknownSemanticType
from .kernel import (
    BusinessRealityKernel,
    CandidateSemanticTypeMismatch,
    EvidenceConflict,
    UnknownCandidate,
    UnknownEvidence,
)

__all__ = [
    "BusinessRealityKernel",
    "CandidateSemanticTypeMismatch",
    "ContractRegistry",
    "ContractViolation",
    "EvidenceConflict",
    "UnknownCandidate",
    "UnknownEvidence",
    "UnknownSemanticType",
]
