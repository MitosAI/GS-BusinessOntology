# GenSigma OS — Master Execution Plan

**Version:** v0.1  
**Status:** BASELINED program execution plan  
**Owner:** CA-001 — Chief Architect  
**Delivery integrator:** PEL-001 — Platform Engineering Lead  
**Contributors:** KOE-001, EDE-001, ECR-001  
**Governing sources:** `CONSTITUTION.md`, `AGENTS.md`, `docs/program/00-PROJECT-BRIEF-v0.1.md`, accepted ADRs, Build Specs, architecture contracts, workstream charters  
**Execution system:** GitHub = durable knowledge and code; Linear = live execution state; Codex = bounded implementation workforce

---

## 1. Purpose

This document is the canonical program map for building the GenSigma AI-Native Operating System.

It exists to answer five questions at all times:

1. What are we building?
2. What is already decided versus still open?
3. What major projects and milestones remain?
4. What is executing now, what is next, and what is blocked?
5. How does any Linear issue or Codex task trace back to the architecture and program plan?

This is not a giant frozen task list. It is a **baselined rolling-wave master plan**: stable at the architectural and program levels, progressively more detailed near execution, and explicitly change-controlled when evidence requires adaptation.

---

## 2. North Star

> **Build the operating brain of GenSigma, not an AI assistant sitting beside GenSigma.**

The target system is a governed operating layer in which Business Intent, Business Reality, External World beliefs, Capability, Executive Judgment, Governed Action, Outcomes and Learning operate through one coherent architecture.

```text
BUSINESS INTENT
      +
BUSINESS REALITY
      +
EXTERNAL WORLD MODEL
      +
CAPABILITY MODEL
      |
      v
EXECUTIVE JUDGMENT / DECISION ENGINE
      |
      v
GOVERNED ACTION
      |
      v
NEW BUSINESS REALITY
      |
      v
OUTCOME / LEARNING
```

The five-dimensional operational frame remains:

1. WORLD
2. TEMPORAL / EVENT
3. DECISION
4. KINETIC
5. OUTCOME / LEARNING

Cross-cutting: Evidence, Provenance, Security, Authority, Time, Confidence and Governance.

---

## 3. Planning doctrine

GenSigma OS uses a hybrid startup/agentic engineering model:

```text
STABLE INTENT
  -> STABLE ARCHITECTURAL CONSTRAINTS
  -> LONG-RANGE PROGRAM MAP
  -> ROLLING-WAVE PROJECT PLANNING
  -> SHAPED MILESTONE
  -> SMALL READY ISSUE
  -> CODEX IMPLEMENTATION
  -> PR / CI / REVIEW
  -> WORKING SOFTWARE
  -> LEARNING
  -> CONTROLLED PLAN UPDATE
```

### 3.1 Planning horizons

| Horizon | Artifact | Detail level | Expected mutability |
|---|---|---|---|
| Years | Constitution / Project Brief | mission, doctrine, invariants | extremely low |
| 6–18 months | Master Execution Plan | major projects, dependencies, gates | controlled |
| 1–4 months | Linear Projects / Build Specs | outcomes, milestones, major interfaces | moderate |
| 2–6 weeks | Linear Milestones | detailed deliverables and acceptance | low once started |
| 1–10 days | Linear Issues | bounded execution contract | frozen once READY |
| Hours–days | Codex task / branch / PR | implementation | constrained by issue |

### 3.2 No false precision

The complete architecture and program map should be visible now, but coding tasks are elaborated only when they are close enough to execution to be accurate.

Future milestones may remain coarse until research, benchmarks or earlier implementation resolves uncertainty.

---

## 4. Change-control model

Not all artifacts are equally mutable.

### Level A — Constitutional / very stable

- Constitution
- North-star mission
- primary architectural doctrine
- accepted top-level invariants

**Change rule:** explicit amendment / VJ + CA-001 architectural approval.

### Level B — Accepted architecture / stable

