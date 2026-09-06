# BUILD SPEC 001 — KOE Minimum Semantic Subset Recommendation

**Version:** v0.1  
**Status:** KOE recommendation to Chief Architect / Build Spec integration  
**Owner:** KOE-001  
**Governing decision:** ADR-002 — broad semantic foundation, narrow BUILD SPEC 001 vertical slice

## Objective

Define the smallest coherent semantic subset that can prove the hardest Business Reality invariants in the first commercial/opportunity vertical slice without forcing the wider ~38-object Business Reality Semantic Foundation into the first runtime.

## Benchmark basis

KOE is using an evolutionary/walking-skeleton delivery posture: small coherent increments, automated architectural fitness functions, realistic pressure tests, and expansion only after the current slice proves its invariants.

See `24-BENCHMARK-FIRST-DELIVERY-PATTERN-v0.1.md`.

## 1. Always-required shared kernel

These are required regardless of which specific commercial episode the Chief Architect selects. They are not all counted as business objects.

```text
CanonicalResource / CanonicalRef
Identity + source mappings
Alias
TypedRelationship
Effective/source/recorded/discovered time
Epistemic status
Provenance / evidence references
Security descriptor + actor/security context
Audit / correction / supersession
RawEvidence
Observation
Candidate
Claim
```

These enforce the cross-cutting invariants the slice exists to prove.

## 2. Minimum canonical/operational semantic subset

### Party and context

1. `Organization`
2. `Person`
3. `BusinessRelationship`
4. `Opportunity`
5. `Solicitation`

### Commercial artifact / commitment chain

6. `Proposal`
7. `Agreement`
8. `Artifact`

### Operational cognition trace

9. `Event`
10. `Assessment`
11. `Decision`
12. `Approval`
13. `Action`
14. `Outcome`

**Recommended core slice size: 14 semantic resource types**, plus the shared evidence/kernel contracts above.

This is a runtime subset, not a reduction of the enterprise foundation.

## 3. Conditional types — include only if the selected episode requires them

### `Project`
Include if the chosen episode crosses award/agreement into actual delivery or project creation.

### `Obligation`
Include if agreement terms/deadlines/commitments are necessary to demonstrate state or decision context.

### `ContractVehicle`
Include only if procurement vehicle eligibility/governance is material to the episode.

### `Capability`
Do not duplicate dynamic capability state into Business Reality. Use a cross-model reference if the episode requires a capability input.

### `Offering`
Reference the Business Intent-owned Offering when relevant; do not create a Business Reality duplicate.

## 4. Explicitly out of first-slice runtime unless the selected episode forces them

```text
LegalEntity
OrganizationalUnit
Position
Place
Milestone
Deliverable
Budget
Invoice
Payment
Assignment
Skill
Credential
Certification
Asset
System
Technology
Registration
Risk as a broad enterprise implementation concern
```

These remain valid parts of the broad semantic foundation. Exclusion from BUILD SPEC 001 is a delivery-scope choice only.

## 5. Required relationship semantics in the slice

At minimum the runtime must represent:

```text
Organization --role_in/context--> Opportunity
Person --participates_in--> Opportunity / Decision / Action
Opportunity --responds_to--> Solicitation
Opportunity --has_proposal--> Proposal
Organization --party/role--> BusinessRelationship
BusinessRelationship --scoped_to--> Opportunity / Agreement
Proposal --represented_by--> Artifact
Agreement --evidenced_by--> Artifact
Event --about--> business context
Assessment --evaluates--> business context
Decision --informed_by--> Assessment / evidence
Approval --authorizes--> Decision / Action / Proposal / Agreement
Action --changes_state_of--> business resource
Outcome --results_from--> Action / Decision / Opportunity
Claim --supported_by / contradicted_by--> evidence
```

Customer/Partner/Vendor remain contextual roles around Organization identity.

## 6. What BUILD SPEC 001 must prove with this subset

### Identity

- one organization/person across aliases/source appearances;
- similar-but-distinct identity remains separate;
- ambiguous identity may remain unresolved;
- contextual role does not create duplicate party identity.

### Evidence / truth

- source evidence remains immutable;
- candidate/claim does not automatically become canonical state;
- duplicate/forwarded evidence does not create false corroboration;
- contradictions remain inspectable.

### Context

- email thread/subject is not automatically Opportunity/Project context;
- relationship role is scoped to business context.

### Time

- current and historical accepted states can differ;
- effective time can differ from discovery/recorded time;
- correction does not rewrite historical evidence.

### Decision trace

The slice can reconstruct a path resembling:

```text
Evidence
 -> Assessment
 -> Decision
 -> Approval where required
 -> Action
 -> State Change
 -> Outcome
```

Historical gaps remain `unknown` or `inferred`; they are not fabricated.

### Security

- restricted evidence cannot leak through direct read/search/traversal/trace;
- a permitted derived operational fact may be visible only under explicit policy;
- read access does not imply promotion/action authority.

### Correctability

- incorrect alias/relationship/state interpretation can be corrected without deleting evidence/history;
- identity merge/split behavior remains reversible where exercised.

## 7. Minimum benchmark queries

The first runtime should support, directly or through a thin logical adapter:

1. resolve party identity from alias/source reference;
2. get current object/state;
3. get state `as_of` time T;
4. get scoped relationships;
5. reconstruct opportunity timeline;
6. retrieve supporting/contradicting evidence;
7. reconstruct decision trace;
8. find unresolved identity/context candidates;
9. find contradictions;
10. perform security-filtered search/traversal.

## 8. Minimum governed write/proposal behaviors

```text
append raw evidence
propose candidate / claim / relationship / event
promote governed candidate
reject candidate
correct canonical interpretation
propose merge / split
```

External-system autonomous writeback is not required for BUILD SPEC 001.

## 9. Slice expansion rule

A new semantic type enters BUILD SPEC 001 only when at least one of the following is true:

1. the selected episode cannot be represented correctly without it;
2. an acceptance test cannot be expressed without it;
3. a required governed action/query depends on its independent identity/lifecycle;
4. omitting it would collapse two materially distinct business concepts.

Convenience, source-schema shape, UI needs, or desire to exercise more of the 38-object catalog are not sufficient reasons.

## 10. Recommendation

Use the 14-type subset above as KOE's default BUILD SPEC 001 semantic boundary, then add only conditional types forced by the Chief Architect-selected episode.

The broad Business Reality Semantic Foundation remains the compatibility envelope and anti-overfitting constraint.

## Architecture disposition

**LOCAL_SOLVE within ADR-002 and the KOE charter.** No new cross-cutting architecture decision is introduced.