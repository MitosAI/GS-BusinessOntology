# ECR-001 — Transition Brief v0.1

**Workstream:** Executive Cognition Research  
**Role:** ECR-001 — Executive Cognition Research Lead  
**Status:** Foundational research DONE; working architecture DECIDED; benchmark implementation READY  
**Authoritative continuation rule:** A fresh ECR agent should be able to continue from this file plus the governing repository artifacts without access to prior chat history.

---

## 1. Mission and scope

ECR-001 owns the research-backed computational foundation of the **Decide / Executive Judgment** portion of GenSigma OS.

Primary mission:

> Determine which combination of rules, formal decision methods, probabilistic reasoning, optimization, causal reasoning, strategic interaction, LLM assistance, human authority, and learning loops can reproduce and improve high-quality executive judgment while remaining explicit, auditable, evidence-backed, correctable, and governed.

ECR owns:

- decision-science and computational-cognition research;
- decision-class analysis;
- method-selection logic as research/design;
- uncertainty / calibration / causal / value-of-information research;
- benchmark and evaluation design;
- Decision Engine architecture proposals;
- benchmark implementation follow-through inside approved architecture.

ECR does **not** own:

- canonical ontology object admission;
- Business Intent semantics;
- production persistence/runtime/platform choices;
- source ingestion architecture;
- security/authority policy definition outside approved contracts;
- cross-workstream architecture decisions;
- production autonomous action authority.

Cross-cutting changes use `ASK_ARCHITECT`. Ordinary ECR research, benchmark design, implementation planning, and reversible benchmark mechanics use `LOCAL_SOLVE`.

---

## 2. Governing artifacts

Read these before material work:

1. `AGENTS.md`
2. `CONSTITUTION.md`
3. `docs/program/00-PROJECT-BRIEF-v0.1.md`
4. `docs/program/01-OPERATING-ARCHITECTURE-v0.1.md`
5. `docs/program/03A-WORKSTREAM-EXECUTION-UPDATE-v0.1.md`
6. `docs/program/05-CHIEF-ARCHITECT-DECISION-METHOD-v0.1.md`
7. `docs/program/08-WORKSTREAM-DELIVERY-STANDARD-v0.1.md`
8. `docs/protocols/AGENT-DEFINITION-AND-ESCALATION-STANDARD-v0.1.md`
9. `docs/roles/02-EXECUTIVE-COGNITION-RESEARCH-LEAD-CHARTER.md`
10. `docs/research/RESEARCH-001-COMPUTATIONAL-EXECUTIVE-JUDGMENT-CHARTER-v0.1.md`
11. `docs/adr/ADR-003-EXECUTIVE-COGNITION-WORKING-ARCHITECTURE.md`
12. `docs/specs/03-DECISION-ENGINE-AND-CAPABILITY-MODEL-SPEC-v0.1.md`
13. `docs/build/BUILD-SPEC-001-BUSINESS-REALITY-MVP-SKELETON-v0.1.md`
14. ECR artifacts `01`–`16` under `docs/workstreams/ecr/`
15. Current ECR implementation issues listed in Section 12 below.

Repository operating law:

`FRAME -> RESEARCH -> DESIGN -> PLAN -> TASK -> BUILD -> VERIFY / LEARN`

Benchmark-first is mandatory before proposing material new engineering/research mechanisms when established public practice plausibly exists.

---

## 3. Current architecture

### 3.1 System context

Current ECR reasoning should use the modular GenSigma architecture, not a giant monolithic world model:

```text
BUSINESS INTENT
BUSINESS REALITY
EXTERNAL REALITY
CAPABILITY
POLICY / AUTHORITY / SECURITY
          |
          v
SITUATION BUILDER
          |
          v
DECISION CLASS + STAKES + REVERSIBILITY + AUTHORITY
          |
          v
DETERMINISTIC GATES
          |
          v
METHOD ROUTER
          |
          +--> probability / Bayesian reasoning
          +--> optimization
          +--> scenario / simulation
          +--> causal / intervention reasoning
          +--> strategic interaction / bargaining
          +--> real-options / staged commitment
          +--> structured qualitative judgment
          +--> LLM interpretation / generation / orchestration
          |
          v
VOI / TIMING + SENSITIVITY + DEBIAS + COUNTERARGUMENT
          |
          v
AUDITABLE RECOMMENDATION
          |
          v
DECISION / APPROVAL / DELEGATED AUTHORITY
          |
          v
GOVERNED ACTION
          |
          v
OUTCOME / VERIFICATION
          |
          v
CALIBRATION / LEARNING / CHANGE PROPOSAL
```

