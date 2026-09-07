# R001 — Executive Cognition Benchmark Harness

**Status:** Research output; ready to inform prototype design. Architecture-sensitive integration remains subject to ASK_ARCHITECT.

## Purpose

GenSigma should not claim an executive-cognition architecture is better because its outputs sound intelligent. It needs repeatable evaluation against realistic decisions.

The benchmark harness should compare methods on identical frozen decision contexts.

## First benchmark class

**Recommended primary class:** Bid / No-Bid.

Reasons:
- repeated enough to accumulate cases;
- economically meaningful;
- directly aligned to RFP-to-Cash;
- combines hard constraints, uncertainty, judgment, capability, and external factors;
- historical artifacts permit replay;
- human executives can review output quality.

**Contrast class:** Staffing / Resource Assignment, because it contains a more formal optimization core.

## Evaluation arms

For each case, compare:

1. **Human historical decision** — reconstructed where evidence permits.
2. **LLM-only** — unstructured reasoning from the same allowed evidence.
3. **Static scorecard** — fixed weighted criteria.
4. **Modular cognition architecture** — deterministic gates + routed methods + challenge/sensitivity + governed recommendation.
5. **Optional specialist baseline** — optimization or statistical model where appropriate.

## Frozen-case protocol

Each case must define an `as-of` time. Only evidence actually available by that time may be supplied.

```text
CASE
- decision question
- as-of timestamp
- business intent applicable then
- business reality then
- external evidence then
- capability then
- policy/authority then
- known uncertainties
- later outcome withheld until scoring
```

This prevents hindsight leakage.

## Scoring dimensions

### A. Correctness / compliance
- hard-constraint violations;
- policy/authority violations;
- arithmetic errors;
- unsupported factual claims.

### B. Evidence use
- material evidence coverage;
- provenance traceability;
- treatment of contradictions;
- explicit unknowns.

### C. Decision framing
- correct decision class;
- stakes/reversibility recognition;
- objective/criteria alignment;
- status-quo alternative present where relevant.

### D. Alternatives
- breadth and relevance;
- staged alternatives where applicable;
- no obviously dominated options presented as peers.

### E. Method quality
- method appropriate to decision class;
- no fake precision;
- probability adequacy respected;
- optimization used only when formalization is defensible;
- causal claims distinguished from prediction.

### F. Recommendation quality
- clear recommendation;
- rationale;
- assumptions;
- uncertainty;
- reversal/sensitivity conditions;
- decision timing / VOI where material.

### G. Auditability
- method/model provenance;
- reproducibility;
- explicit inputs;
- clear human review path.

### H. Operational metrics
- latency;
- compute/tool cost;
- human review time;
- failure/retry rate.

### I. Forecast metrics
Where probabilities are legitimately produced:
- Brier score for binary outcomes;
- calibration by bins/reference classes after enough cases;
- sharpness/discrimination alongside calibration.

## Outcome use

Outcome is deliberately **not** the sole benchmark.

A good decision can have a bad outcome; a bad process can get lucky. The harness should therefore maintain separate:
- ex-ante process score;
- forecast score;
- execution score;
- ex-post outcome.

## Human review protocol

Prefer blind review where feasible. Reviewers should score outputs without knowing which system produced them.

Suggested dimensions:
- would you trust this analysis?
- what material evidence is missing?
- are the alternatives adequate?
- is the recommendation actionable?
- are uncertainty and assumptions honest?
- would this improve the real executive process?

## Acceptance target for first prototype

The modular architecture should not move toward production unless it demonstrates meaningful improvement over LLM-only and static-scorecard baselines on several dimensions, particularly:
- fewer constraint/policy errors;
- better evidence completeness;
- stronger uncertainty honesty;
- superior auditability;
- equal or better human preference;
- acceptable latency/cost.

A single decision case cannot validate the architecture.

## Data fixture strategy

Start with 10–20 historical cases if available, not one showcase example. Cases should deliberately vary:
- win/loss;
- strong/weak relationship;
- high/low capability;
- hard eligibility constraints;
- partner dependence;
- deadline pressure;
- incomplete evidence;
- false-positive attractive opportunities.

The SFO/CRI episode may be one fixture but must not define the benchmark universe.

## Experiment decision rule

The benchmark is intended to produce evidence for Chief Architect decision, not merely demos. If architecture alternatives remain close, extend the case set or run a bounded targeted experiment rather than choosing by aesthetics.
