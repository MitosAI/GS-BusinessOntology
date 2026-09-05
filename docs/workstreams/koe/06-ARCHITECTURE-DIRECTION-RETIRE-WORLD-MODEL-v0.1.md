# Architecture Direction — Current Model Terminology

**Version:** v0.1  
**Status:** Owner-confirmed architecture direction  
**Owner:** Knowledge & Ontology Engineering (KOE-001)

---

## 1. Decision

GenSigma OS will not use **World Model** as the primary current architectural abstraction.

The active architecture is expressed through distinct models with different semantics and responsibilities:

```text
BUSINESS INTENT
+
BUSINESS REALITY
+
EXTERNAL REALITY
+
CAPABILITY
        |
        v
EXECUTIVE JUDGMENT
        |
        v
DECISION / APPROVAL
        |
        v
GOVERNED ACTION
        |
        v
NEW BUSINESS STATE
        |
        v
OUTCOME / LEARNING
```

These models interact through explicit contracts. They should not be collapsed into one generic representation.

---

## 2. Terminology standard

Use these terms in current specifications, APIs, diagrams, and implementation work:

- **Business Intent** — what GenSigma seeks, values, prioritizes, and constrains.
- **Business Reality** — what is operationally true about GenSigma and its direct business relationships, now and historically.
- **External Reality** — material conditions, actors, and changes outside GenSigma that can affect decisions, risk, opportunity, or capability.
- **Capability** — what GenSigma can actually execute with available resources, capacity, qualifications, authority, dependencies, and timing.
- **Executive Judgment / Decision Engine** — how the system evaluates choices from Intent, Reality, Capability, policy, authority, risk, and uncertainty.
- **Governed Action** — authorized business verbs that can change operational state.
- **Outcome / Learning** — what resulted and what should update future state, models, or judgment.

The term **World Model** is now **legacy terminology**. It may appear only when referring to an older artifact or when discussing migration from the earlier architecture language.

---

## 3. Why this is the correct architecture

### Different epistemic roles

- Business Intent is normative.
- Business Reality is descriptive and operational.
- External Reality is environmental and evidence-driven.
- Capability represents feasible action capacity.
- Executive Judgment evaluates alternatives.

Treating all of these as one model hides distinctions the system must preserve.

### Different update tempos

```text
Business Reality          -> fast / operational
External observations     -> continuous
External interpretations  -> governed / slower
Capability                -> changes with resources and time
Business Intent           -> deliberate / governed
```

### Different authority rules

A signed agreement, a procurement addendum, an approved strategic objective, and a staffing-capacity assessment have different authority semantics. They should not inherit one generic truth hierarchy.

### Cleaner decision contract

The decision layer should consume explicit inputs:

```text
judgment(
  business_intent,
  business_reality,
  external_reality,
  capability,
  policy,
  authority,
  uncertainty
)
```

This is more inspectable and auditable than a generic reality object with mixed semantics.

---

## 4. Migration rule

Do not perform a blind rename of older material.

When an older document uses `World Model`, decompose its meaning:

- internal operational truth -> **Business Reality**;
- material external observations/beliefs -> **External Reality**;
- desired direction/preferences -> **Business Intent**;
- feasible resources/authority/capacity -> **Capability**;
- reasoning about alternatives -> **Executive Judgment**;
- state-changing verbs -> **Governed Action**;
- results/feedback -> **Outcome / Learning**.

This is a semantic migration, not find-and-replace.

---

## 5. Build Spec 001

Build Spec 001 is a **Business Reality MVP**.

Its path is:

```text
OUTLOOK + SHAREPOINT
        |
        v
RAW / NORMALIZED EVIDENCE
        |
        v
OBSERVATIONS / CLAIMS / CANDIDATES
        |
        v
IDENTITY + CONTEXT + ARTIFACT RECONCILIATION
        |
        v
CANONICAL BUSINESS REALITY
        |
        v
QUERY / CONTEXT API
```

No generic `World Model` abstraction is required to explain or implement this slice.

---

## 6. Consistency rule for KOE outputs

All new KOE artifacts must follow this terminology. Existing KOE files should use `World Model` only when explicitly discussing legacy repository language. Foundation documents outside this workstream should be migrated in a separate reviewed change so architectural history remains traceable.
