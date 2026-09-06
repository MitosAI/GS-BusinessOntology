# GenSigma OS — Agent Definition and Escalation Standard

**Version:** v0.1  
**Status:** Governing working standard  
**Owner:** Chief Architect  
**Applies to:** Current and future research, engineering, coding, and operational agents/workstreams

---

## 1. Purpose

GenSigma OS will use multiple AI-assisted workstreams and coding agents. Parallelism is useful only if architectural coherence is preserved.

This standard defines the minimum contract every agent/workstream must inherit so agents can move quickly without silently creating incompatible architecture.

The standard intentionally avoids requiring a full A2A runtime. Communication is primarily artifact- and task-driven through GitHub until evidence justifies more elaborate orchestration.

---

## 2. Agent definition schema

Every agent/workstream definition must state at minimum:

```text
Agent / Workstream ID
Mission
Owned decisions
Non-owned decisions
Governing sources
Inputs
Outputs
Tools / data access
Security / authority boundaries
Dependencies
Acceptance criteria
Escalation rule
Durable artifact location
```

An agent identity is a role contract, not a particular model session. The model, UI, coding environment, or provider may change without changing the role's architectural authority.

---

## 3. Mandatory two-state unresolved-question policy

Every unresolved question must be classified as exactly one of:

```text
LOCAL_SOLVE
or
ASK_ARCHITECT
```

### 3.1 LOCAL_SOLVE

The agent owns the answer when all material effects remain inside approved boundaries.

Typical examples:

- internal class/function decomposition;
- naming of a private helper;
- test fixture organization;
- local retry implementation consistent with approved behavior;
- research search sequencing;
- choosing between equivalent libraries behind an approved interface when the choice is reversible and non-architectural.

Local solve does not require Chief Architect approval.

Material local decisions should still be recorded in code, PR notes, tests, or implementation documentation when future maintainers would otherwise lose the rationale.

### 3.2 ASK_ARCHITECT

Escalate when the answer could change shared architecture or create a durable assumption outside the agent's authority.

Triggers include:

- new/redefined canonical ontology concept;
- changed meaning of an existing object, relationship, event, decision, action, outcome, evidence or capability;
- changed identity/reconciliation/promotion/authority/temporal semantics;
- new or changed cross-workstream API/contract;
- security/privacy/access-control changes;
- hard-to-reverse persistence/runtime/platform decisions;
- contradiction with Constitution, ADR, Build Spec, or approved spec;
- competing workstream requirements;
- a decision that would materially constrain future architecture;
- uncertainty where code cannot be safely merged without choosing an architecture.

The originating agent should include its recommendation. Escalation is not permission to offload routine thinking to the architect.

---

## 4. Non-blocking execution rule

Architecture escalation is a dependency boundary, not a reason for the whole worker to go idle.

When ASK_ARCHITECT occurs:

```text
current task
   |
   +--> dependent subtask -> BLOCKED_BY_ARCH_REQUEST
   |
   +--> independent work -> remains READY
```

The agent should continue READY work that does not embed the unresolved assumption.

Where useful, the agent may code behind a stable approved abstraction so multiple future implementations remain possible. It must clearly mark provisional assumptions and may not merge code whose correctness depends on the unresolved architectural choice.

---

## 5. Architecture Decision Request contract

An Architecture Decision Request is a durable handoff object.

Minimum form:

```text
ADR Request ID:
Originating agent/workstream:
Task / issue / PR / branch:
Question:
Why this arose:
Existing governing material checked:
Options:
Recommendation:
Trade-offs / consequences:
Affected workstreams/contracts:
Blocked scope:
Can independent work continue?:
Evidence / benchmark / artifact links:
Urgency:
```

The request should be concise enough to decide but complete enough that the Chief Architect does not need to reconstruct the entire workstream history.

---

## 6. Chief Architect response contract

The Chief Architect must classify the response as one of:

### LOCAL_DISCRETION
The question is within the originating agent's authority. No architecture decision is required.

### DECIDED
A cross-cutting architecture decision is made. The durable artifact is updated accordingly.

### EXPERIMENT_REQUIRED
The architecture cannot be responsibly decided from current evidence. A bounded benchmark/spike is specified with decision criteria.

### ESCALATE_VJ
The decision requires founder/business authority or changes a reserved strategic commitment.

The Chief Architect must identify the authoritative artifact that records the resolution.

---

## 7. Communication topology

The default development topology is:

```text
                       CHIEF ARCHITECT
                              ^
                              |
                   ASK_ARCHITECT only
                              |
       +----------------------+----------------------+
       |                      |                      |
       v                      v                      v
Knowledge/Ontology      Platform              Cognition Research
       |                      |                      |
       +-------- factual/artifact handoffs ----------+
                              |
                       Evidence/Data
```

Agents may collaborate laterally on owned facts and requirements. Architectural authority does not emerge from majority vote or peer consensus.

---

## 8. Durable communication surfaces

Prefer, in order:

1. approved repository artifacts/specs/ADRs;
2. GitHub Issues for unresolved decision requests or cross-workstream tasks;
3. PR descriptions/comments for implementation-specific questions tied to a change;
4. chat/interactive discussion as a workshop only, with material outcomes written back to GitHub.

Do not rely on one agent's private conversation state as organizational memory.

---

## 9. Dispatch today versus later

### Current state

A GitHub request is durable but does not automatically invoke the Chief Architect ChatGPT thread. A human/operator must surface the request.

### Future state

A minimal event-driven dispatcher may subscribe to a marker such as `needs-architect`, invoke CA-001, and write the decision back to GitHub.

That automation changes transport, not governance. The two-state rule and request/response contracts remain the same.

A2A or a broader multi-agent message bus is not required to begin building GenSigma OS.

---

## 10. Agent model independence

No role is defined by a specific LLM.

A future agent definition may include a model policy, for example:

```text
research / synthesis -> strong research/reasoning model
coding -> coding-optimized model
routine extraction -> lower-cost model if evals permit
high-impact architecture -> strongest approved reasoning model + human governance where required
```

Model routing is an implementation concern governed by evaluation, quality, cost, latency, privacy, and tool requirements. It must not alter role authority.

---

## 11. Failure modes this standard prevents

- coding agent silently invents ontology semantics;
- platform agent chooses a database before logical workloads are known;
- research agent turns a hypothesis into canonical architecture;
- evidence pipeline redefines canonical truth for implementation convenience;
- several agents independently create incompatible interfaces;
- an agent stops all useful work because one subtask is awaiting architecture;
- a chat answer resolves a major decision but is never committed to the repo;
- architecture questions accumulate without a clear owner.

---

## 12. Definition-of-ready for a future agent/workstream

A new agent/workstream is not ready to start until its charter:

- identifies owned versus non-owned decisions;
- references repository `AGENTS.md` and this standard;
- defines inputs/outputs and durable artifact locations;
- states LOCAL_SOLVE versus ASK_ARCHITECT behavior;
- identifies Chief Architect escalation path;
- defines acceptance criteria;
- contains enough governing-source references to start without relying on oral/chat memory.

---

## 13. Definition-of-done for an architectural question

An architectural question is not resolved merely because an answer was spoken or posted.

It is done when:

1. the Chief Architect has classified/resolved it;
2. the decision/experiment/escalation is recorded in the appropriate durable artifact;
3. affected workstreams can find the resolution;
4. the blocked dependency can be marked READY or redirected;
5. future agents can answer the same question from the repository without asking again.