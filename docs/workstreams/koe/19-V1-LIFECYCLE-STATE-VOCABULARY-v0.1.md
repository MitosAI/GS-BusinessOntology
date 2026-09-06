# Business Reality V1 — Lifecycle State Vocabulary

**Version:** v0.1  
**Status:** KOE semantic baseline  
**Owner:** Knowledge & Ontology Engineering (KOE-001)

---

## 1. Purpose

State names are semantic contracts, not UI labels. This document defines the minimum lifecycle vocabularies for V1 objects so services, schemas, agents, and applications do not invent incompatible state machines.

States may be extended by domain contract version, but their meaning must remain explicit and auditable.

---

## 2. General rules

1. State is temporal and effective-dated where material.
2. State transitions preserve prior state history.
3. Unknown/unresolved is different from inactive/closed.
4. A source label does not automatically become canonical lifecycle state.
5. State transitions may require evidence, approval, or action depending on object type.
6. Correction of a wrong state is not the same thing as a new business transition.
7. Derived state must identify its derivation basis.

---

# 3. Identity / structure states

## Organization

```text
active
inactive
dissolved
unknown
```

## LegalEntity

```text
forming
active
inactive
dissolved
merged
unknown
```

## OrganizationalUnit

```text
planned
active
reorganizing
retired
unknown
```

## Person

No employment-style lifecycle is attached directly to Person.

Optional identity record status:

```text
active_known
historical_known
deceased
unknown
```

## Position

```text
planned
open
filled
suspended
retired
unknown
```

## Place

Generally no business lifecycle beyond:

```text
active_reference
historical_reference
superseded_reference
```

---

# 4. Relationship / commercial states

## BusinessRelationship

```text
proposed
active
suspended
terminated
expired
superseded
unresolved
```

## Opportunity

```text
discovered
qualifying
pursuing
submitted
awarded
lost
cancelled
dormant
closed
unknown
```

Rules:
- `awarded` is not inferred from optimism or proposal submission.
- `lost` requires sufficient outcome evidence.
- `closed` is administrative lifecycle closure and should retain outcome reason.

## Solicitation

```text
anticipated
draft
issued
amended
closed
cancelled
awarded
complete
unknown
```

## Offering

```text
proposed
active
revised
retired
unknown
```

## Proposal

```text
drafting
in_review
approved
submitted
revised
resubmitted
withdrawn
accepted
rejected
expired
unknown
```

## Agreement

```text
draft
negotiating
approved
executed
active
amended
expired
terminated
superseded
unknown
```

Rules:
- `executed` means execution evidence exists.
- `active` may depend on effective date after execution.
- amendment does not erase prior agreement version.

## Obligation

```text
proposed
active
satisfied
waived
breached
expired
superseded
unknown
```

## ContractVehicle

```text
planned
active
suspended
expired
renewed
superseded
unknown
```

---

# 5. Delivery and finance states

## Project

```text
planned
active
paused
completed
cancelled
closed
unknown
```

## Milestone

```text
planned
due
achieved
missed
cancelled
superseded
unknown
```

## Deliverable

```text
planned
in_progress
submitted
accepted
rejected
rework
completed
cancelled
unknown
```

## Budget

```text
proposed
approved
active
revised
frozen
closed
superseded
unknown
```

## Invoice

```text
draft
issued
partially_paid
paid
disputed
voided
written_off
unknown
```

## Payment

```text
initiated
pending
settled
failed
reversed
refunded
adjusted
unknown
```

---

# 6. Workforce / capability states

## Assignment

```text
proposed
planned
active
paused
completed
cancelled
unknown
```

## Capability

```text
recognized
developing
available
constrained
retired
unknown
```

Important: this is capability identity maturity/status, not real-time feasibility.

## Skill

```text
active
deprecated
superseded
unknown
```

## Credential

```text
pending
active
expired
suspended
revoked
superseded
unknown
```

## Certification

```text
applied
pending
active
suspended
expired
revoked
renewed
superseded
unknown
```

---

# 7. Systems / technology states

## Asset

```text
planned
acquired
active
assigned
maintenance
retired
disposed
unknown
```

## System

```text
planned
development
active
degraded
deprecated
retired
unknown
```

## Technology

```text
current
deprecated
end_of_support
retired
superseded
unknown
```

---

# 8. Legal / compliance states

## Registration

```text
pending
active
delinquent
suspended
expired
withdrawn
renewed
superseded
unknown
```

---

# 9. Knowledge / judgment / control states

## Artifact

```text
draft
active
final
superseded
archived
unknown
```

These describe the canonical artifact lifecycle, not source-file availability.

## Event

Events do not use a conventional business lifecycle. Interpretation status is handled through epistemic/supersession semantics.

Optional processing status is implementation-layer only and must not be confused with Event truth.

## Claim

```text
proposed
supported
contradicted
accepted
rejected
superseded
unresolved
```

## Assessment

```text
draft
issued
reviewed
withdrawn
superseded
```

## Risk

```text
identified
assessed
accepted
mitigating
monitoring
realized
closed
unknown
```

## Decision

```text
proposed
pending
made
superseded
reversed
expired
unknown
```

## Approval

```text
requested
approved
rejected
revoked
expired
superseded
unknown
```

## Action

```text
proposed
authorized
queued
in_progress
succeeded
failed
cancelled
compensated
unknown
```

## Outcome

```text
observed
provisional
confirmed
revised
superseded
unknown
```

---

## 10. State transition contract

A material transition record should conceptually preserve:

```text
resource_ref
from_state?
to_state
transition_type
business_effective_time
recorded_at
actor_ref?
action_ref?
decision_ref?
approval_ref?
evidence_refs[]
reason?
correction_flag
```

`correction_flag=true` means the system is repairing an interpretation, not claiming a new real-world transition occurred.

---

## 11. Transition examples

### Agreement execution

```text
negotiating -> executed
```

Requires authoritative execution evidence or governed acceptance of equivalent proof.

### Invoice payment

```text
issued -> partially_paid -> paid
```

Derived from payment allocation/reconciliation, not email language alone.

### Proposal submission

```text
approved -> submitted
```

Requires submission evidence; approval alone does not imply submission.

### Action compensation

```text
succeeded -> compensated
```

Original successful action remains historical fact; compensation records reversal/mitigation.

### Incorrect opportunity stage correction

```text
pursuing -> submitted
```

If evidence shows submission actually happened earlier, record a correction with correct effective time rather than pretending the transition happened at correction time.

---

## 12. Codex rule

Machine-readable schemas may encode these as controlled vocabularies. They must not add new canonical states merely because a fixture or source system uses a different label.

Unknown source labels should map to candidate/source state and raise a semantic mapping question when no canonical mapping exists.
