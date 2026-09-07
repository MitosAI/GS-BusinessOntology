"""Deterministic architecture benchmark contracts for GenSigma."""

from .business_reality import BenchmarkRunner, ReferenceAdapter, build_fixture
from .executive_cognition import (
    ArmInput,
    BenchmarkContractViolation,
    CognitionContractRegistry,
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
    "ReferenceAdapter",
    "build_fixture",
    "canonical_json",
    "immutable_result_identity",
    "seal_result",
    "stable_digest",
]
