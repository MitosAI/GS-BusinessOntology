# GenSigma AI-Native Operating System — Architecture Integration & Inter-Layer Contracts

**Version:** v0.1  
**Status:** Chief Architect working specification  
**Owner:** Chief Architect  
**Governing sources:** Constitution, Project Brief, Operating Architecture, foundation specs, approved ADRs  
**Decision method:** `docs/program/05-CHIEF-ARCHITECT-DECISION-METHOD-v0.1.md`

---

# 1. Objective

Parallel workstreams must be able to move quickly without creating five incompatible versions of GenSigma OS.

This document freezes the current top-level vocabulary and defines the contracts between:

- Business Intent;
- Business Reality;
- External World Model;
- Capability Model;
- Executive Judgment;
- Decision / Approval;
- Kinetic Action;
- Outcome / Learning;
- Evidence / Data Engineering;
- Knowledge / Ontology Engineering;
- Platform Engineering.

It deliberately specifies **semantic and behavioral contracts before physical implementation**.

---

# 2. Canonical operating model

```text
                      CONTROL & GOVERNANCE
             Identity · Security · Policy · Authority
                         Audit · Risk
                              |
                              v
                       BUSINESS INTENT
      Purpose · Mission · Vision · Strategy · Goals · Plans
          Preferences · Risk Appetite · Decision Principles
                              |
                              v
                       BUSINESS REALITY
     Canonical current + historical state of GenSigma and its
        direct business relationships, decisions and actions
                              |
                 +------------+------------+
                 |                         |
                 v                         v
        EXTERNAL WORLD MODEL        CAPABILITY MODEL
     Selected beliefs about the    What GenSigma can actually
       material outside world       do with current resources,
     that may affect decisions      authority and constraints
                 |                         |
                 +------------+------------+
                              |
                              v
                    EXECUTIVE JUDGMENT
     Evidence · uncertainty · alternatives · evaluation · models
                              |
                              v
                     DECISION / APPROVAL
                              |
                              v
                        KINETIC ACTION
                              |
                              v
                     NEW BUSINESS STATE
                              |
                              v
                     OUTCOME / LEARNING
                              |
                              +----> governed updates to models
```

This replaces ambiguous use of `World Model` as an umbrella for several different concepts.

`World Model` may still appear historically in older documents, but new work should distinguish **Business Reality** from **External World Model**.

---

# 3. Layer ownership

## 3.1 Business Intent

Owns:

- purpose / mission / vision / values;
- business model and offerings;
- strategic priorities;
- goals / OKRs / targets;
- risk appetite;
- decision principles;
- plans / initiatives;
- explicit strategic assumptions that function as planning premises.

Does not own:

- operational facts;
- external raw observations;
- execution details;
- evidence promotion.

Change mode: deliberate, governed, generally slower than operational state.

## 3.2 Business Reality

Owns:

- canonical Organization / Person identities;
- business relationships;
- commercial, delivery, workforce, finance, compliance and systems state;
- events;
- decisions / approvals / actions / outcomes as historical or current business facts;
- current and historical state;
- canonical facts with provenance and authority.

Does not own:

- unvalidated source observations;
- goals/preferences;
- outside-world strategic beliefs;
- optimization or recommendation logic.

Change mode: operationally responsive.

## 3.3 External World Model

Owns:

- material beliefs about external reality;
- evidence and assessments supporting those beliefs;
- uncertainty;
- belief history;
- external strategic hypotheses.

Examples:

- SLED funding environment;
- regulatory shifts;
- technology adoption patterns;
- customer administration changes;
- competitive moves;
- labor market conditions;
- macro factors only where material.

Does not own the entire external information stream.

## 3.4 Capability Model

Owns a decision-ready representation of feasible action:

- current skills;
- capacity / availability;
- cash / budget;
- partner capability;
- systems / assets;
- contractual/legal authority;
- timing constraints;
- dependencies;
- actions currently available to an actor.

