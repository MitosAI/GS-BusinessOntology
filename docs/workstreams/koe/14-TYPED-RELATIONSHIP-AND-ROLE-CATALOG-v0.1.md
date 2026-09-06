# Business Reality V1 — Typed Relationship and Role Catalog

**Version:** v0.1  
**Status:** KOE semantic baseline  
**Owner:** Knowledge & Ontology Engineering (KOE-001)

---

## 1. Purpose

Business Reality is a network of typed, scoped, temporal relationships. This catalog defines the first enterprise relationship vocabulary that connects the 38 V1 business objects without turning contextual roles into duplicate identities.

A relationship is promoted to an independently governed relationship resource when business meaning requires its own:

- participants/roles;
- scope;
- state;
- effective period;
- evidence/provenance;
- security;
- correction history;
- actions.

Otherwise it may be represented as a typed link.

---

## 2. Relationship invariants

1. **Identity is not role.** `Organization: X` may be Customer, Partner, Vendor, Subcontractor, Competitor, or Technology Provider in different contexts.
2. **Scope is explicit.** A relationship may apply enterprise-wide, to one Opportunity, Agreement, Project, OrganizationalUnit, or other context.
3. **Time is explicit where material.** Current relationship does not imply historical relationship and vice versa.
4. **Evidence is retrievable.** Material relationship assertions retain provenance.
5. **Correction preserves history.** Reclassification or participant correction does not erase the prior accepted interpretation.
6. **Links do not smuggle ownership.** Relationship names must not imply stronger semantics than the underlying contract defines.

---

# 3. Structural relationships

| Link | From | To | Meaning |
|---|---|---|---|
| `part_of` | LegalEntity / OrganizationalUnit | Organization / OrganizationalUnit | structural containment/affiliation |
| `owns` | Organization / LegalEntity | Asset / System / other ownable resource | legal/economic ownership where supported |
| `operates` | Organization / OrganizationalUnit | System / Asset | operational responsibility/control |
| `located_at` | LegalEntity / OrganizationalUnit / Project / Asset | Place | material physical/operating location |
| `registered_office_at` | LegalEntity | Place | legally designated registered office for effective period |
| `holds_position` | Person | Position | temporal position-holding relationship |
| `position_in` | Position | OrganizationalUnit / Organization | structural home of Position |
| `reports_to_position` | Position | Position | reporting structure; avoid Person→Person when role is intended |

### Structural rules

- `part_of` does not imply legal ownership unless explicitly modeled.
- organization reorgs are temporal relationship changes.
- `registered_office_at` must not be represented as a fake branch/subsidiary object.

---

# 4. Party and business relationship semantics

## 4.1 BusinessRelationship participant model

A material `BusinessRelationship` has:

```text
relationship_id
relationship_family
relationship_type
participants[]
  party_id
  contextual_role
scope
state
effective_period
evidence[]
security
correction_history
```

### Contextual organization roles

```text
Customer
Prospect
Partner
TeamingPartner
Subcontractor
PrimeContractor
Vendor
Supplier
TechnologyProvider
Competitor
ReferralSource
Lender
Bank
Insurer
AdvisorFirm
CertificationBody
Regulator
ProcurementAuthority
Landlord
Association
```

### Contextual person roles

```text
Employee
Contractor
Candidate
Advisor
Stakeholder
DecisionMaker
Approver
ProjectResource
AccountOwner
OpportunityOwner
ProjectManager
ExecutiveSponsor
CustomerContact
PartnerContact
```

Roles are extensible controlled vocabulary, not canonical party types.

## 4.2 Relationship families

| Family | Typical examples |
|---|---|
| Commercial | customer, prospect, partner, vendor, competitor |
| Workforce | employee, contractor, candidate, recruiter |
| Professional | attorney, accountant, consultant, broker |
| Financial | bank, lender, payment provider, investor |
| Government/compliance | regulator, certification body, registered agent |
| Ecosystem | association, university, referral source |
| Property/operations | landlord, utility, facilities provider |

---

# 5. Commercial / revenue relationships

| Link | From | To | Meaning |
|---|---|---|---|
| `for_customer` | Opportunity | Organization / OrganizationalUnit | customer context for pursuit |
| `responds_to` | Opportunity | Solicitation | pursuit is response to procurement instrument |
| `uses_vehicle` | Opportunity / Solicitation / Agreement | ContractVehicle | governed procurement vehicle |
| `offers` | Opportunity / Proposal | Offering | offering proposed in pursuit |
| `requires_capability` | Opportunity / Solicitation | Capability | required ability for pursuit |
| `has_proposal` | Opportunity | Proposal | proposal business object for pursuit |
| `proposal_for` | Proposal | Solicitation / Opportunity | proposal target/context |
| `represented_by` | Proposal | Artifact | one or more proposal artifacts/versions |
| `governed_by_agreement` | Opportunity / Project / BusinessRelationship | Agreement | legal/operational instrument governing context |
| `creates_obligation` | Agreement / Solicitation | Obligation | source instrument creates material duty |
| `party_to` | Organization / LegalEntity / Person | Agreement | party/signatory/beneficiary relationship with participant role |
| `partner_in` | Organization | Opportunity / Proposal / Project | contextual partner participation; typically backed by BusinessRelationship |
| `stakeholder_in` | Person / Organization | Opportunity / Project | scoped stakeholder relationship |

