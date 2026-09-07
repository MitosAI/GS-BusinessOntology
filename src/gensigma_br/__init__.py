"""GenSigma Business Reality reference kernel."""

from .contracts import ContractRegistry, ContractViolation, UnknownSemanticType
from .kernel import (
    BusinessRealityKernel,
    CandidateSemanticTypeMismatch,
    CanonicalResourceConflict,
    EvidenceConflict,
    RelationshipInvariantViolation,
    UnknownCandidate,
    UnknownEvidence,
)

__all__ = [
    "BusinessRealityKernel",
    "CandidateSemanticTypeMismatch",
    "CanonicalResourceConflict",
    "ContractRegistry",
    "ContractViolation",
    "EvidenceConflict",
    "RelationshipInvariantViolation",
    "UnknownCandidate",
    "UnknownEvidence",
    "UnknownSemanticType",
]
