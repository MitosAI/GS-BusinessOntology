# Build Spec 001 — Business Reality MVP Skeleton

**Version:** v0.1  
**Status:** KOE first-session draft  
**Owner:** Knowledge & Ontology Engineering (KOE-001)  
**Implementation status:** Not approved for build until Chief Architect review of the final spec  
**Physical storage:** Deliberately unspecified

---

## 1. Objective

Prove that GenSigma can construct a trustworthy, evidence-backed, temporally correct, security-aware Business Reality slice from Outlook and SharePoint without allowing source schemas or AI extraction to become canonical truth.

The slice must be narrow enough to implement quickly and rich enough to pressure-test:

- canonical identity and aliases;
- business context resolution;
- source provenance and evidence lineage;
- artifact/version reconciliation;
- temporal state and event history;
- relationship scope;
- decision-fragment reconstruction;
- Event / Decision / Action / Outcome distinctions;
- canonical promotion;
- security-aware retrieval;
- query requirements that can drive a later physical architecture ADR.

---

## 2. Proposed pilot

**Primary recommended episode:** SFO ServiceNow / CRI Advantage pursuit.

Rationale is documented in `05-PILOT-EPISODE-SELECTION-v0.1.md`.

The spec must remain reusable for the comparison episodes and must not encode SFO- or CRI-specific ontology classes.

---

## 3. System boundary

```text
OUTLOOK / EXCHANGE            SHAREPOINT
       |                           |
       +-------------+-------------+
                     |
                     v
               RAW EVIDENCE
                     |
                     v
           NORMALIZED EVIDENCE
                     |
                     v
       OBSERVATIONS / CLAIMS / CANDIDATES
                     |
                     v
           ENTERPRISE EVIDENCE GRAPH
                     |
                     v
      IDENTITY + CONTEXT + ARTIFACT RESOLUTION
                     |
                     v
        PROMOTION / REVIEW / GOVERNANCE
                     |
                     v
          CANONICAL BUSINESS REALITY
                     |
                     v
              QUERY / CONTEXT API
```

### Included

- one bounded Outlook corpus containing the selected episode and required context expansion;
- related SharePoint artifacts and versions;
- evidence extraction and lineage;
- candidate identities, aliases, contexts, relationships, events, claims, decision fragments, actions, and outcome signals;
- human-reviewable reconciliation and promotion states;
- canonical read model and proposed-write semantics;
- query benchmark suite.

### Excluded

- autonomous high-risk actions;
- primary database selection;
- universal enterprise ontology completion;
- broad external-world sensing;
- finance-system truth beyond evidence present in the selected episode;
- full Business Intent encoding;
- production Decision Engine implementation.

---

## 4. Core business questions

The MVP must answer, with evidence and epistemic status visible:

1. What canonical customer organization and organizational unit does this pursuit concern?
2. What canonical Opportunity does shorthand such as `ServiceNow` refer to in each source context?
3. Which Solicitation governs the pursuit, and how is it distinct from the Opportunity?
4. Which people and organizations participated, and in what contextual roles?
5. Which partner candidates were discussed, considered, or selected?
6. What evidence supports CRI's relationship to the pursuit?
7. Which artifacts exist, what are their versions/appearances, and which are copies versus independent documents?
8. What happened, in what order, and what state changes followed?
9. Which decision fragments can be recovered? Which decisions are explicit versus inferred?
10. Which actions followed the apparent partner/bid decisions?
11. What outcome evidence exists, and what remains unknown?
12. What was believed/accepted at a historical point in time?
13. What contradictory or unresolved claims remain?
14. Which evidence is inaccessible under a restricted security context?

---

## 5. Minimum canonical resource set

The MVP should require the smallest structurally representative set.

### Identity / party

- `Organization`
- `Person`

### Business context

- `BusinessRelationship` or equivalent relationship resources consistent with the umbrella doctrine
- `Opportunity`
- `Solicitation`
- `Agreement`
- `Project` only if evidence demonstrates an independent resulting delivery context

### Evidence / knowledge

- `Artifact`
- `Claim`
- `EvidenceReference` or equivalent evidence linkage construct
- `Assessment`

### Activity / decision

- `Event`
- `Decision`
- `Approval` if independent evidence exists and the admission test justifies first-class representation in the slice
- `Action`
- `Outcome`

### Supporting non-canonical/evidence-graph constructs