Underlying facts should resolve to Business Reality. This model should avoid independent duplicate truth.

## 3.5 Executive Judgment

Owns:

- decision-context assembly;
- belief/uncertainty transformation appropriate to the decision class;
- alternative generation;
- evaluation against intent, constraints and risk;
- strategic interaction analysis;
- optimization where appropriate;
- recommendation;
- rationale / assumptions / uncertainty;
- decision-method provenance.

It does not get to declare canonical truth or bypass authority.

## 3.6 Decision / Approval

Decision = choice made.

Approval = authority granted to execute where separate approval is required.

A recommendation does not become a Decision merely because an LLM generated it.

## 3.7 Kinetic Action

Owns governed execution:

- typed action;
- authorized actor;
- preconditions;
- policies;
- required approvals;
- expected state transition;
- external write-back/tool call;
- execution status;
- verification;
- audit.

## 3.8 Outcome / Learning

Owns:

- actual observed result;
- expected-versus-actual comparison;
- learning candidate;
- proposed changes to belief/model/policy/heuristic;
- after-action evidence.

Learning cannot silently alter canonical truth or Intent.

---

# 4. Common contract envelope

All material interfaces must preserve the metadata needed for trust.

## Identity

```text
canonical_id
source_identity[]
aliases / historical_names
reconciliation_status
merge_split_lineage
```

## Time

```text
effective_time
source_time
recorded_time
discovered_time
valid_from / valid_to
truth_domain = current | historical | scenario
```

## Epistemic status

```text
kind = observation | claim | assessment | inference |
       canonical_state | assumption | prediction
explicit_or_inferred
confidence / calibration when meaningful
authority
supporting_evidence[]
contradicting_evidence[]
```

## Provenance

```text
source_reference
source_version
extraction_pipeline_version
model / function version if derived
ontology_version
promotion / correction history
```

## Security / authority

```text
classification
source_access_constraints
object / property / evidence restrictions
actor_security_context
delegated_authority
allowed_actions
approval_requirements
```

---

# 5. Contract C01 — Sensor acquisition

**Provider:** Evidence & Data Engineering / Platform Engineering  
**Consumer:** Raw Evidence Store

Must provide:

- source system identity;
- mailbox/site/library/folder context;
- stable source record identity where possible;
- source timestamps;
- acquired timestamp;
- source reference / retrievable URI or identifier;
- content hash;
- attachment/version relationships;
- source permission metadata where accessible;
- acquisition job/run identity;
- idempotency key.

Must not:

- assign canonical business identity;
- decide that source text is true;
- transform a source folder into an ontology domain;
- drop evidence solely because current extraction does not understand it.

Acceptance condition:

> Every normalized or extracted item can be traced back to the exact acquired source evidence.

---

# 6. Contract C02 — Raw Evidence -> normalized observations

**Provider:** Evidence & Data Engineering  
**Consumer:** Evidence Graph / extraction services

Normalization may produce:

- normalized message/document representation;
- party/source observations;
- clean text segments;
- attachment references;
- thread/document-family relationships;
- duplicate/copy indicators;
- source metadata;
- security labels.

Normalization must preserve raw evidence identity.

Acceptance condition:

> Normalization changes representation, not historical source meaning.

---

# 7. Contract C03 — Knowledge/Ontology -> Extraction Contract

**Provider:** Knowledge & Ontology Engineering  
**Consumer:** Evidence & Data Engineering

This contract defines **what is worth attempting to extract**, not how the extraction code works.

For each candidate concept:

```text
candidate_type
semantic_definition
required_fields
optional_fields
allowed_relationships
context_requirements
source_authority_notes
security_classification_rules
explicit_vs_inferred rules
examples
counterexamples
promotion_eligibility
```

The ontology team must provide negative guidance too.

Example:

```text
Observed word: "ServiceNow"
Do NOT assume: Opportunity
Possible interpretations:
- Technology / Product
- Capability
- Opportunity shorthand
- Project shorthand
- Support topic
Context evidence required before classification.
```

