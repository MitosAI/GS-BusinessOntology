# GenSigma AI-Native Operating System — Chief Architect Decision Method

**Version:** v0.1  
**Status:** Active working method  
**Owner:** Chief Architect  
**Purpose:** Define how architecturally significant decisions are made, challenged, validated, documented, and revisited across GenSigma OS.

---

# 1. Why this document exists

GenSigma OS is too important and too novel to be designed by intuition, vendor fashion, or accumulated best-practice checklists alone.

The Chief Architect therefore uses a disciplined architecture decision process grounded in established software-architecture practice, but adapted to the specific properties of this system:

- ontology-centered operational semantics;
- evidence-before-truth;
- deterministic core with probabilistic reasoning at uncertain edges;
- strong security and authority controls;
- time-native and provenance-native state;
- continuous reconciliation and correction;
- typed kinetic actions;
- eventual executive judgment under uncertainty;
- small-team operability;
- long-term evolvability.

Industry best practices are **inputs to the decision process, not substitutes for architectural judgment**.

The central rule is:

> **Best practice narrows the search space. GenSigma's business drivers, invariants, workload evidence, and trade-offs decide the architecture.**

---

# 2. External methods this process draws from

This method synthesizes several established approaches.

## 2.1 CMU SEI — Architecture Tradeoff Analysis Method (ATAM)

ATAM evaluates architectures against competing quality attributes such as security, performance, availability, and modifiability, and explicitly identifies risks, sensitivity points, and trade-off points.

The most important lesson for GenSigma OS is that architecture quality is not a universal score. It is fitness against **business drivers expressed as prioritized quality-attribute scenarios**.

Applied here:

- start from business drivers;
- define quality attributes in concrete scenarios;
- examine how each architecture option satisfies those scenarios;
- identify trade-offs and sensitivity points;
- do not optimize every quality attribute equally.

## 2.2 Azure / AWS Well-Architected guidance

Cloud architecture should be evaluated across reliability, security, performance efficiency, operational excellence, and cost, with explicit acknowledgment that improving one dimension can worsen another.

Applied here:

- every physical architecture must be evaluated across operational qualities;
- workload-specific priorities control the weighting;
- business requirements come before service selection;
- managed services are preferred when they reduce operating burden without compromising semantics or portability requirements.

## 2.3 Architecture Decision Records (ADR)

Architecturally significant decisions must preserve context, alternatives, decision, consequences, status, and change history. Accepted decisions are not silently rewritten; a later decision supersedes the earlier one.

Applied here:

- GitHub is the durable decision log;
- accepted ADRs are immutable history;
- new evidence produces a new ADR, not revisionist editing;
- the rationale must survive the current team and current AI session.

## 2.4 Evolutionary architecture / fitness functions

Architecture should not only be reviewed at design time. Important architectural properties should be continuously testable where possible.

Applied here:

- architecture principles become executable tests or measurable checks when feasible;
- e.g. every canonical fact has provenance;
- unauthorized actors cannot retrieve restricted evidence;
- ingestion replay is idempotent;
- canonical merges are reversible;
- an accepted typed action leaves an auditable state transition.

## 2.5 Zero Trust security principles

Security decisions should not depend on implicit trust arising from network location or organizational affiliation. Identity, policy, and authorization must be explicit.

Applied here:

- users, services, and AI agents are explicit governed identities;
- authorization is enforced at the relevant object/evidence/action boundary;
- internal network location does not equal trust;
- evidence sensitivity may differ from the visibility of the derived business fact.

---

# 3. The Chief Architect's six decision lenses

The program deliberately avoids maintaining 20 supposedly equal design principles. For architecturally significant decisions, six lenses are sufficient.

## Lens 1 — Correctness & Trust

Can the system represent, preserve, and operate on business reality correctly enough for the decision/action risk involved?

Includes:

- semantic correctness;
- identity integrity;
- temporal correctness;
- provenance;
- authority;
- auditability;
- security;
- deterministic enforcement where possible.

For GenSigma OS, this lens frequently dominates because a fast wrong answer or an untraceable action is worse than a slower correct one.

## Lens 2 — Evolvability & Correctability

Can we change our minds safely?

Includes:

- schema evolution;
- ontology extension;
- versioning;
- reversible merge/split/correction;
- API evolution;
- portability;
- replaceability of infrastructure;
- avoidance of irreversible semantic coupling.

This is critical because our ontology, executive cognition architecture, and source estate will evolve materially.

