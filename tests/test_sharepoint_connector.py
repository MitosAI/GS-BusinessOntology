from __future__ import annotations

from collections.abc import Mapping
from datetime import datetime, timezone

import pytest

from gensigma_connectors.graph import GraphClient, GraphHttpResponse, InMemoryCheckpointStore
from gensigma_connectors.sharepoint import (
    SharePointDeltaSensor,
    SharePointScope,
    SharePointSensorConfig,
    SharePointSensorError,
)


FINAL = "https://graph.microsoft.com/v1.0/drives/drive-1/root/delta?$deltatoken=final"


class FakeTransport:
    def __init__(self, responses: list[GraphHttpResponse]) -> None:
        self.responses = iter(responses)
        self.requests: list[tuple[str, str, Mapping[str, str]]] = []

    def request(self, method: str, url: str, headers: Mapping[str, str]) -> GraphHttpResponse:
        self.requests.append((method, url, headers))
        return next(self.responses)


def response(status: int, body: Mapping[str, object], headers: Mapping[str, str] | None = None) -> GraphHttpResponse:
    return GraphHttpResponse(status, headers or {}, body)


def file_item(**updates: object) -> dict[str, object]:
    value: dict[str, object] = {
        "id": "item-1",
        "name": "proposal.pdf",
        "size": 1024,
        "eTag": '"etag-1"',
        "cTag": '"ctag-1"',
        "createdDateTime": "2026-09-01T00:00:00Z",
        "lastModifiedDateTime": "2026-09-02T00:00:00Z",
        "createdBy": {"user": {"id": "user-1", "displayName": "Author"}},
        "lastModifiedBy": {"user": {"id": "user-2", "displayName": "Editor"}},
        "parentReference": {"path": "/drives/drive-1/root:/Proposals"},
        "file": {"mimeType": "application/pdf", "hashes": {"quickXorHash": "abc", "sha256Hash": "unsupported"}},
        "sharepointIds": {"siteId": "site-1", "listId": "library-1", "listItemId": "7"},
        "webUrl": "https://tenant.sharepoint.com/Proposals/proposal.pdf",
        "content": "must-not-enter-envelope",
    }
    value.update(updates)
    return value


def scope(drive_id: str = "drive-1") -> SharePointScope:
    return SharePointScope("site-1", drive_id, "library-1", ("m365-acl:library-1",))


def sensor(transport: FakeTransport, store: InMemoryCheckpointStore | None = None, scopes: tuple[SharePointScope, ...] | None = None, **client_kwargs: object) -> tuple[SharePointDeltaSensor, InMemoryCheckpointStore]:
    checkpoints = store or InMemoryCheckpointStore()
    graph = GraphClient(
        token_provider=lambda: "secret-access-token",
        transport=transport,
        sleep=lambda _: None,
        correlation_id_factory=lambda: "corr-123",
        **client_kwargs,
    )
    return SharePointDeltaSensor(
        graph=graph,
        checkpoint_store=checkpoints,
        config=SharePointSensorConfig("tenant-1", scopes or (scope(),)),
        clock=lambda: datetime(2026, 9, 6, tzinfo=timezone.utc),
    ), checkpoints


def test_allowlist_is_explicit_nonempty_and_unique() -> None:
    with pytest.raises(ValueError, match="at least one"):
        SharePointSensorConfig("tenant-1", ())
    with pytest.raises(ValueError, match="repeat"):
        SharePointSensorConfig("tenant-1", (scope(), scope()))
    with pytest.raises(ValueError, match="source_acl_refs"):
        SharePointScope("site-1", "drive-1", "library-1", ())


def test_rejects_runtime_scope_outside_allowlist() -> None:
    sharepoint, _ = sensor(FakeTransport([]))
    with pytest.raises(ValueError, match="allowlist"):
        sharepoint.sync_scope(scope("drive-not-allowed"), ingestion_run_id="run-1")


