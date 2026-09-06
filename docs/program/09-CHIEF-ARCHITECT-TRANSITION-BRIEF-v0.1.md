# GenSigma OS — Chief Architect Transition Brief

**Version:** v0.1  
**Status:** Active transition brief  
**Purpose:** Transfer Chief Architect work from the legacy ChatGPT thread into CA-001 Workspace Agent without requiring the agent to read historical chat transcripts.

## 1. Operating transition

The prior Chief Architect chat is deprecated for ongoing architecture work. CA-001 Workspace Agent is the sole Chief Architect working room going forward.

Specialist chats remain active working rooms for their domains:
- Knowledge & Ontology Engineering (KOE)
- Executive Cognition Research (ECR)
- Platform Engineering
- Evidence & Data Engineering (EDE)

Specialists own discussion, research, domain architecture, planning, and task decomposition within their approved boundaries. They make durable outputs in GitHub and escalate only genuine cross-cutting architecture through `ASK_ARCHITECT`.

Operating shorthand:

> **Chats think. GitHub knows. Codex builds. CA-001 governs cross-cutting architecture.**

Linear is expected to become the work-management/control plane for general implementation tasks, dependencies, priorities, and status. It is not a current blocker. Until connected, GitHub issues may continue to hold implementation tasks.

## 2. Benchmark-first governing law

Before proposing a material architecture, engineering mechanism, workflow, platform pattern, research approach, or orchestration method, inspect established public practice from serious practitioners first.

Rules:
- identify the closest real-world benchmark;
- distinguish mature practice from emerging/vendor-specific claims;
- prefer proven patterns when they fit;
- invent only where GenSigma requirements genuinely differ;
- record consequential benchmark findings in durable artifacts;
- do not label something “industry best practice” without verification.

## 3. North-star system intent

Build the operating brain of GenSigma, not an AI assistant sitting beside GenSigma.

The target is an AI-native company operating system in which a governed operational world model is the shared substrate for humans, agents, reasoning, evidence, decisions, actions, outcomes, and learning.

Core conceptual flow:

```text
BUSINESS INTENT
      |
      v
BUSINESS REALITY <---- EXTERNAL WORLD MODEL
      |
      +-------------------+
                          v
                    CAPABILITY MODEL
                          |
                          v
                 DECISION ENGINE
                          |
                          v
                      DECISION
                          |
                          v
                  GOVERNED ACTION
                          |
                          v
                 NEW BUSINESS REALITY
                          |
                          v
                 OUTCOME / LEARNING
```

## 4. Governing ontology doctrine

Palantir is the primary governing ontology doctrine.

Key rules:
1. Model the real business, not source schemas.
2. One canonical concept with clear ownership.
3. Stable promoted core, extensible around it.
4. Composition/interfaces over deep inheritance.
5. Actions are first-class; nouns need verbs.
6. Security belongs inside the ontology.
7. Material writes occur through governed typed business actions, not arbitrary CRUD.
8. Scenarios are isolated hypothetical worlds.
9. Ontology changes are governed like software.
10. Decisions connect to outcomes and learning.
11. Design around decision loops, not giant noun inventories.
12. The ontology is kinetic, not merely descriptive.

Canonical five-dimensional frame:

```text
1. WORLD
2. TEMPORAL / EVENT
3. DECISION
4. KINETIC
5. OUTCOME / LEARNING
```

Cross-cutting concerns: Evidence, Provenance, Security, Authority, Time, Confidence, Governance.

## 5. Executive cognition architecture

Working loop:

```text
INTENT -> OBSERVE -> ORIENT -> DECIDE -> ACT -> VERIFY -> LEARN -> UPDATE MODELS -> REPEAT
```

ADR-003 establishes a hierarchical policy portfolio for the Decision Engine:
- deterministic governance shell;
- decision-class routing;
- modular Bayes/optimization/scenario/game-theory methods where appropriate;
- LLM as a component, not the engine;
- challenge/sensitivity;
- governed action and outcome learning.

Bid/No-Bid is the first decision prototype; Staffing/Resource Assignment is second.

## 6. Evidence/discovery doctrine

> Discovery observes and proposes. Ontology defines and governs.

Raw discovery never directly mutates canonical ontology.

Pipeline:

```text
Source
 -> Raw Snapshot / Raw Evidence
 -> Normalized / Extracted Candidates
 -> Identity Resolution
 -> Authority / Conflict Evaluation
 -> Validation
 -> Governed Promotion
 -> Canonical Ontology
```

Evidence preserves provenance and uncertainty. Promotion into canonical truth is governed and reversible through correction/history semantics.

## 7. Development operating model

All specialist workstreams follow:

```text
FRAME -> RESEARCH -> DESIGN -> PLAN -> TASK -> BUILD -> VERIFY / LEARN
```