- accepted ADRs
- inter-layer contracts
- canonical semantic invariants
- security/authority/time/provenance rules
- approved Build Spec baselines

**Change rule:** do not silently rewrite. Create an architecture request and either amend under explicit decision or supersede with a new ADR/version.

### Level C — Master program / controlled

- this Master Execution Plan
- project boundaries
- milestone dependency structure
- architecture gates

**Change rule:** CA-001 owns material changes. Every material change gets a dated entry in the Change Log with rationale and affected projects.

### Level D — Workstream/project plan / adaptive

- project sequencing
- detailed technical design within approved boundaries
- milestone decomposition

**Change rule:** lead may update under LOCAL_SOLVE if shared architecture does not change.

### Level E — READY issue / frozen

Once a Linear issue is `READY` for Codex, these are frozen for that execution:

- objective
- scope / non-scope
- governing contracts
- acceptance criteria
- tests
- architecture boundary

If new information invalidates the issue, stop/supersede it; do not quietly mutate the contract underneath an active worker.

---

## 5. Execution states

Every material deliverable uses these planning states:

```text
DRAFT
  -> SHAPED
  -> APPROVED
  -> BASELINED
  -> READY
  -> IN EXECUTION
  -> IN REVIEW
  -> VERIFIED
  -> DONE
```

Optional terminal state: `SUPERSEDED`.

A deliverable may move backward only with explicit rationale.

---

## 6. READY gate for Codex

A coding issue may be delegated only when all applicable checks pass:

- [ ] desired system/user behavior is explicit;
- [ ] architecture is settled enough for the scope;
- [ ] required benchmark/research is complete;
- [ ] governing GitHub artifacts are linked;
- [ ] dependencies are satisfied;
- [ ] scope is bounded;
- [ ] non-scope is explicit;
- [ ] acceptance criteria are testable;
- [ ] tests/fitness checks are specified;
- [ ] security/provenance/time implications are understood;
- [ ] LOCAL_SOLVE versus ASK_ARCHITECT boundary is explicit;
- [ ] task is small enough for a bounded coding session.

If any material check fails, the issue remains SHAPED/BLOCKED rather than being handed to Codex prematurely.

---

# 7. Program structure

The top-level Linear Initiative should mirror this program:

**GenSigma OS — AI-Native Operating System**

The Initiative contains the following major projects.

---

# P1 — Architecture & Shared Contracts

**Owner:** CA-001  
**Purpose:** maintain the shared architecture, canonical contracts and decision boundaries that allow the specialist workstreams to evolve independently without drift.

## Milestones

### P1.M1 — Governance baseline — DONE / substantially complete
- Constitution
- AGENTS.md
- role charters
- escalation standard
- delivery standard
- CA decision method
- architecture fitness model

### P1.M2 — Shared architecture baseline — IN PROGRESS
- Business Intent / Business Reality / External World / Capability boundaries
- five-dimensional ontology frame
- inter-layer contracts
- shared time/provenance/security/authority semantics
- DecisionContext seam
- action/outcome/learning seams

### P1.M3 — Architecture consistency closure — NEXT
- resolve known contradictions in old specs/ADRs;
- retire stale World Model naming where appropriate;
- reconcile object-count guardrail question;
- ensure Build Specs and workstream contracts point to current accepted architecture.

### P1.M4 — Architecture fitness automation — PLANNED
- machine-checkable invariants where practical;
- CI enforcement for contract drift;
- acceptance traceability from ADR/Build Spec to tests.

**Exit:** specialists can execute without silent cross-workstream reinterpretation.

---

# P2 — Business Reality Foundation

**Owners:** KOE-001 (semantics), PEL-001 (runtime)  
**Purpose:** make the governed operational world model executable.

## Current baseline

- KOE semantic foundation merged to `main`;
- executable Business Reality reference kernel merged to `main`;
- evidence -> candidate -> governed promotion path exists;
- canonical correction/history exists;
- type compatibility and contract resolution gaps closed.

## Milestones

