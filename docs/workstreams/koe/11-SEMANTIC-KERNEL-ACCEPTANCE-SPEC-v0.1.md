# Semantic Kernel Acceptance Specification

**Version:** v0.1  
**Status:** Build gate for Codex Build 001  
**Owner:** Knowledge & Ontology Engineering (KOE-001)

---

## 1. Purpose

Define observable acceptance behavior for the Business Reality semantic kernel before implementation.

The tests below are technology-neutral. A physical implementation passes only if it preserves these semantics.

---

## 2. Preserve truth

### T01 — Source evidence survives canonical correction

Given source evidence E supports interpretation A, and canonical interpretation is later corrected to B, then E remains retrievable with original source identity, timestamps, lineage, and security metadata; A remains historically auditable as superseded.

### T02 — Historical state does not rewrite itself

Given state A was accepted at time T1 and later corrected/replaced by B at T2, `get_state(as_of=T1)` returns the historically accepted state under the defined temporal semantics rather than silently projecting B backward.

### T03 — Duplicate evidence does not create false corroboration

Given the same underlying statement appears via original email, forwarded email, and copied attachment, origin lineage identifies shared origin so the three appearances do not automatically count as three independent sources.

### T04 — Unknown remains representable

If evidence does not establish a value or relationship, the system may return unknown/unresolved rather than inventing a default fact.

---

## 3. Allow correction

### T05 — Identity merge is reversible

Given canonical identities A and B are merged after reconciliation, a later split operation can restore distinct identities while preserving source mappings, relationship history, audit history, and provenance.

### T06 — Contextual alias can be corrected

Given a shorthand resolves to Opportunity A within one context, correction may remap that contextual occurrence without changing unrelated occurrences or creating a global alias automatically.

### T07 — Relationship interpretation can be superseded

Given Organization X is interpreted as a Partner in context C, later evidence may supersede that interpretation while preserving the prior accepted state and effective period.

### T08 — Derived projections are rebuildable

A correction to canonical identity/state can invalidate and rebuild derived search/vector/read projections without mutating original evidence.

---

## 4. Keep the core stable

### T09 — New domain object does not redefine kernel semantics

Adding a new admitted object type must reuse canonical identity, relationship, time, evidence, security, and correction contracts rather than introducing incompatible copies of those mechanisms.

### T10 — New source does not redefine truth

Adding CRM, ERP, ticketing, finance, or other sensors may add source bindings/evidence but cannot bypass candidate/reconciliation/promotion semantics.

### T11 — New contextual role does not require new party identity type

Adding a role such as Distributor, Auditor, Insurer, ReferralSource, or PrimeContractor can be expressed through role/relationship semantics without creating duplicate Organization/Person identity classes unless independent-object admission criteria are met.

---

## 5. Make boundaries explicit

### T12 — Source record is not canonical object

A source Organization/Contact/Opportunity row can be ingested without automatically creating or overwriting the corresponding canonical business object.

### T13 — Role is not identity

The same Organization may simultaneously or historically be Customer, Partner, Vendor, Subcontractor, or other contextual roles without duplication of canonical Organization identity.

### T14 — Event, Decision, Approval, Action, Outcome remain distinct

A workflow may link these resources, but a query can distinguish what happened, what was chosen, what was authorized, what was done, and what resulted.

### T15 — Business Reality does not absorb adjacent models

A Business Intent objective, External Reality condition, or dynamic Capability assessment may be linked to Business Reality but is not silently reclassified as Business Reality merely for storage convenience.

---

## 6. Identity and relationship behavior

### T16 — Ambiguous identity remains unresolved

Given two plausible canonical matches without sufficient evidence, resolution returns multiple candidates/unresolved state rather than forcing a match.

### T17 — Parent, child, and organizational unit remain distinct

A parent Organization, LegalEntity, and OrganizationalUnit can be linked but are not collapsed merely because names or domains overlap.

### T18 — Relationship scope is respected

A Partner role scoped to Opportunity A does not imply a global strategic partnership or a Partner role in Opportunity B.

---

## 7. Time and state behavior

### T19 — Effective time and discovery time are distinguishable

Evidence discovered today may establish a fact effective last month without pretending the system knew that fact last month. The model can represent both.

### T20 — Hypothetical state is isolated

Scenario/planning state cannot become accepted current Business Reality without an explicit governed transition.

---

## 8. Evidence and epistemic behavior

### T21 — Claim may exist without promotion

An email or model output may create/support a Claim while canonical state remains unchanged.

### T22 — Contradictory claims coexist until resolved

The evidence layer can retain incompatible claims and expose authority/time/provenance differences without deleting the losing claim.

### T23 — Inference remains labeled

A reconstructed Decision, relationship, or event inferred from evidence remains distinguishable from an explicit source assertion or governed canonical fact.

---

## 9. Security and authority behavior

### T24 — Security filters every access path

Unauthorized evidence cannot be exposed through direct lookup, search result/snippet, traversal, timeline, decision trace, derived index, or follow-on fetch.

### T25 — Source access does not imply action authority

An actor or agent permitted to read evidence is not automatically permitted to promote state, approve a decision, or execute an Action.

### T26 — Restricted evidence may support a permitted projection only by policy

A canonical state may be visible while supporting evidence remains hidden only where explicit policy permits that abstraction without leaking restricted content.

---

## 10. Cross-domain validation behavior

### T27 — Commercial-to-delivery chain

The model can represent Opportunity -> Solicitation/Proposal/Agreement -> Project without collapsing these distinct lifecycles.

### T28 — Delivery-to-finance chain

The model can represent Project/Deliverable -> Invoice -> Payment with evidence, time, state, and relationship traceability.

### T29 — Workforce assignment chain

A Person can hold a Position and Skill/Credential and participate through an Assignment in a Project/Opportunity without being duplicated as separate person identities.

### T30 — Compliance chain

A LegalEntity can hold a Registration/Certification with jurisdiction/place, status, effective/expiration dates, evidence, obligation/renewal events, and correction history.

### T31 — Technology dependency chain

An Organization/LegalEntity/System can own, operate, use, or depend on Asset/Technology resources while vendor/provider remains a contextual Organization relationship.

---

## 11. Minimum build gate

Codex Build 001 is acceptable only if the machine-readable contracts and fixtures can express every acceptance case above without adding incompatible semantics outside the specification.

A runtime implementation is not required in Build 001. The purpose is to make the semantic contract executable and implementation-ready without selecting a database or application framework prematurely.
