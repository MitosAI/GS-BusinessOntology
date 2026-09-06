# BUILD SPEC 001 — GenSigma Business Reality MVP

**Version:** v0.1 skeleton  
**Status:** Open integration specification  
**Owner:** Chief Architect  
**Primary contributors:** Knowledge & Ontology Engineering, Evidence & Data Engineering, Platform Engineering, Executive Cognition Research  
**Governing sources:** Constitution, Project Brief, Operating Architecture, Architecture Integration Contracts, Chief Architect Decision Method

---

# 1. Purpose

BUILD SPEC 001 defines the first executable vertical slice of GenSigma OS.

The build is not intended to prove that we can summarize email or populate a graph. It must prove that the architecture can transform real enterprise evidence into a trustworthy, correctable, secure, queryable representation of Business Reality that is suitable as an input to future computational judgment.

The slice must be small enough to build and test quickly but rich enough to exercise the architecture's hardest invariants.

---

# 2. MVP thesis

The MVP succeeds if GenSigma can take a bounded set of real Outlook + SharePoint evidence and reliably produce:

```text
SOURCE EVIDENCE
      |
      v
NORMALIZED EVIDENCE
      |
      v
OBSERVATIONS / CLAIMS / CANDIDATES
      |
      v
IDENTITY + CONTEXT RECONCILIATION
      |
      v
GOVERNED CANONICAL BUSINESS REALITY
      |
      v
SECURITY-AWARE QUERY / CONTEXT API
      |
      v
AUDITABLE DECISION-CONTEXT INPUT
```

No step may erase provenance or uncertainty.

---

# 3. What BUILD SPEC 001 must prove

The MVP must pressure-test at least these architectural properties:

1. **Canonical identity** — the same real-world organization/person can appear under many names without accidental duplicate canonical objects.
2. **Non-collapse** — related-but-distinct entities are not incorrectly merged.
3. **Evidence-before-truth** — extraction remains candidate knowledge until governed promotion.
4. **Context resolution** — email thread/subject/folder does not become business context by assumption.
5. **Temporal correctness** — current state and historical state can coexist.
6. **Provenance** — canonical facts can be traced to source evidence and promotion history.
7. **Contradiction** — conflicting evidence can coexist without silent overwrite.
8. **Correctability** — a wrong merge or classification can be repaired without destroying source history.
9. **Decision trace reconstruction** — at least one historical decision can be assembled with explicit/inferred distinctions.
10. **Security** — permitted business state can be exposed while restricted evidence remains hidden.
11. **Queryability** — meaningful business traversals and timelines are usable interactively.
12. **Platform neutrality of semantics** — Azure/storage implementation details do not leak into ontology meaning.

---

# 4. Scope selection method

The pilot business episode is intentionally not frozen merely because SFO/CRI was the first rich example observed.

Knowledge & Ontology Engineering must propose 2–3 candidate episodes and score them against:

```text
Evidence richness
Identity ambiguity
Relationship richness
Context ambiguity
Document/attachment linkage
Temporal span
Decision trace richness
Action/outcome evidence
Security coverage
Availability of ground truth for validation
Ability to generalize beyond one customer
```

Chief Architect chooses the first slice.

SFO/CRI remains a strong candidate, not a constitutional commitment.

---

# 5. Source boundary

Initial sensors:

- Outlook / Exchange Online;
- SharePoint Online.

Initial acquisition should be bounded by:

- named mailbox(es);
- named folders;
- time window;
- contextual expansion rules;
- selected SharePoint sites/libraries or contextual documents.

Important:

> The processing window controls where discovery starts, not the maximum age of evidence required to resolve context correctly.

The system may retrieve older supporting evidence when needed.

---

# 6. Source acquisition requirements

## Outlook

Required fields/behavior:

```text
mailbox identity
folder identity
stable source ID where possible
internet message ID
conversation/thread ID
sender / recipients
sent / received timestamps
subject
body strategy
attachment metadata
source reference
content hash
permissions/security metadata where available
incremental cursor/change tracking
idempotency
replay behavior
```

## SharePoint

Required fields/behavior:

```text
site identity
library identity
file/item identity
path/name
version identity
created / modified metadata
authorship
source reference
content hash
permissions metadata where available
version lineage
incremental/change tracking
idempotency
```

---

# 7. Raw Evidence contract

