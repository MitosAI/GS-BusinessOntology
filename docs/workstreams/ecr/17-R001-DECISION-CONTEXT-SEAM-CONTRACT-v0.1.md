# R001 - DecisionContext Seam Contract v0.1

**Status:** Candidate cross-workstream contract; READY for KOE/Platform/Chief Architect review  
**Owner:** ECR-001 - Executive Cognition Research  
**Architecture basis:** ADR-003 Hierarchical Policy Portfolio  
**Integration target:** BUILD SPEC 001 Business Reality MVP  
**Decision boundary:** This artifact specifies ECR input requirements. It does not create a canonical `DecisionContext` object or transfer semantic ownership from Business Reality, Business Intent, External Reality, Capability, Policy/Authority, or Governed Action.

## 1. Purpose

Define the smallest implementable read projection by which Business Reality and adjacent owning models can supply time-correct, security-filtered inputs to computational judgment.

The seam is an assembled projection over owned resources. It is not a second source of truth and need not be persisted. Benchmark implementations may materialize an immutable copy for replay, but that copy remains an evaluation artifact.

## 2. Governing rules

1. Every projected item retains its owning model and stable reference.
2. The caller must specify both the business-state time and the knowledge-availability boundary when replaying a historical case.
3. Security filtering occurs before data reaches a cognition arm. Redaction must not leak forbidden existence or content.
4. Unknown, ambiguous, contradicted, partial, and security-filtered results are explicit states, not empty values.
5. Scenario or hypothetical state is isolated from accepted current/historical truth.
6. Outcomes and post-decision evidence are excluded in benchmark mode until scoring.
7. Decision methods consume this projection; they do not mutate owning models through the read seam.
8. Cross-model references use stable identifiers and versioned permitted projections, not copied authoritative objects.

## 3. Request contract

Conceptual operation:

```text
assemble_decision_context(request) -> DecisionContextProjection
```

Minimum request:

```yaml
contract_version: decision-context/0.1
decision:
  question: string
  class: string
  trigger_ref: CanonicalRef | null
  scope_refs: [CanonicalRef, ...]
temporal_boundary:
  state_as_of: RFC3339 timestamp
  knowledge_as_of: RFC3339 timestamp
mode: current | historical_replay | scenario
requested_sections:
  - business_intent
  - business_reality
  - external_reality
  - capability
  - policy_authority
  - available_actions
  - evidence
  - relevant_history
security_context: SecurityContext
scenario_ref: CanonicalRef | null
```

Semantics:

- `state_as_of`: effective-time boundary for the business state being considered.
- `knowledge_as_of`: latest time at which information may have been available to the decision maker/system. In current mode it may equal request time. In historical replay it is mandatory and prevents hindsight leakage.
- `mode=scenario`: scenario overlays must be referenced and separately labeled; they never mutate canonical state.
- `requested_sections`: supports least-privilege and cost-bounded projection.

## 4. Response envelope

```yaml
contract_version: decision-context/0.1
projection_id: content-addressed or otherwise immutable identifier
generated_at: RFC3339 timestamp
request_echo:
  decision_class: string
  scope_refs: [...]
  state_as_of: RFC3339 timestamp
  knowledge_as_of: RFC3339 timestamp
  mode: current | historical_replay | scenario
result_status: ok | partial | unknown | unresolved | ambiguous | contradicted | forbidden | invalid_request
completeness: complete | bounded | security_filtered | partial_dependency_failure
sections: {}
issues: []
provenance_refs: []
source_snapshot_versions: {}
```

A successful response can still be `partial`, `ambiguous`, or `contradicted`. The response must say why and identify permitted disambiguating information where possible.

## 5. Common projected item

Every material item supplied inside a section uses a common wrapper:

```yaml
item_ref:
  canonical_id: string
  object_type: string
  model_owner: string
  contract_version: string
projection: {}
epistemic_status: observed | claimed | inferred | assumed | assessed | predicted | canonical | rejected | superseded | unresolved
effective_time: {}
available_at: RFC3339 timestamp | null
recorded_at: RFC3339 timestamp | null
provenance_refs: [...]
authority_or_source_basis_refs: [...]
explicitness: explicit | inferred | reconstructed | unknown
issues: [...]
```

Requirements:

- `available_at` must not be silently inferred in historical replay. If unavailable, the item is excluded from an accepted frozen case or explicitly marked unusable by benchmark-local validation.
- `projection` contains only fields authorized and necessary for the requested decision.
- `epistemic_status` is not a generic confidence score.
- Copied or quoted evidence must retain origin lineage so repeated copies do not masquerade as independent support.

## 6. Required sections

### 6.1 Framing

```yaml
framing:
  question: string
  decision_class: string
  trigger_ref: CanonicalRef | null
  scope_refs: [...]
  horizon: {}
  deadline: RFC3339 timestamp | null
  stakes: low | medium | high | critical | unknown
  reversibility: reversible | costly_to_reverse | irreversible | unknown
  recurrence: one_off | episodic | repeated | unknown
```

