# RESEARCH-001 — Computational Executive Judgment

**Version:** v0.1  
**Status:** Approved research charter  
**Owner role:** Executive Cognition Research Lead  
**Sponsor:** Chief Architect  
**Program:** GenSigma AI-Native Operating System

---

## 1. Research objective

Determine how GenSigma should computationally represent and execute high-quality executive judgment under uncertainty.

The research must answer a practical architecture question:

> **What should sit inside the GenSigma Decision Engine so that it can progressively perform the kind of judgment currently performed by the founder and executive team — while being more explicit, auditable, consistent, evidence-backed and resistant to human bias?**

The output should not be a survey of interesting theories. It must become an engineering foundation.

---

## 2. Problem statement

An executive does not merely retrieve facts.

A high-quality executive decision typically involves some combination of:

- incomplete and contradictory information;
- uncertain future states;
- multiple goals;
- risk and downside;
- limited resources;
- strategic interaction with customers, competitors, partners, employees or regulators;
- timing;
- path dependency;
- qualitative factors that are difficult to quantify;
- beliefs based on experience;
- explicit and implicit constraints;
- updating as outcomes arrive.

GenSigma OS needs a computational architecture capable of handling this without reducing executive judgment to either:

1. brittle deterministic rules; or
2. an LLM producing plausible prose.

---

## 3. Starting operating loop

The program currently uses this high-level loop:

```text
BUSINESS INTENT
      |
      v
OBSERVE
      |
      v
ORIENT
      |
      v
DECIDE
      |
      v
ACT
      |
      v
VERIFY
      |
      v
LEARN
      |
      +--------> next cycle
```

This is OODA-inspired but makes learning explicit.

Research 001 focuses primarily on **DECIDE**, while clarifying the interfaces between Orient, Decide and Learn.

---

## 4. Inputs to the decision function

The current architectural hypothesis is that a decision consumes:

```text
BUSINESS INTENT
what GenSigma seeks / values / plans / prioritizes

+

BUSINESS REALITY
current and historical state of GenSigma

+

EXTERNAL WORLD MODEL
material beliefs about the outside environment

+

CAPABILITY MODEL
resources, authority, constraints, capacity and feasible actions

+

DECISION CONTEXT / TRIGGER
what requires a choice now
```

The research may refine these interfaces but should not collapse them casually.

---

## 5. Core disciplines to research

### 5.1 Normative decision theory

Study:

- expected utility;
- preferences;
- risk;
- dominance;
- value of information;
- multi-criteria decision analysis;
- decision analysis under uncertainty.

Questions:

- Can Business Intent be translated into utility/decision criteria?
- How should multiple objectives be balanced?
- How should risk appetite enter?
- When is explicit utility useful, and when is it false precision?

### 5.2 Bayesian decision theory

Study:

- priors;
- likelihoods;
- posterior updating;
- Bayesian networks where relevant;
- Bayesian decision rules;
- uncertainty calibration;
- value of additional evidence.

Questions:

- Which GenSigma beliefs are legitimately probabilistic?
- What should be updated continuously versus deliberatively?
- How should weak priors be handled?
- How do we avoid fabricated probabilities?

### 5.3 Operations research

Study:

- linear/integer optimization;
- constrained optimization;
- stochastic optimization;
- resource allocation;
- scheduling;
- queueing;
- portfolio optimization;
- simulation.

Questions:

- Which executive decisions are optimization problems after the strategic judgment has been made?
- Where can the OS outperform human intuition with deterministic solvers?

### 5.4 Game theory and strategic interaction

Study:

- normal/extensive-form games;
- incomplete information;
- Bayesian games;
- bargaining;
- signaling;
- repeated games;
- mechanism design concepts where relevant;
- competitive strategy applications.

Questions:

- When must the system explicitly model other actors' responses?
- How should counterparty incentives be represented?
- When is game theory useful versus overly formal?

### 5.5 Control theory and feedback systems

Study:

- state-space thinking;
- feedback;
- disturbance;
- control policy;
- stability;
- adaptive control;
- model predictive control concepts where transferable.

Questions:

- Can strategy execution be treated partially as a feedback/control problem?
- What should trigger correction versus strategy change?
- How do we distinguish noise from signal?

### 5.6 Behavioral decision science

Study:

- Kahneman and Tversky;
- heuristics and biases;
- prospect theory;
- base-rate neglect;
- anchoring;
- availability/recency;
- loss aversion;
- overconfidence;
- framing;
- escalation of commitment;
- bounded rationality / Herbert Simon;
- debiasing mechanisms.

Questions:

- Which human executive biases should the OS explicitly detect or counter?
- Which heuristics are actually useful compressed expertise?
- How can we preserve expert intuition without reproducing bias blindly?

### 5.7 Strategic management / executive judgment

Study:

- strategic choice;
- competitive advantage;
- portfolio decisions;
- scenario planning;
- real options;
- capital allocation;
- executive team decision processes;
- board/governance decision structures;
- decision rights.

Questions:

- How do real executives structure consequential decisions?
- What is missing from purely mathematical decision theory?
- How should qualitative strategic beliefs be represented and challenged?

### 5.8 AI reasoning, planning and sequential decision-making

Study:

- classical planning;
- heuristic search;
- tree search;
- MDPs/POMDPs;
- model-based RL concepts;
- decision transformers / policy learning where relevant;
- tool-using agents;
- LLM planning/reasoning;
- self-critique/debate;
- verifier models;
- uncertainty/calibration of LLMs.

Questions:

- What have modern AI systems actually solved?
- Where do LLMs add unique capability?
- Where should deterministic planners/solvers replace language-model reasoning?
- Can LLM reasoning be made sufficiently auditable for executive use?

### 5.9 Military command and control / OODA

Study public material on:

- John Boyd's OODA concepts;
- orientation and mental models;
- commander's intent;
- intelligence preparation;
- adversarial adaptation;
- after-action review;
- decision tempo;
- decentralized authority.

Questions:

- What carries into business executive cognition?
- How is uncertainty compressed under time pressure?
- How are intent and local autonomy connected?
- How does learning update doctrine without causing constant strategic thrash?

---

## 6. Source strategy

The research should be deep enough to influence architecture.

### Tier A — Primary / canonical

Prefer:

- textbooks used in serious university courses;
- original/canonical papers;
- peer-reviewed papers;
- major academic monographs;
- official military/public doctrine;
- university lecture notes and syllabi from leading institutions.

### Tier B — High-quality applied

Use:

- quantitative finance/hedge-fund methodology where technically explicit;
- serious operations-research case studies;
- management-science and strategy practitioner material;
- technical documentation from companies that build operational decision systems;
- public Palantir material for ontology/action/governance architecture.

### Tier C — Practitioner discussion

Use Medium/Substack/newsletters/blogs/community discussions to:

- discover ideas;
- identify emerging patterns;
- understand practitioner experience.

Do not elevate them above primary theory without justification.

---

## 7. Institutions and bodies of work to sample

Research should deliberately sample leading material from institutions known for relevant disciplines, for example:

- Stanford;
- MIT;
- Harvard;
- Carnegie Mellon;
- Berkeley;
- Wharton / Penn;
- INSEAD;
- London Business School;
- Oxford / Cambridge;
- RAND where relevant;
- military war colleges / command-and-control research where public;
- INFORMS / operations research community;
- decision analysis professional literature.

This is a starting map, not a ranking.

---

## 8. Practical benchmark: replace-the-executive test

Every research conclusion should be tested against the user-level goal:

> **Could this help the OS make or support a decision currently dependent on VJ's executive judgment?**

Candidate benchmark decisions:

### Strategic

- Which markets should GenSigma enter?
- Should GenSigma deepen SLED AI or diversify?
- How should a major external policy/technology change alter strategy?

### Commercial

- Should we bid this opportunity?
- Which partner should we team with?
- How much pursuit effort should we allocate?
- How should we price or structure the response?

### Operational

- Which projects need intervention?
- Who should be assigned where?
- When should a vendor/employee issue be escalated?

### Financial

- How should capital be allocated?
- Which receivable should be escalated first?
- What trade-offs improve cash flow without damaging relationships?

