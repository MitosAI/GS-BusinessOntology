# R001-A — Executive Cognition Discipline and Source Map

**Version:** v0.1  
**Status:** First-session research artifact; provisional synthesis  
**Owner:** Executive Cognition Research Lead (ECR-001)  
**Program:** GenSigma AI-Native Operating System  
**Research charter:** `docs/research/RESEARCH-001-COMPUTATIONAL-EXECUTIVE-JUDGMENT-CHARTER-v0.1.md`

---

## 1. Purpose

This artifact executes the first-session requirement to build a source map, identify 3–5 canonical sources per required discipline, and synthesize what each discipline can contribute to computational executive judgment.

This is not a literature dump and it is not a final architecture decision. It identifies the intellectual tools that appear useful, their limits, and where they fit GenSigma decision classes.

Current terminology follows the owner-confirmed Knowledge/Ontology direction:

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
OUTCOME / LEARNING
```

`World Model` is treated as legacy repository terminology, not the current abstraction.

---

## 2. Evidence labels used in this workstream

- **Established** — directly grounded in canonical/peer-reviewed theory, official doctrine, or strong empirical research.
- **Applied inference** — a defensible translation of established work into the GenSigma setting.
- **Architecture hypothesis** — a design proposal requiring Chief Architect reconciliation and later empirical validation.

---

## 3. Canonical source map

### 3.1 Normative decision theory / decision analysis

1. **Ronald A. Howard (1988), “Decision Analysis: Practice and Promise,” Management Science 34(6), 679–695.** DOI: https://doi.org/10.1287/mnsc.34.6.679  
   Why it matters: prescriptive decision analysis, explicit separation of normative and descriptive views, decision framing, alternatives, values, uncertainty, influence diagrams, risk attitude and decision quality.

2. **Ralph L. Keeney & Howard Raiffa (1993 Cambridge edition; original 1976), _Decisions with Multiple Objectives: Preferences and Value Trade-Offs_.** DOI: https://doi.org/10.1017/CBO9781139174084  
   Why it matters: objective structuring, multiattribute value/utility, tradeoffs, uncertainty, preferences over time and multi-objective executive choices.

3. **Leonard J. Savage (1954; 2nd revised ed. 1972), _The Foundations of Statistics_.**  
   Why it matters: subjective probability, utility, the sure-thing principle and coherent choice under uncertainty.

4. **John von Neumann & Oskar Morgenstern (1944), _Theory of Games and Economic Behavior_.**  
   Why it matters: expected-utility foundations and strategic choice; foundational but not a complete model of real executive judgment.

### 3.2 Bayesian decision theory / belief updating

1. **James O. Berger (1985), _Statistical Decision Theory and Bayesian Analysis_, 2nd ed.** DOI: https://doi.org/10.1007/978-1-4757-4286-2  
   Why it matters: loss/utility, subjective probability, Bayesian analysis, minimax methods and sequential analysis.

2. **Morris H. DeGroot (1970; Wiley Classics 2004), _Optimal Statistical Decisions_.** DOI: https://doi.org/10.1002/0471729000  
   Why it matters: rigorous Bayesian and sequential decision problems and statistical decision rules.

3. **Howard Raiffa & Robert Schlaifer (1961), _Applied Statistical Decision Theory_.**  
   Why it matters: operational use of utility, subjective probability, sampling and value of information.

4. **Leonard J. Savage, _The Foundations of Statistics_.**  
   Why it matters: axiomatic foundation for personal probability and Bayesian decision behavior.

### 3.3 Operations research / optimization

1. **MIT OpenCourseWare 15.053, _Optimization Methods in Management Science_.** https://ocw.mit.edu/courses/15-053-optimization-methods-in-management-science-spring-2013/  
   Why it matters: linear programming, network optimization, integer programming and decision-tree applications in management.

2. **MIT OpenCourseWare 15.093J, _Optimization Methods_.** https://ocw.mit.edu/courses/15-093j-optimization-methods-fall-2009/  
   Why it matters: linear, network, discrete, nonlinear and dynamic optimization plus optimal control.

3. **Alexander Shapiro, Darinka Dentcheva & Andrzej Ruszczyński, _Lectures on Stochastic Programming: Modeling and Theory_.** DOI: https://doi.org/10.1137/1.9781611976595  
   Why it matters: formal optimization when uncertain quantities materially affect feasible or preferred choices.

4. **Frederick S. Hillier & Gerald J. Lieberman, _Introduction to Operations Research_.**  
   Why it matters: broad operations-research toolkit covering optimization, networks, queueing, simulation and decision analysis.

### 3.4 Game theory / strategic interaction

1. **Martin J. Osborne & Ariel Rubinstein (1994), _A Course in Game Theory_.** MIT Press.  
   Why it matters: strategic, extensive-form, imperfect-information and coalition models; strong conceptual foundation for interacting decision makers.

2. **Drew Fudenberg & Jean Tirole (1991), _Game Theory_.** MIT Press.  
   Why it matters: repeated games, Bayesian games, incomplete information, reputation and bargaining.

3. **Roger B. Myerson, _Game Theory: Analysis of Conflict_.** Harvard University Press.  
   Why it matters: strategic/extensive-form games, Bayesian games, cooperative and noncooperative analysis.

4. **John F. Nash Jr. (1950), “The Bargaining Problem,” Econometrica 18(2), 155–162.** DOI: https://doi.org/10.2307/1907266  
   Why it matters: explicit bargaining solution concepts and negotiated value division.

### 3.5 Control theory / feedback systems

1. **Karl J. Åström & Richard M. Murray (2008), _Feedback Systems: An Introduction for Scientists and Engineers_.** Caltech / Princeton University Press. https://authors.library.caltech.edu/records/yzs24-xsx88  
   Why it matters: state-space models, feedback, stability, robustness and control-system design.

2. **R. E. Kalman (1960), “A New Approach to Linear Filtering and Prediction Problems,” Journal of Basic Engineering 82(1), 35–45.** DOI: https://doi.org/10.1115/1.3662552  
   Why it matters: state estimation under noisy observation; useful conceptual foundation for separating observed signals from estimated state.

3. **James B. Rawlings, David Q. Mayne & Moritz M. Diehl (2026), _Model Predictive Control: Theory, Computation, and Design_, 2nd ed.** https://sites.engineering.ucsb.edu/~jbraw/mpc/  
   Why it matters: receding-horizon control, constraints, forecasts and repeated replanning as new information arrives.

4. **Dimitri P. Bertsekas (2017/2012), _Dynamic Programming and Optimal Control_, 4th ed.** https://athenasc.com/dpbook.html  
   Why it matters: sequential decision making, dynamic programming, Markov decision problems and optimal control.

### 3.6 Behavioral decision science / bounded rationality

1. **Herbert A. Simon (1955), “A Behavioral Model of Rational Choice,” Quarterly Journal of Economics 69(1), 99–118.** DOI: https://doi.org/10.2307/1884852  
   Why it matters: bounded rationality and satisficing challenge unrealistic assumptions of unlimited computation/information.

2. **Amos Tversky & Daniel Kahneman (1974), “Judgment under Uncertainty: Heuristics and Biases,” Science 185(4157), 1124–1131.** DOI: https://doi.org/10.1126/science.185.4157.1124  
   Why it matters: representativeness, availability and anchoring as systematic sources of judgment error.

3. **Daniel Kahneman & Amos Tversky (1979), “Prospect Theory: An Analysis of Decision under Risk,” Econometrica 47(2), 263–292.** DOI: https://doi.org/10.2307/1914185  
   Why it matters: descriptive treatment of loss aversion, reference dependence and nonlinear weighting of probabilities.

4. **Katherine Milkman, Dolly Chugh & Max Bazerman (2009), “How Can Decision Making Be Improved?” Perspectives on Psychological Science 4(4), 379–383.** DOI: https://doi.org/10.1111/j.1745-6924.2009.01142.x  
   Why it matters: moves from bias cataloging toward decision-process improvement and debiasing.

### 3.7 Strategic management / executive decision practice

1. **Henry Mintzberg, Duru Raisinghani & André Théorêt (1976), “The Structure of ‘Unstructured’ Decision Processes,” Administrative Science Quarterly 21(2), 246–275.** DOI: https://doi.org/10.2307/2392045  
   Why it matters: empirical study showing that nonroutine strategic decisions have discoverable phases/routines despite appearing unstructured.

2. **Kathleen M. Eisenhardt (1989), “Making Fast Strategic Decisions in High-Velocity Environments,” Academy of Management Journal 32(3), 543–576.** DOI: https://doi.org/10.2307/256434  
   Why it matters: empirical evidence that faster strategic decision teams used more information, more alternatives, structured advice and active conflict resolution.

3. **Paul C. Nutt (2002), _Why Decisions Fail_.**  
   Why it matters: applied synthesis based on a large sample of strategic decisions, emphasizing failure-prone decision tactics and process design.

4. **Daniel Kahneman, Dan Lovallo & Olivier Sibony (2011), “Before You Make That Big Decision…,” Harvard Business Review.**  
   Why it matters: practical decision hygiene/checklist approach for challenging bias in consequential executive proposals.

### 3.8 AI reasoning, planning and sequential decision making

1. **Stuart Russell & Peter Norvig (2020), _Artificial Intelligence: A Modern Approach_, 4th ed.** https://aima.eecs.berkeley.edu/  
   Why it matters: search, planning, constraint satisfaction, uncertainty, decision theory, multiagent decisions and reinforcement learning in one coherent AI reference.

2. **Richard S. Sutton & Andrew G. Barto (2018), _Reinforcement Learning: An Introduction_, 2nd ed.** MIT Press.  
   Why it matters: sequential decision making, reward, MDPs, dynamic programming and learning from interaction.

3. **Leslie P. Kaelbling, Michael L. Littman & Anthony R. Cassandra (1998), “Planning and Acting in Partially Observable Stochastic Domains,” Artificial Intelligence 101, 99–134.** DOI: https://doi.org/10.1016/S0004-3702(98)00023-X  
   Why it matters: formal treatment of acting when underlying state is uncertain and only partially observed.

4. **Shunyu Yao et al. (2023), “ReAct: Synergizing Reasoning and Acting in Language Models,” ICLR 2023.** https://arxiv.org/abs/2210.03629  
   Why it matters: demonstrates a useful role for language models as interleaved reasoners/tool users, without implying that language modeling itself supplies governance or formal optimality.

5. **Karthik Valmeekam, Kaya Stechly & Subbarao Kambhampati (2024), “LLMs Still Can’t Plan; Can LRMs? A Preliminary Evaluation of OpenAI’s o1 on PlanBench.”** https://arxiv.org/abs/2409.13373  
   Why it matters: evidence that improved language-model reasoning still does not remove planning reliability, efficiency and guarantee concerns.

### 3.9 Military command and control / OODA / after-action learning

1. **John R. Boyd, _A Discourse on Winning and Losing_ / “The Essence of Winning and Losing” (1995 synthesis), Air University Press archive.** https://www.airuniversity.af.edu/Portals/10/AUPress/Books/B_0151_Boyd_Discourse_Winning_Losing.pdf  
   Why it matters: OODA emphasizes orientation, adaptation, tempo and continuous interaction rather than a one-shot decision function.

2. **U.S. Army, ADP 6-0, _Mission Command: Command and Control of Army Forces_ (2019).**  
   Why it matters: commander’s intent, shared understanding, disciplined initiative, delegated authority, competence, trust and risk acceptance.

3. **Joint Chiefs of Staff, JP 5-0, _Joint Planning_.** https://www.jcs.mil/Doctrine/Joint-Doctrine-Pubs/5-0-Planning-Series/  
   Why it matters: structured planning under uncertainty while preserving commander judgment rather than replacing it with procedure.

4. **U.S. Army, TC 7-0.1, _After Action Reviews_ (2025).**  
   Why it matters: explicit learning loop comparing intended versus actual performance and turning outcomes into performance improvement rather than narrative hindsight.

---

## 4. Discipline map

| Discipline | Core contribution | Strongest GenSigma use | Primary failure mode | Likely computational role |
|---|---|---|---|---|
| Normative decision theory | Objectives, values, alternatives, consequences, tradeoffs, risk | Bid/no-bid, capital allocation, market entry, partner selection | False precision; assuming stable/elicitable preferences | Decision framing, criteria, utility/value models, sensitivity |
| Bayesian decision theory | Coherent belief updating from evidence | Win probability, delivery risk, availability, forecast updates | Invented priors/likelihoods; nonstationarity; correlated evidence | Belief models where evidence supports calibration; value of information |
| Operations research | Optimal choice under explicit objectives/constraints | Staffing, scheduling, allocation, pricing subproblems, portfolio allocation | Optimizing the wrong objective; omitted qualitative constraints | LP/MIP/nonlinear/stochastic optimization; simulation |
| Game theory | Strategic interaction among adaptive actors | Pricing/negotiation, teaming, competitive response, bargaining | Fragile assumptions about rationality, payoffs and beliefs | Activated selectively when other actors’ response changes option ranking |
| Control theory | State estimation, feedback, stability, correction, timescale | KPI correction, execution monitoring, adaptive resource control | Treating a business as a stationary engineered plant; wrong setpoint | Feedback architecture, state estimation, receding-horizon replanning |
| Behavioral science | Bias, bounded rationality, debiasing and decision hygiene | All consequential human-in-the-loop decisions | Descriptive models can be mistaken for prescriptions | Bias checks, premortems, reference-class prompts, process controls |
| Strategic management | How real nonroutine executive decisions are formed and executed | Market entry, strategy, organizational bets, executive review | Less formal; context dependence; weaker guarantees | Process design, alternative generation, conflict handling, escalation |
| AI reasoning/planning | Search, planning, partial observability, tool use, hypothesis generation | Unstructured evidence, option generation, model orchestration | Hallucination, brittle planning, poor calibration, weak guarantees | Interpreter/orchestrator, search assistant, hypothesis/alternative generator |
| C2 / OODA | Intent, delegated authority, tempo, adaptation, after-action learning | Delegated agent decisions, exception handling, operating cadence | Military assumptions do not transfer literally to business | Authority envelopes, intent propagation, fast/slow loops, learning discipline |

---

## 5. What appears established

### 5.1 Executive judgment is not one mathematical function

**Established across disciplines:** different problem structures call for different methods. Optimization requires explicit objective/constraints; Bayesian decisions require defensible probabilistic structure; game-theoretic analysis requires strategic interaction; strategic decisions often begin under incomplete framing and require search for alternatives.

**Applied inference:** a universal `decide()` algorithm is unlikely to be the correct GenSigma abstraction.

### 5.2 Objectives and beliefs must remain distinct

Normative decision theory separates preferences/utility from uncertainty about the world. This maps strongly to the existing GenSigma separation between Business Intent and descriptive Business/External Reality.

**Applied inference:** the Decision Engine should not learn “what GenSigma wants” merely by observing historical behavior. Intent and risk appetite remain governed inputs.

### 5.3 Quantitative rigor is conditional, not universal

Formal methods are powerful when their assumptions and inputs are defensible. They create false precision when probabilities, objectives, causal structure or feasible alternatives are invented to satisfy a mathematical form.

**Applied inference:** the system needs a method-selection discipline and an explicit ability to say `unknown`, `qualitative only`, or `insufficient evidence for probability`.

### 5.4 Decision process quality is separable from outcome quality

A good decision can have a bad stochastic outcome; a poor decision can get lucky. Decision analysis and after-action doctrine both imply that learning should inspect the information, assumptions, options and reasoning available at decision time rather than simply rewarding winners.

**Applied inference:** GenSigma must persist ex-ante expectations and assumptions, not only the final Decision and later Outcome.

### 5.5 Fast does not mean shallow

Eisenhardt’s high-velocity study found that faster teams used more information and more alternatives, not less, and relied on structured advice/conflict resolution.

**Applied inference:** executive-cognition speed should come from pre-structured state, parallel analysis and reusable decision policies, not from skipping evidence or collapsing alternatives.

### 5.6 Delegated autonomy requires intent and authority boundaries

Mission-command doctrine emphasizes clear intent, shared understanding, competence, delegated initiative and explicit risk acceptance.

**Applied inference:** agent autonomy should be an authority envelope governed by decision class, risk, scope and action permissions—not a binary autonomous/non-autonomous switch.

---

## 6. First cross-discipline synthesis

The strongest first hypothesis is a **policy portfolio for executive judgment**:

```text
DECISION CONTEXT
      |
      v