Classification may be supplied by the caller or proposed by cognition, but the provenance of either must be explicit.

### 6.2 Business Intent

References and permitted projections for applicable objectives, priorities, risk posture, strategic constraints, and decision criteria. ECR does not own these semantics.

### 6.3 Business Reality

Current/historical accepted state, relevant events and relationships, competing claims, contradictions, and correction history within the requested scope and temporal boundary.

### 6.4 External Reality

External observations, forecasts, market/customer/competitor/regulatory beliefs, and their evidence/adequacy. They remain owned by External Reality.

### 6.5 Capability

Capability assessments and the underlying permitted Reality references needed to understand feasibility, capacity, dependencies, and execution uncertainty. Dynamic capability conclusions remain owned by the Capability model.

### 6.6 Policy and authority

```yaml
policy_authority:
  hard_constraints: [...]
  policy_rules: [...]
  delegated_authority: [...]
  required_approvals: [...]
  prohibited_actions: [...]
```

Known deterministic constraints must be represented as explicit rules/conditions where possible, with rule version and authority basis. Cognition must not turn them into probabilities.

### 6.7 Available actions

References to governed action definitions plus permitted projections of preconditions, required approvals, expected effects, reversibility, and current availability. The seam does not authorize or execute an action.

### 6.8 Evidence and relevant history

Evidence references, decision-relevant timeline entries, prior analogous decisions where authorized, and explicit gaps. Retrieval must preserve provenance, effective time, availability time, epistemic status, and security projection.

### 6.9 Uncertainty and contradictions

```yaml
uncertainty:
  - uncertainty_id: string
    type: fact | identity_context | model | parameter_probability | forecast | capability_execution | strategic_response | preference_criterion | causal
    adequacy: P0 | P1 | P2 | P3 | not_applicable
    statement: string
    evidence_refs: [...]
    probability: number | null
    probability_basis_refs: [...]
contradictions: [...]
unknowns: [...]
```

`P0/P1` must have `probability: null`. `P2/P3` numeric values require a reference class, model/posterior, version, and applicable population/conditions.

## 7. Snapshot and consistency semantics

A projection is acceptable only when:

- all included items satisfy `available_at <= knowledge_as_of` in historical replay;
- state queries are evaluated at `state_as_of`;
- source snapshot or contract versions are recorded;
- cross-section references resolve consistently or the inconsistency is reported;
- security projection is evaluated for the supplied actor/service identity;
- later outcomes and later-discovered evidence are absent in benchmark mode.

The implementation may compose existing Business Reality endpoints. It does not require a new persistence technology or graph database.

## 8. Bid / No-Bid minimum profile

The first prototype requires these fields when available:

- Opportunity, Solicitation, customer/account, proposal deadline, value/term, procurement/contract vehicle, and relationship history;
- mandatory eligibility, registration, certification, compliance, and contractual constraints;
- applicable strategic objectives, target offerings/markets, risk posture, and bid authority;
- capability/skill/credential evidence, staffing availability, delivery dependencies, partner reliance, and opportunity cost;
- external/customer/competitor signals with source and probability adequacy;
- relevant prior pursuits as references, without outcome leakage beyond the historical boundary;
- governed actions such as gather evidence, request approval, form partnership, bid, decline, or stage commitment.

Missing fields remain explicit unknowns. They are not filled by model inference without being labeled as such.

## 9. Non-goals

- No canonical `DecisionContext` resource admission.
- No new source of truth or duplicated object ownership.
- No production Decision Engine, model provider, solver, database, or agent framework selection.
- No automatic approval or governed action.
- No universal requirement that every decision class populate every analytical field.
- No global confidence score.

## 10. Acceptance tests

1. A current Bid/No-Bid request returns a security-filtered projection with stable cross-model refs and contract versions.
2. Historical replay excludes an item whose `available_at` is after `knowledge_as_of`, even if its effective time is earlier.
3. Historical state uses `state_as_of` and does not project later corrections backward without labeling them.
4. Restricted evidence is neither returned nor leaked through counts/snippets; permitted derived state can remain visible.
5. Contradictory claims are returned as contradiction, not silently collapsed.
6. A scenario overlay remains separately labeled and cannot mutate accepted state.
7. P0/P1 uncertainty rejects a numeric probability; P2/P3 requires basis/model metadata.
8. Benchmark mode cannot access held-out outcomes through the projection.
9. Known hard constraints and authority rules include rule/version/basis and are machine-testable where supplied.
10. The projection can be assembled by composing existing read APIs; no new canonical type is required.

## 11. Architecture disposition

The requirements follow ADR-003 and current KOE boundaries. Freezing this as a shared cross-workstream API contract is an `ASK_ARCHITECT` decision. That review is non-blocking for current Business Reality primitives, benchmark-local contracts, synthetic fixtures, or the Bid/No-Bid harness.