Core formulation:

> **One common decision anatomy. Multiple computational methods. Explicit method selection. Governed authority. Measured learning.**

### 3.2 Chief Architect decision

`ADRQ-ECR-001` is **RESOLVED — DECIDED**.

Authoritative artifact:

`docs/adr/ADR-003-EXECUTIVE-COGNITION-WORKING-ARCHITECTURE.md`

ADR-003 accepts the **Hierarchical Policy Portfolio** as the working Decision Engine architecture, subject to M11 prototype validation.

Hierarchy governs:

- Business Intent;
- strategy/policy;
- authority;
- risk/timescale.

Decision-class routing selects appropriate analytical methods.

LLMs are components inside the architecture, not the sole Decision Engine.

### 3.3 Approved shared semantic/query requirements

ADR-003 approves these cross-cutting requirements without automatically creating new canonical object types:

1. probability adequacy;
2. multidimensional uncertainty;
3. ex-ante expectations;
4. reversal / sensitivity conditions;
5. decision-method provenance;
6. causal-versus-predictive distinction.

KOE owns the smallest coherent semantic representation and should avoid object proliferation.

### 3.4 M11 prototype classes

DECIDED:

- first prototype: **Bid / No-Bid**;
- contrast class: **Staffing / Resource Assignment**.

Purpose of the pair: prove that different decision structures genuinely route to different methods rather than hiding one universal prompt behind a router.

---

## 4. Key conclusions

### 4.1 Executive cognition is governed method selection

There is no defensible universal executive-decision algorithm for GenSigma.

Different decision classes require different computational method profiles.

Examples:

- eligibility / hard policy -> deterministic rules;
- formal resource allocation -> optimization;
- repeated uncertain events -> probability/Bayes where calibrated evidence exists;
- novel structural uncertainty -> scenarios/sensitivity;
- adaptive counterparties -> selective game/bargaining reasoning;
- intervention choice -> causal reasoning, not prediction alone;
- irreversible uncertain commitments -> staged commitment / real-options reasoning;
- unstructured evidence / alternative generation / critique -> LLM assistance;
- unresolved high-stakes value tradeoffs -> governed human authority unless explicitly delegated.

### 4.2 Deterministic before probabilistic

Known permissions, rules, arithmetic, deadlines, feasibility conditions, and enforceable authority constraints should not be probabilisticized.

### 4.3 Probability must be earned

Research construct:

```text
P0 — unknown / not quantified
P1 — qualitative / ordered likelihood
P2 — empirical / reference-class estimate
P3 — calibrated model / defensible posterior
```

Do not coerce P0/P1 into fake numeric probability because a downstream formula expects a number.

### 4.4 Prediction is not intervention

Research construct:

```text
C0 — association only
C1 — causal hypothesis with explicit assumptions
C2 — observational causal estimate with defensible identification
C3 — experimental / quasi-experimental / strongly identified causal evidence
```

Predictive accuracy alone does not justify a claim that taking action X will cause outcome Y.

### 4.5 Decision timing is part of judgment

The engine must be able to recommend:

- decide now;
- gather evidence;
- wait;
- run an experiment;
- stage the commitment;
- preserve an option.

Value of information should be used to reduce uncertainty **when it can change/improve the decision**, not merely to increase confidence.

### 4.6 Decision quality is distinct from realized outcome

A good process can lose; a bad process can get lucky.

Preserve ex-ante evidence, assumptions, alternatives, recommendation, forecast, sensitivity, and authority context separately from later outcome.

### 4.7 Learning must be typed and governed

One outcome may update a statistic without justifying a strategy or policy change.

Learning should propose the appropriate level of update rather than silently mutating Business Intent or policy.

### 4.8 Authority is part of cognition

AI autonomy should be decision-class / stakes / risk scoped, not one global autonomy setting.

A recommendation may be analytically attractive yet not executable by the current actor.

---

## 5. DECIDED / TENTATIVE / OPEN / DEPRECATED

### DECIDED

