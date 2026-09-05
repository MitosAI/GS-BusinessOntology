# GenSigma AI-Native Operating System — Ontology Constitution

**Status:** Draft v0.1  
**Governing doctrine:** Palantir-style operational ontology  
**Purpose:** Define the non-negotiable architectural principles for GenSigma's AI-native operating system.

## 1. Purpose

GenSigma is building an AI-native operating layer in which the ontology is not merely a reporting, search, or knowledge layer. It is the operational representation of the business through which humans and AI understand state, reason, decide, act, and learn.

The ontology must represent:
- what exists;
- how things are related;
- what is true now and what was true historically;
- what happened;
- what is known, claimed, inferred, or uncertain;
- what decisions are available and why;
- who may make or approve those decisions;
- what actions may be taken;
- what state changes and outcomes result;
- what the organization learns from those outcomes.

## 2. Primary doctrine

Palantir's operational-ontology model is the primary architectural doctrine for this system. Other frameworks may be consulted only when a material problem is not adequately addressed by that doctrine. The architecture must not become a synthetic blend of unrelated frameworks by default.

The ontology combines four inseparable dimensions:

1. **World** — objects, properties, links, relationships, state.
2. **Temporal / Event** — events, state transitions, historical state.
3. **Decision** — evidence, assessments, alternatives, recommendations, approvals, decisions.
4. **Kinetic** — governed actions, automations, workflows, write-backs, and resulting state changes.

These feed **Outcome / Learning**.

## 3. The ontology is operational

The ontology is not:
- a glossary;
- a document index;
- a source-system schema;
- a search index;
- a static knowledge graph;
- a collection of LLM summaries.

It is the governed operational model of GenSigma.

Business actions must operate through typed, governed actions rather than arbitrary field mutation. "Nouns need verbs."

## 4. Sources are sensors, not truth

Email, SharePoint, finance systems, HR systems, CRM, procurement portals, public registries, and other applications are **sources of evidence**.

A source record does not directly become canonical ontology truth.

The source pipeline is:

`Source → Raw Evidence → Observations / Claims / Candidates → Reconciliation → Ontology Proposal → Validation / Governance → Canonical Operational Ontology`

## 5. Enterprise Evidence Graph

Discovery output is non-authoritative by default.

The Enterprise Evidence Graph may contain:
- duplicate identities;
- contradictory claims;
- aliases;
- candidate relationships;
- candidate events;
- decision fragments;
- AI-generated inferences;
- confidence values;
- provenance;
- unresolved ambiguity.

The Evidence Graph is allowed to be messy. The Canonical Operational Ontology is not.

No discovery process may silently mutate canonical ontology state.

## 6. Canonical identity and reconciliation

Canonical identity must be continuously reconciled as new evidence is discovered.

A newly observed name or reference must first be compared with known identities before a new canonical object is created.

Reconciliation may conclude:
- same object;
- alias;
- parent / child or organizational-unit relationship;
- related but distinct;
- merge candidate;
- split candidate;
- new candidate;
- unresolved.

Source observations are immutable. Canonical interpretation is revisable.

Merge, split, rename, re-parent, and reclassification decisions must preserve provenance and history and be reversible.

## 7. Canonical identities vs contextual roles

The ontology should avoid duplicate identities for contextual roles.

Examples:
- one canonical `Person`; employee, candidate, contractor, owner, advisor, stakeholder, and project resource are contextual relationships or roles;
- one canonical `Organization`; customer, partner, vendor, competitor, regulator, and similar labels are contextual relationships rather than separate organization identities.

Composition and interfaces are preferred over deep inheritance.

## 8. Context before interpretation

An email thread is evidence, not necessarily the business context.

Business meaning should be resolved against canonical contexts such as:
- Customer;
- Opportunity;
- Solicitation / RFP;
- Agreement;
- Project;
- Work Order;
- Invoice;
- Employment or workforce context;
- other governed business objects.

Human shorthand and aliases must be reconciled to canonical objects without replacing canonical naming.

## 9. Time is first-class

The ontology must distinguish, where relevant:
- business / effective time;
- source-created time;
- recorded time;
- discovery time.