Relevant governing files include:
- `AGENTS.md`
- `docs/program/08-WORKSTREAM-DELIVERY-STANDARD-v0.1.md`
- `docs/protocols/AGENT-DEFINITION-AND-ESCALATION-STANDARD-v0.1.md`
- `docs/program/05-CHIEF-ARCHITECT-DECISION-METHOD-v0.1.md`
- the relevant role charter, Build Spec, ADRs, execution plan, PR, and task.

Every unresolved question is either:
- `LOCAL_SOLVE` — local, reversible, within approved architecture; or
- `ASK_ARCHITECT` — cross-cutting/shared architecture, hard-to-reverse choices, shared semantics/interfaces/security/provenance/time/ownership, or contradiction with governing artifacts.

CA responses are:
- `LOCAL_DISCRETION`
- `DECIDED`
- `EXPERIMENT_REQUIRED`
- `ESCALATE_VJ`

## 8. Development workforce vs runtime agents

Do not conflate development tooling with the future GenSigma operational agent runtime.

For development:
- GitHub is durable engineering knowledge/source of truth.
- Specialist chats are working rooms.
- Codex agents are disposable implementation workers for bounded tasks.
- Each coding task should have scope, governing design, interfaces, dependencies, acceptance criteria, and tests.
- Parallel Codex workers should use isolated branches/worktrees and converge through PRs/CI.
- No general agent-to-agent chat mesh is required.

Future GenSigma runtime agents are a separate architecture problem and may require durable identity, wakeup, retries, approvals, security, and event-driven runtime infrastructure.

## 9. Current repository/build state at transition

Repository: `MitosAI/GS-BusinessOntology`

Important current artifacts/state:
- Foundation specs 01–07 are on `main`.
- `AGENTS.md` and program operating documents are on `main`.
- `docs/program/08-WORKSTREAM-DELIVERY-STANDARD-v0.1.md` is governing.
- PR #3: KOE semantic foundation and executable contracts — open; requires reconciliation with `main`.
- PR #4: ECR computational executive judgment foundation — open.
- PR #7: executable Business Reality reference kernel — open and based on the KOE branch because it depends on PR #3 contracts.
- Reference Business Reality kernel tests/CI have passed.

The reference kernel currently demonstrates:
- runtime loading/validation of JSON Schema contracts;
- append-oriented replay-idempotent Raw Evidence;
- candidates requiring known evidence;
- governed candidate -> canonical promotion;
- promotion ledger preserving lineage;
- no direct arbitrary canonical put;
- non-destructive correction/history;
- executable invariant tests and CI.

## 10. Immediate product direction

Priority is Enterprise System product work, not more inter-agent plumbing.

Immediate sequence:
1. Reconcile PR #3 with latest `main` so semantic contracts can land cleanly.
2. Retarget/reconcile PR #7 onto `main` after PR #3 lands.
3. Continue the executable Business Reality kernel with:
   - typed relationships;
   - temporal/as-of reads;
   - security-context enforcement;
   - query/context API.
4. Then implement bounded Outlook/SharePoint evidence ingestion into evidence -> candidate -> canonical flow.
5. Pressure-test against representative RFP-to-cash scenarios.
6. Select production persistence/storage only after representative semantics, temporal queries, security, and workload shapes are concrete.
7. Continue ECR decision-engine research/prototypes in parallel.

## 11. Explicitly deferred / open decisions

Still open unless superseded by a later ADR:
- production database/persistence architecture;
- graph vs relational physical model;
- vector/search architecture;
- exact runtime agent framework;
- identity-resolution algorithms/thresholds;
- `BusinessRelationship` physical representation;
- `DecisionTrace` persistence;
- production kinetic runtime;
- Symphony or other high-concurrency coding-agent orchestration.

Do not prematurely freeze these choices without benchmark-first analysis, quality scenarios, and where appropriate a bounded spike.

## 12. Deprecated paths

Do not resume these as default approaches:
- the legacy Chief Architect chat as the active architecture authority;
- converting every specialist lead into a Workspace Agent merely because it is a “lead”;
- custom agent-to-agent messaging mesh;
- custom MCP solely for workstream coordination;
- Workspace Agents directly spawning Codex as an assumed native capability;
- building a bespoke orchestration layer before an observed scaling bottleneck exists.

## 13. CA-001 takeover instruction

On takeover, CA-001 should:
1. read the governing repository files and this transition brief;
2. inspect current PRs/issues/artifacts before making new architectural claims;
3. treat GitHub, not this historical chat, as durable truth;
4. preserve locked doctrine unless formally amended;
5. use benchmark-first analysis for material new decisions;
6. keep specialists moving independently inside their domain authority;
7. resolve only genuine cross-cutting architecture and integration issues;
8. keep product implementation moving quickly;
9. write all material decisions back to GitHub.
