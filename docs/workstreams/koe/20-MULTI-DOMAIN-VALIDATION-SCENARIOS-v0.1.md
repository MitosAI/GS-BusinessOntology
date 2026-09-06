# Build Spec 001 — Multi-Domain Validation Scenarios

**Version:** v0.1  
**Status:** KOE validation baseline  
**Owner:** Knowledge & Ontology Engineering (KOE-001)

---

## 1. Purpose

The semantic foundation must be validated against structurally different enterprise situations. No single customer, opportunity, or source system is allowed to define the ontology.

Each scenario below is synthetic by default. Real GenSigma evidence can later replace or augment it without changing the expected semantic behavior.

Every scenario must test:

- identity;
- contextual role;
- evidence/provenance;
- time;
- ambiguity or contradiction;
- correction;
- security;
- cross-domain relationships.

---

# Scenario A — Commercial pursuit

## Story

GenSigma identifies a public-sector solicitation, evaluates whether to pursue it, involves a teaming partner, prepares a proposal, obtains internal approval, submits the proposal, and later receives an award/loss outcome.

## Required objects

```text
Organization
Person
BusinessRelationship
Opportunity
Solicitation
Offering
Proposal
Agreement? / ContractVehicle?
Artifact
Claim
Assessment
Risk
Decision
Approval
Action
Event
Outcome
```

## Required relationships

```text
Opportunity -> for_customer -> Organization
Opportunity -> responds_to -> Solicitation
Opportunity -> offers -> Offering
Organization(partner) -> partner_in -> Opportunity
Opportunity -> has_proposal -> Proposal
Proposal -> represented_by -> Artifact
Assessment/Risk -> informs -> Decision
Approval -> authorizes -> Action/Proposal
Action -> changes_state_of -> Proposal/Opportunity
Action/Event -> results_in -> Outcome
```

## Difficult cases

1. Customer appears under acronym, legal name, and agency shorthand.
2. Partner organization is partner only in this pursuit.
3. Solicitation title and Opportunity shorthand overlap but remain distinct objects.
4. Proposal v1 and v2 exist in different source locations.
5. Email says “submitted” before authoritative submission receipt appears.
6. Bid decision is inferred from behavior but no explicit decision artifact exists.
7. Later evidence corrects the actual submission time.
8. One proposal artifact is access-restricted.

## Expected semantics

- aliases resolve contextually without creating duplicate organizations;
- solicitation and opportunity remain distinct;
- proposal submission is not canonical until sufficient evidence/promotion;
- inferred decision remains labeled reconstructed/inferred;
- correction changes accepted state/time without deleting prior evidence;
- restricted artifact does not leak through search/traversal.

---

# Scenario B — Delivery / project execution

## Story

An awarded engagement becomes a Project. People are assigned, milestones and deliverables are tracked, a deliverable is rejected then accepted after rework, and work reaches completion.

## Required objects

```text
Organization
Project
Agreement
Obligation
Assignment
Person
Position
Skill
Capability
Milestone
Deliverable
Artifact
Risk
Action
Event
Approval
Outcome
```

## Required relationships

```text
Project -> arises_from -> Agreement/Opportunity
Project -> fulfills -> Obligation
Assignment -> assigns_resource -> Person
Assignment -> assigned_to -> Project
Project -> has_milestone -> Milestone
Project -> produces -> Deliverable
Deliverable -> satisfies -> Milestone/Obligation
Deliverable -> represented_by -> Artifact
Approval/Event -> accepts -> Deliverable
Risk -> affects -> Project/Milestone
```

## Difficult cases

1. Project folder name differs from canonical Project name.
2. Person changes Position while Assignment continues.
3. Deliverable “final” file exists before customer acceptance.
4. Milestone due date changes twice.
5. Customer rejects deliverable then later accepts revised version.
6. Same Artifact appears in email and SharePoint.
7. Project risk severity changes over time.

## Expected semantics

- Project identity is independent of folder, agreement, and opportunity;
- Position change does not break Person or Assignment identity;
- final artifact does not imply accepted Deliverable;
- schedule revisions preserve historical dates;
- rejection and later acceptance remain separate events/states;
- duplicate artifact appearances preserve common origin lineage.

---

# Scenario C — Workforce / resource lifecycle

## Story

A Person is recruited, becomes a contractor, later becomes an employee, receives credentials, holds a Position, and is assigned to multiple projects over time.

## Required objects

```text
Person
Organization
BusinessRelationship
Position
Assignment
Skill
Credential
Certification
Capability
Project
Artifact
Claim
Event
Action
```

## Required relationships

```text
Person -> participates_in -> BusinessRelationship
Person -> holds_position -> Position
Person -> has_skill -> Skill
Person -> holds_credential -> Credential
Person -> holds_certification -> Certification
Assignment -> assigns_resource -> Person
Assignment -> assigned_to -> Project
Skill/Credential -> supports_capability -> Capability
```

## Difficult cases

1. Candidate email and employee email are different.
2. Name spelling differs across sources.
3. Contractor relationship ends before employment begins.
4. One credential expires while Assignment remains active.
5. Availability is discussed in email but is not a first-class object.
6. HR evidence is more restricted than project staffing data.

## Expected semantics

