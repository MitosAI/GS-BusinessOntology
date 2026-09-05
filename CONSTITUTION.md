# GenSigma AI-Native Operating System — Ontology Constitution

**Status:** Draft v0.2  
**Governing doctrine:** Palantir-style operational ontology  
**Purpose:** Define the durable architectural principles that govern how GenSigma represents, reasons about, acts upon, secures, and learns from its business.

---

## How to read this Constitution

This document is the governing architectural contract for the GenSigma AI-Native Operating System. It is intentionally more durable than any individual database, cloud service, LLM, connector, application, or implementation framework.

It is not the detailed ontology schema and it is not a coding specification. Instead, it defines the principles that future schemas, services, APIs, agents, actions, and storage choices must obey.

For implementation purposes, the words **MUST**, **SHOULD**, and **MAY** have their normal architectural meaning:

- **MUST** — required for constitutional compliance.
- **SHOULD** — preferred unless a documented reason justifies an exception.
- **MAY** — optional and dependent on the use case.

If an implementation conflicts with this Constitution, the implementation does not silently win. The conflict must be documented and the Constitution explicitly amended if the architecture itself is changing.

---

# 1. Purpose — Build an AI-native operating system, not AI bolted onto software

GenSigma is building an AI-native operating layer for the company. The objective is not to place a chatbot or isolated AI automation on top of existing systems. The objective is to make the business itself understandable and operable through a governed operational model that humans and AI can use together.

The system should make the company legible in terms of:

- what exists;
- how things are related;
- what state the company is in now;
- what was true historically;
- what happened and in what order;
- what is known, claimed, inferred, or uncertain;
- what decisions are available and why;
- who may decide or approve;
- what actions may be taken;
- what state changes and outcomes resulted;
- what the organization should learn from those outcomes.

The long-term ambition is that AI participates **inside the operating model of GenSigma**, rather than repeatedly reconstructing the company from prompts, documents, and disconnected application data.

The governing operational loop is:

`World State → Evidence → Reasoning → Decision → Governed Action → New World State → Outcome → Learning`

### Engineering implication

Code should be designed around preserving and operating this loop. A feature that stores information but cannot preserve provenance, state, authority, or action semantics should not be treated as complete simply because it works technically.

---

# 2. Primary doctrine — The Palantir-style operational ontology is the architectural spine

The primary architectural doctrine is the Palantir-style concept of an **operational ontology**: one coherent operating layer connecting business objects, relationships, logic, decisions, actions, security, and resulting state changes.

This is stronger than building any one of the following in isolation:

- a data catalog;
- a knowledge graph;
- a semantic search system;
- a master-data repository;
- a workflow engine;
- an analytics model;
- an agent framework;
- a collection of APIs.

Those capabilities may support the system, but none of them defines it.

The ontology combines five inseparable dimensions:

## 2.1 World
What exists in the business and how it is related.

Examples: Organization, Person, Opportunity, Solicitation, Agreement, Project, Invoice, Relationship, Document, Capability, Location, State.

## 2.2 Temporal / Event
What happened, when it happened, and how business state changed over time.

Examples: RFP released, NDA executed, proposal submitted, contract awarded, employee joined, invoice issued, payment received.

## 2.3 Decision
How the business reasons and chooses.

Examples: evidence considered, assessment performed, alternatives considered, recommendation made, approval obtained, decision made, assumptions or constraints applied.

## 2.4 Kinetic
How the ontology causes governed action in the real business.

Examples: request pricing, approve partner, create proposal workspace, initiate workflow, send communication, update external system, submit proposal, create task, execute automation.

## 2.5 Outcome / Learning
What resulted from the decision and action, and what should influence future decisions.

Examples: win/loss, revenue, margin, customer acceptance, delivery quality, payment delay, partner performance, strategic learning.

These are not separate architectures. They are different dimensions of the same operational ontology.

### Engineering implication

Builders MUST avoid creating parallel systems of meaning where, for example, the graph means one thing, the workflow engine another, and the agent layer another. Supporting technologies may differ physically, but their semantics must resolve back to one coherent ontology.