Acceptance condition:

> Extraction can evolve independently without inventing canonical semantics.

---

# 8. Contract C04 — Extraction -> Enterprise Evidence Graph

**Provider:** Evidence & Data Engineering / extraction models  
**Consumer:** Knowledge/Ontology Toolchain

Possible outputs:

- Observation;
- Claim;
- Candidate Entity;
- Candidate Relationship;
- Alias Observation;
- Candidate Context;
- Candidate Event;
- Decision Fragment;
- Candidate Action;
- Candidate Outcome;
- Candidate Obligation / Commitment;
- Document lineage candidate;
- security candidate.

Every output must retain:

- source evidence;
- extraction method/model;
- timestamp;
- confidence if generated probabilistically;
- explicit vs inferred status.

Rule:

> Extraction output is always non-authoritative unless a separate deterministic promotion rule explicitly says otherwise.

---

# 9. Contract C05 — Evidence Graph -> Reconciliation

**Provider:** Enterprise Evidence Graph  
**Consumer:** Ontology Toolchain

Reconciliation asks:

```text
same canonical object?
alias?
historical name?
parent/child?
organizational unit?
brand/legal entity?
product/opportunity ambiguity?
related but distinct?
changed over time?
new candidate?
unresolved?
```

Inputs may include:

- names;
- domains;
- identifiers;
- addresses;
- people;
- business context;
- opportunity/project/RFP IDs;
- document parties;
- chronology;
- graph neighborhood;
- external authoritative identifiers.

Output:

```text
resolution_proposal
candidate_matches[]
confidence / evidence
rationale_summary
required_review_level
```

No destructive deduplication.

---

# 10. Contract C06 — Reconciliation/Validation -> Canonical Promotion

**Provider:** Ontology Toolchain  
**Consumer:** Business Reality

Promotion input:

```text
candidate statement/entity/relation/event
supporting evidence
contradicting evidence
authority evaluation
identity/context resolution
temporal interpretation
security classification
confidence
promotion policy
review / approval if required
```

Promotion output:

```text
canonical_change
previous_state
new_state
effective_time
promotion_actor/process
source evidence
reason / policy
schema / ontology version
```

Promotion rules vary by fact type.

Examples:

- message sender/recipient/time may be deterministically observed;
- legal execution may require signed agreement evidence;
- payment-cleared state should use financial/bank authority;
- inferred relationship strength may remain an Assessment rather than canonical fact.

---

# 11. Contract C07 — Business Reality -> Capability Model

**Provider:** Business Reality  
**Consumer:** Capability Model

Capability Model must be derivable or traceable to:

- people and skills;
- roles / authority;
- current assignments;
- availability;
- capacity;
- financial resources;
- systems/assets;
- partner capabilities;
- contractual constraints;
- geographic/legal constraints.

Output is not merely a list of resources. It is a feasibility view.

Example:

```text
Capability: Respond to ServiceNow ITAM opportunity
Feasible: YES / PARTIAL / NO
Evidence:
- internal qualified resources
- partner capacity
- vehicle eligibility
- proposal capacity
Constraints:
- LBE cap
- deadline
- required certification
```

---

# 12. Contract C08 — Business Intent -> Executive Judgment

**Provider:** Business Intent  
**Consumer:** Executive Judgment

Must expose decision-relevant intent, such as:

```text
objective hierarchy
strategic priority
success metrics
time horizon
risk appetite
hard constraints
preference ordering
capital constraints
ethical / policy constraints
strategic assumptions
```

The Decision Engine must not reconstruct company strategy from random emails when governed Intent exists.

---

# 13. Contract C09 — External World Model -> Executive Judgment

**Provider:** External World Model  
**Consumer:** Executive Judgment

Each material external belief should expose:

```text
belief statement
scope
validity period
supporting evidence
contradicting evidence
confidence / uncertainty
governance status
last reviewed
materiality links to GenSigma
```

Raw news does not cross this contract as strategic truth.

---

