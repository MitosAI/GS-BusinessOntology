# GenSigma Enterprise Ontology V1 Specification

**Version:** v0.1  
**Status:** Draft / promoted-core candidate  
**Governing doctrine:** Palantir-style operational ontology

---

## 1. Purpose

This document defines the initial semantic language of the GenSigma Operational Ontology.

It does not attempt to enumerate every noun in the business. The goal is to create a small, stable promoted core that can represent real GenSigma operations while remaining extensible.

The governing design principle is:

> The unit of design is the decision loop, not a giant noun inventory.

---

## 2. Ontology layers

```text
L0 Metamodel
L1 Promoted Enterprise Core
L2 Shared Enterprise Domains
L3 GenSigma Extensions
L4 Application / Agent Views
L5 Source Bindings
```

### L0 — Metamodel

Defines object type, property, link type, interface, action type, function/model reference, policy/security rule and event/state semantics.

### L1 — Promoted Enterprise Core

Small, stable concepts used across the company.

### L2 — Shared Enterprise Domains

Commercial, workforce, finance, delivery, compliance, systems and strategy.

### L3 — GenSigma Extensions

Company-specific concepts and relationships.

### L4 — App / Agent Views

Task-specific projections; never independent semantic truth.

### L5 — Source Bindings

Mappings to Outlook, SharePoint, QuickBooks, CRM, procurement portals, etc. Source bindings must not redefine canonical concepts.

---

## 3. Object-type admission test

A proposed canonical object type should normally satisfy several of:

- independent identity;
- independent lifecycle;
- important relationships;
- independent security;
- independent business actions;
- independent ownership;
- independent query value.

If not, it may be better represented as property, value, relationship, relationship role, event, claim, evidence, category, interface, derived value or application view.

---

## 4. V1 promoted core candidates

The initial promoted core should be deliberately small.

### Identity / party

1. `Organization`
2. `Person`
3. `Place`

### Business context

4. `BusinessRelationship`
5. `Opportunity`
6. `Solicitation`
7. `Agreement`
8. `Project`

### Evidence / activity

9. `Artifact`
10. `Event`
11. `Claim`
12. `Assessment`
13. `Decision`
14. `Action`
15. `Outcome`

### Operating semantics

16. `Capability`
17. `Policy`
18. `Risk`

This is a candidate set. Real data may show that some belong at L2 rather than L1.

---

## 5. Organization model

`Organization` is the canonical identity anchor for organizational entities.

Customer, Partner, Vendor and Competitor should generally not be Organization subtypes. They are contextual relationships/roles.

### 5.1 Internal structure

```text
ORGANIZATION
  |
  +--> Enterprise
  +--> Legal Entity
  +--> Organizational Unit
```

Potential Organizational Unit forms include Business Unit, Practice, Department and Team.

### 5.2 Legal entity geography

Avoid the inaccurate US use of `Branch` for state qualification.

Model separately:

- Foreign Registration / Qualification;
- Registered Office;
- Operating Location.

`Registered Office` is fundamentally a relationship between a Legal Entity and Place/Address, not an Organization subtype. Foreign Registration/Qualification relates a Legal Entity to a Jurisdiction and associated registration facts.

---

## 6. Person model

There should generally be one canonical Person identity for a human.

Roles such as Employee, Candidate, Contractor, Owner, Advisor, Customer Stakeholder and Project Resource are represented through relationships, positions, assignments and contextual roles rather than duplicate Person identities.

Important adjacent concepts at domain level may include Position, Position Holding, Employment Relationship, Candidate Relationship, Independent Engagement Relationship, Assignment and Business Role.

---

## 7. Business Relationship umbrella

`BusinessRelationship` is a useful umbrella concept for ongoing material relationships among parties.

Relationship families include:

### Commercial
Customer; Partner; Vendor; Competitor; Technology Provider.

### Workforce / talent
Employment; Contractor; Candidate; Recruiter; Staffing Provider.

