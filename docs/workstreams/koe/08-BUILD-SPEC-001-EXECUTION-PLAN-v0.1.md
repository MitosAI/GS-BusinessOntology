# Build Spec 001 Execution Plan — Business Reality MVP

**Version:** v0.1  
**Status:** Active execution plan  
**Owner:** Knowledge & Ontology Engineering (KOE-001)  
**Primary build target:** Business Reality MVP  
**Primary pilot:** SFO ServiceNow / CRI Advantage pursuit

---

## 1. Direction

The program is no longer organized around a generic `World Model` abstraction.

The active model architecture is:

```text
Business Intent
+ Business Reality
+ External Reality
+ Capability
        -> Executive Judgment
        -> Decision / Approval
        -> Governed Action
        -> New Business State
        -> Outcome / Learning
```

Build Spec 001 is the first executable slice of **Business Reality**.

The V1 enterprise ontology design guidance is approximately **30–40 business objects**, but Build Spec 001 MUST NOT wait for all 30–40 objects to be fully modeled. The first build should implement the smallest coherent subset required to prove the architecture against a real GenSigma episode.

---

## 2. Working mode

### ChatGPT conversation = architecture control plane

Use the Knowledge & Ontology Engineering thread to:

- define semantics;
- resolve object boundaries;
- define identity, context, time, evidence, security, and promotion behavior;
- define logical APIs and action semantics;
- define competency questions and acceptance tests;
- review implementation behavior against the specification;
- approve semantic changes before they become implementation assumptions.

### Codex = implementation workbench

Use Codex for:

- multi-file code changes;
- repository-wide refactors;
- schema/type definitions;
- API implementation;
- fixtures and seed data;
- test harnesses;
- ingestion/reconciliation code;
- running tests and inspecting failures;
- implementation PRs.

Codex MUST implement the semantic contract; it MUST NOT invent ontology meaning, canonical promotion rules, identity behavior, time semantics, or security semantics when the specification is silent.

If implementation exposes an unresolved semantic choice, return that choice to KOE rather than hard-coding an assumption.

---

## 3. Build gate

We do **not** wait for a perfect enterprise ontology before building.

Implementation begins when the following Build Spec 001 kernel is explicit enough that an engineer does not need to invent semantics:

1. pilot boundary and evidence corpus;
2. canonical object subset for the pilot;
3. object identity and key properties;
4. relationship/link semantics;
5. event / decision / action / outcome distinctions;
6. claim/evidence/provenance structure;
7. identity and context reconciliation outcomes;
8. temporal semantics;
9. canonical promotion rules;
10. security semantics;
11. read/query contract;
12. proposed-write contract;
13. benchmark queries;
14. fixture manifest;
15. executable acceptance tests.

When these are stable, Build Spec 001 is buildable even though the wider 30–40-object V1 ontology continues to mature.

---

## 4. Spec completion sequence

### S1 — Canonical object catalog for the pilot

For every business object used by the SFO/CRI episode, define:

- canonical name;
- definition;
- admission rationale;
- identity rule;
- lifecycle/state;
- key properties;
- allowed relationships;
- temporal behavior;
- evidence requirements;
- security considerations;
- actions that may operate on it.

The pilot should reuse enterprise-level objects and MUST NOT introduce SFO- or CRI-specific classes.

### S2 — Link and role catalog

Define typed semantic relationships needed by the episode, including cardinality/scope where material.

Examples include organization participation, opportunity/customer relationships, solicitation-to-opportunity, person participation, partner-in-opportunity, agreement governance, artifact evidence, decision/action/outcome links, and identity/source mappings.

Roles such as Customer, Partner, Vendor, Employee, Stakeholder, Candidate, or Decision Maker should remain contextual unless the object admission test demonstrates an independent object is required.

### S3 — State, event, decision, action, outcome model

Define the minimum event and action vocabulary needed to reconstruct and operate the SFO/CRI lifecycle.

Preserve the distinction:

```text
Event    = what happened
Decision = what choice was made
Action   = what was done
Outcome  = what resulted
```

### S4 — Evidence and epistemic contract

Finalize the logical representation of:

- raw source reference;
- observation;
- claim;
- candidate;
- supporting/contradicting evidence;
- origin lineage;
- authority;
- explicit vs inferred/reconstructed status;
- promotion/rejection/correction history.

### S5 — Identity and context resolution contract

Define legal outcomes for entity/context reconciliation, including:

- exact match;
- alias;
- historical name;
- parent/child;
- organizational unit;
- related but distinct;
- merge proposal;
- split proposal;
- new canonical entity proposal;
- unresolved;
- multiple plausible matches.

### S6 — Temporal and security contract