FRAME + BUILD SITUATION
      |
      v
CHECK HARD CONSTRAINTS / AUTHORITY
      |
      v
GENERATE / RETRIEVE ALTERNATIVES
      |
      v
SELECT METHODS BY DECISION CLASS
      |
      +--> deterministic rules
      +--> probabilistic / Bayesian analysis
      +--> optimization / OR
      +--> simulation / scenario analysis
      +--> strategic-interaction model
      +--> structured qualitative judgment
      +--> LLM interpretation / generation / orchestration
      |
      v
SENSITIVITY + DEBIAS / CHALLENGE
      |
      v
RECOMMENDATION
      |
      v
DECISION / APPROVAL
      |
      v
GOVERNED ACTION
      |
      v
OUTCOME / LEARNING
```

This is an **architecture hypothesis**, not yet canonical.

---

## 7. Implications for GenSigma Research 001

1. Continue with a modular decision architecture rather than searching for one dominant theory.
2. Treat explicit probabilities as earned representations; do not force probability where only ordinal/qualitative uncertainty is defensible.
3. Treat optimization as a solver for formal subproblems after intent and constraints are made explicit.
4. Activate strategic-interaction analysis only when a customer, partner, competitor, employee, regulator or other actor can materially adapt to GenSigma’s action.
5. Use control concepts primarily for feedback, state estimation, timescale separation and receding-horizon correction—not as a metaphor that turns the entire company into one control system.
6. Build debiasing into the decision process rather than attempting to reproduce human executive cognition literally.
7. Use LLMs primarily for unstructured interpretation, hypothesis/alternative generation, qualitative synthesis and tool/model orchestration.
8. Preserve human authority for strategic-intent changes, high-stakes irreversible choices and decisions beyond delegated authority.
9. Evaluate decision quality using ex-ante information and process quality in addition to ex-post outcomes.

---

## 8. Research gaps for the next session

- Formal treatment of value of information and stopping rules for business decisions with deadlines.
- Causal inference versus prediction: when a forecast is insufficient for intervention choice.
- Real-options treatment of staged strategic bets and reversibility.
- Calibration methods for low-frequency executive forecasts.
- Multi-objective decision analysis when criteria are partly lexicographic/veto-based rather than compensatory.
- Decision-rights / delegation models that combine authority, risk class and action type.
- Empirical evaluation framework for comparing modular judgment against LLM-only and human baselines.

---

## 9. Current conclusion

No source reviewed supports the proposition that high-quality executive judgment should be implemented as a single LLM prompt chain, a Bayes-everywhere model, a universal utility maximizer, or a generic optimization problem.

The evidence instead supports a **composite, decision-class-sensitive executive judgment capability** whose formal methods are selected according to problem structure, whose inputs remain traceable to governed Business Intent / Business Reality / External Reality / Capability, and whose outputs remain subject to authority, action and learning semantics.