- one canonical Person survives all role/employer/contact changes;
- Candidate/Contractor/Employee are temporal contextual roles;
- expired Credential state does not delete credential history;
- availability remains measurement/claim unless admission policy changes;
- security permits project staffing projection without exposing restricted HR evidence.

---

# Scenario D — Legal / compliance lifecycle

## Story

A LegalEntity qualifies in a new jurisdiction, designates a registered office, obtains/renews a certification, misses one renewal deadline, corrects the record, and later changes registered office.

## Required objects

```text
Organization
LegalEntity
Place
Registration
Certification
Obligation
Artifact
Claim
Event
Risk
Action
Outcome
```

## Required relationships

```text
LegalEntity -> part_of -> Organization
Registration -> registration_of -> LegalEntity
Registration -> registered_in -> Place/jurisdiction
LegalEntity -> registered_office_at -> Place
Certification -> held_by -> LegalEntity
Registration/Certification -> creates_obligation -> Obligation
Artifact -> evidences -> Registration/Certification/Claim
Risk -> affects -> Registration/LegalEntity
```

## Difficult cases

1. “Branch” appears in source text but legal reality is foreign qualification.
2. Registered office changes without new LegalEntity.
3. Renewal email claims status is active but state registry evidence says delinquent.
4. Correction later shows delinquency started earlier than first discovered.
5. Certification renewal creates new term/expiration date.

## Expected semantics

- no fake Branch object is created;
- registered office is temporal relationship;
- authority-specific evidence controls canonical registration state;
- discovery time differs from effective delinquency time;
- certification renewal preserves prior term history.

---

# Scenario E — Vendor / technology lifecycle

## Story

GenSigma adopts a software technology from a vendor, signs an agreement, operates a system using that technology, later learns of end-of-support risk, migrates to a successor technology, and terminates the old agreement.

## Required objects

```text
Organization
BusinessRelationship
Agreement
System
Technology
Asset?
Capability
Risk
Assessment
Decision
Approval
Action
Event
Outcome
Artifact
```

## Required relationships

```text
Organization(vendor) -> participates_in -> BusinessRelationship
System -> uses_technology -> Technology
Technology -> provided_by -> Organization
System/Technology -> governed_by_agreement -> Agreement
System -> supports -> Capability
Risk -> affects -> Technology/System
Assessment -> informs -> Decision
Approval -> authorizes -> Action
Action -> changes_state_of -> System/Technology/Agreement
```

## Difficult cases

1. Vendor and product share a similar name.
2. Technology version changes without creating new vendor Organization.
3. One source calls the product “platform,” another uses product family name.
4. End-of-support date is revised by vendor.
5. Migration action succeeds but old agreement termination lags.

## Expected semantics

- vendor Organization, Technology, and System remain distinct;
- version/name normalization preserves source labels;
- revised external/vendor evidence updates risk/effective time without deleting prior assessment;
- migration and contract termination remain separate actions/events.

---

# Scenario F — Financial execution

## Story

A Project generates an Invoice. The customer makes two partial Payments, one is reversed, a dispute occurs, and a corrected payment later settles the balance.

## Required objects

```text
Organization
LegalEntity
Agreement
Project
Deliverable
Invoice
Payment
Artifact
Claim
Event
Action
Outcome
```

## Required relationships

```text
Invoice -> bills_for -> Project/Agreement/Deliverable
Invoice -> issued_by -> LegalEntity
Invoice -> issued_to -> Organization/LegalEntity
Payment -> settles -> Invoice
Payment -> paid_by -> Organization/LegalEntity
Payment -> received_by -> LegalEntity
Outcome -> financial_outcome_of -> Project/Agreement
```

## Difficult cases

1. Invoice PDF and accounting-system record disagree on due date.
2. First payment is partial.
3. Second payment settles balance but later reverses.
4. Email says “paid” before bank settlement.
5. Corrected payment arrives later.
6. One financial artifact is restricted to finance users.

## Expected semantics

- authoritative source/authority rules determine canonical due date/payment state;
- Invoice transitions through partial/paid states from reconciled Payment allocations;
- reversal does not delete original Payment;
- email statement is Claim/evidence, not settlement truth;
- finance security applies through search, evidence, and traversal.

---

## 2. Cross-scenario acceptance requirements

The complete validation portfolio must demonstrate:

1. one canonical identity across changing roles and source identifiers;
2. same-name distinct entities remain distinct;
3. contextual role does not mutate party identity;
4. source evidence remains immutable;
5. interpretations can be corrected/reversed;
6. effective time differs from discovery/recorded time;
7. duplicate evidence origin is not false corroboration;
8. restricted evidence does not leak;
9. Event, Assessment, Decision, Approval, Action, and Outcome are distinguishable;
10. cross-model references use stable canonical IDs and ownership;
11. no scenario requires a customer-specific ontology class;
12. the same kernel envelope works in all domains.

---

## 3. Fixture packaging rule

Each synthetic fixture pack should include:

```text
README.md
sources/
expected-identities.yaml
expected-relationships.yaml
expected-state-timeline.yaml
expected-claims.yaml
expected-security.yaml
expected-corrections.yaml
expected-actions-outcomes.yaml
```

The fixture itself is not canonical truth. The expected files define the validation oracle for the contract build and must be reviewed as part of the spec.
