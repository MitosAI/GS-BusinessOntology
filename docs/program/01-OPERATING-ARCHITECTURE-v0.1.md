# GenSigma AI-Native Operating System — Operating Architecture

**Version:** v0.1  
**Status:** Working architecture  
**Governing source:** `CONSTITUTION.md` and approved ADRs/specifications

---

## 1. Architecture objective

The GenSigma OS must provide one coherent operating architecture from evidence to state to judgment to action to learning.

It is designed around a Palantir-style operational ontology, but the full OS is broader than the ontology itself.

The architecture separates durable business semantics from interchangeable infrastructure and AI runtime choices.

---

## 2. Top-level model

```text
                                GENSIGMA OS

  +-----------------------------------------------------------------------+
  |                     CONTROL & GOVERNANCE                              |
  | Identity | security | policy | approval | audit | risk | authority    |
  +-----------------------------------------------------------------------+
                                  |
                                  v
  +-----------------------------------------------------------------------+
  |                    BUSINESS INTENT MODEL                              |
  | Who we are | what we do | what we seek | plans | goals | beliefs     |
  | strategic priorities | values | risk appetite | decision principles  |
  +-----------------------------------------------------------------------+
                                  |
                +-----------------+------------------+
                |                                    |
                v                                    v
  +----------------------------------+   +---------------------------------+
  |      BUSINESS REALITY MODEL      |   |      EXTERNAL WORLD MODEL       |
  | Current/historical state of      |   | Material outside reality:       |
  | GenSigma and direct relationships|   | market, policy, technology,      |
  |                                  |   | customers, competition, macro    |
  +----------------------------------+   +---------------------------------+
                |                                    |
                +-----------------+------------------+
                                  |
                                  v
  +-----------------------------------------------------------------------+
  |                      CAPABILITY MODEL                                 |
  | People | skills | money | systems | capacity | authority | assets     |
  | constraints | timing | partner capacity | feasible actions             |
  +-----------------------------------------------------------------------+
                                  |
                                  v
  +-----------------------------------------------------------------------+
  |                EXECUTIVE DECISION / JUDGMENT ENGINE                   |
  | Belief update | alternatives | utility | uncertainty | game theory    |
  | optimization | causal reasoning | policy | recommendation | decision   |
  +-----------------------------------------------------------------------+
                                  |
                                  v
  +-----------------------------------------------------------------------+
  |                      KINETIC ACTION LAYER                             |
  | Typed actions | preconditions | approvals | tool control | writebacks |
  | workflow | APIs | connectors | agents | human execution               |
  +-----------------------------------------------------------------------+
                                  |
                                  v
                         REAL-WORLD STATE CHANGE
                                  |
                                  v
  +-----------------------------------------------------------------------+
  |                       OUTCOMES & LEARNING                             |
  | Verification | outcome | performance | feedback | model updates       |
  +-----------------------------------------------------------------------+
                                  |
                                  +---------------------> next loop
```

---

## 3. Why separate Business Intent, Business Reality and External World

These three models solve different problems.

### Business Intent

Business Intent is normative. It describes the company GenSigma seeks to be and the outcomes it seeks to create.

It should not be overwritten simply because the world changed yesterday.

### Business Reality

Business Reality is descriptive. It describes the actual state of GenSigma, its relationships, commitments, resources, work, finances, risks, events and historical trajectory.

It can change frequently because business state changes frequently.

### External World Model

The External World Model is interpretive and strategic. It represents the selected portion of external reality that materially affects GenSigma.

Raw external observations can change continuously, but the governed strategic worldview should update only when evidence warrants a material change.

This produces two tempos:

```text
FAST LOOP
new email / contract / payment / RFP / personnel event
-> update operational business state

SLOWER LOOP
accumulated market / political / technology / customer evidence
-> assess materiality
-> propose strategic worldview update
-> govern / approve
```

---

## 4. Evidence and ontology architecture

