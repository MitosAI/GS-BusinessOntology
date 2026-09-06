# GenSigma AI-Native Operating System — Roadmap and Milestones

**Version:** v0.1  
**Status:** Working execution roadmap  
**Scope:** Near-term sequencing from architecture into MVP implementation while preserving the long-term OS vision

---

## 1. Roadmap principle

The program should progress through **thin, real, end-to-end slices** rather than building every subsystem in isolation.

The sequence is:

```text
DOCTRINE
  -> LOGICAL MODEL
  -> BUILD SPEC
  -> PHYSICAL ARCHITECTURE
  -> PLATFORM FOUNDATION
  -> REAL DATA
  -> PRESSURE TEST
  -> REFINE
  -> KINETIC LOOP
  -> SCALE DOMAIN BY DOMAIN
```

The architecture is not considered validated because it looks elegant on paper. Real GenSigma evidence must pressure-test it.

---

## 2. Current status

Completed or substantially drafted:

- Constitution v0.2;
- World Model Platform Spec v0.1;
- Business Intent Layer Spec v0.1;
- Decision Engine and Capability Model Spec v0.1;
- Evidence / Knowledge / Discovery / Reconciliation Pipeline v0.1;
- Enterprise Ontology v0.1;
- Connector and Sensor Architecture v0.1;
- Foundational Architecture Decisions v0.1;
- initial Outlook pilot and evidence inventory;
- high-level Palantir-style kinetic architecture;
- decision-trace concept;
- source-as-sensor doctrine;
- temporal/backward-reconstruction doctrine;
- initial identity and reconciliation doctrine.

Current open frontier:

1. turn the doctrine into a buildable Business Reality / World Model MVP;
2. establish the intellectual architecture of computational executive judgment;
3. choose physical data infrastructure only after the MVP requirements are explicit.

---

## 3. Parallel execution model

Two primary tracks run in parallel.

```text
TRACK A — BUSINESS REALITY / PLATFORM
Ontology -> Evidence -> Reconciliation -> Storage -> APIs -> MVP

TRACK B — EXECUTIVE COGNITION
Decision science research -> computational judgment architecture -> Decision Engine spec
```

They synchronize through explicit contracts:

### Track A outputs to Track B

- current/historical business state;
- evidence and provenance;
- uncertainty/confidence;
- Business Intent;
- material external-world beliefs;
- Capability Model;
- available actions and constraints.

### Track B outputs to Track A

- required query patterns;
- decision-context requirements;
- uncertainty representation requirements;
- model inputs/outputs;
- action recommendations;
- audit/rationale requirements;
- decision-specific data requirements.

Neither workstream should invent the other's architecture silently.

---

# M0 — Foundation Governance

**Goal:** Make GitHub the durable memory and stop architectural drift.

### Deliverables

- project brief;
- operating architecture;
- roadmap;
- role charters;
- Constitution and foundation specs in GitHub;
- branch/PR workflow;
- ADR discipline;
- canonical naming and document hierarchy.

### Exit criteria

- every new workstream can start from repository artifacts without relying on chat history;
- every cross-cutting decision has a documented home;
- all foundational documents are linked from the repository README or index.

---

# M1 — Research 001: Computational Executive Judgment

**Goal:** Determine the intellectual and computational architecture of the `Decide` portion of the operating loop before building an arbitrary LLM-based judgment engine.

### Research domains

- normative decision theory;
- Bayesian decision theory and belief updating;
- operations research and optimization;
- game theory / mechanism / strategic interaction;
- control theory and feedback systems;
- behavioral decision science and bounded rationality;
- strategic management / executive decision practice;
- AI reasoning, planning and LLM-assisted decision systems;
- military command-and-control / OODA where useful.

### Questions

- What is the computational object being optimized?
- How should uncertainty be represented?
- When is Bayesian updating appropriate?
- How should utility be represented from Business Intent?
- When should game theory be activated?
- When is optimization appropriate versus qualitative judgment?
- How should causal reasoning enter?
- Which decisions require deterministic rules?
- Which benefit from probabilistic reasoning?
- Which should use LLMs only for interpretation or alternative generation?
- What should remain human-governed?
- How should outcomes update future decision policy?

### Deliverables

- Research 001 synthesis;
- comparative discipline map;
- candidate executive-cognition architecture;
- decision-class taxonomy;
- deterministic/probabilistic boundary map;
- research-backed updates to Decision Engine Spec.