### Commercial rules

- `Solicitation` and `Opportunity` never collapse into one object.
- `Proposal` and its `Artifact` representations remain distinct.
- `partner_in(Opportunity)` does not imply enterprise-wide partnership.
- award/loss is represented by Event/Outcome/state change, not by renaming the Opportunity.

---

# 6. Delivery relationships

| Link | From | To | Meaning |
|---|---|---|---|
| `arises_from` | Project | Opportunity / Agreement | commercial/legal origin of project |
| `fulfills` | Project | Agreement / Obligation | work satisfies governed commitment |
| `has_milestone` | Project | Milestone | execution checkpoint |
| `produces` | Project | Deliverable | execution output |
| `satisfies` | Deliverable | Obligation / Milestone | output satisfies requirement/checkpoint |
| `represented_by` | Deliverable | Artifact | document/file/work-product representations |
| `assigned_to` | Assignment | Project / Opportunity / OrganizationalUnit | business context receiving resource |
| `assigns_resource` | Assignment | Person / OrganizationalUnit | assigned resource |
| `requires_skill` | Assignment / Project | Skill | required human competency |
| `requires_capability` | Project / Assignment | Capability | required execution ability |
| `accepts` | Approval / Event | Deliverable | formal acceptance/review occurrence |
| `blocked_by` | Project / Milestone / Deliverable | Risk / Obligation / dependency resource | explicit execution blocker |

### Delivery rules

- Project is not synonymous with Agreement or Opportunity.
- assignment lifecycle is independent of employment/contractor relationship.
- Deliverable identity is independent of file/version identity.

---

# 7. Financial relationships

| Link | From | To | Meaning |
|---|---|---|---|
| `funds` | Budget | Project / OrganizationalUnit / Opportunity | authorized financial envelope |
| `bills_for` | Invoice | Agreement / Project / Deliverable | commercial basis of invoice |
| `issued_by` | Invoice | LegalEntity / Organization | billing party |
| `issued_to` | Invoice | LegalEntity / Organization | billed party |
| `settles` | Payment | Invoice | payment application/reconciliation |
| `paid_by` | Payment | LegalEntity / Organization | payer |
| `received_by` | Payment | LegalEntity / Organization | payee |
| `financial_outcome_of` | Outcome | Project / Opportunity / Agreement | linked financial result |

### Financial rules

- Invoice issuance and Payment settlement are separate events/resources.
- partial payment must not force Invoice state to paid.
- reversals/voids are temporal/correction transitions, not destructive deletion.

---

# 8. Workforce and capability relationships

| Link | From | To | Meaning |
|---|---|---|---|
| `has_skill` | Person | Skill | evidenced competency relationship |
| `holds_credential` | Person / Organization | Credential | qualification/attestation |
| `holds_certification` | Person / Organization / LegalEntity | Certification | governed certification status |
| `possesses_capability` | Organization / OrganizationalUnit / Person | Capability | durable ability relationship |
| `requires_capability` | Offering / Opportunity / Project / Position | Capability | required ability |
| `requires_skill` | Position / Assignment | Skill | required competency |
| `depends_on` | Capability | Person / System / Technology / BusinessRelationship / Credential | material dependency |
| `supports_capability` | Skill / Credential / Certification / System / Technology | Capability | evidence/resource supporting capability |

### Workforce/capability rules

- `Capability` is not a current availability reading.
- proficiency, availability, and capacity are time-bound measures/claims unless later admitted as objects.
- Employee/Contractor/Candidate remain relationship roles around Person.

---

# 9. Technology and asset relationships

| Link | From | To | Meaning |
|---|---|---|---|
| `uses_technology` | System / Asset / Offering | Technology | implementation/dependency relationship |
| `hosted_on` | System | System / Technology / Asset | hosting/execution dependency where useful |
| `depends_on` | System / Capability | System / Technology / Asset | operational dependency |
| `supports` | System / Technology / Asset | Capability / Project / OrganizationalUnit | operational support |
| `assigned_to` | Asset | Person / OrganizationalUnit / Project | possession/operational assignment |
| `provided_by` | Technology / System / Asset | Organization | provider/vendor identity without redefining provider as type |
| `governed_by_agreement` | System / Technology / Asset | Agreement | license/service/maintenance agreement |
| `has_risk` | System / Technology / Asset | Risk | material operational/security/business risk |

