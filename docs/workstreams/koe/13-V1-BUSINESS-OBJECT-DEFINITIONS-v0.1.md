# Business Reality V1 — Object Definitions

**Version:** v0.1  
**Status:** KOE semantic baseline  
**Owner:** Knowledge & Ontology Engineering (KOE-001)  
**Scope:** Enterprise-wide candidate definitions for the 38 V1 Business Reality objects

---

## 1. Definition standard

Each object is defined by five things:

1. **Meaning** — what the object represents.
2. **Identity** — what makes one instance the same or different from another.
3. **Lifecycle** — the material states or transitions that matter.
4. **Core links** — the relationships that give the object business meaning.
5. **Truth/correction rule** — what evidence is required and how mistakes are corrected.

The four governing truths apply to every object:

- preserve truth;
- allow correction;
- keep the core stable;
- make boundaries explicit.

---

# A. Enterprise identity and structure

## 1. Organization

**Meaning:** A durable organizational identity that can participate in business relationships and operations.

**Identity:** Stable canonical identity independent of name, alias, domain, source-system record, or current role.

**Lifecycle:** active, inactive, dissolved/ceased, unknown; historical names and aliases remain temporal.

**Core links:** LegalEntity, OrganizationalUnit, Person, BusinessRelationship, Opportunity, Agreement, Project, Capability, System, Certification.

**Truth/correction:** source records may propose identity; merge/split is governed and reversible. Customer/Partner/Vendor are roles, not Organization identities.

## 2. LegalEntity

**Meaning:** A legally constituted entity with independent legal identity, rights, obligations, registrations, and contracting capacity.

**Identity:** legal jurisdiction + legal name/identifier evidence, while preserving stable internal canonical ID through name changes.

**Lifecycle:** formation, active, merged/consolidated, dissolved, inactive.

**Core links:** Organization, Agreement, Registration, Place, Certification, BusinessRelationship, Asset, System.

**Truth/correction:** authoritative legal evidence dominates informal source claims for legal identity/status. Incorrect entity association is corrected without deleting historical evidence.

## 3. OrganizationalUnit

**Meaning:** A durable internal or external organizational subdivision that owns work, people, capability, budget, or authority without necessarily being a legal entity.

**Identity:** scoped to parent Organization/OrganizationalUnit and governed name/function over time.

**Lifecycle:** planned, active, reorganized, retired.

**Core links:** Organization, Position, Person, Project, Budget, Capability, Opportunity, Place.

**Truth/correction:** reorgs create temporal structural changes, not destructive replacement of prior hierarchy.

## 4. Person

**Meaning:** A canonical human identity.

**Identity:** one human across employers, roles, aliases, email addresses, and source records.

**Lifecycle:** active/known, inactive/historical, deceased where materially relevant; employment/contract status does not define Person lifecycle.

**Core links:** Position, Assignment, BusinessRelationship, Skill, Credential, Certification, Decision, Approval, Action.

**Truth/correction:** employer change or role change never creates a new Person. Identity merge/split remains reversible.

## 5. Position

**Meaning:** A durable organizational role/seat that may exist independently of its current holder.

**Identity:** scoped to OrganizationalUnit/Organization, function, and effective period; not the same as a Person.

**Lifecycle:** planned, open, filled, suspended, retired.

**Core links:** OrganizationalUnit, Person, Capability, Skill, Approval/authority references.

**Truth/correction:** title strings alone do not create canonical Position identity. Holder changes are relationship changes.

## 6. Place

**Meaning:** A physical or jurisdictional location used for operations, registration, delivery, ownership, or legal context.

**Identity:** governed physical/jurisdiction identity; addresses may change without implying a different place where semantics permit.

**Lifecycle:** active/relevant, historical, superseded representation.

**Core links:** LegalEntity, OrganizationalUnit, Project, Asset, Registration.

**Truth/correction:** address normalization never destroys source-address evidence.

---

# B. Relationships and commercial / revenue

## 7. BusinessRelationship

**Meaning:** A material relationship among one or more parties with scoped roles, state, evidence, and effective time.

