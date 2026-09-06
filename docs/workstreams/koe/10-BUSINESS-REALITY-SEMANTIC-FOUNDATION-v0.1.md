# Business Reality Semantic Foundation

**Version:** v0.1  
**Status:** Active KOE enterprise semantic compatibility envelope  
**Owner:** Knowledge & Ontology Engineering (KOE-001)  
**Governing scope decision:** ADR-002  
**Physical persistence:** intentionally unspecified

---

## 1. Objective

Define the stable semantic foundation that allows GenSigma to represent, query, correct, and act on Business Reality across commercial, delivery, workforce, finance, compliance, and technology domains.

This is an enterprise foundation. Individual GenSigma episodes are validation fixtures only. Under ADR-002 it is deliberately broader than BUILD SPEC 001, which is a narrow Chief Architect-owned executable vertical slice selected from this foundation.

The design is governed by four truths:

1. preserve truth;
2. allow correction;
3. keep the core stable;
4. make boundaries explicit.

---

## 2. Semantic kernel

The kernel is smaller than the business-object catalog. It defines the rules all domains depend on.

### 2.1 Canonical resource identity

Every canonical business object has a stable internal identity independent of source-system IDs, names, aliases, or current role.

Required behavior:

- multiple source identities may map to one canonical identity;
- one source identity must not silently map to multiple canonical objects in the same identity namespace;
- aliases are contextual and temporal where necessary;
- merge and split are governed, reversible operations;
- source mappings survive correction.

### 2.2 Typed relationships

Relationships carry business meaning and may have their own scope, participant roles, effective period, state, evidence, security, and correction history.

A relationship is not a naked graph edge when those semantics matter.

### 2.3 State and time

Material state must support:

- effective/business time;
- source time;
- recorded time where distinct;
- discovery time;
- current and historical reconstruction;
- supersession/correction;
- approximate time where exact time is unknown;
- isolation of hypothetical/scenario state from accepted truth.

### 2.4 Evidence and epistemic status

The platform must distinguish:

```text
Evidence
Observation
Claim
Assessment
Accepted canonical state
Inferred / reconstructed state
Unknown
Unresolved
Contradicted
Superseded
```

Source evidence may support canonical state but does not become canonical merely because it exists.

### 2.5 Security and authority

Every read, write, promotion, correction, and governed action executes under an actor/security context.

Security may apply at object, property, relationship, evidence, action, and domain level.

Authority to observe, interpret, approve, and act are distinct concerns.

### 2.6 Operational cognition distinctions

The kernel preserves:

```text
Event      = what happened
Assessment = what was judged about a situation
Decision   = what choice was made
Approval   = what authority authorized
Action     = what was done
Outcome    = what resulted
```

These may link closely but must remain query-distinguishable.

### 2.7 Correction and audit

Canonical interpretation is revisable. Evidence/history is not rewritten to make the past look clean.

Every material correction should answer:

- what changed;
- what prior interpretation was superseded;
- who/what changed it;
- why;
- what evidence supported the change;
- when the correction was recorded;
- what effective period changed;
- which derived projections require rebuild.

---

## 3. V1 business-object architecture

The current enterprise candidate architecture is defined in `09-BUSINESS-REALITY-V1-OBJECT-CATALOG-v0.1.md`.

Current KOE design envelope:

- approximately 30–40 V1 business objects as a complexity guardrail, not a quota;
- current candidate count = 38;
- exact admission remains subject to real pressure tests and object-admission criteria.

Domains:

```text
Enterprise identity / structure
Relationships / commercial revenue
Delivery / finance
Workforce / capability
Systems / technology
Legal / compliance
Knowledge / activity / judgment / control
```

This broad catalog does not determine the BUILD SPEC 001 runtime count. KOE's current minimum-slice recommendation is separately defined in `27-BUILD-SPEC-001-MINIMUM-SEMANTIC-SUBSET-v0.1.md`.

---

## 4. Relationship architecture

The following relationship families must be expressible without duplicating canonical identities.

### 4.1 Structural

```text
LegalEntity -> part_of -> Organization
OrganizationalUnit -> part_of -> Organization | OrganizationalUnit
Position -> belongs_to -> OrganizationalUnit
Place -> location_of -> LegalEntity | OrganizationalUnit | Project | Asset
```

### 4.2 Party / role

