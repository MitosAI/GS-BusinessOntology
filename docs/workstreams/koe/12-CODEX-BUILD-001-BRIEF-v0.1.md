# Codex Build 001 Brief — Executable Semantic Contract

**Version:** v0.2  
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
5. `docs/workstreams/koe/13-V1-BUSINESS-OBJECT-DEFINITIONS-v0.1.md`
6. `docs/workstreams/koe/14-TYPED-RELATIONSHIP-AND-ROLE-CATALOG-v0.1.md`
7. `docs/workstreams/koe/15-MODEL-OWNERSHIP-AND-BOUNDARY-MAP-v0.1.md`
8. `docs/workstreams/koe/16-CORE-RESOURCE-ENVELOPE-AND-VERSIONING-v0.1.md`
9. `docs/workstreams/koe/11-SEMANTIC-KERNEL-ACCEPTANCE-SPEC-v0.1.md`
10. `docs/workstreams/koe/03-EVIDENCE-DATA-EXTRACTION-CONTRACT-v0.1.md`
11. `docs/workstreams/koe/04-CANONICAL-PROMOTION-MATRIX-v0.1.md`
12. `docs/workstreams/koe/02-QUERY-AND-WORKLOAD-CONTRACT-v0.1.md`

If documents conflict, the newer KOE semantic-foundation documents control within KOE scope and the conflict must be reported in the PR.

---

## 3. Deliverables

Create a machine-readable contract package under a new top-level `contracts/` directory.

Recommended shape:

```text
contracts/
  README.md
  OPEN-SEMANTIC-QUESTIONS.md
  schemas/
    kernel/
      canonical-resource.schema.json
      canonical-ref.schema.json
      effective-time.schema.json
      epistemic-status.schema.json
      provenance.schema.json
      source-mapping.schema.json
      security-context.schema.json
      audit-correction.schema.json
      alias.schema.json
      typed-relationship.schema.json
      event.schema.json
      assessment.schema.json
      decision.schema.json
      approval.schema.json
      action.schema.json
      outcome.schema.json
    business/
      <one schema per V1 candidate object>
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

Use JSON Schema Draft 2020-12 and OpenAPI 3.1 unless an existing repository convention supersedes them. These are contract formats, not production runtime choices.

---

## 4. Required kernel contracts

The package must make these concepts explicit and reusable rather than redefined independently by every business schema:

- canonical ID and semantic type/version;
- cross-model canonical references and model ownership;
- aliases/source mappings;
- effective/source/recorded/discovered time;
- epistemic status;
- evidence/provenance reference;
- security classification/context hooks;
- audit metadata;
- supersession/correction lineage;
- typed relationship identity, participants, contextual roles, scope, time, evidence, state;
- Event / Assessment / Decision / Approval / Action / Outcome distinctions.

Do not encode physical database keys, indexes, graph labels, SQL constraints, or vendor-specific storage behavior into the semantic contract.

---

## 5. Business schemas

Represent all current V1 candidate object types at contract level using the definitions in `13-V1-BUSINESS-OBJECT-DEFINITIONS-v0.1.md`.

Every schema must compose the common kernel envelope. Do not duplicate or redefine canonical identity, time, provenance, security, correction, alias, or source-mapping semantics inside domain schemas.

Schemas may be intentionally thin where admission questions remain open. In that case:

- preserve common kernel behavior;
- mark unresolved domain-specific fields clearly;
- do not invent lifecycle/property semantics merely to make the schema look complete.

A thin correct schema is preferable to a detailed invented schema.

---

## 6. Relationship contracts

Implement the semantic coverage in `14-TYPED-RELATIONSHIP-AND-ROLE-CATALOG-v0.1.md`.

A typed relationship must support:

- stable relationship identity where independently significant;
- participant references;
- contextual participant roles;
- relationship type/family;
- scope;
- lifecycle state;
- effective time;
- provenance;
- epistemic status;
- security;
- correction/supersession.

Customer, Partner, Vendor, Employee, Contractor, Candidate, Stakeholder, Approver, and similar roles must not become duplicate Person/Organization identity classes.

---

## 7. API contract

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

Ambiguity, unknown, unresolved, forbidden, conflict, superseded, contract-version mismatch, and not-found outcomes must be explicit rather than collapsed into generic null/500 behavior.

---

## 8. Fixture requirements

Create synthetic fixtures spanning all six validation families:

1. commercial pursuit;
2. delivery/project execution;
3. workforce/resource lifecycle;
4. legal/compliance lifecycle;
5. vendor/technology lifecycle;
6. financial execution.

Fixtures must include positive and difficult cases:

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
- cross-domain linkage;
- cross-model canonical reference.

No one customer or opportunity may dominate fixture design.

---

## 9. Acceptance manifest

Map every T01–T31 requirement from `11-SEMANTIC-KERNEL-ACCEPTANCE-SPEC-v0.1.md` to one or more fixture/assertion definitions.

The first Codex build is complete when there is no acceptance requirement that lacks a representable contract and fixture assertion.

If full executable validation would require choosing a runtime, stop at a deterministic machine-readable assertion manifest and document what a future test harness must verify.

---

## 10. Prohibited implementation choices

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
- create customer-specific ontology classes;
- fork the semantics of a concept owned by another model.

---

## 11. Architecture escalation rule

If Codex encounters a question that changes business meaning, identity semantics, evidence authority, time semantics, security/authority, correction behavior, model ownership, or object boundaries:

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

## 12. Completion condition

Build 001 is complete when:

- the semantic kernel is machine-readable;
- all current V1 candidate object types compose the common kernel contracts;
- relationship/role semantics are machine-readable;
- cross-model ownership/reference is explicit;
- the logical API surface is machine-readable;
- all six domain families have representative fixtures;
- T01–T31 are mapped to assertions;
- no production technology choice has been smuggled into semantic contracts;
- semantic ambiguities are surfaced explicitly.

The next build can then implement a reference/runtime Business Reality service after Platform Engineering establishes the appropriate implementation architecture.
