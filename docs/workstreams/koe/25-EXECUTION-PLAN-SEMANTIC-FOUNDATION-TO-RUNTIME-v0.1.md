# EXECUTION PLAN — Semantic Foundation to Runtime

**Status:** IN_PROGRESS  
**Owner workstream:** KOE-001  
**Design basis:** ADR-002, Business Reality Semantic Foundation, Build Spec 001 skeleton, Workstream Delivery Standard, T01–T31, FF-001–FF-010

## Goal

Move KOE from broad semantic-foundation design into verified executable runtime increments without allowing implementation convenience or one pilot to redefine enterprise semantics.

## Architecture / design basis

Governing split:

- **Business Reality Semantic Foundation** = broad enterprise compatibility envelope (~38 current candidate semantic objects plus shared kernel contracts).
- **BUILD SPEC 001** = Chief Architect-owned narrow first vertical slice selecting only the minimum coherent subset plus shared identity/time/evidence/security/correction invariants.

Delivery posture is benchmarked against evolutionary architecture, small self-contained increments, automated fitness functions, and staged verification.

## Deliverables

1. Reframe stale KOE artifacts so `BUILD SPEC 001` no longer names the enterprise-wide semantic foundation.
2. Finalize KOE's recommended minimum semantic subset for BUILD SPEC 001.
3. Review and verify PR #7 Reference Business Reality Kernel against KOE invariants.
4. Convert verified gaps into bounded Codex-ready implementation tasks.
5. Extend the reference kernel incrementally through typed relationships, temporal reads, security enforcement, and query contracts.
6. Preserve runtime neutrality on production persistence/cloud topology until Platform benchmarks are complete.
7. Record verification findings and update semantic contracts only when implementation exposes a genuine semantic defect.

## Work breakdown

### W1 — Governance/name reconciliation

- mark enterprise-wide KOE docs as Business Reality Semantic Foundation artifacts;
- remove stale language implying Issue #5 is unresolved;
- reference accepted ADR-002;
- update PR #3 description to current status.

### W2 — BUILD SPEC 001 subset recommendation

Define:

- shared kernel invariants always required;
- minimum canonical business objects for the first commercial/opportunity vertical slice;
- evidence/candidate resources required below canonical boundary;
- conditional objects that enter only if the chosen episode exercises them;
- competency queries and acceptance tests for the slice.

No pilot-specific ontology classes.

### W3 — Verify reference kernel PR #7

Review against:

- source evidence immutability/replay;
- candidate evidence linkage;
- candidate semantic-type compatibility;
- promotion lineage/audit;
- correction preservation;
- no direct canonical write path;
- contract validation;
- CI status.

Record PASS / GAP / DEFERRED findings.

### W4 — Promotion-integrity increment

Bounded runtime work to close semantic gaps discovered in W3 without adding new architecture.

### W5 — Typed relationship increment

Implement the existing typed-relationship contract with scope, participant roles, effective time, provenance, security metadata, and correction history.

### W6 — Temporal/as-of increment

Implement current and historical reads consistent with effective time vs recorded/discovery time semantics.

### W7 — Security-context increment

Implement explicit actor/security context and non-leakage behavior for reads/traversals/evidence access.

### W8 — Query-contract increment

Implement the smallest query surface needed by BUILD SPEC 001 benchmark scenarios: object, relationships, state/as-of, evidence, contradictions, timeline/decision trace as applicable.

### W9 — VERIFY / LEARN

Run T01–T31 and relevant FF checks against the implemented subset. Update durable design only for verified semantic learning.

## Dependency graph

```text
W1 -----------+
              |
W2 -----------+----> BUILD SPEC 001 semantic handoff

W3 -> W4 -> W5 -> W6 -> W7 -> W8 -> W9

Platform benchmark/persistence choice remains downstream of measured workload.
```

W1/W2 can proceed in parallel with W3.

## Parallelizable tasks

- naming/governance cleanup;
- minimum-slice subset specification;
- PR #7 semantic review;
- benchmark/fitness harness preparation.

Runtime increments W4–W8 should remain small and sequential where later correctness depends on earlier contracts.

## Acceptance suite

A work item is complete only when:

- governing contract is named;
- implementation behavior is tested;
- no direct source-to-canonical bypass exists;
- evidence/provenance survives correction;
- ambiguity is not silently coerced;
- security/time semantics are preserved where in scope;
- CI passes;
- any semantic learning is written back to GitHub.

PR #7 verification additionally requires:

- CI success confirmed from GitHub Actions;
- candidate cannot justify an incompatible semantic type;
- promotion/correction retain enough lineage for audit;
- scope limitations are explicit rather than implied completeness.

## Risks / unknowns

- current KOE PR #3 still contains stale `BUILD SPEC 001` naming in several artifact filenames/text;
- reference kernel PR #7 is stacked on KOE PR #3 and must be retargeted/rebased after PR #3 is reconciled;
- runtime performance/scale targets remain open pending Platform measurement;
- production persistence/search/cloud topology remain intentionally undecided.

## Explicitly out of scope

- production database selection;
- graph vs relational decision;
- vector database selection;
- Azure service topology;
- Outlook/SharePoint connector implementation in KOE;
- agent framework selection;
- autonomous external-system actions;
- full implementation of all ~38 candidate objects in the first runtime.

## Architecture questions

None currently open for KOE. ADR-002 resolved the previous Build Spec scope conflict.

Any new shared semantic/interface/security/time/ownership conflict must use `ASK_ARCHITECT`; all ordinary implementation decomposition is `LOCAL_SOLVE`.