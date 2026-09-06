"""GenSigma Business Reality reference kernel."""

from .contracts import ContractRegistry, ContractViolation
from .kernel import (
    BusinessRealityKernel,
    EvidenceConflict,
    UnknownCandidate,
    UnknownEvidence,
)

__all__ = [
    "BusinessRealityKernel",
    "ContractRegistry",
    "ContractViolation",
    "EvidenceConflict",
    "UnknownCandidate",
    "UnknownEvidence",
]
