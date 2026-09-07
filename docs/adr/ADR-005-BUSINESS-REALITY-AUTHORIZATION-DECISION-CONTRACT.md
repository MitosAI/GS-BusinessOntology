# ADR-005 — Business Reality Authorization Decision Contract

**Status:** Accepted  
**Decision owner:** Chief Architect  
**Date:** 2026-09-06  
**Decision record:** GitHub Issue #40

## Context

Build Spec 001 requires security-aware reads that preserve source permissions and
ontology policy without leaking forbidden existence, text, counts, traversal, or
evidence. The existing SecurityContext and SecurityDescriptor schemas described
inputs but did not define how a Business Reality read obtained and enforced an
authorization decision.

The ambiguity included empty allowlists, subject matching, deny precedence,
unresolved source ACL and policy references, existence-sensitive outcomes, and
property/evidence projection. Implementing any one interpretation locally would
have changed security behavior across Platform, KOE, EDE, connectors, and
Executive Cognition.

## Decision

Adopt an injected policy decision point (PDP) and enforce its result at every
Business Reality read/query policy enforcement point (PEP).

1. The PEP validates and submits a versioned AuthorizationRequest containing
   SecurityContext, operation, protected-resource reference and
   SecurityDescriptor, projection kind, temporal context, and request context.
2. Subject matching uses the exact union of actor_id, principal_refs, role_refs,
   and delegation_refs. References are opaque, exact identifiers in v0.1.
3. An empty allowed_principals_or_scopes list imposes no additional
   descriptor-local constraint; it is not an access grant. A non-empty allowlist
   requires at least one exact subject match.
4. Any matching explicit deny overrides every allow.
5. Every applicable source_acl_ref and policy_ref must resolve and authorize.
   Missing, unavailable, malformed, unsupported, or indeterminate evaluation
   denies access.
6. The PDP returns a versioned AuthorizationDecision with allow/deny, a stable
   reason code, property projection, evidence projection, obligations, safely
   auditable evaluated references, and an existence-disclosure flag.
7. The PEP applies property/evidence restrictions before serialization and may
   only narrow the decision.
8. A denied canonical point read returns the same not-found behavior as an absent
   object unless separate policy grants existence disclosure. The same rule
   governs search, counts, snippets, traversal, evidence, and assembled
   DecisionContext projections.
9. No production path has a permissive fallback. Tests whose subject is not
   authorization may inject an explicitly named permissive test PDP.

## Consequences

- Policy interpretation is not embedded in handlers, query logic, or storage.
- The reference runtime can prove enforcement behavior without selecting an
  identity provider or authorization vendor.
- Empty fixture metadata remains usable only with an explicit test decision
  point; it is never interpreted as public access.
- Canonical visibility and supporting-evidence visibility remain independent.
- New read/query surfaces must use the same PEP and non-disclosure behavior
  before they can claim FF-006.

## Required contracts

- `contracts/schemas/kernel/authorization-request.schema.json`
- `contracts/schemas/kernel/authorization-decision.schema.json`
- `contracts/schemas/kernel/security-context.schema.json`
- `contracts/schemas/kernel/security-descriptor.schema.json`
- `contracts/api/business-reality.openapi.yaml`

## Validation

Runtime tests must cover empty and non-empty allowlists, every subject-reference
class, deny precedence, unresolved/denied source ACL and policy references,
property and evidence projection, diagnostic disclosure, and indistinguishable
not-found behavior. Search/count/snippet/traversal tests become mandatory when
those reference APIs are implemented.

## Non-decisions

This ADR does not select a policy product, identity provider, source ACL resolver,
database, graph engine, cloud, or deployment topology. It does not define
mutation authority or supersede governed promotion/correction requirements.

## Benchmark basis

- NIST policy decision point and policy enforcement point separation
- OWASP deny-by-default and permission validation on every request
- Azure RBAC explicit-deny precedence

## Supersession

Changes to deny precedence, fail-closed reference handling, exact subject
matching, or default non-disclosure require a new Chief Architect decision.