```text
Organization | Person -> participates_in -> BusinessRelationship
BusinessRelationship -> scoped_to -> Opportunity | Agreement | Project | enterprise
BusinessRelationship -> role_of_participant -> Customer | Partner | Vendor | Employee | Contractor | Advisor | other contextual role
```

The role is scoped and temporal. It must not redefine canonical party identity.

### 4.3 Commercial

```text
Opportunity -> for -> Organization | OrganizationalUnit
Opportunity -> responds_to -> Solicitation
Opportunity -> references -> Offering
Opportunity -> has_proposal -> Proposal
Opportunity -> governed_by -> Agreement | ContractVehicle
Opportunity -> requires -> Capability
Proposal -> represented_by -> Artifact
Agreement -> evidenced_by -> Artifact
Agreement -> creates -> Obligation
```

`Offering` is owned by Business Intent. `Capability` is owned by the Capability Model. Business Reality references these shared concepts; it does not fork them.

### 4.4 Delivery / finance

```text
Project -> fulfills -> Agreement | Obligation
Project -> has -> Milestone
Project -> produces -> Deliverable
Assignment -> assigns -> Person | OrganizationalUnit -> Project | Opportunity
Invoice -> bills_for -> Agreement | Project | Deliverable
Payment -> settles -> Invoice
Budget -> funds -> Project | OrganizationalUnit | Initiative reference
```

### 4.5 Workforce / capability evidence

```text
Person -> holds -> Position
Person -> has -> Skill | Credential | Certification
Assignment -> requires -> Skill | Capability
Capability evaluation -> depends_on -> Person | System | Technology | Partner relationship | Credential
```

Business Reality stores the underlying people, skills, credentials, systems, relationships and assignments. Dynamic feasibility belongs to the Capability Model.

### 4.6 Technology / compliance

```text
Asset -> uses | instantiates -> Technology
System -> uses -> Technology
Organization | LegalEntity -> owns | operates | depends_on -> Asset | System
LegalEntity -> has -> Registration
Organization | Person -> holds -> Certification
Registration -> applies_in -> Place/Jurisdiction representation
```

### 4.7 Evidence / judgment / action

```text
Claim -> supported_by | contradicted_by -> Artifact | EvidenceReference
Assessment -> evaluates -> any business context
Risk -> affects -> any material business context
Decision -> considers -> Assessment | Risk | Alternative reference
Decision -> authorizes_or_triggers -> Action
Approval -> authorizes -> Decision | Action | Proposal | Agreement
Action -> changes_state_of -> business object(s)
Event -> records_occurrence_about -> business object(s)
Outcome -> results_from -> Action | Decision | Project | Opportunity
```

Semantic ownership follows `15-MODEL-OWNERSHIP-AND-BOUNDARY-MAP-v0.1.md`: Assessment/Risk/Decision belong to Executive Judgment, Action to Governed/Kinetic Action, Outcome to Outcome/Learning, while their occurrences/history remain queryable through Business Reality.

---

## 5. Core invariants

### Identity

- Customer, Partner, Vendor, Employee, Contractor, Candidate, Stakeholder, Approver, and similar concepts are normally roles, not duplicate Person/Organization identities.
- A source-system record is not a canonical object identity.
- Ambiguity may remain unresolved.

### Evidence

- No material canonical assertion without retrievable provenance or authorized manual origin.
- Duplicate/forwarded/copied evidence cannot count as independent corroboration unless origin lineage supports independence.
- Model output is evidence about an interpretation, not authority by itself.

### Time

- Later knowledge must not silently rewrite what was believed/accepted at an earlier `as_of` time.
- Effective time and discovery/recording time must remain distinguishable when material.

### Correction

- Merge, split, reclassification, relationship correction, and state correction preserve history.
- Destructive overwrite is prohibited for material canonical interpretation.

### Security

- Unauthorized evidence must not leak through direct reads, search, traversal, counts/snippets where sensitive, or derived projections.
- A canonical fact may be visible while restricted supporting evidence remains hidden only when policy explicitly permits that projection.

### Action

- Material state-changing actions are typed and auditable.
- Agents may not bypass authority/policy because they possess source access.

---

## 6. Enterprise competency questions

The foundation must eventually support questions such as:

1. What organizations and people does GenSigma know, and what roles do they hold in each context?
2. What is the accepted current state of an opportunity, project, agreement, invoice, registration, or relationship?
3. What was the accepted state at time T?
4. What evidence supports or contradicts that state?
5. What changed, when, and because of which event/action/decision?
6. Which agreements and obligations govern a project or relationship?
7. Which people, skills, credentials, systems, technologies, and partner resources support a capability evaluation?
8. What work is committed, delivered, billed, paid, overdue, blocked, or at risk?
9. Which legal entities are registered/certified where, and what renewals or obligations exist?
10. Which systems/assets/technologies create operational dependencies or risks?
11. What decision was made, by whom, under what authority, with what evidence and outcome?
12. What remains unknown, unresolved, contradicted, or inferred?

---

## 7. Golden governed actions

The semantic foundation must be able to support typed actions across domains, including:

```text
Create / correct canonical identity
Merge / split identity
Accept / reject relationship proposal
Promote / supersede claim or state
Approve bid / decline bid
Approve partner
Approve / execute agreement
Create project from award/agreement
Assign resource
Record deliverable acceptance
Issue invoice
Record / reconcile payment
Record registration / certification renewal
Approve technology/vendor relationship
Record risk / mitigation action
Correct canonical interpretation
```

Specific action implementations may arrive later; the semantic architecture must not block them.

---

## 8. Multi-domain verification packs

The broad semantic foundation is not accepted against one episode.

Required validation families:

1. commercial pursuit;
2. delivery/project execution;
3. workforce/resource lifecycle;
4. legal/compliance lifecycle;
5. vendor/technology lifecycle;
6. financial execution.

Each pack should contain expected identities, relationships, claims, state transitions, ambiguity/unknown cases, temporal expectations, corrections, and at least one permission constraint.

BUILD SPEC 001 may execute a narrower representative episode, but that episode has no privileged authority over the broader enterprise foundation.

---

## 9. Logical API baseline

Technology-neutral operations should include:

```text
get_object(id, as_of?, security_context)
resolve_identity(reference, context?, as_of?, security_context)
get_relationships(id, filters?, as_of?, security_context)
get_neighbors(id, depth, filters?, as_of?, security_context)
get_state(id, as_of?, security_context)
get_timeline(context_id, range?, security_context)
get_evidence(resource_or_claim_id, security_context)
get_decision_trace(context_or_decision_id, security_context)
find_contradictions(scope, security_context)
find_unresolved_candidates(filters, security_context)
search(query, filters?, as_of?, security_context)

propose_object(...)
propose_relationship(...)
propose_claim(...)
propose_event(...)
propose_merge(...)
propose_split(...)
promote_candidate(...)
reject_candidate(...)
correct_canonical_interpretation(...)
```

Physical persistence must prove it can satisfy these semantics rather than redefine them.

---

## 10. Executive Cognition semantic seam

ADR-003 requires the shared architecture to support, where material:

- probability adequacy;
- multidimensional uncertainty;
- ex-ante expected outcomes/assumptions;
- recommendation reversal/sensitivity conditions;
- decision-method provenance;
- causal-versus-predictive distinction.

These are semantic/query requirements, not automatic new top-level ontology objects. KOE must find the smallest coherent representation, usually through Assessment/Decision/DecisionContext-related structures and metadata, while preserving model ownership boundaries.

---

## 11. Reference implementation boundary

Reference implementations should make the semantic kernel executable before production persistence is selected.

The executable baseline should contain:

- canonical resource/type contracts;
- relationship contract;
- temporal/state contract;
- evidence/provenance references;
- epistemic status;
- security/actor context;
- audit/correction contract;
- proposed mutation contract;
- validation fixtures and tests.

Domain-specific behavior layers on incrementally. A reference runtime is not evidence that its in-memory or library choices are the production architecture.

---

## 12. Handoff readiness condition

The semantic kernel is ready for bounded Codex implementation when contracts and acceptance tests are explicit enough that implementation cannot legally choose a different meaning for identity, role, evidence, time, correction, authority, or Event/Decision/Action/Outcome.

The enterprise object catalog may continue to refine through admission tests without blocking kernel implementation, provided changes do not invalidate the kernel invariants.

BUILD SPEC 001 uses the separately governed minimum-subset recommendation and Chief Architect integration gate rather than this full enterprise catalog as its runtime scope.
