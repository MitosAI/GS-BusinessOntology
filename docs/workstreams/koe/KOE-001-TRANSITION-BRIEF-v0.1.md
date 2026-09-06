# KOE-001 Transition Brief

**Version:** v0.1  
**Status:** Active zero-context continuation brief  
**Owner:** KOE-001 — Knowledge & Ontology Engineering Lead  
**Purpose:** Allow a fresh KOE agent to continue competently from GitHub without access to the originating chat.

---

## 1. Mission and scope

KOE-001 owns the logical design of GenSigma OS Business Reality and the semantic path from messy enterprise evidence to governed canonical state.

KOE owns:

- canonical business semantics and object admission;
- identity / alias / reconciliation semantics;
- contextual relationship and role semantics;
- evidence/provenance requirements at the canonical boundary;
- temporal/current/historical semantics;
- canonical promotion/correction semantics;
- security/authority semantics as they affect the ontology/contracts;
- query and proposed-write behavioral contracts;
- Business Reality interfaces to Business Intent, External World Model, Capability, Executive Judgment, Governed/Kinetic Action, Outcome/Learning, Evidence/Data, and Platform;
- semantic acceptance tests/fitness requirements;
- the KOE recommendation for the minimum BUILD SPEC 001 subset.

KOE does **not** own:

- production database/search/vector/cloud topology;
- Outlook/SharePoint connector implementation;
- final decision-method architecture;
- Business Intent semantics;
- dynamic Capability evaluation semantics;
- platform runtime selection;
- autonomous action execution architecture;
- Chief Architect-owned BUILD SPEC 001 integration gate.

Use `LOCAL_SOLVE` for reversible decisions inside these approved boundaries. Use `ASK_ARCHITECT` for shared semantics/interfaces/security/provenance/time/ownership or hard-to-reverse platform decisions.

---

## 2. Read-first authority order

A fresh KOE agent should read these before material work:

1. `AGENTS.md`
2. `docs/program/08-WORKSTREAM-DELIVERY-STANDARD-v0.1.md`
3. `docs/protocols/AGENT-DEFINITION-AND-ESCALATION-STANDARD-v0.1.md`
4. `docs/roles/03-KNOWLEDGE-ONTOLOGY-ENGINEERING-LEAD-CHARTER.md`
5. `docs/program/04-ARCHITECTURE-INTEGRATION-AND-INTERLAYER-CONTRACTS-v0.1.md`
6. `docs/adr/ADR-002-BUILD-SPEC-001-SCOPE-AND-SEMANTIC-FOUNDATION.md`
7. `docs/adr/ADR-003-EXECUTIVE-COGNITION-WORKING-ARCHITECTURE.md`
8. `docs/build/BUILD-SPEC-001-BUSINESS-REALITY-MVP-SKELETON-v0.1.md`
9. `docs/workstreams/koe/09-SYSTEMS-DESIGN-ENGINEERING-PRINCIPLES-v0.1.md`
10. `docs/workstreams/koe/10-BUSINESS-REALITY-SEMANTIC-FOUNDATION-v0.1.md`
11. `docs/workstreams/koe/15-MODEL-OWNERSHIP-AND-BOUNDARY-MAP-v0.1.md`
12. `docs/workstreams/koe/09-BUSINESS-REALITY-V1-OBJECT-CATALOG-v0.1.md`
13. `docs/workstreams/koe/27-BUILD-SPEC-001-MINIMUM-SEMANTIC-SUBSET-v0.1.md`
14. `docs/workstreams/koe/25-EXECUTION-PLAN-SEMANTIC-FOUNDATION-TO-RUNTIME-v0.1.md`
15. `contracts/` including `OPEN-SEMANTIC-QUESTIONS.md`, API, manifests, fixtures and workload profile
16. PR #3, PR #7, Issue #16, Issue #21

Where older foundation drafts conflict with accepted ADRs/current inter-layer contracts, the newer accepted/current artifact controls.

---