def test_follows_opaque_pagination_and_emits_file_metadata_security_and_hash() -> None:
    next_link = "https://graph.microsoft.com/v1.0/opaque?$skiptoken=do%2Bnot%2Fparse"
    transport = FakeTransport([
        response(200, {"value": [], "@odata.nextLink": next_link}),
        response(200, {"value": [file_item()], "@odata.deltaLink": FINAL}),
    ])
    sharepoint, store = sensor(transport)

    result = sharepoint.sync(ingestion_run_id="run-2")

    assert transport.requests[1][1] == next_link
    assert store.get("sharepoint:tenant-1:site-1:drive:drive-1") == FINAL
    envelope = result.envelopes[0]
    assert envelope["object_kind"] == "file"
    assert envelope["source_container"] == "site-1/library-1/drive-1"
    assert envelope["source_version"] == '"etag-1"'
    assert envelope["content_hash"] == "quickxor:abc"
    assert envelope["metadata"]["path"].endswith("/Proposals/proposal.pdf")
    assert envelope["metadata"]["content_type"] == "application/pdf"
    assert envelope["metadata"]["created_by"]["id"] == "user-1"
    assert "sha256Hash" not in envelope["metadata"]["hashes"]
    assert "content" not in envelope["metadata"]
    assert envelope["security"]["allowed_principals_or_scopes"] == []
    assert envelope["security"]["source_acl_refs"][0] == "m365-acl:library-1"
    assert envelope["security"]["source_acl_refs"][1].endswith("/permissions")


def test_each_allowlisted_drive_has_its_own_checkpoint() -> None:
    scopes = (scope("drive-1"), SharePointScope("site-2", "drive-2", "library-2", ("m365-acl:library-2",)))
    final_two = "https://graph.microsoft.com/v1.0/drives/drive-2/root/delta?$deltatoken=final"
    transport = FakeTransport([
        response(200, {"value": [], "@odata.deltaLink": FINAL}),
        response(200, {"value": [], "@odata.deltaLink": final_two}),
    ])
    sharepoint, store = sensor(transport, scopes=scopes)

    result = sharepoint.sync(ingestion_run_id="run-3")

    assert len(result.checkpoint_keys) == 2
    assert store.get("sharepoint:tenant-1:site-1:drive:drive-1") == FINAL
    assert store.get("sharepoint:tenant-1:site-2:drive:drive-2") == final_two


def test_resume_uses_saved_opaque_delta_link() -> None:
    saved = "https://graph.microsoft.com/v1.0/drive/delta?$deltatoken=saved%2Fopaque"
    key = "sharepoint:tenant-1:site-1:drive:drive-1"
    store = InMemoryCheckpointStore()
    store.put(key, saved)
    transport = FakeTransport([response(200, {"value": [], "@odata.deltaLink": FINAL})])
    sharepoint, _ = sensor(transport, store)

    sharepoint.sync(ingestion_run_id="run-4")

    assert transport.requests[0][1] == saved
    assert store.get(key) == FINAL


def test_tombstones_and_duplicate_items_emit_once() -> None:
    deleted = {"id": "item-deleted", "deleted": {"state": "deleted"}}
    transport = FakeTransport([response(200, {"value": [deleted, deleted], "@odata.deltaLink": FINAL})])
    sharepoint, _ = sensor(transport)

    result = sharepoint.sync(ingestion_run_id="run-5")

    assert len(result.envelopes) == 1
    assert result.tombstone_count == 1
    assert result.envelopes[0]["change_type"] == "deleted"


def test_repeated_item_uses_last_delta_occurrence() -> None:
    transport = FakeTransport([
        response(200, {
            "value": [file_item(eTag='"etag-1"'), file_item(eTag='"etag-2"')],
            "@odata.deltaLink": FINAL,
        })
    ])
    sharepoint, _ = sensor(transport)

    result = sharepoint.sync(ingestion_run_id="run-last")

    assert len(result.envelopes) == 1
    assert result.envelopes[0]["source_version"] == '"etag-2"'


def test_replay_is_stable_and_sink_reports_duplicate() -> None:
    transport = FakeTransport([
        response(200, {"value": [file_item()], "@odata.deltaLink": FINAL}),
        response(200, {"value": [file_item()], "@odata.deltaLink": FINAL + "-2"}),
    ])
    sharepoint, _ = sensor(transport)
    seen: set[str] = set()

    def emit(envelope: Mapping[str, object]) -> bool:
        evidence_id = str(envelope["evidence_id"])
        if evidence_id in seen:
            return False
        seen.add(evidence_id)
        return True

    first = sharepoint.sync(ingestion_run_id="run-6", emit=emit)
    second = sharepoint.sync(ingestion_run_id="run-7", emit=emit)

    assert first.envelopes[0]["evidence_id"] == second.envelopes[0]["evidence_id"]
    assert second.emitted_count == 0
    assert second.duplicate_count == 1


