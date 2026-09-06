# KOE Canonical Promotion Matrix — Build Spec 001

**Version:** v0.1  
**Status:** First-session semantic policy draft  
**Owner:** Knowledge & Ontology Engineering (KOE-001)  
**Rule:** No universal confidence threshold governs promotion.

---

## 1. Promotion doctrine

Canonical state is accepted operational meaning, not merely high-confidence extraction.

Promotion must evaluate:

- claim/resource type;
- source authority for that proposition;
- identity and context resolution;
- corroboration and origin independence;
- contradiction status;
- temporal consistency;
- security classification;
- business impact/risk;
- whether human review is required.

Confidence is one input, not the promotion rule.

---

## 2. Promotion levels

### P0 — Never auto-promote from extraction alone

Requires explicit governed review or authoritative system evidence.

### P1 — Authoritative-source promotion eligible

May be promoted automatically only when source identity, proposition type, authority contract, context, and temporal semantics are unambiguous and no contradiction exists.

### P2 — Corroboration required

Requires multiple independent evidence origins or one strong authoritative source plus consistency checks.

### P3 — Low-risk reconciliation eligible

May be auto-linked under strict rules where error impact is low and reversibility is strong.

### P4 — Evidence-graph only by default

Remain non-canonical unless later evidence/governance justifies promotion.

---

## 3. Matrix

| Proposition / Resource | Default level | Promotion basis | Human review trigger |
|---|---:|---|---|
| Exchange message metadata: sender, recipient, sent time, message ID | P1 | Exchange source record | source inconsistency or suspected corruption |
| SharePoint file existence/version metadata | P1 | SharePoint source metadata | conflicting version lineage or permissions anomaly |
| Exact attachment ↔ SharePoint file identity by cryptographic hash | P3 | exact bytes/hash + source lineage | conflicting business context or security scope |
| Near-duplicate artifact/version relation | P2/P4 | content similarity + metadata + context | material legal/proposal document or ambiguous lineage |
| Organization alias from exact legal identifier/domain + known identity | P3 | deterministic/high-quality identity signals | ambiguous shared domain, subsidiary/unit distinction |
| Organization alias from shorthand in one email/thread | P4 | evidence graph only | promote only after broader reconciliation |
| Person identity from exact email address + continuity evidence | P3 | stable identifier and context | shared mailbox, recycled address, identity conflict |
| Person merge based mainly on name similarity | P0/P4 | insufficient | always review if merge materially changes canonical identity |
| Customer / Partner / Vendor role | P2 | relationship evidence + context scope | role has legal/financial significance or conflicting evidence |
| Opportunity identity | P2 | opportunity identifiers, customer, solicitation, participants, artifacts | ambiguous shorthand or overlapping pursuits |
| Solicitation identity | P1/P2 | official solicitation artifact/identifier | reissue/amendment ambiguity |
| Solicitation deadline | P1 | official procurement source/addendum | conflicting official versions or unclear effective addendum |
| Opportunity status inferred from email tone | P4 | non-authoritative | require stronger evidence/review |
| Proposal submitted | P1/P2 | submission receipt, sent submission email, portal evidence, final artifact | conflicting timestamps/status |
| Agreement exists as draft | P1 | artifact/version evidence | none unless classification disputed |
| Agreement executed | P0/P1 | signed/executed authoritative artifact or legal system | signature validity, competing versions, legal ambiguity |
| Partner selected | P2 | explicit decision/approval or strong downstream confirmation | inferred only, alternatives unclear, high-impact relationship |
| Decision reconstructed from fragments | P0/P4 | evidence graph/reconstruction | human review before canonical Decision unless natively recorded |
| Explicit recorded decision made through governed system | P1 | native decision record with authority | policy/authority exception |
| Approval | P1/P2 | authoritative approval record or explicit approval evidence | authority unclear or high-risk action |
| Event: partner contacted | P1/P2 | direct sent/received communication evidence | identity/context ambiguity |
| Event: interview scheduled | P1 | calendar/email/official notice evidence | conflicting schedule/cancellation |
| Outcome: award won/lost | P1/P2 | official award/loss notice or authoritative procurement record | ambiguous partial award or protest/pending status |
| Payment received | P0/P1 | bank/finance authority, not email alone | reconciliation dispute |
| Employment/payroll status | P0/P1 | HR/payroll authority | sensitive/conflicting records |
| AI-generated assessment | P4 | evidence graph / assessment resource | never silently canonical as fact |
| AI-generated entity match | P3/P4 | depends on deterministic corroboration and risk | material merge/split or ambiguity |
| Historical effective date inferred from later reference | P4 | inferred historical candidate | review/corroboration required |

---

## 4. Conflict rules

1. Stronger proposition-specific authority outranks weaker source assertions; authority is not globally ranked across all facts.
2. New evidence does not delete old observations.
3. Contradictory authoritative evidence blocks automatic promotion until resolved.
4. A later source may change current state without invalidating historical truth.
5. Copied/quoted/forwarded repetitions count as one origin unless independent authorship/evidence exists.
6. A promotion may be reversed or corrected without deleting the promotion history.

---

## 5. Identity-specific review tiers

### Low-risk alias link

Auto-link may be allowed when:

- canonical candidate already exists;
- identifier evidence is strong;
- no plausible competing candidate exists;
- scope is clear;
- operation is reversible;
- no sensitive/legal identity consequence exists.

### Material merge

Requires stronger governance when:

- two canonical identities would be collapsed;
- historical relationships would be rewritten;
- legal entities or organizational units are involved;
- security boundaries differ;
- downstream actions/agreements/payments depend on identity.

### Split

Should normally require review because prior canonical assertions must be redistributed while preserving provenance.

---

## 6. Decision-specific promotion policy

Historical decision reconstruction is high epistemic risk.

A canonical Decision should normally require at least one of:

- explicit decision statement by an authorized decision maker;
- governed/native decision record;
- strong triangulation across independent evidence plus human review.

Downstream action alone may support an **inferred decision candidate**, but must not automatically create an explicit historical Decision.

Known and inferred alternatives, rationale, authority, and time must remain separately labeled.

---

## 7. Security rule

Promotion never weakens access control.

A canonical fact may be promoted while supporting evidence remains restricted. The promotion process must record enough provenance to prove support without exposing restricted content to unauthorized callers.

---

## 8. Promotion audit requirements

Every canonical promotion/correction should preserve:

- candidate/resource promoted;
- evidence set used;
- authority rule applied;
- conflict checks performed;
- actor or automated policy responsible;
- human approver if required;
- effective time;
- promotion time;
- prior state superseded;
- model contribution if any;
- reason/rationale;
- rollback/correction link where applicable.