**Identity:** determined by participants + relationship family/type + scope + effective period when independently significant.

**Lifecycle:** proposed, active, suspended, terminated/expired, historical; subtypes may refine states.

**Core links:** Organization, Person, Opportunity, Agreement, Project, Artifact.

**Truth/correction:** relationship role is contextual and temporal. A partner relationship in one Opportunity does not imply global partner status.

## 8. Opportunity

**Meaning:** A potential business/revenue outcome GenSigma may pursue or evaluate.

**Identity:** canonical pursuit identity independent of CRM row, shorthand, solicitation title, or proposal file.

**Lifecycle:** discovered, qualifying, pursuing, submitted, awarded, lost, cancelled, dormant/closed.

**Core links:** Organization/OrganizationalUnit, Solicitation, Offering, Proposal, BusinessRelationship, Agreement, Capability, Decision, Action, Outcome.

**Truth/correction:** shorthand aliases are contextual. Opportunity state requires evidence and effective time.

## 9. Solicitation

**Meaning:** A customer/procurement authority-issued request or procurement instrument inviting or governing responses.

**Identity:** issuing authority + solicitation identifier/version where available.

**Lifecycle:** draft/anticipated, issued, amended, closed, cancelled, awarded/complete.

**Core links:** Organization, Opportunity, Artifact, ContractVehicle, Agreement, Event.

**Truth/correction:** solicitation amendments are versioned/history-preserving; Solicitation is distinct from Opportunity.

## 10. Offering

**Meaning:** A sellable or deliverable business offering/capability package used in commercial context.

**Identity:** stable offering identity across opportunities and artifacts, with version/effective period when materially changed.

**Lifecycle:** proposed, active, revised, retired.

**Core links:** Opportunity, Capability, Project, Artifact, Organization/OrganizationalUnit.

**Truth/correction:** strategic positioning belongs to Business Intent; Business Reality holds the operational offering identity/state actually used.

## 11. Proposal

**Meaning:** A governed commercial response/submission with its own lifecycle, approvals, and one or more artifacts/versions.

**Identity:** proposal business identity independent of a single file/version.

**Lifecycle:** drafting, review, approved, submitted, revised/resubmitted, withdrawn, accepted/rejected/expired.

**Core links:** Opportunity, Solicitation, Offering, Artifact, Approval, Agreement, Outcome.

**Truth/correction:** file replacement does not destroy Proposal history. Submission state requires evidence.

## 12. Agreement

**Meaning:** A legal or operational instrument establishing rights, permissions, responsibilities, or commercial terms.

**Identity:** agreement identity independent of one scanned/signed file; governed by parties, instrument, and executed/version evidence.

**Lifecycle:** draft, negotiating, approved, executed/active, amended, expired, terminated, superseded.

**Core links:** Organization/LegalEntity/Person, Artifact, Obligation, Project, Opportunity, BusinessRelationship.

**Truth/correction:** executed status requires sufficiently authoritative evidence. Amendments preserve prior versions/effective periods.

## 13. Obligation

**Meaning:** A material duty, commitment, condition, deliverable, payment, deadline, or requirement arising from an Agreement, Solicitation, policy, or other authoritative context.

**Identity:** obligation source + subject + responsible party + scope; independently tracked when lifecycle matters.

**Lifecycle:** proposed, active/open, satisfied, waived, breached, expired, superseded.

**Core links:** Agreement, Solicitation, Project, Deliverable, Invoice, Person/Organization, Risk.

**Truth/correction:** derivation from source text must retain provenance; interpretation may be corrected without changing source text.

## 14. ContractVehicle

**Meaning:** A procurement/contracting vehicle under which opportunities, solicitations, agreements, or orders may be issued.

**Identity:** issuing body + program/vehicle identifier + effective term.

**Lifecycle:** planned, active, suspended, expired, renewed/superseded.

**Core links:** Organization, Solicitation, Opportunity, Agreement, Certification/qualification references.

**Truth/correction:** eligibility and active status are temporal, evidence-backed facts.

---

# C. Delivery and financial execution

## 15. Project