## Lens 3 — Operational Robustness

Can a small team run the system safely and recover when components fail?

Includes:

- reliability;
- recoverability;
- observability;
- failure isolation;
- idempotency;
- deployment safety;
- backup/restore;
- operational simplicity.

## Lens 4 — Performance & Scale

Can the architecture meet actual workload requirements as data, relationships, users, and decision workloads grow?

Includes:

- latency;
- throughput;
- multi-hop traversal;
- indexing/search behavior;
- ingestion scale;
- storage growth;
- concurrency;
- ability to partition/scale where required.

Performance is scenario-based, not prestige-based. A 50 ms requirement is not invented unless the business needs it.

## Lens 5 — Simplicity & Maintainability

Is this the simplest architecture that satisfies the critical requirements without closing important future paths?

Includes:

- conceptual simplicity;
- number of moving parts;
- cognitive load;
- skill availability;
- testability;
- debugging difficulty;
- integration surface.

Complexity requires evidence. Future hypothetical scale is not sufficient justification.

## Lens 6 — Economics & Delivery Velocity

Does the architecture produce sufficient business value for cost and time invested?

Includes:

- cloud and licensing cost;
- engineering effort;
- operating effort;
- vendor dependence;
- time to first useful slice;
- cost of migration/reversal;
- opportunity cost.

---

# 4. There is no universal weighting

The six lenses do **not** receive a fixed score for all decisions.

The decision context determines priority.

Examples:

### Canonical ontology design

Dominant lenses:

1. Correctness & Trust
2. Evolvability & Correctability
3. Simplicity & Maintainability

Performance is relevant but subordinate unless a concrete ontology operation proves otherwise.

### Raw evidence storage

Dominant lenses:

1. Correctness & Trust
2. Operational Robustness
3. Economics & Delivery Velocity

### Query/persistence engine

Dominant lenses:

1. Correctness & Trust
2. Performance & Scale
3. Evolvability & Correctability
4. Operational Robustness

### Executive cognition engine

Dominant lenses:

1. Correctness & Trust
2. Evolvability & Correctability
3. Simplicity & Maintainability
4. Economics & Delivery Velocity

For high-consequence decisions, auditability and uncertainty honesty outweigh apparent intelligence.

---

# 5. Architecture Decision Protocol

Every architecturally significant decision follows the same sequence.

```text
BUSINESS DRIVER / PROBLEM
          |
          v
INVARIANTS + CONSTRAINTS
          |
          v
QUALITY-ATTRIBUTE SCENARIOS
          |
          v
CANDIDATE OPTIONS
          |
          v
TRADE-OFF / RISK ANALYSIS
          |
          v
SPIKE / BENCHMARK IF NEEDED
          |
          v
DECISION + CONFIDENCE
          |
          v
ADR
          |
          v
IMPLEMENTATION
          |
          v
FITNESS TESTS / TELEMETRY
          |
          v
REVIEW TRIGGERS
```

---

# 6. Step 1 — State the architectural decision precisely

Do not begin with a technology.

Bad decision statement:

> Should we use Neo4j?

Better:

> What physical persistence architecture best supports canonical business state, temporal history, multi-hop relationship traversal, transactional promotion, evidence lineage, permission-aware queries, and small-team operations for the World Model MVP?

Bad:

> Should we use Kafka?

Better:

> Do our ingestion and downstream processing requirements require durable asynchronous event transport with independently scalable consumers, replay, and ordering guarantees that cannot be met sufficiently by a simpler job/queue model?

The problem statement must describe the need before the candidate solution.

---

# 7. Step 2 — Establish business drivers and invariants

Every architecture decision must trace to a business or constitutional driver.

GenSigma-wide invariants currently include:

- sources are sensors, not canonical ontology branches;
- evidence is not automatically truth;
- canonical interpretation is revisable while source observation is preserved;
- canonical Person/Organization identity is distinct from contextual role;
- time is first-class;
- Event, Decision, Action, and Outcome are semantically distinct;
- material state changes ultimately occur through typed governed actions;
- security is end-to-end and agents are governed actors;
- operational state can update quickly, while strategic worldview changes deliberately;
- physical technology must not redefine business semantics;
- ambiguous evidence may remain unresolved rather than being forced into false certainty.

Any candidate architecture that violates a constitutional invariant is rejected unless the Constitution itself is deliberately amended.

---

# 8. Step 3 — Convert vague qualities into concrete scenarios

