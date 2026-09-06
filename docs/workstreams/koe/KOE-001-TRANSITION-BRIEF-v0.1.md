# KOE-001 Transition Brief

**Version:** v0.2  
**Status:** Active zero-context continuation brief  
**Owner:** KOE-001 — Knowledge & Ontology Engineering Lead  
**Purpose:** Allow a fresh KOE agent to continue competently from GitHub without access to the originating chat.

---

## 1. Mission / scope

KOE-001 owns the logical design of GenSigma OS Business Reality and the semantic path from messy enterprise evidence to governed canonical state.

KOE owns:

- canonical business semantics and object admission;
- identity / alias / reconciliation semantics;
- contextual relationship and role semantics;
- evidence/provenance requirements at the canonical boundary;
- temporal/current/historical semantics;
- promotion/correction semantics;
- security/authority semantics as they affect ontology/contracts;
- query and proposed-write behavioral contracts;
- interfaces to Business Intent, External World Model, Capability, Executive Judgment, Governed/Kinetic Action, Outcome/Learning, Evidence/Data and Platform;
- semantic acceptance/fitness requirements;
- KOE's minimum semantic subset recommendation for BUILD SPEC 001.

KOE does **not** own production persistence/search/vector/cloud topology, connector implementation, final decision-method architecture, Business Intent semantics, dynamic Capability evaluation, autonomous action runtime, or the Chief Architect-owned BUILD SPEC 001 integration gate.

Use `LOCAL_SOLVE` for reversible choices inside approved KOE boundaries. Use `ASK_ARCHITECT` for shared semantics/interfaces/security/provenance/time/ownership or hard-to-reverse platform decisions.

---

## 2. Read-first authority order

Read before material work:

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
16. live PR #3, PR #7, Issue #16 and Issue #21

Where older foundation drafts conflict with accepted ADRs/current inter-layer contracts, the newer accepted/current artifact controls.

---

## 3. Current architecture

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

`World Model` as an umbrella for internal + external reality is **deprecated**. New work distinguishes Business Reality from External World Model.

Business Reality is canonical current + historical operational state of GenSigma and its direct business relationships, with provenance, time, security, authority and correction semantics.

Sources are sensors/evidence providers, not truth.

Canonicalization path:

```text
Raw Evidence
 -> Observation / Claim / Candidate
 -> Identity + Context Reconciliation
 -> Authority + Conflict Check
 -> Validation / Review
 -> Governed Canonical State
```

---

## 4. Four governing design truths — DECIDED

The earlier long quality-pillar list is not governing doctrine.

1. **Preserve truth** — evidence/history are not destroyed because interpretation changes.
2. **Allow correction** — identity, relations, state and interpretation must be safely revisable.
3. **Keep the core stable** — extend contracts/domains rather than repeatedly redesigning foundational semantics.
4. **Make boundaries explicit** — each subsystem/model owns clear meaning and communicates through explicit contracts.

Quality properties such as robustness, scalability, security, observability and maintainability are evaluated under these truths, not treated as competing constitutional laws.

---

## 5. Key conclusions

### Broad foundation vs first executable build — DECIDED

ADR-002 is authoritative:

- **Business Reality Semantic Foundation** = broad enterprise semantic compatibility envelope.
- **BUILD SPEC 001** = narrow Chief Architect-owned first executable vertical slice.
- The broad foundation does not force all candidate types into the first runtime.
- The pilot does not redefine enterprise ontology.

The former KOE artifact that overloaded `BUILD SPEC 001` for the broad foundation is now a deprecated pointer. The canonical broad artifact is `10-BUSINESS-REALITY-SEMANTIC-FOUNDATION-v0.1.md`.

### Enterprise object envelope — TENTATIVE count / DECIDED admission discipline

Current KOE candidate model: **38 semantic business-object candidates**.

Current KOE design envelope: approximately **30–40**, as a complexity guardrail, not a quota.

Admission is semantic: independent identity, lifecycle, relationships, security, actions, ownership/accountability, temporal state and query value.

Availability and Capacity are not V1 business objects by default; they are temporal measurements/claims unless independent identity/lifecycle emerges.

**Shared-spec conflict:** old draft ADR-016 on `main` still says 25–35. This is ASK_ARCHITECT Issue #21. Do not silently edit shared ADR-016 or churn the model merely to hit a number.

### BUILD SPEC 001 minimum subset — TENTATIVE / KOE recommendation

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

Conditional only when the chosen episode requires them: Project, Obligation, ContractVehicle, Capability reference, Offering reference.

This is a runtime slice, not a reduction of the enterprise foundation.

### Identity / role — DECIDED

One canonical Organization/Person may hold multiple roles across scope/time.

