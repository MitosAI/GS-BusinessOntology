# R001 — Real Options and Staged Commitment

**Status:** Research output; architecture implications are provisional until Chief Architect review.

## Core finding

Executive decisions with uncertainty, irreversibility, and an ability to delay or stage commitment should not be modeled only as `act now` versus `do nothing`. Waiting, piloting, sequencing, and preserving exit options can have economic value.

Dixit and Pindyck's real-options framing is directly relevant: irreversible commitments made under uncertainty carry an option value of waiting when new information can arrive before commitment. This does not mean indefinite delay is optimal; delay also has opportunity cost.

Canonical sources:
- Avinash Dixit & Robert Pindyck, *Investment under Uncertainty* (Princeton University Press, 1994).
- Robert Pindyck, "Irreversibility, Uncertainty, and Investment," NBER Working Paper 3307 / Journal of Economic Literature, 1990/1991.

## Decision pattern

```text
uncertain opportunity
   |
   +--> commit fully now
   +--> reject
   +--> wait for information
   +--> run bounded experiment
   +--> stage commitment
   +--> buy/retain an option to expand later
```

The computational question is not merely expected value. It is:

> What action maximizes value while accounting for information arrival, reversibility, downside exposure, timing cost, and future choice?

## Real-option features to detect

A decision is a strong candidate for staged-commitment reasoning when several of these are true:

- commitment is materially irreversible or costly to unwind;
- uncertainty is high and may resolve over time;
- delaying preserves future choice;
- a small initial commitment can reveal information;
- expansion, abandonment, switching, or deferral are feasible;
- downside is asymmetric;
- future opportunities depend on current commitment.

## GenSigma applications

### Market entry
Instead of `enter / do not enter`, evaluate:
- monitor only;
- obtain registration/vehicle first;
- hire fractional/local capacity;
- pursue one anchor opportunity;
- establish full operating presence only after evidence threshold.

### New AI offering
Instead of building a full practice:
- sell discovery first;
- run a paid pilot;
- package repeated capability only after demand evidence.

### Hiring
Instead of permanent headcount immediately:
- contractor/fractional role;
- fixed-duration trial where lawful and appropriate;
- hire after demand/capacity threshold.

### Partner commitment
Use nonexclusive or opportunity-specific collaboration before broad exclusivity where uncertainty remains material.

## Provisional decision variables

A staged-decision analysis may need:
- current expected payoff;
- downside at risk;
- sunk/irreversible cost;
- delay cost;
- information expected to arrive;
- probability adequacy of that information model;
- cost of experiment;
- abandonment/switching cost;
- expansion value;
- deadline / option expiry;
- path dependencies created by each stage.

These are research requirements, not a canonical schema proposal.

## Rule for the Decision Engine proposal

When a decision is highly irreversible and uncertainty is material, the engine SHOULD explicitly search for **staged alternatives** before comparing final choices.

An LLM can generate candidate stages, but valuation, constraints, and thresholds should use deterministic or quantitative tools when defensible.

## Interaction with value of information

Real options and VOI are coupled:
- VOI asks whether additional information can improve the choice.
- Real options ask whether we can preserve choice until that information arrives.

The best executive move may therefore be neither `yes` nor `no`, but `small yes now, larger decision later`.

## Failure modes

- treating delay as free;
- using real-options language without a real mechanism for future information or flexibility;
- inventing precise option valuations when probabilities/cash-flow distributions are weak;
- allowing endless experimentation to substitute for strategic commitment;
- ignoring competitive pre-emption or deadlines.

## Architecture implication

The Decision Engine should be capable of representing **staged alternatives and contingent follow-on decisions**. Whether this becomes a new shared semantic structure is an `ASK_ARCHITECT` matter; the research finding itself is LOCAL_SOLVE.
