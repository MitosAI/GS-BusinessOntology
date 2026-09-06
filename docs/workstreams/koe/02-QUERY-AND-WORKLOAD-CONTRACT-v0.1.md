# KOE Query and Workload Contract — Build Spec 001

**Version:** v0.1  
**Status:** First-session workload contract for Platform Engineering  
**Owner:** Knowledge & Ontology Engineering (KOE-001)  
**Purpose:** Define logical workload requirements before physical storage selection.

---

## 1. Principles

1. No query may bypass security context.
2. Historical queries must preserve effective-time semantics.
3. Evidence retrieval must preserve provenance and origin lineage.
4. Identity resolution must support ambiguity and contextual aliases.
5. Common business traversals must not require source-schema knowledge.
6. Search is not canonical truth; search results resolve to governed resources/evidence.
7. Proposed writes are not equivalent to canonical writes.

---

## 2. Benchmark query suite

### Q1 — Canonical identity resolution

```text
resolve_identity("SFO", context=<commercial pursuit>, as_of=<date>, security_context=<actor>)
```

**Expected behavior:** return ranked candidate identities, accepted canonical identity if resolvable, alias/context rationale, confidence dimensions, and unresolved status when appropriate.

**Correctness:** must not collapse similarly named organizations or organizational units without evidence.

**Consistency:** read-your-writes for accepted reconciliation changes.

**Performance class:** interactive.

---

### Q2 — Ambiguous contextual shorthand

```text
resolve_identity("ServiceNow", context=<thread/artifact/context bundle>, ...)
```

**Expected behavior:** distinguish product/capability reference from opportunity shorthand where evidence permits; otherwise preserve ambiguity.

**Correctness:** global alias creation is forbidden from one local shorthand occurrence.

---

### Q3 — Current canonical state

```text
get_state(opportunity_id, as_of=NOW, security_context=...)
```

**Expected behavior:** coherent accepted state plus provenance references and effective times.

**Consistency:** transactionally coherent canonical snapshot.

**Performance class:** interactive.

---

### Q4 — Historical state

```text
get_state(opportunity_id, as_of="2026-08-15T17:00:00-07:00", ...)
```

**Expected behavior:** reconstruct accepted state at requested effective time without projecting later facts backward.

**Temporal requirement:** support exact and approximate effective times.

**Performance class:** interactive to short analytical.

---

### Q5 — Opportunity timeline

```text
get_timeline(opportunity_id, time_range=<bounded>, ...)
```

**Expected behavior:** ordered Events, Decisions, Actions, Outcomes, and relevant state changes; explicit/inferred flags visible.

**Correctness:** semantic resource types remain distinguishable.

---

### Q6 — Multi-hop business traversal

```text
get_neighbors(customer_id, depth=3,
  link_filters=[customer_of, governed_by, partner_in, stakeholder_in, governed_by_agreement], ...)
```

Representative path:

```text
Customer -> Opportunity -> Partner -> Person -> Agreement
```

**Requirement:** 1–3 hop traversals are common; occasional deeper traces may occur.

**Performance class:** interactive for common bounded traversals.

---

### Q7 — Evidence for a claim or relationship

```text
get_evidence(relationship_id, ...)
```

**Expected behavior:** supporting and contradicting evidence, source provenance, origin lineage, authority metadata, explicit/inferred status, and security-filtered content.

**Correctness:** copied/quoted appearances cannot masquerade as independent corroboration.

---

### Q8 — Artifact lineage

```text
get_artifact_lineage(artifact_id, ...)
```

**Expected behavior:** attachment appearances, SharePoint appearances, versions, derived/copy relationships, hashes, and source identity.

**Requirement:** exact hash and near-duplicate lineage may both be represented, with confidence/status distinctions.

---

### Q9 — Decision trace

```text
get_decision_trace(opportunity_or_decision_id, ...)
```

**Expected traversal:** Evidence -> Assessment -> Alternative(s) -> Recommendation -> Decision -> Approval -> Action -> Outcome.

**Correctness:** absent stages remain absent; reconstructed stages are labeled inferred/reconstructed.

**Performance class:** interactive for one episode.

---

### Q10 — Contradiction detection

```text
find_contradictions(scope=<opportunity/customer/relationship>, ...)
```

**Expected behavior:** return incompatible claims/state proposals with evidence, authority differences, time scope, and resolution status.

**Analytical class:** may be slower than point reads.

---

### Q11 — Unresolved reconciliation queue

```text
find_unresolved_candidates(filters={type: Organization|Person|Context|Artifact, risk: ...}, ...)
```