Research should determine whether these belong to one architecture or multiple decision-class policies.

---

## 9. Required synthesis framework

For each discipline, produce a table with:

```text
DISCIPLINE
Core idea
What it optimizes / represents
Required inputs
Outputs
Strengths
Failure modes
Data requirements
Deterministic vs probabilistic
Role for LLMs
Best-fit GenSigma decision classes
Architecture implications
```

Then create a cross-discipline synthesis.

---

## 10. Candidate architectural questions

The research must explicitly evaluate at least these architecture hypotheses:

### Hypothesis A — Bayesian belief state + utility decision

World/business beliefs represented probabilistically where feasible; decisions maximize expected utility under Business Intent.

### Hypothesis B — Policy portfolio

Different decision classes invoke different methods: rules, optimization, Bayes, game theory, LLM reasoning, human approval.

### Hypothesis C — Hierarchical executive cognition

High-level strategic beliefs and policies change slowly; lower-level operational decisions run faster under those policies.

### Hypothesis D — LLM as interpreter/orchestrator, not sole judge

LLM handles unstructured context, alternatives, explanation and tool orchestration; deterministic/probabilistic solvers handle formal pieces.

### Hypothesis E — Decision graph / trace as first-class audit structure

Every recommendation can be reconstructed from state, evidence, assumptions, alternatives, criteria, model outputs and authority.

The research may reject or combine these hypotheses.

---

## 11. Deliverable structure

### Part I — Executive summary

10–20 pages maximum, written for architecture decisions.

### Part II — Discipline synthesis

Deep review of the nine areas.

### Part III — Decision taxonomy

Map GenSigma decision classes to computational methods.

### Part IV — Proposed architecture options

At least 2–3 credible alternatives with trade-offs.

### Part V — Recommended architecture

Explain what belongs in the GenSigma Decision Engine, what does not, and why.

### Part VI — Implications for Build Spec 001 and Business Reality

List required state, evidence, uncertainty, scenario, capability and intent structures.

### Part VII — Experiment plan

Define the first bounded decision prototype and how to evaluate whether it beats a baseline human/LLM-only approach.

---

## 12. Evaluation criteria

A recommended cognition architecture should score well on:

- decision quality;
- calibration under uncertainty;
- explainability/auditability;
- consistency;
- computational feasibility;
- robustness to missing/contradictory evidence;
- resistance to known bias;
- ability to model strategic interaction;
- ability to enforce hard constraints;
- ability to learn from outcomes;
- compatibility with the Palantir-style ontology/kinetic spine;
- human governance;
- ease of implementation and testing.

---

## 13. What would count as failure

Research 001 fails if it returns:

- a generic list of decision theories;
- "use an LLM with chain-of-thought";
- a Bayes-everywhere architecture without defensible probabilities;
- optimization disconnected from strategy;
- game theory applied to every interaction;
- a purely human behavioral framework with no computational translation;
- an architecture too academic to implement;
- conclusions without source grounding;
- a recommendation that cannot be tested on a real GenSigma decision.

---

## 14. Output contract to Chief Architect

Return:

```text
RESEARCH-001 HANDOFF
1. What we learned
2. What appears established
3. What is our synthesis/inference
4. Recommended architecture
5. Alternatives rejected and why
6. Changes required to existing Decision Engine spec
7. New data requirements for Business Reality / Intent / Capability
8. First experiment recommendation
9. Open questions
10. Source map / bibliography
```

No cross-cutting architecture change is canonical until reconciled by the Chief Architect and promoted into repository artifacts.

---

## 15. Immediate starting sequence

1. Build the discipline/source map.
2. Start with normative decision theory + Bayesian decision theory to establish the formal baseline.
3. Add behavioral decision science to expose human-model failure modes.
4. Add operations research and game theory for constraint/strategic structure.
5. Add control theory for feedback and adaptation.
6. Add executive strategy and command-and-control material for real decision practice.
7. Only then map modern LLM/agent reasoning onto the functions discovered.
8. Synthesize into candidate architectures.
9. Select the first GenSigma decision class for experimentation.
