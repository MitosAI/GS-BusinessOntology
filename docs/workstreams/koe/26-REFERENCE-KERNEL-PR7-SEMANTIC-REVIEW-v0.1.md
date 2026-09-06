# VERIFY / LEARN — Reference Business Reality Kernel PR #7

**Version:** v0.1  
**Status:** KOE semantic review  
**Owner:** KOE-001  
**Reviewed PR:** #7 `Build 002: executable Business Reality reference kernel v0.1`

## Objective

Verify the first executable reference kernel against approved KOE semantic invariants before expanding runtime scope.

## Evidence reviewed

- `src/gensigma_br/contracts.py`
- `src/gensigma_br/kernel.py`
- `tests/test_kernel_invariants.py`
- `docs/build/BUILD-002-REFERENCE-BUSINESS-REALITY-KERNEL-v0.1.md`
- GitHub Actions run `Reference Business Reality Kernel CI` on head `d674085...` — PASS

## PASS

### Contract enforcement

Runtime loads repository JSON Schema contracts using Draft 2020-12 validation and format checking.

### Raw evidence immutability / replay

`append_raw_evidence`:

- validates RawEvidence contract;
- returns no-op on exact replay;
- rejects reuse of an evidence ID with different content.

This is consistent with source-as-sensor, append-oriented evidence, and replay/idempotency doctrine.

### Evidence-backed candidates

`propose_candidate` rejects candidates whose referenced source evidence is not already present.

### No public direct canonical put path

Canonical state is introduced through `promote_candidate`, not a generic public `put_canonical` method.

### Promotion lineage

Promotion records retain:

- canonical resource ID;
- candidate ID;
- source evidence IDs;
- actor;
- reason;
- recorded time.

### Non-destructive correction

`correct_canonical_state` appends a new accepted interpretation while prior canonical versions remain retrievable through history.

### CI

Current GitHub Actions run is successful.

## GAPS — bounded implementation fixes

### G1 — Candidate semantic type is not enforced at promotion

Current behavior:

- candidate contains `proposed_semantic_type`;
- promoted resource contains `type`;
- runtime does not verify compatibility between them.

Therefore a candidate proposing `Organization` can currently be used to promote a different business type if that target schema validates.

**Required invariant:** when `proposed_semantic_type` is present, promotion must reject an incompatible resource type.

This is `LOCAL_SOLVE`: it enforces an existing contract; it does not create new semantics.

### G2 — Promotion schema resolution is hard-coded to business schemas

Current `_schema_name(...)` resolution always targets:

```text
schemas/business/<type>.schema.json
```

But approved semantic resources such as `Event`, `Assessment`, `Decision`, `Approval`, `Action`, and `Outcome` live under the kernel contract family.

As a result, the reference runtime cannot promote/validate those resource types even though BUILD SPEC 001 requires Event/Decision/Action/Outcome distinctions.

**Required invariant:** semantic-type validation must resolve through a contract registry/type map rather than assume every canonical semantic resource is in `schemas/business/`.

This is `LOCAL_SOLVE`: contract locations already exist; implementation must honor them.

## DEFERRED — explicitly not claimed by PR #7

The following are important but are already outside the stated PR #7 scope and should remain separate increments:

- full proposition-specific promotion authority/conflict evaluation;
- identity-resolution algorithms;
- typed relationship runtime;
- historical/as-of read semantics;
- production security-context enforcement;
- query/context API;
- production persistence;
- connectors;
- external governed actions.

PR #7 should not be rejected for not implementing these, provided its documentation continues to state the boundary clearly.

## Promotion-governance caution

The current runtime permits promotion for candidate states other than `rejected` and `superseded`. The broader promotion doctrine requires identity/context/authority/conflict checks before authoritative promotion.

Do **not** silently invent the final candidate-state transition policy in this reference slice. Until the exact state transition is encoded as an approved contract, treat this runtime as a reference mechanism, not a production authorization boundary.

## Recommendation

PR #7 is directionally correct and should continue after G1/G2 are closed with tests.

Do not broaden the same PR into temporal, security, relationship, query, connector, or persistence work. Keep those as independent increments under the Workstream Delivery Standard.

## Architecture disposition

- G1: `LOCAL_SOLVE`
- G2: `LOCAL_SOLVE`
- production promotion-policy state machine: not required for this PR; escalate only when a shared state-transition contract must be frozen.