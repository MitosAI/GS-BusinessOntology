# ADR-003 — Executive Cognition Working Architecture

**Status:** Accepted as working architecture; subject to prototype validation  
**Decision owner:** Chief Architect  
**Date:** 2026-09-05

## Context

Executive Cognition Research evaluated decision analysis, Bayesian decision theory, operations research, game theory, control theory, behavioral decision science, strategic management, AI reasoning/planning, and command-and-control. The research concluded that GenSigma decisions differ materially by decision class and should not be forced through one universal analytical method.

ECR requested decisions on: (1) the working Decision Engine architecture, (2) shared semantic requirements implied by the research, and (3) the first M11 prototype decision class.

## Decision

### 1. Working architecture

Adopt the **Hierarchical Policy Portfolio** as the working Decision Engine architecture.

It combines:

- a common decision anatomy and deterministic governance/authority shell;
- slower Business Intent / strategy / policy constraints governing faster operational decisions;
- explicit decision-class routing to appropriate analytical methods;
- modular use of rules, probabilistic/Bayesian methods, optimization, scenario analysis, strategic-interaction methods, causal/predictive models, and LLM-assisted interpretation/orchestration;
- challenge/sensitivity analysis before recommendation where material;
- governed approval/action;
- outcome capture and learning.

This is a working architecture, not a claim that every module runs for every decision.

### 2. Shared semantic requirements

Approve the following as **cross-cutting semantic/query requirements**, not automatically as new canonical object types:

1. **Probability adequacy** — distinguish unquantified, qualitative, empirical/reference-class, and calibrated-model probabilities where relevant.
2. **Multidimensional uncertainty** — represent materially different uncertainty sources rather than collapsing them into one confidence score.
3. **Ex-ante expectations** — preserve expected outcomes/assumptions before action so decision quality can later be evaluated independently of realized outcome.
4. **Reversal / sensitivity conditions** — preserve what evidence, parameter, or assumption changes would materially reverse a recommendation where relevant.
5. **Decision-method provenance** — record which rules, models, optimizers, LLM judgments, human judgments, and other analytical methods materially contributed.
6. **Causal-versus-predictive distinction** — do not semantically collapse forecast correlation/prediction with causal intervention claims.

Knowledge/Ontology Engineering must determine the smallest coherent representation of these requirements and avoid object proliferation.

### 3. M11 prototype

Approve **Bid / No-Bid** as the first formal M11 computational decision prototype.

Use **Staffing / Resource Assignment** as the contrast decision class to test whether method routing genuinely differs for an optimization-heavy problem.

## Rationale

A policy portfolio avoids forcing unlike decisions through one method, while the hierarchy preserves strategic intent, authority, risk, and timescale. This keeps the Decision Engine deterministic where governance can be explicit and probabilistic/analytical where uncertainty requires it.

The semantic additions are required for auditability and learning, but should initially be represented through shared decision-context/assessment structures rather than proliferating new top-level ontology objects.

Bid / No-Bid is selected because it is frequent, consequential, data-rich, bounded enough to evaluate, and combines qualitative judgment with explicit criteria and uncertainty. Staffing provides a useful contrast because constraints and optimization should play a larger role.

## Constraints

- LLMs are components, not the sole Decision Engine.
- No fabricated numerical probabilities.
- Formal methods are invoked only when appropriate to the decision class and available evidence.
- Human/organizational authority remains explicit.
- This ADR does not choose a model vendor, database, agent framework, or physical runtime.

## Validation gates

Before this working architecture becomes a stronger frozen design, M11 must demonstrate:

- auditable method routing;
- explicit inputs/assumptions;
- useful sensitivity/reversal analysis;
- measurable comparison with a simpler baseline;
- correct handling of missing/weak probability evidence;
- traceability from recommendation to evidence, intent, constraints, and methods.

If the prototype shows the router/hierarchy adds complexity without decision-quality benefit, revisit this ADR.