## 3. Current architecture

The active top-level operating model is:

```text
CONTROL / GOVERNANCE
        |
        v
BUSINESS INTENT
        |
        v
BUSINESS REALITY
   +----+----+
   |         |
   v         v
EXTERNAL   CAPABILITY
WORLD      MODEL
MODEL
   |         |
   +----+----+
        |
        v
EXECUTIVE JUDGMENT
        |
        v
DECISION / APPROVAL
        |
        v
KINETIC / GOVERNED ACTION
        |
        v
NEW BUSINESS STATE
        |
        v
OUTCOME / LEARNING
```

`World Model` as an umbrella for all reality is **deprecated**. New work distinguishes Business Reality from External World Model.

Business Reality is canonical current + historical operational state of GenSigma and its direct business relationships, with provenance, time, security, authority and correction semantics.

Sources are sensors/evidence providers, not truth.

Evidence flow:

```text
Raw Evidence
 -> Normalized/Observed Evidence
 -> Observation / Claim / Candidate
 -> Identity + Context Reconciliation
 -> Authority + Conflict Check
 -> Validation / Review
 -> Governed Canonical State
```

---

## 4. Four governing design truths — DECIDED

These are the KOE design constitution. The earlier long quality-pillar list is not governing doctrine.

1. **Preserve truth** — evidence/history are not destroyed because interpretation changes.
2. **Allow correction** — identity, relations, state and interpretation must be safely revisable.
3. **Keep the core stable** — extend contracts/domains rather than repeatedly redesigning foundational semantics.
4. **Make boundaries explicit** — each subsystem/model owns clear meaning and communicates through explicit contracts.

Tie-breaker: if a proposal conflicts with one of these truths, revise the proposal.

---

## 5. Key conclusions

### 5.1 Broad foundation, narrow first build — DECIDED

ADR-002 is authoritative:

- **Business Reality Semantic Foundation** = broad enterprise semantic compatibility envelope.
- **BUILD SPEC 001** = narrow Chief Architect-owned first executable vertical slice.
- The foundation must not force all candidate types into the first runtime.
- The pilot must not redefine the enterprise ontology.

The old KOE artifact that overloaded the name `BUILD SPEC 001` for the broad foundation is deprecated and now points to `10-BUSINESS-REALITY-SEMANTIC-FOUNDATION-v0.1.md`.

### 5.2 Enterprise object envelope — TENTATIVE count, DECIDED discipline

Current KOE candidate model contains **38 semantic business-object candidates** and uses approximately **30–40** as a design/complexity guardrail, not a quota.

Admission is semantic: independent identity, lifecycle, relationships, security, actions, ownership/accountability, temporal state and query value.

Availability and Capacity are not V1 business objects by default; they are temporal measurements/claims unless independent lifecycle/identity emerges.

**Shared-spec conflict:** the older draft foundational ADR-016 on `main` still says 25–35. This is now ASK_ARCHITECT Issue #21. Do not silently edit the shared ADR or churn the object model just to hit a number.

### 5.3 BUILD SPEC 001 minimum subset — TENTATIVE / KOE recommendation

Default KOE recommendation: **14 semantic resource types** plus shared kernel/evidence contracts:

```text
Organization
Person
BusinessRelationship
Opportunity
Solicitation
Proposal
Agreement
Artifact
Event
Assessment
Decision
Approval
Action
Outcome
```

Conditional only when the selected episode requires them: Project, Obligation, ContractVehicle, Capability reference, Offering reference.

This is a runtime slice, not a reduction of the enterprise foundation.

### 5.4 Identity and contextual role — DECIDED

One canonical Organization/Person may hold multiple roles across scope/time.

Customer, Partner, Vendor, Subcontractor, Employee, Contractor, Candidate, Approver and similar labels are normally contextual role/relationship semantics, not duplicate identity classes.

Merge/split must be reversible and provenance-preserving.

### 5.5 Organization structure — DECIDED direction

