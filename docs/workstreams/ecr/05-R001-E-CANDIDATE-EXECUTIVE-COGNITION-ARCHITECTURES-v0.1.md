# R001-E — Candidate Executive Cognition Architectures

**Version:** v0.1  
**Status:** First-session architecture hypotheses for Chief Architect review  
**Owner:** Executive Cognition Research Lead (ECR-001)

---

## 1. Purpose

This artifact converts the first-session discipline map, decision anatomy, decision-class pressure test, and deterministic/probabilistic boundary into candidate architectures.

These are **research proposals, not canonical architecture changes**. The Chief Architect owns reconciliation into the program architecture and Decision Engine specification.

---

## 2. Evaluation criteria

Each option is evaluated against the Research 001 criteria:

- decision quality;
- calibration under uncertainty;
- explainability/auditability;
- consistency;
- computational feasibility;
- robustness to missing/contradictory evidence;
- resistance to known bias;
- strategic-interaction capability;
- hard-constraint enforcement;
- outcome learning;
- compatibility with the operational ontology/kinetic spine;
- human governance;
- implementation/testability.

---

## 3. Option A — Universal deliberation pipeline

### Shape

```text
Situation
  -> Alternatives
  -> Score / Utility
  -> Recommendation
  -> Decision
```

One generic pipeline is applied to all decision classes, with a common scoring/evaluation mechanism and optional LLM assistance.

### Strengths

- simple conceptual model;
- easy to explain;
- common audit shape;
- low initial engineering complexity.

### Weaknesses

- assumes more commonality across decision classes than the pressure test supports;
- tends to force incomparable decisions into weighted scores;
- weak fit for formal assignment/scheduling optimization;
- weak fit for strategic bargaining;
- encourages invented probabilities or weights;
- risks becoming an LLM prompt chain with a scorecard attached.

### Assessment

**Not recommended as the primary architecture.** A common trace/anatomy is useful; a common decision algorithm is not.

---

## 4. Option B — Decision-class policy portfolio / method router

### Shape

```text
DECISION TRIGGER
      |
      v
BUILD GOVERNED SITUATION
      |
      v
CLASSIFY DECISION + STAKES + AUTHORITY
      |
      v
DETERMINISTIC GATES
      |
      v
METHOD ROUTER
      |
      +--> rules / policy
      +--> probability / Bayesian model
      +--> optimization / solver
      +--> scenario / simulation
      +--> strategic interaction / bargaining
      +--> structured qualitative judgment
      +--> LLM interpretation / alternative generation / synthesis
      |
      v
SENSITIVITY + CHALLENGE
      |
      v
RECOMMENDATION
      |
      v
DECISION / APPROVAL
      |
      v
GOVERNED ACTION
```

### Strengths

- matches the empirical pressure test across GenSigma decision classes;
- avoids forcing mathematical methods where assumptions are weak;
- lets deterministic software own deterministic work;
- makes method choice explicit and auditable;
- permits decision-class-specific benchmarks;
- allows progressive automation without redesigning the whole engine.

### Weaknesses

- requires routing policy design and governance;
- more engineering modules/integration points;
- risk of inconsistent behavior if decision classes and methods proliferate;
- requires explicit versioning of routing policies and analytical models.

### Assessment

**Recommended core architecture hypothesis.** This appears strongest as the central execution architecture.

---

## 5. Option C — Hierarchical executive-control architecture

### Shape

```text
SLOW GOVERNED LAYER
Business Intent / risk appetite / policy / strategic beliefs
             |
             v
DECISION POLICIES + AUTHORITY ENVELOPES
             |
             v
FASTER DECISION-CLASS LOOPS
commercial / delivery / finance / workforce / compliance
             |
             v
GOVERNED ACTION
             |
             v
OUTCOME / FEEDBACK
             |
             +----> policy/model review triggers
```

This architecture emphasizes different decision tempos. Strategic policy changes slowly; operational decisions execute quickly inside approved boundaries.

### Strengths

- strongly aligned with control theory, OODA/mission-command concepts, and existing GenSigma distinction between deliberate Intent and faster operational state;
- supports delegated agent authority without granting global autonomy;
- reduces repeated executive review for routine choices;
- creates clear escalation when local policy is insufficient.

### Weaknesses

- does not itself specify how a local decision is analytically solved;
- danger of overusing control-system metaphors;
- requires careful policy/version/authority semantics.

### Assessment

**Recommended as a complementary architecture dimension, not a substitute for Option B.**

---

## 6. Recommended synthesis — Hierarchical policy portfolio

The strongest provisional synthesis combines B and C.