**Meaning:** A governed delivery/execution context established to perform work and produce outcomes.

**Identity:** independent project identity, not merely a folder, opportunity, agreement, or accounting code.

**Lifecycle:** planned, active, paused, completed, cancelled, closed.

**Core links:** Agreement, Opportunity, Organization, Assignment, Milestone, Deliverable, Budget, Invoice, Outcome, Risk.

**Truth/correction:** project start/end/state changes preserve history and source evidence.

## 16. Milestone

**Meaning:** A material checkpoint or target in a Project or other execution context.

**Identity:** scoped milestone identity within parent context; duplicates distinguished by scope/effective period.

**Lifecycle:** planned, due, achieved, missed, cancelled, superseded.

**Core links:** Project, Deliverable, Obligation, Event, Risk.

**Truth/correction:** planned date and achieved date are distinct facts; later schedule revisions do not erase earlier commitments.

## 17. Deliverable

**Meaning:** A material output that must be produced, reviewed, accepted, or transferred.

**Identity:** deliverable identity tied to Project/Agreement/Obligation scope, not one file.

**Lifecycle:** planned, in-progress, submitted, accepted, rejected/rework, complete, cancelled.

**Core links:** Project, Milestone, Obligation, Artifact, Approval/acceptance, Invoice, Outcome.

**Truth/correction:** acceptance requires evidence; artifact versions do not redefine deliverable identity.

## 18. Budget

**Meaning:** An approved or proposed financial allocation/control envelope for a defined scope and period.

**Identity:** owner + scope + period/version.

**Lifecycle:** proposed, approved, active, revised, frozen, closed/superseded.

**Core links:** OrganizationalUnit, Project, Opportunity, Agreement, Cost/financial derived measures.

**Truth/correction:** budget revisions preserve prior approved versions. Actual spend is not the Budget object itself.

## 19. Invoice

**Meaning:** A formal receivable/payable request for payment.

**Identity:** issuer + invoice identifier + legal/financial context.

**Lifecycle:** draft, issued, partially paid, paid, disputed, voided, written-off.

**Core links:** Agreement, Project, Deliverable, Organization/LegalEntity, Payment, Outcome.

**Truth/correction:** void/reissue and corrections preserve invoice lineage; source accounting record does not by itself define all business semantics.

## 20. Payment

**Meaning:** A monetary settlement or transfer applied to one or more financial obligations/invoices.

**Identity:** payment transaction identity based on authoritative financial evidence.

**Lifecycle:** initiated, pending, settled, reversed, failed, refunded/adjusted.

**Core links:** Invoice, Agreement, Organization/LegalEntity, Project, Outcome.

**Truth/correction:** reversals/chargebacks are new state/evidence, not deletion of original payment.

---

# D. Workforce and executable capability

## 21. Assignment

**Meaning:** A time-bounded allocation of a Person or organizational resource to a business context with role/responsibility.

**Identity:** assignee + scope + role + effective period when independently material.

**Lifecycle:** proposed, planned, active, paused, completed, cancelled.

**Core links:** Person, OrganizationalUnit, Position, Project, Opportunity, Skill, Capability.

**Truth/correction:** assignment is distinct from employment/relationship. Corrections preserve prior allocation history.

## 22. Capability

**Meaning:** A durable ability that an Organization, OrganizationalUnit, Person, or ecosystem relationship can possess, develop, source, or require.

**Identity:** stable semantic capability identity independent of staffing at a moment in time.

**Lifecycle:** proposed/recognized, developing, available, constrained, retired where useful.

**Core links:** Organization, OrganizationalUnit, Person, Skill, Credential, Technology, System, Opportunity, Project, Offering.

**Truth/correction:** dynamic feasibility/availability belongs to Capability evaluation; canonical Capability identity remains stable.

## 23. Skill

**Meaning:** A human competency or expertise that may support capability and assignments.

**Identity:** normalized skill concept independent of source vocabulary and person.

**Lifecycle:** active taxonomy concept, deprecated/superseded; proficiency is temporal evidence/assessment.

**Core links:** Person, Position, Assignment, Capability, Credential.

