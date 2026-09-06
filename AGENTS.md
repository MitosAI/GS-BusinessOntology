# GenSigma OS — Repository Agent Operating Rules

**Status:** Governing working contract for AI coding/research agents operating in this repository

These instructions apply repository-wide unless a narrower approved instruction explicitly overrides them.

## 1. Read before doing material work

Every agent must begin by reading, in this order where relevant:

1. `CONSTITUTION.md`
2. `docs/program/00-PROJECT-BRIEF-v0.1.md`
3. `docs/program/01-OPERATING-ARCHITECTURE-v0.1.md`
4. `docs/program/03A-WORKSTREAM-EXECUTION-UPDATE-v0.1.md`
5. `docs/program/05-CHIEF-ARCHITECT-DECISION-METHOD-v0.1.md`
6. `docs/program/08-WORKSTREAM-DELIVERY-STANDARD-v0.1.md`
7. `docs/protocols/AGENT-DEFINITION-AND-ESCALATION-STANDARD-v0.1.md`
8. the agent/workstream role charter under `docs/roles/`
9. the relevant Build Spec, ADRs, protocols, execution plan, and task/issue

GitHub is the durable engineering source of truth. Chat history is workshop context, not canonical architecture.

All specialist workstreams use the common delivery cycle defined in `docs/program/08-WORKSTREAM-DELIVERY-STANDARD-v0.1.md`:

`FRAME -> RESEARCH -> DESIGN -> PLAN -> TASK -> BUILD -> VERIFY / LEARN`

## 2. The two-state question rule

Whenever an agent encounters an unresolved question, it has exactly two choices:

### LOCAL_SOLVE

Use LOCAL_SOLVE only when the choice:

- stays inside an already approved architecture/interface/spec;
- is local to the current implementation or research method;
- is reasonably reversible;
- does not redefine shared business semantics;
- does not change a cross-workstream contract;
- does not weaken security, provenance, authority, temporal correctness, or data integrity;
- does not create a hard-to-reverse platform commitment.

The agent should make the decision, record material implementation reasoning where useful, and continue.

### ASK_ARCHITECT

Use ASK_ARCHITECT when the question would change, invent, reinterpret, or contradict any shared architecture, including:

- ontology or canonical business semantics;
- object/relationship/event/decision/action/outcome meaning;
- evidence, provenance, promotion, identity, reconciliation, or temporal rules;
- security, authority, privacy, or approval behavior;
- shared APIs/interfaces/contracts;
- cross-workstream ownership/boundaries;
- hard-to-reverse data/platform/runtime choices;
- Constitution, ADR, Build Spec, or reference architecture assumptions.

If the correctness of a merge depends on an unresolved architectural assumption, ASK_ARCHITECT.

## 3. ASK_ARCHITECT does not mean stop all work

An unresolved architecture question blocks only the dependent work.

The agent must:

1. create an Architecture Decision Request using `.github/ISSUE_TEMPLATE/architecture-decision-request.md` or the same structure in the relevant PR;
2. mark the affected subtask as blocked by that request;
3. continue independent READY work where possible;
4. not merge code whose correctness depends on the unresolved decision.

Do not invent an architecture simply to remain busy.

## 4. Architecture Decision Request minimum payload

Every request must include:

- originating agent/workstream;
- task/PR/branch;
- exact question;
- why the question arose now;
- governing docs/ADRs already checked;
- realistic options;
- agent recommendation, if any;
- affected contracts/workstreams;
- blocked scope;
- whether unrelated work can continue;
- evidence, benchmarks, or artifact references where relevant.

## 5. Chief Architect authority

The Chief Architect owns cross-cutting architecture integration.

The Chief Architect may respond with:

- `LOCAL_DISCRETION` — this is not architecture; the originating agent owns it;
- `DECIDED` — architectural decision is made and recorded;
- `EXPERIMENT_REQUIRED` — run a bounded spike/benchmark before deciding;
- `ESCALATE_VJ` — reserved business/strategic authority requires Vijay.

Material decisions must be written back to GitHub as an ADR, spec/build-spec change, protocol update, or explicit issue/PR decision as appropriate.

## 6. Architecture dispatch

Architecture requests marked `needs-architect` or `ask-architect` may be routed automatically through the repository Chief Architect dispatch workflow. The durable GitHub request and resulting disposition remain the source of truth regardless of the transport or model session used.

Automation changes transport, not governance.

## 7. Peer-agent communication

Agents may exchange factual findings, implementation outputs, test results, research findings, and artifact references.

Agents must not settle cross-cutting architecture by informal peer consensus. If a peer discussion changes shared architecture, use ASK_ARCHITECT.

Prefer durable artifacts, issues, PRs, and typed handoffs over long free-form agent conversations.

## 8. External benchmark first — governing law

Before proposing a material solution, architecture, engineering process, orchestration mechanism, platform pattern, research method, or operating model, first check established public practice when a relevant benchmark plausibly exists.

This is mandatory, not optional.

The agent must:

1. identify the closest real-world analogue or established category;
2. inspect current public practice from serious practitioners, primary vendor documentation, credible engineering organizations, standards bodies, peer-reviewed literature, or other authoritative sources as appropriate;
3. distinguish established practice from emerging practice, vendor claims, and the agent's own inference;
4. prefer a proven standard pattern when it satisfies GenSigma's requirements;
5. invent a novel mechanism only when existing approaches are inadequate, and state exactly why they are inadequate;
6. record consequential benchmark findings or citations in the relevant durable design, ADR, research artifact, or execution plan when they materially influence a decision.

Do not start from a bespoke design when the industry has already solved the class of problem.

Do not use "industry best practice" as an unsupported phrase. Verify what leading practitioners actually do.

When current external evidence is needed, research it before giving the recommendation. If the user explicitly restricts the task to private/repository sources or prohibits external research, honor that constraint and state that the external benchmark step was intentionally skipped.

## 9. Build/research discipline

- Do not silently drift from approved doctrine.
- Do not make source schemas the ontology.
- Do not let probabilistic output silently become canonical truth.
- Do not choose infrastructure because of fashion or model preference.
- Do not broaden task scope without recording it.
- Use interfaces/contracts to isolate unresolved but reversible implementation choices.
- Tests, acceptance criteria, and architecture fitness checks are part of the contract, not optional cleanup.
- When a design is sufficiently specified for a bounded implementation task, stop discussing and build.

## 10. Durable workstream output

A specialist chat may be used for discussion, research, design, and planning, but material results must be made durable in GitHub. A competent future session must be able to continue without reading the originating chat.

Build-ready work must have an execution plan or equivalent governing design plus bounded implementation issues with explicit acceptance criteria.

## 11. Future agents and workstreams

Every future GenSigma OS agent/workstream definition must explicitly inherit:

- this file;
- `docs/program/08-WORKSTREAM-DELIVERY-STANDARD-v0.1.md`;
- `docs/protocols/AGENT-DEFINITION-AND-ESCALATION-STANDARD-v0.1.md`.

No future role should invent its own architecture-escalation or delivery protocol unless the Chief Architect formally supersedes these standards.