Words like scalable, secure, robust, flexible, and fast are not requirements until expressed as scenarios.

Use the structure:

```text
SOURCE / STIMULUS
      -> ENVIRONMENT
      -> SYSTEM ELEMENT
      -> EXPECTED RESPONSE
      -> MEASURE
```

Examples for GenSigma OS:

### Identity correctness scenario

Given ten years of evidence containing `SFO`, `SF Airport`, and legal party names, when a new observation arrives, the system must attempt reconciliation before creating a new canonical Organization and must preserve evidence supporting the reconciliation decision.

### Correctability scenario

If a human later determines that two organizations were incorrectly merged, the system must split the canonical identities without deleting original source observations and must preserve the history of both the merge and correction.

### Security scenario

When a manager queries employee availability, the system may return the permitted operational fact but must not expose HR-restricted medical evidence unless the security context authorizes it.

### Ingestion reliability scenario

If an Outlook ingestion job fails halfway and retries, the second run must not create duplicate raw evidence or duplicate normalized observations.

### Temporal scenario

Given a contract state today and evidence from 2024, the system must answer both `what is true now?` and `what did we believe/know as of 2024-09-01?` without projecting present state backward.

### Traversal performance scenario

For the MVP dataset, `Customer -> Opportunity -> Partner -> Person -> Agreement` must return within the agreed interactive latency target under the expected concurrent load while enforcing the caller's permissions.

Only after scenarios like these exist do storage or platform comparisons become meaningful.

---

# 9. Step 4 — Generate genuinely viable options

Architecture evaluation must compare real alternatives, not one preferred option against straw men.

For each decision:

- include the simplest viable option;
- include the leading technically strong option;
- include a deliberately different architecture where it illuminates a trade-off;
- include `defer / do nothing yet` when that is genuinely viable.

Example persistence decision candidates might be:

- relational-first with graph-like relational traversal;
- graph-native canonical store;
- relational canonical store + graph projection;
- multi-model/document approach;
- defer graph projection until observed query pain justifies it.

No vendor is selected merely because its product vocabulary resembles our architecture vocabulary.

---

# 10. Step 5 — Analyze trade-offs, sensitivities, and risks

For every candidate, evaluate:

- which quality scenarios it satisfies strongly;
- which it weakens;
- what assumptions it depends on;
- where small changes in workload or requirements materially alter the result;
- operational failure modes;
- migration/reversal difficulty;
- security consequences;
- unknowns that require experiments.

A **sensitivity point** is something like:

> This architecture remains attractive only if typical graph traversals remain 1–4 hops and interactive latency remains acceptable.

A **trade-off point** is something like:

> Duplicating canonical relationship data into a graph projection improves traversal flexibility but increases consistency and operational complexity.

A **risk** is something like:

> We do not yet know whether row-/object-level security enforcement remains correct and performant for semantic search plus multi-hop traversal.

Risks become experiments, constraints, or explicit acceptance—not hand-waving.

---

# 11. Step 6 — Prototype or benchmark where uncertainty matters

Do not benchmark everything.

Benchmark when a decision is both:

- materially consequential; and
- uncertain enough that documentation/theory does not settle it.

Examples:

- relational versus graph traversal on realistic ontology paths;
- permission-aware semantic retrieval latency;
- entity-reconciliation candidate generation at historical-mailbox scale;
- temporal-state query models;
- cost and operational complexity of competing Azure database choices.

Benchmark with **representative GenSigma data shapes and queries**, not vendor demo workloads.

The test dataset should include ambiguity, long history, duplicates, restricted evidence, temporal corrections, and relationship-rich contexts.

---

# 12. Step 7 — Decide with explicit confidence and conditions

A decision records:

- selected option;
- why it wins for the prioritized scenarios;
- major trade-offs accepted;
- major risks remaining;
- confidence level;
- what would invalidate the decision;
- whether it is easy or expensive to reverse.

Confidence is useful because architecture decisions are made with incomplete information.

Example:

```text
Decision confidence: MEDIUM-HIGH
Reason: benchmark validates current workload; long-term relationship scale remains uncertain.
Revisit if: traversal P95 exceeds target, graph depth materially grows, or cross-object policy evaluation becomes a bottleneck.
```

---

# 13. Step 8 — Capture the decision as an ADR

An ADR should contain at least:

```text
ADR-XXX — Title
Status
Date
Owner

Context / decision question
Business drivers
Constitutional constraints
Quality-attribute scenarios
Options considered
Evidence / benchmarks
Decision
Consequences
Risks
Confidence
Reversibility
Review triggers
Supersedes / superseded by
```

