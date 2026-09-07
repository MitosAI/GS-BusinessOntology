# Typed Relationship Runtime Contract

**Version:** v0.1  
**Status:** IMPLEMENTED REFERENCE INCREMENT  
**Owner:** KOE-001 — Knowledge & Ontology Engineering Lead  
**Execution plan:** `docs/workstreams/koe/25-EXECUTION-PLAN-SEMANTIC-FOUNDATION-TO-RUNTIME-v0.1.md`

## Objective

Make the accepted typed-relationship semantics executable in the reference Business Reality kernel without choosing production persistence, temporal-query, or authorization architecture.

## Context

The original contracts contained two incompatible shapes:

- `BusinessRelationship` used `relationship_kind`, `participant_refs`, `scope_ref`, and `status`;
- `TypedRelationship` used `relationship_family`, `relationship_type`, role-bearing `participants`, `scope_refs`, and `relationship_state`.

The runtime semantic resolver promotes `BusinessRelationship`, while the richer relationship semantics lived only in the separate kernel component. Codex could not implement both without inventing which representation governed.

## Benchmark evidence

Established Palantir ontology practice treats a link type as the schema of a relationship and a link as one relationship instance. A single link supports traversal from both sides; distinct link types between the same objects remain distinct business relationships.

- https://www.palantir.com/docs/foundry/object-link-types/link-types-overview
- https://www.palantir.com/docs/foundry/ontology/overview

Palantir also treats derived traversal results as security-context-sensitive projections, supporting GenSigma's existing rule that relationship projection must not bypass access policy:

- https://www.palantir.com/docs/foundry/object-link-types/derived-properties

These sources sharpen the existing GenSigma contract; they do not introduce a new ontology doctrine.

## Canonical representation

1. `BusinessRelationship` is the promotable canonical semantic type.
2. `typed-relationship.schema.json` is its reusable kernel envelope, not a second promotable semantic type.
3. The BusinessRelationship schema composes the typed-relationship envelope and fixes:
   - `type = BusinessRelationship`;
   - `model_owner = business_reality`.
4. `participant_ref` is a generic canonical reference. It is not named `party_ref`, because cataloged relationships may connect Opportunity, Solicitation, Agreement, Project, Event, Decision, Action, Outcome, and other non-party resources.
5. Every material relationship has at least two role-bearing participants and at least one explicit canonical scope reference.
6. Enterprise-wide scope is represented by an explicit canonical enterprise/organization context reference. An empty scope must not silently mean enterprise-wide authority.

## Runtime invariants

### Promotion

- A BusinessRelationship must enter canonical state through a candidate whose `candidate_type` is `relationship`.
- The candidate's `proposed_semantic_type`, when present, must be `BusinessRelationship`.
- Each participant and scope reference must resolve to an existing canonical resource.
- Each reference's `type`, `model_owner`, and `contract_version` must match the referenced canonical resource.
- The same participant, contextual role, and role qualifier tuple cannot appear twice.
- One participant may hold multiple distinct contextual roles where business truth requires it.
- A second promotion cannot reuse an existing canonical resource ID. Changes must use the audited correction path.
- Promotion retains candidate and source-evidence lineage.

### Correction

- Relationship correction preserves the canonical relationship ID and semantic type.
- Participant, role, relationship type, state, scope, time, provenance, and security corrections are append-only interpretations.
- Prior accepted interpretations and correction records remain retrievable.
- Reclassification into another canonical semantic type is not part of ordinary correction.

### Query

- `get_relationships(resource_id)` returns the current accepted relationship interpretation for every relationship in which the resource is a participant.
- The same relationship is traversable from every participant side; a reverse duplicate relationship is not created.
- Optional `relationship_type` and `scope_id` filters restrict results without broadening scope.
- Result ordering is deterministic by relationship ID.

## Failure behavior

The runtime fails explicitly when:

- the candidate is not a relationship candidate;
- a participant or scope does not exist canonically;
- a reference claims an incompatible type, model owner, or contract version;
- an exact participant-role-qualifier tuple is duplicated;
- a promotion attempts to overwrite an existing canonical ID;
- a correction attempts to change canonical identity or semantic type.

No failure is converted into an unresolved or accepted relationship silently.

## Security, time, evidence, and authority

This increment preserves security descriptors, effective time, epistemic state, provenance, evidence lineage, and audit metadata.

It does not claim:

- `as_of` evaluation;
- recorded-time replay;
- policy evaluation or non-leakage enforcement;
- relationship-type-specific authority rules;
- production transactions or persistence.

Those remain W6 and W7 or later governed-action work. Callers must not infer those guarantees from this reference API.

## Dependencies

- merged Business Reality reference kernel;
- `14-TYPED-RELATIONSHIP-AND-ROLE-CATALOG-v0.1.md`;
- `16-CORE-RESOURCE-ENVELOPE-AND-VERSIONING-v0.1.md`;
- `02-QUERY-AND-WORKLOAD-CONTRACT-v0.1.md`;
- JSON Schema Draft 2020-12 contracts;
- T07, T13, T18 and applicable provenance/correction rules.

## Acceptance criteria and required tests

- [x] BusinessRelationship composes the typed-relationship kernel envelope.
- [x] Generic canonical participant references replace party-only naming.
- [x] Scope is explicit and non-empty.
- [x] Relationship promotion succeeds through evidence -> relationship candidate -> canonical state.
- [x] Unknown and contract-incompatible participant/scope references fail.
- [x] Exact duplicate participant-role-qualifier tuples fail.
- [x] A non-relationship candidate cannot promote a BusinessRelationship.
- [x] A promoted relationship is traversable from either participant.
- [x] Type and scope filters do not infer broader relationships.
- [x] Relationship correction preserves prior interpretation and changes the current traversal result.
- [x] Repeat promotion cannot bypass correction history.
- [ ] Repository CI passes on the implementation PR.
- [ ] KOE reviews the PR against semantic correctness.

## Explicit non-scope

- no new canonical object type;
- no relationship-specific database/table/graph selection;
- no cardinality constraints beyond semantic minima;
- no `as_of` implementation;
- no security policy engine;
- no multi-hop neighbor traversal;
- no source connector changes;
- no autonomous action or external writeback.

## Architecture disposition

`LOCAL_SOLVE`.

This change resolves an inconsistency inside already-approved KOE semantics. It does not alter cross-workstream ownership, the Build Spec 001 boundary, or production platform architecture.