### Technology rules

- source CMDB relationships are evidence, not canonical truth.
- product, system instance, and vendor organization remain distinguishable.

---

# 10. Legal and compliance relationships

| Link | From | To | Meaning |
|---|---|---|---|
| `registered_in` | Registration | Place / jurisdiction | jurisdictional scope |
| `registration_of` | Registration | LegalEntity / Organization / Person | holder/subject |
| `certified_by` | Certification | Organization | certifying body |
| `held_by` | Certification / Credential | Person / Organization / LegalEntity | holder |
| `requires` | ContractVehicle / Agreement / Opportunity | Certification / Registration / Credential | qualification requirement |
| `creates_obligation` | Registration / Certification / Agreement | Obligation | renewal/reporting/compliance duty |
| `evidenced_by` | Registration / Certification / Credential | Artifact | authoritative/supporting evidence |
| `subject_to` | LegalEntity / Organization / Project | Obligation / Risk | governed compliance exposure |

### Legal/compliance rules

- Registration and Certification are independent from their evidence files.
- expiration/renewal are temporal transitions.
- legal entity and organizational operating structure remain distinct.

---

# 11. Evidence, judgment, action, and outcome relationships

| Link | From | To | Meaning |
|---|---|---|---|
| `asserts_about` | Claim | any business object/relationship/state | proposition subject |
| `supported_by` | Claim / Assessment / Decision | Artifact / evidence reference | supporting provenance |
| `contradicted_by` | Claim | Claim / Artifact / evidence reference | incompatible evidence/assertion |
| `supersedes` | Claim / Assessment / Decision / interpretation | prior resource/interpretation | correction/version lineage |
| `evaluates` | Assessment | any material context | subject of judgment |
| `identifies_risk` | Assessment | Risk | assessment produces/updates risk view |
| `affects` | Risk | any material context | scope of risk |
| `informs` | Claim / Assessment / Risk | Decision | input to choice |
| `made_by` | Decision | Person / Position / governed actor | decision authority/actor |
| `approved_by` | Approval | Person / Position / governed actor | approving authority |
| `authorizes` | Approval | Decision / Action / Proposal / Agreement / Budget | authorized subject |
| `triggers` | Decision / Event | Action | causal/operational trigger |
| `performed_by` | Action | Person / Organization / system/agent actor reference | actor |
| `changes_state_of` | Action | business object / relationship | intended state target |
| `recorded_as` | Action | Event | resulting occurrence record when appropriate |
| `results_in` | Action / Decision / Project / Opportunity | Outcome | result linkage |
| `evidences` | Artifact / Event | Claim / state / Action / Outcome | evidence role |

### Cognition/action rules

- Event ≠ Decision ≠ Approval ≠ Action ≠ Outcome.
- a decision may exist without a subsequent action.
- an action may fail and still have an Event/audit trail.
- outcome attribution may be strong, weak, or unknown and must not be overstated.

---

# 12. Relationship state model

Material relationships should support a common minimum state envelope:

```text
proposed
active
suspended
terminated
expired
superseded
unresolved
```

Domain-specific states may extend this set. A relationship state must not be inferred solely from recency of evidence.

---

# 13. Scope model

Relationship scope should be explicit using one or more canonical context references:

```text
enterprise
organization
organizational_unit
opportunity
solicitation
proposal
agreement
project
assignment
system
other governed context
```

A broader scope must never be inferred from a narrow one without evidence/governance.

---

# 14. Cardinality posture

V1 should avoid unnecessary hard cardinality where real business reality is variable. Hard constraints are appropriate only for semantic impossibilities or invariants.

Examples:

- a Payment may settle multiple Invoices and an Invoice may receive multiple Payments;
- an Opportunity may reference multiple Solicitations in unusual procurement histories;
- a Person may hold multiple Positions;
- an Agreement may have multiple parties;
- a Proposal may have multiple Artifact versions/appearances;
- an Organization may have multiple roles in one context if business semantics justify it.

Cardinality should follow business truth, not database convenience.

---

# 15. Correction behavior

When a relationship is wrong:

```text
preserve original evidence
preserve prior accepted interpretation
record correction/supersession
repair participant/scope/type/time
recompute dependent projections
retain audit trail
```

Never mutate history to make the current graph look clean.

---

## 16. Implementation requirement

Codex should express this catalog through machine-readable relationship contracts. A typed relationship contract must be able to represent:

- relationship ID/type/version;
- participants and contextual roles;
- scope;
- state;
- effective time;
- evidence/provenance;
- epistemic status;
- security;
- audit/correction/supersession.

Domain schemas should reuse that contract rather than invent incompatible relationship structures.
