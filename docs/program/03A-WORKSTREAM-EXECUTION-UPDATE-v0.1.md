# GenSigma OS — Workstream Execution Update

**Version:** v0.1  
**Status:** Governing operating-model update  
**Owner:** Chief Architect

## 1. Purpose

This document updates the execution mechanics described in the original Workstream Lead Starter Pack.

The architectural roles remain valid. The change is **how workstreams execute and communicate**.

Where the older starter pack describes separate ChatGPT threads as the primary execution mechanism, this update supersedes that mechanism with a repository-centered agent/workstream model.

## 2. Current operating model

```text
Chief Architect
     ^
     | ASK_ARCHITECT
     |
Specialist workstreams / coding or research agents
     |
     v
GitHub: specs, ADRs, tasks, issues, branches, PRs, tests
```

A workstream may currently be operated through ChatGPT, Codex, another coding agent, a human engineer, or a future persistent agent runtime. The execution surface is replaceable. The role charter and repository contracts are durable.

## 3. Mandatory question handling

Every agent/workstream inherits exactly two states for unresolved questions:

- `LOCAL_SOLVE`
- `ASK_ARCHITECT`

Definitions and escalation payloads are governed by:

- repository `AGENTS.md`;
- `docs/protocols/AGENT-DEFINITION-AND-ESCALATION-STANDARD-v0.1.md`.

## 4. Communication principle

Agents do not need continuous peer-to-peer conversation to build GenSigma OS.

Default communication is through:

- approved specs and ADRs;
- GitHub Issues/tasks;
- PRs and code review;
- tests/acceptance criteria;
- structured architecture requests when shared decisions are required.

Peer workstreams can exchange factual findings and requirements directly, but cross-cutting architecture returns to the Chief Architect.

## 5. Current limitation

GitHub is durable shared state, but it does not automatically wake an interactive ChatGPT thread. Until an event-driven Chief Architect dispatcher is implemented, `ASK_ARCHITECT` requests must be surfaced manually to the Chief Architect.

This is a transport limitation, not a change in governance.

## 6. Future automation

Later, a minimal event-driven dispatcher may automate:

```text
needs-architect event
      -> invoke CA-001
      -> resolve / request experiment / escalate
      -> write decision to GitHub
      -> unblock dependent task
```

The dispatcher must implement the same existing request/response protocol. A2A or a generalized swarm is not a prerequisite for development.

## 7. Immediate instruction to all current workstreams

Before continuing, each current workstream must re-read:

1. `AGENTS.md`;
2. this document;
3. `docs/protocols/AGENT-DEFINITION-AND-ESCALATION-STANDARD-v0.1.md`;
4. its updated role charter.

Then continue its current objective without restarting or re-inventing prior work.
