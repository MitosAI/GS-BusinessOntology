# GenSigma Foundational Architecture Decisions

**Version:** v0.1  
**Status:** Draft ADR register  
**Purpose:** Capture the durable design decisions already made so future implementation does not drift from the architecture conversations and Constitution.

---

## ADR-001 — Build an AI-native operating system, not bolt-on AI

**Decision:** GenSigma will build an operating layer in which AI participates through the same governed enterprise model used by humans and applications.

**Consequence:** Chatbots, isolated copilots and workflow automations may exist, but they are not the architectural center.

---

## ADR-002 — Palantir-style operational ontology is the primary doctrine

**Decision:** Use the Palantir operational-ontology philosophy as the primary governing reference rather than synthesizing many frameworks into a new doctrine.

**Rationale:** The target is an operational representation combining semantic objects/links with logic, actions, security and decisions.

**Consequence:** Other frameworks may be consulted for gaps, but they do not redefine the architectural spine.

---

## ADR-003 — Three peer models feed the Decision Engine

**Decision:** The OS distinguishes:

- Business Intent Model — what do we want?
- World Model — what is true?
- Capability Model — what can we do?

These feed a governed Decision Engine.

**Consequence:** Strategy is not hidden inside prompts; capability is not confused with aspiration; observed reality does not dictate objectives.

---

## ADR-004 — One World Model covers internal and material external reality

**Decision:** Do not create separate internal and external world-model architectures. Maintain one coherent model with domains.

**Initial bias:** approximately 80% internal operating reality / 20% material external reality.

**Consequence:** External signals are modeled only when they can materially affect GenSigma decisions, strategy, risk, relationships or capability.

---

## ADR-005 — Sources are sensors and evidence providers

**Decision:** Outlook, SharePoint, QuickBooks, CRM and other systems do not directly define ontology truth.

**Consequence:** Ingestion and canonicalization are separate operations.

---

## ADR-006 — Maintain a non-authoritative Enterprise Evidence Graph

**Decision:** Uncertainty, contradictions, duplicate candidates, aliases, decision fragments and AI interpretations need a safe pre-canonical layer.

**Consequence:** The Evidence Graph may be messy; the Canonical Ontology must be governed.

---

## ADR-007 — Identity reconciliation is continuous, reversible and provenance-preserving

**Decision:** New observations must be compared with existing identities before creating new canonical objects.

**Rule:** Source observations are immutable; canonical interpretation is revisable.

**Consequence:** Merge/split/rename/re-parent decisions retain history and can be corrected later.

---

## ADR-008 — Canonical identity is separate from contextual role

**Decision:** Maintain one canonical Person and Organization identity where appropriate.

Customer, Partner, Vendor, Employee, Candidate, Contractor and similar labels are generally contextual relationships/roles.

**Consequence:** Avoid duplicate Person/Organization universes by role.

---

## ADR-009 — Context before interpretation

**Decision:** Email threads, subject lines and folders are evidence structures, not automatically business contexts.

**Consequence:** Discovery must resolve the related Opportunity, Project, Agreement, Customer, workforce matter, etc. before high-confidence interpretation.

---

## ADR-010 — Time is first-class

**Decision:** Distinguish business/effective time, source time, recorded time and discovery time where material.

**Historical discovery strategy:** anchor latest observed reality, then move backward, continuously reconciling.

**Consequence:** Current state must not be projected backward without evidence.

---

## ADR-011 — Decision traces are traversals through first-class resources

**Decision:** Preserve Evidence -> Assessment -> Alternative -> Recommendation -> Decision -> Approval -> Action -> State Change -> Outcome -> Learning.

**Consequence:** Do not collapse a decision trace into an LLM-generated summary blob. A separate DecisionCase object may be introduced only if real lifecycle needs justify it.

---

## ADR-012 — Ontology is kinetic: nouns need verbs

**Decision:** Material business change should occur through typed, governed actions.

**Consequence:** `SubmitProposal(...)` is preferred over arbitrary direct mutation of `opportunity.status`.

---

## ADR-013 — Security is part of the ontology

**Decision:** Security cannot be merely a UI or perimeter wrapper.

**Consequence:** Object/property/evidence/action access must be governed end-to-end, including agent retrieval and tool execution.

---

## ADR-014 — AI agents are governed actors

**Decision:** Agents receive explicit read, infer, recommend and action authority.

**Consequence:** AI outputs are non-authoritative by default, and unrestricted service credentials are architecturally unacceptable.

---

## ADR-015 — Use composition and interfaces over deep inheritance

**Decision:** Prefer interfaces, links and relationship roles to large subtype trees.

**Consequence:** The promoted core remains stable and extensible.

---

## ADR-016 — Keep the promoted core small

**Decision:** V1 should target roughly 25-35 total ontology object types across promoted core and initial domain extensions, not hundreds.

