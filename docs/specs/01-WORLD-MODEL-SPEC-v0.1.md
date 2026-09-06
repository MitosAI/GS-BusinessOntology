# GenSigma World Model Platform Specification

**Version:** v0.1  
**Status:** Draft for architectural review  
**Governing document:** `CONSTITUTION.md`  
**Governing doctrine:** Palantir-style operational ontology  
**Primary purpose:** Define the logical architecture of the GenSigma World Model Platform before physical database selection or implementation.

---

## 1. Purpose

The GenSigma World Model Platform is the durable operational representation of the portion of reality that materially affects GenSigma.

It exists so that humans and AI do not repeatedly reconstruct the company from prompts, disconnected applications, documents, and memory. Instead, the operating system maintains an evidence-backed, temporally aware, governed model of the business and the external environment that matters to it.

The World Model answers five fundamental questions:

1. **What exists?**
2. **How is it related?**
3. **What is true now, and what was true before?**
4. **What happened, what was decided, and what action followed?**
5. **What resulted?**

The World Model is not intended to model the entire universe. It models the slice of reality required for GenSigma to understand itself, understand material external conditions, make decisions, execute governed actions, and learn.

For V1, the expected emphasis is approximately **80% internal operating reality / 20% material external reality**. This ratio is a design bias, not a hard technical constraint.

---

## 2. Relationship to the GenSigma AI-Native Operating System

The full operating system is based on three peer models and one decision capability:

```text
BUSINESS INTENT MODEL        WORLD MODEL        CAPABILITY MODEL
What do we want?             What is true?      What can we do?
          \                      |                    /
           \                     |                   /
            +---------------- DECISION ENGINE ----------------+
                                   |
                                   v
                        RECOMMENDATION / DECISION
                                   |
                                   v
                            KINETIC ACTION
                                   |
                                   v
                           NEW WORLD STATE
                                   |
                                   v
                         OUTCOME / LEARNING
```

The World Model is descriptive and operational. It does not by itself define what GenSigma wants to achieve, and it does not by itself determine whether GenSigma has the capacity to execute a course of action.

It supplies the best governed representation of reality available to the Decision Engine.

---

## 3. One World Model, not separate internal and external models

GenSigma SHALL maintain one coherent World Model with multiple domains of reality.

### 3.1 Internal enterprise reality

Examples include legal entities, organizational units, people, roles and employment relationships, customers, partners, vendors and other business relationships, opportunities and solicitations, proposals and agreements, projects and deliverables, invoices/bills/payments, systems/assets/subscriptions, policies, risks, obligations, capabilities/resources, decisions, actions and outcomes.

### 3.2 External operating reality

Only external reality that can materially affect GenSigma decisions should be modeled. Examples include customer organizational changes, procurement releases/cancellations, public budgets and funding changes, regulations, market demand, competitive moves, partner capability changes, technology shifts, relevant political/administrative changes, and macro conditions that materially affect demand, labor, cost or funding.

The external world is not a generic news lake. External objects, events and claims must connect to a GenSigma decision, risk, opportunity, strategy, capability, relationship or monitored hypothesis to justify promotion into the operational model.

---

## 4. Five dimensions of the World Model

The Palantir-style operational ontology is treated as one coherent model with five inseparable dimensions.

### 4.1 World / Semantic dimension

Represents what exists and how it is related: Organization, Person, Opportunity, Solicitation, Agreement, Project, Document, Relationship, Capability, Location, Policy, Risk.

### 4.2 Temporal / Event dimension

Represents what happened and how state changed: opportunity discovered, RFP released, partner contacted, NDA executed, proposal submitted, interview held, award received, contract signed, employee joined, invoice issued, payment received.

### 4.3 Decision dimension

Represents how GenSigma understood a situation and made a choice: evidence, assessment, assumption, alternative, prediction, recommendation, decision, approval, delegation.

### 4.4 Kinetic dimension

