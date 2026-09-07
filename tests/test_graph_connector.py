from __future__ import annotations

from collections.abc import Mapping
from datetime import datetime, timezone

import pytest

from gensigma_connectors import (
    GraphClient,
    GraphHttpResponse,
    GraphProtocolError,
    GraphRequestError,
    InMemoryCheckpointStore,
)


class FakeTransport:
    def __init__(self, responses: list[GraphHttpResponse]) -> None:
        self.responses = iter(responses)
        self.requests: list[tuple[str, str, Mapping[str, str]]] = []

    def request(
        self, method: str, url: str, headers: Mapping[str, str]
    ) -> GraphHttpResponse:
        self.requests.append((method, url, headers))
        return next(self.responses)


def response(
    status: int, body: Mapping[str, object], headers: Mapping[str, str] | None = None
) -> GraphHttpResponse:
    return GraphHttpResponse(status, headers or {}, body)


def client(
    transport: FakeTransport,
    sleeps: list[float] | None = None,
    **kwargs: object,
) -> GraphClient:
    return GraphClient(
        token_provider=lambda: "injected-token",
        transport=transport,
        sleep=(sleeps if sleeps is not None else []).append,
        correlation_id_factory=lambda: "corr-123",
        **kwargs,
    )


def test_enumerates_collection_using_opaque_next_link() -> None:
    next_link = "https://graph.microsoft.com/v1.0/me/messages?$skiptoken=opaque%2Bvalue"
    transport = FakeTransport(
        [
            response(200, {"value": [{"id": "1"}], "@odata.nextLink": next_link}),
            response(200, {"value": [{"id": "2"}]}),
        ]
    )

    assert client(transport).get_collection("me/messages") == [
        {"id": "1"},
        {"id": "2"},
    ]
    assert transport.requests[1][1] == next_link
    assert transport.requests[0][2]["Authorization"] == "Bearer injected-token"
    assert transport.requests[0][2]["client-request-id"] == "corr-123"


def test_delta_sync_resumes_and_persists_opaque_final_link() -> None:
    saved = "https://graph.microsoft.com/v1.0/me/messages/delta?$deltatoken=saved"
    final = "https://graph.microsoft.com/v1.0/me/messages/delta?$deltatoken=final%2Fopaque"
    store = InMemoryCheckpointStore()
    store.put("mailbox:inbox", saved)
    transport = FakeTransport(
        [response(200, {"value": [{"id": "changed"}], "@odata.deltaLink": final})]
    )

    items = client(transport).sync_delta(
        checkpoint_key="mailbox:inbox",
        initial_path_or_url="me/messages/delta",
        checkpoint_store=store,
    )

    assert items == [{"id": "changed"}]
    assert transport.requests[0][1] == saved
    assert store.get("mailbox:inbox") == final


def test_delta_sync_does_not_checkpoint_an_incomplete_traversal() -> None:
    store = InMemoryCheckpointStore()
    transport = FakeTransport([response(200, {"value": []})])

    with pytest.raises(GraphProtocolError, match="without @odata.deltaLink"):
        client(transport).sync_delta(
            checkpoint_key="mailbox:inbox",
            initial_path_or_url="me/messages/delta",
            checkpoint_store=store,
        )

    assert store.get("mailbox:inbox") is None


def test_429_honors_numeric_retry_after() -> None:
    sleeps: list[float] = []
    transport = FakeTransport(
        [response(429, {}, {"Retry-After": "7"}), response(200, {"value": []})]
    )

    assert client(transport, sleeps).get_collection("me/messages") == []
    assert sleeps == [7.0]


def test_503_uses_deterministic_exponential_backoff() -> None:
    sleeps: list[float] = []
    transport = FakeTransport(
        [response(503, {}), response(503, {}), response(200, {"value": []})]
    )

    assert client(
        transport, sleeps, base_backoff_seconds=0.5
    ).get_collection("me/messages") == []
    assert sleeps == [0.5, 1.0]


def test_retry_after_http_date_uses_injected_clock() -> None:
    sleeps: list[float] = []
    transport = FakeTransport(
        [
            response(503, {}, {"Retry-After": "Mon, 07 Sep 2026 03:00:05 GMT"}),
            response(200, {"value": []}),
        ]
    )

    graph = client(
        transport,
        sleeps,
        now=lambda: datetime(2026, 9, 7, 3, 0, tzinfo=timezone.utc),
    )
    assert graph.get_collection("me/messages") == []
    assert sleeps == [5.0]


def test_terminal_error_contains_safe_structured_metadata() -> None:
    transport = FakeTransport(
        [response(503, {}, {"request-id": "server-456"})]
    )

    with pytest.raises(GraphRequestError) as captured:
        client(transport, max_attempts=1).get_collection("me/messages")

    assert captured.value.metadata == {
        "source": "microsoft-graph",
        "status": 503,
        "url": "https://graph.microsoft.com/v1.0/me/messages",
        "attempt": 1,
        "correlation_id": "corr-123",
        "server_request_id": "server-456",
    }
    assert "injected-token" not in str(captured.value)
    assert "injected-token" not in repr(captured.value.metadata)


def test_rejects_non_graph_continuation_url() -> None:
    transport = FakeTransport(
        [
            response(
                200,
                {
                    "value": [],
                    "@odata.nextLink": "https://example.com/steal-token",
                },
            )
        ]
    )

    with pytest.raises(ValueError, match="graph.microsoft.com"):
        client(transport).get_collection("me/messages")