Current email and current systems provide the latest observed reality and are useful as the present-day identity and context anchor. They are not automatically authoritative for every fact.

Historical reconstruction proceeds from present to past, while preserving historical state and avoiding projection of current state backward.

Historical, operational-current, and hypothetical / scenario truth must remain distinct.

## 10. Events, decisions, and outcomes are distinct

An **event** records what happened.

A **decision** records a choice among possibilities.

A decision loop may include:

`Signal → Evidence → Assessment → Alternative → Recommendation → Decision → Approval → Action → State Change → Outcome → Learning`

A "decision trace" is primarily the connected traversal through these governed ontology resources, not a separate competing architecture.

Historical decision traces may be reconstructed from fragmented evidence. Reconstructed traces must remain distinguishable from natively recorded decisions.

Explicit evidence and inferred conclusions must never be silently conflated.

## 11. Kinetic ontology

The system must be capable not only of representing the business but of acting on it.

Typed actions may:
- request or approve work;
- create or update business objects;
- trigger workflows;
- notify participants;
- write back to source systems;
- execute approved automations;
- change governed business state.

Actions must respect permissions, policies, required approvals, constraints, and audit requirements.

Material business writes should occur through typed actions rather than arbitrary CRUD operations.

## 12. Security is part of the ontology

Security is not an external wrapper.

Objects, relationships, evidence, actions, and sensitive properties must support governed access and action control.

The model should support, as needed:
- role;
- business function;
- delegated authority;
- need-to-know;
- evidence sensitivity;
- object and property-level restrictions;
- action permissions.

Sensitive evidence may be more restricted than the business fact it supports.

## 13. AI agents are governed actors

AI agents are not omnipotent system users.

Agents must operate with explicit delegated authority and within the same policy, security, approval, and action framework as other actors.

AI-generated claims, recommendations, and proposed changes are non-authoritative by default unless promoted through a governed mechanism.

## 14. Ontology layers

The ontology should evolve in layers:

- **L0 — Metamodel**
- **L1 — Promoted enterprise core**
- **L2 — Shared enterprise domains**
- **L3 — GenSigma-specific extensions**
- **L4 — Application / agent views**
- **L5 — Source bindings**

The promoted core must remain deliberately small and stable.

## 15. Ontology admission discipline

A new canonical object type should normally require evidence of several of the following:
- independent identity;
- independent lifecycle;
- important independent relationships;
- independent security requirements;
- independent business actions;
- independent ownership;
- independent query value.

Otherwise the concept may be better represented as a property, relationship, relationship role, event, claim, evidence item, category, interface, derived value, or application view.

MECE applies where useful to canonical identity, definition, domain ownership, source authority, and state dimensions. It does not require eliminating legitimate overlap in roles, relationships, capabilities, or interfaces.

## 16. Ontology changes are governed like software changes

Material ontology changes should be proposed, reviewed, tested, and promoted through governed change mechanisms such as branches, proposals, reviews, releases, and explicit exceptions.

Discovery divergence should generate a proposal or review condition rather than silently rewriting canonical truth.

## 17. Correctness and testing

The ontology must be tested against real GenSigma business situations.

Design proceeds from real evidence through vertical slices:

`Real Source Data → World → Event / State → Decision → Kinetic Action → Outcome / Learning`

Where real business evidence does not fit cleanly, the model is pressure-tested and refined.

Competency questions, golden actions, reconciliation tests, and historical replay should be used to validate correctness.

## 18. Initial design focus

The first deep operational chain is **RFP-to-Cash**, connected upward to strategy and downward to delivery and finance.

Email and SharePoint discovery will be used to reconstruct and pressure-test real business objects, relationships, events, decisions, actions, and outcomes.

## 19. Implementation neutrality

This Constitution defines the logical and operational architecture, not a specific database or cloud implementation.

Database, graph, search, vector, storage, and cloud technology choices must be subordinate to the ontology's required semantics, security, temporal behavior, kinetic actions, query patterns, and performance requirements.

## 20. Amendment rule

This Constitution is a living governed artifact.

Changes should be explicit amendments with rationale. Architectural drift through undocumented conversation or implementation convenience is prohibited.
