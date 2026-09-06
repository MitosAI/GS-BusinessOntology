# GenSigma AI-Native Operating System — Project Brief

**Version:** v0.1  
**Status:** Working program brief  
**Audience:** All GenSigma OS workstreams, architecture threads, research threads, engineering threads, and future contributors  
**Governing source:** `CONSTITUTION.md` and approved ADRs/specifications in this repository

---

## 1. Program mission

GenSigma is building an AI-native operating system for the company: a governed operating layer in which the business is represented, reasoned over, acted upon, and continuously learned from through one coherent semantic and decision architecture.

This is not a chatbot project, not a document-search project, not an agent wrapper, and not an LLM bolted onto existing software.

The long-term objective is to build a system capable of progressively assuming much of the executive and operational cognition currently performed by the founder and leadership team. The system should be able to understand the state of the business, understand the portion of the external world that materially affects the business, reason in light of GenSigma's intent, evaluate alternatives under uncertainty, recommend or make governed decisions, execute approved actions, observe outcomes, and learn.

A useful shorthand for the ambition is:

> **Build the operating brain of GenSigma, not an AI assistant sitting beside GenSigma.**

---

## 2. North-star operating equation

The operating system reasons from three primary models:

```text
BUSINESS INTENT MODEL        BUSINESS REALITY MODEL        CAPABILITY MODEL
Who are we?                  What is actually true          What can we actually
What do we seek?             inside the business?          do, with what resources,
What do we value?                                          constraints and authority?
What are our goals?
What beliefs guide us?
             \                    |                    /
              \                   |                   /
               +--------- EXECUTIVE DECISION ENGINE --------+
                                  |
                                  v
                       RECOMMENDATION / DECISION
                                  |
                                  v
                           GOVERNED ACTION
                                  |
                                  v
                           NEW BUSINESS STATE
                                  |
                                  v
                            OUTCOME / LEARNING
```

The system must also maintain a **material external world model**: a structured representation of external conditions, actors, trends, regulations, market shifts, technology developments, customer changes, competitive moves, and other environmental factors that materially affect GenSigma.

That external model is not a generic news feed. It is a filtered, evidence-backed model of the outside world relevant to GenSigma's intent and decisions.

---

## 3. The four conceptual layers we must keep distinct

### 3.1 Business Intent

Business Intent describes the desired direction of the company and the operating semantics through which choices are judged.

It includes, over time:

- purpose, mission, vision and values;
- business model and value proposition;
- business units, practices and offerings;
- target markets and customer segments;
- strategic priorities and strategic themes;
- goals, OKRs, targets and time horizons;
- risk appetite and decision principles;
- preferred trade-offs;
- strategic beliefs and explicit assumptions;
- plans, initiatives and commitments;
- constraints imposed by ownership, capital, regulation, reputation or culture.

Business Intent is not the same thing as current reality. It describes what GenSigma seeks to become and how it wants to behave.

### 3.2 Business Reality

Business Reality describes what is actually happening inside and immediately around the company.

Examples:

- organizations, customers, partners, vendors and regulators;
- people, roles, employment and stakeholder relationships;
- opportunities, solicitations, proposals and agreements;
- projects, assignments, deliverables and milestones;
- invoices, receivables, bills and payments;
- systems, assets, subscriptions and capabilities;
- events, states, obligations, risks and issues;
- decisions, approvals, actions and outcomes;
- historical state and temporal changes.

Business Reality is evidence-backed and operational. It is the state the system uses when asking, "What is true about GenSigma now, and how did we get here?"

### 3.3 External World Model

The External World Model describes the portion of external reality that is materially relevant to GenSigma.

Examples:

- customer budgets and procurement patterns;
- legislation and regulatory changes;
- market demand and public-sector funding;
- competitive moves;
- technology shifts;
- labor-market changes;
- partner capability changes;
- relevant political or administrative shifts;
- macroeconomic factors when material to GenSigma decisions.