---

# 3. The ontology is operational — it represents the business and participates in running it

The ontology is not merely descriptive.

It is **not**:

- a glossary;
- a document index;
- a source-system schema;
- a reporting model;
- a static knowledge graph;
- a vector store;
- a search index;
- a collection of LLM summaries.

Those systems may support the ontology. They are not the ontology itself.

The ontology must represent business concepts in business terms. An Opportunity should be represented as an Opportunity, not merely as rows copied from CRM, an email subject line, or a SharePoint folder.

The ontology must also represent meaningful business verbs.

> **Nouns need verbs.**

If `Opportunity` exists, the system should eventually be able to expose governed actions such as:

- qualify opportunity;
- approve bid decision;
- add teaming partner;
- request pricing;
- submit proposal;
- record award;
- convert to project.

### Engineering implication

Applications and agents SHOULD interact with the business through ontology-aware services and typed actions. Direct database mutation should not become the primary business interface.

---

# 4. Sources are sensors, not truth

Email, SharePoint, finance systems, HR systems, CRM systems, procurement portals, public registries, spreadsheets, files, and other applications are **sensors and evidence providers**.

A source record proves that a source recorded something. It does not automatically prove that the recorded statement is canonical business truth.

Examples:

- an email may say a partner is expected to participate;
- a signed agreement may establish the legally executed relationship;
- a CRM may show an opportunity as active while the procurement portal shows it was cancelled;
- an invoice proves issuance of an invoice, not receipt of payment.

The system MUST distinguish:

1. what the source recorded;
2. what the discovery system extracted or inferred;
3. what has been accepted as canonical ontology state.

The governing promotion path is:

`Source → Raw Evidence → Observation / Claim / Candidate → Reconciliation → Ontology Proposal → Validation / Governance → Canonical Operational Ontology`

### Engineering implication

Connectors MUST NOT write source records directly into canonical ontology tables or objects merely because a mapping exists. Ingestion and canonicalization are separate operations.

---

# 5. Enterprise Evidence Graph — uncertainty must have a safe home

Before information becomes canonical, the system needs a place where uncertainty, duplication, contradiction, and incomplete understanding can safely exist.

That place is the **Enterprise Evidence Graph**.

The Evidence Graph is intentionally non-authoritative and may contain:

- multiple possible identities for one real-world thing;
- aliases and shorthand;
- contradictory claims;
- duplicate source references;
- candidate relationships;
- candidate events;
- candidate contexts;
- decision fragments;
- AI-generated interpretations;
- confidence values;
- provenance;
- unresolved ambiguity.

Its purpose is to preserve evidence and reasoning without forcing premature certainty.

The central distinction is:

`Evidence Graph = what we observed, extracted, or inferred`

`Canonical Ontology = what the operating system is prepared to rely upon`

### Engineering implication

The Evidence Graph MUST preserve links back to source evidence. AI-generated interpretation MUST be identifiable as interpretation. The system SHOULD prefer unresolved ambiguity over an incorrect canonical merge.

---

# 6. Canonical identity and continuous reconciliation

Identity resolution is a foundational correctness problem.

The same real-world thing may appear differently across years, systems, people, and documents. Examples include:

- `SFO`;
- `SF Airport`;
- `San Francisco International Airport`;
- `ServiceNow` as shorthand for a specific opportunity;
- an employee who changes organizations;
- an organization that renames, merges, spins off, or uses a brand name different from its legal name.

A newly observed name or reference MUST NOT automatically create a new canonical object.

Every candidate should first be compared with what the ontology and Evidence Graph already know.

Reconciliation may determine that an observation represents:

- the same canonical object;
- an alias;
- a historical name;
- a parent / child relationship;
- an organizational unit;
- a related but distinct object;
- a potential merge;
- a potential split;
- a genuinely new object;
- an unresolved case requiring more evidence.

Reconciliation is continuous. New evidence may refine an earlier interpretation.

> **Source observations are immutable; canonical interpretation is revisable.**