```text
OUTLOOK       SHAREPOINT       CRM       FINANCE       PUBLIC SOURCES
   |               |            |            |                |
   +---------------+------------+------------+----------------+
                                  |
                                  v
                         SOURCE CONNECTORS
                                  |
                                  v
                         RAW EVIDENCE STORE
                                  |
                                  v
                    NORMALIZATION / EXTRACTION
                                  |
                                  v
                    ENTERPRISE EVIDENCE GRAPH
                observations | claims | candidates
                ambiguity | confidence | provenance
                                  |
                                  v
                         ONTOLOGY TOOLCHAIN
                identity reconciliation | context
                authority | chronology | validation
                merge/split | security | proposals
                                  |
                                  v
                     CANONICAL OPERATIONAL ONTOLOGY
                                  |
          +-----------------------+--------------------------+
          |                       |                          |
          v                       v                          v
      BUSINESS STATE         DECISION FABRIC            CONTROL
      objects/links          evidence/assessment        policies
      temporal state         alternatives               constraints
      relationships          recommendations            approvals
      events                 decisions                  authority
                             outcomes                    security
                                  |
                                  v
                           TYPED ACTIONS
```

Key invariant:

> Discovery observes and proposes. The canonical ontology defines and governs.

---

## 5. Evidence classes

The system should distinguish at least:

- **Raw Source Record** — source bytes/metadata as received.
- **Observation** — direct extraction from source.
- **Claim** — proposition asserted by a source or model.
- **Evidence** — source supporting or contradicting a claim.
- **Candidate Identity / Relationship / Event / Context** — proposed interpretation.
- **Assessment** — reasoned evaluation of evidence.
- **Canonical State** — accepted operational representation.

AI inference must always be distinguishable from source assertion and canonical fact.

---

## 6. Business Reality structure

Business Reality should represent the company through stable, business-native concepts rather than source-system replicas.

Representative domains:

### Organization and legal structure

- Enterprise
- Legal Entity
- Organizational Unit
- Registered Office
- Operating Location
- Foreign Registration / Qualification

### Parties and relationships

- Organization
- Person
- Business Relationship
- Employment Relationship
- Partner Relationship
- Customer Relationship
- Vendor Relationship
- Regulatory Relationship
- Ownership / Investment Relationship

### Commercial

- Market
- Customer Segment
- Account
- Stakeholder
- Opportunity
- Solicitation
- Proposal
- Agreement
- Contract Vehicle
- Obligation

### Delivery

- Project
- Workstream
- Deliverable
- Milestone
- Assignment
- Acceptance
- Risk
- Issue

### Financial

- Invoice
- Bill
- Payment
- Receivable
- Payable
- Budget
- Cost
- Rate

### Capability and workforce

- Person
- Position
- Position Holding
- Role
- Skill
- Capability
- Credential
- Availability
- Capacity
- Assignment

### Decision and control fabric

- Signal
- Event
- Observation
- Claim
- Evidence
- Assessment
- Assumption
- Model
- Prediction
- Alternative
- Recommendation
- Decision
- Approval
- Delegation
- Action
- Policy
- Constraint
- Risk
- Outcome
- Learning

---

## 7. External World Model architecture

External observations should not directly change strategic beliefs.

```text
EXTERNAL SOURCES
      |
      v
OBSERVATIONS
      |
      v
MATERIALITY FILTER
"Could this affect GenSigma intent, risk, capability or opportunity?"
      |
      +--> NO -> archive/search only
      |
      +--> YES
             |
             v
       EVIDENCE CLUSTER
             |
             v
    INTERPRETATION / ASSESSMENT
             |
             v
    STRATEGIC BELIEF PROPOSAL
             |
             v
    GOVERNANCE / HUMAN REVIEW
             |
             v
    EXTERNAL WORLD MODEL UPDATE
```

The system should preserve prior strategic beliefs and the evidence that caused them to change.

---

## 8. Executive judgment architecture — current hypothesis

The Decision Engine is not yet frozen. The working architecture is a composition of methods rather than one monolithic AI model.

```text
INPUTS
Business Intent
Business Reality
External World Model
Capability Model
Current Trigger / Decision Context
        |
        v
BELIEF / UNCERTAINTY UPDATE
Bayesian methods where appropriate
        |
        v
ALTERNATIVE GENERATION
rules + retrieval + LLM + planners
        |
        v
EVALUATION
utility / goals / constraints / risk
        |
        v
STRATEGIC INTERACTION
counterparty reactions / game theory when material
        |
        v
OPTIMIZATION
operations research / resource allocation when material
        |
        v
RECOMMENDATION
with rationale, assumptions, confidence, alternatives
        |
        v
DECISION / APPROVAL
human or delegated authority
```

