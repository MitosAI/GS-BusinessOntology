# GenSigma AI-Native Operating System — Durable Multi-Agent Operating Architecture

**Version:** v0.1  
**Status:** Chief Architect working architecture  
**Owner:** Chief Architect  
**Purpose:** Replace chat-based specialist roles with durable, addressable, event-driven agents that can coordinate, escalate, produce artifacts, and resume work without relying on a human to manually shuttle context between conversations.

---

# 1. Problem statement

The current workstream model uses separate ChatGPT threads as if they were organizational roles. That works for early design, but it has a structural flaw: a chat thread is not a continuously running worker, cannot reliably wake itself when another thread produces a dependency, and cannot function as a durable agent-to-agent coordination substrate.

GitHub provides durable shared artifacts, but GitHub alone is not an agent runtime and is not a message bus.

The system therefore needs a real agent operating architecture in which:

- each specialist role becomes an addressable agent with a durable identity;
- agents can receive work asynchronously;
- agents can delegate bounded tasks to one another;
- work survives process restarts and model/session boundaries;
- architectural escalations automatically wake the Chief Architect agent;
- agents exchange structured task/decision messages rather than relying on free-form chat;
- large work products are persisted as artifacts and passed by reference;
- every material action is observable, auditable, and authorized;
- humans remain the final authority for explicitly reserved decisions.

---

# 2. Core architectural decision

GenSigma SHALL use a **hierarchical, event-driven, durable agent organization with bounded peer collaboration**.

This is intentionally not a free-form swarm in which every agent talks to every other agent without structure.

The topology is hybrid:

```text
                              VIJAY
                      reserved human authority
                               |
                               v
                       CHIEF ARCHITECT AGENT
                  integration / architecture authority
                               |
          +--------------------+--------------------+
          |                    |                    |
          v                    v                    v
  EXECUTIVE COGNITION   KNOWLEDGE & ONTOLOGY   PLATFORM ENGINEERING
       AGENT                  AGENT                  AGENT
                                   |
                                   v
                         EVIDENCE & DATA AGENT

          <-------- bounded peer-to-peer requests -------->

                     SHARED CONTROL PLANE
       registry | task store | event bus | scheduler | policy
                      |               |
                      v               v
               SHARED ARTIFACTS    OBSERVABILITY
              GitHub / object store traces / metrics / audit
```

The hierarchy governs **authority**. It does not prohibit collaboration.

Specialists may ask one another questions or delegate bounded tasks. However, architectural decisions, cross-workstream conflicts, Constitution/spec changes, and high-impact implementation decisions route through the Chief Architect decision path.

---

# 3. Why not a pure peer-to-peer swarm

A pure swarm is attractive in demos but weak for this program because GenSigma needs durable architecture, clear authority, explicit security, and traceable decisions.

Unbounded peer chat introduces:

- circular delegation;
- duplicate work;
- conflicting conclusions;
- hidden authority changes;
- excessive token/context use;
- unclear ownership of final decisions;
- difficulty reproducing why a choice was made;
- uncontrolled information spread across security boundaries.

The system should permit agent intelligence inside a deterministic governance envelope.

---

# 4. Agent as an operational object

Each persistent agent SHALL have an explicit runtime identity and an explicit organizational identity.

A minimum Agent Definition should include:

```text
AgentDefinition
- agent_id
- role_name
- version
- charter_ref
- governing_docs[]
- skills[]
- capabilities[]
- tools[]
- permitted_data_scopes[]
- permitted_actions[]
- delegated_authority[]
- escalation_rules[]
- subscriptions[]
- runtime_policy
- model_policy
- cost_budget
- concurrency_limit
- active/inactive status
```

The model is replaceable. The agent identity, authority, charter, subscriptions, work history, and outputs are not the same thing as a model session.

This is critical: **Sarah / Chief Architect should be an organizational agent identity, not a single ephemeral chat context.**

---

# 5. Agent Registry

The Control Plane SHALL maintain an Agent Registry.

The Registry answers:

- Which agents exist?
- What can each agent do?
- What work does each agent own?
- Which agent may decide versus only recommend?
- Which events should wake each agent?
- Which tools/data may it use?
- What version of its charter/prompt is active?
- What endpoint/runtime should receive a task?

The Registry should be compatible in spirit with the A2A concept of agent discovery/Agent Cards, but GenSigma's internal registry may begin simpler.

Example:

```text
ChiefArchitectAgent
capabilities:
  - architecture_review
  - resolve_cross_workstream_conflict
  - approve_class_a_architecture_decision
  - issue_adr
subscriptions:
  - architecture.decision_requested
  - architecture.conflict_detected
  - constitution.amendment_proposed
  - build.gate_ready
  - security.exception_requested
  - workstream.blocked
```

---

