# R001 — Benchmark Practice Validation

**Status:** COMPLETE — benchmark-first validation of the existing cognition harness  
**Owner:** ECR-001 — Executive Cognition Research Lead  
**Architecture impact:** `LOCAL_SOLVE`; no shared architecture is changed by this artifact.

## Question

Does the proposed GenSigma executive-cognition benchmark harness follow established public evaluation practice closely enough to proceed to implementation, or are we inventing an unnecessary bespoke evaluation method?

## Why it matters

The new repository operating law requires external benchmark practice to be checked before a material research/evaluation mechanism is adopted. R001-13 already proposed a frozen-case, multi-arm, multi-metric evaluation harness. This artifact validates that design against established evaluation practice before implementation tasks are issued.

## Evidence / public practice

### 1. NIST — automated benchmark evaluation practice

NIST's 2026 draft guidance on automated benchmark evaluations organizes good practice around three broad activities:

1. define evaluation objectives and select appropriate benchmarks;
2. implement and run evaluations rigorously;
3. analyze and report results transparently.

NIST explicitly emphasizes validity, transparency, reproducibility, and evaluation design that informs real deployment/procurement decisions rather than producing decorative scores.

Source: NIST, *Towards Best Practices for Automated Benchmark Evaluations* (2026)  
https://www.nist.gov/news-events/news/2026/01/towards-best-practices-automated-benchmark-evaluations

### 2. Stanford CRFM HELM — standardized scenarios, multiple metrics, reproducibility

HELM treats evaluation as a combination of standardized scenarios and multiple metrics rather than one aggregate score. Current HELM materials emphasize prompt-level transparency and reproducibility of results through a common evaluation framework.

This supports GenSigma's decision to freeze case inputs, compare multiple systems on the same cases, retain full run traces, and avoid reducing executive cognition to a single score.

Sources:  
Stanford CRFM, *Holistic Evaluation of Language Models (HELM)*  
https://crfm.stanford.edu/helm/index.html

Stanford CRFM, *HELM Capabilities*  
https://crfm.stanford.edu/helm/capabilities/v1.14.0/

### 3. Forecast verification — proper scoring and calibration

Gneiting and Raftery show that probabilistic forecasts should be evaluated with proper scoring rules that reward honest probability assessments. The Brier score is a proper score for binary probabilistic forecasts. Related forecast-verification work emphasizes calibration together with sharpness rather than treating apparent confidence as quality.

This supports R001-13's use of Brier score and calibration only where a system produces legitimate probabilities.

Sources:  
Gneiting & Raftery, *Strictly Proper Scoring Rules, Prediction, and Estimation*, JASA 102(477), 2007  
https://sites.stat.washington.edu/people/raftery/Research/PDF/Gneiting2007jasa.pdf

Gneiting, Balabdaoui & Raftery, *Probabilistic forecasts, calibration and sharpness*, JRSS-B 69, 2007  
https://doi.org/10.1111/j.1467-9868.2007.00587.x

## Synthesis

The existing R001 cognition benchmark harness is directionally consistent with established evaluation practice:

- **Objective-first:** evaluate whether a cognition architecture materially improves business decision quality, not whether it sounds intelligent.
- **Scenario/case based:** use frozen decision cases with an `as-of` timestamp.
- **Controlled comparison:** run multiple evaluation arms against the same evidence boundary.
- **Multi-metric:** score constraint compliance, evidence use, uncertainty honesty, recommendation quality, auditability, operational cost, human preference, and calibrated forecasts separately.
- **Reproducible:** preserve inputs, prompts/configuration, method/model versions, outputs, and scoring results.
- **Transparent:** make the full decision trace inspectable.
- **Outcome-aware but not outcome-dominated:** keep ex-ante process quality separate from ex-post luck.

## Gaps to close before implementation

R001-13 should be made more execution-specific in five areas:

1. **Evaluation manifest:** every run needs an immutable manifest containing case version, arm version, configuration, model/tool versions, evaluator versions, random seeds where applicable, and timestamps.
2. **Metric specification:** every metric needs a deterministic definition or a documented human-rating rubric; no unnamed composite score.
3. **Human evaluation protocol:** outputs should be blinded/randomized where feasible and reviewer identity/versioning retained; disagreement should be recorded rather than averaged away silently.
4. **Repetition / variance:** non-deterministic arms should support repeated runs so variance is observable.
5. **Reporting:** produce per-case and aggregate results, not only a leaderboard; include failure examples and confidence/uncertainty around comparisons when sample size permits.

## GenSigma-specific implications

GenSigma does **not** need a novel benchmark science stack. It needs a domain-specific application of established evaluation discipline to executive decisions.

The unique part is the **decision case**, not the evaluation mechanics:

```text
frozen historical business context
+ time-correct evidence
+ governed decision trace
+ multiple cognition arms
+ business-specific correctness / judgment metrics
```

The harness should therefore be implemented as a small reproducible evaluation framework, not as another reasoning architecture.

## Recommendation

Proceed to implementation of the benchmark harness infrastructure now.

The following are `LOCAL_SOLVE` and can be built before the Chief Architect resolves the cognition architecture:

- frozen-case manifest/schema;
- evaluation-run manifest;
- baseline-arm interface;
- LLM-only baseline;
- static-scorecard baseline;
- scoring/evaluation framework;
- forecast scoring utilities;
- blind human-review packet generation;
- reproducibility/report generation.

The **modular routed cognition arm** remains `BLOCKED_BY_ARCH_REQUEST` until `ADRQ-ECR-001` is resolved.

## Architecture impact

`LOCAL_SOLVE` for benchmark mechanics.  
`ASK_ARCHITECT` remains open only for the candidate Decision Engine architecture and any shared semantic contracts.