Merge, split, rename, re-parent, and reclassification operations MUST preserve provenance, history, and reversibility.

### Engineering implication

Builders MUST avoid destructive deduplication. Canonicalization should preserve source identity mappings and reconciliation history so a later correction can be performed without losing evidence.

---

# 7. Canonical identity is distinct from contextual role

Enduring identity and contextual role are different concepts.

There should generally be one canonical `Person` for a human being. That Person may be, at different times or simultaneously:

- Employee;
- Candidate;
- Contractor;
- Owner;
- Advisor;
- Customer Stakeholder;
- Project Resource.

Likewise, there should generally be one canonical `Organization`. That Organization may be:

- Customer;
- Partner;
- Vendor;
- Competitor;
- Technology Provider;
- Certification Body;
- Regulator;
- Member Organization.

These are contextual relationships or roles, not duplicate identities.

Relationships themselves may be scoped by time, opportunity, agreement, project, or other business context.

### Engineering implication

Schemas SHOULD prefer composition, interfaces, and relationship objects over creating a separate identity type for every business role.

---

# 8. Context before interpretation

Business meaning cannot reliably be extracted from records in isolation.

An email thread is a communication structure. It is not automatically the business context.

A thread titled `ServiceNow` may refer to:

- an SFO pursuit;
- an active implementation project;
- an internal capability discussion;
- a partner conversation;
- a technical support matter.

Discovery must therefore attempt to resolve the larger business context before promoting extracted meaning.

Potential context objects include:

- Customer;
- Opportunity;
- Solicitation / RFP;
- Agreement;
- Project;
- Work Order;
- Invoice;
- workforce matter;
- corporate compliance matter;
- another governed business object.

Context resolution may require expanding beyond the initial source record into earlier email, attachments, other threads, SharePoint, proposals, contracts, procurement records, or other systems.

Human shorthand should be retained as observed language or aliases while being reconciled to canonical objects.

### Engineering implication

Extraction pipelines SHOULD support context expansion. A fixed email-processing window may determine where discovery starts, but it MUST NOT prevent retrieval of earlier supporting context when needed for correct interpretation.

---

# 9. Time is first-class

The business evolves continuously. The ontology must be temporally native rather than representing only the latest value of a field.

Where material, the system must distinguish:

- **Business / effective time** — when something was actually true in the business;
- **Source-created time** — when an email, file, or record was created;
- **Recorded time** — when a system formally recorded it;
- **Discovery time** — when the ontology platform learned about it.

These may differ.

A decision could be made verbally on Monday, mentioned in email Tuesday, reflected in a spreadsheet Wednesday, uploaded to SharePoint Friday, and discovered by the platform months later.

Current email and current systems are useful because they provide the best available anchor for the **latest observed reality**. They are not automatically authoritative for every property.

Historical discovery will generally proceed from present to past because current identities help resolve older shorthand. The system must not project current state backward onto history.

The ontology MUST distinguish:

- current operational truth;
- historical truth;
- hypothetical / scenario truth.

### Engineering implication

Important state-changing objects and relationships SHOULD support effective periods or equivalent temporal semantics. Builders MUST NOT assume `updated_at` is sufficient to represent business history.

---

# 10. Events, decisions, actions, and outcomes are different things

The ontology must not collapse all business activity into a generic activity log.

## Event
An Event answers: **What happened?**

Examples: RFP released, NDA signed, interview scheduled, proposal submitted, invoice issued.

## Decision
A Decision answers: **What choice was made?**

Examples: bid or no-bid, choose Partner A instead of Partner B, approve pricing approach.

## Action
An Action answers: **What was done because of the decision, policy, or trigger?**

Examples: send NDA, request pricing, create proposal workspace, submit response.

## Outcome
An Outcome answers: **What resulted?**

Examples: award won, payment received, customer accepted deliverable, partner underperformed.

The core decision loop may include:

`Signal → Evidence → Assessment → Alternative → Recommendation → Decision → Approval → Action → State Change → Outcome → Learning`

A **Decision Trace** is primarily the connected traversal through these ontology resources. It is not automatically a separate giant object or another architecture.