# 6. Durable work objects — agents communicate through work, not chat alone

The core unit of collaboration is a **Task**, not an open-ended conversation.

Minimum coordination objects:

```text
Task
AgentMessage
ArtifactRef
DecisionRequest
DecisionResponse
Escalation
Event
AgentRun
ApprovalRequest
```

## 6.1 Task

```text
Task
- task_id
- task_type
- requested_by
- assigned_to
- objective
- input_refs[]
- required_output_schema
- constraints
- authority_scope
- priority
- due_at
- status
- correlation_id
- parent_task_id
- created_at
- updated_at
```

Suggested lifecycle:

```text
submitted
 -> accepted
 -> working
 -> waiting_on_dependency
 -> waiting_on_human
 -> completed
 -> failed
 -> cancelled
```

## 6.2 ArtifactRef

Large outputs should not be copied through multiple agents.

```text
ArtifactRef
- artifact_id
- uri / repository path
- version / commit SHA
- artifact_type
- producer_agent
- content_hash
- security_classification
- created_at
```

The receiving agent retrieves the artifact it needs, subject to authorization.

This minimizes the agentic version of the "game of telephone."

---

# 7. Communication patterns

GenSigma SHALL support five explicit communication patterns.

## 7.1 Delegate

One agent assigns a bounded task to another.

```text
KOE -> EvidenceData
"Given extraction contract v3, produce normalized source field map."
```

The delegating agent remains responsible for integrating the result unless control is explicitly handed off.

## 7.2 Ask / Consult

A specialist asks another specialist for advice without transferring ownership.

```text
Platform -> KOE
"Does this storage option preserve required temporal correction semantics?"
```

## 7.3 Escalate

A specialist detects an issue outside its authority.

```text
KOE -> Chief Architect
DecisionRequest:
  class: B
  topic: persistence semantics
  conflict: temporal corrections vs selected storage approach
  options: [A, B, C]
  evidence_refs: [...]
```

## 7.4 Publish / Subscribe

Agents publish domain events. Interested agents are automatically awakened only when subscribed.

Examples:

```text
ontology.contract_updated
buildspec.section_ready
research.architecture_implication_found
platform.benchmark_completed
architecture.decision_made
source.connector_failed
```

## 7.5 Handoff

Use only when ownership of the task itself should move to another agent.

A handoff is different from a consultation. The new agent becomes responsible for completing the task.

---

# 8. Chief Architect automatic wake-up

This is the specific mechanism that solves the current problem.

A GitHub comment does not wake the Chief Architect by itself.

Instead:

```text
WORKSTREAM AGENT
     |
     | emits ArchitectureDecisionRequested
     v
EVENT BUS / TASK ROUTER
     |
     | deterministic routing rule
     v
CHIEF ARCHITECT TASK QUEUE
     |
     v
CHIEF ARCHITECT AGENT RUN
     |
     +--> read governing docs
     +--> read requesting artifact / PR / evidence
     +--> compare against Constitution + ADRs
     +--> request specialist clarification if required
     +--> decide within delegated authority
     +--> OR escalate reserved decision to Vijay
     |
     v
ADR / SPEC / DECISION ARTIFACT
     |
     v
architecture.decision_made EVENT
     |
     +--> requesting workstream resumes
     +--> affected subscribers refresh context
```

The Chief Architect is therefore **event-driven and durable**, not "always thinking" and not dependent on a human opening a chat window.

---

# 9. Which events must wake the Chief Architect

Initial automatic escalation triggers:

```text
architecture.decision_requested
architecture.conflict_detected
constitution.amendment_proposed
canonical_concept.change_proposed
cross_workstream_contract.change_proposed
primary_database.selection_ready
security.exception_requested
agent_authority.change_proposed
build.gate_ready
build.acceptance_failed_architecturally
workstream.blocked_by_architecture
```

Events that should generally NOT wake the Chief Architect:

```text
routine source ingestion complete
normal research artifact committed
ordinary connector retry
local refactor
minor library upgrade
internal specialist note
```

This prevents the Chief Architect from becoming the throughput bottleneck.

---

# 10. Human-reserved authority

The Chief Architect should not become an autonomous constitutional dictator.

Some decisions are reserved for Vijay or explicitly delegated human authority.

Initial reserved classes should include:

- change to the fundamental GenSigma OS mission;
- change to core Constitution principles;
- material change to business intent/strategy representation;
- high-risk production action autonomy;
- access to exceptionally sensitive data classes;
- irreversible/high-cost commitments above an agreed threshold;
- changes to which agent may approve high-impact business actions;
- architecture decisions explicitly flagged by Vijay as reserved.

Flow:

```text
Chief Architect concludes: HUMAN_DECISION_REQUIRED
       |
       v
structured Decision Brief
- issue
- recommended option
- alternatives
- evidence
- tradeoffs
- reversibility
- deadline
       |
       v
Vijay
       |
       v
Decision recorded -> agents resume
```

---

# 11. Deterministic orchestration versus LLM orchestration

The system SHALL deliberately mix both.

## Deterministic code/workflow should own

- mandatory escalation rules;
- authority boundaries;
- task state transitions;
- retries/timeouts;
- rate limits;
- approval gates;
- scheduled triggers;
- event subscriptions;
- security checks;
- checkpoint/resume behavior;
- budget/concurrency limits;
- exact irreversible side-effect rules.

## LLM reasoning may own

- decomposing open-ended research;
- choosing which specialist to consult within permitted options;
- generating hypotheses;
- assessing whether a finding is materially architectural;
- synthesizing specialist outputs;
- proposing alternatives;
- drafting Decision Requests and ADR rationale.

The principle is:

> **Use models to reason; use deterministic orchestration to govern.**

---

# 12. Shared state must be separated into four kinds

```text
1. ORGANIZATIONAL TRUTH
   Business Reality / ontology / evidence

2. ENGINEERING TRUTH
   Constitution / ADRs / specs / code / GitHub artifacts

3. ORCHESTRATION STATE
   task status / dependencies / retries / checkpoints / run IDs

4. AGENT WORKING MEMORY
   private summaries / scratch state / temporary plans
```

These must not collapse into one database or one chat history.

Agent working memory never becomes organizational or engineering truth without explicit promotion.

---

# 13. GitHub's role

GitHub remains the durable source of truth for architecture, specifications, code, reviews, and ADRs.

It is **not** the primary real-time agent coordination mechanism.

GitHub SHOULD participate as:

```text
agent creates artifact/branch/PR
        |
        v
GitHub webhook
        |
        v
event router
        |
        v
subscribed agent task
```

Examples:

- PR labeled `needs-architecture-decision` -> wake Chief Architect.
- ADR merged -> emit `architecture.decision_made`.
- Build Spec updated -> notify Platform and Evidence/Data agents.

---

# 14. Protocol boundary: A2A versus MCP

GenSigma should preserve the conceptual distinction:

```text
A2A = AGENT <----> AGENT
MCP = AGENT <----> TOOL / DATA / SERVICE
```

MCP is appropriate for exposing tools, repositories, source systems, search services, world-model APIs, calculators, browsers, and similar capabilities.

A2A is appropriate for independent agent discovery, task exchange, asynchronous status, artifacts, and cross-agent collaboration.

GenSigma does not need full A2A compliance on day one. However, internal agent contracts should avoid designs that make later A2A compatibility difficult.

---

# 15. Recommended runtime direction

## Architectural recommendation

Keep the **agent semantics and protocols framework-neutral**.

## Initial implementation frontrunner

Because GenSigma already leans Azure and needs long-lived/background agents, event-driven wake-ups, multi-agent workflows, checkpoints, retries, human-in-the-loop pauses, and durable state, **Microsoft Agent Framework with the Durable Extension is the current leading implementation candidate for the orchestration/runtime shell**.

This is not yet a constitutional commitment.

OpenAI Agents SDK remains attractive for lightweight agent definitions, manager/handoff patterns, guardrails, sessions, and tracing. It can also be used inside a durable orchestration shell if that proves architecturally cleaner.

The Platform Engineering Lead should benchmark/validate runtime fit before finalizing the framework ADR.

---

# 16. Agent execution topology for V0.1

Do not begin with a large swarm.

Start with five durable agents:

```text
CA   Chief Architect
ECR  Executive Cognition Research
KOE  Knowledge & Ontology Engineering
EDE  Evidence & Data Engineering
PEL  Platform Engineering
```

Each gets:

- one durable identity;
- one charter/version;
- one task queue;
- one event subscription set;
- scoped tools;
- scoped source access;
- one working-memory namespace;
- one artifact output location;
- a run/token/cost budget;
- explicit escalation rules.

No autonomous spawning of unlimited new agents in V0.1.

Subagents may be ephemeral for bounded research or coding tasks, but their parent lead remains accountable.

---

# 17. Example: Knowledge Lead needs Chief Architect decision

```text
1. KOE discovers a conflict:
   BusinessRelationship can be modeled as object or interface.

2. KOE creates DecisionRequest DR-0042:
   - problem
   - affected specs
   - alternatives
   - recommendation
   - evidence/pressure tests
   - reversibility

3. KOE emits:
   architecture.decision_requested

4. Router creates durable task for CA.

5. CA wakes automatically.

6. CA reads:
   Constitution
   current ontology spec
   KOE proposal
   relevant benchmark/pressure-test artifacts

7. CA may call KOE as consultant for clarification.

8. CA decides:
   keep umbrella semantic interface; defer single physical object.

9. CA writes ADR.

10. ADR merge emits:
    architecture.decision_made

11. KOE, EDE and Platform subscribers resume/update work.
```

