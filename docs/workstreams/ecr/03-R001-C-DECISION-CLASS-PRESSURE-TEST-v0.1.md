# R001-C — Decision-Class Pressure Test and Method Routing

**Version:** v0.1  
**Status:** First-session research artifact; provisional  
**Owner:** Executive Cognition Research Lead (ECR-001)

---

## 1. Purpose

The first-session plan requires Research 001 to pressure-test the discipline map against at least five real GenSigma decision classes before proposing architecture.

This artifact tests eight classes so that the emerging architecture is not overfit to one commercial pursuit.

The method map is intentionally plural. It asks which computational techniques are justified by the structure of each decision, not which technique is fashionable.

---

## 2. Routing principles

1. **Hard constraints first.** Ineligible options should not enter probabilistic ranking as if they were merely low scoring.
2. **Probability must be earned.** Numeric probability is used only where reference classes, models, or explicit probabilistic assumptions are defensible.
3. **Optimization follows objective definition.** A solver is valuable only after the objective, constraints and feasible action space are sufficiently explicit.
4. **Game-theoretic analysis is conditional.** Activate only when another actor's adaptive response can materially change the ranking of alternatives.
5. **LLMs are primarily interpreters/generators/orchestrators.** They should not own arithmetic, policy enforcement, permissions, canonical truth or optimization guarantees.
6. **Novel strategic choices remain human-governed.** Formal analysis can improve decision quality without pretending the problem is fully specified.

---

## 3. Decision class: Bid / No-Bid

### Decision question

Should GenSigma pursue a specific opportunity, and at what pursuit intensity?

### Inputs

- strategic fit / Business Intent;
- eligibility and hard solicitation requirements;
- customer/account importance;
- capability and partner coverage;
- delivery capacity;
- pursuit cost and founder/team time;
- expected economics;
- win likelihood where estimable;
- opportunity cost;
- schedule/deadline feasibility;
- material risks.

### Method routing

- **Deterministic rules:** mandatory eligibility, certification, registration, submission requirements, deadlines, approval thresholds.
- **Bayesian/forecasting:** win probability only when usable base rates or calibrated forecasting evidence exists.
- **Multi-criteria decision analysis:** strategic fit, repeatability, customer importance, founder burden, capability fit, downside.
- **Expected value:** useful only if probability/economic ranges are defensible.
- **Optimization:** portfolio-level allocation of limited pursuit resources across many opportunities, not necessarily the single yes/no choice itself.
- **LLM:** extract solicitation requirements, synthesize account context, generate missing questions, propose alternatives such as prime/sub/decline/watch.
- **Human authority:** high-value exceptions, strategic account overrides, ambiguous long-term bets.

### Key failure mode

A precise-looking weighted score can hide weak win probability, correlated criteria, missing opportunity cost, or a strategic veto.

---

## 4. Decision class: Teaming Partner Selection

### Decision question

Which partner structure best improves the probability and quality of pursuing/delivering an opportunity?

### Inputs

- required capabilities;
- partner demonstrated capability and availability;
- customer relevance;
- certifications/vehicles;
- economics and margin split;
- prior performance;
- responsiveness/trust;
- exclusivity/conflicts;
- negotiation posture;
- delivery risk;
- long-term ecosystem value.

### Method routing

- **Deterministic rules:** eligibility, conflicts, required certifications, prohibited relationships, NDA/contract prerequisites.
- **MCDA:** capability fit, relationship, responsiveness, economics, delivery risk, repeatability.
- **Probability:** partner-dependent win or delivery effects only when defensible.
- **Game theory / bargaining:** material when exclusivity, margin split, counteroffers, multi-partner competition or credible walk-away positions affect the result.
- **Optimization:** useful for multi-partner composition when multiple capability gaps must be covered under cost/capacity constraints.
- **LLM:** summarize evidence, surface hidden dependencies, generate partner-combination alternatives, simulate negotiation arguments.
- **Human authority:** relationship/reputation-sensitive partner commitments.

### Key failure mode

Treating “partner quality” as a timeless score rather than context-specific capability, incentives, availability and relationship state.

---

