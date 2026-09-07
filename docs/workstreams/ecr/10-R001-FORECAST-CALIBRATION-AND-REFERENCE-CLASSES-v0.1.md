# R001 — Forecast Calibration and Reference Classes

**Status:** Research output; architecture implications are provisional until Chief Architect review.

## Core finding

If GenSigma uses probabilities, the system must evaluate whether those probabilities correspond to reality over time. Confidence language alone is insufficient.

Brier's probability score established a proper way to evaluate probabilistic forecasts. Gneiting and Raftery emphasize that good probabilistic forecasts should be **calibrated** while remaining as sharp/informative as possible. Reference-class forecasting provides an outside-view correction when inside-view estimates are vulnerable to optimism and uniqueness bias.

Canonical sources:
- Glenn W. Brier, "Verification of Forecasts Expressed in Terms of Probability," *Monthly Weather Review* 78(1), 1950.
- Tilmann Gneiting & Adrian E. Raftery, "Probabilistic Forecasts, Calibration and Sharpness," *JRSS B* 69(2), 2007.
- Bent Flyvbjerg, "From Nobel Prize to Project Management: Getting Risks Right," *Project Management Journal* 37(3), 2006.

## Proposed forecasting discipline

Every material numeric forecast should preserve:

```text
forecast question
forecast timestamp
resolution criterion
resolution date / horizon
forecast probability or distribution
forecast source/model/method
reference class, if any
information available at forecast time
later realized outcome
score / calibration result
```

This is a logical research requirement, not yet a canonical data model.

## Calibration rules

### Rule 1 — Probability must be earned
Do not force qualitative uncertainty into numeric form merely because an algorithm expects a number.

### Rule 2 — Use outside-view evidence where available
For repeated decision classes, historical distributions should constrain or challenge inside-view estimates.

Examples:
- GenSigma win rate for comparable opportunities;
- days-to-pay by customer/contract type;
- proposal effort by solicitation complexity;
- staffing lead time by skill class;
- project margin variance by delivery model.

### Rule 3 — Preserve forecast before outcome
Do not reconstruct probabilities after the fact. The ex-ante forecast must be immutable or versioned once the decision/action occurs.

### Rule 4 — Score forecasts at resolution
Binary probabilities can use Brier score. Distributional forecasts should use proper scoring rules appropriate to their form.

### Rule 5 — Separate calibration from discrimination/sharpness
A model that always predicts the base rate may be calibrated but not useful enough. A useful forecaster must also separate cases when evidence supports doing so.

## Reference-class hierarchy

When generating a forecast, search from the most specific class outward until sample adequacy becomes too weak:

```text
same customer + same solicitation family
-> same customer + similar service
-> same procurement vehicle/type
-> similar SLED customer + service
-> broader GenSigma opportunity class
-> external benchmark if internal evidence sparse
```

Do not choose a narrow class only because it produces a preferred probability.

## Small-sample rule

Executive decisions are often low-frequency. Therefore:
- expose sample size;
- avoid false certainty from tiny samples;
- use hierarchical pooling or qualitative ranges when appropriate;
- keep internal and external reference classes distinguishable;
- allow `not enough evidence to quantify` as a valid result.

## Forecast decomposition

A broad forecast such as `win probability = 62%` may hide distinct uncertainties. Where useful, decompose into drivers:
- eligibility/pass-fail;
- proposal quality;
- relationship position;
- partner strength;
- competitive field;
- price position;
- procurement uncertainty;
- execution capability.

But do not multiply weak subjective component probabilities as though the result were calibrated.

## GenSigma benchmark example — Bid/No-Bid

For each historical opportunity:
1. freeze evidence available by bid-decision date;
2. reconstruct or generate probability;
3. record bid/no-bid recommendation;
4. resolve award outcome where observable;
5. score probability forecasts separately from decision quality;
6. stratify by reference class;
7. inspect calibration bins and systematic optimism/pessimism.

## Architecture implication

A production Decision Engine should eventually support a **forecast registry + resolution loop**. This would allow probabilities to become empirically calibrated assets rather than persuasive prose.

Creating that as a shared interface or canonical semantic object is `ASK_ARCHITECT`; the requirement for calibration is a research conclusion.