Historical traces may be incomplete or reconstructed from multiple sources. The system MUST distinguish explicit recorded evidence from inferred reconstruction.

### Engineering implication

Builders MUST preserve the semantic distinction among Event, Recommendation, Decision, Approval, Action, and Outcome. A single `activity_type` field is unlikely to be sufficient for the core operational model.

---

# 11. The ontology is kinetic — governed actions change the real business

A central property of the architecture is that the ontology can be acted through.

It should not merely tell an agent:

`Opportunity.status = proposal`

It should support a governed business operation such as:

`SubmitProposal(opportunity, proposal, actor, submission_time)`

A typed action can enforce:

- actor authorization;
- required approvals;
- preconditions;
- policy checks;
- required evidence or documents;
- allowed state transitions;
- audit logging;
- notifications;
- downstream side effects;
- write-back to external systems.

Typed actions may be initiated by humans, applications, or AI agents, subject to the same governance model.

### Engineering implication

Material business state changes SHOULD occur through typed actions. Arbitrary CRUD endpoints that bypass policy, validation, authority, and audit controls SHOULD be treated as infrastructure mechanisms, not the business action surface.

---

# 12. Security is part of the ontology, not a wrapper around it

Security must be designed into the operational model itself.

Objects, relationships, properties, evidence, decisions, and actions may carry different sensitivity and authorization requirements.

The model should support, where appropriate:

- role;
- business function;
- delegated authority;
- need-to-know;
- evidence sensitivity;
- object-level restrictions;
- property-level restrictions;
- action permissions;
- restricted domains such as HR, legal, finance, and security.

A business fact may be broadly visible while the evidence supporting it is restricted.

For example, the company may be permitted to know that a Person is unavailable while the medical explanation contained in an email remains HR Restricted.

### Engineering implication

Authorization cannot be postponed until the UI layer. Services, APIs, actions, search, agent retrieval, and evidence access MUST all respect the same security semantics.

---

# 13. AI agents are governed actors

AI agents are participants in the operating system, not omnipotent administrators.

An agent must have explicit authority defining:

- what it may read;
- what it may infer;
- what it may recommend;
- what actions it may invoke;
- what requires human approval;
- what it may never do.

AI-generated claims, entity matches, recommendations, and ontology changes are non-authoritative by default unless promoted through an approved mechanism.

The system should preserve which model or agent generated a material inference or recommendation when that provenance matters.

### Engineering implication

Agents SHOULD authenticate as governed actors with scoped permissions. Agent code MUST NOT rely on unrestricted service credentials merely for convenience.

---

# 14. Ontology layers separate stable meaning from source and application concerns

The ontology should evolve in layers:

- **L0 — Metamodel:** the language of objects, properties, links, interfaces, actions, policies, and related ontology constructs.
- **L1 — Promoted Enterprise Core:** a deliberately small set of highly stable concepts shared across GenSigma.
- **L2 — Shared Enterprise Domains:** reusable business concepts such as commercial, workforce, finance, delivery, and compliance structures.
- **L3 — GenSigma Extensions:** concepts specific to GenSigma's actual operating model.
- **L4 — Application / Agent Views:** task-specific projections or interfaces built for users, agents, and workflows.
- **L5 — Source Bindings:** mappings from Outlook, SharePoint, QuickBooks, CRM, procurement portals, and other source systems.

This structure prevents source schemas or application convenience from contaminating the canonical ontology.

### Engineering implication

A source-specific field SHOULD generally be bound at L5 and mapped upward rather than copied directly into L1. Application-specific views SHOULD generally live at L4 rather than changing core ontology semantics.

---

# 15. New ontology concepts require admission discipline

The ontology should not grow merely because a new noun appears in a source document.

A candidate canonical object type should normally demonstrate several of the following:

- independent identity;
- independent lifecycle;
- meaningful independent relationships;
- independent security requirements;
- independent business actions;
- independent ownership;
- independent query value.

If those conditions are weak, the concept may instead belong as a:

- property;
- relationship;
- relationship role;
- event;
- claim;
- evidence item;
- category;
- interface;
- derived value;
- application view.

MECE applies where it improves canonical identity, definition, domain ownership, source authority, and state dimensions. It does not require eliminating legitimate overlap in roles, relationships, capabilities, or interfaces.

### Engineering implication

Schema expansion SHOULD be treated as an architectural decision rather than an automatic result of extraction. Discovery pipelines may create candidate concepts freely in the Evidence Graph; promotion to canonical type requires review.

---

# 16. Ontology changes are governed like software changes

The ontology is executable business infrastructure. Changes can affect agents, actions, permissions, workflows, reporting, and historical interpretation.

Material ontology changes must therefore be treated with software-engineering discipline.

Changes SHOULD move through mechanisms such as:

- branch or proposal;
- review;
- automated validation;
- compatibility checks;
- approval;
- promotion / release;
- rollback or amendment where required.

Discovery divergence should produce a proposal or review condition rather than silently changing canonical truth.

### Engineering implication

Ontology definitions SHOULD be source controlled. Material schema, action, security, or semantic changes SHOULD be traceable to a reviewed change record or ADR.

---

# 17. Correctness is tested against real GenSigma business situations

The ontology should not be judged primarily by elegance in diagrams. It must accurately represent and operate real GenSigma business situations.

Design proceeds through vertical slices:

`Real Source Data → World → Event / State → Decision → Kinetic Action → Outcome / Learning`

Representative cases should intentionally pressure-test:

- identity ambiguity;
- duplicate records;
- aliases;
- conflicting evidence;
- historical state;
- decision reconstruction;
- restricted information;
- action authorization;
- cross-system context.

Tests may include:

- competency questions — can the ontology answer the business question correctly?
- golden actions — can the business operation be executed safely?
- reconciliation tests — can duplicates and aliases be resolved correctly?
- temporal replay — can historical state be reconstructed consistently?
- security tests — does restricted evidence remain inaccessible to unauthorized actors?

### Engineering implication

Builders SHOULD develop ontology tests alongside schema and action implementations. Correctness is not limited to unit tests on code; semantic and business invariants must also be tested.

---

# 18. The first deep operational chain is RFP-to-Cash

The first major vertical slice is the GenSigma **RFP-to-Cash** lifecycle because it connects strategy, customers, opportunities, partners, proposals, agreements, delivery, finance, decisions, and outcomes.

A representative trace may include:

`Strategic Fit → Opportunity → Solicitation → Bid Decision → Partnering → Proposal → Award → Agreement → Project → Deliverable → Acceptance → Invoice → Payment → Outcome → Learning`

Email and SharePoint are especially valuable initial discovery sources because they contain the context, relationships, documents, decisions, and actions that may not exist in structured systems.

This vertical slice is intended to pressure-test the ontology across all five dimensions: World, Temporal/Event, Decision, Kinetic, and Outcome/Learning.

### Engineering implication

Initial implementation work SHOULD favor capabilities necessary to model and exercise real RFP-to-Cash cases rather than trying to model the entire company at once.

---

# 19. Implementation neutrality — technology serves the ontology

This Constitution defines the logical and operational architecture. It does not mandate a particular physical database, cloud provider, graph engine, vector store, search service, or AI model.

Technology selection must follow requirements derived from the ontology, including:

- identity integrity;
- temporal behavior;
- provenance;
- security;
- transactional correctness;
- graph traversal;
- search;
- evidence retrieval;
- typed actions;
- performance;
- auditability;
- reversibility;
- operational resilience.

Azure may be a practical hosting choice because GenSigma already operates heavily within the Microsoft ecosystem, but cloud infrastructure must remain an implementation detail rather than becoming part of ontology semantics.

### Engineering implication

Builders MUST NOT design ontology concepts around the limitations or conveniences of a chosen database product. Physical models may optimize implementation, but they must preserve the logical semantics defined here.

---

# 20. The promoted core must remain small and stable

The enterprise core should contain only concepts that are broadly reusable, semantically stable, and important across multiple domains.

