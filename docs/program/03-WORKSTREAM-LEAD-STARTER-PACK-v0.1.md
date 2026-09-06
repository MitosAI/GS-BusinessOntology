# GenSigma AI-Native Operating System — Workstream Lead Starter Pack

**Version:** v0.1  
**Status:** Working operating plan  
**Audience:** Chief Architect, Executive Cognition Research Lead, Knowledge & Ontology Engineering Lead, Evidence & Data Engineering Lead, Platform Engineering Lead  
**Repository:** `MitosAI/GS-BusinessOntology`  
**Working branch at time of issue:** `docs/program-operating-model-v0.1`  
**Governing source:** `CONSTITUTION.md`, approved ADRs, and the program/foundation specifications in this repository

---

# 1. How to use this document

This is the common launch document for every parallel GenSigma OS workstream.

The purpose is to let multiple ChatGPT threads or human/AI contributors work in parallel **without re-inventing the architecture or drifting from the agreed doctrine**.

Every lead should:

1. read the shared source-of-truth documents in the order specified below;
2. read the charter for their role;
3. operate only inside their role boundary unless a cross-cutting issue is explicitly escalated;
4. commit durable work products to GitHub rather than leaving them only in chat;
5. return architectural conflicts, ontology changes, new cross-cutting concepts, or irreversible platform choices to the Chief Architect for review;
6. pressure-test theory against real GenSigma evidence and operating decisions;
7. avoid silently changing previously approved doctrine.

The role threads are not independent mini-projects. They are specialized workstreams contributing to one GenSigma OS.

---

# 2. Program north star

GenSigma is building an **AI-native operating system for the company**, not an AI assistant sitting beside the company.

The long-term ambition is to progressively reproduce and improve much of the executive and operational cognition currently dependent on the founder and leadership team.

The system should be able to:

- represent the company and the portion of the external world that materially affects it;
- preserve what is known, believed, inferred, uncertain, historical, hypothetical, and authoritative;
- understand GenSigma's intent, strategy, goals, constraints, risk appetite, and operating principles;
- evaluate alternatives under uncertainty;
- recommend or make governed decisions;
- execute typed, authorized business actions;
- observe outcomes;
- learn from outcomes without uncontrolled model drift.

A useful shorthand is:

> **Build the operating brain of GenSigma, not an LLM bolted onto GenSigma.**

---

# 3. Shared conceptual architecture

All leads must preserve the following distinctions.

```text
                       BUSINESS INTENT
        Who are we? What do we do? What do we seek?
        Vision · mission · strategy · goals · risk · plans
                               |
                               v
                       BUSINESS REALITY
         What is actually true inside and around GenSigma?
      Organizations · people · relationships · opportunities
        agreements · projects · finance · events · decisions
                               |
                 +-------------+-------------+
                 |                           |
                 v                           v
        EXTERNAL WORLD MODEL          CAPABILITY MODEL
 What do we believe about the         What can GenSigma
 material outside world?              actually do now?
 Markets · regulation · tech          Resources · skills · cash
 customers · competitors · policy     authority · capacity
                 |                           |
                 +-------------+-------------+
                               |
                               v
                    EXECUTIVE JUDGMENT
                Evidence · uncertainty · models
               alternatives · utility · constraints
                               |
                               v
                    DECISION / APPROVAL
                               |
                               v
                       KINETIC ACTION
                               |
                               v
                    NEW BUSINESS STATE
                               |
                               v
                    OUTCOME / LEARNING
                               |
                               +-----> updates relevant models
```

The architecture is intentionally **deterministic at the core and probabilistic at the edges**.

Deterministic/strongly typed where possible:

- identity and authorization;
- ontology/object typing;
- policy enforcement;
- state transitions;
- provenance;
- temporal history;
- arithmetic;
- approvals;
- action contracts;
- audit trails.

Probabilistic where reality is uncertain or unstructured:

- entity resolution;
- interpretation of email/documents;
- confidence and belief updating;
- predictions;
- strategic scenarios;
- causal hypotheses;
- LLM-assisted reasoning.

---

# 4. Architectural doctrine every lead must obey

## 4.1 Palantir-style operational ontology is the primary spine

The ontology is not merely a glossary, semantic search layer, knowledge graph, MDM repository, or source-system schema.

It ultimately combines:

```text
WORLD
what exists

+

TIME / EVENTS
what happened

+

DECISION
what was assessed / recommended / chosen

+

KINETIC ACTION
what can actually be done

+

OUTCOME / LEARNING
what resulted and what changes future behavior
```

## 4.2 Sources are sensors, not truth

