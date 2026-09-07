from __future__ import annotations

from collections.abc import Mapping
from datetime import datetime, timezone
from urllib.parse import parse_qs, urlparse

import pytest

from gensigma_connectors.graph import GraphHttpResponse, InMemoryCheckpointStore
from gensigma_connectors.outlook import (
    OutlookDeltaSensor,
    OutlookSensorConfig,
    OutlookSensorError,
    graph_client_for_outlook,
)


FINAL_INBOX = "https://graph.microsoft.com/v1.0/inbox/delta?$deltatoken=final-inbox"
FINAL_SENT = "https://graph.microsoft.com/v1.0/sent/delta?$deltatoken=final-sent"


class FakeTransport:
    def __init__(self, responses: list[GraphHttpResponse]) -> None:
        self.responses = iter(responses)
        self.requests: list[tuple[str, str, Mapping[str, str]]] = []

    def request(self, method: str, url: str, headers: Mapping[str, str]) -> GraphHttpResponse:
        self.requests.append((method, url, headers))
        return next(self.responses)


def response(status: int, body: Mapping[str, object], headers: Mapping[str, str] | None = None) -> GraphHttpResponse:
    return GraphHttpResponse(status, headers or {}, body)


def message(**updates: object) -> dict[str, object]:
    value: dict[str, object] = {
        "id": "immutable-message-1",
        "changeKey": "version-1",
        "internetMessageId": "<message@example.com>",
        "conversationId": "conversation-1",
        "conversationIndex": "AQHZ",
        "subject": "Proposal update",
        "sender": {"emailAddress": {"name": "Sender", "address": "sender@example.com"}},
        "from": {"emailAddress": {"name": "Sender", "address": "sender@example.com"}},
        "toRecipients": [{"emailAddress": {"name": "Recipient", "address": "recipient@example.com"}}],
        "ccRecipients": [],
        "bccRecipients": [],
        "createdDateTime": "2026-09-01T00:00:00Z",
        "lastModifiedDateTime": "2026-09-01T00:01:00Z",
        "sentDateTime": "2026-09-01T00:00:30Z",
        "receivedDateTime": "2026-09-01T00:00:31Z",
        "hasAttachments": True,
        "body": {"content": "must-not-enter-envelope"},
    }
    value.update(updates)
    return value


def attachment(**updates: object) -> dict[str, object]:
    value: dict[str, object] = {
        "id": "immutable-attachment-1",
        "name": "proposal.pdf",
        "contentType": "application/pdf",
        "size": 123,
        "isInline": False,
        "lastModifiedDateTime": "2026-09-01T00:01:00Z",
        "contentBytes": "must-not-enter-envelope",
    }
    value.update(updates)
    return value


def sensor(transport: FakeTransport, store: InMemoryCheckpointStore | None = None, **client_kwargs: object) -> tuple[OutlookDeltaSensor, InMemoryCheckpointStore]:
    checkpoints = store or InMemoryCheckpointStore()
    graph = graph_client_for_outlook(
        token_provider=lambda: "secret-access-token",
        transport=transport,
        sleep=lambda _: None,
        correlation_id_factory=lambda: "corr-123",
        **client_kwargs,
    )
    return OutlookDeltaSensor(
        graph=graph,
        checkpoint_store=checkpoints,
        config=OutlookSensorConfig(
            tenant_id="tenant-1",
            mailbox_id="evidence@example.com",
            source_acl_refs=("m365-acl:mailbox-1",),
        ),
        clock=lambda: datetime(2026, 9, 6, tzinfo=timezone.utc),
    ), checkpoints


def test_syncs_inbox_and_sent_with_opaque_paging_attachments_and_separate_checkpoints() -> None:
    next_link = "https://graph.microsoft.com/v1.0/opaque?$skiptoken=do%2Bnot%2Fparse"
    attachment_next = "https://graph.microsoft.com/v1.0/attachments?$skiptoken=opaque"
    transport = FakeTransport([
        response(200, {"value": [], "@odata.nextLink": next_link}),
        response(200, {"value": [message()], "@odata.deltaLink": FINAL_INBOX}),
        response(200, {"value": [], "@odata.nextLink": attachment_next}),
        response(200, {"value": [attachment()],}),
        response(200, {"value": [message(id="sent-1", changeKey="sent-v1", hasAttachments=False)], "@odata.deltaLink": FINAL_SENT}),
    ])
    outlook, store = sensor(transport)

    result = outlook.sync(ingestion_run_id="run-1")

    assert transport.requests[1][1] == next_link
    assert transport.requests[3][1] == attachment_next
    assert all(request[2]["Prefer"] == 'IdType="ImmutableId"' for request in transport.requests)
    assert store.get("outlook:tenant-1:evidence@example.com:folder:inbox") == FINAL_INBOX
    assert store.get("outlook:tenant-1:evidence@example.com:folder:sentitems") == FINAL_SENT
    assert [item["object_kind"] for item in result.envelopes] == ["message", "attachment", "message"]
    assert result.envelopes[1]["parent_evidence_id"] == result.envelopes[0]["evidence_id"]
    assert result.envelopes[0]["metadata"]["conversation_id"] == "conversation-1"
    assert result.envelopes[1]["metadata"]["content_type"] == "application/pdf"
    assert "body" not in result.envelopes[0]["metadata"]
    assert "contentBytes" not in result.envelopes[1]["metadata"]


