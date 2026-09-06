# ADR-001 — Hierarchical Durable Agent Coordination

**Status:** Proposed / Chief Architect recommendation  
**Date:** 2026-09-05  
**Decision owner:** Chief Architect

---

## Context

GenSigma OS initially represented specialist leads as separate ChatGPT threads. This was useful for role separation but cannot provide reliable autonomous coordination because chat threads are not durable background workers and do not automatically wake when another thread publishes a dependency or architecture decision request.

GenSigma needs specialist agents that can work independently, coordinate with peers, automatically escalate cross-cutting decisions, survive long waits/failures, and preserve auditable outputs.

---

## Decision

Adopt a **hierarchical, event-driven, durable multi-agent architecture with bounded peer collaboration**.

- Chief Architect is a durable, addressable governance agent.
- Specialist leads are durable role agents.
- Agents coordinate through structured Task/Event/DecisionRequest/ArtifactRef contracts.
- Cross-workstream architectural decisions route to Chief Architect automatically.
- Peer consultation/delegation is allowed within scoped authority.
- GitHub remains durable engineering truth but is not used as the primary task/message bus.
- Large work products are stored as artifacts and passed by reference.
- Deterministic workflows enforce authority, task state, retries, approvals, and escalation; LLMs reason within those boundaries.
- MCP is used conceptually for agent-to-tool/data interaction; A2A-compatible patterns are preferred for agent-to-agent boundaries.

---

## Alternatives considered

### A. Continue with independent chat threads

Rejected for production coordination. No reliable wake-up, task durability, event subscriptions, or automatic dependency resumption.

### B. Pure peer-to-peer agent swarm / group chat

Rejected as governing topology. Flexible, but weak on authority, loop prevention, conflict resolution, security, and architectural accountability.

### C. Single monolithic super-agent

Rejected. Creates context overload, weak separation of concerns, poor parallelism, and a large failure/blast radius.

### D. Fully hard-coded workflow with no agent-to-agent reasoning

Rejected as the only model. Too rigid for open-ended research, architecture, ontology, and problem solving.

### E. Hierarchical durable coordination with bounded peer collaboration

Selected. Preserves governance and reliability while allowing specialist autonomy and parallel reasoning.

---

## Consequences

### Positive

- Chief Architect can be automatically invoked on relevant events.
- Specialists can collaborate without Vijay manually copying context between chats.
- Architecture decisions remain attributable and durable.
- Agent state can survive process/model/session restarts.
- Security and authority can be enforced centrally.
- Work can run asynchronously and resume from dependencies.
- The model/provider/runtime can evolve independently of organizational agent identity.

### Negative

- Requires a real control plane, durable task runtime, event routing, and observability.
- More engineering complexity than chat-based agents.
- Multi-agent systems can increase model/tool cost and introduce coordination failure modes.
- Requires careful context engineering and evaluation.

---

## Implementation guidance

The runtime/framework is deliberately not fixed by this ADR.

Current leading candidate: Microsoft Agent Framework + Durable Extension because the GenSigma environment is Azure-oriented and the framework supports durable state, event-driven orchestration, checkpoint/resume, human-in-the-loop, and multi-agent workflow patterns.

OpenAI Agents SDK remains a strong candidate for lightweight agent definitions, handoffs/managers, guardrails, sessions, and tracing, potentially inside the durable shell.

The platform lead must validate the runtime through a small prototype before a framework selection ADR is approved.

---

## Validation condition

The architecture must demonstrate this end-to-end scenario:

```text
Knowledge/Ontology Agent
 -> DecisionRequest
 -> durable event/router
 -> Chief Architect wakes automatically
 -> reads governing artifacts
 -> decides or escalates to Vijay
 -> writes ADR/decision
 -> emits decision_made
 -> Knowledge/Ontology task resumes
```

The design is not considered validated until this works after a forced process restart without manual context copying.

---

## Revisit triggers

Revisit this ADR if:

- agent coordination can be made materially simpler without losing durability/governance;
- A2A or another standard matures into a better internal control-plane abstraction;
- selected runtime prevents required security or workflow semantics;
- coordination overhead exceeds value for the number of active agents;
- evidence shows a decentralized topology performs materially better without compromising governance.
