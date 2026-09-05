# Codex Build 001 Brief — Executable Semantic Contract

**Version:** v0.1  
**Status:** Ready for Codex execution  
**Owner:** Knowledge & Ontology Engineering (KOE-001)

---

## 1. Mission

Turn the Business Reality semantic foundation into an executable, technology-neutral contract package without selecting the production database, service framework, or deployment architecture.

Codex implements the semantics. It must not invent them.

---

## 2. Governing documents

Read first, in order:

1. `CONSTITUTION.md`
2. `docs/workstreams/koe/09-SYSTEMS-DESIGN-ENGINEERING-PRINCIPLES-v0.1.md`
3. `docs/workstreams/koe/10-BUILD-SPEC-001-BUSINESS-REALITY-SEMANTIC-FOUNDATION-v0.1.md`
4. `docs/workstreams/koe/09-BUSINESS-REALITY-V1-OBJECT-CATALOG-v0.1.md`
5. `docs/workstreams/koe/11-SEMANTIC-KERNEL-ACCEPTANCE-SPEC-v0.1.md`
6. `docs/workstreams/koe/03-EVIDENCE-DATA-EXTRACTION-CONTRACT-v0.1.md`
7. `docs/workstreams/koe/04-CANONICAL-PROMOTION-MATRIX-v0.1.md`
8. `docs/workstreams/koe/02-QUERY-AND-WORKLOAD-CONTRACT-v0.1.md`

If documents conflict, the newer KOE semantic-foundation documents control within KOE scope and the conflict must be reported in the PR.

---

## 3. Deliverables

Create a machine-readable contract package under a new top-level `contracts/` directory.

Recommended shape:

```text
contracts/
  README.md
  schemas/
    kernel/
      canonical-resource.schema.json
      temporal-state.schema.json
      epistemic-status.schema.json
      provenance.schema.json
      security-context.schema.json
      audit-correction.schema.json
      typed-relationship.schema.json
      event.schema.json
      assessment.schema.json
      decision.schema.json
      approval.schema.json
      action.schema.json
      outcome.schema.json
    business/
      organization.schema.json
      legal-entity.schema.json
      organizational-unit.schema.json
      person.schema.json
      position.schema.json
      place.schema.json
      business-relationship.schema.json
      opportunity.schema.json
      solicitation.schema.json
      offering.schema.json
      proposal.schema.json
      agreement.schema.json
      obligation.schema.json
      contract-vehicle.schema.json
      project.schema.json
      milestone.schema.json
      deliverable.schema.json
      budget.schema.json
      invoice.schema.json
      payment.schema.json
      assignment.schema.json
      capability.schema.json
      skill.schema.json
      credential.schema.json
      certification.schema.json
      asset.schema.json
      system.schema.json
      technology.schema.json
      registration.schema.json
      artifact.schema.json
      claim.schema.json
      risk.schema.json
  api/
    business-reality.openapi.yaml
  fixtures/
    identity/
    commercial/
    delivery/
    workforce/
    compliance/
    technology/
    finance/
  tests/
    acceptance-manifest.yaml
```

Exact filenames may vary for good reason, but the semantic coverage may not.

Use JSON Schema Draft 2020-12 and OpenAPI 3.1 unless an existing repository convention supersedes them. These are contract formats, not production runtime choices.

---

## 4. Required kernel contracts

The package must make these concepts explicit and reusable rather than redefined independently by every business schema:

- canonical ID and object type/version;
- aliases/source mappings;
- effective/source/recorded/discovered time;
- epistemic status;
- evidence/provenance reference;
- security classification/context hooks;
- audit metadata;
- supersession/correction reference;
- typed relationship identity, participants, roles, scope, time, evidence, state;
- Event / Assessment / Decision / Approval / Action / Outcome distinctions.

Do not encode physical database keys, indexes, graph labels, SQL constraints, or vendor-specific storage behavior into the semantic contract.

---

## 5. Business schemas

Represent all 38 candidate V1 business objects at contract level.

The schemas may be intentionally thin where admission questions remain open. In that case:

- preserve common kernel behavior;
- mark unresolved domain-specific fields clearly;
- do not invent lifecycle/property semantics merely to make the schema look complete.

A thin correct schema is preferable to a detailed invented schema.

---

## 6. API contract

Define technology-neutral request/response shapes for at least:

```text
GET object by id/as_of/security context
resolve identity
get relationships/neighbors
get current/historical state
get timeline
get evidence
get decision trace
find contradictions
find unresolved candidates
search

propose object
propose relationship
propose claim
propose event
propose merge
propose split
promote candidate
reject candidate
correct canonical interpretation
```

Ambiguity, unknown, unresolved, forbidden, conflict, superseded, and not-found outcomes must be explicit rather than collapsed into generic null/500 behavior.

---

## 7. Fixture requirements

Create synthetic fixtures spanning all six validation families:

1. commercial pursuit;
2. delivery/project execution;
3. workforce/resource lifecycle;
4. legal/compliance lifecycle;
5. vendor/technology lifecycle;
6. financial execution.

Fixtures must include positive cases and difficult cases:

- aliases;
- same-name distinct identities;
- contextual roles;
- ambiguous identity;
- contradictory claims;
- duplicate evidence origin;
- historical correction;
- merge/split;
- restricted evidence;
- Event vs Decision vs Approval vs Action vs Outcome;
- cross-domain linkage.

Do not make SFO/CRI the only or dominant fixture.

---

## 8. Acceptance manifest

Map every T01–T31 requirement from `11-SEMANTIC-KERNEL-ACCEPTANCE-SPEC-v0.1.md` to one or more fixture/assertion definitions.

The first Codex build is complete when there is no acceptance requirement that lacks a representable contract and fixture assertion.

If full executable validation would require choosing a runtime, stop at a deterministic machine-readable assertion manifest and document what a future test harness must verify.

---

## 9. Prohibited implementation choices

Build 001 must not:

- choose the production database;
- choose graph vs relational primary persistence;
- choose a vector database;
- choose Azure service topology;
- build Outlook/SharePoint connectors;
- build an agent framework;
- let source schemas define canonical types;
- create Customer/Partner/Vendor as duplicate Organization identity classes;
- create one universal confidence threshold;
- make LLM/model output canonical by default;
- collapse Event, Decision, Approval, Action, and Outcome;
- make corrections destructive;
- encode SFO/CRI-specific classes.

---

## 10. Architecture escalation rule

If Codex encounters a question that changes business meaning, identity semantics, evidence authority, time semantics, security/authority, correction behavior, or object boundaries:

**do not choose silently.**

Record it under:

```text
contracts/OPEN-SEMANTIC-QUESTIONS.md
```

with:

- question;
- affected contract;
- options;
- implementation impact;
- why the existing spec does not resolve it.

Continue all non-blocked work.

---

## 11. Completion condition

Build 001 is complete when:

- the semantic kernel is machine-readable;
- all 38 candidate object types can compose the kernel contracts;
- the logical API surface is machine-readable;
- all six domain families have representative fixtures;
- T01–T31 are mapped to assertions;
- no production technology choice has been smuggled into semantic contracts;
- semantic ambiguities are surfaced explicitly.

The next build can then implement a reference/runtime Business Reality service against these contracts after Platform Engineering establishes the appropriate implementation architecture.