The external world creates entropy continuously. The OS should observe broadly enough to detect relevant change, compress that entropy, identify what matters, and propose updates to the governed external model.

The strategic worldview should not thrash every day. Operational observations may change continuously; material strategic beliefs should change more deliberately through governed review.

### 3.4 Executive Decision / Judgment Engine

The Decision Engine is the computational counterpart of executive judgment.

Its job is not merely to retrieve facts. It evaluates courses of action under incomplete information and uncertainty, using Business Intent to define what "better" means.

It will likely combine multiple disciplines rather than one universal method, including:

- Bayesian belief updating;
- decision theory and expected utility;
- operations research and optimization;
- game theory and strategic interaction;
- control theory and feedback;
- causal reasoning;
- bounded-rationality and behavioral decision science;
- AI/LLM reasoning for unstructured interpretation and hypothesis generation.

The exact composition is deliberately not frozen yet. `RESEARCH-001` exists to establish its intellectual foundation before we over-engineer the Decision Engine.

---

## 4. Palantir-style operational ontology as the spine

The governing architectural doctrine remains a Palantir-style operational ontology.

The ontology is not merely a semantic catalog. It must eventually unite:

```text
WORLD
what exists and how it is related

+

TIME / EVENTS
what happened and how state changed

+

DECISION
what was assessed, recommended, chosen and approved

+

KINETIC ACTION
what the system or people can actually do

+

OUTCOMES / LEARNING
what resulted and what should influence future choices
```

This is why the system must preserve **nouns and verbs**.

An `Opportunity` is incomplete as an operational concept if the platform cannot eventually expose governed actions such as `QualifyOpportunity`, `ApproveBid`, `RequestPartnerPricing`, `SubmitProposal`, or `ConvertAwardToProject`.

---

## 5. Deterministic core, probabilistic edges

The desired system is primarily deterministic where determinism is available and valuable.

Examples of deterministic or strongly typed behavior:

- identity and authorization;
- schema and object typing;
- allowed state transitions;
- policy enforcement;
- workflow preconditions;
- source provenance;
- temporal history;
- auditable actions;
- business rules;
- financial calculations;
- permissions and approvals.

Probabilistic methods are used where reality is uncertain or unstructured:

- entity resolution;
- interpretation of email/documents;
- inference from incomplete evidence;
- confidence scoring;
- prediction;
- scenario assessment;
- causal hypotheses;
- language understanding;
- judgment under uncertainty.

The probabilistic layer must not silently erase the deterministic one.

---

## 6. Source systems are sensors, not the ontology

Initial sensors are Outlook/Exchange and SharePoint. Later sensors may include CRM, QuickBooks, Bill.com, treasury, HR, project systems, procurement portals, public sources and other applications.

Source data follows this conceptual promotion path:

```text
SOURCE
  -> RAW EVIDENCE
  -> OBSERVATION / CLAIM / CANDIDATE
  -> CONTEXT + IDENTITY RECONCILIATION
  -> VALIDATION / AUTHORITY / GOVERNANCE
  -> CANONICAL BUSINESS REALITY
```

A source proves what that source recorded. It does not automatically define operational truth.

---

## 7. Evidence, identity and history are first-class

The OS must preserve:

- provenance;
- source identity;
- source timestamps;
- effective/business time;
- discovery time;
- confidence;
- authority;
- explicit versus inferred status;
- contradictory evidence;
- reconciliation history;
- reversible merge/split behavior;
- document/version lineage.

The core identity rule is:

> **Never let a newly discovered name automatically become a new canonical object. Reconcile first.**

The core evidence rule is:

> **Source observations are immutable; canonical interpretation is revisable.**

---

## 8. Security is architectural, not cosmetic

Security is part of the ontology and operating model itself.

The system must ultimately support appropriate combinations of:

- user identity;
- role;
- business function;
- delegated authority;
- object-level access;
- property-level access where necessary;
- evidence-level access;
- action permissions;
- need-to-know restrictions;
- domain restrictions for HR, legal, finance, security and executive strategy;
- human approval gates;
- agent-specific scopes.

