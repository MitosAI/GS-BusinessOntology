# Executive Cognition Benchmark Contracts

This Issue #11 foundation defines benchmark-local artifacts for comparing
executive-cognition approaches under ADR-003. It does not add canonical ontology
objects or select a production model, provider, database, runtime, or agent
framework.

## Contract Surface

The JSON Schema bundle defines `DecisionCase`, decision-time evidence references,
`HeldOutOutcome`, `EvaluationArm`, `EvaluationRun`, `ArmOutput`, `MetricResult`,
`HumanReviewPacket`, and `BenchmarkReport`.

`DecisionCase.as_of` is the decision-time knowledge cutoff. A case contains a
frozen input projection and the evidence available to it. Outcome data uses the
separate `HeldOutOutcome` contract and is absent from the normal immutable
`ArmInput` object.

Every run records versioned case and arm references plus applicable configuration,
model, prompt, tool, and metric versions. Distinct `run_id` values bind repeated
runs to distinct result identities. Canonical sorted JSON and SHA-256 digests make
serialization and tamper detection reproducible, matching the convention merged
in PR #24.

## Run

Install the repository test dependencies, then run:

```bash
pytest -q
python -m gensigma_benchmarks.executive_cognition \
  DecisionCase \
  benchmarks/executive-cognition/fixtures/bid-no-bid-valid.json
```

The validator prints the stable digest on success and raises a location-specific
contract error on failure. The committed invalid fixtures cover missing time,
mixed input/outcome data, an unresolved evidence reference, and an incomplete run
manifest.

## Frozen-case Loading

`FrozenCaseLoader` validates the Issue #11 contract, then checks every decision-time
evidence reference against `DecisionCase.as_of`. Both `available_at` and
`effective_at` must be no later than the boundary. Missing timestamps fail contract
validation; later timestamps raise `HindsightLeakageViolation`.

Successful loads return `FrozenCaseLoad`, containing an immutable, outcome-free
`ArmInput` and ordered `ValidationAuditEntry` records. Failed loads attach the audit
entries accumulated before rejection to `FrozenCaseLoadError`. These rules are
benchmark replay mechanics only and do not redefine canonical temporal or
provenance semantics.

## Downstream Interfaces

- Issue #12 consumes `DecisionCase` and returns `ArmInput`. It must enforce
  `EvidenceRef.available_at <= DecisionCase.as_of`; held-out outcomes remain on a
  scoring-only path.
- Issue #13 consumes `ArmInput` plus `EvaluationArm`, creates an `EvaluationRun`,
  and emits a sealed `ArmOutput` for each execution attempt.
- Issue #14 consumes `EvaluationRun`, sealed `ArmOutput`, and the separately
  authorized `HeldOutOutcome`; it emits sealed, versioned `MetricResult` records.
- Issue #15 consumes case presentation data and blinded `ArmOutput` references to
  create `HumanReviewPacket` metadata, then reconciles reviews and metric results
  into a sealed `BenchmarkReport` without hiding per-case dimensions.

Temporal filtering, model execution, scoring logic, review randomization, and
report rendering remain owned by those downstream issues.

## Baseline Arms

`EvaluationRunner` executes every `BenchmarkArm` against the same immutable
`ArmInput`, validates the arm metadata, records an `EvaluationRun`, and seals the
common `ArmOutput`. Repeated executions require distinct run identifiers and
therefore produce distinct immutable result identities.

`LLMOnlyBaseline` accepts a provider-neutral `ModelAdapter`. The exact model and
prompt versions are benchmark configuration recorded in the run manifest; no
provider is selected by the architecture. The model receives only the serialized
outcome-free `ArmInput`.

`StaticScorecardBaseline` reads the committed, versioned Bid/No-Bid criteria and
weights. Its criteria, mappings, thresholds, contributions, and configuration
digest remain inspectable rather than hidden in a prompt. Both baselines are
comparators for M11, not production Decision Engine implementations.