**Truth/correction:** synonyms may reconcile; proficiency claims preserve evidence and time.

## 24. Credential

**Meaning:** A formal or informal qualification/attestation held by a Person or Organization that can be verified and may expire.

**Identity:** issuing body + credential type + holder + identifier where applicable.

**Lifecycle:** pending, active, expired, suspended, revoked, superseded.

**Core links:** Person/Organization, Capability, Assignment, Artifact.

**Truth/correction:** credential status should rely on authoritative evidence where material.

## 25. Certification

**Meaning:** A governed certification status held by an Organization, LegalEntity, Person, product/system, or program participant.

**Identity:** certifying authority + certification program/type + holder.

**Lifecycle:** applied, pending, active, suspended, expired, revoked, renewed.

**Core links:** Organization, LegalEntity, Person, ContractVehicle, Capability, Artifact, Obligation.

**Truth/correction:** renewal creates temporal continuity/history rather than overwriting prior term.

---

# E. Systems and operational resources

## 26. Asset

**Meaning:** A material owned, leased, managed, or controlled resource with independent operational or financial significance.

**Identity:** stable asset identity independent of serial number/source system when necessary.

**Lifecycle:** planned, acquired, active, assigned, maintenance, retired/disposed.

**Core links:** Organization/LegalEntity, Person, Project, System, Technology, Place, Agreement.

**Truth/correction:** asset ownership/assignment changes are temporal; source inventory records are sensors.

## 27. System

**Meaning:** An operational information/technology system that performs business functions or holds material dependencies/data.

**Identity:** canonical system identity independent of vendor product, instance name, CMDB row, or environment.

**Lifecycle:** planned, development, active, degraded, deprecated, retired.

**Core links:** Organization, OrganizationalUnit, Technology, Asset, Capability, Risk, Agreement.

**Truth/correction:** environments/instances may be modeled as relationships/properties unless independent lifecycle requires objects.

## 28. Technology

**Meaning:** A reusable technology/product/platform/component used by Systems, Assets, Offerings, or Capabilities.

**Identity:** normalized technology/product identity and material version where needed.

**Lifecycle:** current, deprecated, end-of-support, retired/superseded.

**Core links:** System, Asset, Capability, Offering, Agreement, Risk, Organization/vendor relationship.

**Truth/correction:** technology naming/version normalization preserves original source references.

---

# F. Legal / compliance state

## 29. Registration

**Meaning:** A governed registration, qualification, license-like standing, or official filing state with a jurisdiction/authority.

**Identity:** holder + authority/jurisdiction + registration type + identifier where available.

**Lifecycle:** pending, active, delinquent, suspended, expired, withdrawn, renewed/superseded.

**Core links:** LegalEntity/Organization/Person, Place/jurisdiction, Artifact, Obligation, Certification.

**Truth/correction:** status/renewal must be temporal and evidence-backed; registered office is a relationship, not this object.

---

# G. Knowledge, activity, judgment, and control

## 30. Artifact

**Meaning:** A meaningful business evidence/work-product identity that may have versions and multiple source appearances.

**Identity:** canonical artifact/document identity distinct from each source appearance or binary copy.

**Lifecycle:** created, revised/versioned, finalized, superseded, archived; source-specific states may vary.

**Core links:** Claim, Agreement, Proposal, Solicitation, Deliverable, Event, Decision.

**Truth/correction:** immutable source appearances remain traceable; deduplication never deletes provenance or falsely creates corroboration.

## 31. Event

**Meaning:** A material occurrence that happened at a point/interval in business time.

**Identity:** occurrence identity based on event type + context + participants + time/evidence, not merely log entry.

**Lifecycle:** occurred; may later be corrected/reclassified/superseded as interpretation changes.

**Core links:** any business object, Claim, Artifact, Decision, Action, Outcome.

**Truth/correction:** events are distinct from decisions/actions; uncertain reconstruction remains labeled inferred.

## 32. Claim

**Meaning:** A proposition asserted about one or more business subjects, with provenance, time, authority, and epistemic status.

**Identity:** proposition identity sufficient to compare support, contradiction, supersession, and time scope.