### P2.M1 — Semantic kernel — DONE
- canonical resource/ref contracts;
- evidence/candidate/promotion invariants;
- deterministic contract registry;
- non-destructive correction/history;
- promotion lineage.

### P2.M2 — Typed relationships — IN EXECUTION
- runtime TypedRelationship support;
- participant/contextual-role validation;
- relationship state and scope;
- evidence lineage;
- correction/history tests.

Current Linear seed issue: `GEN-5`.

### P2.M3 — Temporal / as-of state — NEXT
- effective-time aware state reads;
- relationship effective intervals;
- historical state reconstruction;
- no projection of later facts backward;
- correction versus effective history.

### P2.M4 — Security-context enforcement — NEXT
- caller/security context on reads;
- evidence/resource filtering;
- no restricted-data leakage through traversal/search;
- agent identities governed like humans.

### P2.M5 — Query / Context API — PLANNED
- get_object;
- get_state;
- get_relationships;
- get_neighbors;
- get_timeline;
- get_evidence;
- get_claims;
- get_decision_trace;
- contradiction/reconciliation queries;
- search seam.

### P2.M6 — Identity & Context Reconciliation runtime — PLANNED
- alias handling;
- same/related/distinct outcomes;
- unresolved candidates;
- merge/split proposal semantics;
- contextual shorthand;
- evidence-weighted reconciliation.

### P2.M7 — Production persistence handoff — GATED
Triggered only after representative workloads, temporal/security semantics and query contracts are executable enough to benchmark physical architecture.

---

# P3 — Evidence & Enterprise Discovery

**Owner:** EDE-001  
**Semantic partner:** KOE-001  
**Runtime partner:** PEL-001

## Milestones

### P3.M1 — Evidence contracts — DONE / substantially complete
- RawEvidence;
- Observation;
- Candidate;
- provenance;
- source-as-sensor doctrine;
- replay/idempotency requirements.

### P3.M2 — Outlook sensor — READY TO SHAPE
- bounded mailbox/folder/time-window acquisition;
- stable source identifiers;
- message/thread metadata;
- body/attachment strategy;
- immutable raw capture;
- source security metadata;
- incremental cursor/change tracking;
- replay and idempotency tests.

### P3.M3 — SharePoint sensor — READY TO SHAPE
- site/library/file/version identity;
- metadata/security;
- content hashing;
- source lineage;
- version reconciliation;
- attachment-to-SharePoint document matching.

### P3.M4 — Normalization layer — PLANNED
- normalized message/document/artifact shapes;
- quoted/forwarded duplicate handling;
- normalized party/text observations;
- raw lineage preservation.

### P3.M5 — Candidate extraction / Evidence Graph — PLANNED
- entity/relationship/context/event candidates;
- claim/commitment/decision/action/outcome fragments;
- extraction/model provenance;
- confidence/epistemic status;
- no direct canonical mutation.

### P3.M6 — Reconciliation queues & drift detection — PLANNED
- unresolved review queues;
- evidence conflict handling;
- continuous discovery drift proposals;
- merge/split review support.

---

# P4 — Platform & Production Architecture

**Owner:** PEL-001

## Milestones

### P4.M1 — Reference runtime — DONE / substantially complete
- executable in-memory kernel;
- CI-backed invariant tests;
- deterministic contract loading;
- bounded implementation substrate.

### P4.M2 — Workload benchmark harness — NEXT
- identity lookup;
- 1–3 hop traversals;
- temporal state reads;
- evidence lineage;
- security-aware search/traversal;
- canonical promotion/correction;
- representative scale assumptions.

### P4.M3 — Physical persistence ADR — GATED
Evaluate measured candidates only after P2/P3 requirements are concrete.

Candidate categories may include:
- relational-first;
- graph-first;
- relational + graph projection;
- operational DB + object storage + search/vector;
- Azure-native multi-model combinations.