def test_resume_uses_saved_opaque_link_and_commits_only_completed_delta_link() -> None:
    saved = "https://graph.microsoft.com/v1.0/saved?$deltatoken=opaque%2Fsecret"
    store = InMemoryCheckpointStore()
    key = "outlook:tenant-1:evidence@example.com:folder:inbox"
    store.put(key, saved)
    transport = FakeTransport([response(200, {"value": [], "@odata.deltaLink": FINAL_INBOX})])
    outlook, _ = sensor(transport, store)

    outlook.sync_folder("inbox", ingestion_run_id="run-2")

    assert transport.requests[0][1] == saved
    assert store.get(key) == FINAL_INBOX


def test_initial_delta_request_can_be_bounded_by_received_time() -> None:
    transport = FakeTransport(
        [response(200, {"value": [], "@odata.deltaLink": FINAL_INBOX})]
    )
    outlook, _ = sensor(transport)

    outlook.sync_folder(
        "inbox",
        ingestion_run_id="run-bounded",
        received_after=datetime(2026, 9, 1, 8, 30, tzinfo=timezone.utc),
    )

    query = parse_qs(urlparse(transport.requests[0][1]).query)
    assert query["$filter"] == ["receivedDateTime ge 2026-09-01T08:30:00Z"]
    assert query["$orderby"] == ["receivedDateTime desc"]


def test_saved_delta_link_remains_opaque_when_time_bound_is_supplied() -> None:
    saved = "https://graph.microsoft.com/v1.0/saved?$deltatoken=opaque%2Fstate"
    store = InMemoryCheckpointStore()
    key = "outlook:tenant-1:evidence@example.com:folder:inbox"
    store.put(key, saved)
    transport = FakeTransport(
        [response(200, {"value": [], "@odata.deltaLink": FINAL_INBOX})]
    )
    outlook, _ = sensor(transport, store)

    outlook.sync_folder(
        "inbox",
        ingestion_run_id="run-resume-bounded",
        received_after=datetime(2026, 9, 1, tzinfo=timezone.utc),
    )

    assert transport.requests[0][1] == saved


def test_time_bound_must_be_timezone_aware() -> None:
    transport = FakeTransport([])
    outlook, _ = sensor(transport)

    with pytest.raises(ValueError, match="timezone-aware"):
        outlook.sync_folder(
            "inbox",
            ingestion_run_id="run-naive-time",
            received_after=datetime(2026, 9, 1),
        )
    assert transport.requests == []


@pytest.mark.parametrize("bad_item", [{}, {"id": "1"}, {"id": 123, "changeKey": "v1"}])
def test_invalid_message_does_not_advance_checkpoint(bad_item: Mapping[str, object]) -> None:
    store = InMemoryCheckpointStore()
    transport = FakeTransport([response(200, {"value": [bad_item], "@odata.deltaLink": FINAL_INBOX})])
    outlook, _ = sensor(transport, store)

    with pytest.raises(OutlookSensorError) as captured:
        outlook.sync_folder("inbox", ingestion_run_id="run-bad")

    assert captured.value.metadata["category"] == "malformed_response"
    assert store.get("outlook:tenant-1:evidence@example.com:folder:inbox") is None


def test_sink_failure_does_not_advance_checkpoint() -> None:
    store = InMemoryCheckpointStore()
    transport = FakeTransport([response(200, {"value": [message(hasAttachments=False)], "@odata.deltaLink": FINAL_INBOX})])
    outlook, _ = sensor(transport, store)

    with pytest.raises(RuntimeError, match="sink unavailable"):
        outlook.sync_folder("inbox", ingestion_run_id="run-3", emit=lambda _: (_ for _ in ()).throw(RuntimeError("sink unavailable")))

    assert store.get("outlook:tenant-1:evidence@example.com:folder:inbox") is None


def test_tombstones_and_duplicate_changes_emit_once() -> None:
    deleted = {"id": "immutable-deleted-1", "@removed": {"reason": "deleted"}}
    transport = FakeTransport([response(200, {"value": [deleted, deleted], "@odata.deltaLink": FINAL_INBOX})])
    outlook, _ = sensor(transport)

    result = outlook.sync_folder("inbox", ingestion_run_id="run-4")

    assert len(result.envelopes) == 1
    assert result.tombstone_count == 1
    assert result.envelopes[0]["change_type"] == "deleted"


