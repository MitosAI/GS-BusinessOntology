# GenSigma Evidence, Knowledge, Discovery and Reconciliation Pipeline

**Version:** v0.1  
**Status:** Draft for architectural review  
**Initial sensors:** Outlook / Exchange Online and SharePoint Online

---

## 1. Purpose

This specification defines how raw enterprise sources become evidence-backed candidate meaning and, after reconciliation and governance, canonical operational ontology state.

The central rule is:

> Discovery observes and proposes. Ontology defines and governs.

The pipeline is intentionally designed to prevent two catastrophic failure modes:

1. turning source-system records directly into ontology truth;
2. allowing duplicate/incorrect identities to contaminate the world model.

---

## 2. End-to-end pipeline

```text
SOURCE SYSTEMS
Outlook | SharePoint | Finance | HR | CRM | Other
       |
       v
RAW CAPTURE
       |
       v
NORMALIZATION
       |
       v
THREAD / DOCUMENT / QUOTE LINEAGE
       |
       v
ROUTING + SECURITY CLASSIFICATION
       |
       v
OBSERVATION / CLAIM EXTRACTION
       |
       v
CONTEXT RESOLUTION
       |
       v
IDENTITY + DOCUMENT RECONCILIATION
       |
       v
ENTERPRISE EVIDENCE GRAPH
       |
       v
ONTOLOGY PROPOSAL
       |
       v
VALIDATION / AUTHORITY / GOVERNANCE
       |
       v
CANONICAL OPERATIONAL ONTOLOGY
```

---

## 3. Sources are sensors

A connector's job is to observe a source accurately, not interpret the entire business.

Outlook is authoritative for facts such as message ID, sender/recipients, sent/received timestamps, message content as recorded and attachment membership. It is not automatically authoritative for legal agreement status, payment status, employment status, final opportunity state, partner status or business authority.

SharePoint is authoritative for the existence/version of a stored artifact, not necessarily for the substantive truth asserted inside the artifact.

---

## 4. Raw evidence capture

Raw evidence should be preserved or securely referenceable with stable identifiers.

Minimum metadata:

- source_system;
- source_native_id;
- source_container/folder/site;
- source_created_time;
- source_modified_time;
- captured_time;
- content hash;
- MIME/type;
- actor/owner where available;
- source ACL/security metadata;
- deletion/tombstone state where supported;
- parent/thread/document lineage IDs.

Raw evidence must be idempotently ingestible.

---

## 5. Email normalization

The email corpus should be normalized before semantic reasoning.

Preserve message identity, conversation/thread identity, direction, participants, external domains, subject, source timestamps, attachment references, folder/mailbox and human/automated indicators.

Analytical cleanup should identify quoted prior messages, forwarded blocks, signatures, disclaimers, repeated campaign content, duplicate attachments and near-duplicate content. Cleanup must not destroy the original artifact.

---

## 6. Threads are communication structures, not business contexts

Messages should be grouped into threads where possible because the thread is usually a better semantic unit than a single message. But the thread is not automatically the business object.

```text
Thread: "ServiceNow"
   |
   v
Context resolution
   |
   +--> SFO ServiceNow opportunity
   +--> active project
   +--> internal capability discussion
   +--> vendor support issue
```

The system must preserve thread membership while separately resolving the governing business context.

---

## 7. Independent routing dimensions

Every meaningful message/thread should be classified on independent axes.

### 7.1 Signal type

Human substantive; System / automated operational; Informational / contextual; Noise.

### 7.2 Business significance

High; Medium; Low.

Automated does not mean unimportant. A renewal deadline can be automated and high-significance.

### 7.3 Business domain

Multi-label where needed: Customer, Partner, Vendor, Opportunity/RFP, Delivery, Workforce, Finance, Legal, Tax/Accounting, Compliance, Technology/IT, Association/Certification, Internal Operations, Strategy, Other.

### 7.4 Security

Normal, Business Confidential, HR Restricted, Finance Restricted, Legal Restricted, Security Restricted, Executive Restricted.

Signal type, significance, domain and security must not be collapsed into one classifier.

---

## 8. What gets extracted

A single email or document may yield multiple observation types.

```text
Source artifact
  +--> Identity observation
  +--> Relationship observation
  +--> Context observation
  +--> Event observation
  +--> Claim
  +--> Decision fragment
  +--> Commitment
  +--> Deadline
  +--> Document reference
  +--> Action evidence
  +--> Outcome signal
```

The extraction layer proposes observations. It does not create canonical truth.

---

## 9. Evidence, knowledge, situation and judgment

The platform should maintain conceptual separation among:

- **Raw data** — bytes/records obtained from source systems.
- **Evidence** — source-backed information supporting or contradicting a proposition.
- **Knowledge** — reconciled, connected propositions the platform can responsibly use, subject to epistemic status and authority.
- **Situation** — the subset of current/historical knowledge relevant to a decision or operational context.
- **Judgment** — assessment of a situation against Business Intent, Capability, policy, risk and uncertainty.

These are stages of increasing interpretation, not interchangeable names for the same database row.

---

## 10. Context resolution

Before interpreting shorthand, events or decisions, discovery should identify the likely business context.

Signals include customer name, opportunity/RFP number, project number, contract/work-order number, participants, partner names, attachment filenames, SharePoint path, dates/deadlines, recurring aliases, document text and related threads.

A temporary **Context Bundle** may be used during discovery as a working construct containing suspected context, participants, artifacts, aliases and confidence. It does not automatically become a canonical ontology type.

---

## 11. Continuous identity reconciliation

Every new candidate identity should first be compared with what is already known.

