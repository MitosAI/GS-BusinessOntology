# GenSigma Connector and Sensor Architecture Specification

**Version:** v0.1  
**Status:** Draft for architectural review  
**Initial sensors:** Microsoft 365 Outlook and SharePoint

---

## 1. Purpose

Connectors are the controlled boundary between external systems and the GenSigma World Model Platform.

Their job is to observe sources accurately, preserve provenance/security, and deliver evidence into the discovery pipeline.

They do not own business semantics and do not write canonical ontology truth directly.

---

## 2. Core principle

> A data source is a sensor and evidence provider. It is not an ontology branch.

Therefore the system SHALL NOT create source-defined canonical concepts such as Outlook Customer, SharePoint Customer, QuickBooks Customer or CRM Customer.

Instead, source records map through evidence and reconciliation to canonical `Organization`, `Person`, `Opportunity`, `Agreement`, `Invoice`, etc.

---

## 3. Connector responsibilities

A connector is responsible for:

- authentication;
- authorized source access;
- discovery of source containers;
- incremental synchronization;
- source-native IDs;
- metadata capture;
- content/attachment retrieval where allowed;
- source ACL/security capture;
- tombstone/deletion detection where supported;
- rate-limit handling;
- retry/backoff;
- idempotency;
- checkpointing;
- observability;
- provenance.

A connector is not responsible for canonical identity, final business context, promotion of facts, final partner/customer status, decision-trace interpretation or bypassing source permissions.

---

## 4. Canonical connector contract

Every source connector should conceptually emit a normalized envelope.

```text
SourceEnvelope
  source_system
  source_tenant
  source_container
  source_native_id
  parent_native_id
  object_kind
  source_created_time
  source_modified_time
  source_version
  content_hash
  payload_pointer / normalized payload
  source_acl
  capture_time
  connector_version
  correlation_id
```

The normalized envelope is a transport/evidence contract, not the enterprise ontology.

---

## 5. Cloud and identity posture

Azure is the likely first hosting environment because GenSigma already uses Microsoft 365 and Entra ID.

However:

- ontology semantics must remain cloud-neutral;
- connector contracts must not assume Azure-specific business meaning;
- Entra should provide identity/auth integration where useful;
- secrets should be isolated in managed secret storage;
- least privilege must be enforced.

Azure is an implementation decision, not part of the ontology's meaning.

---

## 6. Outlook sensor

The Outlook/Exchange connector should support mailbox/folder discovery, message capture, incremental sync and historical backfill.

### Message capture

Preserve immutable source ID, internet message ID where available, conversation/thread metadata, sender, recipients, sent/received timestamps, subject, body reference/content, attachment metadata, labels where available and source permissions.

### Incremental sync

Prefer source-supported delta/change tracking when reliable. Polling may be used where necessary but must be checkpointed.

### Historical backfill

Support controlled windows and resumable pagination. Current-to-past processing is an orchestration choice above the connector; the connector should support arbitrary authorized time ranges.

---

## 7. SharePoint sensor

The SharePoint connector should support site discovery under configured scope, libraries/folders, document/item IDs, version metadata, author/editor, created/modified times, file hash/content hash, content type, path, source ACLs, list metadata, file bytes/text retrieval under policy and version history where required.

SharePoint is both evidence storage and a source of operational metadata. It is not automatically the authority for the substantive truth contained in a document.

---

## 8. Attachment handling

Email attachments should be captured as distinct artifacts linked to their containing message.

```text
Email
  -> AttachmentAppearance
        -> source bytes/hash
        -> candidate Document identity
```

This enables later reconciliation against SharePoint copies and versions.

---

## 9. Idempotency

Repeated synchronization must not create duplicate evidence objects.

Conceptual key:

```text
(source_system, source_native_id, source_version)
```

If source version is unavailable, use a defined substitute such as modified time + hash while preserving the native ID.

---

## 10. Change detection and tombstones

The sensor layer should represent change rather than silently overwriting local evidence.

Potential change types: created, updated, moved, permissions changed, deleted/tombstoned, restored.

Deleting a source artifact should not erase previously used ontology provenance. The platform may mark evidence unavailable at source while retaining permitted audit metadata.

---

## 11. Security propagation

Source ACLs should be captured as evidence for access policy.

The World Model security model may impose stronger restrictions, but never silently weaker access than legally/operationally permitted.

Connector credentials should use least privilege and should not be reused by agents directly.

Sensitive content should be isolated during ingestion and classified before broad search/vector exposure.

---

## 12. Secret and credential management

Connectors should never embed credentials in code/config repositories.

Requirements include managed secrets, rotation support, separate dev/test/prod identities, scoped OAuth/application permissions, audit of token use where available, and revocation procedure.

---

## 13. Reliability model

Connectors should be designed for replay.

Required concepts include checkpoint, batch/correlation ID, retry count, dead-letter/quarantine state, transient versus permanent error, rate-limit state, replay command and connector version.

A failed semantic extraction must not require re-downloading the source if raw evidence is already safely captured.

---

## 14. Separation of stages

```text
CONNECTOR
   -> raw evidence
NORMALIZER
   -> normalized evidence
EXTRACTOR
   -> observations/claims/candidates
RESOLVER
   -> identity/context candidates
GOVERNANCE
   -> ontology proposals
ONTOLOGY
   -> canonical state
```

This separation allows connectors to remain simple and trustworthy while semantic logic evolves independently.

---

## 15. Source permission versus ontology permission

The system must account for both:

```text
Source ACL
   AND
Ontology Security Policy
```

A user or agent should only receive content if the effective access policy permits it.

A canonical object may be visible even when a specific evidence artifact is not.

---

## 16. Observability

Each connector should expose last successful sync, sync lag, item counts, bytes processed, API throttling, failures by category, permission errors, checkpoint state, duplicates avoided, tombstones processed, source/schema changes and connector version.

---

## 17. Future sensors

Later connectors may include QuickBooks Online, Bill.com/AP/AR, Rho/bank data, CRM/pipeline, Teams, HR/payroll, procurement portals, legal/corporate registries, project/timesheet systems and external market/regulatory feeds.

Each should follow the same sensor contract rather than creating a new semantic universe.

---

## 18. Connector SDK direction

A future internal connector SDK should provide common primitives for:

```text
authenticate()
discover_containers()
read_changes(checkpoint)
fetch_item(id, version)
fetch_binary(id)
read_acl(id)
checkpoint()
normalize_envelope()
emit_metrics()
classify_error()
```

This is implementation guidance, not a programming-language/framework commitment.

---

## 19. First implementation slice

### Outlook

One mailbox; Inbox + Sent Items; bounded recent window; metadata + body + attachment metadata; thread identifiers; source IDs/hashes; incremental checkpoint.

### SharePoint

Selected opportunity/proposal libraries; metadata + files + version information; ACL capture; hash/content retrieval.

### Goal

```text
Outlook + SharePoint
  -> reproducible raw evidence
  -> normalized evidence
  -> document/thread lineage
  -> discovery pipeline
```

---

## 20. Acceptance criteria

The connector architecture passes V0.1 when re-running sync does not duplicate evidence; every normalized record points to stable provenance; attachments remain separately identifiable; SharePoint versions can be distinguished; source permissions are available downstream; sync can resume from checkpoint; raw evidence can be reprocessed without source re-fetch where permitted; semantic changes do not require connector rewrites; connectors never write canonical ontology state directly; and Azure hosting can change later without changing business semantics.
