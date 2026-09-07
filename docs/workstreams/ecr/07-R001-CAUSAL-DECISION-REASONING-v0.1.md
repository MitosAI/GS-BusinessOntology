# R001 — Causal Decision Reasoning: Prediction, Intervention, and Policy Choice

**Version:** v0.1  
**Status:** Research finding / architecture input; not canonical architecture  
**Owner:** ECR-001 — Executive Cognition Research Lead  
**Research program:** RESEARCH-001 — Computational Executive Judgment

---

## 1. Why this matters

A decision engine that predicts well can still recommend bad actions.

The core distinction is:

```text
PREDICTIVE QUESTION
What is likely to happen, given what we observe?

vs.

CAUSAL / INTERVENTION QUESTION
What is likely to happen if we deliberately do X instead of Y?
```

These are not interchangeable.

A model can exploit stable correlation to forecast an outcome without identifying what would happen under an intervention. Executive judgment frequently requires the second question because the purpose of a decision is to choose an action that changes the future.

For GenSigma OS, the practical implication is that a forecast must not silently become an intervention claim.

---

## 2. Established findings from the causal-inference literature

### 2.1 Observation and intervention are distinct operations

Pearl's causal framework distinguishes observing `X = x` from intervening to set `X = x`, commonly represented as `P(Y | X=x)` versus `P(Y | do(X=x))`. A causal graph/model is used to determine when interventional quantities can be identified from observational data.

**Implication:** a strong predictive association between a business factor and an outcome does not by itself justify acting on that factor.

### 2.2 Causal questions require a defined action, outcome, and target context

Hernán and Robins frame causal questions around a specific action/intervention, an outcome, and a target population/context. Randomization makes causal comparison especially credible because treatment assignment is independent of the potential outcomes by design.

**Implication:** GenSigma should reject vague causal questions such as "Does partner quality cause wins?" in favor of operationally testable questions such as "For opportunities of class C, what is the expected change in win probability if we add a qualified incumbent partner before proposal submission versus proceeding alone?"

### 2.3 Observational causal inference is possible only under assumptions

Causal effects can sometimes be identified from observational data, but only under assumptions about confounding, treatment assignment, measurement, transportability, and the causal structure. Those assumptions are not automatically established by model fit.

**Implication:** causal assumptions should be exposed as assumptions, not buried inside a model score.

### 2.4 Prediction of future outcomes and forecasts of intervention effects are different tasks

The causal literature explicitly distinguishes forecasting what an outcome will be under the observed/passive system from forecasting the effect of a hypothetical intervention. The second task requires a model of how the data-generating process changes when the intervention occurs.

**Implication:** the Decision Engine should know whether a model is estimating passive-world outcomes or intervention-world outcomes.

### 2.5 Policy choice is not identical to precise causal-effect estimation

Work on causal decision making and policy learning shows that the business objective can be to choose a good policy under constraints rather than to estimate every individual causal effect with maximum point-estimation accuracy. Policy learning can optimize treatment/action assignment subject to budget, fairness, simplicity, and other constraints when causal effects are identified sufficiently for the policy problem.

**Implication:** GenSigma should optimize for decision quality, not for causal-model elegance. The required causal precision depends on whether a decision would change.

---

## 3. Four computational question classes

ECR proposes the following **research classification** for causal reasoning. This is not yet a shared ontology contract.

### Q1 — Descriptive / diagnostic

> What happened? What is associated with what?

Examples:

- Which opportunity attributes correlate with wins?
- Which customers pay most slowly?
- Which partners appear most often in successful proposals?

Suitable methods:

- descriptive statistics;
- retrieval and evidence synthesis;
- association analysis;
- exploratory ML.

No causal claim is implied.

### Q2 — Predictive / passive-world forecast

> What is likely to happen if the current process/policy continues?

Examples:

- What is the probability this opportunity will be won under the current pursuit plan?
- When is this invoice likely to be paid if we take no new collection action?
- What delivery delay is likely under the current staffing plan?

Suitable methods:

- calibrated prediction;
- time-series / survival models;
- probabilistic forecasting;
- reference-class forecasting;
- LLM-supported evidence interpretation where appropriate.

Causal identification is not necessarily required if the output is explicitly passive-world prediction.

