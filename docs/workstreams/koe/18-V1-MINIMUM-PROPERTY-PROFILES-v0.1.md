# Business Reality V1 — Minimum Property Profiles

**Version:** v0.1  
**Status:** KOE implementation baseline  
**Owner:** Knowledge & Ontology Engineering (KOE-001)

---

## 1. Rule

All objects compose the common kernel envelope from `16-CORE-RESOURCE-ENVELOPE-AND-VERSIONING-v0.1.md`.

The properties below are **domain-specific minimums**, not complete database schemas.

Do not duplicate kernel fields such as canonical ID, contract version, effective time, provenance, security, audit, source mappings, aliases, or supersession inside every object definition.

---

# A. Enterprise identity and structure

## Organization

Minimum domain properties:

```text
canonical_name
organization_kind?
website_domain?
external_identifiers[]?
operational_status?
```

## LegalEntity

```text
legal_name
entity_type?
formation_jurisdiction
formation_date?
legal_identifiers[]?
legal_status
```

## OrganizationalUnit

```text
name
unit_kind
parent_scope_ref
purpose_or_function?
status
```

## Person

```text
preferred_name
full_name?
primary_contact_methods[]?
external_identifiers[]?
```

Sensitive personal attributes are excluded unless a governed business need exists.

## Position

```text
position_name
position_code?
organizational_scope_ref
position_kind?
status
```

## Place

```text
place_kind
canonical_label
address_components?
jurisdiction_code?
geo_reference?
```

---

# B. Relationships and commercial / revenue

## BusinessRelationship

```text
relationship_family
relationship_type
participants[]
context_scope_ref?
relationship_state
relationship_significance?
```

## Opportunity

```text
canonical_name
opportunity_kind?
commercial_stage
customer_ref?
owner_ref?
expected_value?
currency?
expected_close_date?
```

Amounts and dates may be unknown/estimated and must carry appropriate epistemic/time semantics.

## Solicitation

```text
solicitation_title
issuer_ref
solicitation_identifier?
procurement_method?
issue_date?
response_deadline?
solicitation_status
```

## Offering

```text
offering_name
offering_family?
offering_version?
status
owner_scope_ref?
```

Primary semantic owner is Business Intent.

## Proposal

```text
proposal_name
opportunity_ref
proposal_version?
proposal_status
submission_deadline?
submitted_at?
```

## Agreement

```text
agreement_name
agreement_type
parties[]
agreement_status
effective_date?
expiration_date?
execution_date?
```

## Obligation

```text
obligation_type
obligation_summary
source_ref
responsible_party_ref?
due_date_or_period?
obligation_status
```

## ContractVehicle

```text
vehicle_name
issuing_authority_ref
vehicle_identifier?
vehicle_type?
start_date?
end_date?
vehicle_status
```

---

# C. Delivery and financial execution

## Project

```text
project_name
project_type?
customer_ref?
project_status
start_date?
target_end_date?
actual_end_date?
project_owner_ref?
```

## Milestone

```text
milestone_name
parent_context_ref
planned_date?
actual_date?
milestone_status
owner_ref?
```

## Deliverable

```text
deliverable_name
deliverable_type?
project_ref
owner_ref?
due_date?
deliverable_status
acceptance_status?
```

## Budget

```text
budget_name
scope_ref
budget_period
currency
approved_amount?
status
owner_ref?
version_label?
```

## Invoice

```text
invoice_number
issuer_ref
recipient_ref
currency
amount_due
issue_date
due_date?
invoice_status
```

## Payment

```text
payment_reference?
payer_ref
payee_ref
currency
amount
payment_date?
settlement_date?
payment_status
```

---

# D. Workforce and executable capability

## Assignment

```text
assignee_ref
assignment_scope_ref
assignment_role
allocation_fraction_or_units?
start_date?
end_date?
assignment_status
```

## Capability

```text
capability_name
capability_family?
capability_level_or_tier?
status?
```

Dynamic feasibility is not a static property of this object.

## Skill

```text
skill_name
skill_family?
taxonomy_code?
status
```

## Credential

```text
credential_type
holder_ref
issuing_authority_ref?
credential_identifier?
issue_date?
expiration_date?
credential_status
```

## Certification

```text
certification_type
holder_ref
certifying_authority_ref
certificate_identifier?
issue_date?
expiration_date?
certification_status
```

---

# E. Systems and operational resources

## Asset

```text
asset_name
asset_type
owner_ref?
serial_or_asset_tag?
acquisition_date?
asset_status
```

## System

```text
system_name
system_kind?
owner_scope_ref?
business_function?
system_status
criticality?
```

## Technology

```text
technology_name
technology_kind?
provider_ref?
product_family?
version?
support_status?
```

---

# F. Legal/compliance state

## Registration

```text
registration_type
holder_ref
jurisdiction_ref
authority_ref?
registration_identifier?
registration_status
issue_or_effective_date?
expiration_or_renewal_date?
```

---

# G. Knowledge, activity, judgment, and control

## Artifact

```text
artifact_name
artifact_kind
canonical_media_type?
artifact_status?
current_version_ref?
```

Source appearances, hashes, paths, and binary versions belong to provenance/source structures.

## Event

```text
event_type
subject_refs[]
participant_refs[]?
event_time
event_summary?
```

## Claim

```text
predicate_or_claim_type
subject_refs[]
object_value_or_ref
claim_polarity?
claim_status
```

Provenance and epistemic status remain kernel fields.

## Assessment

```text
assessment_type
subject_refs[]
assessment_result
assessor_ref?
method_ref?
assessment_status
```

## Risk

```text
risk_title
risk_type?
scope_refs[]
risk_owner_ref?
risk_status
likelihood_assessment_ref?
impact_assessment_ref?
```

## Decision

```text
decision_question
decision_scope_refs[]
decision_maker_refs[]?
chosen_option_ref_or_value?
decision_status
decided_at?
```

## Approval

```text
approval_subject_ref
approver_ref
authority_basis_ref?
approval_status
requested_at?
decided_at?
```

## Action

```text
action_type
actor_ref
target_refs[]
action_status
requested_at?
started_at?
completed_at?
idempotency_key?
```

## Outcome

```text
outcome_type
subject_refs[]
outcome_value_or_summary
measurement_period?
outcome_status
attribution_strength?
```

---

## 2. Property design rules

1. **No property duplicates canonical identity.** Names, codes, and source IDs do not become identity by themselves.
2. **Unknown is allowed.** Required business semantics do not imply every field must always be known.
3. **Material estimates are labeled.** Estimated values/dates must remain distinguishable from authoritative values.
4. **Temporal values use the kernel.** Do not add random `updated_at` fields as a substitute for effective-time semantics.
5. **Evidence-backed properties preserve provenance.** Material property values must be traceable when used canonically.
6. **Sensitive properties are not added casually.** Security/privacy classification is part of admission.
7. **Derived properties are marked as derived.** They can be recomputed and must not masquerade as directly observed facts.
8. **Enums are governed.** Domain vocabularies may evolve through versioned controlled terms; free-text is not a substitute for missing semantics.

---

## 3. Codex rule

The machine-readable schemas may add structural details necessary for JSON Schema/OpenAPI correctness, but they must not invent new required business properties or lifecycle meanings without raising an open semantic question.