- `Observation`
- `CandidateIdentity`
- `CandidateRelationship`
- `CandidateContext`
- `CandidateEvent`
- `DecisionFragment`
- `ArtifactAppearance`
- `ReconciliationProposal`

These supporting constructs may be logical records rather than promoted ontology object types.

---

## 6. Required identity semantics

The implementation must support:

- one canonical identity with multiple aliases;
- contextual shorthand that does not become a global alias automatically;
- parent/child and organizational-unit distinctions;
- same-name-but-distinct entities;
- source identity mappings;
- historical names;
- unresolved candidates;
- merge proposals;
- split proposals;
- reversible reconciliation decisions.

### Minimum identity acceptance cases

- `SFO`, `SF Airport`, and `San Francisco International Airport` can resolve to one canonical organization where evidence supports it.
- `ServiceNow` can remain ambiguous until context distinguishes product/capability from pursuit shorthand.
- a new organization name in email does not automatically create a canonical `Organization`.
- a person changing employer does not create a new canonical `Person`.

---

## 7. Required context semantics

A source thread, folder, or document path is never canonical context by itself.

Context resolution must score or reason over at least:

- organizations;
- people;
- subject/aliases;
- solicitation identifiers;
- opportunity identifiers;
- attachment names/content;
- SharePoint paths;
- dates/deadlines;
- known relationship neighborhood;
- prior resolved context.

The resolver must permit `unresolved` and `multiple plausible contexts` outcomes.

---

## 8. Evidence and provenance semantics

Every material claim, candidate, event, reconstructed decision, or promoted fact must be traceable to source evidence.

Required provenance fields conceptually include:

- source system;
- source native ID;
- source version where applicable;
- source container/mailbox/site;
- source URL/reference;
- source-created/sent/received time;
- capture/discovery time;
- content hash;
- extractor/model/version if interpreted;
- explicit versus inferred status;
- source actor/author;
- source ACL/security metadata;
- origin-lineage links for quotes/forwards/copies/versions.

Repeated appearances of one origin must not count as independent corroboration without justification.

---

## 9. Temporal semantics

The slice must support at least:

- `effective_time` or effective interval;
- `source_time`;
- `recorded_time` when materially distinct/available;
- `discovered_time`;
- `superseded_time` or equivalent current-state retirement semantics;
- exact versus approximate time;
- current versus historical versus hypothetical truth.

A historical query must not use current classification unless evidence supports that classification at the requested time.

---

## 10. Relationship semantics

Relationship records must support:

- participant identities;
- participant roles;
- relationship family/type;
- context scope such as Opportunity or Agreement;
- effective period;
- state;
- evidence;
- epistemic status/confidence;
- security classification.

A partner relationship scoped to one Opportunity must not automatically imply a global strategic partnership.

---

## 11. Event / Decision / Action / Outcome semantics

### Event
What happened.

Examples for the slice: solicitation released, partner contacted, MNDA executed, proposal submitted.

### Decision
What choice was made.

Examples: bid/no-bid, choose CRI, approve proposal submission.

### Action
What was done because of a decision/policy/trigger.

Examples: request MNDA, send pricing request, submit proposal.

### Outcome
What resulted.

Examples: partner joined proposal, interview occurred, award/loss if evidenced.

The implementation must not use one generic activity record as the only semantic representation.

---

## 12. Decision reconstruction requirements

Historical reconstruction begins with fragments.

For each proposed Decision, preserve:

- decision question;
- context;
- alternatives known versus inferred;
- recommendation if evidenced;
- chosen alternative;
- actor/decision maker if known;
- authority/approval evidence;
- exact/approximate time;
- evidence set;
- explicit/inferred status;
- confidence dimensions;
- resulting action(s);
- outcome linkage where available.

The system must permit a partial decision trace without inventing missing stages.

---

## 13. Promotion semantics

Promotion follows:

```text
RAW RECORD
 -> OBSERVATION
 -> CLAIM / CANDIDATE
 -> IDENTITY + CONTEXT RESOLUTION
 -> AUTHORITY + CONFLICT CHECK
 -> VALIDATION / REVIEW
 -> CANONICAL STATE
```

The claim-type promotion matrix is defined separately in `04-CANONICAL-PROMOTION-MATRIX-v0.1.md`.

No single global confidence threshold is permitted.

---

## 14. Security requirements