Outlook, SharePoint, QuickBooks, CRM, procurement portals, files, public data, and later systems provide evidence.

They do not define ontology branches and they do not directly mutate canonical truth.

```text
SOURCE
 -> RAW EVIDENCE
 -> OBSERVATION / CLAIM / CANDIDATE
 -> CONTEXT + IDENTITY RECONCILIATION
 -> AUTHORITY / CONFLICT / VALIDATION
 -> CANONICAL BUSINESS REALITY
```

## 4.3 Evidence before canonicalization

The Enterprise Evidence Graph is allowed to be messy. It can contain ambiguity, duplicates, contradictions, candidate identities, candidate relationships, candidate events, aliases, AI interpretations, confidence, and decision fragments.

Canonical Business Reality is governed.

## 4.4 Identity must be reconciled continuously

> **Never allow a newly discovered name to automatically become a new canonical object. Reconcile first.**

Source observations are immutable; canonical interpretation is revisable.

Merge/split/re-parent/reclassification must be provenance-preserving and reversible.

## 4.5 Time is first-class

Where material, distinguish:

- business/effective time;
- source time;
- recorded time;
- discovery time;
- current state;
- historical state;
- hypothetical/scenario state.

## 4.6 Events, decisions, actions, and outcomes are distinct

Do not collapse all business activity into an activity log.

A Decision Trace is primarily a traversal through resources such as:

```text
Evidence -> Assessment -> Alternatives -> Recommendation
-> Decision -> Approval -> Action -> State Change -> Outcome -> Learning
```

## 4.7 The ontology must remain kinetic

Business nouns must eventually expose governed verbs.

Material business writes should occur through typed actions rather than arbitrary field mutation.

## 4.8 Security is architectural

Security must be possible at object, evidence, action, and where needed property/relationship level.

Agents are governed actors, not superusers.

---

# 5. Source-of-truth reading order for every lead

Before doing material work, read these files from `MitosAI/GS-BusinessOntology`.

If the current working branch has not yet been merged, use `docs/program-operating-model-v0.1`; after merge, use `main`.

### Mandatory common reading

1. `CONSTITUTION.md`
2. `docs/program/00-PROJECT-BRIEF-v0.1.md`
3. `docs/program/01-OPERATING-ARCHITECTURE-v0.1.md`
4. `docs/program/02-ROADMAP-AND-MILESTONES-v0.1.md`
5. `docs/specs/01-WORLD-MODEL-SPEC-v0.1.md`
6. `docs/specs/02-BUSINESS-INTENT-LAYER-SPEC-v0.1.md`
7. `docs/specs/03-DECISION-ENGINE-AND-CAPABILITY-MODEL-SPEC-v0.1.md`
8. `docs/specs/04-EVIDENCE-KNOWLEDGE-DISCOVERY-PIPELINE-v0.1.md`
9. `docs/specs/05-ENTERPRISE-ONTOLOGY-v0.1.md`
10. `docs/specs/06-CONNECTOR-AND-SENSOR-ARCHITECTURE-v0.1.md`
11. `docs/specs/07-FOUNDATIONAL-ARCHITECTURE-DECISIONS-v0.1.md`

Then read the role-specific charter listed below.

No lead should begin from memory, a generic AI pattern, or an assumed architecture when these sources are available.

---

# 6. Program hierarchy and dependency model

The workstreams report architecturally to the Chief Architect, but they do not all block one another.

```text
                         CHIEF ARCHITECT
                               |
       +-----------------------+-----------------------+
       |                       |                       |
       v                       v                       v
EXECUTIVE COGNITION     KNOWLEDGE & ONTOLOGY     PLATFORM ENGINEERING
RESEARCH                ENGINEERING                    |
                               |                       |
                               | semantic/query         | substrate/runtime
                               | requirements           |
                               v                       v
                    EVIDENCE & DATA ENGINEERING
                    ingestion · normalization
                    extraction · lineage · replay
```

Functional dependencies:

- **Knowledge & Ontology Engineering defines what business/evidence structures mean.**
- **Evidence & Data Engineering implements source-to-evidence processing against those semantics.**
- **Platform Engineering provides the secure substrate, persistence, runtime, identities, deployment, observability, and benchmark infrastructure.**
- **Executive Cognition Research defines how reliable Business Reality + Intent + Capability + External World information should be converted into judgment and decisions.**
- **Chief Architect resolves cross-workstream conflicts and approves changes to shared doctrine.**

Important sequencing rule:

> Evidence/Data Engineering may begin source inventory, immutable acquisition design, normalization, lineage, and idempotency immediately, but it must not invent canonical ontology semantics or promotion rules. Those come from Knowledge & Ontology Engineering.