Represents governed business verbs that can change reality: QualifyOpportunity, ApproveBid, AddTeamingPartner, RequestPricing, ApproveNDA, SubmitProposal, ConvertAwardToProject, IssueInvoice, EscalateReceivable.

### 4.5 Outcome / Learning dimension

Represents what resulted and what future decisions should learn from it: win/loss, revenue, margin, customer acceptance, payment delay, delivery performance, partner performance, strategic learning.

---

## 5. Evidence Graph versus Canonical Operational Ontology

The World Model Platform SHALL preserve a strict distinction between uncertainty and governed operational state.

```text
SOURCE SYSTEMS
      |
      v
RAW EVIDENCE
      |
      v
ENTERPRISE EVIDENCE GRAPH
observations / claims / candidates / ambiguity
      |
      v
RECONCILIATION + VALIDATION + GOVERNANCE
      |
      v
CANONICAL OPERATIONAL ONTOLOGY
      |
      v
ACTIONS / APPLICATIONS / AGENTS
```

The Evidence Graph is deliberately permissive and non-authoritative. It may contain duplicate identities, unresolved aliases, contradictory claims, candidate events, candidate relationships, candidate contexts, decision fragments, model-generated interpretations, confidence values, copied/quoted evidence, and supporting/contradicting evidence.

The canonical ontology contains identities, relationships, states and operational resources that the system is prepared to rely upon for governed business use. Canonical means accepted under defined source authority, confidence, reconciliation, validation and governance rules.

---

## 6. Epistemic model

The World Model MUST know the difference between what was observed, asserted, inferred and accepted.

Minimum epistemic classes:

- **Raw Record** — source artifact as obtained from a source system.
- **Observation** — directly observable metadata or content derived from a source.
- **Claim** — proposition asserted by a source or extraction process.
- **Evidence** — artifact or observation used to support or contradict a claim.
- **Candidate Fact** — proposition proposed for canonical use.
- **Canonical Fact / State** — accepted operational proposition.
- **Assessment** — reasoned interpretation of evidence.
- **Inference** — derived proposition not explicitly stated by an authoritative source.
- **Assumption** — explicit proposition used for reasoning despite uncertainty.
- **Prediction** — proposition about a future state.

Every material inference SHOULD preserve source evidence, generator/agent/model where relevant, reasoning method or function reference, timestamp, confidence, authority level, and explicit/inferred status. AI-generated content is non-authoritative by default.

---

## 7. Identity and reconciliation

Identity resolution is a core World Model capability, not a cleanup script.

```text
SOURCE OBSERVATION
      |
      v
CANDIDATE GENERATION
      |
      v
COMPARE TO KNOWN IDENTITIES
      |
      +--> SAME OBJECT
      +--> ALIAS / HISTORICAL NAME
      +--> PARENT / CHILD
      +--> ORGANIZATIONAL UNIT
      +--> RELATED BUT DISTINCT
      +--> POSSIBLE MERGE
      +--> POSSIBLE SPLIT
      +--> NEW CANDIDATE
      +--> UNRESOLVED
```

The core invariant is:

> Source observations are immutable; canonical interpretation is revisable.

Merges, splits, re-parenting, renaming and reclassification MUST retain reconciliation history and must be reversible.

Identity should be based on multi-signal evidence rather than string similarity alone. Signals can include legal name, aliases, email/website domain, addresses, registration/tax identifiers, contract party names, source-system IDs, known people, customer context, opportunity/RFP identifiers, related documents, temporal overlap and relationship neighborhood.

---

## 8. Context model

Meaning depends on business context. The system SHALL not assume that an email thread, document folder, subject line or source-system record is itself the canonical business context.

Example: an email subject `ServiceNow` could mean a technology/product, an SFO ServiceNow opportunity, an active project, a partner capability conversation, a support issue, or an internal practice discussion.

