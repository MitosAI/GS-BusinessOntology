# R001-D — Deterministic / Probabilistic / Judgment Boundary

**Version:** v0.1  
**Status:** First-session research artifact; provisional architecture boundary  
**Owner:** Executive Cognition Research Lead (ECR-001)

---

## 1. Purpose

This artifact defines where GenSigma Executive Judgment should prefer deterministic software, formal optimization, probabilistic/statistical methods, scenario reasoning, LLM-assisted reasoning, or human authority.

The objective is not to assign every cognitive act to exactly one technique. The objective is to prevent three architectural errors:

1. using probabilistic/LLM machinery for functions that software can perform reliably;
2. forcing numerical precision onto uncertainty that cannot support it;
3. leaving formalizable decision subproblems inside unstructured executive prose.

This is a research output and method-selection contract. It does not change canonical architecture without Chief Architect reconciliation.

---

## 2. Boundary principle

The default hierarchy is:

```text
CAN THIS BE KNOWN / ENFORCED DETERMINISTICALLY?
        |
        +--> YES: deterministic rule / typed computation / policy
        |
        +--> NO
              |
              v
IS THE CHOICE A FORMAL OPTIMIZATION PROBLEM WITH DEFENSIBLE
OBJECTIVE, CONSTRAINTS, VARIABLES AND FEASIBLE ACTIONS?
        |
        +--> YES: solver / OR module
        |
        +--> NO or PARTIAL
              |
              v
IS NUMERIC UNCERTAINTY DEFENSIBLE FROM DATA, REFERENCE CLASS,
CALIBRATED FORECAST OR EXPLICIT PROBABILISTIC MODEL?
        |
        +--> YES: probability / Bayes / statistical model
        |
        +--> NO
              |
              v
USE STRUCTURED QUALITATIVE UNCERTAINTY, SCENARIOS, SENSITIVITY,
REFERENCE CLASSES, AND HUMAN/LLM-ASSISTED JUDGMENT
```

Strategic interaction and causal analysis are orthogonal modules activated when their assumptions are materially relevant.

---

## 3. Deterministic governed core

The following should normally be deterministic or strongly typed when the required state is available:

- identity and authorization checks;
- policy applicability and enforcement;
- mandatory approval thresholds;
- delegated-authority limits;
- eligibility rules;
- deadline/time comparisons;
- required document/completeness checks;
- arithmetic and financial calculations;
- contractual hard constraints that have been canonically represented;
- allowed state transitions;
- typed-action preconditions;
- security restrictions;
- provenance and audit recording;
- exact historical retrieval when evidence/state is known.

### Rule

An LLM may interpret unstructured evidence to *propose* that a deterministic condition exists, but once that condition is represented canonically, enforcement should not depend on repeating language-model judgment.

### Example

```text
Solicitation requires certification X.
GenSigma does not possess certification X and no permitted partner route exists.
=> infeasible / no-bid gate
```

This should not become “82% confidence no-bid.”

---

## 4. Deterministic optimization / operations research

Optimization belongs where the decision contains sufficiently explicit:

- decision variables;
- objective(s);
- hard constraints;
- feasible set;
- resource/capacity structure;
- cost/value functions that can be defended.

Strong candidate areas:

- staffing/resource assignment;
- scheduling;
- capacity allocation;
- collections prioritization;
- pursuit-resource portfolio allocation;
- routing/sequencing;
- budget allocation subproblems;
- pricing/commercial structure when response/economic functions are credible.

### Boundary

Optimization should not decide what the enterprise values. Business Intent, approved criteria, risk appetite and strategic constraints define the problem that the optimizer solves.

### Failure test

If the team cannot state what the optimizer is maximizing/minimizing without hand-waving, the problem is not yet ready for optimization.

---

## 5. Probabilistic / Bayesian boundary

Probability is appropriate when uncertainty is material **and** numeric representation is defensible.

Examples:

- opportunity win probability based on a meaningful reference class;
- expected payment timing/default risk from historical receivable behavior;
- delivery delay probability from repeated operational data;
- uncertain partner/resource availability when estimates can be calibrated;
- posterior belief updates when new evidence has an interpretable relationship to an uncertain proposition.

### Probability adequacy requirement

Use the R001-B scale:

- `P0` — unknown / not quantified;
- `P1` — ordered or qualitative likelihood only;
- `P2` — empirical/reference-class estimate;
- `P3` — calibrated model/posterior.

Numeric probabilities should normally be restricted to P2/P3 unless an explicit subjective probability is deliberately elicited and labeled as such.

### Bayesian updating is not universal

Bayesian methods are strongest when the system can define:

- the uncertain proposition/state;
- prior/base-rate information;
- incoming evidence;
- likelihood or defensible evidence-weighting logic;
- the decision consequence of the posterior.

If the likelihood structure is fabricated, Bayes creates mathematical decoration rather than better judgment.

---

## 6. Scenario and qualitative uncertainty boundary

Use scenario reasoning when:

- probabilities are P0/P1;
- structural uncertainty dominates parameter uncertainty;
- strategic actors may change the environment;
- the decision is novel and low-frequency;
- regime change is plausible;
- the main value is discovering robust actions rather than ranking one predicted future.

Suitable methods include:

- named scenarios;
- assumption sets;
- sensitivity ranges;
- stress tests;
- robust/minimax-regret reasoning where appropriate;
- real-options/staged commitment;
- trigger conditions for later review.

### Rule

A scenario is a hypothetical state, not a prediction and never canonical current truth.

---

## 7. Strategic-interaction boundary

Game theory / bargaining analysis should activate when all of the following are substantially true:

1. another actor has choices;
2. that actor's incentives differ from or interact with GenSigma's;
3. the actor is likely to observe or infer GenSigma's action;
4. the actor's response can materially change the ranking of GenSigma alternatives.

Examples:

- partner exclusivity/teaming negotiation;
- pricing negotiations;
- customer concession strategy;
- competitive bidding dynamics;
- repeated partner behavior where reputation matters.

Do **not** invoke game theory merely because another organization is present.

The method may range from qualitative incentive mapping to explicit bargaining/game models. Formality should match evidence quality.

---

## 8. Causal boundary

Prediction answers:

> What is likely to happen?

Causal decision reasoning asks:

> What will change because GenSigma chooses action A rather than B?

A predictive model should not automatically be used as an intervention model.

Before the system claims that an action will produce an outcome, it should identify the causal assumption, experiment/quasi-experiment/reference evidence, mechanism, or at minimum label the relationship as a hypothesis.

This boundary is a major next-session research topic.

---

## 9. LLM boundary

### LLMs are well suited to

- extracting structured meaning from unstructured evidence;
- summarizing a decision situation;
- identifying missing information;
- generating hypotheses;
- proposing alternatives;
- translating narrative requirements into candidate constraints/models;
- retrieving and synthesizing analogous cases;
- constructing scenario narratives from explicit assumptions;
- surfacing stakeholder perspectives and counterarguments;
- critiquing a recommendation;
- explaining solver/model outputs;
- orchestrating tools and analytical modules;
- drafting recommendation/decision narratives.

### LLMs should not own

- canonical truth;
- source authority;
- permissions;
- hard-policy enforcement;
- arithmetic when deterministic calculation is available;
- optimization guarantees;
- legal/contract state transitions;
- probability calibration by assertion;
- high-impact final authority;
- hidden chain-of-thought as the sole audit record.

### Audit rule

The durable rationale should preserve explicit inputs, assumptions, alternatives, analytical outputs, decisive evidence and sensitivity—not depend on preserving opaque model-internal reasoning.

---

## 10. Human-judgment boundary

Human decision/approval should remain primary where one or more of the following apply:

- Business Intent itself may change;
- risk appetite or policy exception is being set;
- decision is novel, high-stakes and weakly modeled;
- action is difficult to reverse;
- legal, employment, fiduciary or major reputational consequences are involved;
- value tradeoffs are contested or not yet governed;
- evidence is materially incomplete and no safe default exists;
- decision exceeds delegated agent authority;
- a recommendation would create strategic lock-in.

Human judgment should still be structured and evidence-backed. “Human required” is not permission for unaudited intuition.

---

## 11. Cognitive-function ownership matrix

| Cognitive function | Deterministic software | Prob/statistics | Optimization | Scenario / strategic models | LLM | Human |
|---|---:|---:|---:|---:|---:|---:|
| Retrieve governed state | **Primary** | — | — | — | Support | Support |
| Apply permissions/policy | **Primary** | — | — | — | No authority | Approval exceptions |
| Frame decision question | Support | — | — | Support | **Support** | **Primary for novel/high-stakes** |
| Identify applicable Intent | **Primary retrieval** | — | — | — | Support | Approves Intent |
| Extract unstructured evidence | Rules + parsers | C | — | — | **Primary semantic component** | Review high risk |
| Estimate uncertain state/outcome | — | **Primary when P2/P3** | — | C | Support | P0/P1 judgment |
| Generate alternatives | Rules/retrieval | — | Search C | C | **Primary support** | **Primary for novel strategy** |
| Check feasibility | **Primary** | C | **Primary where formal** | — | Support | Exceptions |
| Evaluate multi-objective tradeoff | Rules/criteria | C | C | C | Explain/support | **Primary where values unresolved** |
| Allocate constrained resources | C | C | **Primary** | C | Orchestrate | Approve significant changes |
| Model counterparty response | — | C | C | **Primary when strategic interaction** | Support | **Primary for sparse/novel cases** |
| Challenge/debias | Checklists/tests | Reference classes | Sensitivity | Premortem/scenario | **Strong support** | **Primary accountability** |
| Produce recommendation | Aggregate | Inputs | Inputs | Inputs | **Synthesis** | Review/own where required |
| Make decision | Rules only if delegated | — | — | — | Never by model status alone | **Authority or delegated policy** |
| Execute action | **Typed action layer** | — | — | — | Tool orchestration only | Approval where required |
| Score outcome/forecast | **Primary metrics** | **Calibration** | — | Compare scenarios | Summarize | Interpret learning |
| Change Intent/policy | Version/governance | Evidence support | — | Scenario support | Propose only | **Primary authority** |

---

## 12. Proposed method-routing metadata

A future decision context should expose enough metadata for the engine to select methods deliberately:

```text
decision_class
stakes
reversibility
time_horizon
deadline
recurrence
hard_constraints_present
objective_formalizability
feasible_set_formalizability
probability_adequacy
strategic_interaction_materiality
causal_claim_required
scenario_need
security_class
authority_required
```

These are logical requirements, not a mandated schema.

---

## 13. Architecture implication

The research now supports a **deterministic-governance shell around a modular analytical core**:

```text
GOVERNED INPUTS
      |
      v
DETERMINISTIC GATES / AUTHORITY
      |
      v
METHOD ROUTER
      |
      +--> probability / Bayes
      +--> optimization
      +--> scenario / simulation
      +--> strategic interaction
      +--> structured qualitative judgment
      +--> LLM interpretation / synthesis
      |
      v
SENSITIVITY / DEBIAS / CHALLENGE
      |
      v
RECOMMENDATION
      |
      v
DECISION / APPROVAL
      |
      v
TYPED ACTION
```

This is a provisional Research 001 architecture implication. It should be reconciled by the Chief Architect rather than promoted silently.