Customer, Partner, Vendor, Subcontractor, Employee, Contractor, Candidate, Approver and similar labels are normally contextual role/relationship semantics, not duplicate identity classes.

Merge/split must be reversible and provenance-preserving.

### Evidence / authority — DECIDED

- raw/source observations are append-oriented and preserved;
- canonical interpretation is revisable;
- authority is proposition/property-specific, not a universal source ranking;
- confidence is one input, not a universal promotion threshold;
- copied/forwarded/quoted evidence is not independent corroboration without origin independence;
- model output is non-authoritative by default;
- connectors never write canonical truth directly.

### Time — DECIDED

Distinguish where material:

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

### Event / cognition / action distinctions — DECIDED

```text
Event != Assessment != Decision != Approval != Action != Outcome
```

Decision Trace is primarily traversal through first-class resources, not a giant summary object. Historical reconstruction must label explicit vs inferred vs unknown.

### Model ownership — DECIDED current baseline

- Organization/Person/commercial/delivery/workforce/finance/compliance/system facts -> Business Reality;
- Offering -> Business Intent;
- dynamic Capability feasibility -> Capability Model;
- Assessment/Risk/Decision -> Executive Judgment;
- Approval -> Executive Judgment / Governed Action boundary;
- Action -> Governed/Kinetic Action;
- Outcome -> Outcome/Learning;
- Claim currently -> shared/business-reality knowledge layer, with ownership still an open refinement question.

Other models reference owned concepts via stable canonical references; they do not fork authoritative copies.

### Executive Cognition seam — DECIDED requirement / READY implementation

ADR-003 requires the smallest coherent representation of:

1. probability adequacy;
2. multidimensional uncertainty;
3. ex-ante expectations;
4. reversal/sensitivity conditions;
5. decision-method provenance;
6. causal-versus-predictive distinction.

These are semantic/query requirements, **not automatic new object types**.

### Physical architecture — OPEN / intentionally deferred

Do not select production database, graph-vs-relational primary store, vector/search engine, Azure topology, or agent framework from KOE semantics alone.

Platform must benchmark against object/link shapes, temporal queries, traversal, evidence lineage, correction, security, read/write patterns and realistic scale.

---

## 6. DECIDED / TENTATIVE / OPEN / DEPRECATED

### DECIDED

- four design truths;
- Business Reality vs External World Model separation;
- sources are sensors, not truth;
- non-authoritative evidence/candidate layer;
- identity distinct from contextual role;
- reversible/provenance-preserving reconciliation;
- time first-class;
- evidence origin lineage;
- property-specific authority;
- Event/Assessment/Decision/Approval/Action/Outcome distinction;
- typed/governed material actions;
- semantic security/authority end-to-end;
- one semantic contract with replaceable physical projections;
- broad foundation vs narrow BUILD SPEC 001 split (ADR-002);
- ADR-003 six cognition-facing semantic/query obligations.

### TENTATIVE

- exact final V1 admitted object list; current candidates = 38;
- KOE default BUILD SPEC 001 subset = 14 types pending Chief Architect integration / selected episode;
- BusinessRelationship physical representation;
- Risk operational-record vs judgment split;
- Outcome operational vs strategic-learning split;
- OfferingInstance need;
- long-term Claim subsystem ownership;
- exact candidate/promotion state machine beyond current safe rules.

### OPEN

- Issue #21: old ADR-016 25–35 vs current KOE ~30–40 guardrail;
- Issue #16: reference-kernel promotion/type-contract fixes;
- production persistence/search/vector/cloud architecture;
- exact identity-resolution algorithm;
- calibrated thresholds where later justified;
- realistic performance/scale targets;
- final BUILD SPEC 001 pilot selection/integration by Chief Architect;
- runtime representation/tests for ADR-003 semantic requirements.

### DEPRECATED / SUPERSEDED

- `World Model` as primary umbrella term;
- SFO/CRI or any single episode as enterprise ontology center;
- 15–18 pilot objects as ontology target;
- broad semantic foundation called `BUILD SPEC 001`;
- 16-pillar checklist as governing design law;
- Customer/Partner/Vendor/etc. as duplicate Organization subclasses;
- source-system schema as ontology;
- universal confidence threshold for promotion;
- destructive correction/overwrite;
- direct connector-to-canonical writes;
- premature database selection.

---

## 7. Rejected approaches and why

