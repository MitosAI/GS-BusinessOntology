# GenSigma AI-Native Operating System — System Acceptance & Architecture Fitness

**Version:** v0.1  
**Status:** Chief Architect acceptance framework  
**Owner:** Chief Architect  
**Purpose:** Define how we know GenSigma OS is becoming a trustworthy operating brain rather than a collection of impressive demos.

---

# 1. Acceptance philosophy

The architecture is not accepted because:

- a diagram looks coherent;
- an LLM gives a persuasive answer;
- a graph visualization looks rich;
- an ingestion pipeline processed a large corpus;
- an agent completed a workflow;
- a database benchmark is fast.

The system is accepted when it preserves the invariants required for trusted executive and operational use under realistic conditions.

Acceptance has two levels:

1. **Architectural fitness** — does the implementation continue to satisfy system invariants and quality scenarios?
2. **Business cognition fitness** — can the system correctly understand, reason about, and act on real GenSigma situations with appropriate authority and uncertainty?

---

# 2. North-star end-to-end test

Given a real business situation, the mature OS should eventually be able to:

```text
1. OBSERVE
   detect relevant evidence / trigger

2. UNDERSTAND REALITY
   identify objects, relationships, context, history and uncertainty

3. ORIENT TO INTENT
   retrieve goals, priorities, constraints, risk appetite and external beliefs

4. ASSESS CAPABILITY
   understand what GenSigma can actually do now

5. JUDGE
   generate and evaluate credible alternatives using appropriate methods

6. DECIDE / SEEK APPROVAL
   expose rationale, uncertainty and authority requirements

7. ACT
   execute only an authorized typed action

8. VERIFY
   confirm whether the intended state change actually occurred

9. MEASURE OUTCOME
   distinguish action success from business outcome

10. LEARN
    propose evidence-backed updates without uncontrolled drift
```

Each step must remain auditable.

---

# 3. Architecture fitness dimensions

## F1 — Semantic correctness

Questions:

- Are canonical objects business-native rather than source-schema replicas?
- Is one real identity represented canonically despite source aliases?
- Are contextual roles distinct from enduring identity?
- Are Event, Decision, Action and Outcome distinct?
- Are external beliefs distinct from internal state and raw observations?

Failure examples:

- `QuickBooksCustomer` becomes an ontology object separate from `Organization`;
- every email reference creates a new Person;
- a recommendation is stored as a Decision;
- API success is recorded as business Outcome.

## F2 — Evidence integrity

Questions:

- Can every material belief/state be traced to evidence or authorized manual origin?
- Are contradictions visible?
- Is model-generated interpretation marked?
- Are source observations preserved even when interpretation changes?

## F3 — Temporal integrity

Questions:

- Can the system answer current state?
- Can it answer historical state?
- Can it distinguish when an event occurred from when the OS learned about it?
- Can a correction preserve earlier recorded belief/history?

## F4 — Correctability

Questions:

- Can identity merges be reversed?
- Can relationships be reclassified?
- Can false inference be rejected without deleting evidence?
- Can ontology evolution migrate prior data safely?

The system must prefer revisable interpretation over false certainty.

## F5 — Security / authority

Questions:

- Does every access occur under an explicit security context?
- Can restricted evidence remain hidden while permitted derived state is exposed?
- Do agents have scoped authority?
- Do actions fail closed without authority/approval?
- Does semantic/vector retrieval preserve permissions?

## F6 — Kinetic governance

Questions:

- Are material business writes typed actions?
- Are preconditions and policies evaluated?
- Is actor/approval context preserved?
- Is the expected effect explicit?
- Is actual effect verified?
- Can failed execution be compensated/recovered where appropriate?

## F7 — Reliability / replay

Questions:

- Is ingestion idempotent?
- Can jobs restart safely?
- Can raw evidence be replayed through newer extraction versions?
- Can canonical state be recovered?
- Are pipeline failures observable?

## F8 — Performance / scale

Questions:

- Are latency/throughput targets tied to real scenarios?
- Does graph-like traversal meet the target?
- Does security filtering remain performant?
- Does backfill fit operational time/cost constraints?
- Can scale grow without redesigning the semantic model?

## F9 — Evolvability

Questions:

- Can new domains reuse canonical identity and interfaces?
- Can source connectors change independently?
- Can storage components be replaced without changing ontology semantics?
- Can Decision Engine methods evolve without rewriting Business Reality?

## F10 — Operability / simplicity

Questions:

- Can the expected small team understand and operate the system?
- Are failures diagnosable?
- Is observability built in?
- Are unnecessary distributed components avoided?
- Is operational complexity justified by measured requirements?

---

# 4. Executable fitness-function candidates

The following should become automated tests/checks where practical.

## FF-001 Provenance completeness

For every promoted canonical claim/state change:

```text
assert provenance exists
OR
assert authorized_manual_origin exists
```

Target: 100% for material canonical changes.

## FF-002 No direct connector-to-canonical write

Static/runtime architecture rule:

```text
connector -> raw/normalized evidence only
connector -X-> canonical state
```

## FF-003 Idempotent ingestion

Replay the same bounded source dataset twice.

Expected:

- no duplicate raw source identity;
- no duplicate normalized observation caused solely by replay;
- no duplicate canonical promotion effect.

## FF-004 Reversible identity merge

Fixture:

- create two canonical entities;
- merge based on candidate evidence;
- later introduce contradictory evidence;
- split.

Expected:

- original evidence remains;
- source mappings remain traceable;
- historical merge action remains auditable;
- corrected identity graph is coherent.

## FF-005 Historical as-of query

Fixture with multiple time-qualified state transitions.

Expected:

```text
get_state(entity, as_of=T1) == expected_T1
get_state(entity, as_of=T2) == expected_T2
```

## FF-006 Security non-leakage

Given:

- HR restricted evidence;
- manager-visible derived fact;
- normal user identity.

Expected:

- manager receives permitted fact;
- normal user receives only permitted state;
- neither receives restricted evidence unless authorized;
- search does not leak restricted snippets or embeddings.

## FF-007 Explicit vs inferred decision trace

Historical reconstruction fixture.

Expected:

- explicit Decision is marked explicit;
- inferred rationale remains inferred;
- missing alternatives remain unknown rather than fabricated;
- supporting evidence is linked.

## FF-008 Typed action enforcement

Attempt direct material state mutation through public business API.

Expected: rejected unless routed through approved typed-action contract.

## FF-009 Action verification

Run a low-risk action.

Expected audit chain:

```text
Decision / trigger
 -> authorization
 -> action execution
 -> external receipt / verification
 -> Event
 -> updated Business Reality
```

## FF-010 Projection non-authority

Delete/rebuild search/vector/graph projection where architecture uses one.

Expected:

- canonical Business Reality remains intact;
- projection can be recreated from canonical/evidence sources;
- projection cannot silently become source of truth.

---

# 5. MVP 001 acceptance scenarios

The first Business Reality MVP should pass the following scenario family.

## Scenario A — Alias and identity

Evidence contains several names for one organization plus one similar but distinct organization.

Pass if:

- system proposes correct alias resolution;
- distinct organization remains distinct;
- evidence/rationale for both is inspectable;
- uncertain case can remain unresolved.

## Scenario B — Context ambiguity

Email subject uses product/capability shorthand.

Pass if:

- system does not automatically make it an Opportunity;
- supporting context is discovered;
- business context can be corrected.

## Scenario C — Contradictory claims

Two emails and a formal artifact disagree.

Pass if:

- all evidence remains;
- authority is evaluated by claim type;
- canonical state uses defined promotion logic;
- contradiction remains inspectable.

## Scenario D — Historical reconstruction

Current state differs from older state.

Pass if:

- present state is correct;
- historical state is reconstructable;
- current role/status is not projected backward.

## Scenario E — Decision reconstruction

Evidence fragments are spread across email and document sources.

Pass if:

- decision path can be assembled;
- explicit/inferred/unknown distinctions survive;
- Decision is separate from Action;
- outcome evidence is separate.

## Scenario F — Restricted evidence

A sensitive message supports a broadly useful operational fact.

Pass if:

- sensitive evidence remains protected;
- derived fact follows its own classification policy;
- unauthorized retrieval/search does not leak source content.

---

# 6. Decision-engine acceptance framework — reserved for Research 001 integration

A later computational decision prototype should be evaluated on more than agreement with the founder.

Candidate dimensions to be finalized by Executive Cognition Research:

- state/evidence completeness;
- uncertainty honesty;
- alternative quality;
- correct use of deterministic constraints;
- appropriate use of probability;
- correct optimization formulation where applicable;
- strategic counterparty reasoning where applicable;
- rationale traceability;
- calibration;
- sensitivity to changed assumptions;
- robustness under missing/conflicting evidence;
- human override and authority behavior;
- observed decision outcome over repeated cases.

No `executive intelligence` claim should be accepted from anecdotal single-case success.

---

# 7. Architecture health dashboard — future

Eventually maintain a compact architectural health view:

```text
Semantic integrity      PASS / WARN / FAIL
Provenance completeness %
Unresolved identity rate
Incorrect merge rate
Extraction review error rate
Historical query tests
Security leakage tests
Action audit completeness
Ingestion replay health
P95 key query latency
Source lag
Recovery test status
Architecture fitness CI status
```

The exact metrics will evolve, but architecture must become observable rather than dependent on diagram review.

---

# 8. Review cadence

## Per pull request / build

Run automated fitness functions relevant to the changed component.

## Per architecture milestone

Run scenario-based architecture review using the Chief Architect Decision Method.

## Before a new domain

Pressure-test whether the domain fits existing canonical identities/interfaces before adding new abstractions.

## Before increased autonomy

Re-run security, authority, action-verification and rollback tests.

## Periodic strategic review

Review whether Business Intent or External World assumptions materially changed. Do not modify them merely because operational data changed.

---

# 9. Stop conditions

A build does not advance to the next autonomy/production level if any of these are unresolved:

- source lineage is lost;
- restricted data can leak through derived/search surfaces;
- identity corrections destroy history;
- LLM inference silently becomes canonical state;
- canonical storage ownership is ambiguous;
- material state changes bypass typed actions;
- historical state cannot be reconstructed where the domain requires it;
- architecture cannot be reasonably operated/recovered;
- benchmark evidence contradicts the accepted architecture assumptions.

---

# 10. Definition of architectural success

GenSigma OS architecture succeeds when it can evolve from one thin slice to many business domains without losing:

- one coherent semantic model;
- trust in evidence and provenance;
- explicit uncertainty;
- historical correctness;
- security and delegated authority;
- governed action;
- correctability;
- operational simplicity appropriate to the team;
- measurable decision quality;
- the ability to replace physical technologies without rewriting what the business means.

That is the standard against which every impressive demo must eventually be judged.
