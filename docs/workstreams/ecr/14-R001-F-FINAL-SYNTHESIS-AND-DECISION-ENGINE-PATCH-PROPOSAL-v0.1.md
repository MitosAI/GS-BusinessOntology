# R001-F — Final Synthesis and Decision Engine Patch Proposal

**Status:** Research program synthesis complete; architecture changes remain proposals pending `ASK_ARCHITECT` resolution.

**Owner:** ECR-001 — Executive Cognition Research Lead

---

## 1. Executive conclusion

GenSigma should not build executive cognition as a universal LLM prompt, a single optimization model, or a monolithic Bayesian system.

The strongest research-backed design is a **governed portfolio of decision methods** operating over one common decision trace and selected by decision class, stakes, uncertainty structure, reversibility, strategic interaction, and authority.

The working hypothesis remains:

```text
BUSINESS INTENT
BUSINESS REALITY
EXTERNAL REALITY
CAPABILITY
POLICY / AUTHORITY / SECURITY
          |
          v
SITUATION BUILDER
          |
          v
DECISION CLASS + STAKES + REVERSIBILITY + AUTHORITY
          |
          v
DETERMINISTIC GATES
          |
          v
METHOD ROUTER
          |
          +--> probability / Bayesian reasoning
          +--> optimization
          +--> scenario / simulation
          +--> causal / intervention reasoning
          +--> strategic interaction / bargaining
          +--> real-options / staged commitment
          +--> structured qualitative judgment
          +--> LLM interpretation / generation / orchestration
          |
          v
VOI / TIMING + SENSITIVITY + DEBIAS + COUNTERARGUMENT
          |
          v
AUDITABLE RECOMMENDATION
          |
          v
DECISION / APPROVAL / DELEGATED AUTHORITY
          |
          v
GOVERNED ACTION
          |
          v
OUTCOME / VERIFICATION
          |
          v
CALIBRATION / LEARNING / CHANGE PROPOSAL
```

**One common decision anatomy. Multiple computational methods. Explicit method selection. Governed authority. Measured learning.**

---

## 2. What Research 001 establishes

### 2.1 There is no universal executive-decision algorithm

Different decision classes require different method profiles.

- Eligibility and policy checks -> deterministic rules.
- Resource allocation -> optimization where objectives/constraints are formalizable.
- Repeated uncertain events -> probability/Bayes where calibration is defensible.
- Novel structural uncertainty -> scenarios and sensitivity rather than fake probability.
- Adaptive counterparties -> selective game/bargaining reasoning.
- Intervention decisions -> causal reasoning, not prediction alone.
- Irreversible uncertain commitments -> staged commitment / real-options thinking.
- Unstructured evidence and alternative generation -> LLM assistance.
- High-stakes value tradeoffs -> governed human authority unless explicitly delegated.

### 2.2 Deterministic before probabilistic

Known rules, arithmetic, permissions, deadlines, authority, and enforceable constraints should not be turned into probabilistic reasoning problems.

### 2.3 Probability must be earned

Use numeric probability only when the evidence/model supports it. Preserve qualitative uncertainty otherwise.

### 2.4 Prediction is not intervention

A model that predicts an outcome does not automatically estimate what will happen if GenSigma takes an action. Causal claims require explicit assumptions, experiments, or defensible identification.

### 2.5 Timing is part of judgment

The engine must ask not only `what should we do?` but also `should we decide now, gather information, stage the commitment, or preserve an option?`

### 2.6 Authority is part of cognition

A recommendation cannot be separated from who may decide, approve, execute, or escalate it. AI autonomy should be decision-class and risk scoped, not global.

### 2.7 Decision quality is distinct from outcome quality

The system must preserve the ex-ante evidence, assumptions, alternatives, forecast, recommendation, and authority context. Outcomes must be evaluated without hindsight contamination.

### 2.8 Learning must be typed and governed

An outcome may justify updating a statistic without justifying a strategy change. Learning should produce progressively governed updates, not uncontrolled mutation of Business Intent or policy.

---

## 3. Common decision anatomy — proposed logical contract

A material decision context should be able to express:

### Framing
- decision type/class;
- trigger/question;
- scope;
- horizon/deadline;
- stakes;
- reversibility;
- recurrence.

### Evaluation frame
- applicable Business Intent;
- objectives/criteria;
- constraints;
- policy;
- risk posture;
- authority/delegation.