Lock business/effective time, source time, recorded time, discovery time, supersession/correction behavior, and historical `as_of` semantics.

Define security propagation from source evidence through candidate and canonical layers, including security-aware search and traversal.

### S7 — Logical API contract

Finalize read operations, proposed-write operations, error states, ambiguity responses, provenance exposure, security context, and historical query behavior.

Physical database technology remains unspecified until the workload is benchmarked.

### S8 — Acceptance fixture package

Create a reproducible SFO/CRI fixture set containing representative Outlook messages and SharePoint artifacts/versions or sanitized equivalents, expected extraction candidates, expected identity/context outcomes, expected canonical state, expected contradictions/unknowns, and at least one restricted-security case.

### S9 — Executable acceptance suite

Translate competency questions into machine-testable assertions.

The spec is ready for implementation when these tests define what success means before the implementation exists.

---

## 5. Build sequence

### Build 1 — Semantic kernel

Implement the logical types/contracts for canonical objects, relationships, claims/evidence, time, security context, and proposed mutations.

Goal: representation and invariants, not sophisticated AI extraction.

### Build 2 — Fixture-backed Business Reality service

Load the pilot fixtures through deterministic/manual adapters first and prove:

- identity resolution states;
- evidence-backed canonical state;
- temporal reads;
- relationship traversal;
- decision trace reconstruction;
- security filtering;
- canonical promotion/correction auditability.

### Build 3 — Outlook and SharePoint sensor pipeline

Connect actual/sanitized source capture to the evidence layer while preserving immutable source identity, hashes, versions, timestamps, ACLs, and lineage.

Sensors create evidence and candidates; they do not create canonical truth directly.

### Build 4 — Candidate extraction and reconciliation assistance

Introduce LLM/probabilistic extraction for observations, claims, aliases, candidate entities, relationships, contexts, events, and decision fragments.

Probabilistic output remains below the canonical boundary until governed promotion.

### Build 5 — Canonical promotion workflow

Implement review/approval, promotion, rejection, correction, merge/split, provenance history, and audit trail.

### Build 6 — Query/context service

Expose the benchmark query suite needed by humans, Executive Judgment, and future agents.

### Build 7 — Pressure test against comparison episodes

Run the same semantic contract against:

- Stridepath / CCSF HRSD;
- Fivetran partner agreement.

Any SFO/CRI-specific modeling leakage is treated as a defect.

---

## 6. Parallel ontology work

The wider 30–40-business-object V1 ontology continues in parallel with Build Spec 001.

Objects are admitted from real business loops rather than brainstormed exhaustively. Each new object must survive the object-admission test and at least one competency question or governed action test.

Build Spec 001 is therefore the first proving ground for the ontology, not the final ontology inventory.

---

## 7. Division of responsibility

### KOE owns

- semantic definitions;
- object/link boundaries;
- evidence and epistemic semantics;
- identity/context/time/security semantics;
- promotion rules;
- logical API behavior;
- competency questions and golden actions;
- acceptance semantics.

### Evidence & Data Engineering owns

- source capture;
- normalization;
- lineage preservation;
- extraction implementation;
- evidence/candidate production consistent with KOE contracts.

### Platform Engineering owns

- physical persistence;
- indexing/search implementation;
- service/runtime architecture;
- performance/availability/observability;
- transaction mechanisms;
- benchmarked technology selection.

### Executive Cognition consumes

- Business Intent;
- Business Reality;
- External Reality;
- Capability;
- evidence/uncertainty;
- decision trace context;
- governed action definitions.

It does not redefine canonical business semantics.

---

## 8. Immediate next deliverables

KOE should now produce, in this order:

1. **Business Reality V1 object catalog — candidate 30–40 object map** with clear L1/L2 boundaries;
2. **Build Spec 001 pilot object subset** selected from that catalog;
3. **typed link/role catalog** for the pilot;
4. **pilot event/action vocabulary**;
5. **fixture manifest** for SFO/CRI;
6. **executable acceptance-test specification**;
7. **Codex implementation brief** referencing the above contracts.

After items 2–6 are explicit, implementation should begin in Codex. Items outside the pilot can continue evolving in parallel and should not block the first build.

---

## 9. Non-negotiable build rule

The program should optimize for a repeating cycle:

```text
SPECIFY SEMANTICS
    -> WRITE ACCEPTANCE TESTS
    -> IMPLEMENT IN CODEX
    -> RUN AGAINST REAL EPISODE
    -> IDENTIFY SEMANTIC FAILURE
    -> REFINE ONTOLOGY / SPEC
    -> RE-RUN
```

The objective is not to finish the ontology before implementation. The objective is to make the ontology computational, testable, and operational as early as possible without allowing implementation convenience to define business meaning.
