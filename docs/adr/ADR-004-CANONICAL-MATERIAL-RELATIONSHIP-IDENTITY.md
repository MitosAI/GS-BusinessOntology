# ADR-004 — Canonical Material Relationship Identity

**Status:** Accepted  
**Date:** 2026-09-07  
**Decision owner:** CA-001 — Chief Architect  
**Semantic owner:** KOE-001 — Knowledge & Ontology Engineering  
**Decision record:** GitHub Issue #41  
**Implementation:** PR #37  
**Supersedes implementation interpretation:** PR #22 / Linear GEN-5, only where it treated `TypedRelationship` as independently promotable

## Context

GenSigma's accepted Business Reality catalog and Build Spec 001 minimum subset admit `BusinessRelationship` as the canonical object for a material relationship with independent identity, lifecycle, evidence, time, security, correction, query value, or actions.

The repository also contains `typed-relationship.schema.json`, intended as the reusable structural relationship envelope. PR #22 interpreted that helper schema as a separate canonical semantic type and registered `TypedRelationship` for promotion. This left both `BusinessRelationship` and `TypedRelationship` available to represent the same real-world relationship, with incompatible fields and lifecycle vocabularies.

The conflict risks duplicate canonical identity, ambiguous downstream APIs, and weaker participant/scope integrity.

## Decision

1. `BusinessRelationship` is the sole canonical promotable semantic type for material relationships.
2. `typed-relationship.schema.json` is a reusable kernel shape composed by the BusinessRelationship schema. It is not independently promotable.
3. Lightweight typed links may exist as non-object projections. They do not have separate canonical identity and must resolve to governing canonical semantics.
4. A canonical BusinessRelationship requires:
   - at least two distinct canonical participants;
   - explicit contextual roles for every participant;
   - generic `participant_ref` references, because relationship endpoints are not limited to parties;
   - an explicit canonical scope reference, including an explicit governed enterprise/organization context for enterprise-wide scope;
   - effective time, epistemic status, provenance, security, audit, and correction semantics through the shared resource envelope.
5. Participant and scope references must resolve to existing canonical resources and match their semantic type, model owner, and contract version.
6. Relationship correction preserves the relationship identity and prior accepted interpretations. A second promotion cannot overwrite or silently extend an existing canonical identity.
7. The same canonical relationship is traversable from each participant side; reverse traversal does not create a second relationship identity.

## Consequences

### Required changes

- remove `TypedRelationship` from the promotable contract registry;
- make BusinessRelationship compose the typed-relationship envelope;
- align the relationship vocabulary on `relationship_family`, `relationship_type`, `participants`, `scope_refs`, and `relationship_state`;
- update OpenAPI proposal/list contracts to BusinessRelationship;
- update GEN-5 tests and fixtures;
- retain/add endpoint-existence, distinct-participant, scope, traversal, correction, lineage, and overwrite-protection tests;
- treat GEN-5 as implementation evidence, not semantic completion, until the corrected tests pass.

### Compatibility

No production migration is required because the reference kernel is pre-production and no canonical production data store has been selected. Fixtures or clients using `type: TypedRelationship` or `party_ref` must move to `type: BusinessRelationship` and `participant_ref`.

### Deferred

This ADR does not choose:

- production relationship persistence;
- graph versus relational storage;
- temporal query algorithms;
- security policy evaluation;
- relationship-type-specific authority;
- multi-hop query implementation.

## Alternatives rejected

### TypedRelationship as the canonical type

Rejected because it conflicts with the admitted BusinessRelationship object and would require a breaking semantic rewrite across the catalog, Build Spec subset, APIs, fixtures, and consumers without a distinct real-world identity.

### Both types promotable

Rejected because no non-overlapping identity, lifecycle, or ownership distinction exists. Two types would allow duplicate canonical representations of one relationship.

## Governing basis

- `CONSTITUTION.md`
- `docs/adr/ADR-002-BUILD-SPEC-001-SCOPE-AND-SEMANTIC-FOUNDATION.md`
- `docs/build/BUILD-SPEC-001-BUSINESS-REALITY-MVP-SKELETON-v0.1.md`
- `docs/workstreams/koe/09-BUSINESS-REALITY-V1-OBJECT-CATALOG-v0.1.md`
- `docs/workstreams/koe/13-V1-BUSINESS-OBJECT-DEFINITIONS-v0.1.md`
- `docs/workstreams/koe/14-TYPED-RELATIONSHIP-AND-ROLE-CATALOG-v0.1.md`
- `docs/workstreams/koe/19-V1-LIFECYCLE-STATE-VOCABULARY-v0.1.md`
- `docs/workstreams/koe/27-BUILD-SPEC-001-MINIMUM-SEMANTIC-SUBSET-v0.1.md`
- Issue #41 CA-001 `DECIDED` disposition
