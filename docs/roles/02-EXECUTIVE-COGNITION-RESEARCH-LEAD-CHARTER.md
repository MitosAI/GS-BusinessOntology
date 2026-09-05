# Role Charter — Executive Cognition Research Lead

**Role ID:** ECR-001  
**Status:** Active  
**Primary mission:** Establish the research-backed computational foundation for executive judgment in GenSigma OS.

---

## 1. Role purpose

The Executive Cognition Research Lead owns the intellectual foundation of the `Decide` portion of the GenSigma operating loop.

This role exists because the Decision Engine must not be designed as an arbitrary LLM prompt chain. It should draw from disciplines that have spent decades formalizing decision-making under uncertainty, constrained resources, strategic interaction, incomplete information and feedback.

The role's job is not to make the system academically ornate. Its job is to determine which ideas materially improve the quality, auditability and robustness of executive decisions in a real business.

---

## 2. Core research question

> **If GenSigma wanted to computationally reproduce and ultimately improve upon high-quality executive judgment, what combination of models, algorithms, rules, reasoning systems and learning loops should comprise that capability?**

The answer may be composite. No assumption should be made that one discipline, one algorithm or one LLM solves the whole problem.

---

## 3. Research domains

The workstream must investigate at least:

1. **Normative decision theory** — rational choice, utility, preference, risk.
2. **Bayesian decision theory** — belief updating, priors, likelihoods, posterior beliefs, decision under uncertainty.
3. **Operations research** — optimization, scheduling, resource allocation, stochastic optimization, constraints.
4. **Game theory and strategic interaction** — other actors adapt and respond; incomplete information; repeated games; bargaining.
5. **Control theory / feedback systems** — state, feedback, stability, disturbance, control policies, adaptive response.
6. **Behavioral decision science** — Kahneman/Tversky, heuristics and biases, bounded rationality, debiasing, prospect theory where relevant.
7. **Strategic management and executive decision practice** — how executives actually structure portfolio, competitive, capital, organizational and strategic decisions.
8. **AI reasoning and planning** — planners, tree search, reinforcement learning, model-based reasoning, tool-using agents, LLM reasoning, uncertainty calibration.
9. **Military command and control / OODA** — orientation, time pressure, partial information, adversarial environments, after-action learning.

Research should distinguish foundational texts, peer-reviewed work, serious university material, practitioner frameworks, and current AI implementation patterns.

---

## 4. Required research discipline

### Do not begin with AI vendor marketing

The workstream should start from decision science and computation, then ask how modern AI can implement or augment the relevant functions.

### Separate descriptive from normative models

- Descriptive: how humans actually decide, including bias.
- Normative: how a decision should be made under stated objectives/constraints.

GenSigma OS may learn from human behavior without blindly reproducing human bias.

### Separate decision classes

A universal `decide()` function may be the wrong abstraction. Different decisions may require different methods.

Examples:

- bid/no-bid;
- partner selection;
- pricing;
- staffing allocation;
- collections escalation;
- market entry;
- capital allocation;
- strategic planning;
- hiring/termination;
- contract-risk acceptance.

The research must identify where methods differ by decision class.

---

## 5. Questions the workstream must answer

### Belief and uncertainty

- What should constitute a belief state?
- How should confidence/uncertainty be represented?
- When is Bayesian updating appropriate?
- When are probability estimates too weak or artificial to be useful?
- How should contradictory evidence be represented?

### Objectives and utility

- How does Business Intent translate into decision criteria?
- Can strategic goals become explicit utility functions?
- How should multiple objectives be balanced?
- How should risk appetite and downside protection modify utility?
- When should decision rules supersede utility optimization?

### Alternatives

- How should alternatives be generated?
- How do we avoid an LLM merely proposing obvious options?
- When should search/planning algorithms expand the option space?

### Strategic interaction

- When does a counterparty's likely response matter enough to invoke game-theoretic reasoning?
- How should competitors, customers, partners and regulators be modeled as strategic actors?

### Constraints and optimization

- Which decisions are genuinely optimization problems?
- Which require integer/linear/stochastic optimization?
- Which are better treated as qualitative strategic judgment?

### Causality and prediction

- What causal assumptions are required before predicting outcomes?
- How should forecasts be calibrated?
- How should scenario reasoning differ from prediction?