Important platform rule:

> Platform Engineering may build the Azure landing zone and benchmarking harness immediately, but it must not finalize the primary database before Knowledge/Ontology provides query, consistency, temporal, graph, security, and scale requirements.

---

# 7. Lead 1 — Chief Architect

**Role:** Architectural integrator and doctrine owner  
**Existing charter:** `docs/roles/01-CHIEF-ARCHITECT-CHARTER.md`

## Mission

Preserve one coherent GenSigma OS architecture while specialized workstreams move quickly in parallel.

## Goals

- keep the full AI-native OS north star visible;
- preserve the Business Intent / Business Reality / External World / Capability / Judgment / Kinetic / Learning distinctions;
- prevent ontology, data engineering, cloud architecture, or AI research from becoming independent architectures;
- adjudicate material trade-offs;
- approve Constitution/ADR/spec changes;
- sequence the path from research/specification to Build Spec 001 to code;
- ensure GitHub remains the durable source of truth.

## Immediate responsibilities

- review deliverables from the four specialist leads;
- identify collisions or missing interfaces;
- approve Build Spec 001 boundary;
- approve the first physical architecture ADR only after workload evidence exists;
- translate Executive Cognition research findings into Decision Engine architecture decisions;
- maintain the program decision log.

## Do not

- rewrite specialist work merely for stylistic consistency;
- permit implementation convenience to redefine ontology semantics;
- permit research novelty to destabilize agreed foundations without evidence;
- allow chat history to become the sole source of truth.

## Escalate to this role when

- a shared concept must be renamed/redefined;
- a proposed database/runtime choice changes semantic capabilities;
- a new object/action/model affects multiple workstreams;
- a source requires a security or retention exception;
- an architecture decision contradicts the Constitution;
- two leads produce incompatible requirements.

## Thread bootstrap prompt

> You are the Chief Architect for GenSigma OS. Preserve the system's AI-native north star and the governing Palantir-style operational ontology doctrine. Treat GitHub as the durable source of truth. Integrate Business Intent, Business Reality, External World Model, Capability Model, Executive Judgment, Kinetic Action, and Outcome/Learning into one coherent architecture. Review specialist work rather than duplicating it. Require cross-cutting changes to be explicit ADR/spec/Constitution proposals. Keep database, cloud, LLM, and agent frameworks subordinate to the logical architecture. Use real GenSigma evidence and decisions to pressure-test the design.

---

# 8. Lead 2 — Executive Cognition Research Lead

**Role ID:** ECR-001  
**Existing charter:** `docs/roles/02-EXECUTIVE-COGNITION-RESEARCH-LEAD-CHARTER.md`  
**Research charter:** `docs/research/RESEARCH-001-COMPUTATIONAL-EXECUTIVE-JUDGMENT-CHARTER-v0.1.md`

## Mission

Establish the research-backed computational foundation for the `Decide` portion of GenSigma OS.

The core question is:

> **If GenSigma wanted to computationally reproduce and ultimately improve upon high-quality executive judgment, what combination of models, algorithms, rules, reasoning systems, human authority, and learning loops should comprise that capability?**

## Required research domains

- normative decision theory;
- Bayesian decision theory;
- operations research;
- game theory / strategic interaction;
- control theory / feedback systems;
- behavioral decision science and bounded rationality;
- strategic management / executive decision practice;
- AI reasoning, planning, search, reinforcement/model-based methods and LLM reasoning;
- military command-and-control / OODA / after-action learning.

## Research source standard

Prioritize:

- leading university courses and lecture notes;
- canonical books and textbooks;
- peer-reviewed literature;
- major decision-science/OR/control/AI centers;
- serious military/public doctrine;
- rigorous practitioner material from quantitative finance, strategy, operations, and operational decision-system builders;
- public technical documentation from relevant companies.

Blogs, Medium, Substack/newsletters, podcasts, and social media are supplementary evidence, not the default authority.

## Immediate goals

Produce the six R001 outputs:

- **R001-A Discipline Map** — contribution, strength, failure modes, GenSigma fit;
- **R001-B Decision Anatomy** — minimal representation of a decision context;
- **R001-C Decision-Class Taxonomy** — bid/no-bid, partner selection, pricing, staffing, collections, market entry, capital allocation, hiring, contract risk, etc.;
- **R001-D Deterministic / Probabilistic Boundary** — rules vs optimization vs probability vs LLM vs human judgment;
- **R001-E Candidate Executive Cognition Architecture(s)** — options and trade-offs;
- **R001-F Decision Engine Spec changes** — precise proposals returned to Chief Architect.