### P4.M4 — Azure secure foundation — PLANNED
- resource organization;
- Entra identities;
- managed identity/service principals;
- Key Vault;
- raw evidence storage;
- compute/runtime;
- environment separation;
- logging/monitoring;
- infrastructure as code.

### P4.M5 — Production service/runtime — PLANNED
- persistence adapters;
- API runtime;
- retry/recovery;
- dead-letter/error handling;
- observability;
- deployment pipeline.

---

# P5 — Security & Governance

**Architecture owner:** CA-001  
**Implementation owner:** PEL-001  
**Domain contributions:** KOE-001 / EDE-001

## Milestones

### P5.M1 — Security semantics — IN PROGRESS
- security classes;
- object/evidence access semantics;
- authority/delegation model;
- agent identity treatment;
- promotion cannot widen access silently.

### P5.M2 — Runtime authorization — PLANNED
- caller context;
- policy checks;
- denied traversal/search leakage tests;
- action authorization.

### P5.M3 — Audit & approval fabric — PLANNED
- actors/approvers;
- decision/action audit chains;
- approval gates;
- security-denial telemetry.

---

# P6 — Executive Cognition / Decision Engine

**Owner:** ECR-001

## Milestones

### P6.M1 — Research 001 foundation — IN PROGRESS
- normative decision theory;
- Bayesian reasoning;
- OR/optimization;
- game theory;
- control theory;
- behavioral decision science;
- strategic/executive judgment;
- AI reasoning/planning;
- OODA/C2.

### P6.M2 — Decision architecture baseline — IN PROGRESS
Preserve ADR-003 direction unless superseded:
- hierarchical policy portfolio;
- deterministic governance shell;
- decision-class routing;
- modular Bayes/optimization/scenario/game theory;
- LLM as component, not entire engine;
- challenge/sensitivity;
- governed action/outcome learning.

### P6.M3 — DecisionContext contract — NEXT
Inputs from Business Reality / Intent / Capability / External World;
uncertainty, available actions, constraints, authority and rationale requirements.

### P6.M4 — Bid / No-Bid prototype — PLANNED
First bounded computational decision class.

### P6.M5 — Staffing / Resource Assignment prototype — PLANNED
Second bounded decision class with stronger optimization characteristics.

---

# P7 — Kinetic Action & Learning

**Architecture:** CA-001 + ECR-001  
**Runtime:** PEL-001

## Milestones

### P7.M1 — Typed action contract — PLANNED
- named business actions;
- preconditions;
- authorization;
- approvals;
- idempotency;
- result verification.

### P7.M2 — First low-risk action — PLANNED
Candidate examples:
- create follow-up task;
- request missing evidence;
- draft partner outreach;
- create opportunity workspace;
- controlled internal status update.

### P7.M3 — Outcome & verification fabric — PLANNED
- execution result vs business outcome;
- verification events;
- state update;
- audit chain.

### P7.M4 — Learning loop — PLANNED
- observed outcome;
- policy/model feedback;
- governed updates;
- no uncontrolled self-modification.

---

# P8 — First End-to-End GenSigma Operating Loop

**Owners:** CA-001 integration; PEL-001 delivery; all specialist leads contribute.

**Goal:** prove one real operating loop using representative GenSigma evidence.

## Milestones

### P8.M1 — Episode selection & fixture — SHAPED
Choose a rich RFP-to-cash or comparable episode based on evidence richness, ambiguity, relationships, temporal span, decision trace, action/outcome evidence, security and available ground truth.

### P8.M2 — Evidence -> Business Reality — PLANNED
- ingest real bounded source evidence;
- normalize;
- produce evidence graph;
- reconcile identity/context;
- promote canonical Business Reality.

### P8.M3 — Decision reconstruction — PLANNED
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
Explicit vs inferred distinctions must remain visible.

### P8.M4 — Computational recommendation — PLANNED
Use P6 DecisionContext/decision architecture to produce an auditable recommendation.

### P8.M5 — Governed action — PLANNED
Execute one low-risk typed action through P7 controls.

