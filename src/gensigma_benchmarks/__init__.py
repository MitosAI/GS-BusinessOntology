"""Deterministic architecture benchmark contracts for GenSigma."""

from .business_reality import BenchmarkRunner, ReferenceAdapter, build_fixture
from .cognition_arms import (
    ArmDecision,
    ArmExecution,
    BenchmarkArm,
    EvaluationRunner,
    LLMOnlyBaseline,
    ModelAdapter,
    StaticScorecardBaseline,
    arm_input_document,
)
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
    "ArmDecision",
    "ArmExecution",
    "BenchmarkArm",
    "BenchmarkContractViolation",
    "BenchmarkRunner",
    "CognitionContractRegistry",
    "FrozenCaseLoad",
    "FrozenCaseLoadError",
    "FrozenCaseLoader",
    "HindsightLeakageViolation",
    "EvaluationRunner",
    "LLMOnlyBaseline",
    "ModelAdapter",
    "ReferenceAdapter",
    "StaticScorecardBaseline",
    "ValidationAuditEntry",
    "arm_input_document",
    "build_fixture",
    "canonical_json",
    "immutable_result_identity",
    "seal_result",
    "stable_digest",
]