Keep LegalEntity, OrganizationalUnit and Organization semantically distinct where lifecycle/legal/authority boundaries require it.

For U.S. state presence use concepts such as Registration/Qualification, Registered Office relationship and Operating Location; do not create inaccurate generic `Branch` semantics merely to mirror forms/source systems.

### 5.6 Evidence and authority — DECIDED

- raw/source observations are append-oriented and preserved;
- canonical interpretation is revisable;
- authority is proposition/property-specific, not a universal source ranking;
- confidence is one input, not a universal promotion threshold;
- copied/forwarded/quoted evidence does not count as independent corroboration without origin independence;
- model output is non-authoritative by default;
- connectors never write canonical truth directly.

### 5.7 Time — DECIDED

Distinguish when material:

```text
effective/business time
source time
recorded time
discovery time
current state
historical state
scenario/hypothetical state
```

Do not project current classification backward without evidence.

### 5.8 Event / cognition / action distinctions — DECIDED

Preserve distinct resources/semantics:

```text
Event != Assessment != Decision != Approval != Action != Outcome
```

Decision Trace is primarily traversal through first-class resources, not a giant summary object.

Historical reconstruction must label explicit vs inferred vs unknown.

### 5.9 Model ownership — DECIDED current baseline

Primary semantic owners:

- Organization/Person/commercial/delivery/workforce/finance/compliance/system facts -> Business Reality;
- Offering -> Business Intent;
- Capability feasibility -> Capability Model;
- Assessment/Risk/Decision -> Executive Judgment;
- Approval -> Executive Judgment / Governed Action boundary;
- Action -> Governed/Kinetic Action;
- Outcome -> Outcome/Learning;
- Claim currently -> shared/business-reality knowledge layer, with ownership still an open refinement question.

Other models reference owned concepts using stable canonical references; they do not fork authoritative copies.

### 5.10 Executive Cognition semantic seam — DECIDED requirement, implementation READY

ADR-003 requires KOE to support the smallest coherent representation of:

1. probability adequacy;
2. multidimensional uncertainty;
3. ex-ante expectations;
4. reversal/sensitivity conditions;
5. decision-method provenance;
6. causal-versus-predictive distinction.

These are semantic/query requirements, **not automatic new object types**.

### 5.11 Physical architecture — OPEN / intentionally deferred

Do not select production database, graph-vs-relational primary store, vector/search engine, Azure topology, or agent framework from KOE semantics alone.

Platform must benchmark against object/link shapes, temporal queries, traversal, evidence lineage, correction, security, read/write patterns and realistic scale.

---

## 6. DECIDED / TENTATIVE / OPEN / DEPRECATED register

### DECIDED

- four design truths;
- Business Reality vs External World Model separation;
- sources are sensors, not truth;
- Enterprise Evidence Graph / candidate layer is non-authoritative;
- identity distinct from contextual role;
- reversible/provenance-preserving reconciliation;
- time first-class;
- evidence origin lineage matters;
- property-specific authority;
- Event/Assessment/Decision/Approval/Action/Outcome distinction;
- typed/governed material actions;
- semantic security/authority required end-to-end;
- one semantic contract, replaceable physical projections;
- broad foundation vs narrow BUILD SPEC 001 split (ADR-002);
- ADR-003 six cognition-facing semantic/query obligations.

### TENTATIVE

- exact final V1 admitted object list; current candidates = 38;
- KOE default BUILD SPEC 001 subset = 14 types pending Chief Architect build integration / selected episode;
- BusinessRelationship physical representation;
- whether Risk later splits into operational record + judgment assessments;
- whether Outcome later splits operational vs strategic learning semantics;
- whether OfferingInstance becomes necessary;
- long-term Claim subsystem ownership;
- exact candidate/promotion state machine beyond current safe rules.

### OPEN