## 5. Decision class: Pricing / Commercial Structure

### Decision question

What price, margin, risk allocation and commercial structure should GenSigma propose?

### Inputs

- cost structure and rate cards;
- capacity and subcontract costs;
- target margin / floor;
- customer budget signals;
- competitive environment;
- contract/payment terms;
- demand elasticity where known;
- strategic-account value;
- probability of award at different structures;
- delivery/collection risk.

### Method routing

- **Deterministic:** arithmetic, cost floors, required margin guardrails, contractual constraints.
- **Scenario / simulation:** margin and cash consequences under utilization, delay, subcontract and scope assumptions.
- **Optimization:** price/structure under explicit margin, capacity and risk constraints where response curves are credible.
- **Probability:** award likelihood or collection risk only if estimable.
- **Game theory / bargaining:** negotiation, anchoring, counterparty reservation values, response to concessions.
- **LLM:** interpret customer language, generate packaging options, synthesize negotiation positions.
- **Human authority:** final strategic pricing exceptions and risk acceptance.

### Key failure mode

Optimizing price against an invented demand curve or unvalidated win-probability function.

---

## 6. Decision class: Staffing / Resource Assignment

### Decision question

Which people/partners should be assigned to which projects or pursuits, when, under what constraints?

### Inputs

- skills/credentials;
- availability and capacity;
- project requirements;
- rates/costs;
- geography/time zone;
- continuity/customer preferences;
- labor/legal constraints;
- development goals;
- workload and deadlines.

### Method routing

- **Deterministic:** qualification, availability, labor rules, schedule conflicts.
- **Optimization:** strong fit for assignment, scheduling, capacity balancing and cost minimization/maximization subject to constraints.
- **Probability:** delivery risk, attrition or uncertain future availability where calibrated enough to matter.
- **MCDA:** softer client/team fit factors not captured in hard constraints.
- **LLM:** extract requirements, summarize qualitative feedback, identify hidden mismatch risks.
- **Human authority:** sensitive people decisions, exceptions, performance-related assignments.

### Key failure mode

Letting a qualitative LLM recommendation replace a tractable assignment optimization problem.

---

## 7. Decision class: Collections Escalation

### Decision question

Which receivable should be escalated, how aggressively, and through which action path?

### Inputs

- amount and age;
- contractual due date;
- customer payment history;
- dispute status;
- relationship importance;
- cash need;
- communication history;
- likelihood/timing of payment;
- legal/contract rights;
- reputational cost of escalation.

### Method routing

- **Deterministic:** due dates, contractual rights, aging thresholds, mandatory notice requirements.
- **Risk scoring / probability:** payment-delay/default estimates if supported by history/reference classes.
- **Optimization:** collections prioritization under limited staff time and cash objectives.
- **Control / feedback:** escalation ladder that increases/decreases intervention based on observed response.
- **LLM:** summarize communications, detect dispute/context, draft escalation options.
- **Human authority:** relationship-sensitive legal/escalation decisions.

### Key failure mode

Treating aged receivables as homogeneous and ignoring dispute/relationship context.

---

## 8. Decision class: Market Entry / Strategic Expansion

### Decision question

Should GenSigma enter, deepen or exit a market/geography/offering?

### Inputs

- strategic fit;
- market attractiveness;
- customer access;
- competitive position;
- required capability investment;
- contract vehicles/certifications;
- capital and founder attention;
- reversibility;
- time to learn;
- option value;
- external policy/technology/regulatory conditions.

### Method routing

- **Deterministic:** legal/regulatory eligibility and hard capital constraints.
- **Scenario planning:** central; multiple futures rather than one forecast.
- **Real options:** useful for staged entry, pilot-before-scale, abandonment/expansion options.
- **Probability:** only where market/customer reference classes support it; uncertainty will often remain qualitative.
- **Game theory:** material when incumbent/competitor/customer response changes attractiveness.
- **LLM:** synthesize external evidence, generate hypotheses, construct scenarios and challenge assumptions.
- **Human/board authority:** primary; high irreversibility and strategic consequences.

### Key failure mode

Converting sparse strategic uncertainty into a fake NPV/probability model that hides assumptions.