Accepted ADRs are historical facts. If circumstances change, create a new ADR that supersedes the old one.

---

# 14. Step 9 — Convert architecture into fitness functions

Where feasible, architecture rules should become automatically verifiable.

Potential GenSigma fitness functions:

## Evidence integrity

- every promoted canonical claim has provenance or an explicit authorized manual-origin record;
- no raw source record is mutated by interpretation processing;
- repeated ingestion is idempotent.

## Identity

- no canonical entity creation occurs without reconciliation-state metadata;
- merge/split history remains reversible.

## Security

- restricted evidence is denied under unauthorized security contexts;
- agent actions fail closed if delegated authority is absent;
- source permissions are not widened accidentally by indexing/search.

## Temporal integrity

- historical query tests return the expected `as-of` state;
- state correction does not erase prior belief/record history.

## Kinetic governance

- material state-changing API calls require a typed action or explicitly documented infrastructure exception;
- each action execution records actor, authority, inputs, decision/approval context, effect, and verification result.

## Architecture boundaries

- connector code cannot directly write canonical state;
- search/vector representations are projections, not canonical truth stores;
- cloud-specific resource identifiers do not leak into canonical ontology semantics.

These become tests, schema constraints, CI checks, policy checks, telemetry alerts, or review checks depending on the property.

---

# 15. Step 10 — Revisit decisions only on explicit triggers

The architecture should neither fossilize nor thrash.

An accepted decision is revisited when one of the following occurs:

- a benchmark/fitness function fails materially;
- workload scale crosses a documented threshold;
- security/compliance requirements change;
- a major business driver changes;
- a foundational assumption proves false;
- operating cost materially exceeds expectation;
- implementation complexity is materially higher than modeled;
- a new source/domain exposes an ontology incompatibility;
- Research 001 changes requirements of the Decision Engine;
- vendor/platform lifecycle risk changes significantly.

New technology existing is **not by itself** a revisit trigger.

---

# 16. Decision classes and required rigor

Not every choice deserves ATAM-level analysis.

## Class A — Constitutional / structural

Examples:

- ontology governing doctrine;
- canonical identity model;
- truth/evidence separation;
- action/security semantics;
- major architecture boundaries.

Required rigor:

- deep analysis;
- Chief Architect approval;
- Constitution/spec/ADR change;
- explicit cross-workstream review.

## Class B — Platform / hard-to-reverse

Examples:

- primary operational database;
- major eventing architecture;
- identity/security architecture;
- long-term persistence model;
- execution runtime that creates strong coupling.

Required rigor:

- quality scenarios;
- alternatives;
- benchmark/spike where uncertainty is material;
- ADR;
- Chief Architect review.

## Class C — Component / reversible

Examples:

- library choice;
- implementation language inside a bounded service;
- local caching implementation;
- observability library.

Required rigor:

- local engineering decision unless it violates a shared invariant;
- short ADR only when cross-team impact or lock-in warrants it.

## Class D — Tactical

Examples:

- naming of a private helper;
- small refactor;
- local test layout.

Owned by engineering. Do not burden architecture governance with these.

---

# 17. How the Chief Architect uses research and expert recommendations

Research is separated into four evidence classes.

## Level 1 — Foundational / authoritative

Examples:

- standards;
- canonical academic methods;
- cloud-vendor architectural guidance for their own platforms;
- primary technical documentation;
- recognized security standards.

Used for:

- established constraints;
- known failure modes;
- terminology;
- mature operating practices.

## Level 2 — Strong industry practice

Examples:

- engineering publications from mature organizations;
- architecture books/frameworks with broad adoption;
- serious practitioner case studies;
- well-supported open-source patterns.

Used for:

- candidate patterns;
- implementation lessons;
- operational trade-offs.

## Level 3 — Emerging research/practice

Examples:

- recent papers;
- early AI architecture methods;
- vendor innovations;
- new ontology/agent approaches.

Used for:

- hypotheses;
- experiments;
- future options.

Not promoted to architecture merely because it is novel.

## Level 4 — Opinion / anecdote

Examples:

- blogs;
- newsletters;
- social media;
- conference opinions without evidence.

Useful for discovering questions, not settling decisions.

---

# 18. GenSigma-specific anti-patterns

Reject or challenge architecture decisions that exhibit these patterns.

## Technology-first architecture

`We need a graph, therefore use a graph database.`