### Exit criteria

We can explain, without hand-waving, how a decision moves from evidence/state/intent to recommendation/decision and why each computational technique is used.

---

# M2 — Build Spec 001: Business Reality / World Model MVP

**Goal:** Define the smallest build that proves the business-reality architecture against actual GenSigma evidence.

### Build Spec must settle

- MVP domain boundary;
- concrete business questions to answer;
- required canonical objects;
- required relationships;
- required event types;
- evidence/claim structure;
- temporal semantics;
- identity and context-resolution behavior;
- security behavior;
- canonical promotion path;
- read/query API contract;
- proposed-write API contract;
- benchmark queries;
- realistic dataset size and ingestion volume;
- acceptance tests.

### Important discipline

Do not pick the database before these requirements are concrete.

### Exit criteria

A competent engineering team can implement the slice without inventing ontology semantics or core correctness rules during coding.

---

# M3 — Physical Data Architecture Decision

**Goal:** Select the initial physical persistence/search architecture from measured requirements rather than preference.

### Candidate architecture categories

- relational-first;
- graph-first;
- relational + graph projection;
- document/graph hybrid;
- Azure-native multi-model options;
- dedicated object storage + operational database + search/vector index.

### Benchmark dimensions

- identity lookup;
- multi-hop relationship traversal;
- temporal queries;
- transactional canonical writes;
- evidence lineage;
- source-record scale;
- version history;
- security enforcement;
- semantic/full-text search;
- decision-trace traversal;
- operational complexity;
- cloud cost;
- portability;
- developer velocity;
- recovery and audit.

### Deliverables

- ADR for physical storage architecture;
- benchmark results;
- schema/persistence mapping;
- migration/portability strategy.

### Exit criteria

We can state exactly why the selected architecture wins for Build Spec 001 workloads and what would cause us to revisit it.

---

# M4 — Azure Platform Foundation

**Goal:** Establish the minimal secure cloud substrate for the MVP.

### Expected components

- Azure subscription/resource-group structure;
- Entra service principals / managed identities;
- Key Vault;
- immutable/raw evidence storage;
- selected operational database(s);
- compute/runtime for connector and processing services;
- logs/telemetry;
- environment separation;
- network/security baseline;
- infrastructure-as-code where practical.

### Security baseline

- no credentials in source code;
- least privilege;
- separate service identities;
- auditable access;
- restricted HR/legal/security data paths;
- dev/test/prod separation appropriate to MVP maturity.

### Exit criteria

The system can securely receive source data and run the ingestion/reconciliation pipeline without manual secrets or local-only dependencies.

---

# M5 — Sensor 001: Outlook / Exchange Online

**Goal:** Build production-shaped evidence ingestion from the highest-value initial communication source.

### Required behavior

- incremental ingestion;
- stable source IDs;
- mailbox/folder identity;
- sender/recipient metadata;
- timestamps;
- thread/conversation IDs;
- MIME/body preservation strategy;
- attachment references;
- content hashes;
- idempotency;
- source deletions/changes policy;
- access-control metadata;
- raw evidence immutability.

### Pilot

Use the already observed main Inbox + Sent pilot as the first benchmark dataset.

### Exit criteria

Repeated ingestion produces no accidental duplicates and every normalized observation can be traced back to the exact source record.

---

# M6 — Sensor 002: SharePoint

**Goal:** Add document evidence and version lineage so context can be expanded beyond email.

### Required behavior

- site/library/file identity;
- version metadata;
- permissions metadata;
- source URLs/IDs;
- content hashes;
- document family/version lineage;
- attachment-to-SharePoint reconciliation;
- immutable evidence references;
- metadata and textual extraction boundaries.

### Exit criteria

The system can recognize that an emailed attachment and a SharePoint document/version are copies, descendants or related artifacts rather than blindly distinct documents.

---

# M7 — Evidence Graph + Candidate Extraction

**Goal:** Give uncertainty a structured home.

### Extract

- organizations;
- people;
- names/aliases;
- relationships;
- business contexts;
- opportunities/solicitations/projects/agreements;
- events;
- claims;
- commitments;
- decision fragments;
- actions;
- outcomes;
- dates/deadlines;
- security classifications.

### Rules

- extracted output is non-authoritative;
- provenance is mandatory;
- repeated quoted/forwarded copies should not count as independent evidence;
- model/version provenance is preserved for material inference.

### Exit criteria

