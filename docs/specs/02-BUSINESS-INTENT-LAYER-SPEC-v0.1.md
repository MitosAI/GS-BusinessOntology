# GenSigma Business Intent Layer Specification

**Version:** v0.1  
**Status:** Draft for architectural review  
**Governing document:** `CONSTITUTION.md`  
**Primary question:** What is GenSigma trying to accomplish, under what principles, constraints, and measures of success?

---

## 1. Purpose

The Business Intent Layer represents the operating semantics of GenSigma's purpose and direction.

The World Model can tell us what is true. The Capability Model can tell us what GenSigma can realistically do. Neither tells us what GenSigma should prefer.

The Business Intent Layer therefore exists to represent, in explicit and governable form:

- why GenSigma exists;
- what outcomes it is trying to create;
- which markets and customers matter;
- what business models and offerings it chooses to pursue;
- what strategic objectives take priority;
- what values and principles constrain decisions;
- what risk posture is acceptable;
- what success means;
- what tradeoffs are acceptable;
- what policies and decision rules should guide action.

The Business Intent Layer is a first-class peer of the World Model and Capability Model.

```text
BUSINESS INTENT MODEL        WORLD MODEL        CAPABILITY MODEL
What do we want?             What is true?      What can we do?
          \                      |                    /
           \                     |                   /
            +---------------- DECISION ENGINE ----------------+
```

---

## 2. Why intent must be explicit

Two companies exposed to the same external reality can make completely different choices because their intent differs.

A procurement opportunity may be attractive to one company and irrelevant to another. A high-growth market may be rejected because it conflicts with risk appetite, capital constraints, geography, strategic focus, or founder time objectives.

Without an explicit Intent Layer, an AI system will tend to substitute generic optimization goals such as maximize revenue, maximize win probability, minimize cost, or maximize utilization. Those may be locally rational and globally wrong.

The system should instead reason over explicit organizational intent.

Example:

```text
World Model:
Large public-sector AI RFP has appeared.

Capability Model:
GenSigma has moderate delivery capability and two viable partners.

Business Intent:
Prioritize AI-native SLED opportunities that can become repeatable offerings,
while protecting founder time and avoiding low-margin commodity staffing.

Decision:
Pursue only if partner structure and economics satisfy strategic criteria.
```

---

## 3. Intent is not a static mission statement

The Business Intent Layer is not merely a page containing Vision, Mission and Values. It is a structured operating model that connects high-level purpose to practical decision criteria.

```text
Enterprise Purpose
    |
    v
Vision
    |
    v
Mission
    |
    v
Strategic Themes
    |
    v
Strategic Objectives
    |
    v
Initiatives / Bets
    |
    v
Target Markets / Segments
    |
    v
Desired Customer Outcomes
    |
    v
Offerings / Capabilities to Build
    |
    v
Operational Objectives / OKRs
    |
    v
Decision Criteria / Policies
```

This is a traceability spine, not necessarily a rigid hierarchy. Objects may have many-to-many relationships.

---

## 4. Core Intent resources

The initial Business Intent ontology should support the following concepts.

### 4.1 Enterprise Purpose

The durable reason the organization exists beyond a single plan cycle.

### 4.2 Vision

A desired future state of GenSigma, potentially across multiple horizons.

### 4.3 Mission

The durable description of how GenSigma creates value and for whom.

### 4.4 Values / Decision Principles

Values should become operational only when they can influence decisions. Examples include accountability, customer trust, security by design, long-term value over short-term expediency, evidence before belief, and governed AI rather than opaque autonomy.

### 4.5 Strategic Theme

A broad area of strategic focus such as AI Transformation, SLED expansion, recurring managed services, ontology/world-model platform development, or geographic expansion.

### 4.6 Strategic Objective

A measurable or directional objective derived from strategy.

### 4.7 Initiative / Strategic Bet

A concrete program or bet intended to advance one or more objectives.

### 4.8 Market

A commercial or institutional environment GenSigma may choose to operate in.

### 4.9 Customer Segment

A group of customers sharing material decision/use-case characteristics.

### 4.10 Customer Problem / Pain

A recurring problem the company chooses to solve.

### 4.11 Desired Outcome

An outcome GenSigma intends to create for a customer, business unit, stakeholder, or the enterprise.

### 4.12 Offering

A packaged value proposition or service intentionally brought to a market. Offerings reference required capabilities, but capability state belongs to the Capability Model.

### 4.13 Objective / Key Result / Metric

The model should distinguish objective, key result, KPI, threshold, target, and guardrail metric.

### 4.14 Policy

A durable rule that constrains or governs action.

### 4.15 Constraint

A situational or durable limit such as capital, founder time, LBE cap, delivery capacity, geographic registration, contract vehicle eligibility, or security requirements.

### 4.16 Risk Appetite

A structured representation of what risk the company is willing to accept by domain.

### 4.17 Decision Criterion

A reusable rule or weighted factor used by the Decision Engine: strategic alignment, win probability, margin potential, capability fit, customer importance, repeatability, partner quality, founder time burden, downside exposure, etc.

---

## 5. Business units and organizational structure

The Intent Layer may reference Business Units, Practices, Departments or Teams, but canonical organizational identity belongs to the World Model / enterprise ontology.

The Intent Layer defines what an organizational unit is responsible for trying to achieve.

---

## 6. Intent relationships

Important relationships include:

