import pytest

from gensigma_benchmarks import BenchmarkRunner, ReferenceAdapter, build_fixture


def run(scale: str) -> dict:
    fixture = build_fixture(scale)
    return BenchmarkRunner(ReferenceAdapter(fixture), fixture).run()


def test_small_baseline_is_reproducible() -> None:
    assert run("small") == run("small")


def test_scale_cardinalities_are_deterministic() -> None:
    assert run("tiny")["cardinality"] == {
        "identities": 3, "relationships": 2, "evidence": 2, "temporal_states": 2,
    }
    assert run("medium")["cardinality"] == {
        "identities": 75, "relationships": 50, "evidence": 50, "temporal_states": 50,
    }


def test_executable_and_pending_workloads_are_explicit() -> None:
    workloads = {item["name"]: item for item in run("small")["workloads"]}
    assert workloads["canonical_identity_lookup"]["status"] == "complete"
    assert workloads["typed_relationship_neighborhood"]["result_count"] == 10
    assert workloads["evidence_lineage"]["result_count"] == 10
    assert workloads["historical_as_of_read"]["status"] == "complete"
    assert workloads["historical_as_of_read"]["result_count"] == 5
    assert workloads["historical_as_of_read"]["digest"] is not None
    assert workloads["security_scoped_traversal"]["status"] == "pending"


def test_reference_temporal_adapter_uses_half_open_intervals() -> None:
    adapter = ReferenceAdapter(build_fixture("tiny"))
    assert adapter.get_state_as_of("opportunity-000", "2025-12-31T23:59:59Z") is None
    assert adapter.get_state_as_of("opportunity-000", "2026-06-30T23:59:59Z") == "proposed"
    assert adapter.get_state_as_of("opportunity-000", "2026-07-01T00:00:00Z") == "active"


def test_unknown_scale_fails_clearly() -> None:
    with pytest.raises(ValueError, match="unknown scale"):
        build_fixture("huge")