### Professional services
Accountant/Auditor; Tax Advisor; Attorney; Insurance Broker; Consultant.

### Financial
Bank; Lender; Payment Provider; Investor.

### Government / compliance
Regulator; Tax Authority; Certification Body; Registered Agent; Procurement Authority.

### Ecosystem
Association; Membership Organization; University; Community Organization; Referral Source.

### Property / operations
Landlord; Office Provider; Utility Provider; Facilities Vendor.

The umbrella should not become one flat type code. The model should preserve parties, relationship family/type, participant roles, scope/context, effective period, state, significance, evidence, confidence and security.

Different relationship shapes are allowed, including Organization↔Organization and Person↔Organization.

---

## 8. Purpose-to-value spine

```text
Enterprise
 -> Vision
 -> Mission
 -> Strategic Objective
 -> Initiative
 -> Market
 -> Customer Segment
 -> Account / Customer
 -> Stakeholder
 -> Problem / Pain
 -> Desired Outcome
 -> Capability
 -> Offering
 -> Opportunity
 -> Solicitation
 -> Proposal / Artifact
 -> Agreement
 -> Obligation
 -> Project
 -> Deliverable
 -> Acceptance
 -> Invoice
 -> Payment
 -> Customer Outcome
 -> Enterprise Outcome
 -> Strategic Learning
```

This is a traceability spine, not a rigid hierarchy. Business Intent resources may live in their own model but link into this spine.

---

## 9. Operating Resource Network

```text
Legal Entity
Organization Unit
Person
Position
Role
Employment Relationship
Partner Relationship
Skill
Capability
Credential
Availability
Capacity
Assignment
Asset
System
Technology
Contract Vehicle
Certification
Location
Budget
Cost
Rate
Authority
```

This is a network, not a tree.

---

## 10. Decision and control fabric

The ontology should support the connected decision loop:

```text
Signal
Event
Observation
Claim
Evidence
Assessment
Assumption
Model
Prediction
Recommendation
Alternative
Decision
Approval
Delegation
Action
Automation
Policy
Constraint
Risk
Scenario
State Change
Outcome
Learning
```

Not all of these must become L1 object types. Some may be domain resources, links, interfaces or specialized types. The semantic distinctions must be preserved.

---

## 11. Opportunity model

`Opportunity` represents a commercial pursuit or potential business outcome, not merely a CRM row.

Potential relationships:

```text
Opportunity -> Customer Organization
Opportunity -> Customer Organizational Unit
Opportunity -> Solicitation
Opportunity -> Partner Relationship
Opportunity -> Stakeholder(s)
Opportunity -> Capability requirements
Opportunity -> Offering
Opportunity -> Agreement(s)
Opportunity -> Proposal Artifact(s)
Opportunity -> Decision(s)
Opportunity -> Event(s)
Opportunity -> Project (if awarded/converted)
```

Opportunity aliases are expected and must be contextual. The canonical name should not be replaced by shorthand.

---

## 12. Solicitation versus Opportunity

A customer-issued RFP/solicitation and GenSigma's opportunity are related but distinct.

A Solicitation exists independently of whether GenSigma pursues it. An Opportunity represents GenSigma's commercial pursuit/context.

This supports no-bid decisions, reissues/amendments, external solicitations monitored but not pursued, and more than one pursuit around a procurement program.

---

## 13. Agreement model

Agreement is a general legal/operational instrument.

Domain specializations may include NDA/MNDA, MSA, subcontract, teaming agreement, work order, statement of work, purchase order, customer contract and vendor agreement.

Agreement status must be grounded in authoritative evidence such as executed artifacts where applicable.

---

## 14. Artifact / Document model

`Artifact` represents meaningful business evidence or work product such as email, attachment, RFP, proposal, pricing spreadsheet, agreement PDF, invoice, resume, presentation or meeting notes.

A distinction may later be needed among Artifact, Document and Message, but V1 should avoid premature hierarchy.