- **One pilot -> ontology:** overfits enterprise semantics to accidental local evidence. Correct order is enterprise foundation -> domain semantics -> episode pressure tests.
- **All 38 in first runtime:** rejected by ADR-002; confuses compatibility envelope with build scope.
- **Giant principle checklist:** rejected as governing doctrine because too many equal-status principles dilute architectural truth.
- **Fixed role subclasses:** rejected because party roles vary by context/time.
- **Source schema = canonical model:** rejected because source applications are sensors, not semantic authority.
- **LLM/model inference = truth:** rejected because probabilistic interpretation requires evidence, uncertainty and governance.
- **Direct CRUD for material state change:** rejected in favor of typed governed actions and audited promotion/correction paths.
- **Destructive merge/correction:** rejected because evidence/history and reversal must survive.
- **Database-first architecture:** rejected until logical workloads/benchmarks are real.
- **Universal decision method:** rejected by ADR-003; decision classes require method routing under a common governance shell.

---

## 8. Important benchmark / research findings

`24-BENCHMARK-FIRST-DELIVERY-PATTERN-v0.1.md` records the external benchmark.

Thoughtworks evolutionary-architecture and Google SRE/reliability practice support:

- long-lived architecture broader than one release;
- small coherent/self-contained increments;
- executable architecture fitness functions/tests;
- staged qualification against realistic behavior/data;
- reversibility and isolation of unrelated change;
- expansion only after the prior slice proves fitness.

GenSigma delivery posture:

```text
Broad Semantic Foundation
 -> Small Executable Slice
 -> Automated Semantic/Fitness Tests
 -> Realistic Fixture/Evidence Pressure Test
 -> Learn/Correct
 -> Next Slice
```

Judge the first runtime by whether hard invariants work end-to-end, not by how many candidate objects it implements.

---

## 9. Current contracts / artifacts

The KOE branch contains:

- JSON Schema Draft 2020-12 semantic contracts;
- OpenAPI 3.1 logical Business Reality API contract;
- canonical resource/ref, identity/source mapping, alias, time, epistemic, provenance, security, audit/correction and typed-relationship contracts;
- Event, Assessment, Decision, Approval, Action, Outcome schemas;
- business schemas spanning the current candidate model;
- RawEvidence, Observation, Candidate schemas;
- identity fixture + six domain fixture packs;
- T01–T31 semantic acceptance manifest;
- FF-001–FF-010 architecture-fitness manifest;
- workload/scale measurement profile;
- explicit open semantic questions.

Runtime-required fitness checks remain `NOT_RUN` / `CONTRACT_READY` until corresponding behavior exists.

---

## 10. Reference runtime status

PR #7 is the first in-memory executable Business Reality reference kernel.

Verified PASS at reviewed head:

- schema registry/runtime validation;
- replay-idempotent raw evidence;
- immutable evidence ID/content behavior;
- candidates reference known evidence;
- no public direct canonical put path;
- promotion lineage retains candidate/evidence IDs + actor/reason/time;
- correction appends new interpretation and preserves history;
- CI passed on reviewed head.

Issue #16 tracks two bounded LOCAL_SOLVE gaps:

- enforce candidate `proposed_semantic_type` vs promoted `resource.type` compatibility;
- resolve contracts across business + kernel resource schemas rather than hard-coding `schemas/business/`.

The current reference kernel is not the final production promotion authorization state machine.

---

## 11. Assumptions

- Initial evidence sensors remain Outlook/Exchange and SharePoint unless program scope changes.
- RFP-to-cash remains the first deep value-chain bias, but no one customer/episode has privileged ontology authority.
- BUILD SPEC 001 should prove identity, evidence-before-truth, context, time, provenance, contradiction, correction, decision trace, security and queryability with a bounded episode.
- A small team must be able to operate the eventual system; complexity requires measured justification.
- The Python/in-memory kernel is a reference mechanism, not a platform selection.
- KOE contracts are technology-neutral requirements consumed by Platform/Evidence/Data/Cognition.
- Exact latency/throughput/scale targets remain evidence-backed OPEN values, not invented numbers.

---

## 12. DONE / READY / BLOCKED

### DONE

- four design truths durable;
- current conceptual boundaries and World Model retirement direction durable;
- broad Business Reality Semantic Foundation defined;
- 38-candidate catalog + definitions/admission/property/lifecycle docs;
- typed relationship/role catalog;
- model ownership map;
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
- stale broad-foundation Build Spec artifact deprecated/replaced;
- zero-context transition state made durable.

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

- PR #3 is not semantically blocked; GitHub currently reports it mergeable, but clean integration is process-gated by reconciliation with current `main` because the branch is materially diverged;
- PR #7 is currently non-mergeable and integration is gated by PR #3/base reconciliation;
- production persistence/search/cloud selection is gated by Platform benchmarks + architecture decision;
- changing shared ADR-016 count wording is gated by Issue #21 / CA-001;
- final authoritative BUILD SPEC 001 pilot/scope is Chief Architect-owned.