No human has to copy a GitHub comment into another chat.

---

# 18. Example: specialist-to-specialist communication

```text
Platform Agent
   |
   | AskRequest
   v
Ontology Agent
"Benchmark option X cannot support property-level temporal correction cheaply.
Is this semantic requirement mandatory for MVP or only future-state?"
   |
   v
Ontology Agent answers with structured requirement + spec reference
   |
   v
Platform continues
```

This is direct peer collaboration and does not need Chief Architect involvement unless the answer changes shared doctrine.

---

# 19. Reliability requirements

Every durable agent run should support:

- idempotent task acceptance;
- stable task IDs and correlation IDs;
- retry with bounded backoff;
- checkpoint/resume;
- duplicate event detection;
- timeout and dead-letter behavior;
- cancellation;
- dependency waits;
- human approval waits;
- explicit failure reason;
- artifact checksums;
- run/version provenance.

No agent should lose a multi-hour workstream because a model request or host process failed.

---

# 20. Observability requirements

The Control Plane should capture:

```text
trace_id
agent_id
agent_version
model/version
parent task
input artifact refs
output artifact refs
tool calls
handoffs/delegations
policy/guardrail results
latency
token/cost usage
status transitions
retries
human approvals
final outcome
```

We should be able to reconstruct why an agent was awakened, what it saw, what it delegated, what it produced, and what downstream work it triggered.

---

# 21. Context engineering rule

Agents should not automatically receive full history from all other agents.

The Context Engine should construct a scoped context pack from:

- charter and governing doctrine;
- current task;
- relevant Git/ADR/spec artifacts;
- relevant World Model state/evidence;
- relevant prior run summaries;
- dependency results;
- current permissions.

This preserves security and reduces context pollution.

---

# 22. Cost and effort controls

Multi-agent systems can consume substantially more model/tool resources than single-agent workflows.

V0.1 must therefore enforce:

- maximum subagent count;
- token/model budget per task;
- max tool calls;
- task complexity classes;
- timeout limits;
- escalation when a task exceeds budget;
- parallelism only when work is genuinely separable.

Do not create five agents for a task one agent can complete reliably.

---

# 23. Evaluation strategy

Evaluate both local quality and organizational behavior.

## Local agent tests

- did the specialist produce a correct artifact?
- did it use proper sources/tools?
- did it stay inside authority?

## Coordination tests

- was the correct agent selected?
- did duplicate work occur?
- was architectural conflict escalated?
- did downstream agents receive the decision?
- was sensitive context over-shared?
- did the workflow recover after a forced failure?

## End-state tests

For a complex multi-agent task, judge the final durable repository/world state, not whether agents followed one exact conversational path.

---

# 24. V0.1 build sequence

```text
A. Define Agent Registry schema
B. Define Task / DecisionRequest / ArtifactRef schemas
C. Implement durable task runtime
D. Implement event router + subscriptions
E. Instantiate Chief Architect Agent
F. Instantiate KOE and Platform Agents
G. Prove architecture-decision escalation end-to-end
H. Add ECR and Evidence/Data agents
I. Add GitHub webhooks / artifact events
J. Add scoped MCP tools
K. Add A2A-compatible boundary where useful
L. Add observability + coordination evals
```

The first proof should be tiny:

```text
KOE agent creates architecture decision request
        -> CA wakes automatically
        -> CA reads relevant Git artifacts
        -> CA issues structured decision
        -> decision is committed
        -> KOE resumes automatically
```

If that works reliably, we have crossed from "multiple chats" to a genuine multi-agent engineering organization.

---

# 25. Decisions versus open items

## Decided

- Move from chat-role simulation to durable agents.
- Use hierarchical governance with bounded peer collaboration.
- Use structured tasks/events for coordination.
- Chief Architect must be event-addressable and automatically invokable.
- GitHub remains durable engineering truth, not the message bus.
- Large outputs pass by artifact reference rather than repeated conversation copying.
- Deterministic workflow governs authority/reliability; LLMs supply reasoning.
- MCP and agent-to-agent communication remain distinct concerns.

## Tentative

- A2A-inspired/compatible agent boundary.
- Microsoft Agent Framework Durable Extension as initial orchestration/runtime frontrunner.

## Open

- exact event-bus technology;
- exact durable task store;
- exact agent runtime framework mix;
- whether all agents expose A2A endpoints in V0.1;
- exact GitHub webhook/event mapping;
- exact working-memory implementation;
- exact agent cost/model routing policy.

These belong to Platform Engineering ADRs after a thin prototype validates the semantics above.