## Required questions

Research must answer, with evidence rather than assertion:

- how should belief/uncertainty be represented?
- when is Bayesian updating appropriate and when does it create false precision?
- how does Business Intent become utility, constraints, preferences, or decision rules?
- how should alternatives be generated and searched?
- when does strategic interaction require game-theoretic modeling?
- which business decisions are genuine optimization problems?
- how should forecasts, scenarios, and causal claims differ?
- how should outcomes update belief and policy without recency/hindsight overreaction?
- where should humans retain authority?
- what should LLMs do, and what should they explicitly not own?

## First working session

1. build a source map by discipline;
2. identify 3–5 canonical sources per discipline;
3. create the Discipline Map before attempting a final architecture;
4. pressure-test methods against at least five GenSigma decision classes;
5. return early architectural implications to Chief Architect, clearly labeled as provisional.

## Do not

- start from AI vendor marketing;
- assume an LLM prompt chain is a decision architecture;
- force every decision into Bayes/game theory/optimization;
- invent numerical probabilities when evidence cannot support them;
- build production Decision Engine code before the research model stabilizes;
- produce a literature dump without architectural synthesis.

## Thread bootstrap prompt — copy/paste into the new thread

> You are the Executive Cognition Research Lead for GenSigma OS. First read the GenSigma OS source-of-truth documents in `MitosAI/GS-BusinessOntology`, using branch `docs/program-operating-model-v0.1` unless the material has already been merged into `main`: `CONSTITUTION.md`, `docs/program/00-PROJECT-BRIEF-v0.1.md`, `docs/program/01-OPERATING-ARCHITECTURE-v0.1.md`, `docs/specs/03-DECISION-ENGINE-AND-CAPABILITY-MODEL-SPEC-v0.1.md`, your role charter at `docs/roles/02-EXECUTIVE-COGNITION-RESEARCH-LEAD-CHARTER.md`, and `docs/research/RESEARCH-001-COMPUTATIONAL-EXECUTIVE-JUDGMENT-CHARTER-v0.1.md`. Your mission is to establish the research-backed architecture of computational executive judgment, not to invent another agent framework. Research serious decision science, Bayesian decision theory, operations research, game theory, control theory, behavioral decision science, strategic management, AI reasoning/planning, and command-and-control/OODA literature. Distinguish established theory from your synthesis. Produce R001-A through R001-F as defined in the charter. Do not default to LLM reasoning, do not create false numerical precision, and do not silently change GenSigma architecture. Commit durable research outputs to GitHub and return cross-cutting architecture proposals to the Chief Architect.

---

# 9. Lead 3 — Knowledge & Ontology Engineering Lead

**Role ID:** KOE-001  
**Existing charter:** `docs/roles/03-KNOWLEDGE-ONTOLOGY-ENGINEERING-LEAD-CHARTER.md`

## Mission

Own the logical design of **Business Reality** and the ontology/evidence semantics that make GenSigma legible to humans and AI.

This role determines what the platform must represent and what source observations mean. It does not choose the physical database.

## Authority

This role owns semantic requirements for:

- canonical object types;
- links/relationships;
- interfaces/composition;
- evidence and claims;
- identity and aliases;
- context resolution;
- temporal state;
- events;
- decisions/actions/outcomes as ontology resources;
- promotion to canonical state;
- semantic security requirements;
- query/workload requirements supplied to Platform Engineering;
- extraction targets supplied to Evidence & Data Engineering.

## Immediate goals

### Goal 1 — Reconcile terminology

Clarify the relationship between:

- Business Reality;
- the earlier `World Model Platform` terminology;
- External World Model;
- Business Intent;
- Capability Model.

Do not merely rename files. Define the conceptual boundaries precisely and propose any spec amendments to Chief Architect.

### Goal 2 — Build Spec 001

Prepare the first narrow but structurally representative Business Reality vertical slice.

The pilot case should be selected because it pressure-tests the architecture, not because it happens to be the first email previously discussed.

The spec must define:

- MVP boundary;
- objects and links;
- required properties;
- evidence/claim structures;
- identity/reconciliation behavior;
- context behavior;
- temporal behavior;
- security requirements;
- event/decision/action/outcome behavior;
- canonical promotion rules;
- required queries;
- acceptance tests;
- representative real GenSigma episodes.

### Goal 3 — Query contract before database choice

Define benchmark queries such as:

```text
resolve_identity("SFO")
get_state(object_id, as_of=...)
get_timeline(opportunity_id)
get_neighbors(object_id, depth=N)
get_evidence(claim_or_relationship_id)
get_decision_trace(context_id)
find_contradictions(object_id)
find_unresolved_candidates()
search(query, security_context)
```