# 14. Contract C10 — Decision Context Assembly

Before judgment can run, a `DecisionContext` is assembled from governed sources.

Candidate structure:

```text
DecisionContext
- decision_class
- trigger
- current business state
- relevant history
- Business Intent
- external-world beliefs
- capabilities
- evidence
- unknowns / uncertainty
- constraints
- actors / counterparties
- available actions
- authority context
- deadline / time horizon
```

This structure is provisional pending Research 001.

The Decision Engine should be able to request missing information rather than pretending completeness.

---

# 15. Contract C11 — Executive Judgment -> Recommendation

Minimum recommendation output:

```text
recommendation
alternatives_considered[]
expected_consequences[]
key_assumptions[]
uncertainties[]
relevant_constraints[]
risk_analysis
method(s)_used
supporting_context_refs
confidence / calibration if defensible
human_approval_required
recommended_action
```

The recommendation must be auditable enough to distinguish:

- rule-based conclusion;
- optimization result;
- probabilistic inference;
- LLM-generated qualitative reasoning;
- human override.

---

# 16. Contract C12 — Recommendation -> Decision / Approval

Decision records:

```text
selected_alternative
decision_maker
made_at
recommendation_ref
rationale
conditions
explicit_vs_inferred
```

Approval records:

```text
approver
authority_basis
approved_action / scope
limits / conditions
approved_at
expiry if relevant
```

Historical reconstruction may have unknown or inferred fields; these must remain visibly uncertain.

---

# 17. Contract C13 — Decision/Approval -> Typed Action

A material action requires:

```text
action_type
actor
authority
inputs
targets
preconditions
policies
required_approval
expected_effect
verification_rule
idempotency semantics
failure / compensation behavior
```

Example:

```text
SubmitProposal(
  opportunity_id,
  proposal_id,
  submitted_by,
  channel,
  submission_time
)
```

The action execution should not simply become:

```text
opportunity.status = submitted
```

The state transition is an effect of the governed action.

---

# 18. Contract C14 — Execution -> Verified Outcome

Execution response:

```text
execution_id
started_at
finished_at
success / failure / uncertain
external_system_receipts
observed_side_effects
verification_status
errors
compensation_status
```

A successful API call is not automatically a successful business outcome.

Example:

- API call `send proposal` succeeded;
- receipt/portal confirmation verifies submission;
- later customer acknowledgment strengthens state;
- award/loss is downstream outcome, not action success.

---

# 19. Contract C15 — Outcome -> Learning

Learning proposal should separate:

```text
observed outcome
expected outcome
deviation
possible causal explanation
confidence
sample size / evidence sufficiency
proposed belief update
proposed model/policy update
proposed Intent change if strategic
review authority
```

One outcome should not automatically rewrite strategy.

Learning update destinations may include:

- Business Reality;
- External World beliefs;
- capability estimates;
- decision model parameters;
- procedure/skill;
- policy proposal;
- Business Intent proposal.

Each destination has its own governance threshold.

---

# 20. Security contract across every layer

Security is not a single downstream service.

Every layer receives `SecurityContext` including at minimum:

```text
actor identity
actor type = human | service | agent
roles
business function
scopes
delegated authority
need-to-know context
```

A downstream layer must not widen access granted upstream.

Required architectural properties:

- restricted raw evidence remains restricted;
- derived facts may have a different classification than evidence;
- semantic/vector search must enforce effective permissions;
- agent retrieval uses agent identity and delegation;
- typed actions separately authorize read and execute rights;
- audit logs record material access/decision/action events where required.

---

# 21. Workstream handoff contracts

## Knowledge/Ontology -> Evidence/Data

Must provide:

- extraction semantics;
- object/link definitions;
- context rules;
- event/decision/action distinctions;
- security tagging rules;
- promotion requirements.

## Evidence/Data -> Knowledge/Ontology

Must provide:

- observed source reality;
- extraction precision/recall findings;
- ambiguous/unmodeled cases;
- duplicate/copy behavior;
- volume/scale metrics;
- examples that break the ontology.

