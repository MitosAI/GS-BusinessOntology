# Executive Cognition Benchmark Scoring

The scoring layer emits separate, versioned `MetricResult` records. It does not
produce a composite intelligence or decision-quality score.

Deterministic metrics are limited to conditions that the benchmark can verify
from structured case data, output fields, and explicit fixture rules: hard
constraints, policy/authority combinations, trace completeness, and evidence
reference membership. The unsupported-evidence metric does not claim to detect
all unsupported natural-language assertions.

Each rule-derived result records the case-bound fixture-rule version and digest.
Rules for another case or case version fail explicitly rather than being applied
silently.

Operational values are measurements supplied by runtime instrumentation. They
are retained independently as latency, cost, review-time, and retry metrics.

Binary probability forecasts use mean Brier loss. Every raw probability/outcome
pair and its squared error is retained in the metric details. Calibration bins
are produced only when bin edges are explicitly supplied and the configured
minimum of 20 observations is met; otherwise the result records why calibration
was not computed.

Subjective executive-quality dimensions are emitted as a `human_rubric` hook
with a null value and `awaiting_human_review` status. Issue #15 owns blinded
review collection and reporting. Process quality, forecast quality, operational
performance, human judgment, and realized outcomes remain distinct.

All definitions in `cognition-metrics-v1.json` are benchmark-local. They do not
change canonical ontology, evidence, authority, temporal, or Decision Engine
semantics.