@pytest.mark.parametrize("bad_item", [{}, {"id": "item-1"}, {"id": "item-1", "eTag": '"v1"'}])
def test_invalid_drive_item_does_not_advance_checkpoint(bad_item: Mapping[str, object]) -> None:
    store = InMemoryCheckpointStore()
    transport = FakeTransport([response(200, {"value": [bad_item], "@odata.deltaLink": FINAL})])
    sharepoint, _ = sensor(transport, store)

    with pytest.raises(SharePointSensorError) as captured:
        sharepoint.sync(ingestion_run_id="run-8")

    assert captured.value.metadata["category"] == "malformed_response"
    assert store.get("sharepoint:tenant-1:site-1:drive:drive-1") is None


def test_sink_failure_does_not_advance_checkpoint() -> None:
    store = InMemoryCheckpointStore()
    transport = FakeTransport([response(200, {"value": [file_item()], "@odata.deltaLink": FINAL})])
    sharepoint, _ = sensor(transport, store)

    with pytest.raises(RuntimeError, match="sink unavailable"):
        sharepoint.sync(ingestion_run_id="run-9", emit=lambda _: (_ for _ in ()).throw(RuntimeError("sink unavailable")))
    assert store.get("sharepoint:tenant-1:site-1:drive:drive-1") is None


@pytest.mark.parametrize("status,category", [(401, "auth"), (403, "permission"), (429, "throttled"), (503, "retry_exhausted"), (500, "terminal")])
def test_terminal_errors_are_structured_and_redacted(status: int, category: str) -> None:
    sensitive_link = "https://graph.microsoft.com/v1.0/drive/delta?$deltatoken=sensitive-state"
    store = InMemoryCheckpointStore()
    store.put("sharepoint:tenant-1:site-1:drive:drive-1", sensitive_link)
    transport = FakeTransport([response(status, {}, {"request-id": "server-1"})])
    sharepoint, _ = sensor(transport, store, max_attempts=1)

    with pytest.raises(SharePointSensorError) as captured:
        sharepoint.sync(ingestion_run_id="run-10")

    assert captured.value.metadata["category"] == category
    rendered = str(captured.value) + repr(captured.value.metadata)
    assert "secret-access-token" not in rendered
    assert "sensitive-state" not in rendered


def test_429_retries_using_graph_foundation() -> None:
    sleeps: list[float] = []
    transport = FakeTransport([
        response(429, {}, {"Retry-After": "2"}),
        response(200, {"value": [], "@odata.deltaLink": FINAL}),
    ])
    graph = GraphClient(token_provider=lambda: "secret", transport=transport, sleep=sleeps.append)
    sharepoint = SharePointDeltaSensor(
        graph=graph,
        checkpoint_store=InMemoryCheckpointStore(),
        config=SharePointSensorConfig("tenant-1", (scope(),)),
    )

    sharepoint.sync(ingestion_run_id="run-11")

    assert sleeps == [2.0]


def test_malformed_collection_is_rejected_and_envelope_is_noncanonical() -> None:
    malformed = FakeTransport([response(200, {"value": "not-an-array"})])
    sharepoint, _ = sensor(malformed)
    with pytest.raises(SharePointSensorError) as captured:
        sharepoint.sync(ingestion_run_id="run-12")
    assert captured.value.metadata["category"] == "malformed_response"

    valid = FakeTransport([response(200, {"value": [file_item()], "@odata.deltaLink": FINAL})])
    sharepoint, _ = sensor(valid)
    envelope = sharepoint.sync(ingestion_run_id="run-13").envelopes[0]
    required = {"evidence_id", "source_system", "source_record_id", "acquired_time", "security", "ingestion_run_id"}
    assert required <= envelope.keys()
    assert not any(key.startswith("canonical") for key in envelope)
