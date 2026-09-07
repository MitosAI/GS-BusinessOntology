"""Deterministic architecture benchmark contracts for GenSigma."""

from .business_reality import BenchmarkRunner, ReferenceAdapter, build_fixture
from .executive_cognition import (
    ArmInput,
    BenchmarkContractViolation,
    CognitionContractRegistry,
    FrozenCaseLoad,
    FrozenCaseLoadError,
    FrozenCaseLoader,
    HindsightLeakageViolation,
    ValidationAuditEntry,
    canonical_json,
    immutable_result_identity,
    seal_result,
    stable_digest,
)

__all__ = [
    "ArmInput",
    "BenchmarkContractViolation",
    "BenchmarkRunner",
    "CognitionContractRegistry",
    "FrozenCaseLoad",
    "FrozenCaseLoadError",
    "FrozenCaseLoader",
    "HindsightLeakageViolation",
    "ReferenceAdapter",
    "ValidationAuditEntry",
    "build_fixture",
    "canonical_json",
    "immutable_result_identity",
    "seal_result",
    "stable_digest",
]
