"""GenSigma Business Reality reference kernel."""

from .authorization import (
    DenyAllPolicyDecisionPoint,
    PermissiveTestPolicyDecisionPoint,
    PolicyDecisionPoint,
    ReferencePolicyDecisionPoint,
)
from .contracts import ContractRegistry, ContractViolation, UnknownSemanticType
from .kernel import (
    AmbiguousTemporalState,
    AuthorizationDenied,
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
    "AuthorizationDenied",
    "BusinessRealityKernel",
    "CandidateSemanticTypeMismatch",
    "CanonicalResourceConflict",
    "ContractRegistry",
    "ContractViolation",
    "EvidenceConflict",
    "DenyAllPolicyDecisionPoint",
    "PermissiveTestPolicyDecisionPoint",
    "PolicyDecisionPoint",
    "ReferencePolicyDecisionPoint",
    "RelationshipInvariantViolation",
    "TemporalQueryError",
    "TemporalStateNotFound",
    "UnknownCandidate",
    "UnknownEvidence",
    "UnknownSemanticType",
    "UnsupportedTemporalPrecision",
]
