# GenSigma Systems Design Truths

**Version:** v0.2  
**Status:** Active KOE design doctrine  
**Owner:** Knowledge & Ontology Engineering (KOE-001)

---

## 1. Purpose

The architecture will be governed by a small number of truths that can actually be remembered and used. They are not a scorecard and they are not optional aspirations.

Every major semantic, platform, data, agent, and action design should be explainable through these four truths.

---

## 2. The four design truths

### Truth 1 — Preserve truth

Evidence and history are never destroyed merely because the system's interpretation changes.

Implications:

- source evidence is preserved with provenance;
- historical state remains reconstructable;
- corrections supersede rather than erase;
- copied or repeated evidence does not become false corroboration;
- current truth, historical truth, inferred truth, and hypothetical truth remain distinguishable.

**Invariant:** the system must be able to explain what it knew, why it believed it, and what changed.

---

### Truth 2 — Allow correction

Every interpretation can be wrong and must be safely correctable.

Implications:

- identity reconciliation supports merge and split correction;
- aliases and relationships are revisable;
- canonical state changes preserve prior interpretations;
- inferred decisions and classifications remain distinguishable from explicit facts;
- derived projections can be rebuilt from preserved evidence;
- ontology and policy changes are versioned and migratable.

**Invariant:** no probabilistic or human interpretation is allowed to become operationally irreversible merely because it was once accepted.

---

### Truth 3 — Keep the core stable

The system must grow by extension rather than repeated redesign of its foundations.

The stable semantic kernel owns cross-domain concepts such as:

- canonical identity;
- typed relationships;
- state and time;
- evidence and provenance;
- epistemic status;
- security and authority;
- Event / Decision / Action / Outcome distinctions;
- audit and correction semantics.

Business domains extend this kernel with enterprise objects and domain-specific behavior.

**Invariant:** adding a new source, business domain, agent, workflow, or business object should normally extend contracts rather than redefine foundational meaning.

---

### Truth 4 — Make boundaries explicit

Every subsystem owns a clear responsibility and communicates through explicit contracts.

Examples:

- connectors observe; they do not define canonical truth;
- evidence systems preserve observations and provenance; they do not invent ontology semantics;
- KOE defines business semantics; persistence technology does not;
- Executive Judgment reasons over governed inputs; it does not redefine them;
- agents act only through governed action contracts;
- contextual role is distinct from canonical identity;
- Business Intent, Business Reality, External Reality, and Capability remain distinct models even when linked.

**Invariant:** if two implementations can satisfy an interface while assigning materially different business meaning, the boundary is not specified well enough.

---

## 3. What these truths imply for quality

We do not maintain a long independent list of architectural virtues. The normal qualities of a good system should emerge from the four truths:

- robustness follows from preserved state, explicit uncertainty, and explicit boundaries;
- extensibility follows from a stable core and contractual edges;
- scalability follows from modular boundaries and avoiding semantic coupling;
- reliability follows from correction, replay, idempotency, and preserved history;
- security follows from explicit authority boundaries and governed access contracts;
- observability follows from provenance, audit, and reconstructable state;
- maintainability follows from stable semantics and explicit interfaces.

When two qualities conflict, the four truths are the tie-breaker.

---

## 4. Consequences for Build Spec 001

Build Spec 001 is the **Business Reality Semantic Foundation**, not an SFO/CRI application and not a narrow pilot ontology.

It must define the enterprise-wide foundations needed to support approximately 30–40 V1 business objects across major operating domains.

The first implementation may be incremental, but the specification must not be architected around a single customer, RFP, project, source system, or fixture.

Validation must use multiple materially different business scenarios.

---

## 5. Non-negotiable examples

These follow directly from the truths:

```text
Source evidence != canonical truth
Canonical identity != contextual role
Current interpretation != immutable history
Event != Decision != Action != Outcome
Unknown != false
Unresolved != forced match
One business episode != enterprise architecture
Physical schema != ontology
LLM inference != authority
```

---

## 6. Design review test

For any major proposal, ask only four questions:

1. **Does it preserve truth and history?**
2. **Can we safely correct it when wrong?**
3. **Does it preserve a stable core while allowing extension?**
4. **Are responsibility and semantic boundaries explicit?**

If the answer to any is no, the design requires revision.