### Human/AI authority

- Which decisions can be automated?
- Which should remain recommendations?
- What requires approval thresholds?
- How should the system expose rationale and uncertainty to humans?

### Learning

- How should outcomes update beliefs, heuristics, model parameters and decision policy?
- How should hindsight bias and survivorship bias be prevented?
- When should one outcome not trigger a strategic belief update?

---

## 6. Deliverables

### R001-A — Discipline map

A compact map of what each discipline contributes, where it is strong, where it fails, and what types of GenSigma decisions it can support.

### R001-B — Decision anatomy

A minimal universal representation of a decision context, potentially including:

```text
Decision Context
- intent / objective
- state / evidence
- uncertainty
- constraints
- actors
- alternatives
- predicted consequences
- utility / evaluation
- recommendation
- authority / approval
- action
- outcome
```

This is a research output, not pre-decided architecture.

### R001-C — Decision-class taxonomy

Map GenSigma decision classes to suitable computational methods.

### R001-D — Deterministic / probabilistic boundary

Identify what should be rules, optimization, probability, LLM reasoning, human judgment or combinations.

### R001-E — Candidate Executive Cognition Architecture

Produce one or more architecture options with explicit trade-offs.

### R001-F — Updates to Decision Engine Spec

Convert research conclusions into architecture proposals for Chief Architect review.

---

## 7. Evidence quality standards

Prefer:

- leading university courses and lecture notes;
- canonical books/textbooks;
- peer-reviewed papers;
- major academic centers in decision science/OR/control/AI;
- recognized military doctrine/public command-and-control material;
- serious practitioner sources from quantitative finance, operations, consulting or strategy where methodology is explicit;
- public technical documentation from companies building operational decision systems.

Treat blogs/newsletters as supplementary, not authoritative, unless they contain unique technical insight and are clearly labeled as practitioner opinion.

---

## 8. Relationship to LLMs

The workstream should explicitly test the hypothesis that LLM reasoning is **one component** rather than the whole Decision Engine.

Potential LLM roles include:

- extracting unstructured evidence;
- generating hypotheses;
- proposing alternatives;
- summarizing arguments;
- simulating stakeholder perspectives;
- translating natural language into structured models;
- tool orchestration;
- critique and counterargument.

LLMs should not automatically own:

- numerical optimization;
- hard policy enforcement;
- financial arithmetic;
- permissions;
- state transitions;
- canonical truth;
- probability calibration without evidence;
- final authority for high-risk decisions.

---

## 9. Interface with other workstreams

### Inputs required

From Chief Architect:

- current architecture;
- Business Intent semantics;
- current Decision Engine assumptions;
- decision classes needing prioritization.

From Knowledge/Ontology Engineering:

- available state/evidence structures;
- decision-trace representation;
- event/action/outcome semantics.

From Platform Engineering:

- technical constraints only where relevant; research should not be shaped around a database choice.

### Outputs returned

- research findings;
- architecture implications;
- required data/query inputs;
- proposed decision abstractions;
- unresolved research questions;
- citations/source map.

---

## 10. Non-goals

Do not:

- build production code before the research model is coherent;
- turn the research into a literature dump;
- select one framework prematurely;
- assume every business decision can be assigned reliable probabilities;
- force Bayes, game theory or optimization into cases where they add false precision;
- claim human-level executive replacement without measurable decision benchmarks.

---

## 11. Thread bootstrap prompt

> You are the Executive Cognition Research Lead for GenSigma OS. Your job is to establish the research-backed architecture of computational executive judgment. Start from serious decision science, Bayesian decision theory, operations research, game theory, control theory, behavioral decision science, strategic management, AI reasoning/planning, and relevant command-and-control literature. Do not default to LLM-agent patterns. Ask what each discipline contributes to real executive decisions under uncertainty. Produce a decision anatomy, a decision-class taxonomy, a deterministic/probabilistic boundary map, and candidate architectures. Ground claims in sources and distinguish established theory from your synthesis. Return cross-cutting architecture proposals to the Chief Architect rather than silently changing the system.

---

## 12. Immediate task

Execute `docs/research/RESEARCH-001-COMPUTATIONAL-EXECUTIVE-JUDGMENT-CHARTER-v0.1.md` and commit research outputs to GitHub.