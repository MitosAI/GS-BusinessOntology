# EXECUTION PLAN — Executive Cognition Benchmark v0.1

**Status:** READY  
**Owner workstream:** ECR-001 — Executive Cognition Research  
**Design basis:** R001-13 benchmark harness + R001-15 benchmark-practice validation  
**Architecture dependency:** `ADRQ-ECR-001` blocks only the modular routed-cognition arm.

## Goal

Build a reproducible evaluation harness that can compare executive-cognition approaches on identical frozen business decision cases without hindsight leakage, and produce evidence strong enough to keep, modify, or reject the candidate cognition architecture.

## Governing design / research

- `docs/workstreams/ecr/13-R001-COGNITION-BENCHMARK-HARNESS-v0.1.md`
- `docs/workstreams/ecr/15-R001-BENCHMARK-PRACTICE-VALIDATION-v0.1.md`
- `docs/workstreams/ecr/14-R001-F-FINAL-SYNTHESIS-AND-DECISION-ENGINE-PATCH-PROPOSAL-v0.1.md`
- `docs/specs/03-DECISION-ENGINE-AND-CAPABILITY-MODEL-SPEC-v0.1.md`
- `AGENTS.md`
- `docs/program/08-WORKSTREAM-DELIVERY-STANDARD-v0.1.md`

## Deliverables

1. Frozen decision-case schema and fixture validator.
2. Evaluation-run manifest capturing all reproducibility metadata.
3. Common evaluation-arm interface.
4. LLM-only baseline arm.
5. Static-scorecard baseline arm.
6. Historical-human/reconstructed-decision comparison format.
7. Metric/scoring engine for deterministic and rubric-based metrics.
8. Probabilistic forecast scoring utilities including Brier score and calibration-ready output.
9. Blind human-review packet generator.
10. Per-case and aggregate benchmark report generator.
11. Synthetic/test fixture pack proving the harness end to end.
12. Modular routed-cognition evaluation arm after `ADRQ-ECR-001` is resolved.

## Work breakdown

### T1 — Benchmark core contracts

Define machine-readable contracts for:

- `DecisionCase`
- `EvidenceItemRef`
- `EvaluationArm`
- `EvaluationRun`
- `ArmOutput`
- `MetricResult`
- `HumanReviewPacket`
- `BenchmarkReport`

The contracts are benchmark-local and must not invent canonical ontology semantics.

### T2 — Frozen-case loader and leakage guard

Implement case loading and validation with an explicit `as_of` boundary. Evidence dated after the boundary must be rejected from the decision input. Outcome data must remain withheld from arms until scoring.

### T3 — Baseline arm interface + two executable baselines

Implement a stable arm interface and:

- LLM-only baseline;
- static weighted-scorecard baseline.

The interface must permit later addition of the modular routed arm without changing benchmark case semantics.

### T4 — Scoring engine

Implement deterministic metrics first:

- hard-constraint violations;
- policy/authority violations where fixture data supplies rules;
- unsupported claim counts where evidence references are required;
- required-field/trace completeness;
- latency/cost metadata ingestion.

Implement rubric hooks for human-rated dimensions rather than hard-coding subjective judgments as fake deterministic scores.

### T5 — Forecast scoring

Implement Brier score for binary probabilities and retain raw forecast/outcome pairs for later calibration analysis. Do not compute or display calibration bins until sample size/configuration is sufficient and explicitly requested.

### T6 — Blind human review packets

Generate randomized/blinded output packets where feasible so reviewers need not know which arm produced which recommendation. Preserve mapping internally for later scoring.

### T7 — Reporting and reproducibility

Produce:

- per-case arm comparison;
- aggregate metric tables;
- run manifest;
- failure examples;
- reviewer disagreement where applicable;
- raw machine-readable results.

### T8 — Historical case pack

After the harness works on synthetic fixtures, assemble 10–20 historical Bid/No-Bid cases where sufficient evidence exists. This task requires Evidence/Data cooperation and must preserve time-correct evidence boundaries.

### T9 — Modular routed cognition arm

`BLOCKED_BY_ARCH_REQUEST: ADRQ-ECR-001`

Implement only after the Chief Architect approves/modifies the working Decision Engine architecture.

## Dependency graph

```text
T1
|\
| +--> T2
| +--> T3
| +--> T4
| +--> T5
| +--> T6
|       |
+-------+--> T7
            |
            +--> T8
            +--> T9  [blocked by ADRQ-ECR-001]
```

## Parallelizable tasks

After T1 stabilizes, T2–T6 can proceed substantially in parallel.

T8 may begin with case-discovery metadata while T2–T7 are implemented, but no historical fixture is considered valid until the frozen-case schema and leakage checks exist.

## Acceptance suite

- [ ] A benchmark case cannot expose post-`as_of` evidence to an evaluation arm.
- [ ] Outcome fields are withheld from arms and available only to scoring/reporting.
- [ ] Identical frozen cases can be run across multiple arms.
- [ ] Every run records arm/model/tool/configuration versions and timestamps.
- [ ] Non-deterministic arms can be run repeatedly without overwriting previous results.
- [ ] LLM-only and static-scorecard baselines execute end to end on synthetic fixtures.
- [ ] Brier score is tested against known examples.
- [ ] Human-review packets can be blinded/randomized and later reconciled to arm IDs.
- [ ] Reports preserve per-case results and do not hide failures behind a single aggregate score.
- [ ] Benchmark-local contracts do not modify canonical ontology or Decision Engine semantics.
- [ ] CI tests pass for core contracts, leakage guards, scoring, and report generation.

## Risks / unknowns

1. Historical cases may have incomplete evidence; the harness must permit partial cases without fabricating missing context.
2. Human review may be noisy; reviewer disagreement must remain visible.
3. Too few cases may make calibration statistics misleading; raw forecast records should exist before aggregate calibration claims.
4. LLM model changes can alter baseline results; exact model/configuration versions must be preserved.
5. Cost/latency comparisons depend on runtime/tool instrumentation and may evolve.

## Explicitly out of scope

- selecting production database/platform architecture;
- changing canonical ontology schemas;
- approving Decision Engine shared semantics;
- production autonomous decisions;
- using realized outcome as the sole measure of decision quality;
- building the modular routed cognition arm before architecture resolution.

## Architecture questions

Open: `ADRQ-ECR-001` — working Decision Engine architecture and shared cognition semantics.

This does **not** block T1–T8.