- Issue #21: shared ADR-016 25–35 vs current KOE 30–40 guardrail;
- Issue #16: reference-kernel promotion/type-contract fixes;
- production persistence/search/vector/cloud architecture;
- exact identity-resolution algorithm;
- calibrated thresholds where any domain later needs them;
- realistic performance/scale targets;
- final BUILD SPEC 001 pilot selection/integration by Chief Architect;
- runtime implementation of ADR-003 semantic requirements.

### DEPRECATED / SUPERSEDED

- `World Model` as the primary umbrella term for internal + external reality;
- SFO/CRI or any one episode as the source/center of enterprise ontology design;
- 15–18 pilot objects as the ontology target;
- broad semantic foundation called `BUILD SPEC 001`;
- long independent 16-pillar quality checklist as governing design law;
- Customer/Partner/Vendor/etc. as duplicate Organization subclasses;
- source-system schemas as ontology;
- universal confidence threshold for canonical promotion;
- destructive correction/overwrite;
- direct connector-to-canonical writes;
- premature production database selection.

---

## 7. Rejected approaches and why

### One pilot -> ontology
Rejected because it overfits the enterprise model to accidental local evidence. Correct order is:

```text
Enterprise semantic foundation
 -> domain semantics
 -> real episode pressure tests
```

### Implement all ~38 types in first runtime
Rejected by ADR-002. It slows learning and confuses compatibility envelope with build scope.

### Giant design-principle checklist
Rejected as governing doctrine because too many equal-status principles dilute architectural truth. Quality properties are diagnostics; four truths govern.

### Fixed role subclasses
Rejected because one party can be Customer, Partner, Vendor, Subcontractor, etc. in different contexts/times.

### Source schema = canonical model
Rejected because sources are sensors and their schemas encode application conventions, not enterprise meaning.

### LLM/model inference = truth
Rejected because probabilistic interpretation must remain evidence-backed, uncertainty-aware and governed before promotion.

### Direct CRUD mutation for material state change
Rejected in favor of typed, governed actions and auditable correction/promotion paths.

### Destructive merge/correction
Rejected because the system must preserve evidence/history and support reversal.

### Database-first architecture
Rejected because physical architecture must be benchmarked against logical workloads and invariants.

### Universal decision method
Rejected by ADR-003: decision classes require method routing under a common governance shell.

---

## 8. Important benchmark / research findings

`24-BENCHMARK-FIRST-DELIVERY-PATTERN-v0.1.md` records the external engineering benchmark used for delivery posture.

Findings from Thoughtworks evolutionary architecture and Google SRE/reliability practice:

- keep long-lived architecture broader than any one release;
- ship small coherent/self-contained increments;
- protect architecture using executable fitness functions/tests;
- stage qualification against realistic behavior/data;
- preserve reversibility and isolate unrelated change;
- expand after the prior slice proves fitness.

GenSigma consequence:

```text
Broad Semantic Foundation
 -> Small Executable Slice
 -> Automated Semantic/Fitness Tests
 -> Realistic Fixture/Evidence Pressure Test
 -> Learn/Correct
 -> Next Slice
```

Judge the first runtime by whether hard invariants work end-to-end, not by how many of the 38 candidates are implemented.

---

## 9. Current executable contracts/artifacts

The KOE branch currently contains:

- JSON Schema Draft 2020-12 semantic contracts;
- OpenAPI 3.1 logical Business Reality contract;
- canonical resource/ref, identity/source mapping, alias, time, epistemic, provenance, security, audit/correction and typed-relationship kernel contracts;
- Event, Assessment, Decision, Approval, Action, Outcome schemas;
- business schemas spanning the current candidate model;
- RawEvidence, Observation, Candidate evidence schemas;
- identity fixture + six domain fixture packs;
- T01–T31 semantic acceptance manifest;
- FF-001–FF-010 architecture-fitness manifest;
- workload/scale measurement profile;
- explicit open semantic questions.

Runtime-required fitness checks must not be marked PASS until corresponding runtime behavior exists.

---

## 10. Reference runtime status

PR #7 is the first in-memory executable Business Reality reference kernel.