- Hierarchical Policy Portfolio is the working Executive Cognition architecture, subject to M11 validation (`ADR-003`).
- Bid / No-Bid is the first M11 decision class.
- Staffing / Resource Assignment is the contrast optimization-heavy class.
- LLM is a component, not the sole Decision Engine.
- deterministic constraints/authority precede softer probabilistic or LLM reasoning where known;
- probability adequacy, multidimensional uncertainty, ex-ante expectations, sensitivity/reversal, method provenance, and causal-vs-predictive distinction are approved cross-cutting requirements;
- benchmark mechanics follow frozen time-correct cases, multiple arms, multiple metrics, reproducible run manifests, proper probabilistic scoring, and blind human review where feasible;
- benchmark-local `DecisionCase` is an evaluation construct, **not** automatically a canonical ontology object;
- broad foundational Research 001 literature expansion is complete; further research should be question-driven.

### TENTATIVE / WORKING

- Exact implementation of the Hierarchical Policy Portfolio remains a working architecture implementation to be validated by M11.
- P0–P3 probability adequacy and C0–C3 causal adequacy are useful research constructs; exact canonical representation is KOE/shared-spec work.
- Decision adequacy levels L0–L3 are research/design constructs until shared architecture explicitly adopts a representation.
- 10–20 historical Bid/No-Bid cases is the target initial case pack; actual valid case count depends on reconstructable evidence.
- blind human review is preferred where arm identity can reasonably be hidden; exact review workflow is benchmark implementation detail.
- model/provider choices for benchmark arms remain configuration, not architecture.

### OPEN

- Exact smallest semantic representation of ADR-003 requirements in KOE contracts / Decision Engine shared spec.
- Shared Decision Engine spec on `main` still predates ADR-003 and has not yet been reconciled with all approved research semantics.
- Exact benchmark implementation library/runtime is open and should remain reversible.
- Historical case availability and evidence completeness are not yet validated.
- Staffing/Resource Assignment optimization module details remain future benchmark work after the Bid/No-Bid harness is operational.
- Whether any research construct requires a new canonical resource remains subject to semantic admission / `ASK_ARCHITECT` if necessary.
- Production autonomy/approval thresholds are not selected by Research 001.

### DEPRECATED / DO NOT REVIVE AS DESIGN CENTER

- universal `decide()` / universal deliberation pipeline as the primary architecture;
- LLM-only executive judgment architecture;
- one weighted score as the definition of judgment;
- one global confidence number as the primary uncertainty representation;
- fabricated probabilities for novel/weakly evidenced uncertainty;
- predictive models silently treated as causal intervention models;
- realized outcome as the sole decision-quality measure;
- uncontrolled learning that silently changes Intent/policy;
- one global agent-autonomy switch;
- a monolithic `World Model` as the ECR design center. Older repository documents may retain historical `World Model` terminology; current ECR work should reason through Business Intent + Business Reality + External Reality + Capability.

---

## 6. Rejected approaches and why

### Universal deliberation pipeline

Rejected as primary architecture because unlike decision classes would be forced through one reasoning pattern, creating false uniformity and poor method fit.

### LLM-only decision engine

Rejected because LLMs are weak authority boundaries, are not reliable numerical optimizers/calibrators, can fabricate certainty, and should not own canonical truth, policy enforcement, arithmetic guarantees, or high-impact final authority.

### Pure Bayesian executive architecture

Rejected as universal architecture because many executive uncertainties cannot support defensible priors/likelihoods and some important choices are optimization, causal, strategic, rule-based, or qualitative problems.

### Optimization-everywhere

Rejected because objectives/constraints are often incomplete or value-laden; optimization is powerful only after formalization is legitimate.

### Static weighted scorecard as the engine

Rejected as primary architecture because hard vetoes, lexicographic preferences, uncertainty structure, timing, causal effects, and strategic response cannot be reduced safely to one compensatory score.

### Outcome-only evaluation

Rejected because luck confounds process quality; benchmark must separate ex-ante process, forecast quality, execution, and outcome.

### One showcase case

Rejected because architecture cannot be validated on SFO/CRI or any single story; benchmark needs varied frozen historical cases.

### Bespoke benchmark science

Rejected after benchmark-first validation. Established public evaluation practice is sufficient; GenSigma's novelty should be in the business decision cases and semantic context, not invented evaluation mechanics.

---

## 7. Important research / benchmark findings

### Research domains covered

R001 completed the required foundational pass across:

- normative decision theory;
- Bayesian decision theory;
- operations research;
- game theory / strategic interaction;
- control theory / feedback;
- behavioral decision science / bounded rationality;
- strategic management / executive decision practice;
- AI reasoning / planning;
- military command-and-control / OODA.

Representative canonical sources are mapped in `01-R001-A-DISCIPLINE-AND-SOURCE-MAP-v0.1.md`.

### Executive-decision practice finding