### P8.M6 — Verified outcome / learning — PLANNED
Close the first complete loop and feed results into the next planning wave.

---

## 8. Dependency graph

```text
P1 Architecture & Shared Contracts
   |-------------------------------|
   v                               v
P2 Business Reality            P6 Executive Cognition
   |                               |
   +-----------+-------------------+
               v
P8 End-to-End Operating Loop

P3 Evidence & Discovery ---> P2 Business Reality
       |                       |
       +----------+------------+
                  v
             P4 Platform
                  |
                  v
             P5 Security

P6 Decision Engine + P2 Reality + P5 Governance
                  |
                  v
             P7 Kinetic Action
                  |
                  v
             P8 Full Loop
```

This is a dependency map, not a waterfall. Independent work proceeds in parallel where contracts permit.

---

## 9. Architecture / research gates

The following choices remain intentionally gated:

### Gate G1 — Production persistence
Do not select until representative temporal, traversal, security, search, lineage and canonical-write workloads are executable and benchmarkable.

### Gate G2 — Exact identity-resolution algorithm
Do not freeze until real evidence fixtures and false-merge/false-split tests exist.

### Gate G3 — Decision engine method per decision class
Route by decision type; do not impose one universal LLM or optimization method.

### Gate G4 — Runtime agent framework
Do not select as the foundation of Business Reality. Decide later from durable workflow/wakeup/approval/operational requirements.

### Gate G5 — Broad autonomous kinetic actions
Do not enable until typed action, authority, approval, idempotency, verification and audit are proven.

---

## 10. Current execution wave — Wave 1

**Goal:** make the Business Reality kernel capable of representing governed relationships, time, security and usable context while the next Evidence and Cognition increments are shaped in parallel.

### IN EXECUTION
- P2.M2 Typed relationships — Linear `GEN-5`.

### SHAPE NEXT / highest priority
1. P2.M3 Temporal / as-of reads.
2. P2.M4 Security-context enforcement.
3. P2.M5 Query/context API.
4. P3.M2 Outlook sensor task decomposition.
5. P3.M3 SharePoint sensor task decomposition.
6. P4.M2 workload benchmark harness.
7. P6.M3 DecisionContext contract.

### PARALLEL RESEARCH / ARCHITECTURE
- ECR Research 001 and DecisionContext;
- KOE identity/context/temporal/security pressure tests;
- EDE connector and evidence-lineage design;
- CA shared architecture contradiction cleanup.

### Blocker
Codex delegation through Linear depends on the Codex integration/delegate being available in the Linear workspace. Issue creation and shaping continue independently of that connection.

---

## 11. Wave 2 — Real evidence and production architecture

Triggered when Wave 1 kernel semantics are sufficiently executable.

Expected scope:
- Outlook ingestion;
- SharePoint ingestion;
- normalization;
- Evidence Graph/candidate extraction;
- identity/context reconciliation runtime;
- query API integration;
- benchmark harness execution;
- physical persistence ADR;
- Azure secure substrate.

---

## 12. Wave 3 — Decision and kinetic loop

Expected scope:
- first historical decision reconstruction;
- DecisionContext integration;
- Bid/No-Bid computational prototype;
- first typed low-risk action;
- verification/outcome recording;
- end-to-end RFP-to-cash or comparable operating loop.

---

## 13. Linear mapping standard

Linear mirrors this plan; it does not replace or redefine it.

```text
MASTER EXECUTION PLAN
        |
        v
LINEAR INITIATIVE
GenSigma OS — AI-Native Operating System
        |
        v
LINEAR PROJECT
P1..P8 major bodies of work
        |
        v
LINEAR MILESTONE
P?.M? execution stage
        |
        v
LINEAR ISSUE
small bounded deliverable
        |
        v
CODEX SESSION
implementation against frozen issue contract
        |
        v
GITHUB PR + CI
        |
        v
REVIEW / MERGE
        |
        v
LINEAR STATUS + MASTER PLAN PROGRESS
```

