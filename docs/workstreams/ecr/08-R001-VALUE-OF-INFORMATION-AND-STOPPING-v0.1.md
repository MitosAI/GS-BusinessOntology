# R001 — Value of Information, Decision Timing, and Stopping Rules

**Version:** v0.1  
**Status:** Research finding / architecture input; not canonical architecture  
**Owner:** ECR-001 — Executive Cognition Research Lead  
**Research program:** RESEARCH-001 — Computational Executive Judgment

---

## 1. Executive problem

Good executives do not merely ask:

> What do we know?

They also ask:

> Is it worth learning more before we decide?

and:

> When does more analysis stop being useful?

The Decision Engine therefore needs a principled way to choose among:

```text
DECIDE NOW

WAIT FOR EXISTING INFORMATION

GATHER MORE INFORMATION

RUN AN EXPERIMENT / PILOT

TAKE A REVERSIBLE ACTION AND LEARN
```

This is a decision problem in its own right.

---

## 2. Established decision-analysis principle

The value of information is not the amount of uncertainty removed.

It is the **expected improvement in decision value made possible by the information**.

Information has little or no decision value when:

- the same action remains optimal across plausible states;
- the information arrives after the decision deadline;
- the information cannot be acted upon;
- the cost of acquiring it exceeds the expected improvement;
- the decision is already dominated by a hard constraint;
- the uncertainty concerns a variable that is not decision-sensitive.

This is central for GenSigma because an AI system can always generate another search, analysis, model, or question. Without a stopping principle, “more intelligence” becomes unbounded analysis cost and delayed action.

---

## 3. Core value-of-information quantities

Let `A` be the set of available actions, `θ` an uncertain state or parameter, and `U(a, θ)` the value of taking action `a` when `θ` obtains.

### 3.1 Current decision value

Without new information:

```text
V_current = max_a E[U(a, θ)]
```

The decision maker chooses the action with the highest current expected value under the present information state.

### 3.2 Expected Value of Perfect Information — EVPI

If the uncertain state could be learned perfectly before acting:

```text
EVPI = E_θ[max_a U(a, θ)] - max_a E_θ[U(a, θ)]
```

EVPI is an upper bound on what it could ever be worth to eliminate that uncertainty completely.

If EVPI is small, additional research about that uncertainty is unlikely to be worthwhile.

### 3.3 Expected Value of Sample Information — EVSI

For a feasible information-gathering action `I` producing possible result `d`:

```text
EVSI(I) = E_d[max_a E[U(a, θ) | d]] - max_a E[U(a, θ)]
```

EVSI measures how much the actual study/search/test is expected to improve the decision.

### 3.4 Expected net value of information

A practical system must subtract acquisition and timing costs:

```text
NET_VOI(I)
  = EVSI(I)
  - direct_information_cost(I)
  - delay/opportunity_cost(I)
  - execution/disruption_cost(I)
```

For some decisions, waiting also changes the available actions. In those cases timing must be modeled explicitly rather than treated as a simple additive penalty.

---

## 4. The key GenSigma insight: uncertainty is not enough; decision sensitivity matters

Suppose a Bid / No-Bid decision currently has:

- pursue expected value: strongly positive across reasonable win-probability estimates;
- no hard capability constraint;
- adequate margin;
- manageable downside.

Learning whether win probability is 55% or 65% may have low decision value if GenSigma bids either way.

By contrast, if the recommendation flips at 58%, then improving the estimate around that region can be highly valuable.

Therefore the correct order is:

```text
1. Identify the decision.
2. Identify the current best action.
3. Test sensitivity / reversal conditions.
4. Identify which uncertainty can change the action.
5. Value information only about those decision-sensitive uncertainties.
```

This is more efficient than indiscriminately trying to increase confidence in every input.

---

## 5. Provisional stopping rule

ECR proposes the following **research rule**, not yet a shared runtime contract:

> Continue gathering information only while the expected marginal improvement in decision value exceeds the full marginal cost of obtaining and waiting for that information.

Operationally:

```text
For candidate information action I:

IF information cannot arrive before the relevant decision point
    -> do not wait for it

ELSE IF plausible result of I cannot change the preferred action
    -> stop; information is decision-irrelevant

ELSE estimate / bound expected decision improvement

IF expected improvement <= acquisition + delay + disruption cost
    -> stop and decide

ELSE
    -> gather information / experiment
       then re-evaluate
```

A full numerical EVSI calculation is not required for every business choice. Sensitivity bounds and qualitative decision relevance may be sufficient when precision would be artificial.