Verified PASS at review head:

- schema registry/runtime validation;
- replay-idempotent raw evidence;
- immutable evidence ID/content behavior;
- candidate must reference known evidence;
- no public direct canonical put path;
- promotion lineage retains candidate + evidence IDs + actor/reason/time;
- correction appends new interpretation and preserves history;
- CI passed on reviewed head.

Known gaps tracked in Issue #16:

- enforce candidate `proposed_semantic_type` vs promoted `resource.type` compatibility;
- resolve contract paths across business + kernel semantic resources instead of hard-coding `schemas/business/`.

The current reference kernel is not the final production promotion authorization state machine.

---

## 11. Assumptions

- Initial evidence sensors remain Outlook/Exchange and SharePoint unless program scope changes.
- RFP-to-cash remains the first deep value-chain bias, but no one customer/episode has privileged ontology authority.
- BUILD SPEC 001 should prove identity, evidence-before-truth, context, time, provenance, contradiction, correction, decision trace, security and queryability with a bounded episode.
- A small team must be able to operate the eventual system; operational complexity requires measured justification.
- The current Python/in-memory kernel is a reference mechanism, not a platform selection.
- KOE contracts are technology-neutral requirements consumed by Platform/Evidence/Data/Cognition.
- Exact latency/throughput/scale targets remain evidence-backed OPEN values, not invented numbers.

---

## 12. DONE / READY / BLOCKED

### DONE

- four design truths durable;
- top-level conceptual boundaries and World Model retirement direction durable;
- broad Business Reality Semantic Foundation defined;
- 38-candidate catalog + definitions/admission/property/lifecycle docs;
- typed relationship/role catalog;
- ownership boundary map;
- temporal/evidence/security/correction kernel semantics;
- promotion matrix;
- logical API and ambiguity outcomes;
- multi-domain fixtures;
- T01–T31 and FF-001–FF-010 manifests;
- workload profile;
- minimum BUILD SPEC 001 subset recommendation;
- benchmark-first delivery finding;
- first reference-kernel semantic review;
- ADR-002 scope conflict resolved;
- stale broad-foundation Build Spec artifact deprecated/replaced.

### READY

- reconcile/rebase PR #3 with current `main`;
- close Issue #16 in PR #7;
- retarget/rebase PR #7 after KOE base reconciliation;
- integrate ADR-003 six requirements into smallest coherent contracts/acceptance cases;
- typed relationship runtime;
- temporal/as-of reads;
- security-context enforcement/non-leakage tests;
- query/context API implementation;
- continue VERIFY/LEARN against T/FF manifests;
- provide KOE minimum subset to Chief Architect BUILD SPEC integration.

### BLOCKED / GATED

- PR #3 merge: branch currently diverged/non-mergeable and needs reconciliation;
- PR #7 integration: stacked on KOE branch and gated by PR #3/base reconciliation;
- production persistence/search/cloud selection: gated by Platform benchmarks + architecture decision;
- changing shared ADR-016 count wording: gated by Issue #21 / CA-001;
- final authoritative BUILD SPEC 001 pilot/scope: Chief Architect-owned integration gate.

---

## 13. Current branches / PRs / issues

At transition time:

### Branches

- `main` — governing shared program/ADRs/standards;
- `workstream/koe-first-session-v0.1` — active KOE semantic foundation branch;
- `build/reference-business-reality-kernel-v0.1` — reference runtime branch.

### Pull requests

- **PR #3** — `KOE: Business Reality Semantic Foundation + Executable Contracts` — OPEN; currently non-mergeable because KOE branch has diverged from `main`.
- **PR #7** — `Build 002: executable Business Reality reference kernel v0.1` — OPEN; stacked on KOE branch; currently non-mergeable pending base reconciliation.

### Issues