def test_repeated_message_uses_last_delta_occurrence() -> None:
    transport = FakeTransport([
        response(200, {
            "value": [
                message(changeKey="version-1", hasAttachments=False),
                message(changeKey="version-2", hasAttachments=False),
            ],
            "@odata.deltaLink": FINAL_INBOX,
        })
    ])
    outlook, _ = sensor(transport)

    result = outlook.sync_folder("inbox", ingestion_run_id="run-last")

    assert len(result.envelopes) == 1
    assert result.envelopes[0]["source_version"] == "version-2"


def test_replay_uses_stable_evidence_id_and_reports_sink_duplicate() -> None:
    transport = FakeTransport([
        response(200, {"value": [message(hasAttachments=False)], "@odata.deltaLink": FINAL_INBOX}),
        response(200, {"value": [message(hasAttachments=False)], "@odata.deltaLink": FINAL_INBOX + "-2"}),
    ])
    outlook, _ = sensor(transport)
    seen: set[str] = set()

    def emit(envelope: Mapping[str, object]) -> bool:
        evidence_id = str(envelope["evidence_id"])
        if evidence_id in seen:
            return False
        seen.add(evidence_id)
        return True

    first = outlook.sync_folder("inbox", ingestion_run_id="run-5", emit=emit)
    second = outlook.sync_folder("inbox", ingestion_run_id="run-6", emit=emit)

    assert first.envelopes[0]["evidence_id"] == second.envelopes[0]["evidence_id"]
    assert second.emitted_count == 0
    assert second.duplicate_count == 1


@pytest.mark.parametrize("status,category", [(401, "auth"), (403, "permission"), (429, "throttled"), (503, "retry_exhausted"), (500, "terminal")])
def test_terminal_errors_are_structured_and_redacted(status: int, category: str) -> None:
    sensitive_link = "https://graph.microsoft.com/v1.0/messages/delta?$deltatoken=sensitive-state"
    store = InMemoryCheckpointStore()
    store.put("outlook:tenant-1:evidence@example.com:folder:inbox", sensitive_link)
    transport = FakeTransport([response(status, {}, {"request-id": "server-1"})])
    outlook, _ = sensor(transport, store, max_attempts=1)

    with pytest.raises(OutlookSensorError) as captured:
        outlook.sync_folder("inbox", ingestion_run_id="run-7")

    assert captured.value.metadata["category"] == category
    rendered = str(captured.value) + repr(captured.value.metadata)
    assert "secret-access-token" not in rendered
    assert "sensitive-state" not in rendered


def test_429_retries_using_graph_foundation() -> None:
    sleeps: list[float] = []
    transport = FakeTransport([
        response(429, {}, {"Retry-After": "3"}),
        response(200, {"value": [], "@odata.deltaLink": FINAL_INBOX}),
    ])
    graph = graph_client_for_outlook(
        token_provider=lambda: "secret-access-token",
        transport=transport,
        sleep=sleeps.append,
        correlation_id_factory=lambda: "corr-123",
    )
    outlook = OutlookDeltaSensor(
        graph=graph,
        checkpoint_store=InMemoryCheckpointStore(),
        config=OutlookSensorConfig("tenant-1", "evidence@example.com", ("m365-acl:mailbox-1",)),
    )

    outlook.sync_folder("inbox", ingestion_run_id="run-8")

    assert sleeps == [3.0]


def test_malformed_collection_and_attachment_responses_are_rejected() -> None:
    malformed_collection = FakeTransport([response(200, {"value": "not-an-array"})])
    outlook, _ = sensor(malformed_collection)
    with pytest.raises(OutlookSensorError) as captured:
        outlook.sync_folder("inbox", ingestion_run_id="run-9")
    assert captured.value.metadata["category"] == "malformed_response"

    malformed_attachment = FakeTransport([
        response(200, {"value": [message()], "@odata.deltaLink": FINAL_INBOX}),
        response(200, {"value": "not-an-array"}),
    ])
    outlook, _ = sensor(malformed_attachment)
    with pytest.raises(OutlookSensorError):
        outlook.sync_folder("inbox", ingestion_run_id="run-10")


def test_envelopes_preserve_security_boundary_and_raw_evidence_required_fields() -> None:
    transport = FakeTransport([response(200, {"value": [message(hasAttachments=False)], "@odata.deltaLink": FINAL_INBOX})])
    outlook, _ = sensor(transport)
    envelope = outlook.sync_folder("inbox", ingestion_run_id="run-11").envelopes[0]

    required = {"evidence_id", "source_system", "source_record_id", "acquired_time", "security", "ingestion_run_id"}
    assert required <= envelope.keys()
    assert envelope["security"]["source_acl_refs"] == ["m365-acl:mailbox-1"]
    assert envelope["security"]["allowed_principals_or_scopes"] == []
    assert not any(key.startswith("canonical") for key in envelope)
