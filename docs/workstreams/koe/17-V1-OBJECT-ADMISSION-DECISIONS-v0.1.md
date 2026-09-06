# V1 Object Admission Decisions

**Version:** v0.1  
**Status:** KOE decisions  
**Owner:** Knowledge & Ontology Engineering (KOE-001)

---

## 1. Purpose

Resolve the main open V1 object-admission questions using the governing design truths and the object-admission test.

Admission test:

A first-class canonical object should normally have several of:

- independent identity;
- independent lifecycle;
- important relationships;
- governed actions;
- independent ownership/authority;
- material temporal behavior;
- independent security;
- high query value.

The 30–40 range remains guidance, not a quota.

---

## 2. Decisions

### `LegalEntity` — ADMIT

**Decision:** First-class object.

**Reason:** legal identity, registrations, agreements, ownership, tax/compliance, jurisdiction, and lifecycle differ materially from the broader enterprise/operating `Organization` concept.

**Constraint:** `LegalEntity` must remain linked to the relevant enterprise/organization identity and must not create duplicate party semantics accidentally.

---

### `OrganizationalUnit` — ADMIT

**Decision:** First-class object.

**Reason:** business units, practices, departments, and teams can own people, positions, budgets, capabilities, projects, decisions, and authority while lacking legal identity.

**Constraint:** hierarchy changes are temporal relationships, not destructive renaming/reparenting.

---

### `Position` — ADMIT

**Decision:** First-class object.

**Reason:** a position exists independently of its holder, carries authority/responsibility/skill requirements, and has its own lifecycle.

**Constraint:** title strings alone do not create canonical Position objects.

---

### `Offering` — ADMIT AS SHARED ENTERPRISE OBJECT; PRIMARY OWNER = BUSINESS INTENT

**Decision:** First-class cross-model object.

**Reason:** an offering has stable identity across opportunities, proposals, agreements, and projects and is strategically governed.

**Boundary:** Business Intent owns canonical Offering semantics; Business Reality references the Offering actually proposed/sold/delivered.

**Constraint:** customer-specific proposal language does not automatically create a new canonical Offering.

---

### `Obligation` — ADMIT

**Decision:** First-class object.

**Reason:** obligations have owner, source, due date, state, fulfillment evidence, breach/waiver semantics, risk, and lifecycle independent from the Agreement text that created them.

**Constraint:** low-value extracted clauses may remain Claims until an obligation admission threshold is met.

---

### `Budget` — ADMIT

**Decision:** First-class object.

**Reason:** budgets have ownership, scope, period, approval, versioning, allocation, constraints, and revision lifecycle.

**Constraint:** actual spend, cost, or invoice totals are not the Budget object itself.

---

### `Milestone` — ADMIT

**Decision:** First-class object.

**Reason:** material milestones have independent planned/actual dates, ownership, dependencies, obligations, risk, and status and are queried/acted on directly.

**Constraint:** trivial task dates do not become Milestone objects automatically.

---

### `Claim` — ADMIT AS KERNEL KNOWLEDGE RESOURCE

**Decision:** First-class governed resource in the operational ontology.

**Reason:** contradictions, authority, provenance, temporal validity, promotion, supersession, and correction attach to the proposition itself.

**Boundary:** `Claim` is a cross-cutting knowledge resource, not a business party/process object. Raw observations/extractions remain below it.

**Constraint:** not every extracted statement becomes a canonical Claim; low-value observations may remain evidence-layer records.

---

### `Approval` — ADMIT

**Decision:** First-class object.

**Reason:** approval has requester/approver, authority basis, approved subject, scope, time, state, revocation/expiration, and audit significance independent of the Decision or Action it authorizes.

**Constraint:** trivial acknowledgements are not approvals.

---

### `Risk` — ADMIT

**Decision:** First-class managed object.

**Reason:** a durable risk record can have owner, scope, mitigation, status, realization, decisions, and lifecycle across multiple assessments.

**Boundary:** `Risk` is the managed risk identity; changing probability/severity/confidence is captured through `Assessment` or time-bounded properties/claims.

---

### `Outcome` — ADMIT

**Decision:** First-class object.

**Reason:** outcomes can be observed, revised, measured, attributed, compared, and linked across actions, decisions, projects, opportunities, and strategic intent.

**Boundary:** observed operational outcome is distinct from strategic desired outcome in Business Intent.

---

## 3. Deliberate non-admissions

### `Availability` — DO NOT ADMIT IN V1

Represent as a time-bounded measurement/claim about Person, OrganizationalUnit, resource pool, Assignment, or Capability.

Promote later only if planning semantics demonstrate independent lifecycle/identity.

### `Capacity` — DO NOT ADMIT IN V1

Represent as a time-bounded measure/assessment over a resource or Capability.

Promote later only if capacity planning requires independent objects with allocations, reservations, and lifecycle.

### `Customer`, `Partner`, `Vendor`, `Employee`, `Contractor`, `Candidate` — DO NOT ADMIT AS PARTY TYPES

Represent as contextual roles/relationship semantics around canonical `Organization` or `Person` identity.

### `RegisteredOffice` — DO NOT ADMIT

Represent as a temporal typed relationship between `LegalEntity` and `Place`.

### `Document`, `Message`, `Email`, `RFPFile`, `ProposalPDF` — DO NOT ADMIT AS CORE V1 OBJECTS

Represent as Artifact kinds/source appearances unless independent lifecycle and business actions justify specialization later.

---

## 4. V1 status

The current 38-object architecture remains the working V1 operational object/resource set.

This decision does **not** freeze every property or domain specialization. It freezes the present admission posture so Codex and Platform Engineering do not independently collapse or multiply these concepts.

Future object admission/removal requires:

1. explicit semantic rationale;
2. impact on identity/lifecycle/relationships;
3. migration impact;
4. competency question or governed action demonstrating need;
5. KOE approval and contract version change.