### Situation
- Business Reality snapshot;
- External Reality;
- Capability;
- evidence and provenance;
- claims/contradictions;
- assumptions;
- unknowns.

### Uncertainty
At least conceptually distinguish:
- fact uncertainty;
- identity/context uncertainty;
- model uncertainty;
- parameter/probability uncertainty;
- forecast uncertainty;
- capability/execution uncertainty;
- strategic-response uncertainty;
- preference/criterion uncertainty;
- causal uncertainty.

### Alternatives
- status quo;
- candidate alternatives;
- staged/contingent alternatives where relevant;
- provenance of alternative generation.

### Analysis
- method(s) selected;
- why selected;
- model/rule/solver versions;
- calculations;
- scenarios;
- forecasts;
- causal assumptions;
- strategic response;
- value of information;
- timing/staging;
- sensitivity.

### Recommendation
- recommended alternative;
- rationale;
- key assumptions;
- material uncertainty;
- reversal conditions;
- missing information worth obtaining;
- required approval/escalation.

### Learning contract
- ex-ante expected outcomes;
- review/resolution horizon;
- actual outcome;
- execution variance;
- forecast score where applicable;
- decision-process review;
- learning/change proposal.

This is a logical research contract. ECR does **not** claim each item should become a standalone ontology object.

---

## 4. Decision adequacy

Research 001 proposes four practical levels:

```text
L0 — deterministic operational rule
L1 — structured choice
L2 — analytical decision under uncertainty
L3 — strategic / novel judgment
```

The level should influence method depth, audit requirements, human authority, and expected latency/cost.

---

## 5. Probability adequacy

```text
P0 — unknown / not quantified
P1 — qualitative or ordered likelihood
P2 — empirical / reference-class estimate
P3 — calibrated model or defensible posterior
```

**Rule:** downstream components must not coerce P0/P1 into fake numeric probability.

---

## 6. Causal adequacy

Research 001 proposes a parallel research construct:

```text
C0 — association only
C1 — causal hypothesis with explicit assumptions
C2 — observational causal estimate with defensible identification strategy
C3 — experimental / quasi-experimental or otherwise strongly identified causal evidence
```

Use this to prevent predictive models from silently becoming intervention models.

Whether this construct becomes shared architecture is an `ASK_ARCHITECT` matter.

---

## 7. Method-routing policy — proposed

```text
1. Apply hard policy / authority / feasibility gates.
2. Classify decision type, stakes, reversibility, recurrence and uncertainty.
3. Determine whether a formal objective + constraints exist.
4. Determine whether probability is defensible.
5. Determine whether causal intervention reasoning is required.
6. Determine whether other actors adapt strategically.
7. Determine whether delay/staging has option value.
8. Route to one or more analytical modules.
9. Challenge with sensitivity, counterargument and behavioral debiasing.
10. Compose recommendation with uncertainty and reversal conditions.
11. Check authority envelope before decision/action.
12. Preserve ex-ante trace.
13. Verify outcome and update only the appropriate learning layer.
```

---

## 8. Proposed Decision Engine specification patch

ECR recommends the Chief Architect consider the following changes to `docs/specs/03-DECISION-ENGINE-AND-CAPABILITY-MODEL-SPEC-v0.1.md`.

### Patch A — Method routing
Add an explicit concept that decision classes invoke different analytical methods rather than treating all available methods as an undifferentiated toolkit.

### Patch B — Probability adequacy
Add P0-P3 or an equivalent mechanism preventing fabricated numeric probability.

### Patch C — Multidimensional uncertainty
Replace or supplement a generic confidence field with typed uncertainty where material.

### Patch D — Causal versus predictive claims
Require the trace to distinguish forecast/prediction from claims about intervention effects.

### Patch E — Decision timing / VOI
Permit a recommendation to be `gather evidence`, `wait`, `experiment`, or `stage commitment`, not only select a final business alternative.

### Patch F — Staged alternatives
Allow contingent/staged decision paths where irreversibility and information arrival make them decision-relevant.

### Patch G — Ex-ante expectation preservation
Require material forecasts/expectations to be preserved before action for later scoring and learning.

### Patch H — Reversal conditions
Recommendations should identify material assumptions, evidence changes, or thresholds that would change the recommendation.

### Patch I — Decision-method provenance
Preserve methods/models/rules/solver versions used to produce a recommendation.