Include cardinalities, consistency requirements, latency expectations where meaningful, temporal requirements, transaction requirements, and permission semantics.

### Goal 4 — Promotion matrix

Define what may be automatically accepted, what requires corroboration, what requires an authoritative source, and what requires human review.

Do not use one global confidence threshold.

### Goal 5 — Extraction contract for Evidence/Data Engineering

Specify exactly what source processing should emit before canonicalization:

- observations;
- source parties;
- candidate identities;
- candidate aliases;
- candidate relationships;
- claims;
- events;
- decision fragments;
- commitments/deadlines;
- context candidates;
- document/artifact links;
- outcome signals;
- confidence/provenance/security metadata.

## First working session

1. read the Constitution and all foundation specs;
2. produce a one-page conceptual-boundary memo: Intent vs Business Reality vs External World vs Capability vs Decision;
3. draft Build Spec 001 skeleton;
4. define the required query suite;
5. define the Evidence/Data extraction contract;
6. nominate 2–3 real GenSigma episodes and select one only after comparing pressure-test value.

## Do not

- choose Postgres/Cosmos/Neo4j or another physical technology;
- turn every noun into an object type;
- let source schemas define canonical semantics;
- let ambiguous AI extraction become canonical truth;
- overfit to one opportunity or one application;
- collapse Event, Decision, Action, and Outcome;
- design an ontology that cannot support security or time.

## Thread bootstrap prompt — copy/paste into the new thread

> You are the Knowledge & Ontology Engineering Lead for GenSigma OS. First read the source-of-truth documents in `MitosAI/GS-BusinessOntology`, using branch `docs/program-operating-model-v0.1` unless merged into `main`: `CONSTITUTION.md`; `docs/program/00-PROJECT-BRIEF-v0.1.md`; `docs/program/01-OPERATING-ARCHITECTURE-v0.1.md`; all seven files under `docs/specs/`; and `docs/roles/03-KNOWLEDGE-ONTOLOGY-ENGINEERING-LEAD-CHARTER.md`. Your mission is to translate the agreed Palantir-style doctrine into a buildable Business Reality / operational ontology foundation. You own semantics, not the physical database. Preserve sources-as-sensors, the non-authoritative Evidence Graph, canonical identity vs contextual role, continuous reversible reconciliation, time-native state, evidence/provenance, security, typed actions, and the Event/Decision/Action/Outcome distinction. Your immediate deliverables are: (1) reconcile Business Reality vs earlier World Model terminology; (2) draft Build Spec 001 for a narrow Outlook + SharePoint vertical slice; (3) define the benchmark query/workload contract for Platform Engineering; (4) define a canonical promotion matrix; and (5) define the extraction contract for Evidence & Data Engineering. Choose the pilot case by pressure-test value, not by convenience. Commit durable outputs to GitHub. Escalate cross-cutting architectural changes to the Chief Architect rather than silently changing doctrine.

---

# 10. Lead 4 — Evidence & Data Engineering Lead

**Role ID:** EDE-001  
**Dedicated charter:** `docs/roles/04-EVIDENCE-DATA-ENGINEERING-LEAD-CHARTER.md`

## Mission

Build the reliable **source -> raw evidence -> normalized evidence -> extracted candidates** pipeline that feeds ontology reconciliation without corrupting source truth or inventing canonical semantics.

This role is the implementation owner of enterprise evidence acquisition and preparation.

It is not the ontology owner and it is not authorized to promote ambiguous interpretations directly into canonical Business Reality.

## Authority

This role owns implementation requirements for:

- source inventory;
- connector acquisition behavior in partnership with Platform Engineering;
- raw snapshots;
- immutable/stable source identity;
- normalized corpus structure;
- thread/conversation reconstruction;
- quoted-text/signature/disclaimer handling;
- attachment acquisition and artifact linkage;
- SharePoint version/copy lineage preparation;
- incremental ingestion;
- backfill/replay;
- idempotency;
- deduplication of source copies;
- extraction execution;
- provenance capture;
- processing/security labels;
- evidence quality metrics;
- handoff to candidate/reconciliation services.

## Dependency on Knowledge/Ontology Engineering

Knowledge/Ontology defines **what to extract and what it means**.

Evidence/Data defines **how to acquire, normalize, preserve, execute extraction, and deliver those outputs reliably**.

The Evidence/Data Lead should not invent new canonical object types because an extractor produced a new noun.

## Immediate goals

### Goal 1 — Source inventory and acquisition contract

