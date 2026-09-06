# KOE Pilot Episode Selection — Build Spec 001

**Version:** v0.1  
**Status:** First-session recommendation  
**Owner:** Knowledge & Ontology Engineering (KOE-001)

---

## 1. Selection criterion

The first pilot should maximize **architectural pressure-test value**, not convenience or familiarity.

The episode should exercise as many of the following as possible without forcing the ontology into a one-off schema:

- identity ambiguity and aliases;
- organization versus organizational-unit distinction;
- contextual roles;
- opportunity versus solicitation distinction;
- partner relationship scoping;
- Outlook + SharePoint evidence;
- artifact/version lineage;
- temporal reconstruction;
- event extraction;
- decision fragments and explicit/inferred distinctions;
- action evidence;
- outcomes;
- source authority differences;
- security constraints;
- contradiction/unresolved cases.

---

## 2. Candidate A — SFO ServiceNow / CRI Advantage

### Strengths

- repeated shorthand and alias risk (`SFO`, airport naming, `ServiceNow`);
- clear need to distinguish technology/product name from opportunity context;
- customer, opportunity, solicitation, partner, people, artifact, agreement, event, decision, and action semantics all appear relevant;
- MNDA/agreement evidence allows source-authority testing;
- partner-selection reasoning can remain partial/inferred rather than fabricated;
- proposal artifacts can test attachment ↔ SharePoint lineage;
- event chronology can include partner contact, agreement execution, proposal preparation/submission, and later pursuit activity;
- suitable for a reconstructed decision trace;
- aligns with the repository's existing reference-case doctrine.

### Weaknesses

- may tempt overfitting to one public-sector procurement process;
- outcome completeness may be partial depending on available evidence;
- `ServiceNow` shorthand introduces deliberate ambiguity that increases first-slice complexity.

### Pressure-test score

**Very high.**

---

## 3. Candidate B — Stridepath / CCSF HRSD

### Strengths

- customer/partner/project/opportunity distinctions likely require careful context handling;
- HRSD/ServiceNow terminology can test product/capability versus pursuit/project ambiguity;
- may include staffing/resource and delivery context in addition to commercial context;
- useful test that CCSF is not modeled as a special ontology class.

### Weaknesses

- boundary between pursuit and active delivery may introduce more domains than necessary for the first slice;
- could pull the MVP prematurely toward workforce/delivery semantics;
- agreement/proposal artifact chain may be less complete than SFO/CRI for the specific Build Spec 001 goals.

### Pressure-test score

**High.**

---

## 4. Candidate C — Fivetran partner agreement

### Strengths

- good legal/artifact/version/source-authority case;
- useful for Organization identity, Partner relationship, Agreement status, execution evidence, and relationship effective time;
- likely easier to bound tightly.

### Weaknesses

- weaker opportunity/solicitation/decision-trace complexity;
- less representative of the first deep RFP-to-cash chain;
- may under-test context resolution and multi-hop business traversal.

### Pressure-test score

**Medium-high.**

---

## 5. Recommendation

Select **SFO ServiceNow / CRI Advantage** as the primary Build Spec 001 episode.

It is the best first slice because it forces the architecture to solve the hard semantic problems early:

```text
ambiguous names
-> canonical identity
-> business context
-> opportunity vs solicitation
-> partner relationship
-> artifacts + agreement evidence
-> event chronology
-> decision fragments
-> action evidence
-> partial outcome
```

This is a stronger test than a clean, easily modeled episode.

The recommendation is consistent with the existing foundation specs, so it does not require a new architecture decision.

---

## 6. Required anti-overfitting checks

Before Build Spec 001 is considered complete, the model defined for SFO/CRI must also be mentally or fixture-tested against:

1. **Stridepath / CCSF HRSD** — verifies that the same semantics handle pursuit/project/partner ambiguity without CCSF-specific classes.
2. **Fivetran partner agreement** — verifies that Agreement and Partner relationship semantics do not depend on a solicitation/opportunity being present.

If a concept works only for SFO/CRI, it should be treated as a pilot-specific view or extension rather than promoted into shared core semantics.

---

## 7. First fixture bundle to request from Evidence/Data Engineering

For the SFO/CRI slice, assemble a bounded evidence bundle containing, where available:

- relevant Outlook Inbox/Sent messages;
- thread history needed to resolve shorthand;
- proposal-related attachments;
- MNDA/agreement artifacts;
- corresponding SharePoint proposal/agreement files and versions;
- any explicit submission/receipt artifact;
- any later message that confirms or contradicts the inferred partner/decision state.

The bundle should preserve original source identity, timestamps, hashes, permissions, and lineage.

The goal is not to collect every related record. The goal is to create the smallest evidence set that still forces correct identity, context, time, evidence, decision, and artifact behavior.
