# R001 — Delegated Decision Rights and Authority Envelopes

**Status:** Research output; architecture implications are provisional until Chief Architect review.

## Core finding

AI autonomy should not be a binary `allowed / not allowed` setting. Delegation should be scoped by decision class, stakes, risk, reversibility, evidence quality, and action authority.

Aghion and Tirole distinguish **formal authority** (the right to decide) from **real authority** (effective control produced by information and initiative). This matters directly for AI systems: an agent may lack formal approval authority yet still exercise substantial real influence by controlling what evidence, alternatives, or recommendations decision makers see.

Canonical source:
- Philippe Aghion & Jean Tirole, "Formal and Real Authority in Organizations," *Journal of Political Economy* 105(1), 1997.

## Proposed authority-envelope concept

A decision authority envelope is a runtime boundary such as:

```text
actor / agent
  + decision class
  + business scope
  + financial/stake limit
  + risk class
  + reversibility class
  + evidence / confidence threshold
  + allowed actions
  + approval requirements
  + time validity
  + escalation destination
```

This is a research abstraction, not an approved canonical schema.

## Four practical authority levels

### A0 — Observe / analyze
May retrieve authorized context, compute, summarize, identify issues.

### A1 — Recommend
May produce a recommendation but cannot select or execute the business decision.

### A2 — Decide within delegated envelope
May select a decision where policy explicitly delegates that class/stake/risk combination.

### A3 — Decide + execute governed action
May decide and invoke specified typed actions when preconditions and control policy are satisfied.

The levels should not be globally assigned to an agent. The same agent may be A3 for a routine low-risk action and A1 for a strategic or personnel decision.

## Escalation triggers

Escalate outside the envelope when any material condition holds:
- stake exceeds threshold;
- action is hard to reverse;
- uncertainty exceeds policy threshold;
- evidence conflict remains unresolved;
- decision touches legal/employment/fiduciary/reputational risk;
- new value tradeoff is required;
- proposed action violates or requires reinterpretation of policy;
- model detects novel/out-of-distribution case;
- decision requires authority not explicitly delegated.

## Separation of powers

Where consequence warrants it, GenSigma should separate:
- evidence assembly;
- recommendation generation;
- decision authority;
- approval authority;
- action execution;
- outcome verification.

One AI process need not own all stages merely because it technically can.

## Real-authority risk

Even recommendation-only systems can exert real authority through:
- evidence selection;
- ranking alternatives;
- framing the decision question;
- choosing the baseline;
- setting default assumptions;
- deciding when to escalate.

Therefore auditability must include **framing and information selection**, not only the final recommendation.

## Delegation design principle

Delegate when:
- the decision class is understood;
- relevant constraints are explicit;
- outcomes are measurable enough to audit;
- downside is bounded;
- actions are reversible or containable;
- exception/escalation paths are clear.

Retain human authority when:
- values themselves are being chosen;
- strategic intent changes;
- irreversible/high-consequence commitments are made;
- legal or human consequences are significant;
- policy does not cover the situation.

## Architecture implication

The Decision Engine proposal should evaluate authority **before** recommendation-to-action handoff, not bolt approval on afterward.

Changing shared authority/security semantics is explicitly `ASK_ARCHITECT`. ECR therefore proposes requirements but does not modify the canonical authority model itself.
