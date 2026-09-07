# Executive Cognition Research — First Session Handoff

**Version:** v0.1  
**Status:** Ready for first integration gate  
**Owner:** Executive Cognition Research Lead (ECR-001)  
**Research program:** RESEARCH-001 — Computational Executive Judgment

---

## 1. What is now established

### Repository/governance baseline

The workstream has read the governing Constitution, program brief, operating architecture, roadmap, starter pack, foundation specifications, ECR role charter, and Research 001 charter before producing material work.

The workstream also reconciled against the latest Knowledge & Ontology Engineering direction on `workstream/koe-first-session-v0.1`:

- `World Model` is legacy terminology;
- current architecture uses Business Intent, Business Reality, External Reality, Capability, Executive Judgment, Governed Action, and Outcome/Learning;
- current V1 business-object guidance is approximately 30–40 objects;
- the current Business Reality candidate catalog contains 37 objects;
- Executive Judgment methods must not become a parallel semantic system.

### Research conclusions supported strongly enough for the first integration gate

1. **Executive judgment requires a portfolio of methods, not one universal algorithm.**
2. **Business Intent and beliefs about reality must remain distinct.** Normative preferences cannot be inferred silently from observed behavior.
3. **Hard constraints, authority, arithmetic and policy should remain deterministic wherever possible.**
4. **Optimization is appropriate for formalizable subproblems after objectives and constraints are explicit.**
5. **Probability/Bayesian reasoning is valuable only when numeric uncertainty is defensible; false precision is an architectural failure.**
6. **Scenario reasoning is preferable to fake probabilities for structural/novel uncertainty.**
7. **Game-theoretic reasoning is conditional on material adaptive counterparty response.**
8. **LLMs are valuable for unstructured interpretation, alternative/hypothesis generation, synthesis, critique and orchestration, but should not own canonical truth, policy enforcement, arithmetic, optimization guarantees, calibration, or high-impact authority.**
9. **Decision quality and outcome quality must be evaluated separately.** The system must preserve ex-ante information, assumptions and expectations.
10. **Delegated AI autonomy should be expressed through explicit authority envelopes by decision/action class and risk, not a global autonomy switch.**

---

## 2. First-session deliverables committed

### R001-A

`docs/workstreams/ecr/01-R001-A-DISCIPLINE-AND-SOURCE-MAP-v0.1.md`

Contains canonical source map across all nine required research disciplines, comparative discipline map, established findings, initial synthesis and research gaps.

### R001-B

`docs/workstreams/ecr/02-R001-B-DECISION-ANATOMY-v0.1.md`

Defines logical decision anatomy, uncertainty categories, decision adequacy levels, probability-adequacy levels, ex-ante/ex-post quality distinction and semantic/query requirements for KOE.

### R001-C

`docs/workstreams/ecr/03-R001-C-DECISION-CLASS-PRESSURE-TEST-v0.1.md`

Pressure-tests eight GenSigma decision classes and demonstrates different method profiles for bid/no-bid, partner selection, pricing, staffing, collections, market entry, capital allocation and consequential people decisions.

### R001-D

`docs/workstreams/ecr/04-R001-D-DETERMINISTIC-PROBABILISTIC-BOUNDARY-v0.1.md`

Defines the boundary among deterministic software, optimization, probability/Bayes, scenario reasoning, strategic interaction, LLM assistance and human authority.

### R001-E

`docs/workstreams/ecr/05-R001-E-CANDIDATE-EXECUTIVE-COGNITION-ARCHITECTURES-v0.1.md`

Evaluates three candidate architecture patterns and recommends, provisionally, a **hierarchical policy portfolio**: deterministic governance shell + decision-class method router + modular analytics + challenge/sensitivity + governed authority/action + outcome learning.

---

## 3. Provisional architecture recommendation

The strongest research-backed architecture hypothesis is:

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
DECISION CLASS + STAKES + AUTHORITY
          |
          v
DETERMINISTIC GATES
          |
          v
METHOD ROUTER
          |
          +--> probability / Bayes
          +--> optimization
          +--> scenario / simulation
          +--> strategic interaction
          +--> structured qualitative judgment
          +--> LLM interpretation / generation / orchestration
          |
          v
SENSITIVITY / DEBIAS / COUNTERARGUMENT
          |
          v
AUDITABLE RECOMMENDATION
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

This is **not canonical until Chief Architect reconciliation**.

---

## 4. Required inputs from Knowledge & Ontology Engineering

The ECR workstream now has concrete interface requirements. KOE should make it possible to retrieve or construct, without prescribing physical storage:

1. time-qualified Business Reality for a decision context;
2. applicable Business Intent, criteria, policy and risk posture at that time;
3. time-qualified Capability;
4. material External Reality observations/beliefs;
5. evidence, claims, contradictions and provenance;
6. explicit assumptions used by a recommendation;
7. alternatives considered and provenance/source of alternative generation;
8. model/method references and versions;
9. prediction versus scenario distinction;
10. uncertainty category plus probability-adequacy metadata;
11. recommendation sensitivity/reversal conditions;
12. decision maker, delegation and approval semantics;
13. ex-ante expected outcomes and ex-post actual outcomes;
14. learning/change proposals without automatic mutation of governed Intent/policy.

