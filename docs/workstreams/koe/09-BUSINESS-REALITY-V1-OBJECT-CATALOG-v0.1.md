# Business Reality V1 — Candidate Business Object Catalog

**Version:** v0.1  
**Status:** KOE candidate catalog for admission testing  
**Owner:** Knowledge & Ontology Engineering (KOE-001)  
**Design guidance:** approximately 30–40 V1 business objects  
**Current candidate count:** 37

---

## 1. Purpose

This catalog establishes the candidate V1 business-object map from which Build Spec 001 selects its first implementation subset.

The count is a design guardrail, not a quota. An item remains a first-class business object only if it survives the object-admission test: independent identity/lifecycle, meaningful relationships, query value, security, ownership, and/or governed actions.

This catalog covers the **Business Reality operational ontology** and the operational resources needed to connect reality to capability, decisions, actions, and outcomes. It does not attempt to duplicate the full Business Intent model or the External Reality model.

Not counted in the 37-object guidance:

- relationship/link types;
- contextual roles such as Customer, Partner, Vendor, Competitor, Employee, Candidate, or Stakeholder;
- event/action subtypes;
- interfaces;
- properties/value objects;
- source bindings;
- raw evidence records;
- observations;
- extraction candidates;
- reconciliation proposals;
- vector/search representations;
- application/agent views.

---

## 2. Candidate object map

### A. Enterprise identity and structure — 6

1. `Organization`
2. `LegalEntity`
3. `OrganizationalUnit`
4. `Person`
5. `Position`
6. `Place`

### B. Relationship and commercial context — 7

7. `BusinessRelationship`
8. `Opportunity`
9. `Solicitation`
10. `Proposal`
11. `Agreement`
12. `Obligation`
13. `ContractVehicle`

### C. Delivery and financial execution — 5

14. `Project`
15. `Deliverable`
16. `Invoice`
17. `Payment`
18. `Budget`

### D. Workforce and executable capability — 7

19. `Assignment`
20. `Capability`
21. `Skill`
22. `Credential`
23. `Certification`
24. `Availability`
25. `Capacity`

### E. Systems and operational resources — 3

26. `Asset`
27. `System`
28. `Technology`

### F. Compliance — 1

29. `Registration`

`Registration` includes governed registrations/qualifications with an independent lifecycle, such as foreign qualification in a jurisdiction. `Registered Office` remains a relationship between a LegalEntity and Place rather than a standalone organization type.

### G. Knowledge, activity, judgment, and control — 8

30. `Artifact`
31. `Event`
32. `Claim`
33. `Assessment`
34. `Decision`
35. `Approval`
36. `Action`
37. `Outcome`

---

## 3. Important non-objects / contextual roles

The following are **not** separate canonical party identities by default:

```text
Customer
Partner
Vendor
Competitor
Technology Provider
Employee
Contractor
Candidate
Advisor
Stakeholder
Decision Maker
Approver
Project Resource
```

These are normally contextual roles or relationship semantics attached to canonical Organization or Person identities.

Examples:

```text
Organization: CRI Advantage
Role in Opportunity A: teaming partner
Role in another context: subcontractor
Possible future role: vendor
```

One organization identity can therefore participate in multiple contextual relationships without identity duplication.

---

## 4. Objects that require explicit admission review

The following candidates are useful but should be pressure-tested before final V1 promotion:

### `LegalEntity`

Question: independent object type versus specialized Organization shape/interface.

Reason to keep separate: legal identity, registrations, tax/compliance, contracts, ownership, jurisdictions, and independent actions/security.

### `OrganizationalUnit`

Question: independent object type versus Organization specialization.

Reason to keep separate: business units/practices/departments can own work, people, budgets, capabilities, and decisions without being legal entities.

### `Position`

Question: independent object versus relationship/value structure.

Reason to keep separate: position can exist independently of a current holder and carry authority, reporting, capability requirements, and lifecycle.

### `Proposal`