A large core makes change expensive, encourages weak abstractions, and causes downstream applications and agents to become tightly coupled to accidental design decisions.

GenSigma-specific or domain-specific concepts should remain outside the promoted core until repeated evidence demonstrates that they belong there.

### Engineering implication

The default response to a new concept SHOULD be to model it in an extension or proposal first. Promotion to the enterprise core requires stronger evidence than ordinary schema creation.

---

# 21. Historical reconstruction and native future operation use the same ontology

Historical company knowledge will often be reconstructed from fragmented evidence such as email, documents, spreadsheets, and source-system records.

Future company activity should increasingly be recorded natively through the operational ontology.

Therefore the same model must be capable of representing both:

### Reconstructed history
A decision inferred from older email, with incomplete evidence and explicit confidence.

### Native operation
A decision made through the platform, with known actors, alternatives, approval, action, and outcome.

The system MUST preserve the distinction between reconstructed and natively recorded information.

### Engineering implication

Historical ingestion SHOULD NOT require a different ontology from live operations. Provenance and epistemic status should explain how knowledge entered the system.

---

# 22. Evidence lineage must prevent false corroboration

Historical business records frequently repeat the same underlying information.

An original email may be quoted in replies, forwarded multiple times, copied into meeting notes, and attached to another document. These appearances must not automatically be counted as independent evidence.

The system should preserve evidence lineage such that it can distinguish:

`one statement appearing five times`

from

`five independent statements reaching the same conclusion`.

### Engineering implication

Evidence records SHOULD support lineage such as `derived_from`, `quoted_from`, `copied_from`, `version_of`, or equivalent semantics. Confidence calculations MUST NOT treat duplicate appearances as independent corroboration without justification.

---

# 23. Discovery proceeds incrementally and reconciles continuously

The historical corpus is too large and too interconnected to treat as a one-time extraction job.

Discovery should proceed in controlled waves, generally beginning with recent data and moving backward through time.

Each wave should:

`Discover → Classify → Resolve Context → Reconcile → Propose → Validate → Enrich History`

Newly discovered evidence may add aliases, reveal an earlier relationship, change the understood start date of an event, surface a previously unknown alternative in a decision, or expose an incorrect merge.

The architecture must allow the ontology to become more accurate as evidence accumulates without losing prior source observations.

### Engineering implication

Ingestion jobs SHOULD be idempotent and re-runnable. Reprocessing older evidence MUST NOT create uncontrolled duplication. Reconciliation state and source provenance must support incremental enrichment.

---

# 24. Architectural decisions must remain inspectable and durable

The AI-native operating system will evolve over years. Important design choices cannot live only in chat transcripts or individual memory.

The Constitution records the governing principles. Significant architectural choices beneath it should be captured in Architecture Decision Records (ADRs) or equivalent governed documents.

Examples include:

- physical persistence architecture;
- graph technology selection;
- temporal modeling strategy;
- identity-resolution algorithm;
- security enforcement architecture;
- action execution model;
- event infrastructure.

### Engineering implication

A future builder should be able to understand both **what the architecture is** and **why it became that way** without reconstructing the reasoning from chat history.

---

# 25. Amendment rule — architectural drift must be explicit

This Constitution is a living governed artifact.

It may evolve as real GenSigma evidence, implementation experience, or deeper architectural research reveals a better design. However, changes must be explicit.

An amendment should explain:

- what principle is changing;
- why the current principle is insufficient;
- what evidence or requirement caused the change;
- what downstream implications exist.

Undocumented architectural drift through implementation convenience, agent behavior, or repeated conversational reinterpretation is prohibited.

---

## Constitutional summary

The GenSigma AI-Native Operating System is built around one coherent operational ontology that represents the business, preserves evidence and time, reconstructs decisions, enables governed kinetic actions, secures access at the semantic level, and learns from outcomes.

Sources provide evidence. Discovery proposes meaning. Governance promotes meaning. The ontology provides operational context. Humans and AI reason and act through it. Actions change the real business. Outcomes return as new evidence and learning.

That closed loop is the foundation of the system.
