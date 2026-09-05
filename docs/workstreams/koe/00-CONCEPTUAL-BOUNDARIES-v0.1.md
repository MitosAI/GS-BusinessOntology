# KOE Conceptual Boundary Memo — Business Reality and Adjacent Models

**Version:** v0.2  
**Status:** Architecture direction confirmed by owner  
**Owner:** Knowledge & Ontology Engineering (KOE-001)  
**Scope:** Establishes the current conceptual model and retires `World Model` as the primary organizing term.

---

## 1. Architecture correction

The repository contains an earlier generation of terminology in which **World Model** attempted to cover both internal operating reality and material external reality.

That label no longer matches the architecture we are actively designing.

The system has already decomposed reality, intent, capability, judgment, action, and learning into distinct models with different semantics, authority rules, security requirements, and update tempos. Recombining them conceptually under a single `World Model` umbrella now reduces clarity.

Therefore:

> **`World Model` is retired as the primary current architectural concept.**

Older documents may continue to contain the term until they are revised, but new work should not use `World Model` as the organizing abstraction.

---

## 2. Current top-level operating architecture

```text
BUSINESS INTENT
What do we seek, prefer, value, constrain, and prioritize?
        |
        +---------------------+
        |                     |
        v                     v
BUSINESS REALITY       EXTERNAL REALITY
What is operationally  What material conditions
true about GenSigma?   exist outside GenSigma?
        |                     |
        +----------+----------+
                   |
                   v
             CAPABILITY
      What can GenSigma actually do
      now, with what resources,
      capacity, authority, and timing?
                   |
                   v
          EXECUTIVE JUDGMENT
      Evidence + uncertainty + intent
      + capability + policy + risk
                   |
                   v
       DECISION / APPROVAL
                   |
                   v
          GOVERNED ACTION
                   |
                   v
          NEW BUSINESS STATE
                   |
                   v
          OUTCOME / LEARNING
                   |
                   +----> updates the relevant model(s)
```

The models are connected, but they are not collapsed into one generic representation.

---

## 3. Model boundaries

### 3.1 Business Intent

**Question:** What does GenSigma seek, prefer, value, constrain, and prioritize?

Includes purpose, vision, mission, strategy, goals, initiatives, target markets, policies, risk appetite, decision criteria, and approved strategic assumptions.

Business Intent is **normative**. It describes what the company wants and how choices should be judged.

It must not be overwritten merely because current reality changes.

---

### 3.2 Business Reality

**Question:** What is operationally true about GenSigma and its direct business relationships, now and historically?

Includes canonical organizations, people, relationships, opportunities, solicitations, agreements, projects, artifacts, events, decisions, actions, outcomes, obligations, risks, and state transitions.

Business Reality is:

- evidence-backed;
- temporally native;
- security-aware;
- identity-reconciled;
- operational;
- suitable for governed use by humans and AI.

**Build Spec 001 targets Business Reality.**

---

### 3.3 External Reality

**Question:** What material conditions, actors, changes, and evidence outside GenSigma could affect decisions, risk, opportunity, or capability?

Includes customer conditions, procurement changes, regulation, technology shifts, competition, public funding, labor-market conditions, political/administrative changes, and other external factors when materially relevant.

The preferred term is **External Reality**, not `External World Model`, unless a future implementation specifically needs a governed strategic belief layer distinguished from raw external evidence.

External evidence may change continuously. Governed strategic beliefs derived from that evidence should update more deliberately.

Build Spec 001 does not attempt broad external sensing. It includes external evidence only where necessary to resolve the selected commercial episode, such as a customer-issued solicitation or addendum.

---

### 3.4 Capability

**Question:** What can GenSigma actually execute, with what resources, capacity, qualifications, authority, dependencies, and timing?

Capability is not aspiration and not a generic copy of Business Reality.

Business Reality provides many underlying resources and evidence: People, Credentials, Agreements, Assets, Partner Relationships, Availability, Capacity observations, and so on.

The Capability model expresses the **decision-relevant ability to act** using those resources.

---

### 3.5 Executive Judgment

**Question:** Given Business Intent, Business Reality, External Reality, Capability, policy, authority, risk, and uncertainty, what should be recommended or decided?

The judgment method belongs to the Executive Cognition / Decision Engine workstream.

Its outputs are nevertheless represented in the operational ontology when they have business significance:

- Assessment;
- Alternative;
- Recommendation;
- Decision;
- Approval;
- Action;
- Outcome.