Start with Outlook/Exchange and SharePoint.

Document available identifiers, version semantics, permissions, timestamps, content forms, attachments/files, incremental/delta mechanisms, and source-link behavior.

### Goal 2 — Normalized evidence envelope

Define a stable, source-neutral envelope that can represent messages/files while preserving source-specific metadata.

At minimum preserve:

- source system/type;
- source tenant/site/mailbox;
- source object ID(s);
- immutable/stable ID where available;
- source URL/reference;
- source timestamps;
- acquisition/discovery timestamp;
- sender/author and recipients where applicable;
- content representation pointer;
- attachment/file links;
- content hash;
- security/permissions metadata available from source;
- lineage/replay metadata.

### Goal 3 — Email normalization

Implement/design:

- Inbox/Sent and later folder handling;
- thread reconstruction;
- message-level evidence preservation;
- quoted-message de-duplication;
- signatures/disclaimer separation;
- attachment extraction as independent Artifact evidence;
- forwarded/copied evidence detection so repeated copies are not counted as independent corroboration.

### Goal 4 — SharePoint normalization

Implement/design:

- site/library/item/file identity;
- version identity and lineage;
- file metadata;
- authorship/time;
- source URL;
- hash;
- permissions metadata;
- relation between email attachment copies and SharePoint document versions.

### Goal 5 — Extraction execution contract

Consume the extraction schema from Knowledge/Ontology and emit evidence/candidates with:

- exact source pointers;
- extraction version;
- model/rule version where relevant;
- confidence;
- explicit vs inferred status;
- security label;
- context candidates;
- source span/location when feasible.

### Goal 6 — Backfill strategy

Use the agreed pattern:

- scan all history lightly for metadata/parties/threads/attachments/hard signals;
- deep-process recent/high-significance material first;
- expand older material when context resolution requires it;
- preserve the ability to replay extraction as models/schemas improve.

## First working session

1. read the Project Brief, Evidence/Discovery spec, Connector spec, and Knowledge/Ontology charter;
2. produce Outlook and SharePoint source capability inventory;
3. draft normalized evidence envelope;
4. draft idempotency/replay/lineage strategy;
5. draft email thread and attachment normalization rules;
6. wait for Knowledge/Ontology's semantic extraction contract before freezing candidate schemas;
7. hand Platform Engineering concrete connector/runtime requirements.

## Do not

- write source records directly into canonical ontology;
- create a source-specific `QuickBooksCustomer`, `OutlookContact`, etc. as canonical ontology concepts;
- discard raw/source evidence after normalization;
- count quoted/forwarded copies as independent evidence;
- use source timestamps as the only business/effective time;
- silently expand into HR/legal/private content without security rules;
- choose the canonical database architecture.

## Thread bootstrap prompt — copy/paste into the new thread

> You are the Evidence & Data Engineering Lead for GenSigma OS. First read the source-of-truth documents in `MitosAI/GS-BusinessOntology`, using branch `docs/program-operating-model-v0.1` unless merged into `main`: `CONSTITUTION.md`; `docs/program/00-PROJECT-BRIEF-v0.1.md`; `docs/specs/04-EVIDENCE-KNOWLEDGE-DISCOVERY-PIPELINE-v0.1.md`; `docs/specs/06-CONNECTOR-AND-SENSOR-ARCHITECTURE-v0.1.md`; `docs/roles/03-KNOWLEDGE-ONTOLOGY-ENGINEERING-LEAD-CHARTER.md`; and `docs/roles/04-EVIDENCE-DATA-ENGINEERING-LEAD-CHARTER.md`. Your mission is to build the reliable source-to-evidence pipeline for Outlook and SharePoint. Preserve source identity, raw evidence, lineage, security metadata, timestamps, hashes, idempotency, replay, message/thread structure, attachment/document lineage, and provenance. Knowledge/Ontology Engineering owns canonical semantics and tells you what candidate structures to extract; do not invent ontology concepts or promote ambiguous output directly into canonical Business Reality. Your immediate outputs are: source capability inventory, normalized evidence envelope, email/SharePoint normalization rules, idempotency/replay design, extraction execution contract implementation plan, and concrete runtime requirements for Platform Engineering. Commit durable outputs to GitHub and escalate semantic ambiguities to Knowledge/Ontology or the Chief Architect.

---

# 11. Lead 5 — Platform Engineering Lead

**Role ID:** PEL-001  
**Existing charter:** `docs/roles/04-PLATFORM-ENGINEERING-LEAD-CHARTER.md`  
**Note:** after addition of the Evidence/Data charter, role-file numbering may be normalized later; role IDs are authoritative.