## Knowledge/Ontology -> Platform

Must provide:

- canonical data shapes;
- cardinalities;
- query scenarios;
- temporal requirements;
- transaction/consistency requirements;
- security boundaries;
- search requirements;
- scale assumptions;
- migration/versioning requirements.

## Platform -> Knowledge/Ontology

Must provide:

- measured technology capabilities;
- benchmark results;
- operational trade-offs;
- constraints that require semantic discussion;
- ADR proposals.

## Executive Cognition -> Knowledge/Ontology

Must provide:

- decision-context data requirements;
- uncertainty representation requirements;
- scenario/alternative requirements;
- decision trace extensions;
- historical outcomes needed for learning.

## Knowledge/Ontology -> Executive Cognition

Must provide:

- governed state;
- provenance;
- confidence/epistemic status;
- historical timeline;
- available actions;
- Business Intent links;
- capability inputs.

---

# 22. Integration gates

## Gate G0 — Doctrine gate

Question:

> Does the proposal violate the Constitution or frozen architectural invariants?

If yes: stop or create explicit amendment proposal.

## Gate G1 — Semantic gate

Question:

> Is ownership of the concept clear, and does the same semantic fact have one canonical owner?

## Gate G2 — Evidence gate

Question:

> Can material state be traced to source, authority, time and interpretation history?

## Gate G3 — Security gate

Question:

> Can every relevant access/action path enforce the effective security context?

## Gate G4 — Correctability gate

Question:

> Can a wrong interpretation, merge, state or model decision be corrected without destroying history?

## Gate G5 — Workload gate

Question:

> Are performance/scale requirements expressed as concrete scenarios rather than adjectives?

## Gate G6 — Operational gate

Question:

> Can the expected team operate, observe, recover and evolve this component?

## Gate G7 — Decision gate

Question:

> Does the downstream consumer receive enough context, uncertainty and authority information to make an auditable decision?

## Gate G8 — Kinetic gate

Question:

> Does a material write happen through an authorized typed business action with a verifiable effect?

---

# 23. Current architectural boundaries: DECIDED / TENTATIVE / OPEN

## DECIDED

- Palantir-style operational ontology is primary doctrine.
- Business Intent is distinct from Business Reality.
- Business Reality is distinct from material External World Model.
- Sources are sensors/evidence, not ontology branches.
- Evidence Graph is non-authoritative.
- Identity reconciliation occurs before new canonical identity creation.
- Time/provenance/security are first-class.
- Decision/Event/Action/Outcome are distinct.
- Material writes ultimately use typed governed actions.
- AI outputs are non-authoritative by default.
- Azure is pragmatic initial hosting direction, not semantic doctrine.
- Physical persistence remains unresolved until workload evaluation.

## TENTATIVE

- Capability Model as a derived decision-facing view over Business Reality rather than a wholly independent canonical store.
- DecisionContext as a stable cross-layer object/interface.
- External strategic beliefs update on slower governance cadence than raw external observations.

## OPEN

- primary persistence architecture;
- graph projection necessity;
- vector/search architecture;
- exact confidence representations;
- exact canonical promotion policies by claim class;
- decision engine computational architecture;
- degree of autonomy;
- whether some decision-trace groupings merit persistent objects;
- exact data-contract implementation mechanism.

---

# 24. Architecture review rule

A workstream proposal is considered **local** if it does not change a shared contract, invariant, security posture, portability assumption, ontology meaning, or hard-to-reverse technology commitment.

A proposal is **architectural** if it changes any of those.

Architectural proposals return to the Chief Architect with:

```text
Decision question
Business driver
Current contract/invariant affected
Options considered
Quality scenarios
Evidence / benchmark
Trade-offs
Recommendation
Confidence
Reversibility
Files/ADRs affected
```

The Chief Architect reviews using `05-CHIEF-ARCHITECT-DECISION-METHOD-v0.1.md`.