We can inspect a source thread and see a transparent candidate graph rather than opaque LLM prose.

---

# M8 — Identity and Context Reconciliation

**Goal:** Resolve observations against what GenSigma already knows before creating canonical objects.

### Cases to support

- same object;
- alias;
- historical name;
- parent/child;
- organization/unit;
- person changed organization;
- product name versus opportunity shorthand;
- related but distinct;
- probable merge;
- split;
- unresolved;
- genuinely new candidate.

### Acceptance examples

`SFO`, `SF Airport`, and `San Francisco International Airport` should be reconcilable without forcing all CCSF references into one undifferentiated object.

`ServiceNow` should not automatically become an opportunity when it may refer to a platform or capability.

### Exit criteria

We can move backward through older evidence without multiplying canonical entities every time naming changes.

---

# M9 — Canonical Business Reality Service

**Goal:** Materialize governed operational state and expose it through stable APIs.

### Minimum read surface

```text
get_object
resolve_identity
get_neighbors
get_relationships
get_state
get_timeline
get_evidence
get_decision_trace
search
```

### Minimum proposed-write surface

```text
propose_object
propose_relationship
propose_claim
propose_event
propose_merge
propose_split
promote_candidate
reject_candidate
```

### Exit criteria

A user or AI can ask factual/contextual questions without touching raw source schemas directly.

---

# M10 — First Decision Reconstruction

**Goal:** Reconstruct one real historical decision loop from evidence.

### Target structure

```text
Evidence
  -> Assessment
  -> Alternatives
  -> Recommendation
  -> Decision
  -> Approval
  -> Action
  -> State Change
  -> Outcome
```

The exact business episode should be chosen for richness, not merely because it was the first email observed.

### Exit criteria

The system can clearly distinguish explicit versus inferred parts of the decision trace and show supporting evidence.

---

# M11 — First Computational Decision Prototype

**Goal:** Apply the Research 001 architecture to one bounded real decision class.

Candidate decision classes might include:

- bid/no-bid;
- partner selection;
- opportunity prioritization;
- staffing/resource assignment;
- collections escalation.

The choice should follow from data availability, decision frequency, impact and evaluability.

### Exit criteria

The system produces an auditable recommendation using explicit state, intent, uncertainty, alternatives and decision criteria — not merely an LLM opinion.

---

# M12 — First Kinetic Action

**Goal:** Close the loop with one low-risk typed business action.

Example classes:

- create follow-up task;
- request missing evidence;
- draft partner outreach;
- create opportunity workspace;
- update an internal controlled status.

### Exit criteria

```text
STATE
 -> DECISION
 -> AUTHORIZATION
 -> TYPED ACTION
 -> EXECUTION
 -> VERIFIED RESULT
 -> EVENT
 -> UPDATED STATE
```

The full audit chain must be visible.

---

# M13 — Domain Expansion

After the first vertical loop works, expand deliberately:

1. Commercial / opportunities;
2. Delivery;
3. Finance;
4. Workforce;
5. Systems/assets;
6. Compliance/legal;
7. broader external-world sensing.

Each domain must reuse canonical identity and shared interfaces rather than spawning disconnected ontologies.

---

## 4. Workstream synchronization cadence

Each workstream should maintain:

- current objective;
- decisions made;
- assumptions;
- open questions;
- changes proposed to Constitution/ADRs/specs;
- artifacts committed to Git;
- dependencies on other workstreams.

Cross-cutting changes return to the Chief Architect workstream before being treated as canonical.

---

## 5. What not to do

- Do not build a huge ontology before testing real data.
- Do not choose graph storage because the word `graph` appears in the architecture.
- Do not make email summaries canonical truth.
- Do not allow LLM output to silently mutate business state.
- Do not model every external news event.
- Do not mix strategic intent with current state.
- Do not let a framework own GenSigma's semantics.
- Do not let parallel threads create conflicting architecture without reconciliation.
- Do not postpone security until the UI.
- Do not confuse a successful demo with a trustworthy operating system.

---

## 6. Immediate next actions

1. Complete and review the role charters.
2. Start `RESEARCH-001` in the Executive Cognition Research Lead thread.
3. Start Build Spec 001 preparation in the Knowledge/Ontology Engineering thread.
4. Start Azure and physical-data option discovery in Platform Engineering, but do not finalize database selection before Build Spec query requirements are stable.
5. Reconcile outputs through the Chief Architect thread.
