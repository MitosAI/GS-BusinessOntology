# GenSigma Decision Engine and Capability Model Specification

**Version:** v0.1  
**Status:** Draft for architectural review  
**Governing document:** `CONSTITUTION.md`

---

## 1. Purpose

The Decision Engine converts governed understanding into recommendation, decision, and eventually action.

It sits above three peer models:

```text
BUSINESS INTENT MODEL        WORLD MODEL        CAPABILITY MODEL
What do we want?             What is true?      What can we do?
          \                      |                    /
           \                     |                   /
            +---------------- DECISION ENGINE ----------------+
                                   |
                     recommendation / decision
                                   |
                              approval
                                   |
                            kinetic action
                                   |
                              outcome
```

The Decision Engine is not synonymous with an LLM. It is the governed decision capability of the OS. It may use deterministic logic, models, optimization, rules, simulation, LLM reasoning, human judgment, or combinations of these.

---

## 2. Capability Model

The Capability Model answers:

> What can GenSigma realistically execute, with what resources, authority, dependencies, and constraints, at this time?

This is distinct from:

- **Intent:** what GenSigma wants;
- **World:** what is true;
- **Capability:** what GenSigma can actually do.

### 2.1 Capability resources

The first Capability Model should represent:

- business capability;
- skill;
- credential/certification;
- person availability;
- team capacity;
- partner capability;
- subcontractor capability;
- technology/platform capability;
- contract vehicle eligibility;
- jurisdictional registration;
- budget/capital availability;
- authority/delegation;
- time/deadline feasibility;
- delivery capacity;
- operational dependencies.

### 2.2 Capability is temporal

Capability is not a timeless label.

```text
ServiceNow architecture capability
  current_level: HIGH
  internal_capacity: 1
  partner_capacity: 3
  availability: LOW until Oct 15
  evidence: project history + resumes + partner commitments
```

The Decision Engine should reason over capability state at the relevant decision time.

### 2.3 Capability versus qualification

A certification or resume claim is evidence of capability, not capability itself. The model may distinguish claimed, validated, demonstrated and currently available capability.

---

## 3. Decision loop

The canonical decision loop is:

```text
Signal
  -> Evidence
  -> Situation / Context
  -> Assessment
  -> Assumptions
  -> Alternatives
  -> Models / Predictions
  -> Recommendation
  -> Decision
  -> Approval / Delegation
  -> Action
  -> State Change
  -> Outcome
  -> Learning
```

Not every decision needs every stage. The ontology must nonetheless preserve the semantic distinctions.

---

## 4. Situation and judgment

A raw collection of facts is not yet a decision context.

The Decision Engine may create a governed **Situation Assessment** binding together relevant World Model state, material events, relevant Business Intent, applicable policies/constraints, current capabilities, risks, uncertainty and missing information.

Judgment is the evaluation of that situation against intent, capability, policy, risk and alternatives.

This resolves the conceptual chain:

```text
raw data -> evidence -> knowledge -> situation -> judgment -> decision -> action
```

The system should preserve the inputs to material judgments rather than only the final answer.

---

## 5. Decision as a first-class resource

A Decision should be represented explicitly when it has independent business significance.

Potential fields include decision ID/type, context objects, decision question, alternatives considered, recommendation, chosen alternative, decision maker, participants, authority, decision/effective time, rationale, assumptions, constraints, policies applied, evidence used, confidence/uncertainty, status, approval state, resulting actions and resulting outcomes.

The exact physical schema remains deferred.

---

## 6. Decision Trace

A Decision Trace is primarily the connected traversal through decision-related resources rather than an opaque narrative summary.

```text
Opportunity
   |
   +--> Evidence
   +--> Assessment
   +--> Alternative A
   +--> Alternative B
   +--> Recommendation
   +--> Decision
   +--> Approval
   +--> Action(s)
   +--> Outcome(s)
```

Historical traces may be reconstructed incrementally from email and documents.

The platform MUST distinguish explicit versus inferred decision, explicit versus inferred rationale, known versus inferred alternatives, exact versus approximate decision time, independent versus copied evidence, decision versus recommendation, decision versus approval, and decision versus action.

A dedicated `DecisionCase` or `DecisionProcess` object MAY be introduced later if real data shows an independent lifecycle that cannot be represented cleanly through links and events.

---

## 7. Historical reconstruction

Historical decision recovery is an archaeology problem. A decision may be distributed across email threads, forwarded messages, attachments, pricing spreadsheets, proposals, meeting notes, SharePoint documents, system changes and later references.

The system should build **decision trace fragments** first.

```text
Fragment 1: "CRI looks strongest" -> assessment evidence
Fragment 2: "Let's proceed" -> possible decision evidence
Fragment 3: signed NDA -> action/state evidence
Fragment 4: proposal includes CRI -> downstream confirmation
```

Only after context resolution and evidence accumulation should the platform propose a reconstructed Decision.

---

## 8. Native future decision traces

Going forward, the OS should capture traces natively.

```text
Evidence snapshot
   -> Recommendation
   -> Alternatives
   -> Human/Agent Decision
   -> Approval
   -> Typed Action
   -> Verification
   -> Outcome
```

