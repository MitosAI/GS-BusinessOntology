# GenSigma Agent Coordination Protocol

**Version:** v0.1  
**Status:** Draft protocol  
**Owner:** Chief Architect

---

# 1. Purpose

Define the minimum structured contract by which GenSigma OS agents assign work, consult peers, escalate decisions, publish events, exchange artifacts, and resume dependent work.

This protocol is semantic. It can initially be implemented with internal APIs/queues and later exposed through A2A-compatible interfaces.

---

# 2. Coordination principle

> **Agents exchange intentions, tasks, decisions, and artifact references. They do not depend on copying whole conversations to each other.**

Every cross-agent interaction must be attributable to an agent identity and correlation/task ID.

---

# 3. Message envelope

```text
AgentEnvelope
- message_id
- message_type
- sender_agent_id
- recipient_agent_id | topic
- task_id
- correlation_id
- causation_id
- priority
- created_at
- expires_at?
- security_context
- payload_schema_version
- payload
- artifact_refs[]
```

Recommended message types:

```text
task.delegate
task.accepted
task.progress
task.completed
task.failed
consult.request
consult.response
decision.request
decision.response
approval.request
approval.response
event.publish
escalation
cancel
```

---

# 4. Decision Request schema

```text
DecisionRequest
- decision_request_id
- architectural_class: A | B | C | D
- requesting_agent
- title
- decision_needed
- why_now
- affected_artifacts[]
- governing_constraints[]
- options[]
- recommended_option?
- tradeoffs[]
- evidence_refs[]
- reversibility
- deadline?
- blocked_tasks[]
- reserved_human_authority: true | false | unknown
```

The Chief Architect must not be awakened by prose saying merely "what do you think?" when a structured decision request can be produced.

---

# 5. Decision Response schema

```text
DecisionResponse
- decision_request_id
- decision_status:
    approved | rejected | revise | deferred | human_required
- selected_option?
- rationale_summary
- constraints_added[]
- affected_artifacts[]
- adr_ref?
- spec_updates[]
- required_followups[]
- effective_at
- supersedes?
```

---

# 6. Artifact rule

For outputs larger than a short structured result, agents should persist the result and send a reference.

Preferred durable locations:

1. GitHub for architecture/spec/code/research artifacts;
2. controlled object/document storage for data/report artifacts not appropriate for Git;
3. Business Reality / Evidence platform for operational facts/evidence after that system exists.

Never force large reports through repeated agent-to-agent paraphrase chains when the receiving agent can retrieve the original artifact.

---

# 7. Publish/subscribe topics

Initial topic namespace:

```text
architecture.*
constitution.*
spec.*
build.*
research.*
ontology.*
evidence.*
platform.*
security.*
agent.*
source.*
```

Initial critical topics:

```text
architecture.decision_requested
architecture.decision_made
architecture.conflict_detected
constitution.amendment_proposed
spec.contract_changed
build.gate_ready
research.architecture_implication_found
ontology.extraction_contract_changed
platform.benchmark_completed
security.exception_requested
agent.blocked
agent.failed
```

---

# 8. Subscription rules

Subscriptions are part of the Agent Definition and version-controlled.

Example:

```text
ChiefArchitect:
  architecture.decision_requested
  architecture.conflict_detected
  constitution.amendment_proposed
  build.gate_ready
  security.exception_requested

Platform:
  architecture.decision_made
  ontology.query_contract_changed
  ontology.extraction_contract_changed
  build.physical_requirements_ready

EvidenceData:
  ontology.extraction_contract_changed
  security.classification_policy_changed

ExecutiveCognition:
  architecture.decision_made
  business_intent.contract_changed
  ontology.decision_context_contract_changed
```

Agents should not subscribe to every event by default.

---

# 9. Automatic wake-up rule

A subscribed event must create or resume a durable task for the subscriber.

```text
Event
 -> subscription match
 -> authorization/filter
 -> dedupe check
 -> create/resume Task
 -> schedule AgentRun
 -> context pack assembly
 -> execute
```

A notification without a durable task is informational only and does not count as guaranteed work execution.

---

# 10. Context pack

The runtime should construct a task-specific context pack rather than forwarding all prior conversation history.

```text
ContextPack
- role charter/version
- governing docs refs
- task objective
- triggering event
- dependency results
- relevant artifacts
- relevant ADRs
- relevant Business Reality / Evidence references
- authority/security scope
- previous task summary if resuming
```

---

# 11. Delegation versus handoff

## Delegation

Parent retains accountability.

```text
Chief Architect -> Research Agent
"Investigate alternatives and return recommendation."
```

## Handoff

Recipient takes task ownership.

```text
Triage -> Platform Agent
"This is a platform implementation task; you now own completion."
```

For GenSigma's leadership agents, prefer **delegation/consultation** over handoff unless ownership clearly changes.

---

# 12. Loop prevention

Runtime must reject or flag:

- repeated A -> B -> A delegation for the same unchanged task;
- duplicate decision requests within a correlation window;
- unbounded recursive subagent creation;
- event storms generated by an agent responding to its own event;
- repeated retries after terminal policy denial.

Every task should have depth/budget limits.

---

# 13. Authority enforcement

A message does not confer authority.

Receiving agent must verify that:

- sender is authenticated;
- sender may request the task;
- recipient may perform it;
- tools/data required are permitted;
- any requested side effect is within delegated authority;
- human approval is obtained where required.

---

# 14. Failure behavior

On transient failure:

```text
retry -> checkpoint -> retry budget -> dead-letter/escalate
```

On semantic uncertainty:

```text
request clarification OR return unresolved
```

On authority failure:

```text
stop -> emit policy_denied -> do not improvise around the restriction
```

On dependency failure:

```text
waiting_on_dependency -> resume when dependency event arrives
```

---

# 15. GitHub event integration

GitHub webhooks/events may be translated into internal events.

Examples:

```text
PR labeled needs-architecture-decision
 -> architecture.decision_requested

ADR merged
 -> architecture.decision_made

Build Spec section merged
 -> spec.contract_changed
```

GitHub remains the durable artifact store; the coordination runtime guarantees execution.

---

# 16. V0.1 acceptance scenario

The protocol is proven when:

1. KOE creates a structured DecisionRequest and persists supporting artifact.
2. `architecture.decision_requested` is emitted.
3. Chief Architect agent is invoked automatically without Vijay opening a chat.
4. Chief Architect retrieves only the necessary governing docs and proposal.
5. Chief Architect issues a structured DecisionResponse and ADR or asks Vijay if human-reserved.
6. `architecture.decision_made` is emitted.
7. KOE's blocked task resumes automatically.
8. End-to-end trace contains both agent runs, messages, artifacts, decision, and timestamps.