```text
NEW OBSERVATION
     |
     v
CANDIDATE SEARCH
     |
     +--> strong match -> link evidence / alias
     +--> probable match -> reconciliation proposal
     +--> ambiguous -> keep unresolved
     +--> no match -> create candidate identity
```

Matching may use exact legal identifiers, domain/email address, legal name, aliases, address, known people, source IDs, customer/opportunity context, document overlap, temporal history, relationship neighborhood and semantic similarity.

No single fuzzy-name score should control high-risk merges.

---

## 12. Reconciliation outcomes

The system must support more than `same` or `different`.

Possible outcomes: same canonical object, accepted alias, historical name, parent/child, organizational unit, brand/product versus organization, related but distinct, merge proposal, split proposal, new candidate, unresolved.

Source identity mappings and reconciliation decisions must be preserved.

---

## 13. Document reconciliation and version lineage

Attachments and SharePoint files require their own identity resolution.

```text
Proposal_v4.docx
Proposal_Final.docx
Proposal_Final2.docx
Proposal_SUBMITTED.pdf
email attachment copy
SharePoint copy
```

The system should attempt to represent:

```text
Canonical Document / Artifact
   +--> Version 1
   +--> Version 2
   +--> Final
   +--> Submitted
```

Signals include cryptographic hash, near-duplicate content, filename, author, timestamps, source lineage, embedded metadata and business context.

Multiple appearances of one artifact must not count as independent evidence by default.

---

## 14. Evidence origin lineage

Copied evidence can falsely amplify confidence.

```text
Original email statement
  -> quoted in reply
  -> forwarded
  -> copied into meeting notes
```

These may be four appearances but only one independent origin.

The evidence model should support concepts equivalent to `origin_evidence_id`, `derived_from`, `quoted_from`, `forwarded_from`, `copied_from`, and `document_version_of`.

---

## 15. Source authority

Authority is proposition-specific and temporal.

```text
Email sent/received -> Exchange Online
Payment cleared -> bank/finance authority
Executed legal terms -> signed agreement
Employee payroll status -> payroll/HR authority
RFP deadline -> official procurement source/addendum
```

The platform should preserve source authority contracts that can vary by property and time period.

---

## 16. Chronological discovery strategy

Default historical discovery proceeds from latest observed reality backward.

```text
RECENT WINDOW
  -> establish current identities/context
  -> reconcile
  -> expand to prior month/quarter/year
  -> reconcile additions
  -> add historical state/events/decisions
  -> continue backward
```

This improves identity resolution because current organizations, people and opportunities provide anchors. The system must avoid current-state projection into the past.

---

## 17. Context expansion beyond batch window

The processing window controls where discovery starts, not where evidence may come from.

If a current thread references an older RFP or document, the pipeline may retrieve earlier thread messages, older attachments, SharePoint source documents, proposal versions, signed agreements or related procurement records.

Expanded material should be marked as supporting context rather than counted as activity in the original batch window.

---

## 18. Promotion workflow

No discovery output becomes canonical merely because confidence is high.

```text
Discover
  -> Propose
  -> Compare
  -> Merge/Split/Reject/Keep Unresolved
  -> Validate Source Authority
  -> Apply Security
  -> Review Policy / Human Review as required
  -> Promote
```

The rigor of review varies by risk. Low-risk alias links may auto-link under strict rules; legal-entity merges require stronger evidence; employment/payment state must respect authoritative sources; high-impact decision reconstruction may require human confirmation.

---

## 19. Pilot orchestration

The Aug 31-Sep 4 Outlook pilot demonstrated the initial operating loop.

```text
612 messages
   |
   v
Route + classify
   |
   v
Collapse threads / remove analytical duplication
   |
   v
Identify parties and contexts
   |
   v
Expand context when needed
   |
   v
Extract candidates:
identity / relationship / event / decision / artifact
   |
   v
Reconcile against existing candidates
   |
   v
Produce ontology proposals
```

The first high-value vertical slice should focus on SFO ServiceNow / CRI because it contains relationship, opportunity, document, event, decision and action evidence.

---

## 20. Processing depth strategy

Not all corpus items need the same reasoning cost.

### Lightweight processing

Metadata, participant/domain inventory, hashes, thread membership, attachments, security routing and obvious identifiers.

### Deep processing

Semantic extraction, decision trace analysis, relationship interpretation, context expansion, document reasoning and contradiction analysis.

Historical backfill should combine broad lightweight scanning with targeted deepening.

---

## 21. Security and privacy

The pipeline must classify before broad downstream exposure. Sensitive evidence must retain source permissions or stronger restrictions.

The minimal-extraction principle applies: extract only the sensitive content required to create the permitted business fact.

---

## 22. Observability

The pipeline should expose ingestion lag, records processed, parse failures, duplicate rate, unresolved identity rate, auto-link rate, human review rate, contradiction count, evidence-without-context rate, context-resolution confidence, promotion/rejection counts and restricted-data routing errors.

Quality metrics matter as much as throughput.

---

## 23. Acceptance criteria

The pipeline passes V0.1 when raw evidence remains recoverable after extraction; reprocessing is idempotent; quotes/forwards do not masquerade as independent evidence; email threads remain separate from business context; attachments reconcile with SharePoint documents; new aliases are compared before new canonical objects are proposed; ambiguity can remain unresolved; current-to-past discovery enriches history without corrupting current state; AI claims remain non-authoritative; and security classification carries through to evidence access.

---

## 24. Non-goals

V1 does not ingest every historical source immediately, deeply reason over every email, use email as universal truth, deduplicate destructively, auto-promote high-risk facts solely from LLM confidence, flatten all artifacts into embeddings, or assume one global authority ranking for all sources.
