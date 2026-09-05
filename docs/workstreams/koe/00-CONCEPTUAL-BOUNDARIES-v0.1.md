# KOE Conceptual Boundary Memo — Business Reality and Adjacent Models

**Version:** v0.1  
**Status:** Workstream proposal for Chief Architect review  
**Owner:** Knowledge & Ontology Engineering (KOE-001)  
**Scope:** Terminology reconciliation only; no foundational doctrine is amended by this memo.

---

## 1. Problem

The repository currently uses two generations of terminology:

1. earlier foundation documents use **World Model** as one coherent model covering both internal and material external reality;
2. newer program documents distinguish **Business Reality** from an **External World Model**, while keeping Business Intent and Capability as peer inputs to Executive Judgment.

Build Spec 001 needs an unambiguous boundary without silently rewriting approved doctrine.

---

## 2. Working boundary for KOE and Build Spec 001

### Business Intent

**Question:** What does GenSigma seek, prefer, value, constrain, and prioritize?

Includes purpose, vision, mission, strategy, goals, initiatives, target markets, policies, risk appetite, decision criteria, and approved strategic assumptions.

**Not Business Reality:** a target, policy, or strategic preference remains normative even when current reality differs from it.

### Business Reality

**Question:** What is operationally true about GenSigma and its direct business relationships, now and historically?

Includes canonical organizations, people, relationships, opportunities, solicitations, agreements, projects, artifacts, events, decisions, actions, outcomes, obligations, operational risks, and state transitions.

Business Reality is evidence-backed, temporally native, security-aware, and suitable for governed operational use.

**Build Spec 001 targets this model.**

### External World Model

**Question:** What material external conditions or beliefs could change GenSigma's decisions, risk, opportunity, or capability?

Includes external customer conditions, procurement changes, regulation, technology shifts, competitive moves, funding, labor-market conditions, and other selected external factors.

Raw external observations are not strategic beliefs. Promotion into the governed external model requires materiality and evidence.

**Out of scope for Build Spec 001 except where an external artifact directly defines the business context**, such as a customer-issued solicitation or procurement addendum.

### Capability Model

**Question:** What can GenSigma actually execute, with what resources, capacity, qualifications, authority, dependencies, and timing?

Capability is descriptive but purpose-specific: it represents feasible action capacity, not the full operational state of the company.

Business Reality may provide underlying evidence and state (for example, a Person, Credential, Agreement, or Capacity observation), while the Capability Model represents the decision-relevant ability derived from or linked to those resources.

### Executive Decision / Judgment

**Question:** Given Intent, Reality, External World, Capability, policies, authority, risk, and uncertainty, what should be recommended or decided?

Decision resources such as Assessment, Recommendation, Decision, Approval, and Action are represented in the operational ontology for traceability, but the **judgment method** that creates them belongs to the Decision Engine workstream.

---

## 3. Recommended terminology rule

Until the Chief Architect resolves the older/newer naming at foundation level:

- use **Business Reality** for the operational internal/direct-relationship state targeted by Build Spec 001;
- use **External World Model** for governed material external reality/beliefs;
- use **World Model** only when referring to the older foundation specification or as a historical umbrella term for reality modeling;
- do not treat Business Intent or Capability as subdomains of Business Reality;
- do not treat Executive Judgment as a state domain, even though its outputs are represented as first-class ontology resources.

This rule is intentionally conservative: it enables implementation work without changing ADR-004 or rewriting `01-WORLD-MODEL-SPEC-v0.1.md` inside this workstream.

---

## 4. Boundary tests

| Example | Primary model | Reason |
|---|---|---|
| "GenSigma is pursuing SFO solicitation X" | Business Reality | current commercial state |
| "Grow repeatable SLED AI offerings" | Business Intent | strategic preference |
| "SFO published an addendum changing the deadline" | Business Reality evidence + external source | external source directly changes an active internal context |
| "California procurement policy is shifting toward AI assurance" | External World Model | material external condition/belief |
| "CRI has three available ServiceNow specialists this month" | Capability Model, evidence-linked to Business Reality | current feasible capacity |
| "Proceed with CRI as teaming partner" | Decision resource in Business Reality; judgment owned by Decision Engine | choice must be traceable operationally |
| "Send MNDA to CRI" | Action resource in Business Reality / Kinetic layer | governed business verb |
| "Proposal was submitted on date X" | Event + state change in Business Reality | historical operational fact |

---

## 5. Interface implications

### KOE provides

- canonical Business Reality semantics;
- evidence and provenance semantics;
- identity/context reconciliation semantics;
- temporal and security semantics;
- decision-trace resource shapes;
- query and workload contracts.

### Executive Cognition consumes

- current/historical Business Reality;
- evidence and uncertainty;
- decision-trace resources;
- links to Business Intent and Capability;
- available action definitions.

### Evidence/Data Engineering consumes

- extraction targets;
- candidate structures;
- lineage and provenance requirements;
- context-resolution inputs;
- security labels.

### Platform Engineering consumes

- query, consistency, temporal, transactional, graph/traversal, search, audit, and permission requirements;
- no database mandate from KOE.

---

## 6. Proposed Chief Architect decision

The Chief Architect should later choose one of two documentation strategies:

**Option A — Preserve World Model as umbrella.** Define Business Reality and External World Model as two governed domains inside the broader World Model.

**Option B — Retire World Model as the primary current term.** Use Business Reality and External World Model as peer models and mark `01-WORLD-MODEL-SPEC-v0.1.md` as legacy terminology pending revision.

KOE does **not** select between these options in this memo because that would change cross-workstream doctrine.

---

## 7. Build Spec 001 working decision

No blocker exists for M2. Build Spec 001 will use **Business Reality MVP** as its explicit scope and will model only the external facts necessary to resolve the selected commercial episode. This is compatible with both documentation strategies above.