The slice must demonstrate:

- security context passed into all reads;
- source ACL retained as an input to effective access;
- ontology policy may make access stricter, never silently weaker;
- evidence-level restriction;
- canonical state visible without exposing restricted supporting evidence where policy allows;
- AI/agent caller treated as a governed actor;
- search results filtered before content exposure, not only after retrieval.

A minimum acceptance test must include one synthetic or real restricted-evidence case that does not expose sensitive evidence to an unauthorized test principal.

---

## 15. Read/query surface

Minimum logical operations:

```text
get_object(id, security_context)
resolve_identity(reference, context, as_of, security_context)
get_relationships(id, filters, as_of, security_context)
get_neighbors(id, depth, link_filters, as_of, security_context)
get_state(id, as_of, security_context)
get_timeline(context_id, time_range, security_context)
get_evidence(resource_or_claim_id, security_context)
get_decision_trace(context_or_decision_id, security_context)
find_contradictions(scope, security_context)
find_unresolved_candidates(filters, security_context)
search(query, filters, as_of, security_context)
```

Detailed workload requirements are in `02-QUERY-AND-WORKLOAD-CONTRACT-v0.1.md`.

---

## 16. Proposed-write surface

Build Spec 001 may expose proposed writes only; canonical mutation remains governed.

```text
propose_object(...)
propose_relationship(...)
propose_claim(...)
propose_event(...)
propose_merge(...)
propose_split(...)
promote_candidate(...)
reject_candidate(...)
correct_canonical_interpretation(...)
```

Every promotion/correction must be auditable and provenance-preserving.

---

## 17. Acceptance tests

### Identity

- aliases resolve correctly when context supports them;
- ambiguous aliases remain unresolved;
- same-name distinct entities remain distinct;
- merge and correction do not delete source mappings/history.

### Evidence

- every promoted material fact has retrievable supporting evidence;
- quote/forward/copy lineage prevents false independent corroboration;
- an email can support a claim without the claim becoming canonical.

### Artifact lineage

- identical attachment and SharePoint file can be linked as appearances of one artifact/version;
- changed document versions remain distinguishable.

### Time

- `get_state(as_of=T)` reconstructs the accepted state at T;
- later evidence does not silently backdate a state without effective-time evidence.

### Context

- one email thread may contain records linked to more than one business context;
- thread subject alone cannot force a context.

### Decision trace

- explicit and inferred decision components remain visibly distinct;
- missing alternatives/rationale remain missing rather than fabricated;
- Decision, Approval, Action, Event, and Outcome are query-distinguishable.

### Security

- unauthorized callers cannot retrieve restricted evidence through direct lookup, traversal, timeline, or search;
- permitted canonical state can remain visible without leaking restricted evidence.

### Reprocessing

- repeated ingestion/extraction is idempotent at the evidence layer;
- semantic model updates can reprocess evidence without re-fetching raw source where permitted.

### Technology neutrality

- no acceptance criterion requires a specific database product.

---

## 18. Initial non-functional requirements

These are workload targets for benchmarking, not product SLAs.

- deterministic canonical ID lookup should be optimized for interactive use;
- common 1–3 hop traversals should be interactive under representative MVP data;
- current-state reads must be transactionally coherent;
- canonical promotion/correction must preserve atomic semantic invariants;
- historical state reconstruction must be reproducible;
- evidence retrieval must preserve lineage and permissions;
- search must combine exact/alias/lexical/semantic modes without bypassing security;
- all canonical writes/promotions must be auditable.

Numeric latency targets should be finalized with Platform Engineering after benchmark harness design.

---

## 19. Open items for final Build Spec 001

These are not blockers for the first-session skeleton:

- exact source corpus boundaries and expected record counts;
- final canonical property set and link cardinalities;
- which decision-related resources are promoted core versus domain-level;
- concrete security principals and ACL fixtures for the pilot;
- exact expected outcomes available in the SFO/CRI evidence;
- latency targets after platform benchmark design;
- final acceptance fixture packaging.

---

## 20. Exit condition for M2

Build Spec 001 is complete when an engineering team can implement the slice without inventing:

- ontology meaning;
- epistemic/promotion rules;
- identity/context behavior;
- temporal semantics;
- security semantics;
- required queries;
- acceptance criteria;

and when Platform Engineering can use the workload contract to evaluate physical architecture options objectively.
