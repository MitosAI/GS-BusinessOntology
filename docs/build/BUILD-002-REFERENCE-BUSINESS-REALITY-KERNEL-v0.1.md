# Business Reality Reference Kernel v0.1

This is the first executable runtime slice of GenSigma OS Business Reality.

It deliberately does **not** choose the production database, graph engine, search stack, Azure topology, or agent framework. It exists to make the semantic contracts executable and to pressure-test the invariants before physical architecture is frozen.

## What this slice proves

- repository JSON Schema contracts can be loaded and enforced at runtime;
- raw evidence is append-oriented and replay-idempotent;
- source evidence cannot be silently overwritten;
- candidates must reference known evidence;
- canonical state enters through an explicit candidate-promotion path;
- every promotion retains the candidate and evidence lineage used to justify it;
- invalid business shapes are rejected by the semantic contracts;
- canonical corrections append a new interpretation while preserving prior history.

## Not in scope yet

- Outlook or SharePoint connectors;
- production persistence;
- graph versus relational choice;
- vector/semantic search;
- production authorization enforcement;
- automatic identity resolution;
- broad CRUD APIs;
- autonomous external-system writeback.

## Run

```bash
python -m pip install -e '.[test]'
pytest
```

The next increment should add typed relationships, temporal/as-of reads, security-context enforcement, and the first query-contract endpoints against the same kernel interface.
