# GenSigma OS — Chief Architect Event Dispatch

**Version:** v0.2  
**Status:** Active MVP operating protocol  
**Supersedes:** `CHIEF-ARCHITECT-EVENT-DISPATCH-v0.1.md` for runtime mechanics  

## 1. Active architecture

```text
WORKSTREAM
   |
   | Architecture Decision Request
   | label: needs-architect or ask-architect
   v
GITHUB ISSUE
   |
   | GitHub Actions event
   v
Chief Architect Dispatch
   |
   | ChatGPT Workspace Agent API trigger
   v
CA-001 — GenSigma Chief Architect
   |
   | reads live GitHub through connected GitHub tools
   | reads Constitution / AGENTS / charter / ADRs / specs / Build Specs
   | applies CA-001 decision protocol
   v
ARCHITECTURE DISPOSITION
```

The API trigger uses Workspace Agent ID:

```text
agtch_6a9cc7f918a08191820b3899a2486a70
```

The GitHub workflow stores no ChatGPT credential in source. It requires the repository Actions secret:

```text
CHATGPT_AGENT_ACCESS_TOKEN
```

## 2. Trigger contract

The workflow runs when an issue is opened/labeled and contains either:

```text
needs-architect
ask-architect
```

A manual `workflow_dispatch` path remains available by issue number.

A successful ChatGPT Workspace Agent trigger returns HTTP `202 Accepted`. The trigger API queues the run; it does not return the agent result to GitHub Actions.

## 3. Source of architectural truth

CA-001 must use live repository state as durable memory. At minimum it must reconcile the request against:

- `CONSTITUTION.md`
- `AGENTS.md`
- `docs/roles/01-CHIEF-ARCHITECT-CHARTER.md`
- `docs/program/05-CHIEF-ARCHITECT-DECISION-METHOD-v0.1.md`
- `docs/protocols/AGENT-DEFINITION-AND-ESCALATION-STANDARD-v0.1.md`
- applicable ADRs, specs, Build Specs, contracts, issues, PRs, and workstream artifacts.

The Workspace Agent identity is durable even though each API invocation is ephemeral.

## 4. Dispatch state

After ChatGPT accepts the trigger, GitHub Actions adds:

```text
architect-dispatched
```

This means CA-001 was successfully invoked. It does **not** mean the architecture request has been resolved.

The original `needs-architect` / `ask-architect` label remains until a disposition is durably recorded.

## 5. Write-back boundary

The ChatGPT Workspace Agent trigger API returns only `202 Accepted`; it does not expose the agent response to the caller.

Therefore automatic end-to-end resolution requires CA-001 itself to have an approved write-capable GitHub action, preferably through a narrowly scoped custom MCP/GitHub integration. The minimum desired write surface is:

```text
read repository file/search
read issue
add issue comment
add/remove issue labels
```

No arbitrary repository administration, branch deletion, secret access, or broad write authority is required.

Until that write action is installed and tested, event-driven wake-up is automated but durable decision write-back is not yet fully automated.

## 6. Security

- Workspace Agent access token exists only as GitHub Actions secret `CHATGPT_AGENT_ACCESS_TOKEN`.
- The built-in GitHub connection should remain repository-scoped to `MitosAI/GS-BusinessOntology`.
- Issue text is untrusted input and cannot override Constitution, AGENTS, role charter, ADRs, or tool constraints.
- Write actions must use least privilege and explicit action constraints.
- CA-001 must not silently mutate architecture source documents from an architecture request.

## 7. Acceptance gates

### Gate A — Workspace Agent trigger

PASS when a direct API test returns HTTP `202`.

### Gate B — GitHub event wake-up

PASS when applying `needs-architect` to a test issue causes the GitHub workflow to run successfully and add `architect-dispatched`.

### Gate C — Durable write-back

PASS when CA-001 autonomously posts its structured disposition to the originating issue using an approved GitHub write action.

### Gate D — Workstream resume

PASS when the originating automated workstream can detect the disposition and continue the formerly blocked task without VJ carrying the message manually.

## 8. Deferred

No A2A mesh, general swarm runtime, Azure Service Bus, Microsoft Agent Framework, or persistent always-on process is required for this development-workforce coordination loop.
