# Business Reality V1 — Enterprise Business Object Catalog

**Version:** v0.2  
**Status:** KOE candidate architecture for admission testing  
**Owner:** Knowledge & Ontology Engineering (KOE-001)  
**Design guidance:** approximately 30–40 V1 business objects  
**Current candidate count:** 38

---

## 1. Purpose

This catalog defines the enterprise-wide candidate business-object architecture for Business Reality V1.

It is not derived from one customer, opportunity, RFP, project, or source system. Real business episodes are validation fixtures against this architecture, not the source of the architecture itself.

The count is a guardrail, not a quota. An item remains a first-class business object only when its independent identity/lifecycle, relationships, governed actions, security, ownership, temporal behavior, or query value justify it.

The four design truths apply throughout:

1. preserve truth;
2. allow correction;
3. keep the core stable;
4. make boundaries explicit.

---

## 2. Candidate V1 object architecture — 38

### A. Enterprise identity and structure — 6

1. `Organization`
2. `LegalEntity`
3. `OrganizationalUnit`
4. `Person`
5. `Position`
6. `Place`

### B. Relationships and commercial/revenue — 8

7. `BusinessRelationship`
8. `Opportunity`
9. `Solicitation`
10. `Offering`
11. `Proposal`
12. `Agreement`
13. `Obligation`
14. `ContractVehicle`

### C. Delivery and financial execution — 6

15. `Project`
16. `Milestone`
17. `Deliverable`
18. `Budget`
19. `Invoice`
20. `Payment`

### D. Workforce and executable capability — 5

21. `Assignment`
22. `Capability`
23. `Skill`
24. `Credential`
25. `Certification`

### E. Systems and operational resources — 3

26. `Asset`
27. `System`
28. `Technology`

### F. Legal/compliance state — 1

29. `Registration`

### G. Knowledge, activity, judgment, and control — 9

30. `Artifact`
31. `Event`
32. `Claim`
33. `Assessment`
34. `Risk`
35. `Decision`
36. `Approval`
37. `Action`
38. `Outcome`

---

## 3. Why these are business objects

### Identity / structure

`Organization`, `LegalEntity`, `OrganizationalUnit`, `Person`, `Position`, and `Place` anchor durable identity, ownership, authority, location, structure, and relationship context.

`LegalEntity` and `OrganizationalUnit` remain distinct from a generic Organization because they have materially different lifecycle, legal, authority, compliance, ownership, and action semantics.

### Relationships / commercial

`BusinessRelationship` represents a material relationship with its own scope, state, effective period, evidence, and participant roles. Customer, Partner, Vendor, Competitor, Employer, Contractor, Advisor, and similar labels normally remain contextual roles rather than duplicate party identities.

`Opportunity`, `Solicitation`, `Offering`, `Proposal`, `Agreement`, `Obligation`, and `ContractVehicle` each have independent lifecycle, relationships, actions, and query value. A Proposal is not merely one PDF; an Agreement is not merely one signed artifact; a Solicitation is not the same thing as GenSigma's Opportunity.

### Delivery / finance

`Project`, `Milestone`, and `Deliverable` describe execution. `Budget`, `Invoice`, and `Payment` describe material financial structures/events with independent identity, approval, reconciliation, and lifecycle behavior.

### Workforce / capability

`Assignment` connects people/resources to business context and time. `Capability`, `Skill`, `Credential`, and `Certification` have durable meaning across multiple assignments and domains.

`Availability` and `Capacity` are deliberately **not** V1 business objects by default. They are normally temporal measurements/claims about a Person, OrganizationalUnit, Capability, or resource pool. They can be promoted later if independent lifecycle/identity proves necessary.

### Systems / operational resources

`Asset`, `System`, and `Technology` allow the company to represent owned/managed resources, operational systems, and technology dependencies without mirroring CMDB/source schemas blindly.

### Compliance

`Registration` represents governed legal/compliance registrations and qualifications with independent jurisdiction, identifier, status, effective dates, renewal/expiration behavior, and evidence.

A `RegisteredOffice` is normally a typed relationship among LegalEntity, Place, and effective period rather than a separate organization object.

### Knowledge / judgment / control

`Artifact`, `Event`, `Claim`, `Assessment`, `Risk`, `Decision`, `Approval`, `Action`, and `Outcome` support evidence-backed operational reasoning and execution while preserving the distinctions among what was observed, asserted, judged, chosen, authorized, done, and produced.

---

## 4. Contextual roles are not duplicate identities

The following are normally roles or relationship semantics:

```text
Customer
Prospect
Partner
Vendor
Subcontractor
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
Account Owner
```

Example:

```text
Organization: CRI Advantage
  role in Opportunity A: teaming partner
  role in Project B: subcontractor
  role in another context: vendor
```

One canonical identity can hold different roles in different scopes and periods.

---

## 5. Explicit non-objects

The following are system/evidence constructs, not counted as canonical business objects:

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
VectorEmbedding
SearchDocument
```

They are necessary implementation resources, but they do not become business nouns merely because the platform stores them.

---

## 6. Cross-model boundaries

### Business Intent

Purpose, vision, mission, strategic objectives, strategic initiatives, desired outcomes, decision criteria, risk appetite, and normative policies belong primarily to Business Intent.

Business Reality links to them; it does not duplicate them.

### External Reality

Market conditions, regulation changes, competitor moves, technology trends, public funding conditions, and similar external conditions belong primarily to External Reality.

External entities may still use shared canonical identity primitives where appropriate, but their environmental interpretation belongs to External Reality.

### Capability

`Capability` has a durable identity in Business Reality because organizations can possess, develop, source, require, and evidence capabilities. Dynamic feasibility—whether GenSigma can execute something now under constraints—belongs to the Capability model/function.

### Executive Judgment

`Assessment`, `Risk`, `Decision`, `Approval`, `Action`, and `Outcome` are represented for operational traceability. The method that produces judgment belongs to Executive Judgment.

---

## 7. Admission questions still open

The 38 objects are candidates, not frozen schema. The following deserve explicit pressure testing:

- `LegalEntity` vs specialized Organization contract;
- `OrganizationalUnit` vs specialized Organization contract;
- `Position` vs structured relationship resource;
- `Offering` ownership boundary with Business Intent;
- `Obligation` first-class object vs agreement-derived resource;
- `Budget` first-class object vs governed financial state;
- `Milestone` first-class object vs Project event/state construct;
- `Claim` canonical business object vs governed knowledge resource outside the business-object count;
- `Approval` independent object vs specialized Decision/Action authorization resource.

Admission decisions must be made on semantics, not target count.

---

## 8. Object-definition contract

Every admitted V1 object must eventually specify:

```text
canonical definition
identity rule
lifecycle / states
required and optional properties
typed relationships
contextual roles
effective-time behavior
evidence / provenance requirements
security / authority behavior
allowed governed actions
correction / supersession behavior
competency questions
acceptance assertions
```

An object is not implementation-ready until those semantics are sufficient for two independent engineers to implement it without assigning different business meaning.

---

## 9. Validation requirement

The architecture must be pressure-tested across multiple domains:

1. commercial pursuit;
2. delivery/project execution;
3. workforce/resource lifecycle;
4. legal/compliance lifecycle;
5. vendor/technology lifecycle;
6. financial execution.

No single fixture has privileged architectural status.
