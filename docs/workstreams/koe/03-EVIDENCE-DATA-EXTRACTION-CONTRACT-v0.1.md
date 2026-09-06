# KOE Evidence/Data Extraction Contract — Build Spec 001

**Version:** v0.1  
**Status:** First-session handoff contract to Evidence & Data Engineering  
**Owner:** Knowledge & Ontology Engineering (KOE-001)

---

## 1. Purpose

Define exactly what semantic extraction should emit before canonicalization. This contract does **not** authorize promotion to canonical Business Reality.

The governing rule is:

> Discovery observes and proposes. Ontology defines and governs.

---

## 2. Required output envelope

Every extracted item must carry enough metadata to preserve provenance, security, epistemic status, and replayability.

Conceptual fields:

```text
extraction_id
source_evidence_id
source_system
source_native_id
source_version
source_container
source_reference
source_time
captured_or_discovered_time
content_hash
extractor_name
extractor_version
model_name_or_id (if applicable)
model_version (if applicable)
extracted_at
security_classification
source_acl_reference
explicit_or_inferred
confidence_dimensions
origin_lineage_id(s)
```

Confidence must be decomposable by task where possible (identity, context, relation, event, etc.), not represented only by one universal score.

---

## 3. Extraction target types

### 3.1 Observation

Directly observed metadata or content feature from source evidence.

Examples:

- sender address;
- recipient address;
- stated organization name;
- stated deadline;
- attachment filename;
- phrase indicating approval;
- message sent timestamp.

An Observation must retain the exact source span or source location where practical.

### 3.2 Source Party

A source-local participant record that may or may not map to a canonical Person or Organization.

Required fields conceptually:

- observed name;
- email/domain/identifier if present;
- source role (sender, recipient, author, signer, etc.);
- source evidence reference;
- candidate canonical matches if later resolution runs.

### 3.3 Candidate Identity

A proposed identity interpretation for an observed party or named entity.

Possible candidate types:

- Organization;
- Person;
- Artifact;
- Opportunity;
- Solicitation;
- Agreement;
- Project;
- other approved context types.

Must support zero, one, or multiple plausible canonical matches.

### 3.4 Candidate Alias

A proposed alias or shorthand linking an observed reference to a canonical or candidate identity.

Must include:

- observed text;
- scope/context;
- candidate target;
- global-versus-contextual status;
- evidence;
- confidence;
- whether historical/temporary shorthand is suspected.

### 3.5 Candidate Relationship

A proposed relationship among candidate/canonical parties or contexts.

Required semantics:

- participants;
- participant roles;
- proposed relationship family/type;
- scope/context;
- effective time or interval if inferable;
- evidence;
- explicit/inferred status;
- confidence;
- security classification.

### 3.6 Claim

A proposition asserted by a human source, document, system, or model.

Must preserve:

- proposition structure;
- asserting source/actor;
- claim time if known;
- supporting source evidence;
- claim target/context;
- whether the extractor is quoting, paraphrasing, or inferring;
- confidence in extraction, not truth.

### 3.7 Candidate Event

A proposed occurrence of something that happened.

Fields conceptually include:

- event type candidate;
- participants/objects;
- context;
- effective time or interval;
- exact/approximate flag;
- evidence;
- explicit/inferred status;
- confidence.

### 3.8 Decision Fragment

A source-backed fragment that may contribute to a historical Decision trace.

Examples:

- alternative mentioned;
- recommendation language;
- explicit choice statement;
- approval statement;
- rationale fragment;
- rejection of an alternative;
- authority statement.

Required fields:

- fragment kind;
- context candidate;
- actor/source;
- exact source span/reference;
- effective/source time;
- candidate linked alternatives/decision/action;
- explicit/inferred status;
- confidence.

Do not emit a canonical Decision merely because a message says "let's proceed."

### 3.9 Commitment / Deadline

A proposed obligation, promised action, or due date.

Must distinguish:

- who committed;
- to whom;
- to what action/deliverable;
- due/effective time;
- conditionality;
- evidence;
- whether the deadline is authoritative or informal.

### 3.10 Candidate Context

A proposed governing business context for a source record or extracted item.

Examples:

- Opportunity;
- Solicitation;
- Agreement;
- Project;
- workforce matter;
- compliance matter;
- invoice/payment matter.

Must allow:

- one strong context;
- multiple plausible contexts;
- unresolved;
- context hierarchy/parent relation;
- context expansion request.

### 3.11 Artifact / Document Link

A proposed relationship among an email attachment, SharePoint file, version, or canonical Artifact.

Possible link semantics:

- exact same bytes;
- copy of;
- version of;
- derived from;
- submitted form of;
- attachment appearance of;
- related but distinct.

Must preserve hash and source/version evidence.

### 3.12 Outcome Signal

A source-backed indicator of an Outcome.

Examples:

- award notice;
- loss notice;
- interview invitation;
- partner included in final proposal;
- acceptance confirmation.

An outcome signal is not automatically a canonical Outcome without authority/context checks.

---

## 4. Required independent classifications

Every source item should support independent routing dimensions:

### Signal type

- human substantive;
- system/automated operational;
- informational/contextual;
- noise.

### Business significance

- high;
- medium;
- low.

### Business domain

Multi-label where appropriate, including Commercial/Opportunity, Customer, Partner, Vendor, Delivery, Finance, Workforce, Legal, Compliance, Technology/IT, Internal Operations, Strategy, Other.

### Security

At minimum:

- Normal;
- Business Confidential;
- HR Restricted;
- Finance Restricted;
- Legal Restricted;
- Security Restricted;
- Executive Restricted.

These dimensions must not be collapsed into one class.

---

## 5. Provenance requirements

For every extracted semantic item, Evidence/Data Engineering must retain a resolvable chain back to the source evidence.

Minimum expectations:

- message/file native ID;
- source version;
- content hash;
- source location/URL where permitted;
- source timestamps;
- source actor/author;
- extractor/model provenance;
- source span or position when practical;
- security metadata;
- lineage to quoted/forwarded/copied origins.

---

## 6. Duplicate / origin-lineage rules

Repeated appearances must not be treated as independent origins by default.

The extraction layer should emit lineage equivalent to:

```text
origin_evidence_id
quoted_from
forwarded_from
copied_from
attachment_appearance_of
document_version_of
derived_from
```

If origin cannot be established, mark it unresolved rather than assuming independence.

---

## 7. Context-expansion request contract

The extractor/resolver may request additional evidence when current context is insufficient.

A request should specify:

- triggering source item;
- unresolved question;
- candidate contexts/entities;
- evidence types likely to help;
- proposed retrieval scope;
- security constraints;
- reason for expansion.

Examples:

- fetch earlier messages in the thread;
- retrieve referenced attachment;
- inspect SharePoint proposal versions;
- find solicitation number in related documents;
- retrieve prior partner discussion.

Expansion is support for interpretation; it does not redefine the original batch window.

---

## 8. What Evidence/Data Engineering must not do

The extraction pipeline must not:

- create canonical identities directly;
- promote Customer/Partner/Vendor as separate Organization universes;
- globally alias a shorthand based on one thread;
- mark legal agreement status canonical from casual email;
- count forwards/quotes as independent corroboration;
- collapse Event, Decision, Action, and Outcome;
- infer current state backward into history;
- hide model-generated inference as source assertion;
- weaken source security restrictions;
- create new ontology object types because an extractor found a new noun.

---

## 9. Minimal validation fixture for the SFO/CRI slice

For one representative thread/document bundle, the extraction output should visibly contain:

- observed `SFO` / airport references;
- observed `ServiceNow` shorthand;
- source parties and domains;
- candidate customer identity;
- candidate Opportunity and Solicitation context;
- CRI candidate Organization identity;
- candidate partner relationship scoped to the pursuit;
- artifact appearances and SharePoint candidate matches;
- event candidates such as partner contact / MNDA execution / proposal submission if evidenced;
- decision fragments rather than fabricated complete decisions;
- provenance and security metadata on every item;
- unresolved candidates where ambiguity remains.

The target output is an inspectable candidate graph, not an LLM narrative summary.

---

## 10. Handoff acceptance criteria

KOE considers the extraction contract satisfied when:

1. every emitted semantic item is source-traceable;
2. canonicalization has not occurred implicitly;
3. identity/context ambiguity can remain unresolved;
4. repeated evidence preserves origin lineage;
5. decision fragments remain semantically distinct from decisions/actions/events;
6. context expansion can be requested explicitly;
7. security labels persist into downstream candidate/reconciliation processing;
8. reprocessing can produce new interpretations without mutating raw evidence.