Wrong direction. Define graph workload first.

## Semantic duplication

Separate truths in CRM projection, graph store, search index, and agent memory with no canonical ownership.

## False future-proofing

Adding multiple distributed systems today solely because the full OS may someday be huge.

## AI exceptionalism

Allowing an LLM path to bypass policy, provenance, deterministic validation, or security because it is `intelligent`.

## Source-schema gravity

Letting Outlook, SharePoint, QuickBooks, or another application dictate business ontology semantics.

## Security by wrapper

Attempting to add authorization only at the application/UI layer after data architecture is fixed.

## Irreversible inference

Converting probabilistic entity resolution or historical decision reconstruction into permanent truth with no correction path.

## Architectural thrashing

Reopening settled decisions because a new tool is fashionable rather than because documented assumptions changed.

## Architecture astronautics

Adding abstractions with no current decision, workload, correctness, or evolvability benefit.

---

# 19. Chief Architect decision scorecard template

This is a discussion aid, not a mechanical decision maker.

```text
DECISION:
BUSINESS DRIVER:
ARCHITECTURAL CLASS: A / B / C / D

NON-NEGOTIABLE INVARIANTS:
- ...

PRIORITIZED QUALITY SCENARIOS:
1. ...
2. ...
3. ...

OPTIONS:
A. ...
B. ...
C. ...

LENS REVIEW:
                         A       B       C
Correctness & Trust      ---     ---     ---
Evolvability             ---     ---     ---
Operational Robustness   ---     ---     ---
Performance & Scale      ---     ---     ---
Simplicity               ---     ---     ---
Economics / Velocity     ---     ---     ---

SENSITIVITY POINTS:
TRADE-OFF POINTS:
RISKS / UNKNOWN UNKNOWNS:
EXPERIMENTS REQUIRED:

DECISION:
CONFIDENCE:
REVERSIBILITY:
REVIEW TRIGGERS:
ADR:
```

Scores are never allowed to hide a disqualifying architectural violation. A candidate that violates a constitutional invariant is not rescued by a high aggregate score.

---

# 20. Immediate application to current GenSigma OS decisions

The method should now be applied to the following live decisions in order.

## D1 — Canonical top-level semantic boundaries

Business Intent vs Business Reality vs External World Model vs Capability Model vs Executive Judgment.

Status: conceptually strong; requires contract freeze and terminology reconciliation against older `World Model` documents.

## D2 — Build Spec 001 boundary

Decide the smallest end-to-end slice that exercises the most critical architecture properties without overfitting to an arbitrary email episode.

## D3 — Canonical data/evidence model required by Build Spec 001

Must be specified before final physical persistence selection.

## D4 — Physical persistence architecture

Relational/graph/hybrid/search/object-store responsibilities.

Requires workload scenarios and benchmark data.

## D5 — Security enforcement architecture

Must preserve object/evidence/action security and agent delegated authority end-to-end.

## D6 — Outlook + SharePoint acquisition architecture

Must preserve provenance, source identity, replay/idempotency, lineage, and permissions.

## D7 — Executive Cognition architecture

Deferred to Research 001 findings, then evaluated using this same decision method.

---

# 21. Reference sources

- CMU Software Engineering Institute — Architecture Tradeoff Analysis Method (ATAM): https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/
- CMU SEI — ATAM: Method for Architecture Evaluation: https://www.sei.cmu.edu/library/atam-method-for-architecture-evaluation/
- Microsoft Azure Well-Architected Framework: https://learn.microsoft.com/en-us/azure/well-architected/
- Microsoft Azure Architecture Center — Design Principles: https://learn.microsoft.com/en-us/azure/architecture/guide/design-principles/
- Microsoft — Maintain an Architecture Decision Record: https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record
- AWS Prescriptive Guidance — Architectural Decision Records: https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/
- NIST SP 800-207A — Zero Trust Architecture Model: https://csrc.nist.gov/pubs/sp/800/207/a/final
- Martin Fowler / Thoughtworks — architectural fitness functions: https://martinfowler.com/articles/fitness-functions-data-products.html

---

# 22. Final governing rule

The Chief Architect does not ask:

> What architecture is considered best practice?

The Chief Architect asks:

> Given GenSigma's business objective, constitutional invariants, concrete quality scenarios, realistic workload, security requirements, operational capacity, and current uncertainty, which architecture has the best justified trade-off profile—and what evidence would make us change our mind?

That is the architecture decision standard for GenSigma OS.