AI agents are governed actors, not superusers.

---

## 9. Learning loop

The long-term OS must be recursively learning, but learning must be governed.

A useful operating loop is:

```text
INTENT
  -> OBSERVE
  -> ORIENT
  -> DECIDE
  -> ACT
  -> VERIFY
  -> LEARN
  -> UPDATE RELEVANT MODELS
  -> REPEAT
```

This is inspired by OODA but makes learning explicit.

Operational state may update frequently. Strategic beliefs and Business Intent should update more deliberately and through appropriate review.

---

## 10. Current program phase

We are not yet building the full GenSigma OS.

We are building the **World Model / Business Reality foundation** and simultaneously researching the **Executive Decision Engine**.

Two workstreams therefore run in parallel:

### Track A — Deterministic / World Model Foundation

- ontology refinement;
- business reality model;
- evidence model;
- source connectors;
- identity/context reconciliation;
- storage/query architecture;
- Azure platform foundation;
- security model;
- first end-to-end vertical slice.

### Track B — Executive Cognition / Decision Research

- study how high-quality human and machine decision systems operate;
- examine formal decision science and practical executive judgment;
- determine what parts should be deterministic, probabilistic, optimization-based, game-theoretic, or LLM-assisted;
- produce a computational architecture for GenSigma executive judgment.

Neither track should block the other. Their contract is explicit: Track A exposes reliable state, evidence, intent and capability inputs; Track B defines how the Decision Engine consumes those inputs and produces auditable recommendations/decisions.

---

## 11. Immediate MVP target

The first engineering MVP is not a generic AI agent.

It should prove that GenSigma can build a trustworthy business-reality foundation from real sources.

Initial scope:

```text
OUTLOOK + SHAREPOINT
        |
        v
RAW EVIDENCE
        |
        v
NORMALIZATION / EXTRACTION
        |
        v
EVIDENCE GRAPH / CANDIDATES
        |
        v
IDENTITY + CONTEXT RECONCILIATION
        |
        v
CANONICAL BUSINESS REALITY / WORLD MODEL
        |
        v
QUERY / CONTEXT API
```

The pilot should be narrow enough to build quickly but rich enough to pressure-test identity, time, evidence, relationships, decision traces and security.

---

## 12. What is deliberately not decided

The following remain open until the evidence and required query patterns justify a decision:

- physical database technology;
- relational versus graph-native primary persistence;
- vector/search architecture;
- exact Azure service selection;
- exact entity-resolution algorithms;
- universal confidence thresholds;
- whether `DecisionTrace` is a persistent object or a computed traversal;
- exact harness/framework selection for the full OS;
- degree of agent autonomy;
- final executive-cognition architecture.

Do not fill these gaps by fashion or convenience.

---

## 13. Program working method

1. **Architecture conversation is the workshop.**
2. **GitHub is the durable source of truth.**
3. Important decisions become Constitution amendments, ADRs, specs, research artifacts or build specs.
4. Each parallel thread gets a role charter and reads this brief before beginning.
5. Threads may propose decisions; cross-cutting architectural decisions return to the Chief Architect thread.
6. Real GenSigma evidence should pressure-test the architecture continuously.
7. We prefer a thin working vertical slice over a huge speculative implementation.
8. We do not silently drift from previously approved doctrine.

---

## 14. Success definition

The program succeeds when GenSigma has an operating system in which:

- the company and its material environment are represented coherently;
- every material belief can be traced to evidence;
- uncertainty is explicit rather than hidden;
- intent is represented explicitly;
- judgment can be computationally assisted and eventually partially automated;
- decisions are auditable;
- actions are typed, governed and authorized;
- outcomes feed learning;
- humans and AI operate through the same business semantics;
- the system can progressively perform executive and operational work currently dependent on individual memory and judgment.

That is the north star for every workstream.