Each acquired evidence item must have a durable technical identity independent of canonical business identity.

Candidate structure:

```text
RawEvidence
- evidence_id
- source_system
- source_tenant
- source_container
- source_record_id
- source_version
- source_reference
- source_created_time
- source_modified_time
- acquired_time
- content_hash
- content_pointer / secure copy
- security_metadata
- parent_evidence_id if attachment/version derivative
- ingestion_run_id
```

Raw Evidence is immutable/append-oriented where practical.

---

# 8. Normalized Evidence contract

Normalization should create consistent representations while preserving raw lineage.

Candidate structures:

```text
NormalizedMessage
NormalizedDocument
NormalizedPartyObservation
NormalizedAttachment
NormalizedTextSegment
```

Normalization may remove quoted duplication from analytical text but must not delete the raw original.

Forwarded/quoted repetitions must be recognizable so they do not become false independent corroboration.

---

# 9. Candidate Evidence Graph objects

The non-authoritative Evidence Graph must support at minimum:

```text
Observation
Claim
CandidateEntity
CandidateRelationship
CandidateContext
CandidateEvent
AliasObservation
DecisionFragment
CandidateAction
CandidateOutcome
CandidateCommitment
DocumentLineageCandidate
Assessment
```

Every candidate must be linked to evidence.

---

# 10. Canonical object subset

Knowledge & Ontology Engineering must finalize the minimum subset required by the chosen slice.

Expected candidates:

```text
Organization
Person
BusinessRelationship
Opportunity
Solicitation
Proposal
Agreement
Project
DocumentArtifact
Event
Decision
Approval
Action
Outcome
```

Evidence/Claim/Assessment may remain evidence/fabric resources rather than equivalent business objects depending on final logical design.

No object type is admitted merely because a noun occurs in source text.

---

# 11. Object admission gate

For each new canonical object type, answer:

- independent identity?
- independent lifecycle?
- independently important relationships?
- meaningful security boundary?
- meaningful actions?
- ownership/accountability?
- important query value?
- important temporal state?

If weak, prefer property, role, relationship, event, evidence, category, interface, derived value, or application view.

---

# 12. Relationship model requirements

Relationships must support where relevant:

```text
relationship_id
type / family
participant roles
party/object endpoints
business context
scope
effective_from
effective_to
current state
provenance
confidence / epistemic status
security
```

Customer/Partner/Vendor are relationship semantics around canonical Organization identity unless evidence justifies another model.

---

# 13. Identity resolution requirements

System must support outcomes:

```text
same object
alias
historical name
parent/child
organizational unit
brand/legal-entity distinction
related but distinct
probable merge
split
new candidate
unresolved
```

Resolution must use multiple signals when possible:

- exact identifiers;
- legal names;
- domains;
- addresses;
- people;
- contract parties;
- RFP/project IDs;
- shared documents;
- chronology;
- business context;
- graph neighborhood.

Candidate generation and final resolution are separate operations.

No automatic canonical merge solely from vector/name similarity.

---

# 14. Alias model requirements

Alias must be context-aware and provenance-aware.

The design must support that `ServiceNow` can refer to:

- technology/product;
- capability;
- opportunity shorthand;
- project shorthand;
- support topic.

Alias semantics should therefore include observed text, possible/confirmed target, scope/context, source evidence, effective period where relevant, and confidence/status.

---

# 15. Context resolution requirements

Context candidates may include:

```text
Customer / Account
Opportunity
Solicitation / RFP
Agreement
Project
Work Order
Invoice / Payment matter
Workforce matter
Compliance matter
Internal initiative
```

The resolver should seek the governing business context before extracting/promoting relationship/event meaning that depends upon context.

Context expansion may query:

- older messages;
- other threads;
- attachments;
- SharePoint documents;
- prior proposals/contracts;
- known canonical business objects.

---

# 16. Epistemic model

Every material proposition must be classifiable as one of:

```text
Observed
Claimed
Inferred
Assumed
Assessed
Predicted
Canonical / Accepted
Rejected
Superseded
Unresolved
```

The exact metamodel may differ, but the semantics must remain explicit.

---

# 17. Authority model

Authority is property/claim-specific, not merely source-system-wide.

Build Spec must include an initial promotion matrix such as:

```text
Claim / State            Preferred Authority           Auto-promotion?
Message sent/received    Exchange metadata              likely yes
Agreement executed       signed agreement               governed rule
Opportunity awarded      buyer/portal/award artifact    high bar
Invoice paid             finance/bank authority         source-specific
Partner preference       decision evidence              likely assessment
Relationship strength    derived assessment             no canonical fact by default
```

Knowledge/Ontology owns the semantics; Evidence/Data implements detection; Platform enforces persistence/audit.

---

# 18. Temporal model

Required distinctions where material:

```text
effective_time
source_time
recorded_time
discovered_time
valid_from
valid_to
superseded_at
```

Required queries:

- current state;
- state as of effective date;
- what the system knew as of a discovery/recorded date where meaningful;
- event timeline;
- correction history.

---

# 19. Decision trace reconstruction

The MVP must reconstruct at least one path resembling:

```text
Evidence
 -> Assessment
 -> Alternative(s)
 -> Recommendation
 -> Decision
 -> Approval
 -> Action
 -> State Change
 -> Outcome
```

It is acceptable for historical traces to be incomplete.

Each field/resource must indicate whether it is:

- explicit;
- inferred;
- unknown.

DecisionTrace itself remains a traversal/view unless later admission tests justify persistence.

---

# 20. Security model for MVP

Minimum conceptual classes:

```text
Normal Business
Business Confidential
Finance Restricted
HR Restricted
Legal Restricted
Security Restricted
Executive / Strategy Restricted
```

This is not necessarily the final taxonomy.

Security tests must prove:

- source evidence retains appropriate restriction;
- a less-sensitive derived operational fact may be exposed independently;
- unauthorized semantic search cannot recover restricted text;
- agent/service identity is evaluated just like human identity;
- canonical promotion cannot silently widen access.

---

# 21. Query contract

Minimum read capabilities:

```text
get_object(id, security_context)
resolve_identity(observation, context, security_context)
get_relationships(object_id, filters, as_of, security_context)
get_neighbors(object_id, depth, filters, as_of, security_context)
get_state(object_id, as_of, security_context)
get_timeline(context_id, time_range, security_context)
get_evidence(target_id, security_context)
get_claims(target_id, security_context)
get_decision_trace(context_id, security_context)
find_contradictions(target_id, security_context)
search(query, filters, security_context)
```

API naming is provisional. Behavioral requirements matter more than syntax.

---

# 22. Proposed-write contract

Minimum proposal operations:

```text
propose_entity
propose_relationship
propose_context
propose_event
propose_claim
propose_alias
propose_merge
propose_split
propose_canonical_change
approve_promotion
reject_promotion
correct_canonical_state
```

The MVP does not require broad autonomous writes to external systems.

---

# 23. Benchmark scenarios for physical architecture

Platform Engineering must implement representative benchmarks from the final logical model.

At minimum:

## B1 Identity lookup

Resolve exact and alias identifiers against canonical identity plus source mappings.

## B2 Neighborhood traversal

Retrieve 1-hop and multi-hop context with type/time/security filters.

## B3 Temporal state

Retrieve current and historical state with provenance.

## B4 Evidence lineage

Traverse canonical state -> claim/promotion -> evidence -> raw source.

## B5 Decision trace

Retrieve decision path across evidence, decision, action and outcome resources.

## B6 Security-aware search

Search text/semantic representations while excluding evidence caller cannot access.

## B7 Canonical promotion transaction

Promote a candidate state and required relationships atomically or with equivalent correctness guarantees.

## B8 Correction

Split an incorrectly merged identity and show preservation of source evidence and prior history.

---

# 24. Performance requirements

Knowledge/Ontology + Platform must replace vague terms like `fast` and `scalable` with measurable targets.

Required target classes:

```text
interactive object lookup P50/P95
interactive relationship traversal P50/P95
search P50/P95
ingestion throughput
backfill throughput
canonical promotion throughput
maximum acceptable source lag
expected concurrent users/agents
expected evidence/object/link scale at 1y / 3y
```

Targets remain OPEN until realistic workload estimates are produced.

---

# 25. Reliability / recovery requirements

Must specify:

- retry model;
- dead-letter/error handling;
- exactly-once-effect/idempotency expectations;
- backup/restore;
- RPO/RTO appropriate to MVP;
- source replay;
- partial pipeline failure behavior;
- canonical-write recovery;
- monitoring/alerting.

