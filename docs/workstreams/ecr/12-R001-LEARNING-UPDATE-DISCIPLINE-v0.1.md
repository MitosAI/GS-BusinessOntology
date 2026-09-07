# R001 — Learning and Update Discipline

**Status:** Research output; architecture implications are provisional until Chief Architect review.

## Core finding

Learning must be governed by **what kind of thing is allowed to change**. An outcome should not automatically rewrite strategy, policy, or beliefs.

Argyris and Schön distinguish single-loop learning (change actions while governing variables remain fixed) from double-loop learning (question governing assumptions/values). This maps cleanly to GenSigma's need for different update tempos.

Sources:
- Chris Argyris, "Double Loop Learning in Organizations," Harvard Business Review, 1977.
- Argyris & Schön, *Organizational Learning* / later double-loop literature.

## Proposed learning ladder

```text
L0 RECORD
Capture outcome and verification only.

L1 PARAMETER UPDATE
Update empirical rate, estimate, calibration statistic, model parameter.

L2 HEURISTIC / POLICY-TUNING PROPOSAL
Propose changing a decision rule, threshold, routing policy, or operating heuristic.

L3 MODEL / ASSUMPTION REVISION
Propose changing causal assumptions, reference classes, decision model, or strategic belief.

L4 INTENT / GOVERNANCE CHANGE
Propose changing goals, risk appetite, values, authority, or strategic direction.
```

L0-L1 may eventually support substantial automation. L2-L4 require progressively stronger governance.

## Update eligibility

Before learning from an outcome, ask:
- Was the decision actually executed?
- Was the outcome observable and attributable enough?
- Was the original forecast/recommendation preserved ex ante?
- Did execution deviate materially from the plan?
- Were external shocks material?
- Is this one case or a repeated pattern?
- Does the evidence support parameter update versus model change?

## Prevent hindsight contamination

The system must preserve:
- evidence available at decision time;
- assumptions at decision time;
- forecast at decision time;
- chosen action;
- execution deviations;
- later-arriving evidence;
- actual outcome.

Do not score the decision using facts that were unavailable when it was made.

## Outcome taxonomy

Learning should distinguish at least:
- expected good outcome;
- expected bad outcome;
- lucky good outcome;
- unlucky bad outcome;
- execution failure;
- model/forecast error;
- assumption failure;
- policy/constraint failure;
- external shock;
- measurement ambiguity.

## Single-case restraint

One success or failure should rarely cause strategy mutation.

The default rule should be:
- update observation/history immediately;
- update statistics when methodologically valid;
- propose heuristic/model change only when evidence threshold is met;
- never silently alter Business Intent from observed behavior/outcomes.

## Decision-quality review

A post-decision review should score at least:
1. framing quality;
2. evidence quality;
3. alternative coverage;
4. method appropriateness;
5. uncertainty honesty;
6. authority/process compliance;
7. execution quality;
8. forecast calibration where applicable;
9. outcome;
10. lesson/update proposal.

Outcome is only one dimension.

## Architecture implication

The learning loop should emit **typed change proposals** rather than directly mutating higher-order governed state.

Exact shared semantics, approval workflow, and canonical change-proposal representation are `ASK_ARCHITECT` matters. The research conclusion is that update targets and governance levels must be explicit.
