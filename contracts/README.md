# GenSigma Operational Ontology Contracts

This directory is the executable semantic contract for Build Spec 001.

It is intentionally technology-neutral. It does **not** choose the production database, graph engine, vector store, cloud topology, agent framework, or application runtime.

## Governing truths

1. Preserve truth.
2. Allow correction.
3. Keep the core stable.
4. Make boundaries explicit.

## Structure

```text
contracts/
  schemas/
    kernel/        shared semantic primitives
    business/      V1 business object contracts
  api/             logical OpenAPI contract
  fixtures/        multi-domain validation fixtures
  tests/           acceptance manifest
```

## Kernel rule

Every business object composes the common kernel contracts for:

- canonical identity and semantic type/version;
- effective/source/recorded/discovered time;
- aliases and source mappings;
- epistemic status;
- provenance;
- security;
- audit/correction/supersession;
- typed relationships;
- cross-model references.

Domain schemas must not redefine these semantics independently.

## Status

This package is an executable semantic baseline, not a persistence schema. Fields should not be interpreted as relational columns, graph labels, indexes, partitions, or physical keys.

See `docs/workstreams/koe/12-CODEX-BUILD-001-BRIEF-v0.1.md` for the implementation brief.