---

## 13. Current branches / PRs / issues

### Branches

- `main` — governing shared program/ADRs/standards;
- `workstream/koe-first-session-v0.1` — active KOE semantic foundation branch;
- `build/reference-business-reality-kernel-v0.1` — reference runtime branch.

### Pull requests

- **PR #3** — `KOE: Business Reality Semantic Foundation + Executable Contracts` — OPEN; GitHub currently reports mergeable, but branch is materially diverged from `main` and should be reconciled/rebased before clean integration.
- **PR #7** — `Build 002: executable Business Reality reference kernel v0.1` — OPEN; stacked on KOE branch; currently non-mergeable pending base reconciliation.

### Issues

- **Issue #5** — Build Spec scope conflict — CLOSED / DECIDED by ADR-002.
- **Issue #16** — promotion/type-contract gaps in PR #7 — OPEN / READY.
- **Issue #21** — reconcile old ADR-016 25–35 with current KOE ~30–40 guardrail — OPEN / ASK_ARCHITECT; not build-blocking.
- **Issue #18** — Platform persistent-lead pilot references the Business Reality kernel path; coordinate facts/artifacts only and do not let agent-pilot mechanics redefine KOE semantics.

At migration audit the KOE branch was materially both ahead of and behind `main`; re-check live counts/status before any merge/rebase because they change as branches advance.

---

## 14. Dependencies

### CA-001
Owns cross-cutting architecture, accepted ADRs, shared spec conflicts, BUILD SPEC 001 integration and Issue #21 disposition.

### Evidence / Data Engineering
Consumes KOE evidence/candidate/promotion semantics and implements sensor/ingestion/extraction/reconciliation pipelines. EDE may propose candidates; it must not redefine canonical meaning or write truth directly.

### Platform Engineering
Consumes semantic contracts, workload/scale/security/temporal requirements and benchmarks physical implementations. Platform must not encode different business meaning for convenience.

### Executive Cognition Research
ADR-003 supplies six shared semantic/query requirements. KOE must represent them minimally while preserving ownership boundaries.

### Intent / Capability / External World
KOE references their owned concepts via stable cross-model contracts; Business Reality must not duplicate authoritative meanings.

---

## 15. Risks

1. **Branch drift:** careless reconciliation can reintroduce deprecated terminology or overwrite newer governance.
2. **Stacked runtime:** PR #7 depends on KOE branch topology; fix base before treating it as merge-ready.
3. **Shared ADR drift:** older draft ADRs retain legacy World Model wording and ADR-016 25–35 guidance. Newer accepted/current artifacts control where explicit; Issue #21 covers the count contradiction.
4. **Runtime overreach:** in-memory kernel is a reference, not proof of production platform/promotion architecture.
5. **Security leakage:** future search/traversal/derived projections must preserve source + semantic access restrictions.
6. **False certainty:** unknown/unresolved/contradicted/inferred states must not be coerced into accepted truth.
7. **Pilot overfitting:** no single commercial episode may drive enterprise classes without admission pressure.
8. **Object proliferation:** ADR-003 requirements should reuse existing structures where possible, not become six new top-level objects.
9. **Count gaming:** do not add/remove objects to satisfy a numeric target.
10. **Unmeasured platform commitments:** no persistence/search topology before realistic benchmark evidence.

---

## 16. Next five actions

1. **Reconcile PR #3 with current `main`.** Preserve ADR-002/ADR-003, delivery standards, current inter-layer contracts and this brief; resolve stale legacy wording carefully.
2. **Integrate KOE's 14-type minimum subset into the Chief Architect BUILD SPEC 001 process.** Keep broad foundation separate and add only episode-forced conditional types.
3. **Close Issue #16 and retarget/rebase PR #7.** Add tests for candidate/resource type compatibility and business+kernel contract resolution; keep the PR narrow.
4. **Implement ADR-003's six semantic/query requirements minimally.** Prefer Assessment/Decision/context metadata/contracts and acceptance assertions over new object types; ASK_ARCHITECT only if shared interfaces must change.
5. **Continue bounded runtime increments and VERIFY/LEARN:** typed relationships -> temporal/as-of reads -> security context/non-leakage -> query/context API -> applicable T01–T31/FF checks -> measured workload handoff to Platform before production persistence decisions.

---

## 17. Transition rule

This brief is a navigation/control document, not a replacement for the governing artifacts it references.

A fresh agent should continue from GitHub alone. Do not reconstruct architecture from old chat history. If a question is not answered by current governing artifacts, classify it `LOCAL_SOLVE` or `ASK_ARCHITECT` and make the result durable.