---

## 6. Five modes of information acquisition

### 6.1 Retrieval

Obtain evidence that already exists.

Examples:

- locate the executed agreement;
- retrieve the customer's latest RFP amendment;
- inspect current staffing availability;
- retrieve payment history.

Usually low cost and often high value when the fact is material.

### 6.2 Clarification

Ask a human or counterparty for missing information.

Examples:

- ask procurement whether subcontractor substitution is allowed;
- ask a delivery lead whether a named engineer is actually available;
- ask a partner for committed pricing.

### 6.3 Analysis

Transform existing evidence into a more decision-relevant estimate.

Examples:

- run margin sensitivity;
- build a reference-class forecast;
- simulate staffing schedules;
- estimate a causal effect from historical data.

### 6.4 Experiment / pilot

Take an action designed partly to learn.

Examples:

- trial a collections message on a subset of accounts;
- run a small outbound campaign before market expansion;
- pilot a new staffing process on one project;
- A/B test a proposal communication pattern where feasible.

This creates stronger evidence but may itself have cost, risk, and ethical/relationship implications.

### 6.5 Reversible action with monitoring

Act now because the decision is reversible and instrument the outcome tightly.

Examples:

- allocate one engineer for a week rather than a quarter;
- launch a limited partner pilot rather than an exclusive agreement;
- pursue one geography under a bounded investment before full market entry.

This mode connects value of information to real-options and staged-commitment reasoning.

---

## 7. Reversibility changes the information threshold

The rational amount of pre-decision information depends on how costly it is to be wrong.

### Highly reversible / low-regret decision

Bias toward:

- act sooner;
- instrument outcomes;
- learn from real feedback;
- avoid expensive pre-analysis.

### Irreversible / high-downside decision

Bias toward:

- higher evidence threshold;
- explicit causal assumptions;
- stronger sensitivity analysis;
- additional approvals;
- pilot/stage where possible before full commitment.

This is not a universal “move fast” versus “analyze deeply” principle. It is a decision-specific trade between learning value, delay cost, and reversibility.

---

## 8. Time itself is a state variable

In executive decisions, waiting can change the problem.

Examples:

- an RFP deadline closes;
- a candidate accepts another offer;
- a customer budget is allocated elsewhere;
- capacity is consumed by another project;
- a partner becomes unavailable;
- a market-entry window narrows;
- a discount deadline expires.

Therefore:

```text
VALUE OF INFORMATION
!=
VALUE OF INFORMATION RECEIVED TOO LATE
```

The Decision Engine should evaluate information against the **decision horizon and option expiry**, not only its epistemic quality.

---

## 9. GenSigma pressure tests

### 9.1 Bid / No-Bid

Potential missing information:

- likely incumbent position;
- partner commitment;
- actual internal delivery capacity;
- evaluation weighting;
- estimated competitor field;
- customer budget realism.

Decision-focused questions:

- Which unknowns can actually flip Bid to No-Bid or materially change pursuit level?
- Can the unknown be resolved before the response deadline?
- Is the cost of resolving it lower than the expected improvement in pursuit allocation?

A low-value behavior would be spending hours refining win probability from 62% to 64% when the organization would bid in either case.

### 9.2 Teaming Partner Selection

Additional diligence can include:

- references;
- pricing;
- staff commitments;
- conflict checks;
- past performance.

Stop when remaining uncertainty no longer changes partner ranking enough to justify delay or risks missing the teaming window.

### 9.3 Staffing

The system may be uncertain whether a project requires another senior engineer.

Instead of committing a six-month assignment immediately, it may recommend a two-week bounded allocation with milestone telemetry. The action both delivers value and creates information.

### 9.4 Collections

Waiting for more information may have direct cash cost.

If the customer reliably pays after a known processing cycle, waiting may be optimal. If delay probability is rising and escalation is reversible/low-risk, further analysis may have negative net value.

### 9.5 Market Entry

Market entry has large structural uncertainty and potentially expensive irreversibility.

High-value information may include:

- a small sales experiment;
- partner conversations;
- one cooperative-contract test;
- one local BD hire on a limited mandate;
- a fixed-budget pilot.

The system should prefer experiments that reduce the uncertainties most likely to change the scale or direction of commitment.

---

## 10. Architecture implications from the research

These are **proposals for later Chief Architect review**, not canonical contracts.

### Implication A — Information gathering should be treated as an action candidate