Version lineage and source representations must be supported.

---

## 15. Event model

Events represent what happened.

Initial commercial event types include OpportunityDiscovered, RFPReleased, BidDecisionMade, PartnerContacted, NDARequested, AgreementExecuted, PricingRequested, ProposalSubmitted, InterviewScheduled, InterviewCompleted, AwardReceived, OpportunityLost, OpportunityCancelled, ProjectStarted, InvoiceIssued and PaymentReceived.

Event types should be added from real decision loops, not exhaustive brainstorming.

---

## 16. Decision model

Decision is distinct from Event.

Examples include bid/no-bid, partner selection, resource selection, pricing approval and proposal submission approval.

Decision traces link evidence, assessment, alternatives, recommendations, approvals, actions and outcomes.

---

## 17. Action model

Action types represent governed verbs.

Initial candidates:

- QualifyOpportunity;
- ApproveBid;
- DeclineBid;
- AddPartnerToOpportunity;
- ApprovePartner;
- RequestNDA;
- ApproveAgreement;
- RequestPricing;
- SubmitProposal;
- RecordAward;
- ConvertOpportunityToProject;
- IssueInvoice;
- EscalateReceivable.

Action definitions should eventually include permission, precondition, policy, effect and audit semantics.

---

## 18. Interfaces

Candidate interfaces include `Party`, `TemporalObject`, `EvidenceBacked`, `SecuredResource`, `Actionable`, `DecisionContext`, `VersionedArtifact`, `Locatable` and `ExternallySourced`.

Interfaces should represent common shape/capability, not create accidental inheritance trees.

---

## 19. State and time

Objects and relationships should support temporal state where material.

Key times: effective/business time, source time, recorded time and discovery time. Historical, current and scenario truth must remain separable.

---

## 20. Security

Security is part of ontology semantics. The design must permit object-level restrictions, property-level restrictions, evidence-level restrictions, action permissions, domain restrictions and delegated authority.

App views and agents may expose only the authorized projection of an object.

---

## 21. RFP-to-cash first deep chain

The first deep domain chain is:

```text
Customer
 -> Opportunity
 -> Solicitation
 -> Partner(s)
 -> Proposal
 -> Agreement
 -> Project
 -> Deliverable
 -> Invoice
 -> Payment
 -> Outcome
```

This chain should connect upward to Business Intent and downward to delivery/finance. The objective is not to implement it all at once; it is to ensure early modeling does not block it.

---

## 22. V1 guardrails

Initial target ranges:

- promoted core object types: roughly 12-18;
- first domain extensions: roughly 12-18;
- total V1 object types: roughly 25-35;
- relationship/link types: roughly 35-60;
- interfaces: roughly 8-12;
- event types: roughly 15-25;
- action types: roughly 10-20.

These are complexity guardrails, not quotas.

---

## 23. Competency questions

The ontology should support questions such as:

1. Who is this organization and what relationships does GenSigma have with it?
2. What aliases have referred to this opportunity over time?
3. Which solicitation created this opportunity?
4. Which partners were considered and which were used?
5. What agreements govern the relationship?
6. What events changed opportunity state?
7. What evidence supports the current state?
8. What decision caused the next action?
9. What project resulted from an award?
10. What invoice/payment/outcome resulted?
11. What was true at a historical point in time?
12. What action is permitted now?

---

## 24. Golden action tests

The model should also be tested by verbs, not only queries: approve a bid, approve a teaming partner, request pricing, submit a proposal, record an award and convert opportunity to project.

If the ontology cannot support the business action without bypassing its semantics, the model is incomplete.

---

## 25. Non-goals

V1 will not mirror source-system schemas, treat Customer/Partner/Vendor as duplicate Organization identities, model CCSF as a special ontology class, use `Branch` as a generic US state-registration concept, promote every email noun to an object type, build a deep inheritance hierarchy, or finalize every finance/workforce type before the RFP-to-cash slice is proven.