Fast strategic decisions need not be shallow. Empirical executive-decision literature supports using rich information, multiple alternatives, structured advice, and managed conflict rather than equating speed with intuition-only decision making.

### Control / feedback finding

Executive cognition benefits from explicit state estimation, feedback, correction cadence, and different timescales: fast operational corrections should not automatically become slow strategic worldview changes.

### Causal finding

Action selection requires stronger reasoning than outcome prediction. The system should expose causal assumptions and identification quality rather than turning correlations into action claims.

### Value-of-information finding

The decision system should stop researching when expected decision improvement no longer justifies information cost/delay. More certainty is not automatically more valuable.

### Real-options finding

When commitment is irreversible and material new information may arrive, staged commitment / delay can itself carry value.

### Forecasting finding

Probability quality must be scored over time. Brier score is appropriate for binary forecasts; calibration claims require adequate sample size and retained raw forecast/outcome pairs.

### Benchmark-first validation

`15-R001-BENCHMARK-PRACTICE-VALIDATION-v0.1.md` checked the harness against established public practice:

- NIST benchmark-evaluation guidance: objective definition, rigorous implementation, validity, transparency, reproducibility, useful reporting;
- Stanford HELM: standardized scenarios, multiple metrics, reproducibility and run transparency;
- Gneiting/Raftery forecast-evaluation literature: proper scoring rules, calibration, sharpness.

Conclusion:

> GenSigma does not need novel benchmark science. Use frozen domain cases + established evaluation discipline.

---

## 8. Benchmark architecture and evaluation arms

Each benchmark case must freeze the decision-time state:

```text
DecisionCase
- decision question
- as_of timestamp
- applicable Business Intent
- Business Reality then
- External Reality then
- Capability then
- policy / authority then
- evidence available by as_of
- known uncertainty
- later outcome held out until scoring
```

Planned comparison arms:

1. reconstructed historical human decision;
2. LLM-only baseline;
3. static weighted-scorecard baseline;
4. modular routed cognition architecture;
5. specialist quantitative baseline where appropriate.

Evaluation dimensions:

- hard-constraint / policy / authority violations;
- factual/evidence support;
- evidence completeness and contradiction handling;
- decision framing;
- alternative quality;
- method appropriateness;
- uncertainty/probability/causal honesty;
- sensitivity / reversal transparency;
- auditability and reproducibility;
- latency / cost / review burden;
- blinded human reviewer preference;
- Brier score / calibration-ready forecast records where probabilities are legitimate;
- realized outcome kept separate from ex-ante process quality.

No unnamed composite intelligence score should hide failures across dimensions.

---

## 9. Assumptions

1. Existing GenSigma evidence can yield a meaningful subset of historical Bid/No-Bid cases; this must be validated, not assumed as fact.
2. Evidence/Data can support time-correct retrieval/provenance for historical case construction.
3. Benchmark contracts may be local evaluation artifacts without becoming canonical ontology semantics.
4. Model/provider/runtime choices can remain replaceable benchmark configuration.
5. Human reviewers can assess at least a subset of cases; reviewer disagreement should remain visible.
6. Synthetic fixtures are sufficient to validate benchmark mechanics before historical data is introduced.
7. ADR-003 is the authoritative current architecture even though the older shared Decision Engine spec still contains pre-ADR terminology/structure.
8. Branch divergence must be reconciled before PR #4 can merge cleanly.
9. M11 is a validation gate: if the router/hierarchy adds complexity without measurable benefit, ADR-003 should be revisited rather than defended by default.

---

## 10. DONE / READY / BLOCKED

### DONE

- R001 foundational literature/research program.
- R001-A discipline/source map.
- R001-B decision anatomy.
- R001-C decision-class pressure test.
- R001-D deterministic/probabilistic/judgment boundary.
- R001-E candidate cognition architectures.
- causal decision reasoning.
- value-of-information / stopping research.
- real-options / staged-commitment research.
- forecast calibration/reference-class research.
- delegated decision-rights research.
- learning/update-discipline research.
- cognition benchmark harness design.
- R001-F final synthesis / Decision Engine patch proposal.
- benchmark-first validation against external public practice.
- CA architecture gate (`ADRQ-ECR-001`) resolved `DECIDED` via ADR-003.
- benchmark execution plan reconciled to ADR-003.
- Codex-ready issues for benchmark tasks created.

### READY