A native trace should be visibly distinguishable from a historical reconstructed trace. Recommended trace origins: `native_recorded`, `historically_reconstructed`, `hybrid`.

---

## 9. Deterministic and probabilistic reasoning

The Decision Engine should not treat all reasoning as LLM work.

### Deterministic examples

Deadline comparison, eligibility rules, margin thresholds, mandatory approvals, registration status, hard contract requirements, attachment completeness.

### Probabilistic/model-based examples

Win probability, delivery risk, customer relationship strength, partner fit, expected value, likely resource availability.

### LLM-suitable examples

Synthesizing dispersed evidence, generating plausible alternatives, extracting rationale from narrative, explaining tradeoffs, identifying missing context, preparing recommendation narrative.

LLMs are reasoning components operating within governed context, not the source of authority.

---

## 10. Recommendation model

A recommendation should normally include recommended alternative, decision context, supporting intent/objective, relevant world state, capability fit, constraints, risks, alternatives, confidence, missing information, policy/authority requirements, and next action if approved.

```text
Recommendation = f(
  WorldState,
  BusinessIntent,
  CapabilityState,
  Policies,
  Constraints,
  Risk,
  Authority,
  Uncertainty
)
```

The function is not assumed to be a single numeric score.

---

## 11. Multi-objective decisions

Many GenSigma decisions contain competing objectives: strategic alignment, win probability, expected margin, customer importance, repeatability, partner quality, delivery risk, founder time and opportunity cost.

The Decision Engine must support hard constraints, soft preferences, weighted criteria, minimum thresholds, veto policies, lexicographic rules, risk-adjusted expected value and human override with rationale.

A weighted score is an available method, not the constitutional definition of judgment.

---

## 12. Policies, constraints, and authority

A recommendation may be analytically attractive but operationally forbidden.

The engine must evaluate policy constraints, legal constraints, security requirements, delegated authority, approval requirements, budget authority and action risk class.

It should produce both a substantive recommendation and execution eligibility.

---

## 13. Decision confidence and uncertainty

Confidence should not be reduced to one magical number. The system should separately express uncertainty about identity, facts, context, prediction, rationale and outcome expectation.

Example:

```text
Decision recommendation: BID
Confidence: medium-high
Key uncertainty: partner availability
Decision sensitivity: if partner availability = false, recommendation changes to NO-BID
```

---

## 14. Scenario reasoning

Scenarios must remain isolated from operational truth. The Decision Engine should evaluate alternative worlds such as partner unavailable, price reduced, budget delayed, customer funding increased or resource delayed.

Scenario state may reference canonical objects but must not silently mutate them.

---

## 15. Kinetic handoff

The Decision Engine does not directly perform arbitrary writes. Approved decisions hand off to typed actions.

```text
Decision: Use CRI as teaming partner
Approval: Founder approved
Action: ApproveTeamingPartner(...)
Effects:
  - create/update partner relationship scoped to opportunity
  - create action event
  - request NDA/pricing workflow
  - write audit record
```

---

## 16. Outcome linkage and learning

A decision trace is incomplete if no outcome can ever be linked.

```text
Decision -> Action -> Immediate Outcome -> Downstream Outcome -> Learning
```

Learning should not automatically alter approved Business Intent or policy. It may update models, assessments, capability confidence, or propose governance changes.

---

## 17. Initial decision types for V1

1. Bid / no-bid.
2. Teaming partner selection.
3. Resource/candidate selection for a pursuit.
4. Pricing approach approval.
5. Proposal submission approval.
6. Escalation of opportunity risk.
7. Compliance renewal action.

---

## 18. Reference case: SFO ServiceNow / CRI

The initial trace should attempt to answer: What was the actual opportunity? Which aliases referred to it? Why did CRI enter the pursuit? Were alternatives considered? Was selection explicit or behaviorally inferred? What evidence supported the choice? Who had authority? What actions followed? What did the MNDA change? Did CRI appear in the proposal? What outcome resulted?

The model should tolerate missing answers without inventing certainty.

---

## 19. Logical interfaces

Illustrative only:

```text
decision.build_situation(context_id)
decision.get_applicable_intent(context_id)
decision.get_capability_state(context_id)
decision.generate_alternatives(decision_type, context_id)
decision.evaluate_alternative(...)
decision.recommend(...)
decision.record_decision(...)
decision.request_approval(...)
decision.get_trace(decision_id)
decision.link_outcome(decision_id, outcome_id)
```

---

## 20. Acceptance criteria

The design passes when a recommendation can be traced to World, Intent and Capability inputs; a decision is not confused with an event, recommendation, approval or action; historical traces can remain partial; AI inference remains visibly inferred; hard policies can block a recommendation; capability changes can change recommendations without changing intent; approved decisions can hand off to typed actions; outcomes link back to decisions; and reconstructed/native traces can coexist.

---

## 21. Non-goals

V1 does not create a universal autonomous decision maker, replace executive judgment, encode every decision as a weighted score, allow LLM reasoning to bypass policy, infer hidden motives as fact, execute high-risk actions without authority, or finalize all decision object types before real-data pressure tests.