**Expected behavior:** review queue with candidate matches, evidence, confidence dimensions, and proposed resolution actions.

**Consistency:** newly accepted reconciliation results should disappear from unresolved queue atomically with promotion/update.

---

### Q12 — Security-aware search

```text
search("CRI ServiceNow MNDA", filters=<domain/time/type>, as_of=<optional>, security_context=...)
```

**Expected behavior:** combine exact, alias, lexical/fuzzy, and semantic retrieval while filtering unauthorized resources/evidence before exposure.

**Security:** forbidden results must not leak through snippets, counts where sensitive, vector retrieval, traversals, or follow-on evidence fetches.

---

## 3. Write/transaction workload

### W1 — Propose candidate object

A proposal may be created from extraction without canonical mutation.

### W2 — Accept alias / identity link

Must atomically update reconciliation state, canonical alias mapping, audit history, and unresolved queue state.

### W3 — Promote relationship/state

Must validate required evidence/authority/policy and atomically create or update canonical state plus promotion audit.

### W4 — Correct canonical interpretation

Must preserve previous interpretation, provenance, effective period, and reversibility. Destructive overwrite is not acceptable.

### W5 — Merge / split proposal and execution

Merge/split operations must preserve source mappings and allow later correction. High-risk identity changes require stronger governance than low-risk aliases.

---

## 4. Scale assumptions for MVP benchmarking

These are order-of-magnitude planning assumptions, not contractual production limits.

- initial Outlook pilot: hundreds to low-thousands of messages in the focused window, with contextual expansion outside the window;
- SharePoint pilot: tens to low-hundreds of relevant artifacts/versions for the selected episode and adjacent pursuits;
- evidence records: multiple observations/claims/candidates per source artifact;
- canonical entities for first slice: low-hundreds or less;
- relationships/events/evidence links: potentially several times entity count;
- historical backfill is expected to scale progressively to much larger corpora, so design must not depend on all data fitting in a single in-memory graph.

Platform Engineering should benchmark beyond the immediate slice to detect architectural cliffs, but KOE does not prescribe the physical benchmark implementation.

---

## 5. Consistency requirements

### Strong consistency required for

- canonical identity acceptance;
- canonical promotion/correction;
- merge/split decisions;
- security policy changes affecting canonical access;
- action/state transitions when kinetic writes are introduced;
- audit records associated with canonical mutations.

### Eventual consistency acceptable for derived projections where safe

- semantic/vector indexes;
- denormalized read projections;
- non-authoritative analytics;
- background contradiction scans;
- candidate ranking refreshes.

Derived projections must never silently become more authoritative than canonical state.

---

## 6. Temporal requirements

The physical architecture must support queries over:

- current state;
- state as of effective time;
- event/action/decision timelines;
- relationship effective intervals;
- discovery time versus source/effective time;
- corrections that preserve prior accepted interpretations;
- scenario/hypothetical state isolated from current truth.

A single mutable row plus `updated_at` is insufficient as the only temporal mechanism.

---

## 7. Graph/traversal requirements

The workload includes:

- frequent identity-to-context and context-to-evidence hops;
- 1–3 hop bounded traversals as a normal interactive pattern;
- decision traces crossing heterogeneous resource types;
- relationship-neighborhood signals used during reconciliation;
- path filters by type, time, security, and context.

Graph-like traversal capability is a requirement; graph-native primary persistence is not.

---

## 8. Search requirements

Search must support combinations of:

- exact identifiers;
- canonical names;
- aliases/historical names;
- lexical/fuzzy text;
- metadata filtering;
- source/provenance filtering;
- time filtering;
- semantic retrieval;
- security context.

Search must return governed resources or evidence references with epistemic status; it must not flatten canonical and candidate/evidence layers into one undifferentiated result set.

---

## 9. Audit and explainability requirements

For any material canonical fact or identity resolution, the platform must be able to answer:

- what source evidence supported it;
- what reconciliation/promotion decision created it;
- who/what actor made or approved that decision;
- when it became effective;
- what prior interpretation it superseded;
- whether AI/model output contributed;
- whether the conclusion is explicit, inferred, or reconstructed.

---

## 10. Benchmark success criteria for M3 handoff

A physical architecture candidate is viable only if it can demonstrate, using representative fixtures:

- correct alias/identity resolution support;
- temporal state queries;
- common multi-hop traversals;
- evidence lineage retrieval;
- transactional canonical promotion/correction;
- end-to-end security-aware search and traversal;
- auditability and reversibility;
- acceptable operational complexity and cost for an MVP.

The winning technology choice must be documented later in an ADR with measured trade-offs.