Question: business object versus Artifact specialization.

Reason to keep separate: the commercial proposal has a lifecycle, status, submission/approval actions, customer/opportunity linkage, and multiple artifact versions. The proposal business object should not be identical to one PDF/file.

### `Obligation`

Question: first-class business object versus Agreement property/link.

Reason to keep separate where obligations have owner, due date, status, evidence, fulfillment actions, breach/risk, and lifecycle.

### `Budget`

Question: first-class object versus finance-domain state/value structure.

Keep only if budget needs independent ownership, approvals, effective period, allocation relationships, versioning, and decision/action semantics.

### `Availability` and `Capacity`

Question: first-class objects versus temporal measurements on Person/Capability/OrganizationalUnit.

Do not promote merely to reach the object-count range. Promote only if their lifecycle, provenance, granularity, planning relationships, and decisions require independent identity.

### `Claim`

`Claim` is a governed semantic assertion, distinct from raw evidence/observation. It may be first-class because contradictions, provenance, authority, temporal validity, and promotion history attach to the proposition itself.

Raw evidence records and extraction observations remain outside the canonical business-object count.

---

## 5. Build Spec 001 pilot subset

Build Spec 001 should begin with the smallest coherent subset needed to represent the SFO ServiceNow / CRI episode.

### Required pilot objects

1. `Organization`
2. `Person`
3. `BusinessRelationship`
4. `Opportunity`
5. `Solicitation`
6. `Proposal`
7. `Agreement`
8. `Artifact`
9. `Event`
10. `Claim`
11. `Assessment`
12. `Decision`
13. `Approval`
14. `Action`
15. `Outcome`

### Conditional pilot objects

16. `Project` — include if award/delivery evidence exists in the fixture.
17. `Obligation` — include if agreement or solicitation commitments need independent lifecycle semantics.
18. `OrganizationalUnit` — include when SFO/GenSigma internal/customer units are needed to resolve context correctly.

The initial implementation therefore proves roughly 15–18 business objects, while the wider 37-object candidate catalog continues through admission testing in parallel.

---

## 6. Explicit separation from evidence-layer records

The implementation may contain many logical record types that are **not business objects**.

Examples:

```text
RawSourceRecord
SourceAppearance
Observation
CandidateIdentity
CandidateRelationship
CandidateContext
CandidateEvent
EvidenceReference
OriginLineage
ReconciliationProposal
PromotionDecision
ExtractionRun
ModelOutput
SecurityLabel
```

These are necessary system/evidence constructs but must not inflate the canonical business ontology count.

---

## 7. Cross-model boundaries

### Business Intent

Purpose, vision, mission, strategic objectives, initiatives, target markets, desired outcomes, decision criteria, and normative policies belong primarily to Business Intent and are not duplicated into Business Reality merely to make them queryable.

Business Reality links to those resources where relevant.

### External Reality

Market conditions, regulation changes, competitor moves, public procurement shifts, technology trends, and similar outside conditions belong to External Reality unless they directly instantiate an active Business Reality context, such as a customer-issued Solicitation.

### Capability

`Capability` is represented because Business Reality must identify the organizational resources and evidence from which executable capability is assessed. Rich capability evaluation remains its own model/function and should not turn the entire Business Reality graph into a capability model.

### Executive Judgment

`Assessment`, `Decision`, `Approval`, `Action`, and `Outcome` are represented for operational traceability. The reasoning method that produces a recommendation or decision belongs to Executive Judgment, not to the Business Reality storage model.

---

## 8. Next specification step

For the 15–18 Build Spec 001 objects, KOE must now produce an implementable definition sheet containing:

- semantic definition;
- identity rule;
- lifecycle/state model;
- required/optional properties;
- typed links;
- admissible contextual roles;
- temporal semantics;
- evidence/provenance requirements;
- security behavior;
- governed actions;
- competency questions;
- fixture examples;
- acceptance assertions.

That definition sheet is the immediate semantic input to the Codex build.