---

# 26. Observability requirements

Minimum metrics:

```text
source lag
ingestion success/failure
replay/duplicate rate
normalization failures
extraction volume/confidence distribution
unresolved candidate count
identity merge/split proposal count
promotion/rejection count
API latency/errors
security denials
storage growth
model usage/cost
connector health
```

Trust metrics should eventually include precision/error rates from reviewed extractions and reconciliations.

---

# 27. Physical architecture decision gate

The primary persistence/search architecture may be selected only after:

- canonical shapes exist;
- benchmark queries exist;
- security scenarios exist;
- consistency requirements exist;
- scale assumptions exist;
- representative data fixture exists.

Candidate options must be evaluated under the Chief Architect Decision Method and recorded as an ADR.

---

# 28. Azure platform requirements

Platform Engineering may proceed in parallel on reversible foundation work:

- resource organization;
- Entra identities;
- managed identities/service principals;
- Key Vault;
- logging/monitoring;
- raw evidence object storage;
- CI/CD / infrastructure-as-code baseline;
- connector runtime prototype;
- network/security baseline.

It must not lock the semantic architecture into an Azure-specific representation.

---

# 29. Executive Cognition integration seam

The Business Reality MVP must be capable of producing a future `DecisionContext` containing at least:

```text
trigger / decision class
current relevant state
relevant history
source evidence
uncertainty / epistemic status
Business Intent references
Capability references
External World belief references
available actions
constraints / authority
```

The exact schema is OPEN pending Research 001.

Build Spec 001 must therefore preserve enough semantic richness to avoid rebuilding the data foundation later.

---

# 30. Acceptance test suite

## A. Identity

- aliases resolve correctly;
- similar names can remain separate;
- new-name observation does not automatically create canonical entity;
- merge/split correction is reversible.

## B. Evidence

- every canonical change has traceable evidence/promotion origin;
- contradicted claims remain inspectable;
- quoted copies do not count as independent corroboration by default.

## C. Time

- current and historical queries return distinct correct states;
- present classification is not projected backward without evidence.

## D. Context

- a thread subject alone does not define opportunity/project context;
- context expansion can retrieve older/supporting evidence.

## E. Decision trace

- explicit and inferred decision resources are distinguishable;
- action is distinct from decision;
- outcome is distinct from execution result.

## F. Security

- restricted evidence is inaccessible to unauthorized test identities;
- permitted derived facts remain available where policy allows;
- search honors restrictions.

## G. Replay

- repeated source ingestion produces no accidental duplicate raw/normalized effects.

## H. Query

- required traversals, timelines, evidence queries and search meet agreed targets.

---

# 31. Deliverables by lead

## Knowledge & Ontology Engineering

- final logical subset;
- relationship definitions;
- event/decision/action distinctions;
- identity/reconciliation spec;
- context rules;
- authority/promotion matrix;
- benchmark queries;
- candidate pilot episodes.

## Evidence & Data Engineering

- source inventory;
- acquisition schemas;
- normalization format;
- extraction contract implementation plan;
- replay/idempotency design;
- duplicate/quote/document-lineage approach;
- representative fixtures.

## Platform Engineering

- Azure landing zone;
- source identity/access plan;
- persistence candidate benchmark harness;
- security implementation options;
- operational requirements/estimates;
- physical architecture ADR proposal.

## Executive Cognition Research

- DecisionContext requirements that affect the MVP;
- uncertainty semantics that should be preserved;
- decision trace data requirements;
- any missing historical outcome requirements.

## Chief Architect

- choose MVP episode;
- resolve cross-team semantic conflicts;
- approve Build Spec 001;
- approve physical architecture ADR;
- prevent scope creep.

---

# 32. Exit criteria

BUILD SPEC 001 is ready to code when:

1. the chosen business episode is explicit;
2. canonical object/link subset is frozen for the slice;
3. extraction contract is explicit;
4. identity/context resolution behavior is testable;
5. promotion rules are explicit enough for implementation;
6. temporal semantics are explicit;
7. security scenarios are explicit;
8. benchmark/query suite is explicit;
9. representative fixtures exist;
10. physical architecture ADR is accepted;
11. Azure foundation is ready;
12. unresolved questions are either non-blocking or explicitly deferred.

A competent engineering team should not need to invent foundational semantics while coding.