### Q3 — Intervention effect

> What would change if we deliberately take action X rather than action Y?

Examples:

- Will adding a partner increase our chance of winning?
- Will escalating collections now accelerate payment enough to justify relationship risk?
- Will adding one senior architect reduce delivery slippage?
- Will lowering price increase expected contribution margin through a higher win probability?

Suitable methods depend on evidence and identification:

- randomized experiments / A-B tests where feasible;
- natural experiments or quasi-experimental designs;
- adjustment for observed confounding;
- instrumental variables / discontinuity / panel methods where defensible;
- structural causal models;
- sensitivity analysis;
- expert causal assumptions when data are insufficient, explicitly labeled.

### Q4 — Policy / sequential intervention choice

> Which action should we choose, for whom, when, and under what constraints?

Examples:

- Which opportunities receive scarce solution-architect attention?
- Which overdue invoices receive an escalation, and at what time?
- Which bids receive price concessions?
- Which partner should be engaged under limited BD capacity?

Suitable methods may combine:

- identified causal effects or response models;
- policy learning;
- optimization;
- dynamic programming / sequential decision methods;
- constraints and authority rules;
- utility / multi-objective evaluation;
- human judgment for unresolved assumptions.

The distinction matters because Q4 is ultimately an action-selection problem, not merely an estimation problem.

---

## 4. Provisional causal-adequacy ladder

To avoid both fake certainty and unnecessary sophistication, ECR proposes this **research-only adequacy ladder**.

### C0 — Association only

Evidence supports correlation/association but not an intervention claim.

Allowed output:

- descriptive insight;
- predictive signal if independently validated;
- hypothesis for experimentation.

Not allowed:

- "doing X will cause Y" language.

### C1 — Causal hypothesis

A plausible mechanism exists and the intervention/outcome are well defined, but confounding or identification remains materially unresolved.

Allowed output:

- scenario analysis;
- assumption-explicit recommendation;
- experiment / information-gathering proposal.

### C2 — Identified observational effect

A causal estimand is identified under stated, defensible assumptions using observational or quasi-experimental data, with sensitivity analysis where material.

Allowed output:

- intervention-effect estimate with explicit assumptions and uncertainty;
- policy analysis if the decision is not highly sensitive to remaining uncertainty.

### C3 — Experimental / strongly validated causal effect

The intervention has credible experimental or otherwise unusually strong causal evidence in a sufficiently comparable context.

Allowed output:

- higher-confidence intervention reasoning;
- policy optimization subject to transportability, execution, cost, authority, and changing-context risks.

**Rule:** a downstream component must not silently promote C0/C1 evidence into C2/C3 because a numerical optimizer expects a causal coefficient.

---

## 5. Minimum causal decision packet

For an intervention-sensitive recommendation, the reasoning trace should be able to answer the following, at least logically:

```text
INTERVENTION
What action are we considering?

COMPARATOR
Compared with what alternative / status quo?

TARGET
For which opportunity, customer, project, employee, invoice, market, or other unit/context?

OUTCOME
What consequence are we trying to change?

HORIZON
Over what time period?

CAUSAL CLAIM
What effect do we believe the intervention has on the outcome?

IDENTIFICATION BASIS
Experiment, quasi-experiment, observational adjustment, structural assumption,
expert mechanism, analogy/reference class, or unresolved hypothesis?

CONFOUNDERS / ASSUMPTIONS
What must be true for the estimate to be interpreted causally?

UNCERTAINTY / SENSITIVITY
How much would the conclusion change if assumptions or effect sizes change?

TRANSPORTABILITY
Why should evidence from prior cases apply here?

DECISION RELEVANCE
Would plausible changes in the causal estimate actually change the recommendation?
```

This packet is a research requirement for auditable judgment. It does **not** imply that every field should become a new canonical ontology property or object.

---

## 6. Decision logic: when causal reasoning is required

A practical routing rule is:

```text
Does the question only ask what is likely to happen under current behavior?
    |
    +-- YES --> predictive reasoning may be sufficient
    |
    +-- NO --> Does the recommendation depend on choosing an action
               because of its expected effect?
                    |
                    +-- NO --> causal model may be unnecessary
                    |
                    +-- YES --> causal/intervention reasoning required
                                  |
                                  +--> Is credible causal evidence available?
                                  |       |
                                  |       +-- YES --> estimate effect + uncertainty
                                  |       |
                                  |       +-- NO --> assumptions/scenarios/experiment
                                  |
                                  +--> Does remaining uncertainty change the choice?
                                          |
                                          +-- NO --> act under bounded uncertainty
                                          |
                                          +-- YES --> gather information / experiment /
                                                     stage commitment / escalate
```

The last step links causal reasoning directly to value-of-information and staged-commitment research.

---

## 7. GenSigma pressure tests

### 7.1 Bid / No-Bid

Predictive question:

> What is our probability of winning if we pursue under the current plan?

Causal questions:

- What is the incremental effect of adding a particular teaming partner?
- What is the effect of increasing executive engagement?
- What is the effect of lowering price or changing solution scope?

A win-probability model trained on historical bids may answer the first question while being unsafe for the latter three if historical actions were confounded by opportunity quality.

Example confounding:

- executives may engage more heavily on already-promising opportunities;
- strong partners may be recruited on strategically important opportunities;
- discounts may be offered when a deal is already difficult.

Naive historical correlation could therefore reverse or distort the action effect.

### 7.2 Staffing / Resource Assignment

Predictive question:

> Under the current team, what is the probability of missing the milestone?

Causal question:

> What is the expected reduction in delay risk if we add a senior engineer for the next four weeks?

Teams are not assigned randomly. Difficult projects often receive stronger staff, so historical correlation between senior staffing and poor outcomes can be misleading without intervention reasoning.

### 7.3 Collections Escalation

Predictive question:

> When will this customer probably pay if the current follow-up pattern continues?

Causal question:

> Will an executive escalation now accelerate payment enough to justify relationship cost?

Accounts selected for escalation are usually the hardest cases. A raw comparison of escalated versus non-escalated invoices may make escalation look ineffective even when it helps.

### 7.4 Pricing

Predictive question:

> At the current proposed price, what is the likely win probability and margin outcome?

Causal question:

> What would a 5% price reduction do to win probability, expected gross profit, and long-term account value?

This is an intervention problem with strategic-response effects; competitor/customer reaction may require causal + game-theoretic reasoning rather than predictive modeling alone.

---

## 8. Research-backed architecture implications

These are **ECR proposals**, not architecture decisions.

### Implication A — Forecast provenance should include question type

A prediction artifact or method trace should distinguish at minimum:

- passive-world prediction;
- intervention-effect estimate;
- counterfactual/scenario analysis;
- policy recommendation.

This prevents semantic leakage from prediction into causation.

### Implication B — Causal assumptions should be first-class in the decision trace

If an action recommendation relies on a causal effect, the material assumptions and identification basis should be inspectable.

The assumptions may live in a model/method artifact, trace structure, evidence graph, or other KOE-approved representation. ECR does not prescribe ontology placement.

### Implication C — LLM causal prose must not be treated as causal identification

An LLM can:

- propose mechanisms;
- identify potential confounders;
- construct candidate causal diagrams;
- critique causal claims;
- explain assumptions;
- translate natural language into an analysis plan.

It cannot establish identification merely by producing a plausible story.

### Implication D — Experimentation is part of cognition, not an afterthought

When causal uncertainty is decision-relevant and an experiment is feasible, a high-quality executive system should be able to recommend an experiment, pilot, staged rollout, or information-gathering action instead of forcing a premature answer.

### Implication E — Causal and strategic-response reasoning can compose

A pricing action may have:

- direct customer response;
- competitor response;
- signaling effects;
- future negotiation effects.

The causal module should therefore not assume that all interventions occur in a passive environment. Game-theoretic or strategic-response modules may be needed for some decision classes.

### Implication F — Causal evidence has a transportability problem

Even a strong historical or experimental effect may not carry directly into a new customer, market, contract vehicle, team, or economic environment.

The system should ask whether the intervention, population/context, implementation, and outcome definition are sufficiently comparable before reusing an effect estimate.

---

## 9. What should remain deterministic

Causal reasoning does not replace hard constraints.

Examples:

- an expired registration blocks eligibility regardless of modeled win uplift;
- an approval threshold applies regardless of estimated intervention value;
- a budget ceiling constrains policy choice regardless of causal benefit;
- legal/employment authority remains governed even if a model predicts positive outcome.

The correct composition is:

```text
DETERMINISTIC POLICY / AUTHORITY / FEASIBILITY
                 |
                 v
          CAUSAL EFFECT QUESTION
                 |
                 v
     UNCERTAINTY + VALUE / TRADE-OFF
                 |
                 v
         RECOMMEND / DECIDE / ACT
```

---

## 10. Relationship to the Hierarchical Policy Portfolio hypothesis

This research strengthens one part of the current ECR architecture hypothesis:

> Method routing should depend not only on decision class, but also on the **question type** being asked.

A Bid / No-Bid workflow may invoke:

- prediction for passive win probability;
- causal reasoning for proposed pursuit interventions;
- optimization for resource allocation;
- game theory for competitor/customer response;
- qualitative judgment for novel strategic factors;
- deterministic gates for eligibility, authority, and policy.

This supports the policy-portfolio idea, but the architecture remains subject to `ADRQ-ECR-001` and Chief Architect resolution.

---

## 11. Open research questions carried forward

1. How should causal assumptions and identification strength be represented without overloading the canonical ontology?
2. When is a causal estimate decision-useful even if statistically imprecise?
3. How should GenSigma score transportability from historical cases to a new decision context?
4. What classes of GenSigma decisions can support randomized or quasi-randomized experimentation?
5. How should policy learning interact with fairness, customer relationship, employee impact, and authority constraints?
6. How should causal uncertainty feed value-of-information and stopping rules?
7. How should the system distinguish model error from intervention-execution failure after an outcome occurs?

Items 1 and any resulting shared contract change are `ASK_ARCHITECT` once a concrete architecture proposal is ready. Items 2–7 remain ECR `LOCAL_SOLVE` research work until they imply a cross-workstream contract.

---

## 12. Canonical / high-quality sources

1. Pearl, J. *Causality: Models, Reasoning, and Inference*, 2nd ed., Cambridge University Press, 2009. Intervention semantics and the `do` operator. UCLA materials: https://bayes.cs.ucla.edu/BOOK-09/
2. Pearl, J., Glymour, M., Jewell, N. *Causal Inference in Statistics: A Primer*. Intervention-versus-observation distinction. UCLA primer materials: https://bayes.cs.ucla.edu/PRIMER/
3. Hernán, M. A., Robins, J. M. *Causal Inference: What If*, 2020, continuously updated online edition. https://miguelhernan.org/whatifbook
4. Peters, J., Janzing, D., Schölkopf, B. *Elements of Causal Inference: Foundations and Learning Algorithms*. MIT Press, 2017. https://mitpress.mit.edu/9780262037310/elements-of-causal-inference/
5. Dawid, A. P. “Decision-theoretic foundations for statistical causality.” *Journal of Causal Inference* 9(1), 2021, 39–77. https://doi.org/10.1515/jci-2020-0008
6. Gische, C., West, S. G., Voelkle, M. C. “Forecasting Causal Effects of Interventions versus Predicting Future Outcomes.” *Structural Equation Modeling* 28(3), 2021, 475–492. https://doi.org/10.1080/10705511.2020.1780598
7. Athey, S., Wager, S. “Policy Learning with Observational Data.” *Econometrica* 89(1), 2021, 133–161. https://www.gsb.stanford.edu/faculty-research/publications/policy-learning-observational-data
8. Provost, F. et al. “Causal Decision Making and Causal Effect Estimation Are Not the Same…and Why It Matters.” *INFORMS Journal on Data Science*, 2022. https://doi.org/10.1287/ijds.2021.0006

---

## 13. Current ECR position

The minimum safe doctrine from this research is:

> **Prediction estimates what happens under a specified observational/passive regime. Causal reasoning estimates what changes under an intervention. A decision engine must know which question it is answering.**

And:

> **No intervention recommendation should inherit causal authority merely because a predictive model is accurate.**

These are research conclusions. Any new shared semantic contract derived from them remains subject to the repository `ASK_ARCHITECT` protocol.