Context resolution should attempt to identify the governing Opportunity, Solicitation, Agreement, Project, Work Order, Customer relationship, Vendor relationship, Employee matter, Compliance matter, Invoice/payment matter, or other business context.

A processing time window may define where discovery starts, but contextual expansion may retrieve older messages, attachments, SharePoint material or other source records when required.

---

## 9. Temporal semantics

The World Model is temporally native. Where material, it must distinguish:

- **effective_time** — when something was actually true or occurred in the business;
- **source_time** — when the source artifact was created/sent/received;
- **recorded_time** — when a source system formally recorded it;
- **discovered_time** — when the World Model Platform learned it;
- **superseded_time** — when an accepted fact/state ceased to be operationally current.

The model SHALL distinguish current operational truth, historical truth and hypothetical/scenario truth. A single `updated_at` is not sufficient.

### Historical reconstruction strategy

```text
PRESENT / LATEST OBSERVED REALITY
          |
          v
MOVE BACKWARD THROUGH HISTORY
          |
          v
RECONSTRUCT PRIOR STATES, EVENTS, DECISIONS
          |
          v
OPTIONALLY REPLAY FORWARD
          |
          v
COMPARE RECONSTRUCTED PRESENT TO OBSERVED PRESENT
```

Current records provide an identity/context anchor, but current classifications MUST NOT be projected backward without historical evidence.

---

## 10. State model

State is the set of accepted, time-qualified propositions describing an object or relationship. State SHOULD be derived from events/actions where possible rather than treated only as mutable fields.

Example opportunity lifecycle:

```text
discovered -> qualified -> bid_approved -> proposal_in_progress
-> submitted -> interview -> awarded | lost | cancelled
```

The platform must support explicit state transitions, transition provenance, causative event, actor/action, effective time, and correction without deleting history.

---

## 11. Decision traces inside the World Model

A Decision Trace is primarily a connected traversal through first-class ontology resources, not an opaque narrative blob.

```text
Signal -> Evidence -> Assessment -> Alternative(s) -> Recommendation
-> Decision -> Approval / Delegation -> Action -> State Change
-> Outcome -> Learning
```

Historical reconstruction may produce partial traces. The World Model MUST distinguish explicit versus inferred decision, explicit versus inferred rationale, known versus suspected alternatives, and exact versus approximate decision time.

---

## 12. Kinetic semantics

The World Model SHALL expose business actions as typed, governed operations.

Examples:

```text
SubmitProposal(opportunity_id, proposal_id, actor_id, submission_time)
ApprovePartner(opportunity_id, partner_relationship_id, approver_id)
RequestPricing(opportunity_id, partner_id, due_date)
```

An action definition may include allowed actor classes, input types, preconditions, policies, constraints, required approvals, allowed state transitions, effects on multiple objects/links, external write-back, audit requirements and compensating/recovery action.

The ontology should be capable of becoming kinetic even if the first MVP initially supports read/reason/propose rather than autonomous execution.

---

## 13. Security model requirements

Security is part of the semantic model. The platform must support, conceptually, object-level, relationship-level where needed, property-level and evidence-level security, action permissions, delegated authority, business-function access, need-to-know restrictions, and source permissions/legal constraints.

Security-sensitive domains include HR, legal, finance, cybersecurity and executive strategy.

The platform must permit a canonical fact to be visible while its sensitive evidence remains restricted.

---

## 14. Internal versus external authority

Authority is property-specific and time-specific. There is no universal source hierarchy.

Examples:

```text
Payment status -> finance system / bank evidence
Executed legal terms -> signed agreement
Email sent/received metadata -> Microsoft 365
Employee payroll status -> payroll/HR authority
Procurement deadline -> procurement portal / issued addendum
```

An email may be highly authoritative for what a person communicated but weak evidence for whether a payment actually cleared.

---

## 15. Scenarios and hypothetical worlds

Hypothetical state must remain isolated from current operational truth. Scenario objects/views may reuse canonical identities and business logic but MUST NOT silently mutate current state.

---

