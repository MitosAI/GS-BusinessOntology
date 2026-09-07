# R001-B — Decision Anatomy

**Version:** v0.1  
**Status:** First-session research artifact; provisional semantic requirements  
**Owner:** Executive Cognition Research Lead (ECR-001)

---

## 1. Purpose

This artifact defines the minimum information required to reason about a material GenSigma decision in a way that is auditable, method-selectable, uncertainty-aware, and learnable.

It is deliberately a **logical anatomy**, not a new ontology object or physical schema. Nothing here requires creation of a `DecisionCase`, `DecisionPacket`, or similar canonical type. Knowledge/Ontology Engineering should decide whether each requirement belongs in an existing object, property, link, evidence record, computed view, or temporary reasoning context.

The anatomy consumes the current modular architecture:

```text
Business Intent
Business Reality
External Reality
Capability
Policies / Authority / Security
             |
             v
      Decision Context
             |
             v
     Executive Judgment
```

---

## 2. Minimal anatomy

A material decision should be reconstructable through nine logical sections.

### A. Decision framing

Minimum fields/semantics:

- decision identifier or trace anchor;
- decision type/class;
- trigger / why the decision exists now;
- decision question;
- scope and linked business context objects;
- decision horizon;
- deadline / latest useful decision time;
- stakes / consequence magnitude;
- reversibility / cost of reversal;
- recurrence: one-off, episodic, recurring;
- status: framing, analysis, recommended, decided, approved, acted, closed.

**Reasoning requirement:** the system must distinguish a poorly framed question from a difficult answer.

### B. Business Intent and evaluation frame

- applicable strategic objective(s);
- local decision objective(s);
- decision criteria;
- hard constraints / veto rules;
- soft preferences;
- risk appetite / tolerance;
- time preferences where material;
- applicable policies;
- historical Intent version effective at the decision time.

**Invariant:** observed historical behavior is not allowed to silently redefine approved Intent.

### C. Situation / epistemic state

- Business Reality snapshot and effective time;
- material External Reality observations/beliefs;
- Capability snapshot;
- relevant events/state changes;
- claims and evidence references;
- explicit assumptions;
- known contradictions;
- unresolved unknowns;
- source authority where material;
- security-filtered view actually available to the decision maker/agent.

**Invariant:** the recommendation must be reproducible from the information that was available at the time, not from hindsight.

### D. Uncertainty structure

Uncertainty must not collapse into a single confidence number. At minimum distinguish:

1. **fact uncertainty** — is the underlying state/claim true?
2. **identity/context uncertainty** — are we reasoning about the correct object/context?
3. **model uncertainty** — is the analytical model appropriate?
4. **parameter / probability uncertainty** — how uncertain are model inputs?
5. **forecast uncertainty** — what future outcome may occur?
6. **capability/execution uncertainty** — can GenSigma actually execute as assumed?
7. **strategic-response uncertainty** — how may other actors adapt?
8. **preference/criterion uncertainty** — are priorities/tradeoffs clear and approved?

A decision may have different confidence levels across these categories.

### E. Actors, authority and strategic interaction

- decision maker / accountable owner;
- recommender(s);
- required approver(s);
- delegated authority limits;
- affected stakeholders;
- counterparties whose response can change outcomes;
- relevant incentives, commitments and bargaining positions;
- conflicts of interest where material.

**Method-selection implication:** game-theoretic or bargaining analysis should activate only when strategic response is material.

### F. Alternatives

Every material decision context should preserve:

- alternatives considered;
- status quo / do-nothing option when meaningful;
- source of each alternative: rule, precedent, human, model, LLM, solver, retrieval;
- feasibility status;
- eliminated alternatives and elimination reason;
- whether the alternative set is known to be incomplete.

**Research finding:** alternative generation is a distinct cognitive function. The quality of evaluation cannot rescue a decision where the viable alternative was never generated.

### G. Analysis and consequence model

For each material alternative, preserve or reference as applicable:

- method(s) used;
- assumptions;
- deterministic calculations;
- constraints/feasibility result;
- predicted consequences;
- scenarios;
- probability distributions or qualitative likelihoods where defensible;
- expected value / utility / multi-criteria result where appropriate;
- optimization result where appropriate;
- counterparty-response analysis where appropriate;
- causal assumptions where action-effect reasoning is claimed;
- sensitivity thresholds;
- value-of-information assessment where waiting/gathering evidence is an option.

**Invariant:** a forecast is not automatically a causal model, and a numerical score is not automatically judgment.

### H. Judgment, decision and action handoff

The judgment output should preserve:

- recommended alternative;
- concise rationale;
- decisive evidence and criteria;
- key assumptions;
- key uncertainties;
- conditions that would reverse/change the recommendation;
- confidence by uncertainty category where useful;
- rejected alternatives and why;
- execution eligibility;
- approval requirement.

Then preserve the existing semantic distinctions:

```text
Recommendation
   != Decision
   != Approval
   != Action
```

The decided/approved course should hand off only to governed typed actions.

### I. Outcome and learning contract

At decision time, define:

- expected immediate outcome(s);
- expected downstream outcome(s);
- metrics/observables by which success or failure will later be assessed;
- review horizon / when the decision should be revisited;
- assumptions to test;
- forecasts that can later be scored/calibrated.

After action, preserve:

- actual outcome(s);
- variance from expectation;
- whether variance was caused by randomness, bad state estimate, bad model, execution failure, strategic response, or poor criteria where known;
- calibration result for probabilistic forecasts;
- process-quality assessment;
- proposed learning/update;
- whether a policy/model/Intent change is merely proposed or actually approved.