- Issue #11 — benchmark core contracts.
- Issue #12 — frozen-case loader / hindsight-leakage guard (after #11 contract stability).
- Issue #13 — common arm interface + LLM-only + scorecard baselines (after #11/#12 as specified).
- Issue #14 — scoring engine / forecast metrics (can proceed after #11, with later end-to-end integration).
- Issue #15 — blind human review / reporting (core may proceed after #11; full integration depends on #12–#14).
- Issue #19 — historical Bid/No-Bid case pack (case discovery may begin; accepted fixtures depend on #11/#12).
- Issue #20 — modular routed cognition benchmark arm under ADR-003 (implementation depends on #11/#13; full scoring on #14).
- precise shared Decision Engine spec reconciliation against ADR-003 / R001-F, subject to normal repository integration/review.

### BLOCKED

No ECR subtask is currently blocked by `ADRQ-ECR-001`; it is resolved.

Practical merge/integration blocker:

- PR #4 branch is materially diverged from `main` and must be reconciled/rebased before merge.

Potential future blockers must use `ASK_ARCHITECT` only if implementation discovers a need to change shared semantics, authority/security, provenance/time, ownership boundaries, or hard-to-reverse platform/runtime architecture.

---

## 11. Current branch / PR state

### Active ECR branch

`workstream/ecr-first-session-v0.1`

At migration review before this transition brief commit, comparison to `main` showed:

- status: `diverged`;
- ECR branch: 16 commits ahead / 32 commits behind before the migration commits;
- PR #4 was open and GitHub reported `mergeable: false`.

This branch has since gained migration commits updating R001-15, R001-16, and adding this transition brief, so exact ahead count should be rechecked before merge.

### Pull request

PR #4 — `ECR first session: computational executive judgment foundation`

Base: `main`  
Head: `workstream/ecr-first-session-v0.1`

The PR body predates some later research and should not be treated as the full current workstream state; this transition brief plus ADR-003 and the current file set are authoritative for continuation.

---

## 12. Current issues

### ECR implementation issues

- **#11** — `[BUILD][ECR] Executive cognition benchmark core contracts`
- **#12** — `[BUILD][ECR] Frozen decision case loader and hindsight-leakage guard`
- **#13** — `[BUILD][ECR] Benchmark arm interface with LLM-only and scorecard baselines`
- **#14** — `[BUILD][ECR] Benchmark scoring engine and probabilistic forecast metrics`
- **#15** — `[BUILD][ECR] Blind human review packets and benchmark reporting`
- **#19** — `[BUILD][ECR] Historical Bid/No-Bid benchmark case pack`
- **#20** — `[BUILD][ECR] Modular routed cognition benchmark arm`

### Resolved architecture request

`ADRQ-ECR-001` was raised in PR #4 and resolved `DECIDED` by CA-001.

Authoritative resolution: `docs/adr/ADR-003-EXECUTIVE-COGNITION-WORKING-ARCHITECTURE.md`.

---

## 13. Current durable ECR artifact set

Under `docs/workstreams/ecr/`:

1. `01-R001-A-DISCIPLINE-AND-SOURCE-MAP-v0.1.md`
2. `02-R001-B-DECISION-ANATOMY-v0.1.md`
3. `03-R001-C-DECISION-CLASS-PRESSURE-TEST-v0.1.md`
4. `04-R001-D-DETERMINISTIC-PROBABILISTIC-BOUNDARY-v0.1.md`
5. `05-R001-E-CANDIDATE-EXECUTIVE-COGNITION-ARCHITECTURES-v0.1.md`
6. `06-FIRST-SESSION-HANDOFF-v0.1.md`
7. `07-R001-CAUSAL-DECISION-REASONING-v0.1.md`
8. `08-R001-VALUE-OF-INFORMATION-AND-STOPPING-v0.1.md`
9. `09-R001-REAL-OPTIONS-AND-STAGED-COMMITMENT-v0.1.md`
10. `10-R001-FORECAST-CALIBRATION-AND-REFERENCE-CLASSES-v0.1.md`
11. `11-R001-DELEGATED-DECISION-RIGHTS-AND-AUTHORITY-ENVELOPES-v0.1.md`
12. `12-R001-LEARNING-UPDATE-DISCIPLINE-v0.1.md`
13. `13-R001-COGNITION-BENCHMARK-HARNESS-v0.1.md`
14. `14-R001-F-FINAL-SYNTHESIS-AND-DECISION-ENGINE-PATCH-PROPOSAL-v0.1.md`
15. `15-R001-BENCHMARK-PRACTICE-VALIDATION-v0.1.md`
16. `16-EXECUTION-PLAN-COGNITION-BENCHMARK-v0.1.md`
17. `ECR-001-TRANSITION-BRIEF-v0.1.md` (this file)