“Get more information” is not passive. It consumes time, money, attention, and sometimes relationship capital.

The Decision Engine should be able to compare information-gathering actions with business actions.

### Implication B — Reversal conditions are computationally useful

The R001 decision-anatomy proposal already recommends recording reversal conditions. VOI research shows why:

- reversal conditions identify decision-sensitive variables;
- decision-sensitive variables identify where more information has value;
- information value determines whether to gather, wait, experiment, or decide.

### Implication C — Uncertainty reduction is not itself an objective

A system should not maximize confidence or minimize entropy indiscriminately.

It should reduce uncertainty when doing so improves governed decision quality.

### Implication D — Decision deadlines belong in the reasoning context

Information value depends on when it arrives. Decision timing and option expiry should be available to the reasoning process.

### Implication E — Experiment proposals need authority and ethics controls

An experiment is a governed action. It may affect customers, employees, partners, pricing, or commitments. Research value does not bypass approval, privacy, fairness, or contractual constraints.

### Implication F — LLMs may identify questions, not manufacture numeric VOI

LLMs can help:

- identify material unknowns;
- propose information sources;
- generate candidate experiments;
- reason qualitatively about decision sensitivity;
- explain why more analysis is or is not useful.

A numeric EVPI/EVSI should come from an explicit decision model or remain qualitative/bounded when the required distributions and utilities are not defensible.

---

## 11. Relationship to causal reasoning

R001-07 established that intervention recommendations require causal reasoning when the recommendation depends on what an action will change.

VOI adds the next question:

> If the causal effect is uncertain, is it worth resolving that uncertainty before acting?

The composition is:

```text
INTERVENTION QUESTION
      |
      v
CURRENT CAUSAL EVIDENCE / ASSUMPTIONS
      |
      v
DOES UNCERTAINTY CHANGE THE DECISION?
      |
      +-- NO --> decide under current evidence
      |
      +-- YES --> can information improve the choice in time?
                     |
                     +-- NO --> decide / stage / escalate
                     |
                     +-- YES --> compare information value with cost/delay
                                      |
                                      +-- net positive --> learn more
                                      +-- net nonpositive --> decide
```

---

## 12. Relationship to the current architecture hypothesis

The current Hierarchical Policy Portfolio hypothesis contains sensitivity/challenge before recommendation.

VOI research suggests that this stage should not only challenge the recommendation. It should be capable of producing a distinct result:

```text
NOT ENOUGH DECISION-RELEVANT INFORMATION YET
-> recommended information action
-> expected reason it may change the decision
-> deadline / stopping condition
```

Whether this becomes a shared Decision Engine contract is an `ASK_ARCHITECT` matter. The research conclusion itself remains within ECR scope.

---

## 13. Canonical / high-quality sources

1. Howard, R. A. “Decision Analysis: Practice and Promise.” *Management Science* 34(6), 1988, 679–695. https://doi.org/10.1287/mnsc.34.6.679
2. Howard, R. A. “An Assessment of Decision Analysis.” *Operations Research* 28(1), 1980, 4–27. https://doi.org/10.1287/opre.28.1.4
3. Howard, R. A., Matheson, J. E. “Influence Diagrams.” *Decision Analysis* 2(3), 2005, 127–143. https://doi.org/10.1287/deca.1050.0020
4. Raiffa, H., Schlaifer, R. *Applied Statistical Decision Theory*. Harvard University, 1961. Foundational treatment of sample information and Bayesian decision analysis.
5. DeGroot, M. H. *Optimal Statistical Decisions*. Wiley Classics edition, 2004; original work 1970. https://doi.org/10.1002/0471729000
6. Jackson, C. H. et al. “Value of Information: Sensitivity Analysis and Research Design in Bayesian Evidence Synthesis.” *Journal of the American Statistical Association* / methodological review available via PMC. https://pmc.ncbi.nlm.nih.gov/articles/PMC7034331/
7. Stanford Decision Analysis Group, MS&E 355 — influence diagrams, decision structuring, information states, Bayesian updating. https://dara.stanford.edu/classes/mse-355

---

## 14. Current ECR position

The minimum safe doctrine from this research is:

> **The Decision Engine should seek information for the purpose of improving a decision, not for the purpose of maximizing certainty.**

And:

> **Stop analyzing when additional information is unlikely to change the preferred action enough to justify its cost, delay, or disruption.**

This remains a research conclusion until any shared runtime or semantic contract derived from it is reviewed under `ASK_ARCHITECT`.
