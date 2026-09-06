# Semantic Kernel — Core Resource Envelope and Versioning

**Version:** v0.1  
**Status:** KOE implementation contract  
**Owner:** Knowledge & Ontology Engineering (KOE-001)

---

## 1. Purpose

Every canonical resource in the operational ontology must compose the same small kernel for identity, time, provenance, security, correction, and contract versioning.

Domain objects extend this envelope; they do not redefine it.

---

## 2. Canonical resource envelope

Conceptual shape:

```text
CanonicalResource
  id
  type
  contract_version
  display_name?
  lifecycle_state?
  effective_time
  recorded_at
  discovered_at?
  epistemic_status
  provenance_refs[]
  security
  source_mappings[]
  supersession
  audit
  extensions?
```

### `id`

Stable opaque canonical identifier.

Rules:
- never derived solely from current name;
- survives rename/reclassification where identity remains the same;
- never reused for a different canonical identity;
- source IDs are mappings, not canonical IDs.

### `type`

Canonical semantic type under a versioned contract.

Rules:
- type changes that alter meaning are audited corrections/migrations;
- contextual roles do not mutate `type`.

### `contract_version`

Version of the semantic contract used to interpret the resource.

Rules:
- version is explicit;
- readers must know compatibility/migration behavior;
- schema version and resource identity are independent.

### `display_name`

Human-friendly current label, not identity.

Historical names/aliases belong in alias/source mapping structures with scope/time where material.

---

## 3. Temporal envelope

Minimum temporal semantics:

```text
effective_time
  valid_from
  valid_to?
  precision: exact | approximate | unknown

recorded_at
source_time?
discovered_at?
```

### Effective/business time

When the state/relationship/proposition is true in business reality.

### Source time

When the source created/sent/recorded the evidence.

### Recorded time

When the canonical/evidence system recorded the interpretation.

### Discovery time

When the platform first discovered the evidence/state.

Rules:
- these times must not be silently collapsed;
- later discovery can support earlier effective time only when evidence justifies it;
- historical `as_of` queries operate on effective time plus recorded/correction semantics defined by the query contract.

---

## 4. Epistemic envelope

Canonical resources and assertions may carry explicit epistemic state:

```text
observed
asserted
inferred
reconstructed
accepted
unresolved
contradicted
rejected
superseded
unknown
```

Not every business object needs every state. The common vocabulary allows consistent handling.

Rules:
- probabilistic extraction never silently becomes `accepted`;
- `accepted` means governed canonical interpretation, not metaphysical certainty;
- contradiction may coexist with an accepted current interpretation while resolution is pending;
- unresolved is a valid output, not an error condition.

---

## 5. Provenance reference

Every material canonical assertion/state/relationship must be traceable to provenance.

Conceptual reference:

```text
ProvenanceRef
  provenance_id
  source_system
  source_native_id?
  source_version?
  artifact_or_evidence_id?
  origin_lineage_id?
  extractor_or_actor?
  interpretation_method?
  model_version?
  captured_at?
  support_role: supports | contradicts | contextualizes | derives
```

Rules:
- copied/forwarded/duplicated evidence with common origin does not become independent corroboration;
- provenance references may be security-restricted independently from the canonical resource projection;
- canonical state without retrievable provenance is prohibited for material claims unless an explicit policy exemption exists.

---

## 6. Source mapping

Conceptual shape:

```text
SourceMapping
  source_system
  source_namespace
  source_native_id
  source_version?
  mapping_state
  valid_from?
  valid_to?
  evidence_ref?
```

Mapping states:

```text
accepted
proposed
rejected
superseded
ambiguous
```

Rules:
- a source record may map to a candidate without canonical acceptance;
- merge/split operations preserve prior source mappings and mapping history;
- source mapping never grants authority to redefine canonical semantics.

---

## 7. Security envelope

Conceptual shape:

```text
SecurityDescriptor
  classification?
  policy_refs[]
  source_acl_refs[]
  allowed_principals_or_scopes[]?
  denied_principals_or_scopes[]?
  property_restrictions[]?
  evidence_restrictions[]?
```

Rules:
- effective access is computed under actor/security context;
- source ACLs are inputs, not the only policy;
- ontology policy may be stricter than source ACLs;
- unauthorized data must not leak through search, traversal, counts/snippets where sensitive, inference, or derived projections.

---

## 8. Audit envelope

Conceptual shape:

```text
AuditMetadata
  created_by
  created_at
  last_changed_by?
  last_changed_at?
  change_reason?
  change_request_id?
  approval_ref?
  correlation_id?
```

Rules:
- every material canonical mutation is attributable to an actor;
- actor may be human, service, or governed AI agent;
- AI agent identity never bypasses normal authority/security rules.

---

## 9. Supersession and correction

Conceptual shape:

```text
Supersession
  supersedes_ids[]
  superseded_by_ids[]
  correction_type?
  correction_reason?
  effective_correction_time?
  recorded_correction_time?
```

Correction types may include:

```text
state_correction
identity_merge
identity_split
reclassification
relationship_correction
time_correction
provenance_correction
security_correction
semantic_migration
```

Rules:
- destructive overwrite of material interpretation is prohibited;
- source evidence is never rewritten to match a corrected interpretation;
- derived projections can be rebuilt from current accepted interpretation plus preserved history.

---

## 10. Alias contract

Aliases are not plain strings attached forever to an identity.

Conceptual shape:

```text
Alias
  value
  alias_type
  scope?
  valid_from?
  valid_to?
  source_or_evidence_ref?
  status
```

Alias types may include:

```text
legal_name
trade_name
historical_name
acronym
source_label
contextual_shorthand
email_domain
identifier
```

Rules:
- contextual shorthand does not become global alias automatically;
- historical names retain effective periods where material;
- ambiguous alias resolution may return multiple candidates.

---

## 11. Cross-model reference

Models reference each other's canonical resources without copying semantic ownership.

Conceptual shape:

```text
CanonicalRef
  id
  type
  model_owner
  contract_version
  projection_version?
```

Rules:
- a referencing model cannot silently mutate the owning model's object;
- cached projections are derived and replaceable;
- contract incompatibility must fail explicitly rather than reinterpret silently.

---

## 12. Extension rule

Domain contracts may add fields through versioned schemas, but extensions must not override kernel semantics.

Allowed:
- domain lifecycle details;
- typed domain properties;
- domain-specific relationship references;
- domain-specific action/state constraints.

Not allowed:
- second canonical ID system;
- alternative time semantics;
- bypassing provenance/security;
- redefining epistemic status differently per domain;
- destructive correction behavior;
- domain-owned copies of shared canonical identities.

---

## 13. Contract evolution

Semantic contract changes are classified:

### Compatible additive

New optional property, new optional link, new enum value where consumers are forward-compatible.

### Compatible-with-migration

Property semantics clarified or structure evolved while identity meaning remains stable.

### Breaking semantic change

Object meaning, identity rule, ownership boundary, required invariant, or action semantics change.

Breaking semantic changes require:

1. explicit KOE decision/ADR;
2. new contract version;
3. migration strategy;
4. affected-resource identification;
5. regression/acceptance tests;
6. dependent model/service impact assessment.

---

## 14. Minimal machine-readable requirements for Codex

The machine-readable kernel must define reusable schemas/components for:

- CanonicalResource;
- CanonicalRef;
- EffectiveTime;
- EpistemicStatus;
- ProvenanceRef;
- SourceMapping;
- SecurityDescriptor;
- AuditMetadata;
- Supersession;
- Alias;
- TypedRelationship.

Every business schema should compose these common contracts rather than copy/paste their fields independently.