Older artifacts such as `06-FIRST-SESSION-HANDOFF` and portions of `14-R001-F` preserve the pre-decision architecture-gate state. Where they conflict with current status, use ADR-003 + R001-15 + R001-16 + this transition brief.

---

## 14. Dependencies

### Chief Architect / shared architecture

- ADR-003 is resolved and supplies architecture authority.
- Any new shared semantic or cross-workstream architecture discovered during build goes through CA-001.

### Knowledge & Ontology Engineering

ECR depends on KOE for the smallest coherent representation of approved decision semantics, including time/evidence/Decision/Approval/Action/Outcome relationships and the new ADR-003 query requirements.

ECR must not create a parallel semantic architecture inside benchmark code.

### Evidence & Data Engineering

Historical case pack (#19) depends on EDE for source retrieval, provenance correctness, temporal availability, duplicate/quoted-evidence handling, and safe evidence access.

### Platform Engineering

Initial harness mechanics should remain lightweight/reversible. Platform concerns become relevant for runtime instrumentation, repeatability, cost/latency measurement, and later productionization, but no production platform choice is required to begin the benchmark.

### Build Spec 001

BUILD SPEC 001 is primarily Business Reality MVP work, but it explicitly requires an **auditable DecisionContext input seam**. ECR benchmark contracts should pressure-test that future seam without redefining Business Reality semantics.

---

## 15. Risks

1. **Branch divergence:** PR #4 is far behind `main`; merge conflicts/integration drift are likely unless rebased/reconciled deliberately.
2. **Shared spec lag:** main Decision Engine spec predates ADR-003; agents may accidentally follow stale language unless they read ADR-003 first.
3. **Architecture self-confirmation bias:** M11 must be allowed to reject/modify the Hierarchical Policy Portfolio if simpler baselines perform as well with less complexity.
4. **Historical evidence incompleteness:** real cases may lack reconstructable decision-time context; do not fill gaps using later knowledge.
5. **Hindsight leakage:** the biggest benchmark validity risk; outcome/post-decision evidence must be structurally inaccessible to arms.
6. **Small-sample calibration abuse:** do not claim calibration from a handful of cases; preserve raw forecasts first.
7. **Reviewer noise/bias:** blind/randomize where feasible and retain disagreement.
8. **Model drift:** model/provider versions can change baseline behavior; manifests must preserve exact versions/configuration.
9. **Semantic leakage from benchmark into ontology:** benchmark-local contracts must not silently become canonical business objects.
10. **Overengineering:** M11 is a bounded architecture-validation experiment, not permission to build a full production cognition platform before evidence.

---

## 16. Next five actions

### 1. Reconcile PR #4 with current `main`

Rebase/merge current main changes into `workstream/ecr-first-session-v0.1`, resolve conflicts using ADR-003 and current governance as authority, rerun artifact consistency checks, and update PR #4 description to reflect the completed research + accepted architecture + benchmark phase.

### 2. Start Issue #11

Implement benchmark-local contracts and synthetic fixture validation first. This is the dependency root for the remaining harness.

### 3. Parallelize Issues #12–#15 after #11 stabilizes

Build leakage protection, baseline arms, scoring, and blind review/reporting as independent Codex tasks where dependencies allow.

### 4. Begin historical case discovery for Issue #19

Coordinate with Evidence/Data to inventory candidate Bid/No-Bid cases now, but only promote them to accepted benchmark fixtures after #11/#12 contracts and leakage validation are operational.

### 5. Implement Issue #20 and run the first comparative M11 benchmark

Once the common arm interface is stable, implement the modular routed cognition arm under ADR-003 and compare it against LLM-only + static-scorecard + reconstructed-human baselines on identical cases. Use the results to keep, modify, or challenge the working architecture.

---

## 17. Fresh-agent continuation instruction

Do **not** restart Research 001 or rebuild the literature map.

Start by reading:

1. `AGENTS.md`;
2. ECR role charter;
3. ADR-003;
4. R001-14 final synthesis;
5. R001-15 benchmark validation;
6. R001-16 execution plan;
7. this transition brief;
8. issues #11–#15, #19, #20;
9. current PR #4/main divergence.

Then continue at the **TASK / BUILD / VERIFY** phase.

Additional research is justified only by a specific unresolved benchmark/implementation question and must obey benchmark-first repository law.