The ontology owns the semantic contract for these resources; the Decision Engine owns how judgment is computed.

---

## 4. Why retiring `World Model` improves the design

### Different epistemic roles

- Business Reality represents governed operational truth.
- External Reality contains observations and governed interpretations about the environment.
- Intent represents desired direction.
- Capability represents feasible action capacity.

They should not share one undifferentiated truth model.

### Different update tempos

```text
Business Reality       -> often fast
External observations  -> continuous
External strategic belief -> slower/governed
Capability             -> changes with resources/time
Business Intent        -> deliberate/governed
```

### Different authority rules

A signed agreement may define Business Reality. A government publication may support External Reality. A leadership-approved strategy defines Business Intent. A resource/capacity assessment contributes to Capability.

There is no single source-authority hierarchy that cleanly spans them all.

### Better decision architecture

Executive Judgment becomes clearer when it explicitly consumes distinct inputs instead of receiving a monolithic `World Model` whose contents have mixed semantics.

---

## 5. Terminology rule going forward

Use:

- **Business Intent**
- **Business Reality**
- **External Reality**
- **Capability**
- **Executive Judgment / Decision Engine**
- **Governed Action**
- **Outcome / Learning**

Do not introduce `World Model` in new specifications, APIs, service names, repository paths, or implementation components unless referring to a legacy document that still carries the old terminology.

Where an older document says `World Model`, interpret it contextually and migrate its semantics into the appropriate current model rather than performing a blind rename.

---

## 6. Boundary tests

| Example | Primary model | Reason |
|---|---|---|
| `GenSigma is pursuing SFO solicitation X` | Business Reality | current commercial state |
| `Grow repeatable SLED AI offerings` | Business Intent | strategic preference |
| `SFO issued an addendum changing the deadline` | External evidence linked into Business Reality | external event changes active business context |
| `California procurement policy is shifting toward AI assurance` | External Reality | material environmental condition |
| `CRI has three available ServiceNow specialists this month` | Capability | feasible execution capacity |
| `Proceed with CRI as teaming partner` | Decision resource | operationally significant choice |
| `Send MNDA to CRI` | Governed Action | business verb changing state |
| `Proposal was submitted on date X` | Business Reality Event + state change | historical operational fact |

---

## 7. Workstream interfaces

### Knowledge & Ontology Engineering owns

- Business Reality semantics;
- canonical identity and contextual role semantics;
- evidence/provenance semantics;
- temporal semantics;
- relationship semantics;
- Event / Decision / Action / Outcome resource semantics;
- promotion rules;
- semantic security requirements;
- query/workload contracts;
- interfaces among Business Reality, Intent, External Reality, Capability, and Decision resources.

### Executive Cognition consumes

- Business Reality;
- External Reality where material;
- Business Intent;
- Capability;
- evidence and uncertainty;
- policies and authority;
- available governed actions.

### Evidence/Data Engineering consumes

- extraction targets;
- evidence and candidate structures;
- lineage/provenance requirements;
- context/identity semantics;
- security classifications.

### Platform Engineering consumes

- semantic/query requirements;
- consistency and transactional requirements;
- temporal requirements;
- graph/traversal requirements;
- security requirements;
- search and audit requirements.

Physical database choice remains outside KOE authority.

---

## 8. Migration implications

The following existing artifacts require later foundation-level reconciliation:

- `docs/specs/01-WORLD-MODEL-SPEC-v0.1.md`;
- ADR-003 and ADR-004 language in `07-FOUNDATIONAL-ARCHITECTURE-DECISIONS-v0.1.md`;
- roadmap references to `World Model` where they mean Business Reality;
- any role charter or architecture diagram still treating `World Model` as a peer input.

Migration should preserve the durable ideas in those documents—evidence-before-truth, identity reconciliation, temporal state, operational ontology, external materiality, security, decision traces, and kinetic actions—while redistributing them into the current model boundaries.

This is a semantic migration, not a find-and-replace exercise.

---

## 9. Build Spec 001 working decision

Build Spec 001 is explicitly a **Business Reality MVP**.

Its core path remains:

```text
OUTLOOK + SHAREPOINT
        |
        v
RAW / NORMALIZED EVIDENCE
        |
        v
OBSERVATIONS / CLAIMS / CANDIDATES
        |
        v
IDENTITY + CONTEXT + ARTIFACT RECONCILIATION
        |
        v
CANONICAL BUSINESS REALITY
        |
        v
QUERY / CONTEXT API
```

No `World Model` abstraction is required to implement or explain this slice.