---

## 9. Decision class: Capital Allocation

### Decision question

How should finite capital be allocated among operating needs, growth investments, acquisitions, debt reduction, reserves or other uses?

### Inputs

- cash/liquidity;
- obligations and runway;
- risk appetite;
- expected return distributions;
- strategic fit;
- correlations/dependencies;
- reversibility/liquidity;
- capability/management bandwidth;
- tax/legal constraints.

### Method routing

- **Deterministic:** liquidity floors, debt covenants, mandatory obligations.
- **Portfolio/optimization:** useful when return/risk assumptions are defensible and constraints explicit.
- **Scenario/stress testing:** essential for downside and liquidity.
- **Probability:** model uncertainty must be explicit; strategic investments may not support precise distributions.
- **Real options:** staged funding/commitment where learning changes later choices.
- **LLM:** synthesize qualitative strategic considerations and generate investment cases, not own calculations.
- **Human/board authority:** high.

### Key failure mode

Optimizing against point-estimate returns that conceal model error and illiquidity.

---

## 10. Decision class: Hiring / Termination / Critical People Decision

### Decision question

Should GenSigma hire, retain, redeploy, promote or terminate a person in a material role?

### Inputs

- job requirements;
- performance evidence;
- capability fit;
- behavior/values evidence;
- legal/HR policy;
- team impact;
- replacement cost/time;
- business need;
- compensation economics;
- documented feedback and commitments.

### Method routing

- **Deterministic:** legal/HR process, required approvals, documentation, policy.
- **Structured evidence / MCDA:** role fit and evidence-based criteria with explicit uncertainty.
- **Probability:** limited and high-risk; avoid pseudo-scientific prediction of human behavior without validated models.
- **Behavioral-debiasing:** particularly important for recency, affinity, halo/horns, attribution and escalation biases.
- **LLM:** summarize documented evidence and identify missing/contradictory records; must not infer protected/sensitive traits.
- **Human authority:** required for consequential employment actions.

### Key failure mode

Automating subjective people judgments with opaque scores or inferred traits.

---

## 11. Cross-class method matrix

Legend: **P** primary, **S** supporting, **C** conditional, **—** generally not central.

| Decision class | Rules | Probability/Bayes | MCDA/Utility | Optimization | Game/Bargaining | Scenario/Control | LLM | Human authority |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Bid/no-bid | P | C | P | C | C | S | S | P |
| Partner selection | P | C | P | C | C/P | S | S | P |
| Pricing | P | C | S | P/C | P/C | P | S | P |
| Staffing | P | C | S | P | — | S | S | C/P |
| Collections | P | C | S | C | C | P | S | P |
| Market entry | P | C | P | C | C | P | S | P |
| Capital allocation | P | C | P | C/P | — | P | S | P |
| People decision | P | C/low | P | — | — | S | S | P |

---

## 12. Provisional routing architecture

The pressure test supports a routing model rather than a universal method:

```text
classify decision
      |
      v
apply hard constraints + authority
      |
      v
assess uncertainty quality
      |
      v
select analytical modules
      |
      +--> criteria/value model
      +--> forecast/Bayes
      +--> optimization
      +--> scenario/simulation
      +--> strategic interaction
      +--> structured qualitative judgment
      +--> behavioral challenge
      |
      v
sensitivity / reversal conditions
      |
      v
recommendation -> decision -> approval -> action
```

The routing policy itself should become testable and versioned.

---

## 13. Implications for first prototype selection

The strongest early prototype candidate remains **bid/no-bid** because it:

- occurs frequently;
- has meaningful but bounded stakes;
- links directly to the RFP-to-Cash ontology chain;
- exercises Intent, Business Reality, External Reality and Capability together;
- contains both hard gates and soft judgment;
- permits comparison against historical outcomes;
- can incorporate probability when defensible without requiring it;
- is understandable to human reviewers.

A second strong candidate is **staffing/resource assignment** because it is more directly optimizable and provides a useful contrast to LLM-heavy judgment.

Selection of the formal M11 prototype remains a Chief Architect/integration decision after the first gate.