### Patch J — Authority envelope
Evaluate whether the deciding actor/agent is delegated for the decision class/stakes/risk before allowing autonomous decision/action.

### Patch K — Forecast registry / calibration loop
Provide a durable path for forecasts to resolve and be scored over time.

### Patch L — Governed learning proposals
Learning should distinguish parameter updates from heuristic/policy/model/Intent change and govern them differently.

None of these patches should be applied to shared architecture without Chief Architect resolution.

---

## 9. First formal prototype recommendation

### Primary: Bid / No-Bid

This remains the best first executive-cognition benchmark because it exercises:
- Business Intent;
- Business Reality;
- External Reality;
- Capability;
- hard constraints;
- uncertainty;
- partner/customer strategic factors;
- optional probability;
- decision timing;
- human authority;
- observable outcome.

### Contrast: Staffing / Resource Assignment

This is deliberately different because formal optimization should play a larger role.

The pair tests whether the architecture is genuinely modular rather than a disguised universal prompt.

---

## 10. Benchmark requirement

The system should be compared on frozen historical cases across:

1. reconstructed human decision;
2. LLM-only baseline;
3. static weighted scorecard;
4. modular routed architecture;
5. specialist quantitative baseline where relevant.

Measure:
- constraint/policy errors;
- evidence completeness;
- factual support;
- alternative quality;
- method appropriateness;
- probability/causal honesty;
- sensitivity/reversal transparency;
- auditability;
- human reviewer preference;
- latency/cost;
- calibration after sufficient cases;
- outcome separately from ex-ante process quality.

Do not validate the architecture on one showcase case.

---

## 11. LLM role — final Research 001 position

LLMs are strongly suited to:
- interpret unstructured evidence;
- summarize context;
- generate hypotheses and alternatives;
- identify missing evidence;
- translate natural language into structured analytical inputs;
- simulate stakeholder arguments;
- critique recommendations;
- explain results;
- orchestrate tools.

LLMs should not silently own:
- canonical truth;
- source authority;
- permissions/security;
- arithmetic;
- optimization guarantees;
- probability calibration by assertion;
- causal identification by rhetoric;
- policy mutation;
- high-impact final authority outside delegation.

**Final hypothesis:** LLMs are a reasoning/orchestration component inside the Decision Engine, not the Decision Engine itself.

---

## 12. Architecture decisions still required

The following remain `ASK_ARCHITECT`:

1. Adopt / reject / modify the **Hierarchical Policy Portfolio** as the working Decision Engine architecture.
2. Approve which proposed shared semantics belong in the Decision Engine / ontology contracts:
   - probability adequacy;
   - multidimensional uncertainty;
   - causal-vs-predictive distinction;
   - ex-ante expectations;
   - reversal conditions;
   - method provenance;
   - staged alternatives / decision timing;
   - authority envelope integration;
   - governed learning proposals.
3. Formally designate the first prototype decision class(es).
4. Decide whether any proposed logical constructs require new canonical resources or remain attributes/relationships/trace structures.

Until resolved, ECR treats these as proposals and does not edit canonical shared specs.

---

## 13. Research 001 completion state

Research 001's foundational research objective is now satisfied sufficiently to move into architecture selection and empirical prototyping.

Completed durable outputs include:
- discipline/source map;
- decision anatomy;
- decision-class pressure test;
- deterministic/probabilistic boundary;
- candidate cognition architectures;
- first-session handoff;
- causal decision reasoning;
- value of information/stopping rules;
- real options/staged commitment;
- forecast calibration/reference classes;
- delegated decision rights;
- learning/update discipline;
- cognition benchmark harness;
- this final synthesis / R001-F patch proposal.

Further literature research should now be **question-driven**, not open-ended. The highest-value next work is an architecture decision plus a bounded benchmark prototype.

---

## 14. Final ECR recommendation

Do not spend another cycle expanding the literature map before testing.

The program should now:

```text
CHIEF ARCHITECT RESOLVES ARCHITECTURE GATE
        |
        v
PATCH SHARED DECISION ENGINE SPEC
        |
        v
BUILD BID/NO-BID BENCHMARK FIXTURES
        |
        v
IMPLEMENT 4 BASELINES
        |
        v
RUN BLIND / REPEATABLE EVALUATION
        |
        v
KEEP / MODIFY / REJECT COGNITION ARCHITECTURE
```

The research has reached the point where **empirical architecture evidence is more valuable than additional broad reading**.