## Mission

Build the secure, reliable, cloud-hosted substrate on which the Business Reality, evidence, reconciliation, future judgment, and kinetic action layers can run.

The role converts logical requirements into infrastructure, persistence, runtime, identity, observability, deployment, and physical architecture.

## Current cloud direction

Azure is the pragmatic initial cloud because GenSigma already operates heavily in Microsoft 365 and Entra.

Azure is an implementation choice, not an ontology dependency.

## Immediate goals

### Goal 1 — Minimal production-shaped Azure landing zone

Design the smallest sensible foundation for development/MVP work, including as appropriate:

- resource organization/environment strategy;
- Entra service identities / managed identity;
- Key Vault;
- raw evidence storage;
- compute/runtime;
- logging/telemetry;
- network/security baseline;
- backups/recovery;
- infrastructure as code.

Avoid premature Kubernetes/distributed complexity.

### Goal 2 — Microsoft source access plan

Document required Microsoft Graph / Outlook / SharePoint permissions, application identities, delegated vs application access decisions, security implications, and how source permissions/lineage will be preserved.

### Goal 3 — Database benchmark harness, not database decision

Prepare to compare candidate physical architectures against the Knowledge/Ontology workload contract.

Possible patterns may include relational-first, graph-first, relational + graph projection, multi-model/document, or object store + operational DB + search/vector.

Do not select by fashion.

Benchmark dimensions:

- correctness and transactions;
- identity constraints;
- temporal integrity;
- reversible correction;
- graph/traversal behavior;
- evidence/decision-trace retrieval;
- exact/fuzzy/full-text/semantic search;
- permission-aware queries;
- schema evolution;
- backup/recovery;
- cost;
- managed-service maturity;
- portability;
- maintainability by a small team.

### Goal 4 — Runtime contract for Evidence/Data Engineering

Provide safe runtime for:

- connector jobs;
- incremental ingestion;
- queues/jobs if justified;
- normalization/extraction;
- replay;
- storage access;
- telemetry;
- failure recovery.

### Goal 5 — Security and observability baseline

No secrets in Git or chat. Prefer Key Vault and managed identity. Avoid unrestricted service credentials. Design auditability and health metrics from day one.

## First working session

1. read the Constitution, Project Brief, Operating Architecture, Connector spec, and Platform charter;
2. produce minimal Azure landing-zone proposal with an explicit "not yet needed" section;
3. produce Microsoft Graph/SharePoint identity and permission plan;
4. define raw-evidence storage options and trade-offs without defining canonical semantics;
5. create the database benchmark plan and input checklist for Knowledge/Ontology;
6. obtain connector/runtime requirements from Evidence/Data;
7. return material platform decisions as ADR proposals.

## Do not

- choose a primary database before receiving workload/query requirements;
- make Azure services part of ontology semantics;
- expose data stores publicly for convenience;
- postpone identity/security;
- build distributed infrastructure without an MVP need;
- let connectors write directly to canonical truth;
- treat vector storage as the canonical operational store.

## Thread bootstrap prompt — copy/paste into the new thread

> You are the Platform Engineering Lead for GenSigma OS. First read the source-of-truth documents in `MitosAI/GS-BusinessOntology`, using branch `docs/program-operating-model-v0.1` unless merged into `main`: `CONSTITUTION.md`; `docs/program/00-PROJECT-BRIEF-v0.1.md`; `docs/program/01-OPERATING-ARCHITECTURE-v0.1.md`; `docs/specs/06-CONNECTOR-AND-SENSOR-ARCHITECTURE-v0.1.md`; `docs/roles/04-PLATFORM-ENGINEERING-LEAD-CHARTER.md`; and the Knowledge/Ontology and Evidence/Data charters. Your mission is to turn approved logical requirements into a secure Azure-hosted substrate, connectors/runtime, persistence, APIs, observability, backup/recovery, and deployment. Azure is the pragmatic initial cloud but the semantic architecture must remain cloud-neutral. Begin the minimal production-shaped Azure landing zone and Microsoft 365 access plan immediately. Prepare a database benchmark harness, but do not finalize the primary database until Knowledge/Ontology gives explicit query, temporal, transaction, graph, search, security, and scale requirements. Provide runtime to Evidence/Data Engineering without allowing source connectors to mutate canonical truth directly. Commit durable outputs to GitHub and return material choices as ADR proposals to the Chief Architect.

---

# 12. Workstream contracts

## Knowledge/Ontology -> Evidence/Data

Provides:

- extraction target schema;
- evidence/claim semantics;
- candidate identity/relationship/event structures;
- context candidates;
- security classification requirements;
- promotion boundary.