**Invariant:** outcome does not retroactively rewrite what was known at the time of decision.

---

## 3. Decision adequacy levels

Not every decision needs the same analytical depth. A provisional four-level classification is useful for routing effort.

### Level 0 — Deterministic operational rule

Characteristics:

- known state;
- clear rule;
- low ambiguity;
- low discretion;
- reversible/low risk.

Example: a renewal deadline has passed and policy requires escalation.

Primary machinery: deterministic software + typed action + audit.

### Level 1 — Structured choice

Characteristics:

- finite alternatives;
- explicit criteria;
- moderate uncertainty;
- limited strategic interaction.

Example: choose among qualified candidate resources for a pursuit.

Primary machinery: hard gates + multi-criteria evaluation + limited prediction + human/authorized decision.

### Level 2 — Analytical decision under uncertainty

Characteristics:

- important probabilistic outcomes;
- resource constraints;
- scenarios or optimization materially affect ranking;
- meaningful sensitivity.

Example: pricing, resource allocation, bid/no-bid with defensible base rates.

Primary machinery: rules + probability/forecasting + optimization/scenario + structured judgment.

### Level 3 — Strategic / novel judgment

Characteristics:

- unclear or evolving frame;
- sparse precedent/data;
- high stakes or irreversibility;
- endogenous counterparty response;
- multiple competing objectives;
- significant reputational/legal/strategic consequences.

Example: enter a new market, acquire a company, change strategic focus.

Primary machinery: structured executive process, scenario analysis, strategic interaction, reference classes, explicit assumptions, challenge/red-team, human authority. Numeric formalism may support but should not create false precision.

This classification is provisional and should not become ontology doctrine without KOE/Chief Architect review.

---

## 4. Probability adequacy levels

A key safeguard is to represent the **quality of probabilistic support**, not merely a probability value.

### P0 — Unknown / not quantified

No defensible numeric probability. Preserve uncertainty qualitatively.

### P1 — Ordered / qualitative

Evidence supports rankings such as low/medium/high or more/less likely, but not calibrated numerical probabilities.

### P2 — Empirical / reference-class estimate

Historical base rates or comparable cases support an approximate numeric estimate with known limitations.

### P3 — Calibrated model / posterior

A validated model, explicit likelihood/prior structure, or repeatedly scored forecast process supports numeric probability and calibration tracking.

**Rule:** the engine should never promote P0/P1 uncertainty to a precise probability merely because a downstream formula expects one.

---

## 5. Decision quality versus outcome quality

The platform should eventually support two separate evaluations.

### Ex-ante decision quality

Was the decision process good given what was knowable then?

Questions:

- Was the question framed correctly?
- Were relevant objectives explicit?
- Were hard constraints applied correctly?
- Was the evidence sufficient for the stakes?
- Were credible alternatives generated?
- Were uncertainty and assumptions explicit?
- Was the selected method fit for the decision class?
- Were material sensitivities tested?
- Was required authority obtained?

### Ex-post outcome quality

What actually happened?

Questions:

- Did intended actions execute?
- Did predicted outcomes occur?
- Where did reality diverge?
- Were forecasts calibrated?
- Did an unmodeled actor response matter?
- Was failure attributable to decision process, execution, or stochastic outcome?

This prevents lucky outcomes from legitimizing poor reasoning and unlucky outcomes from automatically condemning sound decisions.

---

## 6. Trace relationship to existing ontology semantics

This anatomy maps onto the existing decision/control fabric without requiring one container object:

```text
Artifact / Evidence / Claim
        |
        v
Assessment + Assumption
        |
        +--> Alternative(s)
        +--> Model / Prediction / Scenario references
        |
        v
Recommendation
        |
        v
Decision
        |
        v
Approval / Delegation
        |
        v
Action
        |
        v
Outcome
        |
        v
Learning proposal
```

Business Intent, Business Reality, External Reality and Capability remain distinct inputs linked into the trace.

---

## 7. Required interface implications for Knowledge/Ontology Engineering

ECR requires the logical architecture to make it possible to retrieve or construct:

1. time-qualified Business Reality relevant to a decision;
2. applicable Intent/criteria/policies at that time;
3. time-qualified Capability;
4. material External Reality beliefs/observations;
5. evidence and claim provenance;
6. assumptions explicitly used in reasoning;
7. alternatives and their provenance;
8. analytical model/method references;
9. scenario versus prediction distinction;
10. uncertainty category and probability-adequacy metadata;
11. recommendation sensitivity / reversal conditions;
12. decision rights, approvals and delegation;
13. ex-ante expected outcomes and later actual outcomes;
14. learning proposals without automatically mutating governed Intent/policy.

These are **semantic/query requirements**. ECR does not prescribe whether they are implemented as object types, links, records, views, functions or transient reasoning structures.

---

## 8. Immediate acceptance tests

A future decision-context implementation should answer:

- What exactly was the decision question?
- What Intent and criteria governed it?
- What was believed true at that time, and from what evidence?
- What was unknown?
- What alternatives were considered and how were they generated?
- Which hard constraints eliminated options?
- Which analytical methods were used and why?
- Which assumptions were decisive?
- What evidence would have changed the recommendation?
- Who had authority to decide/approve?
- What action followed?
- What outcome was expected before acting?
- What actually happened?
- What should be learned without hindsight distortion?

If these cannot be answered for a material decision, the trace is insufficient for computational executive learning.
