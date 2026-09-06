# Open Semantic Questions

These questions are intentionally unresolved. Implementations must not choose silently.

## Q1 — Risk ownership split

Should V1 keep one managed `Risk` object owned by Executive Judgment with Business Reality references, or later split into:

- durable operational `RiskRecord` in Business Reality; and
- time/version-specific `RiskAssessment` in Executive Judgment?

**Current rule:** keep one `Risk` object plus separate `Assessment` resources. Do not add a second risk type yet.

## Q2 — Outcome split

Should V1 later distinguish:

- operational observed outcome; and
- strategic learning/impact outcome?

**Current rule:** one `Outcome` contract with explicit type/scope/measurement and cross-model ownership. Do not create duplicate outcome identities yet.

## Q3 — Offering instance/configuration

Do customer-specific implementations require an `OfferingInstance`/configuration object distinct from canonical Business Intent `Offering`?

**Current rule:** use Proposal/Agreement/Project configuration and references to canonical Offering. Admit a new object only if independent lifecycle/query/action requirements emerge.

## Q4 — Claim subsystem ownership

Should `Claim` ultimately be owned by a separate Knowledge/Evidence subsystem rather than the shared semantic kernel?

**Current rule:** treat Claim as a first-class shared-kernel knowledge resource with model-owner `shared_kernel`.

## Q5 — Cross-model contract distribution

Will the long-term physical architecture expose separate model services or one logical contract with multiple model-owned projections?

**Current rule:** semantic ownership is independent of deployment. Do not infer service boundaries from model boundaries.