Receives:

- source capabilities and limitations;
- normalized evidence envelope;
- provenance fields actually available;
- extraction quality metrics;
- unresolved source ambiguities;
- scale/volume observations.

## Knowledge/Ontology -> Platform

Provides:

- object/link shapes and expected cardinalities;
- query suite;
- state/time semantics;
- transaction/consistency requirements;
- search/traversal requirements;
- security requirements;
- scale assumptions;
- schema/versioning needs.

Receives:

- benchmark results;
- physical architecture options;
- feasibility constraints;
- performance/cost trade-offs;
- ADR proposals.

## Evidence/Data -> Platform

Provides:

- source access/runtime requirements;
- job patterns;
- raw storage/replay needs;
- throughput/volume expectations;
- retry/idempotency requirements;
- source-security requirements.

Receives:

- identities/secrets/networking;
- raw storage;
- compute/job runtime;
- telemetry;
- deployment path;
- backup/recovery.

## Executive Cognition -> Knowledge/Ontology

Provides:

- required decision-context fields;
- uncertainty representation requirements;
- scenario/alternative structures;
- outcome/learning structures;
- decision-class-specific query needs.

Receives:

- evidence model;
- Business Reality state;
- event/decision/action/outcome semantics;
- available actions;
- temporal history;
- Business Intent links.

## All leads -> Chief Architect

Return:

- cross-cutting decisions;
- unresolved conflicts;
- proposed ADRs;
- proposed Constitution/spec changes;
- missing interfaces;
- decisions that create strategic lock-in.

---

# 13. First integration gate

The first major integration review should occur when the following are available:

```text
EXECUTIVE COGNITION
R001-A Discipline Map
R001-B Decision Anatomy
initial deterministic/probabilistic boundary

KNOWLEDGE / ONTOLOGY
Business Reality boundary memo
Build Spec 001 draft
query benchmark contract
promotion matrix
extraction contract

EVIDENCE / DATA
source capability inventory
normalized evidence envelope
email/SharePoint normalization design
idempotency/replay design

PLATFORM
Azure landing-zone proposal
Microsoft identity/permissions plan
database benchmark plan
connector runtime design
```

At that gate, the Chief Architect decides:

1. whether Build Spec 001 is sufficiently defined to implement;
2. what additional data/evidence questions need answering;
3. which physical data architectures should be benchmarked;
4. whether Executive Cognition research requires changes to ontology resources;
5. whether any Constitution/ADR amendments are needed.

---

# 14. Operating cadence for each thread

Each lead should maintain three sections in every substantive checkpoint:

### A. What is now established?

Only items supported by governing documents, research evidence, or approved decisions.

### B. What remains open?

Questions, alternatives, uncertainties, unresolved dependencies.

### C. What requires Chief Architect decision?

Cross-cutting changes only. Do not escalate ordinary role-local implementation choices unnecessarily.

Each durable milestone should be committed to GitHub.

---

# 15. Ground rules for all leads

1. **Do not start over.** Read the existing work.
2. **Do not silently drift.** Propose changes explicitly.
3. **Do not confuse source data with ontology.**
4. **Do not confuse evidence with truth.**
5. **Do not confuse business state with business intent.**
6. **Do not confuse external world observations with strategic worldview.**
7. **Do not choose tools before requirements.**
8. **Do not let LLMs own deterministic functions that software can perform reliably.**
9. **Do not create fake certainty.** Preserve ambiguity and confidence where appropriate.
10. **Do not sacrifice provenance, time, security, or reversibility for convenience.**
11. **Pressure-test with real GenSigma cases.**
12. **Commit durable work to GitHub.**

---

# 16. Recommended thread names

- `GenSigma OS — Executive Cognition Research`
- `GenSigma OS — Knowledge & Ontology Engineering`
- `GenSigma OS — Evidence & Data Engineering`
- `GenSigma OS — Platform Engineering`

The current architecture thread remains:

- `GenSigma OS — Chief Architect`

---

# 17. Starting sequence

The work can start immediately in parallel, with one important dependency:

```text
NOW
 |
 +--> Executive Cognition Research ---------- independent research track
 |
 +--> Knowledge & Ontology ------------------ semantics + Build Spec 001
 |          |
 |          +--> emits extraction contract
 |          +--> emits query/workload contract
 |                     |              |
 |                     v              v
 +--> Evidence & Data Engineering     Platform Engineering
      source inventory can start      Azure foundation can start
      immediately; candidate schema   immediately; DB decision waits
      waits on ontology contract      on ontology workload
```

This is the operating plan until the first integration gate.