```text
                GOVERNANCE / SECURITY / AUTHORITY
                              |
                              v
                    BUSINESS INTENT
          strategy | objectives | risk | policy
                              |
                              v
                 DECISION POLICY LAYER
       decision classes | routing | authority envelopes
                              |
                              v
+-------------------------------------------------------------+
|                  EXECUTIVE JUDGMENT RUNTIME                 |
|                                                             |
|  1. Build situation                                         |
|  2. Apply hard gates                                        |
|  3. Generate/retrieve alternatives                          |
|  4. Route analytical methods                                |
|     - probability/Bayes where defensible                    |
|     - optimization where formalizable                       |
|     - scenario/simulation where structural uncertainty      |
|     - strategic interaction where adaptive actors matter    |
|     - structured qualitative judgment otherwise             |
|     - LLM interpretation/orchestration across modules       |
|  5. Sensitivity / debias / counterargument                  |
|  6. Produce auditable recommendation                        |
+-------------------------------------------------------------+
                              |
                              v
                    DECISION / APPROVAL
                              |
                              v
                     GOVERNED ACTION
                              |
                              v
                    OUTCOME / LEARNING
                              |
                              v
          MODEL / POLICY / INTENT CHANGE PROPOSALS
```

---

## 7. Six architectural components implied by the synthesis

### 7.1 Situation Builder

Purpose: construct the decision-relevant slice of Business Reality, External Reality, Capability, Intent, evidence, assumptions, policy and authority.

It should not create new canonical truth merely to answer a decision.

### 7.2 Decision Classifier and Policy Router

Purpose: identify decision class, stakes, reversibility, time horizon, probability adequacy, strategic-interaction materiality, available authority, and required methods.

The router should be explicit/versioned/testable rather than hidden inside an LLM prompt.

### 7.3 Analytical Module Registry

Purpose: expose named analytical capabilities with contracts and provenance, for example:

```text
EligibilityRuleSet
WinProbabilityModel
PartnerEvaluationModel
AssignmentOptimizer
PricingScenarioModel
CollectionsRiskModel
BargainingAnalysis
ScenarioGenerator
ReferenceClassRetriever
```

A model output should record model/version/input snapshot and limitations where material.

### 7.4 Deliberation / Challenge Layer

Purpose: improve robustness by testing:

- missing alternatives;
- decisive assumptions;
- base rates/reference classes;
- sensitivity and reversal conditions;
- contradictory evidence;
- premortem / failure modes;
- counterparty response;
- whether numeric precision is justified.

LLMs can contribute strongly here, but durable outputs should be explicit artifacts/claims rather than opaque internal reasoning.

### 7.5 Recommendation Composer

Purpose: combine formal and qualitative outputs into the governed recommendation contract:

- recommended alternative;
- rationale;
- decisive evidence;
- criteria/Intent served;
- assumptions;
- uncertainty;
- sensitivity/reversal conditions;
- alternatives rejected;
- approval/action requirements.

### 7.6 Outcome Evaluator / Learning Proposer

Purpose: compare ex-ante expectations with outcomes, score forecasts where possible, diagnose model/process/execution error, and propose—not silently enact—changes to models, policy or Intent.

---

## 8. Architecture invariants proposed for Chief Architect review

1. **One trace, multiple methods.** Decisions should share auditable anatomy while methods vary by decision class.
2. **Deterministic before probabilistic.** Do not ask AI to reason about facts/rules software can evaluate exactly.
3. **Probability is earned.** Numeric uncertainty requires explicit adequacy/provenance.
4. **Method selection is explicit.** Analytical routing must be inspectable and testable.
5. **LLM is a governed cognitive component, not the Decision Engine.**
6. **Intent is not learned implicitly from behavior.** Approved organizational preference remains governed.
7. **Authority envelopes govern autonomy.** Agents may decide only within explicitly delegated decision/action scope.
8. **Outcome does not equal decision quality.** Learning preserves ex-ante state and expectations.
9. **Strategic belief/policy changes occur on a slower governed loop.** Operational outcomes may propose changes but not silently mutate them.
10. **No new parallel semantic architecture.** The runtime reads/writes through existing ontology/evidence/action semantics.

---

## 9. What this proposal does not decide

This artifact intentionally does **not** decide:

- physical persistence;
- an agent framework;
- a specific LLM/model vendor;
- exact probability representation storage;
- whether a `DecisionCase` object exists;
- exact routing implementation;
- exact model registry technology;
- whether individual analytical modules are services, functions, libraries or agents;
- the degree of autonomous authority for any real decision class.

Those are downstream architecture/implementation decisions after semantic and benchmark requirements are reconciled.

---

## 10. First prototype implication

For `bid/no-bid`, the candidate runtime becomes:

```text
Opportunity trigger
 -> Situation Builder
 -> eligibility/deadline gates
 -> Intent + criteria retrieval
 -> Capability fit
 -> alternative set: BID / NO-BID / PARTNER / WATCH / CONDITIONAL BID
 -> win/reference-class model if probability adequate
 -> pursuit cost/economics
 -> strategic-fit multi-criteria evaluation
 -> scenario/sensitivity
 -> challenge missing evidence / assumptions
 -> recommendation
 -> founder/delegated approval
 -> typed next action
 -> outcome tracking
```

The prototype should be benchmarked against:

1. unstructured LLM-only recommendation;
2. simple static weighted scorecard;
3. historical human decision where reconstructable;
4. the modular architecture above.

The goal is not to prove “AI beats VJ” from one case. The goal is to test whether the modular architecture produces more complete, consistent, auditable and appropriately calibrated decisions.