`RESEARCH-001` will determine which pieces are universal, which are decision-class-specific, and which should remain human-led.

---

## 9. Kinetic layer

The system must ultimately be able to act on its own semantic model.

A typed action is the bridge between cognition and the real business.

Example:

```text
ApproveBid(
  opportunity_id,
  approver_id,
  decision_id,
  approved_budget,
  conditions
)
```

An action may enforce:

- authorization;
- policy;
- preconditions;
- required evidence;
- required approvals;
- valid state transition;
- side effects;
- audit record;
- writeback to source systems;
- compensating action.

Material state changes should not be reduced to arbitrary field updates.

---

## 10. Context and execution graphs are different

The architecture must distinguish:

### World / business graph

Represents reality:

```text
GenSigma
  -> pursues -> Opportunity
  -> serves  -> Customer
Opportunity
  -> involves -> Partner
  -> governed_by -> Solicitation
```

### Execution graph

Represents work to perform:

```text
Assess opportunity
  -> collect missing evidence
  -> identify partners
  -> evaluate options
  -> request approval
  -> execute action
  -> verify result
```

The harness may generate an execution graph dynamically, but it must read and write through the governed business semantics.

---

## 11. Organizational knowledge versus agent memory

The OS must distinguish shared organizational truth from local agent experience.

```text
AGENT EXPERIENCE
      |
      v
CANDIDATE LEARNING
      |
      v
VALIDATION / PROMOTION
      |
      +--> Skill / Procedure
      +--> Organizational Knowledge
      +--> Policy / Model update
```

An agent's memory must never silently become company truth.

---

## 12. Security architecture

Security must apply at every layer:

```text
Identity / Entra
      |
      v
Security Context
      |
      +--> object permissions
      +--> property permissions
      +--> evidence permissions
      +--> action permissions
      +--> delegated authority
      +--> need-to-know
```

The same canonical object may expose different detail depending on actor authority.

Example:

- `Person unavailable through Friday` may be visible to a manager.
- the medical email supporting that state may remain HR-only.

---

## 13. MVP architecture boundary

The first MVP should stop before full autonomous decision execution.

```text
OUTLOOK + SHAREPOINT
      |
      v
RAW EVIDENCE
      |
      v
EXTRACTION
      |
      v
EVIDENCE GRAPH
      |
      v
IDENTITY / CONTEXT RECONCILIATION
      |
      v
CANONICAL BUSINESS REALITY
      |
      v
QUERY / CONTEXT API
      |
      v
HUMAN + AI REASONING / PROPOSALS
```

A later MVP can add the first governed typed action.

---

## 14. Physical architecture principles

Physical technology remains subordinate to logical requirements.

Storage selection must support at minimum:

- strong identity lookup;
- temporal history;
- complex relationships;
- graph-like traversals;
- strong transactional semantics for canonical state;
- provenance;
- security-aware retrieval;
- evidence lineage;
- full-text and semantic retrieval;
- typed action writes;
- auditability.

The architecture may be polyglot if necessary, but semantic duplication must be controlled. A graph database, relational database, vector store, object store or search engine is an implementation component, not the ontology.

---

## 15. Cloud principle

Azure is the pragmatic initial cloud because GenSigma already operates heavily in Microsoft 365 and Entra identity.

Cloud choice must not leak into the semantic model.

Expected implementation areas include:

- Entra ID for identity;
- Key Vault for secrets;
- object/blob storage for immutable evidence;
- managed compute for connectors/services;
- managed database services selected after Build Spec requirements;
- logging/telemetry;
- private networking and least-privilege service identities.

Exact services remain ADR decisions.

---

## 16. Architecture invariants

1. Business semantics are not owned by source systems.
2. Evidence is not automatically truth.
3. Identity is canonical and reconciliation is continuous.
4. Time is first-class.
5. Decisions, events, actions and outcomes remain distinct.
6. Material writes become governed typed actions.
7. Security is semantic and end-to-end.
8. AI is a governed actor.
9. External entropy is filtered by materiality.
10. Operational state may update rapidly; strategic beliefs update deliberately.
11. Learning is explicit and provenance-preserving.
12. Physical technology may change without changing the business semantics.
13. The full OS must remain deterministic where possible and probabilistic where necessary.
14. Every workstream must remain traceable to the Constitution and project brief.
