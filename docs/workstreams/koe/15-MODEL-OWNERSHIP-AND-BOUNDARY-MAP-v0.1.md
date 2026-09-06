# Model Ownership and Boundary Map

**Version:** v0.1  
**Status:** KOE architecture baseline  
**Owner:** Knowledge & Ontology Engineering (KOE-001)

---

## 1. Rule

Every canonical concept has one primary semantic owner.

Other models may reference, project, assess, or derive from that concept, but they must not create competing canonical meanings.

The active model architecture is:

```text
Business Intent
Business Reality
External Reality
Capability
        -> Executive Judgment
        -> Decision / Approval
        -> Governed Action
        -> Outcome / Learning
```

---

## 2. Ownership categories

### Business Reality owned

Represents what operationally exists, happened, or is currently/historically true about GenSigma and its direct business context.

### Business Intent owned

Represents what GenSigma seeks, prioritizes, values, targets, or intends to offer/do.

### Capability owned

Represents decision-relevant ability to execute now or under specified conditions.

### Executive Judgment owned

Represents assessments, recommendations, choices, approvals, and judgment methods.

### Shared semantic identity

Some concepts have stable identity usable across models. One model still owns the authoritative object semantics; others link to it.

---

# 3. V1 object ownership map

| Object | Primary owner | Cross-model use |
|---|---|---|
| Organization | Business Reality | referenced by all models |
| LegalEntity | Business Reality | capability, intent, compliance references |
| OrganizationalUnit | Business Reality | intent/capability ownership and scope |
| Person | Business Reality | capability/judgment actor reference |
| Position | Business Reality | authority/capability reference |
| Place | Business Reality | external/compliance/delivery reference |
| BusinessRelationship | Business Reality | capability and judgment context |
| Opportunity | Business Reality | intent alignment; judgment input |
| Solicitation | Business Reality | external source context; judgment input |
| Offering | Business Intent | instantiated/referenced by Business Reality Opportunity/Proposal/Project |
| Proposal | Business Reality | judgment/approval/action context |
| Agreement | Business Reality | capability constraints and action authority |
| Obligation | Business Reality | capability constraint, risk/judgment input |
| ContractVehicle | Business Reality | intent targeting and opportunity eligibility |
| Project | Business Reality | intent/outcome/capability reference |
| Milestone | Business Reality | outcome/risk/judgment reference |
| Deliverable | Business Reality | obligation/outcome reference |
| Budget | Business Reality | intent constraint and judgment input |
| Invoice | Business Reality | outcome/finance state |
| Payment | Business Reality | outcome/finance state |
| Assignment | Business Reality | capability/resource evidence |
| Capability | Capability | Business Reality links to possessed/evidenced capability identity; dynamic feasibility owned by Capability model |
| Skill | Business Reality | capability evidence/requirement |
| Credential | Business Reality | capability/compliance evidence |
| Certification | Business Reality | capability/compliance/eligibility evidence |
| Asset | Business Reality | capability/technology dependency |
| System | Business Reality | capability/technology dependency |
| Technology | Business Reality | external technology interpretation may exist separately |
| Registration | Business Reality | compliance state |
| Artifact | Business Reality | evidence across all models |
| Event | Business Reality | signal/input to judgment/outcome learning |
| Claim | Business Reality knowledge layer | evidence input to all models |
| Assessment | Executive Judgment | may evaluate Reality, Capability, Intent, External Reality |
| Risk | Executive Judgment | risk identity/state linked to Reality; risk appetite remains Intent |
| Decision | Executive Judgment | recorded into Business Reality trace after occurrence |
| Approval | Executive Judgment / Governed Action boundary | authorization trace persisted in Business Reality |
| Action | Governed Action | action occurrence/state effect persisted in Business Reality |
| Outcome | Outcome/Learning | observed outcome persisted/referenced in Business Reality |

---

## 4. Important boundary decisions

### 4.1 Offering belongs primarily to Business Intent

An `Offering` describes what GenSigma chooses to package and take to market. That is normative/strategic by default.

Business Reality does not create a second Offering object. It references the governed Offering identity from Opportunity, Proposal, Agreement, Project, and actual delivery evidence.

An unapproved or ad-hoc customer-specific package may begin as a proposal/candidate and later be promoted into Business Intent if the company adopts it as an offering.

### 4.2 Capability belongs primarily to Capability

Business Reality stores the people, skills, credentials, systems, partner relationships, assignments, and evidence that capability evaluation depends on.

The Capability model owns statements such as:

```text
GenSigma can deliver X
for customer Y
within time T
with confidence/constraints Z
```

That is not a static Business Reality property.

### 4.3 Assessment and Risk belong to Executive Judgment

Reality contains facts and evidence. `Assessment` interprets them.

`Risk` is a governed judgment about uncertainty/exposure, even when linked to concrete Reality objects.

Business Reality stores the resulting trace and historical state; it does not own the judgment method.

### 4.4 Decision and Approval belong to Executive Judgment

A Decision is the result of judgment; Approval is authorization.

Once made, both become historical operational facts and are queryable through Business Reality.

This does not transfer ownership of their semantics to the Business Reality storage layer.

### 4.5 Action belongs to Governed Action

The action definition, preconditions, permissions, policy, effects, idempotency, and execution contract belong to the Governed Action/Kinetic layer.

The fact that an action was proposed, authorized, attempted, succeeded, failed, or compensated becomes Business Reality history.

### 4.6 Outcome belongs to Outcome/Learning

Outcome identity and measurement semantics belong to the learning/outcome layer.

Observed outcomes are persisted/linked into Business Reality so they can be traversed historically.

---

## 5. Shared identity without shared ownership

Cross-model references use canonical IDs rather than copied semantic objects.

Example:

```text
Business Intent Offering: AI Workflow Automation
        |
        | referenced_by
        v
Business Reality Opportunity
        |
        | requires
        v
Capability evaluation
        |
        | informs
        v
Executive Judgment Decision
        |
        | authorizes
        v
Governed Action
        |
        | produces
        v
Outcome
```

No layer is allowed to fork its own incompatible definition of `Organization`, `Offering`, `Capability`, `Decision`, or other shared referent.

---

## 6. API implication

Model APIs should expose references across boundaries using stable canonical identifiers plus explicit projection contracts.

Do not serialize another model's entire internal object and then treat the copy as authoritative.

A cross-model reference should at minimum contain:

```text
canonical_id
object_type
model_owner
contract_version
optional permitted projection
```

---

## 7. Correction implication

When an owning model corrects canonical interpretation:

1. the correction is versioned/audited;
2. dependent models are notified or their projections invalidated;
3. historical references remain resolvable;
4. derived conclusions may be recomputed;
5. dependent models do not rewrite the owning model's truth independently.

---

## 8. Open ownership questions

These remain explicit rather than hidden:

- whether `Risk` should later split into a durable Business Reality risk record plus Executive Judgment risk assessments;
- whether `Outcome` needs separate operational-observation and strategic-learning resources;
- whether `Offering` needs a Business Reality `OfferingInstance`/configuration concept for customer-specific delivery;
- whether `Claim` ultimately belongs to a cross-cutting Knowledge/Evidence subsystem rather than Business Reality.

None of these questions blocks the current semantic kernel because ownership references and versioned contracts preserve the boundary.
