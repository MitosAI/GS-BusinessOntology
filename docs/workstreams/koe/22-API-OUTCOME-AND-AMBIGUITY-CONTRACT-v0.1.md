# Business Reality API — Outcome, Ambiguity, and Failure Contract

**Version:** v0.1  
**Status:** KOE semantic baseline  
**Owner:** Knowledge & Ontology Engineering (KOE-001)

---

## 1. Purpose

The API must represent business uncertainty and semantic failure explicitly. `null`, empty arrays, and generic HTTP 500 responses are not sufficient for identity ambiguity, contradiction, security denial, historical supersession, or semantic conflict.

---

## 2. Common response envelope

Conceptual shape:

```text
result_status
request_id
contract_version
data?
candidates[]?
issues[]?
provenance_refs[]?
security_projection?
```

Recommended `result_status` vocabulary:

```text
ok
partial
unknown
unresolved
ambiguous
contradicted
superseded
conflict
forbidden
not_found
invalid_request
invalid_transition
unauthorized_action
contract_version_mismatch
```

---

## 3. Semantics

### `ok`

The request resolved successfully under current contract/security context.

### `partial`

Some valid data is returned but requested scope is incomplete because of missing data, restricted projection, unavailable dependency, or bounded traversal.

The reason must be explicit.

### `unknown`

The system has no established value/state for the requested proposition.

This is not the same as `not_found`.

### `unresolved`

Evidence/candidates exist but the system has not accepted a canonical resolution.

### `ambiguous`

Multiple plausible resolutions satisfy the current evidence/context. Candidate references/rationale should be returned where authorized.

### `contradicted`

Material incompatible claims/states exist and have not been fully resolved.

The accepted current interpretation, if any, must remain distinguishable from competing claims.

### `superseded`

Requested resource/interpretation/version is historical and has a known successor/correction.

Historical access may still return the superseded resource with successor references.

### `conflict`

The requested write/promotion cannot be accepted because it conflicts with current canonical state, concurrency/version, identity rules, or invariant constraints.

### `forbidden`

Caller identity is known but security policy prohibits the requested read/projection.

No sensitive existence/content leakage beyond policy.

### `not_found`

No authorized matching canonical resource exists for the requested identifier.

Must not reveal whether an unauthorized resource exists unless policy permits.

### `invalid_request`

Request violates API/contract shape or lacks required semantic context.

### `invalid_transition`

Requested state/action transition is not legal under the semantic lifecycle contract.

### `unauthorized_action`

Caller may have read access but lacks authority to propose/promote/approve/execute the requested action.

### `contract_version_mismatch`

Caller and service cannot safely interpret the same semantic contract version.

Fail explicitly; do not silently reinterpret.

---

## 4. Identity resolution response

Conceptual response:

```text
result_status: ok | unresolved | ambiguous | not_found | forbidden
accepted_match?
  canonical_ref
  resolution_basis
  confidence_dimensions?
candidates[]
  canonical_ref
  rationale
  evidence_refs[]
  disambiguating_context[]
```

Rules:
- no forced match when ambiguity remains;
- confidence alone is not authority;
- contextual alias resolution must expose scope when material.

---

## 5. Historical state response

Conceptual response:

```text
resource_ref
as_of_effective_time
accepted_state_at_time?
recorded_interpretation_at_query_time?
subsequent_corrections[]?
result_status
```

The contract must make clear whether the caller requests:

1. **business state effective at T using current knowledge**, or
2. **what the system had accepted/recorded as of T**.

These are different temporal questions and must not be conflated.

---

## 6. Evidence response

Evidence retrieval may return:

```text
ok
partial
forbidden
not_found
```

A permitted canonical projection does not imply all supporting evidence is visible.

Restricted evidence references may be omitted/redacted according to policy without leaking protected content.

---

## 7. Proposed-write response

Conceptual shape:

```text
proposal_id?
result_status
validation_issues[]
conflicts[]
required_approvals[]?
next_allowed_actions[]?
```

Proposed writes may return `ok` even though canonical state has not changed. The response must distinguish proposal acceptance from canonical promotion.

---

## 8. Promotion/correction response

A promotion/correction must expose:

```text
result_status
changed_resource_refs[]
prior_version_refs[]
new_version_refs[]
effective_time
recorded_at
actor_ref
approval_refs[]?
audit_ref
rebuild_or_invalidation_refs[]?
```

Correction must never appear as a silent overwrite.

---

## 9. Search/traversal response

Search and traversal may be incomplete because of security, ambiguity, or explicit depth/limit.

The API should distinguish:

```text
complete
bounded
security_filtered
partial_dependency_failure
```

Do not expose counts/snippets that reveal unauthorized resources where policy forbids existence leakage.

---

## 10. Error handling principle

Transport errors and semantic outcomes are different.

Examples:

- HTTP/service timeout = transport/runtime failure.
- `ambiguous` = valid semantic outcome.
- `invalid_transition` = valid governed rejection.
- `forbidden` = authorization outcome.
- `contradicted` = valid knowledge state.

Applications and agents must be able to branch on semantic outcomes without parsing free-text messages.

---

## 11. Agent behavior

Agents consuming this API must:

- treat `unknown`, `unresolved`, and `ambiguous` as meaningful states;
- not convert `partial` into certainty;
- not retry `unauthorized_action` as if it were transient;
- not promote a proposal simply because creation returned `ok`;
- preserve contract-version information in tool/action calls;
- surface semantic conflicts rather than fabricating a resolution.

---

## 12. Codex rule

OpenAPI must model these outcomes explicitly through typed response schemas/components. Generic `data: any` plus free-text error strings is insufficient for Build 001 acceptance.