## 16. Interfaces and polymorphism

The ontology SHOULD favor interfaces/composition over deep class inheritance. Candidate interfaces include `TemporalObject`, `EvidenceBacked`, `SecuredResource`, `Actionable`, `Locatable`, `Party`, `FinanciallyRelevant`, `DecisionContext`, and `VersionedArtifact`.

---

## 17. Query requirements that drive physical architecture

Database selection is explicitly deferred until the logical model is pressure-tested against real query patterns.

The V1 platform must support:

- canonical ID lookup and alias resolution;
- current and historical state retrieval with provenance;
- one-hop and multi-hop relationship traversal;
- Customer -> Opportunity -> Partner -> Person -> Agreement traversals;
- supporting and contradicting evidence retrieval;
- distinction between independent and copied evidence;
- object/event timelines;
- decision-trace retrieval;
- exact, lexical/fuzzy, alias and semantic search;
- effective permission enforcement on every query.

---

## 18. V1 MVP scope

### Sensors

- Outlook / Exchange Online;
- SharePoint Online.

### Domain

Commercial / opportunity world, with enough adjacent relationship and document structure to understand real conversations.

### Core objects

- Organization;
- Person;
- Business Relationship;
- Opportunity;
- Solicitation;
- Agreement;
- Project;
- Document/Artifact;
- Event;
- Claim/Evidence;
- Assessment;
- Decision;
- Action;
- Outcome.

### Initial use cases

1. Reconstruct current business relationships from recent email.
2. Resolve opportunity shorthand and aliases.
3. Connect threads and attachments to canonical opportunities/customers/partners.
4. Reconstruct event timelines.
5. Recover decision fragments and assemble candidate decision traces.
6. Preserve provenance, confidence, time and security.
7. Support human review before canonical promotion.

---

## 19. Reference pilot cases

Initial pressure tests include SFO ServiceNow / CRI Advantage; Stridepath / CCSF HRSD; Veraqor / UCSD; Fivetran partner agreement; active SFO/SFPUC/SFDEM/DHR delivery and invoice evidence; Nevada compliance renewal; NMSDC; Zoho/Bitdefender; and HR-restricted workforce signals.

No case should distort the enterprise ontology into a one-off application schema.

---

## 20. Acceptance criteria

The design is acceptable when we can answer:

1. Can one real-world organization appear under many names without duplicate canonical identity?
2. Can similar names remain distinct when evidence says they are different?
3. Can an email remain evidence without becoming truth?
4. Can an email attachment and SharePoint file resolve to one document/version lineage?
5. Can we reconstruct current and historical state?
6. Can we reconstruct an opportunity timeline?
7. Can we distinguish Decision, Event and Action?
8. Can inferred decisions remain visibly inferred?
9. Can objects participate in governed typed actions?
10. Can sensitive evidence remain restricted while less-sensitive state is available?
11. Can external events connect to internal strategy without creating an undisciplined news graph?
12. Can storage technology change without changing the semantic contract?

---

## 21. Non-goals for V1

V1 does not model every domain, ingest every source, autonomously execute high-risk actions, finalize storage before benchmarks, create hundreds of object types, make AI inference authoritative, replace source systems of record, or build a universal knowledge graph.

---

## 22. Doctrine references

- Palantir Ontology overview: https://www.palantir.com/docs/foundry/ontology/overview/
- Palantir core concepts: https://www.palantir.com/docs/foundry/ontology/core-concepts
- Object types: https://www.palantir.com/docs/foundry/object-link-types/object-types-overview
- Link types: https://www.palantir.com/docs/foundry/object-link-types/link-types-overview
- Function-backed actions: https://www.palantir.com/docs/foundry/action-types/function-actions-overview

---

## 23. Status

This is a logical specification, not a database schema. Physical persistence technology SHALL be selected only after the related specifications produce explicit query patterns, correctness requirements, security requirements, write semantics and realistic GenSigma benchmark data.