**Consequence:** New object types must pass the independent identity/lifecycle/relationship/security/action/query-value admission test.

---

## ADR-017 — RFP-to-cash is the first deep decision/value chain

**Decision:** The first deep domain chain is:

```text
Customer -> Opportunity -> Solicitation -> Proposal -> Agreement
-> Project -> Deliverable -> Invoice -> Payment -> Outcome
```

**Consequence:** Early ontology choices must support this chain and its decision loops.

---

## ADR-018 — Outlook and SharePoint are the first sensors

**Decision:** Begin evidence discovery with email and SharePoint because they contain the richest relationship, opportunity, document and decision context.

**Consequence:** QuickBooks/finance comes later when transactions can be connected to business context.

---

## ADR-019 — Historical processing starts from present and moves backward

**Decision:** Use current/recent email and systems as the identity/context anchor, then progressively process older history.

**Consequence:** Each historical wave may add aliases, states, events and decision evidence and trigger reconciliation.

---

## ADR-020 — Context windows may expand outside batch windows

**Decision:** A processing batch defines where discovery starts, not a hard boundary on supporting evidence.

**Consequence:** Earlier threads/documents may be pulled as supporting context without being counted as activity in the batch period.

---

## ADR-021 — Duplicate evidence must preserve origin lineage

**Decision:** Quotes, forwards, copies and document versions must not automatically count as independent corroboration.

**Consequence:** Evidence should support `derived_from` / `quoted_from` / origin-lineage semantics.

---

## ADR-022 — Authority is property-specific, not globally source-ranked

**Decision:** Define authority contracts per proposition/domain and time period.

**Consequence:** Email may be authoritative for what was communicated but not for payment clearance or legal execution.

---

## ADR-023 — Database selection is deferred

**Decision:** Do not select PostgreSQL, graph databases, vector stores or other persistence technologies as doctrine before logical requirements are stable.

**Consequence:** Physical architecture must be benchmarked against real GenSigma query, traversal, history, reconciliation, security and write workloads.

---

## ADR-024 — Azure is a likely implementation environment, not semantic architecture

**Decision:** Prefer Azure initially because GenSigma already uses Microsoft 365/Entra, but maintain cloud-neutral ontology and service contracts.

**Consequence:** The business model does not know or care which cloud persists it.

---

## ADR-025 — Initial harness approach is framework-based; target may become hybrid

**Decision:** For the broader AI OS, start with a framework-based harness to avoid rebuilding commodity agent plumbing, while retaining GenSigma ownership of ontology, world model, context, governance, decision semantics and kinetic actions.

**Target evolution:** Framework-Based -> Selective Customization -> Hybrid Enterprise Stack.

**Consequence:** No agent framework is allowed to become the system's semantic system of record.

---

## ADR-026 — World Graph and Execution Graph are distinct

**Decision:** The graph of business reality is not the graph/plan of work an agent executes.

**Consequence:** Execution plans may be ephemeral and framework-specific, while World Model semantics remain durable.

---

## ADR-027 — Organizational knowledge and agent memory are distinct

**Decision:** Agent memory/learning cannot silently become organizational truth.

**Consequence:** Reusable learned knowledge must be proposed, validated and promoted into appropriate governed artifacts/ontology/skills.

---

## ADR-028 — One authoritative semantic contract; derived physical projections may vary

**Decision:** Search, graph, vector and application read models may exist physically, but they must resolve back to one coherent semantic contract and governed state.

**Consequence:** Avoid parallel meanings where graph/search/agent representations disagree without reconciliation.

---

## ADR-029 — Scenarios are isolated hypothetical worlds

**Decision:** Hypothetical reasoning may reuse canonical objects and logic but must not mutate current truth.

**Consequence:** Scenario outputs remain explicitly hypothetical until a governed action changes reality.

---

## ADR-030 — Ontology changes are governed like software changes

**Decision:** Significant ontology modifications should be proposed, reviewed, tested, versioned and promoted rather than silently edited in production.

**Consequence:** Use branches/proposals/reviews/releases or equivalent governance even if the physical implementation is not Palantir Foundry.

---

# Decision register status

These ADRs record architecture already substantially decided in design discussions. They remain draft until reviewed against the Constitution and first real vertical slice.

The following decisions are intentionally **not yet made**:

- authoritative database technology;
- graph database selection;
- search/vector engine selection;
- exact Azure service architecture;
- exact agent framework;
- exact confidence thresholds;
- exact identity-resolution algorithm;
- whether BusinessRelationship is one physical object type or an interface/umbrella over specialized relationship records;
- whether DecisionCase/Episode becomes a first-class object;
- final V1 object/link/event/action counts.

These should be resolved through real-data pressure tests and explicit future ADRs.
