# Business Reality Workload Benchmark

This deterministic harness exercises the currently implemented portion of the
Build Spec 001 workload contract without selecting a production persistence
technology.

Run the default baseline:

```bash
python -m gensigma_benchmarks --scale small
```

Write machine-readable results:

```bash
python -m gensigma_benchmarks \
  --scale small \
  --output benchmarks/business-reality/baseline-small.json
```

Supported profiles are `tiny`, `small`, and `medium`. Measurements are stable
logical operation and result counts plus SHA-256 digests. They intentionally do
not use wall-clock timing, which belongs in later persistence-candidate runs.

Temporal as-of reads now execute against deterministic half-open validity
intervals in the reference adapter. Security-scoped traversal remains explicitly
pending until its runtime contract is executable.

The temporal workload is a logical correctness baseline, not a production
persistence recommendation. It verifies point-in-time adapter behavior while the
reference kernel separately verifies the contracted effective-time and
recorded-time modes.
