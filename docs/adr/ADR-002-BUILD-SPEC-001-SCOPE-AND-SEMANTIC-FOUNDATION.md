# ADR-002 — BUILD SPEC 001 Scope vs Business Reality Semantic Foundation

**Status:** Accepted  
**Decision owner:** Chief Architect  
**Date:** 2026-09-05

## Context

Knowledge & Ontology Engineering produced an enterprise-wide Business Reality semantic foundation with a V1 compatibility envelope of approximately 30–40 candidate business objects, executable semantic contracts, fixtures, API semantics, and fitness mappings. Separately, the Chief Architect-owned BUILD SPEC 001 defines the first executable vertical slice and intentionally keeps that build narrow enough to implement, benchmark, and validate quickly.

The phrase `BUILD SPEC 001` was being used for both scopes, creating an architecture and ownership collision.

## Decision

Adopt **Option A** from Architecture Decision Request #5.

1. **Business Reality Semantic Foundation** is the broader enterprise semantic compatibility envelope. It may define more objects, relationships, shared-kernel contracts, and cross-domain semantics than the first executable build uses.
2. **BUILD SPEC 001** remains the Chief Architect-owned **narrow first executable vertical slice**.
3. BUILD SPEC 001 selects the minimum coherent subset of the Business Reality Semantic Foundation required for the chosen pilot episode plus the shared cross-cutting invariants required for correctness, provenance, time, security, identity/reconciliation, and correction.
4. The broader semantic foundation must not force all candidate V1 objects into the first runtime.
5. The first vertical slice must not redefine the enterprise ontology merely because the pilot happens to expose only part of it.
6. KOE artifacts that currently call the enterprise-wide semantic package `BUILD SPEC 001` must be renamed/reframed before merge so the two scopes are unambiguous.

## Rationale

This preserves both architectural truths:

- the ontology must be enterprise-oriented and must not be defined by one pilot;
- implementation must proceed through thin, testable, end-to-end slices rather than a broad platform build.

The split also keeps Platform and Evidence/Data workload bounded while preserving forward compatibility with the broader semantic model.

## Consequences

- KOE keeps and evolves the enterprise Business Reality semantic foundation.
- Chief Architect owns BUILD SPEC 001 scope and integration gate.
- KOE must recommend the minimum canonical subset for BUILD SPEC 001.
- Platform Engineering benchmarks only the selected Build Spec workload, while checking that the physical design does not foreclose the broader compatibility envelope.
- Evidence/Data extracts only the semantic targets required by the active slice plus shared-kernel evidence requirements.

## Supersession / revisit condition

Revisit only if repeated vertical slices demonstrate that a shared semantic-foundation build must itself be deployed as an independent runtime milestone. If so, create a new explicitly named build milestone rather than overloading BUILD SPEC 001.