**Lifecycle:** proposed/observed, supported, contradicted, accepted/promoted, superseded, rejected/unresolved.

**Core links:** subjects, Artifact/evidence, Assessment, canonical state, Claim contradictions.

**Truth/correction:** claim text/assertion history is preserved; acceptance may change without rewriting evidence.

## 33. Assessment

**Meaning:** A governed judgment/evaluation about a situation, subject, risk, capability, option, or state.

**Identity:** assessment question/scope + assessor/model + time/version.

**Lifecycle:** draft/proposed, issued, reviewed, superseded/withdrawn.

**Core links:** Claim, Risk, Opportunity, Project, Capability, Decision, Artifact.

**Truth/correction:** assessment is not canonical fact; model/human basis and version remain visible.

## 34. Risk

**Meaning:** A material uncertain condition with potential adverse or beneficial effect on business objectives or operations.

**Identity:** risk statement + scope + owner/context when independently managed.

**Lifecycle:** identified, assessed, accepted, mitigated, monitored, realized, closed.

**Core links:** Opportunity, Project, Agreement, System, Technology, Registration, Assessment, Decision, Action, Outcome.

**Truth/correction:** risk level is time-bound assessment, not immutable fact.

## 35. Decision

**Meaning:** A material choice among alternatives or a commitment to a course of action.

**Identity:** decision question/scope + decision-maker/authority + decision occurrence.

**Lifecycle:** proposed/pending, made, superseded/reversed, expired where applicable.

**Core links:** Assessment, Risk, alternatives/reference, Approval, Action, Outcome, Artifact.

**Truth/correction:** explicit vs reconstructed decisions remain distinguishable; reversal does not erase original decision.

## 36. Approval

**Meaning:** An authorization by a recognized authority permitting a Decision, Action, Agreement, Proposal, financial commitment, or state transition.

**Identity:** approver/authority + approved subject + scope + occurrence/time.

**Lifecycle:** requested, approved, rejected, revoked, expired/superseded.

**Core links:** Person/Position/authority, Decision, Action, Proposal, Agreement, Budget, Artifact.

**Truth/correction:** approval and decision are distinct. Delegated authority must be traceable where material.

## 37. Action

**Meaning:** A governed act performed by a human, agent, or system that changes or attempts to change business state.

**Identity:** action instance with actor, action type, target/scope, request/command identity, and time.

**Lifecycle:** proposed, authorized, queued/in-progress, succeeded, failed, cancelled, compensated/reversed.

**Core links:** actor, Decision, Approval, target business objects, Event, Outcome, Artifact/audit evidence.

**Truth/correction:** material actions are idempotent/auditable where feasible; compensating action preserves original history.

## 38. Outcome

**Meaning:** A material result attributable or linked to one or more actions, decisions, projects, opportunities, or external events.

**Identity:** outcome observation/measurement scoped to subject + measure/result + time period when independently material.

**Lifecycle:** observed/provisional, confirmed, revised/superseded.

**Core links:** Action, Decision, Project, Opportunity, Deliverable, Payment, Assessment, Business Intent outcome reference.

**Truth/correction:** attribution strength must remain explicit. Outcome revision does not rewrite underlying events/actions.

---

## 2. Cross-object identity rules

1. Canonical identity is independent of source-system identity.
2. Roles do not create duplicate Organization or Person identities.
3. Business objects with file representations (`Proposal`, `Agreement`, `Deliverable`, etc.) are not identical to their `Artifact` representations.
4. Temporal change normally changes state/relationships, not canonical identity.
5. Merge/split/correction must preserve source mappings and historical interpretation.
6. The system may remain unresolved rather than force false identity.

---

## 3. Admission status

All 38 definitions are **candidate semantic contracts**. The following remain under explicit admission pressure test:

- `Position`;
- `Offering`;
- `Obligation`;
- `Budget`;
- `Milestone`;
- `Claim` as counted business object versus governed knowledge resource;
- `Approval` as independent object versus specialized authorization resource.

Codex may represent these thinly but must not collapse them until KOE resolves the admission question.
