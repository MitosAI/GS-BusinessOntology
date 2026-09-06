# GenSigma OS — Workstream Delivery Standard

**Version:** v0.1  
**Status:** Governing working standard  
**Applies to:** KOE, ECR, Platform, Evidence/Data, and future specialist workstreams  
**Purpose:** Give every specialist thread one common method for thinking, researching, planning, creating durable GitHub artifacts, and handing build-ready work to Codex.

---

## 1. Operating model

Each specialist chat is a working room for its domain. GitHub is the durable system of record. Codex is the implementation workforce. Chief Architect is used only for genuine cross-cutting architecture decisions.

```text
SPECIALIST CHAT
  discuss / research / design / plan
          |
          v
       GITHUB
  durable design + execution plan + issues
          |
          +---- ASK_ARCHITECT ----> CA-001
          |                         |
          |                         v
          |                    durable decision
          |
          v
        CODEX
  bounded implementation tasks
          |
          v
    PR + CI + TESTS
          |
          v
   specialist review / learning
          |
          +--------------------> update GitHub
```

The rule is:

> **Chats think. GitHub remembers. Codex builds. CA-001 resolves cross-cutting architecture.**

---

## 2. Standard work cycle

Every specialist workstream uses the same seven-stage cycle.

```text
FRAME
  -> RESEARCH
  -> DESIGN
  -> PLAN
  -> TASK
  -> BUILD
  -> VERIFY / LEARN
```

### 2.1 FRAME

Before doing material work, state:

```text
Objective
Why now
Owned scope
Non-owned scope
Governing artifacts
Current constraints
Definition of done
```

Do not start from a technology or implementation detail when the real question is architectural or semantic.

### 2.2 RESEARCH

Research is required when the answer depends on external technical practice, scientific literature, vendor capability, architecture patterns, or empirical evidence.

Research output must separate:

```text
Established evidence / public practice
GenSigma-specific inference
Recommendation
Remaining uncertainty
```

Public practice should be checked before inventing a novel mechanism where established approaches plausibly exist.

### 2.3 DESIGN

Design enough to make the next implementation slice safe and coherent. At minimum define:

```text
Problem / objective
Invariants
Module or semantic boundaries
Interfaces / contracts
Data or state semantics where relevant
Failure / ambiguity behavior
Security / authority implications
Dependencies
Acceptance criteria
Open questions
```

Do not design the whole future system before building the next coherent slice.

### 2.4 PLAN

When design is sufficiently stable, create or update a durable execution plan in GitHub.

A plan must contain:

```text
Goal
Architecture / design basis
Deliverables
Work breakdown
Dependencies / ordering
Parallelizable work
Acceptance tests
Out-of-scope items
Known risks
Architecture questions, if any
```

A plan is not a chat summary. It is the bridge from architecture into implementation.

### 2.5 TASK

Break the execution plan into bounded GitHub issues that a coding agent can execute without reconstructing the entire project history.

Each implementation issue must contain:

```text
Owner workstream
Objective
Why this task exists
Required inputs / governing docs
Scope
Explicit non-scope
Interfaces / contracts to preserve
Dependencies
Acceptance criteria / tests
Files or modules likely affected, when known
LOCAL_SOLVE boundaries
ASK_ARCHITECT triggers
Expected output: code / tests / PR / benchmark / artifact
```

A task should normally be small enough for one Codex worker to own end-to-end.

### 2.6 BUILD

Codex executes bounded implementation tasks using repository state as context.

Each coding task should result in:

```text
branch / worktree
code
required tests
PR
implementation notes when material
new ASK_ARCHITECT request only if shared architecture is encountered
```

Parallel workers are encouraged when task dependencies allow it.

### 2.7 VERIFY / LEARN

A workstream does not stop at code generation.

Verify:

```text
acceptance tests pass
architecture invariants still hold
interfaces remain compatible
security / provenance / time behavior is preserved where applicable
CI passes
unexpected implementation findings are recorded
```

If implementation reveals a wrong assumption, update the durable design/plan or raise ASK_ARCHITECT. Do not leave the correction only in chat.

---

## 3. Decision rule

Every unresolved question has exactly two states:

```text
LOCAL_SOLVE
ASK_ARCHITECT
```

Use `LOCAL_SOLVE` for local, reversible choices inside approved architecture.

Use `ASK_ARCHITECT` only when the question changes or conflicts with shared semantics, cross-workstream contracts, security/authority, evidence/provenance/time rules, or hard-to-reverse platform/runtime architecture.

