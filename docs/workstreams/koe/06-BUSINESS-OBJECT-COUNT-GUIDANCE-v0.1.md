# KOE Architecture Guidance — Business Object Count

**Version:** v0.1  
**Status:** Confirmed architecture guidance  
**Owner:** Knowledge & Ontology Engineering (KOE-001)  
**Confirmed by:** Founder / program authority

---

## Decision

The agreed V1 ontology design guidance is approximately **30–40 business objects**.

This is a complexity guardrail, not a quota and not a requirement to force exactly 30–40 canonical types.

The purpose of the range is to keep the model:

- broad enough to represent the real enterprise operating system rather than a single pilot;
- small enough to remain understandable, governable, testable, and evolvable;
- structurally representative across the first major business domains;
- resistant to source-schema mirroring and noun proliferation.

## Interpretation

The count refers to the practical V1 set of business objects / canonical ontology object types across the promoted core and initial shared/domain extensions.

It does **not** include every:

- property;
- relationship/link type;
- role;
- category;
- interface;
- event subtype;
- action type;
- claim/evidence record shape;
- application view;
- source binding.

Those remain separate semantic constructs.

## Admission discipline

The 30–40 range does not weaken the object-type admission test. A concept should still normally demonstrate several of:

- independent identity;
- independent lifecycle;
- important relationships;
- meaningful security boundary;
- independent business actions;
- ownership/accountability;
- important query value;
- temporal state.

If it does not, model it as a property, relationship, role, event, claim, evidence item, category, interface, derived value, or application view instead.

## Repository reconciliation note

Earlier repository language that suggests roughly **25–35 total V1 object types** should be treated as superseded by this confirmed **30–40 business object** guidance and reconciled in the next foundation-spec/ADR update.

Until that reconciliation lands, KOE work, Build Spec 001, extraction contracts, query contracts, and downstream platform requirements will use **30–40** as the governing design range.