- **Issue #5** — Build Spec scope conflict — CLOSED / DECIDED by ADR-002.
- **Issue #16** — promotion/type-contract gaps in PR #7 — OPEN / READY.
- **Issue #21** — reconcile old ADR-016 25–35 with current ~30–40 guardrail — OPEN / ASK_ARCHITECT; not build-blocking.
- **Issue #18** — Platform persistent-lead pilot references the same Business Reality kernel path; coordinate factually but do not let agent-pilot mechanics redefine KOE semantics.

Latest branch comparison observed during migration: KOE branch was 102 commits ahead and 32 commits behind `main`; exact counts can move, so re-check before reconciliation.

---

## 14. Dependencies and interfaces

### Chief Architect / CA-001

Owns cross-cutting architecture, accepted ADRs, shared spec conflicts, BUILD SPEC 001 integration and Issue #21 disposition.

### Evidence / Data Engineering

Consumes KOE evidence/candidate/promotion semantics and implements sensor/ingestion/extraction/reconciliation pipelines. EDE may propose candidates; it must not redefine canonical meaning or write truth directly.

### Platform Engineering

Consumes semantic contracts, workload/scale/security/temporal requirements and benchmarks physical implementations. Platform must not encode different business meaning for convenience.

### Executive Cognition Research

ADR-003 supplies six shared semantic/query requirements. KOE must represent them minimally while preserving ownership boundaries.

### Business Intent / Capability / External World

KOE references their owned concepts via stable cross-model contracts; Business Reality must not duplicate authoritative meanings.

---

## 15. Risks

1. **Branch drift:** PR #3 is far behind `main`; careless merge/rebase can reintroduce deprecated terminology or overwrite newer shared governance.
2. **Stacked runtime:** PR #7 depends on the KOE branch; fix base topology before treating it as merge-ready.
3. **Shared ADR drift:** old draft foundational ADRs still contain legacy World Model wording and ADR-016 25–35 guidance. Newer accepted/current artifacts control where explicit; Issue #21 covers the unresolved count contradiction.
4. **Semantic overreach from runtime:** the in-memory kernel is a reference, not proof of production platform/promotion architecture.
5. **Security leakage:** future search/traversal/derived projections must preserve source and semantic access restrictions.
6. **False certainty:** unknown/unresolved/contradicted/inferred states must not be coerced into accepted truth.
7. **Pilot overfitting:** do not let SFO/CRI or any single commercial episode drive new enterprise classes without admission pressure.
8. **Object proliferation:** ADR-003 requirements should be represented through existing structures where possible, not six new top-level objects.
9. **Count gaming:** do not add/remove objects to satisfy a numeric target; use semantic admission tests.
10. **Unmeasured platform commitments:** do not select persistence/search topology before realistic benchmark evidence.

---

## 16. Next five actions

1. **Reconcile PR #3 with current `main`.** Preserve ADR-002/ADR-003, the Workstream Delivery Standard, current inter-layer contracts and this transition brief; resolve stale naming/legacy wording carefully.
2. **Integrate KOE's 14-type minimum subset into the Chief Architect BUILD SPEC 001 process.** Keep the broad foundation separate and add only episode-forced conditional types.
3. **Close Issue #16 and retarget/rebase PR #7.** Add tests for candidate/resource type compatibility and business+kernel contract resolution; keep the PR narrow.
4. **Implement ADR-003's six semantic/query requirements minimally.** Prefer Assessment/Decision/context metadata/contracts and acceptance assertions over new object types; ASK_ARCHITECT only if shared interfaces must change.
5. **Continue bounded runtime increments and VERIFY/LEARN:** typed relationships -> temporal/as-of reads -> security context/non-leakage -> query/context API -> run applicable T01–T31/FF checks -> hand measured workload evidence to Platform before production persistence decisions.

---

## 17. Transition rule

This brief is a navigation/control document, not a replacement for the governing artifacts it references.

A fresh agent should be able to continue from GitHub alone. Do not reconstruct architecture from old chat history. If a question is not answered by current governing artifacts, classify it `LOCAL_SOLVE` or `ASK_ARCHITECT` and make the result durable.