Normal specialist planning does **not** require Chief Architect approval.

---

## 4. Durable artifact rule

Material work must leave GitHub in a state where another competent session can continue without reading the originating chat.

At the end of any substantial discussion or research cycle, the specialist must ensure GitHub contains the durable result in one or more of:

```text
design / research artifact
spec / contract
execution plan
implementation issues
ADR request
PR / tests
```

Chat history may explain how we arrived there, but it is not required to continue the work.

---

## 5. Workstream update template

Use this concise update when a meaningful work cycle ends:

```text
WORKSTREAM UPDATE

Objective:

What changed:

Key findings / decisions:

Durable artifacts created or updated:

Build-ready tasks created:

Architecture questions:

Blocked work:

Next READY work:
```

This is a handoff summary, not a substitute for the underlying design or plan.

---

## 6. Research artifact template

```text
# <Topic>

Question
Why it matters to GenSigma OS

## Evidence / public practice
- source / finding
- source / finding

## Synthesis
What the evidence implies

## GenSigma-specific implications
What changes or constrains our system

## Recommendation
Recommended direction and why

## Uncertainty / experiments
What remains unknown and how to resolve it

## Architecture impact
LOCAL_SOLVE / ASK_ARCHITECT / none
```

---

## 7. Design artifact template

```text
# <Design Name>

## Objective

## Context / problem

## Governing invariants

## Boundaries
Owns:
Does not own:

## Proposed design

## Interfaces / contracts

## State / time / evidence / security semantics
Only include dimensions that materially apply.

## Failure and ambiguity behavior

## Dependencies

## Acceptance criteria

## Open questions

## Architecture disposition
LOCAL_SOLVE / ASK_ARCHITECT / no open architecture question
```

---

## 8. Execution plan template

```text
# EXECUTION PLAN — <Name>

Status: DRAFT / READY / IN_PROGRESS / COMPLETE
Owner workstream:
Design basis:

## Goal

## Deliverables

## Work breakdown
1.
2.
3.

## Dependency graph

## Parallelizable tasks

## Acceptance suite

## Risks / unknowns

## Explicitly out of scope

## Architecture questions
```

When the plan reaches `READY`, create implementation issues.

---

## 9. Implementation issue template

```text
[BUILD] <bounded task title>

Owner workstream:
Execution plan:

## Objective

## Why

## Governing artifacts

## Scope

## Non-scope

## Interfaces / invariants to preserve

## Dependencies

## Acceptance criteria
- [ ]
- [ ]
- [ ]

## Expected output
Code / tests / PR / benchmark / artifact

## Decision boundary
LOCAL_SOLVE:
ASK_ARCHITECT if:
```

---

## 10. Thread bootstrap instruction

Send this once to each current specialist chat after this standard is merged:

> **Operating model update:** Continue as the specialist lead for your existing workstream. Do not restart or summarize old work. Read `AGENTS.md`, `docs/program/08-WORKSTREAM-DELIVERY-STANDARD-v0.1.md`, `docs/protocols/AGENT-DEFINITION-AND-ESCALATION-STANDARD-v0.1.md`, your role charter, and the current governing artifacts for your work. From now on use the common cycle FRAME → RESEARCH → DESIGN → PLAN → TASK → BUILD → VERIFY/LEARN. Discussion and research may happen in this chat, but material results must be made durable in GitHub. When design is build-ready, create/update an execution plan and bounded implementation issues with acceptance criteria suitable for Codex. Use LOCAL_SOLVE for owned reversible choices and ASK_ARCHITECT only for genuine cross-cutting architecture. Continue from your current state and move toward executable output quickly.

---

## 11. Chief Architect boundary

CA-001 is not the program manager for every specialist task.

CA-001 owns:

```text
cross-workstream architecture
shared invariants / contracts
architecture conflicts
hard-to-reverse system choices
ASK_ARCHITECT dispositions
system-level integration
```

Specialist workstreams own their domain research, design, execution planning, task creation, implementation follow-through, and review inside approved boundaries.

---

## 12. Definition of ready for Codex

A task is ready for Codex when:

- its objective is unambiguous;
- governing design/contracts are named;
- scope and non-scope are explicit;
- dependencies are known;
- acceptance criteria are testable;
- architecture-sensitive boundaries are identified;
- unresolved architecture does not block correctness.

If these are not true, keep planning. If they are true, stop discussing and build.