Every material implementation issue should carry a reference such as:

`Master Plan: P2.M3`  
`Governing Build Spec/ADR: ...`  
`Workstream owner: ...`

---

## 14. Codex execution model

Codex is a bounded implementation worker, not an architect or source of truth.

### Flow

1. Lead shapes issue.
2. Issue passes READY gate.
3. Issue is delegated to Codex.
4. Codex reads `AGENTS.md` + explicitly linked governing artifacts.
5. Codex works in an isolated branch/environment.
6. Codex runs specified tests/lint/build.
7. Codex opens or prepares a PR.
8. Domain lead reviews correctness.
9. CI/fitness checks run.
10. Merge only when acceptance criteria are satisfied.
11. Linear issue moves to VERIFIED/DONE.
12. Dependent issue unblocks.

### Codex must stop/escalate rather than invent if it encounters
- contradictory shared architecture;
- missing semantic definition;
- security/authority ambiguity;
- time/provenance contradiction;
- hard-to-reverse infrastructure choice not already approved.

---

## 15. Progress reporting

VJ should be able to inspect one Initiative and answer:

- overall project progress;
- current milestones;
- issues executing now;
- blockers;
- active Codex sessions;
- PRs waiting for review;
- latest verified capability.

The weekly delivery summary should use exactly these headings:

```text
NOW BUILDING
NEXT
BLOCKED
CODEX ACTIVE
PRS IN REVIEW
VERIFIED THIS WEEK
ARCHITECTURE CHANGES
PLAN CHANGES
```

No percentage should be treated as meaningful unless it is backed by milestone/issue completion, not narrative estimation alone.

---

## 16. Program success gates

### Gate A — Trustworthy Business Reality
Evidence-backed, correctable, temporal, secure, queryable canonical state from real sources.

### Gate B — Computational Judgment
At least one decision class produces an auditable recommendation using explicit state, intent, uncertainty, alternatives and decision criteria.

### Gate C — Governed Kinetic Loop
At least one typed action is authorized, executed, verified, recorded and reflected in new Business Reality.

### Gate D — Learning
Observed outcomes can update future assessments/policies through governed mechanisms.

### Gate E — Domain scalability
The architecture can expand into commercial, delivery, finance, workforce, systems/assets and compliance without spawning disconnected semantics.

---

## 17. Decision status

### DECIDED
- GitHub is durable engineering knowledge/source of truth.
- Linear is live work state, dependencies, milestones and execution visibility.
- Codex is bounded implementation workforce.
- CA-001 owns cross-cutting architecture.
- Specialist agents own their domains.
- Palantir-style operational ontology doctrine governs semantics.
- Discovery observes/proposes; ontology defines/governs.
- Source systems are sensors, not ontology branches.
- Material canonical writes are governed and auditable.
- Build in thin real end-to-end slices.
- Benchmark first for material architecture/technology decisions.
- READY issues freeze execution scope/acceptance/tests.

### TENTATIVE / ACTIVE DESIGN
- exact minimum first production object set;
- exact DecisionContext schema;
- first end-to-end episode selection;
- exact security classification taxonomy.

### OPEN / GATED
- production persistence architecture;
- graph vs relational primary model;
- vector/search architecture;
- exact Azure service set;
- exact identity-resolution algorithms;
- runtime agent framework;
- broad autonomy levels;
- exact kinetic runtime.

---

## 18. Change log

### v0.1 — Baselined
- Established one canonical Master Execution Plan.
- Adopted rolling-wave planning and explicit mutability levels.
- Defined P1–P8 program structure.
- Defined READY gate and frozen execution-contract rule.
- Mapped GitHub -> Linear -> Codex -> PR/CI -> verified capability.
- Set Wave 1 around typed relationships, time, security, query context, evidence sensor shaping, platform benchmarks and DecisionContext.

Future material plan changes must add a dated entry here describing:
- what changed;
- why;
- evidence/decision that justified the change;
- affected projects/milestones;
- whether any active issues are superseded.
