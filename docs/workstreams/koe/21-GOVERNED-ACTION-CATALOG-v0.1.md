# Business Reality V1 — Governed Action Catalog

**Version:** v0.1  
**Status:** KOE semantic baseline  
**Owner:** Knowledge & Ontology Engineering (KOE-001)

---

## 1. Purpose

The ontology is operational only if it supports governed verbs, not just nouns.

An Action is a first-class governed act by a human, service, or AI agent. Every material Action must preserve authority, preconditions, intended effect, execution status, evidence, idempotency where applicable, and audit history.

---

## 2. Common Action contract

Conceptual shape:

```text
Action
  action_id
  action_type
  actor_ref
  target_refs[]
  context_refs[]
  requested_at
  authorized_by?
  authority_basis?
  policy_refs[]
  preconditions[]
  intended_effects[]
  idempotency_key?
  status
  execution_evidence[]
  resulting_event_refs[]
  outcome_refs[]
  failure_reason?
  compensation_action_ref?
```

Rules:
- read access does not imply action authority;
- an agent cannot self-grant missing authority;
- failed actions remain auditable;
- compensating/reversal actions do not erase original execution;
- state changes caused by Actions must be traceable.

---

# 3. Identity / knowledge actions

## `ProposeCanonicalObject`

**Purpose:** propose a new canonical business object from evidence/candidate data.

**Preconditions:** sufficient candidate structure; no unresolved hard identity conflict ignored.

**Effect:** creates proposal only, not accepted canonical identity.

## `AcceptCanonicalObject`

**Purpose:** promote a proposed canonical object.

**Preconditions:** admission/identity checks satisfied; actor has promotion authority.

**Effect:** canonical resource becomes accepted under current contract version.

## `ProposeIdentityMerge`

**Purpose:** propose that two canonical identities represent the same real-world entity.

**Preconditions:** evidence set and merge rationale.

**Effect:** merge proposal only.

## `ExecuteIdentityMerge`

**Purpose:** accept merge after governance.

**Preconditions:** approval/authority; conflict checks; correction path preserved.

**Effect:** canonical identity reconciliation with source mappings/history retained.

## `ExecuteIdentitySplit`

**Purpose:** reverse/correct an incorrect conflation.

**Preconditions:** split rationale and mapping plan.

**Effect:** restores distinct identities and remaps relationships/source mappings without deleting history.

## `PromoteClaim`

**Purpose:** accept a governed claim as canonical interpretation/state input.

**Preconditions:** claim-type-specific authority/evidence rules satisfied.

**Effect:** claim status/state promoted; supporting provenance retained.

## `SupersedeCanonicalInterpretation`

**Purpose:** correct an accepted interpretation.

**Preconditions:** replacement interpretation and correction reason.

**Effect:** prior interpretation remains auditable; new accepted interpretation takes effect under explicit time semantics.

---

# 4. Commercial actions

## `QualifyOpportunity`

**Target:** Opportunity

**Effect:** advances or updates qualification state with evidence/rationale.

## `ApproveBid`

**Target:** Opportunity

**Preconditions:** appropriate decision/approval authority.

**Effect:** authorizes pursuit actions; does not imply proposal submission.

## `DeclineBid`

**Target:** Opportunity

**Effect:** records governed no-bid decision/action and resulting opportunity state.

## `AddPartnerToOpportunity`

**Target:** Opportunity + Organization

**Effect:** creates/proposes scoped partner relationship.

## `ApprovePartner`

**Target:** BusinessRelationship / Organization-in-context

**Preconditions:** relationship context and authority.

**Effect:** partner relationship becomes approved/active for scope.

## `RequestAgreement`

**Target:** Agreement context

**Effect:** initiates agreement workflow; does not imply execution.

## `ApproveProposal`

**Target:** Proposal

**Effect:** marks proposal approved for submission subject to any remaining conditions.

## `SubmitProposal`

**Target:** Proposal

**Preconditions:** approved proposal; submission channel/context valid.

**Effect:** execution attempt produces submission evidence/Event; canonical submitted state requires successful evidence.

## `RecordAward`

**Target:** Opportunity

**Preconditions:** authoritative award evidence or governed equivalent.

**Effect:** records award Event/Outcome and opportunity state.

---

# 5. Agreement / legal actions

## `ApproveAgreement`

**Target:** Agreement

**Effect:** records internal authorization; does not itself mean executed.

## `ExecuteAgreement`

**Target:** Agreement

**Preconditions:** authorized signatory/authority and required parties/process.

**Effect:** produces execution evidence and Agreement state transition where valid.

## `AmendAgreement`

**Target:** Agreement

**Effect:** creates governed amendment/version relationship; prior agreement terms remain historical.

## `TerminateAgreement`

**Target:** Agreement

**Effect:** terminates under effective date/authority; does not delete prior active period.

## `SatisfyObligation`

**Target:** Obligation

**Preconditions:** sufficient fulfillment evidence.

**Effect:** obligation state becomes satisfied under effective time.

## `WaiveObligation`

**Target:** Obligation

**Preconditions:** authority to waive.

**Effect:** obligation state changes to waived with evidence/authority.

---

# 6. Delivery actions

## `CreateProject`

**Target:** new Project

**Preconditions:** valid business/legal origin or governed internal authorization.