These requirements do not imply new canonical object types. KOE remains responsible for semantic placement and object admission.

---

## 5. Proposed changes to the existing Decision Engine specification

These are **proposals for Chief Architect review**, not direct edits to the shared spec.

### Proposal 1 — Replace generic decision-function framing with explicit method routing

The existing spec correctly states that the engine may combine rules, models, optimization, LLM reasoning and human judgment. Research 001 should make that operational by introducing a decision-class/method-routing concept.

### Proposal 2 — Add probability adequacy

The spec should distinguish:

- unknown/not quantified;
- qualitative/ordered likelihood;
- empirical/reference-class probability;
- calibrated model/posterior probability.

This prevents downstream components from fabricating numeric probability.

### Proposal 3 — Expand uncertainty into dimensions

Do not use one `confidence` field as the primary representation. Preserve, where material, fact, context, model, forecast, capability, strategic-response and preference uncertainty.

### Proposal 4 — Require ex-ante expectation capture

Material recommendations/decisions should preserve predicted/expected outcomes before action so later learning can distinguish process quality from luck.

### Proposal 5 — Add reversal/sensitivity conditions to Recommendation

A recommendation should state what assumptions, thresholds or new evidence would change it.

### Proposal 6 — Make authority envelope a first-class decision-runtime concern

The system should determine not only whether an action is permitted, but whether an actor/agent is delegated to make this class of decision at this stake/risk level without escalation.

### Proposal 7 — Add decision-method provenance

Material recommendation traces should identify analytical method/model/rule versions used, not only narrative rationale.

### Proposal 8 — Preserve causal claims distinctly from forecasts

A predicted outcome should not silently become evidence that a chosen action will cause that outcome.

---

## 6. Decision classes tested

The first-session architecture was pressure-tested against:

- bid/no-bid;
- teaming partner selection;
- pricing/commercial structure;
- staffing/resource assignment;
- collections escalation;
- market entry/strategic expansion;
- capital allocation;
- hiring/termination/critical people decisions.

This breadth is deliberate. SFO/CRI remains one useful commercial episode, not the architecture boundary.

---

## 7. Recommended first computational decision prototype

### Primary candidate: Bid / No-Bid

Why:

- frequent enough to generate repeated tests;
- economically meaningful;
- direct fit with the RFP-to-Cash chain;
- exercises Intent, Reality, Capability and External Reality;
- mixes hard gates, qualitative judgment and potentially calibrated probability;
- easy for executives to inspect;
- historical decisions/outcomes may permit replay.

### Benchmark baselines

Compare the modular prototype against:

1. LLM-only recommendation;
2. static weighted scorecard;
3. reconstructed historical human decision where possible;
4. modular routed architecture.

### Evaluation dimensions

- completeness of relevant evidence;
- constraint violations;
- alternative coverage;
- calibration where probabilities are used;
- sensitivity transparency;
- consistency across repeated cases;
- explainability/auditability;
- decision latency/cost;
- human reviewer preference;
- outcome metrics only after sufficient cases accumulate.

A single historical win/loss must not be treated as proof of decision quality.

---

## 8. What remains open

Research 001 is not complete. Priority open areas are:

1. **Causal decision reasoning** — intervention choice versus predictive forecasting.
2. **Value of information / stopping rules** — when to gather more evidence versus decide now.
3. **Real options / staged commitment** — particularly for strategic bets and market entry.
4. **Forecast calibration** — especially low-frequency executive judgments.
5. **Multi-objective value models** — combining hard vetoes, lexicographic preferences and compensatory tradeoffs.
6. **Delegated decision-rights model** — explicit mapping of decision class, stakes, risk and action authority.
7. **Learning update policy** — when outcomes should update a model, heuristic, policy or strategic assumption.
8. **Cognition benchmark harness** — replay datasets and scoring rules for human vs LLM-only vs modular systems.

---

## 9. What requires Chief Architect decision

Only the following cross-cutting items require architecture reconciliation now:

1. **Adopt or reject the hierarchical policy-portfolio pattern** as the working Decision Engine architecture direction.
2. **Approve the new semantic requirements** for probability adequacy, multidimensional uncertainty, ex-ante expectations, reversal conditions and method provenance for integration into Decision Engine/KOE specs.
3. **Select the first formal M11 prototype class** (ECR recommends bid/no-bid; staffing/resource assignment is the strongest contrast case).

No physical platform, database, model vendor, agent framework, or new canonical ontology type is being requested by this handoff.

---

## 10. Next ECR execution sequence after integration gate

Unless redirected by an architecture decision, ECR should continue with:

1. causal reasoning and decision versus prediction;
2. value-of-information and decision timing;
3. real-options/staged commitment;
4. calibration and reference-class forecasting;
5. delegated decision rights / authority envelopes;
6. learning/update discipline;
7. bid/no-bid experiment design and benchmark fixture requirements;
8. final R001 synthesis and R001-F proposed Decision Engine spec patch.