```text
Vision ADVANCES EnterprisePurpose
Mission SUPPORTS Vision
StrategicTheme SUPPORTS Vision
StrategicObjective ADVANCES StrategicTheme
Initiative ADVANCES StrategicObjective
Market IS_TARGETED_BY StrategicObjective
CustomerSegment EXISTS_WITHIN Market
Problem AFFECTS CustomerSegment
DesiredOutcome ADDRESSES Problem
Offering DELIVERS DesiredOutcome
Objective MEASURED_BY Metric
Policy CONSTRAINS ActionType
Constraint LIMITS DecisionContext
RiskAppetite GOVERNS RiskDomain
DecisionCriterion APPLIES_TO DecisionType
OrganizationalUnit OWNS Objective
```

The exact physical representation remains open.

---

## 7. Intent hierarchy versus graph

The Intent Layer should permit hierarchical navigation but must not force every concept into a tree. One initiative may advance several objectives; one offering may support several outcomes; one policy may constrain many action types; one objective may require many capabilities.

---

## 8. Temporal semantics of intent

Intent changes. The platform MUST not overwrite history when strategy changes.

Material intent objects should support effective period, version, status, approval, supersession and rationale for change.

When reconstructing historical decisions, the Decision Engine should reason using intent that was in force at the decision's effective time.

---

## 9. Levels of intent

### 9.1 Constitutional intent

Extremely durable operating principles such as security is first-class, evidence before belief, material writes through governed actions, and AI is a governed actor.

### 9.2 Strategic intent

Multi-year direction.

### 9.3 Operating intent

Quarter/year-level objectives, priorities and constraints.

### 9.4 Local decision intent

The objective for a specific decision context.

---

## 10. Intent and external reality

External events do not automatically rewrite GenSigma's intent. They may invalidate assumptions, create opportunities/threats, trigger strategy review, change priority scores, or produce a proposed strategy change.

This preserves the distinction between **what is happening** and **what GenSigma wants**.

---

## 11. Intent and the Capability Model

Intent may describe capabilities GenSigma wants to develop, but actual capability state belongs elsewhere.

The gap between desired and actual capability becomes a strategic planning input.

---

## 12. Intent and the Decision Engine

A recommendation is not simply a function of observed reality.

```text
Recommendation / Decision
    = f(
        World State,
        Business Intent,
        Capability State,
        Policies,
        Constraints,
        Risk,
        Authority,
        Uncertainty
      )
```

The Decision Engine must preserve which intent objects materially influenced a recommendation or decision when traceability is important.

---

## 13. Priority and conflict resolution

Intent can conflict: maximize growth versus protect margin, grow AI business versus reduce founder time, pursue strategic customer versus avoid concentration, move quickly versus maintain controls.

The model must support priority and conflict semantics through hard constraints, soft preferences, weighted criteria, minimum thresholds, veto policies, lexicographic ordering, or risk-adjusted utility. A weighted score is an available method, not the definition of judgment.

---

## 14. Governance of intent

Intent is powerful and therefore governed. The system should preserve who authored it, who approved it, when it became effective, what it superseded, why it changed, and who may edit or retire it.

AI may propose changes to strategy or objectives but MUST NOT silently change approved Business Intent.

```text
Signal / Learning
      |
      v
Strategy Assessment
      |
      v
Intent Change Proposal
      |
      v
Human Review / Approval
      |
      v
New Effective Version
```

---

## 15. Security

Not all intent is equally visible. Acquisition strategy, pricing strategy, investment plans, executive risk appetite, confidential partner strategy and employee-related operating changes may require restriction.

---

## 16. V1 Business Intent scope

V1 should remain small but decision-useful.

- Enterprise: Vision, Mission, Values, Strategic Themes.
- Strategy: Strategic Objectives, Initiatives, Target Markets, Customer Segments, Desired Outcomes, Offerings.
- Operating guidance: Metrics, Decision Criteria, Policies, Constraints, Risk Appetite.

Suggested first strategic objects should be encoded only after human review rather than assumed canonical from conversation.

---

## 17. Competency questions

The Business Intent Layer should eventually answer:

1. What is GenSigma trying to achieve this year?
2. Which strategic objective does this opportunity advance?
3. Which customer segments are currently prioritized?
4. Which initiatives depend on a particular capability?
5. What policies constrain this decision?
6. Which metric determines whether an initiative is succeeding?
7. Why was an opportunity pursued even though its margin was lower?
8. What strategic assumptions were in force when a historical decision was made?
9. Which current external signals could invalidate a strategic assumption?
10. Where is there a gap between desired and current capability?

---

## 18. Logical operations

Illustrative only:

```text
intent.get_current_strategy()
intent.get_objectives(scope)
intent.get_applicable_policies(context)
intent.get_decision_criteria(decision_type)
intent.get_risk_appetite(domain)
intent.get_constraints(context)
intent.trace_to_vision(object_id)
intent.propose_change(...)
intent.approve_change(...)
```

Machine consumers should receive structured intent, not merely a long strategy document pasted into a prompt.

---

## 19. Non-goals

V1 will not formalize every management philosophy, replace strategic planning, convert all narrative documents into machine-enforced rules, let AI autonomously alter strategy, model every KPI, collapse capability state into intent, or collapse external market facts into strategy.

---

## 20. Acceptance criteria

The design is sound when World state and Business Intent remain distinct; a decision can point to objectives and criteria it served; historical decisions can be evaluated against historical intent; policies can constrain kinetic actions; conflicting priorities can coexist; AI can propose intent changes without silently making them canonical; capability gaps remain distinct from intent; and external events can trigger strategy review without automatically changing strategy.

---

## 21. Status

This initial logical specification should be pressure-tested against real decisions: bid/no-bid, partner selection, market expansion, hiring versus subcontracting, build versus buy, offering prioritization, and pricing/margin tradeoffs.
