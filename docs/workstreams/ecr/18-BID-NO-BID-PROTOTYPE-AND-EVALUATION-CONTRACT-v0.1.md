# Bid / No-Bid Prototype and Evaluation Contract v0.1

**Status:** READY for benchmark implementation  
**Owner:** ECR-001 - Executive Cognition Research  
**Architecture basis:** ADR-003 Hierarchical Policy Portfolio  
**Input contract:** R001 DecisionContext Seam Contract v0.1  
**Benchmark basis:** R001 cognition harness and benchmark-practice validation

## 1. Experiment question

Does deterministic gating plus decision-class method routing produce materially better Bid/No-Bid recommendations than an LLM-only arm and a static weighted-scorecard arm on identical frozen cases, at acceptable cost and latency?

This is an architecture-validation experiment, not a production Decision Engine.

## 2. Evidence basis

Established findings used here:

- Bid/No-Bid is multi-attribute and context-dependent. Published decision-support work emphasizes explicit attributes, aspiration levels, assumptions, and decision documentation. Quantitative scorecards are credible baselines, but weights and thresholds vary across firms and markets.
- Proper scoring rules are required to evaluate probabilistic forecasts and incentivize honest probability reporting. Calibration claims require resolved forecasts and adequate samples.
- Staffing is structurally different: published models jointly schedule tasks and assign multi-skilled workers using integer or mixed-integer optimization, supporting its use as ADR-003's contrast class.
- NIST benchmark guidance emphasizes defined objectives, validity, transparent implementation, reproducibility, and reporting. HELM likewise supports common scenarios and multiple metrics rather than one opaque score.

GenSigma hypothesis to test, not assume: a governed routed architecture should reduce critical errors and improve uncertainty handling and auditability without sacrificing actionability.

Primary sources:

- I. Ahmad, "Decision-Support System for Modeling Bid/No-Bid Decision Problem," ASCE JCEM 116(4), 1990, https://doi.org/10.1061/(ASCE)0733-9364(1990)116:4(595)
- M. L. Chisala, "Quantitative Bid or No-Bid Decision-Support Model for Contractors," ASCE JCEM 143(12), 2017, https://doi.org/10.1061/(ASCE)CO.1943-7862.0001407
- T. Gneiting and A. E. Raftery, "Strictly Proper Scoring Rules, Prediction, and Estimation," JASA 102(477), 2007, https://doi.org/10.1198/016214506000001437
- V. Fernandez-Viagas and J. M. Framinan, "Integrated Project Scheduling and Staff Assignment with Controllable Processing Times," 2014, https://doi.org/10.1155/2014/924120
- NIST AI 800-2 draft overview, 2026, https://www.nist.gov/news-events/news/2026/01/towards-best-practices-automated-benchmark-evaluations
- Stanford CRFM HELM, https://crfm.stanford.edu/helm/

## 3. Frozen input

Every case supplies one immutable DecisionContext projection with:

- explicit `state_as_of` and `knowledge_as_of`;
- decision question and scope;
- Business Intent, Business Reality, External Reality, Capability, policy/authority, available-action, evidence, and history sections;
- explicit unknown, ambiguous, contradicted, partial, and security-filtered states;
- outcome and post-boundary evidence structurally withheld.

All arms receive semantically equivalent input. Arm-specific preprocessing is versioned in the run manifest.

## 4. Recommendation vocabulary

The arm returns exactly one primary disposition:

```text
BID
NO_BID
CONDITIONAL_BID
DEFER_GATHER_EVIDENCE
ESCALATE_AUTHORITY
INVALID_OR_INSUFFICIENT_CONTEXT
```

`CONDITIONAL_BID` requires machine-readable conditions and a deadline. `DEFER_GATHER_EVIDENCE` requires a bounded information request, expected decision relevance, and latest useful decision time. `ESCALATE_AUTHORITY` means the recommendation is outside the current actor's authority envelope.

## 5. Deterministic gates

The routed arm evaluates fixture-supplied hard conditions before compensatory scoring or LLM judgment:

1. submission deadline and minimum preparation time;
2. mandatory eligibility, registration, certification, clearance, or contract-vehicle access;
3. legal/compliance prohibitions and unacceptable mandatory terms;
4. minimum delivery feasibility/capacity explicitly defined by policy;
5. bid authority and required approval;
6. mandatory partner or subcontractor commitments;
7. explicit financial and risk limits.

Each gate emits `pass | fail | unknown | not_applicable`, rule/version/basis, evidence references, and whether it blocks BID. Unknown is never silently treated as pass. Policy determines whether unknown blocks, escalates, or triggers information gathering.

## 6. Decision criteria

After gates, the arm assesses:

- strategic and offering alignment;
- customer access and relationship quality;
- problem and solution fit;
- capability and delivery feasibility;
- staffing capacity and opportunity cost;
- economics, bid cost, margin potential, and downside;
- competitive position and win likelihood;
- contract, compliance, and delivery risk;
- partner dependence;
- timing, staging, and value of information.

Criteria remain separate dimensions by default. Vetoes and severe downside cannot be hidden inside a compensatory score.

## 7. Method routing

Required routing policy:

1. Deterministic rules handle gates, authority, arithmetic, deadlines, and explicit feasibility.
2. Structured qualitative/MCDA analysis handles remaining criteria.
3. Probability/Bayesian or reference-class analysis runs only for P2/P3 quantities with documented basis.
4. Scenario and sensitivity analysis handles P0/P1, model uncertainty, and material parameter ranges.
5. Expected-value/downside analysis runs only when probability and consequence inputs are adequate.
6. Strategic-response analysis runs when customer, partner, or competitor adaptation is material.
7. VOI/timing analysis runs when obtainable evidence could reverse the decision before the deadline.
8. LLM support is limited to evidence synthesis, contradiction surfacing, alternative generation, counterargument, and explanation.
9. Authority is checked before declaring a recommendation executable.

Every invoked or skipped module records its reason and version.

## 8. Probability adequacy

```text
P0 unknown/unquantified       -> numeric probability forbidden
P1 qualitative/ordered        -> numeric probability forbidden
P2 empirical/reference class  -> numeric allowed with population, sample, window, and source
P3 calibrated model/posterior -> numeric allowed with model/version and calibration/posterior basis
```

The arm must be able to recommend without a numeric win probability. Numeric output without the required basis is a critical defect.

Legitimate binary forecasts retain the raw `probability, outcome, forecast_time, model/basis version` tuple and are scored with Brier score. No calibration conclusion is made from the pilot case count alone.

## 9. Output contract

```yaml
disposition: BID | NO_BID | CONDITIONAL_BID | DEFER_GATHER_EVIDENCE | ESCALATE_AUTHORITY | INVALID_OR_INSUFFICIENT_CONTEXT
executability: executable | approval_required | blocked | unknown
gate_results: []
criteria_assessments: []
selected_methods: []
skipped_methods: []
recommendation_rationale: string
material_claims: []
uncertainties: []
assumptions: []
contradictions: []
alternatives_considered: []
expected_outcomes: []
reversal_conditions: []
information_actions: []
required_approvals: []
causal_claims: []
run_provenance: {}
```

Material factual claims require evidence references or an explicit assumption/inference label. Causal claims require an explicit causal basis and cannot be inferred from prediction alone.

## 10. Evaluation arms

Required arms:

1. reconstructed historical human decision, when evidence permits;
2. LLM-only;
3. static weighted scorecard;
4. routed modular cognition.

An optional specialist quantitative/reference-class baseline may be added where data permits. All arms use the same frozen case and common benchmark interface.

## 11. Metrics

Critical defects:

- hindsight leakage;
- hard-constraint violations;
- policy/authority violations;
- fabricated numeric probabilities;
- unsupported material claims;
- unlabeled causal-intervention claims;
- missing method/model/rule provenance.

Five-point anchored human rubric:

- evidence coverage and traceability;
- framing and alternative quality;
- method appropriateness;
- uncertainty honesty;
- reversal/sensitivity usefulness;
- auditability;
- actionability and trust.

Operational metrics: latency, model/tool cost, human review time, failure/retry rate, and invoked-module count. Forecast metrics: Brier score and raw probability/outcome pairs; calibration and sharpness only after a separately documented minimum-sample rule.

No default single composite intelligence score.

## 12. Pre-registered pilot decision rule

The routed arm passes the first architecture gate only if all conditions hold:

1. zero hindsight leakage;
2. zero fabricated numeric probabilities;
3. zero executable BID recommendations violating a known blocking gate or authority rule;
4. method/rule/model provenance for every run;
5. material-claim evidence coverage at least 95%, with exceptions explicitly labeled assumption/inference;
6. blind reviewers prefer or tie the routed arm against the stronger simple baseline in at least 65% of valid pairwise comparisons;
7. mean paired uncertainty-honesty and auditability ratings improve by at least 0.5 on the five-point rubric versus LLM-only, without actionability falling more than 0.25;
8. median cost is no more than 3x and P95 latency no more than 4x LLM-only, unless Chief Architect review accepts a documented larger quality gain;
9. at least ten valid varied historical cases exist before any architecture-strengthening claim.

These are pre-observation pilot hypotheses, not production service objectives. Failure means modify or reject the routed implementation, not tune thresholds after observing results.

## 13. Synthetic fixture matrix

At minimum:

1. attractive case failing mandatory eligibility;
2. strategically aligned, feasible, evidence-rich BID;
3. weak capability with high partner dependence;
4. P0/P1 win uncertainty where numeric probability is forbidden;
5. P2 reference-class case with legitimate numeric forecast;
6. contradictory customer/relationship evidence;
7. evidence acquisition that can reverse the decision before deadline;
8. authority-insufficient case requiring escalation;
9. high apparent value with unacceptable downside/terms;
10. conditional bid unlocked by a partner or staffing commitment.

Two fixtures must appear similarly attractive in narrative form but route differently because gates, uncertainty adequacy, or reversibility differ.

## 14. Dependencies and non-scope

Dependencies: #11 benchmark contracts, #12 leakage guard, #13 common arm and baselines, #14 scoring, #15 review/reporting, #19 historical case pack, and #20 routed arm.

Non-scope:

- production autonomous bid decisions;
- source ingestion redesign;
- canonical schema changes;
- permanent scorecard weights;
- permanent model/provider/solver selection;
- staffing optimizer implementation;
- tuning on held-out outcomes.

## 15. Contrast experiment

After the Bid/No-Bid harness works, instantiate the same common anatomy for Staffing / Resource Assignment. It should route to explicit assignment/scheduling optimization with skills, availability, precedence, workload, continuity, cost, and risk constraints. If both classes reduce to the same prompt or scorecard path, ADR-003's routing hypothesis has failed its intended contrast test.
