from gensigma_benchmarks import BenchmarkRunner, ReferenceAdapter, build_fixture


def run(scale: str) -> dict:
    fixture = build_fixture(scale)
    return BenchmarkRunner(ReferenceAdapter(fixture), fixture).run()


def test_small_baseline_is_reproducible() -> None:
    assert run("small") == run("small")


def test_scale_cardinalities_are_deterministic() -> None:
    assert run("tiny")["cardinality"] == {
        "identities": 3,
        "relationships": 2,
        "evidence": 2,
    }
    assert run("medium")["cardinality"] == {
        "identities": 75,
        "relationships": 50,
        "evidence": 50,
    }


def test_executable_and_pending_workloads_are_explicit() -> None:
    workloads = {item["name"]: item for item in run("small")["workloads"]}
    assert workloads["canonical_identity_lookup"]["status"] == "complete"
    assert workloads["typed_relationship_neighborhood"]["result_count"] == 10
    assert workloads["evidence_lineage"]["result_count"] == 10
    assert workloads["historical_as_of_read"]["status"] == "pending"
    assert workloads["security_scoped_traversal"]["status"] == "pending"


def test_unknown_scale_fails_clearly() -> None:
    try:
        build_fixture("huge")
    except ValueError as error:
        assert "unknown scale" in str(error)
    else:
        raise AssertionError("expected ValueError")
