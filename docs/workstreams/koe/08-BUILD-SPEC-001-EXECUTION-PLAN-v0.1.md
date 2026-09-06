# Build Spec 001 Execution Plan — Business Reality Semantic Foundation

**Version:** v0.2  
**Status:** Active execution plan  
**Owner:** Knowledge & Ontology Engineering (KOE-001)  
**Primary build target:** Enterprise Business Reality semantic foundation

---

## 1. Direction

Build Spec 001 is not a customer-specific pilot and not a narrow RFP ontology.

Its purpose is to define the stable semantic foundation for GenSigma's Business Reality across the enterprise.

The governing design truths are:

1. preserve truth;
2. allow correction;
3. keep the core stable;
4. make boundaries explicit.

The V1 ontology guidance is approximately **30–40 business objects**. The specification should define the full enterprise object architecture and cross-domain contracts before implementation decisions are allowed to shape meaning.

Implementation may proceed incrementally once a kernel contract is stable, but it must implement the enterprise semantics rather than derive them from one episode.

---

## 2. Architecture boundary

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

Build Spec 001 owns the **Business Reality semantic foundation** and the operational resources needed to connect it safely to the other models.

It does not define the reasoning algorithm of Executive Judgment, the full Business Intent ontology, the full External Reality model, or physical persistence technology.

---

## 3. Specification sequence

### S1 — Semantic kernel

Define the cross-domain primitives and invariants that all business objects inherit or compose:

- canonical identity;
- typed relationships;
- contextual roles;
- state and lifecycle;
- effective/source/recorded/discovered time;
- evidence/provenance;
- epistemic status;
- security/authority;
- Event / Decision / Action / Outcome distinctions;
- audit/correction semantics;
- versioning and migration behavior.

### S2 — Full V1 business-object architecture

Define and admission-test the approximately 30–40 enterprise business objects across:

- enterprise identity and structure;
- commercial/revenue;
- agreements/legal;
- delivery/project execution;
- workforce/resources;
- finance;
- compliance;
- systems/technology/assets;
- knowledge/activity/judgment/control.

For every admitted object define:

- semantic definition;
- identity rule;
- lifecycle/state;
- key properties;
- typed relationships;
- temporal behavior;
- evidence requirements;
- security behavior;
- governed actions;
- correction behavior.

### S3 — Relationship and role architecture

Define cross-domain links, participant roles, scope, lifecycle, cardinality where material, and relationship identity.

Roles such as Customer, Partner, Vendor, Employee, Contractor, Candidate, Stakeholder, Decision Maker, and Approver are contextual unless independent identity/lifecycle requirements justify otherwise.

### S4 — Evidence and epistemic contract

Finalize observation, claim, evidence, authority, contradiction, inference, provenance, lineage, promotion, rejection, supersession, and correction semantics.

### S5 — Identity and context reconciliation contract

Define exact match, alias, historical name, parent/child, organizational unit, related-but-distinct, merge, split, new identity proposal, unresolved, and multiple-plausible outcomes.

### S6 — Temporal/state contract

Define effective time, source time, recorded time, discovery time, state intervals, supersession, historical `as_of` behavior, hypothetical isolation, and correction/replay.

### S7 — Security and authority contract

Define semantic access policy, source ACL propagation, object/property/evidence restrictions, actor identity, delegation, approval authority, and governed action permissions.

### S8 — Query and action contract

Define enterprise query patterns and governed verbs before storage selection.

### S9 — Verification suite

Convert invariants and competency questions into machine-testable assertions.

### S10 — Multi-domain validation portfolio

Pressure-test the same semantic foundation against materially different enterprise scenarios rather than one golden episode.

---

## 4. Validation portfolio

At minimum, Build Spec 001 must survive these scenario families:

### A. Commercial pursuit
Opportunity, solicitation, account/customer context, partner relationship, proposal, agreement, decision, action.

### B. Delivery/project execution
Project, assignment, milestone/deliverable, customer acceptance, invoice/payment linkage, outcome.

### C. Workforce/resource lifecycle
Person, position, employment/engagement relationship, skill, credential, assignment, availability/capacity.

### D. Legal/compliance lifecycle
Legal entity, jurisdiction/place, registration/qualification, certification, obligation, renewal/expiration.

### E. Vendor/technology lifecycle
Organization relationship, agreement, system, technology, asset, cost/risk/capability dependency.

### F. Financial execution
Agreement/project, budget, invoice, payment, receivable/payable state, financial outcome.

SFO/CRI may remain one commercial fixture. It has no privileged architectural status.

---

## 5. Coding gate

Codex may begin implementation when the **semantic kernel** and the contracts required for the component being built are explicit enough that implementation does not need to invent business meaning.

The first build does not require every domain behavior to be complete, but it must be compatible with the full V1 object architecture.

A component is build-ready when these are known:

- responsibility and boundary;
- semantic inputs/outputs;
- invariants;
- identity and role behavior;
- time/state behavior;
- evidence/provenance behavior;
- security/authority behavior;
- failure/ambiguity behavior;
- correction behavior;
- acceptance tests;
- adjacent interfaces.

---

## 6. Build sequence

### Build 1 — Semantic kernel and type contracts

Implement technology-neutral domain contracts for canonical resources, typed links, state/time, evidence references, epistemic status, security context, audit/correction, and proposed mutations.

### Build 2 — Core Business Reality service

Implement canonical CRUD/proposed-write behavior, historical reads, relationship traversal, promotion/correction, and audit semantics against deterministic fixtures.

### Build 3 — Multi-domain fixtures and tests

Load representative commercial, delivery, workforce, compliance, vendor/technology, and finance fixtures and make the same kernel pass all of them.

### Build 4 — Sensor integration

Add Outlook and SharePoint as sensors that produce evidence/candidates without bypassing canonical governance.

### Build 5 — Probabilistic extraction/reconciliation assistance

Introduce LLM/model assistance below the canonical boundary.

### Build 6 — Governed promotion and review workflow

Implement promotion, rejection, correction, merge/split, provenance history, and review.

### Build 7 — Query/context service

Expose enterprise query contracts to humans, Executive Judgment, and future agents.

### Build 8 — Expand domain modules

Add richer finance, workforce, compliance, delivery, and technology behavior without changing kernel semantics except through governed versioned evolution.

---

## 7. Working mode

### ChatGPT / KOE thread

Owns semantic architecture, object/link definitions, invariants, correction rules, acceptance semantics, and architecture decisions.

### GitHub

Is the durable source of truth for specifications, ADRs, contracts, fixtures, and implementation changes.

### Codex

Implements the contracts, runs tests, refactors code, and raises semantic ambiguities rather than inventing ontology behavior.

---

## 8. Non-negotiable build loop

```text
DEFINE SEMANTICS
    -> WRITE ACCEPTANCE TESTS
    -> IMPLEMENT
    -> RUN ACROSS MULTIPLE DOMAINS
    -> FIND FAILURE / AMBIGUITY
    -> CORRECT SPEC OR CODE
    -> RE-RUN
```

The implementation is incremental. The architecture is enterprise-wide.