**Effect:** creates project identity and initial state.

## `AssignResource`

**Target:** Assignment

**Preconditions:** assignee/context valid; required authority.

**Effect:** creates/activates Assignment; does not alter Person identity.

## `UpdateMilestoneCommitment`

**Target:** Milestone

**Effect:** records revised planned date/commitment without deleting prior plan.

## `SubmitDeliverable`

**Target:** Deliverable

**Effect:** records submission Event and associated Artifact/version evidence.

## `AcceptDeliverable`

**Target:** Deliverable

**Preconditions:** authorized customer/internal acceptance actor.

**Effect:** acceptance state with evidence; may satisfy linked obligation/milestone.

## `RejectDeliverable`

**Target:** Deliverable

**Effect:** rejection/rework state with reason/evidence.

## `CloseProject`

**Target:** Project

**Preconditions:** required completion/closure checks.

**Effect:** Project state closed while preserving full execution history.

---

# 7. Finance actions

## `ApproveBudget`

**Target:** Budget

**Effect:** approved budget version becomes active/authorized.

## `ReviseBudget`

**Target:** Budget

**Effect:** creates revised/superseding version; prior approved budget remains historical.

## `IssueInvoice`

**Target:** Invoice

**Preconditions:** issuer authority and required billing context.

**Effect:** invoice state issued; produces evidence/Event.

## `RecordPayment`

**Target:** Payment

**Effect:** records payment evidence; settlement state may remain pending.

## `ReconcilePayment`

**Target:** Payment + Invoice(s)

**Preconditions:** authoritative settlement/allocation evidence.

**Effect:** applies payment to invoice balances and derives invoice state.

## `ReversePayment`

**Target:** Payment

**Effect:** records reversal without deleting original settlement history.

## `WriteOffInvoice`

**Target:** Invoice

**Preconditions:** appropriate financial authority.

**Effect:** invoice state written_off with reason/approval.

---

# 8. Workforce actions

## `CreatePosition`

**Target:** Position

**Effect:** creates governed Position identity under Organization/Unit.

## `FillPosition`

**Target:** Position + Person

**Effect:** creates temporal Person-position holding relationship.

## `EndPositionHolding`

**Target:** Person-position relationship

**Effect:** closes holding period without retiring Person or Position automatically.

## `RecordCredential`

**Target:** Credential

**Effect:** creates/updates credential state with evidence.

## `RenewCertification`

**Target:** Certification

**Effect:** creates new effective certification term/history.

---

# 9. Technology / asset actions

## `RegisterAsset`

**Target:** Asset

**Effect:** establishes canonical asset identity from governed evidence.

## `AssignAsset`

**Target:** Asset + Person/Unit/Project

**Effect:** creates temporal assignment relationship.

## `AdoptTechnology`

**Target:** Technology/System context

**Preconditions:** decision/approval as required.

**Effect:** establishes governed use/dependency relationship.

## `RetireTechnology`

**Target:** Technology/System

**Effect:** records retirement/deprecation action and effective state without deleting history.

## `ApproveVendorRelationship`

**Target:** BusinessRelationship

**Effect:** activates vendor/provider relationship in specified scope.

---

# 10. Compliance actions

## `RecordRegistration`

**Target:** Registration

**Effect:** establishes registration state from authoritative evidence.

## `RenewRegistration`

**Target:** Registration

**Effect:** records renewed term/status with effective dates.

## `ChangeRegisteredOffice`

**Target:** LegalEntity + Place relationship

**Effect:** closes prior registered-office effective period and starts new one.

## `RecordComplianceException`

**Target:** Registration/Certification/Obligation/Risk

**Effect:** creates governed exception/risk/assessment context; does not silently override compliance truth.

---

# 11. Risk / judgment actions

## `RecordAssessment`

**Target:** Assessment

**Effect:** persists governed judgment with method/actor/provenance.

## `AcceptRisk`

**Target:** Risk

**Preconditions:** actor has risk-acceptance authority.

**Effect:** risk state accepted for explicit scope/time; does not make risk disappear.

## `ApproveMitigation`

**Target:** Risk + Action

**Effect:** authorizes mitigation action.

## `RecordDecision`

**Target:** Decision

**Effect:** records explicit choice and actor/authority; separate from action execution.

## `ApproveAction`

**Target:** Action

**Effect:** authorizes action execution; does not imply success.

---

## 12. Action design rules

1. **Actions are typed.** Avoid generic `doThing`/free-text mutation semantics.
2. **Preconditions are explicit.** Invalid transitions fail predictably.
3. **Authority is explicit.** Actor identity and permission are required.
4. **Effects are bounded.** An Action changes only governed targets/relationships it is allowed to change.
5. **Idempotency where applicable.** Repeated network/request delivery should not duplicate irreversible effects.
6. **Failure is first-class.** Failed actions retain audit/evidence.
7. **Compensation is explicit.** Reversal/mitigation is a new Action, not history deletion.
8. **Evidence of execution matters.** Requested/authorized Action is distinct from successful real-world effect.
9. **Outcome is separate.** Success of Action does not guarantee desired business Outcome.

---

## 13. Codex rule

Build 001 should represent action contracts and references, not execute high-risk real-world actions.

Machine-readable Action schemas must support the common Action contract and typed action vocabulary without implementing application-specific workflows prematurely.
