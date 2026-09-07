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

Temporal as-of reads and security-scoped traversal remain explicitly pending
until their runtime contracts are executable.
