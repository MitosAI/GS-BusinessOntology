# Executive Cognition Human Review and Reporting

The benchmark uses blind human review for judgment dimensions that automated
metrics cannot establish. Review packet generation and reconciliation are
benchmark-local; they do not change canonical decision, identity, audit,
security, or authority semantics.

## Artifact separation

Packet generation emits three distinct artifacts:

1. `packet_metadata` validates against `HumanReviewPacket` and records the case,
   rubric version, blind result references, seed digest, and generation time.
2. `reviewer_packet` contains the case material, rubric, and neutral candidate
   labels. It excludes run IDs, arm IDs, result IDs, timestamps, result digests,
   and method traces because those fields can reveal the producing arm.
3. `reconciliation` is held away from reviewers. It maps blind labels to exact
   run, arm, and result references and protects that mapping with a digest.

The randomization seed is recorded only in the reconciliation artifact. The
review packet records a case-bound digest of that seed so a packet can be
reproduced and audited without disclosing the assignment during review.

## Review capture

Every response records a unique review ID, blind result ID, reviewer identity
and version, rubric version, a rating for every rubric dimension, comments, and
submission time. Reconciliation rejects unknown labels, mapping tampering,
rubric-version mismatch, partial ratings, out-of-range values, duplicate review
IDs, and duplicate reviewer assignments.

Reviewer disagreement is retained as the original reviewer/rating pairs plus
the mean and range. A mean is descriptive, not an automatic resolution or a
replacement for the underlying judgments.

## Reporting

The report generator emits:

- validated `BenchmarkReport` metadata with exact case, run, metric, packet,
  and raw-artifact references;
- per-case machine metrics, human reviews, disagreement, and failure examples;
- aggregate metric rows grouped by their original metric identities;
- aggregate human-review disagreement rows;
- a raw machine-readable export containing manifests and uncollapsed results.

`composite_score` is explicitly null. Process quality, forecast quality,
operational performance, human judgment, execution, and realized outcomes must
remain separately inspectable.
