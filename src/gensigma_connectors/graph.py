"""Transport-neutral Microsoft Graph paging, delta, and retry support."""

from __future__ import annotations

from collections.abc import Callable, Mapping
from dataclasses import dataclass
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from typing import Any, Protocol
from urllib.parse import urljoin, urlparse
from uuid import uuid4


GRAPH_SOURCE = "microsoft-graph"
DEFAULT_BASE_URL = "https://graph.microsoft.com/v1.0/"


@dataclass(frozen=True)
class GraphHttpResponse:
    status: int
    headers: Mapping[str, str]
    body: Mapping[str, Any]


class GraphTransport(Protocol):
    def request(
        self, method: str, url: str, headers: Mapping[str, str]
    ) -> GraphHttpResponse: ...


class CheckpointStore(Protocol):
    def get(self, key: str) -> str | None: ...

    def put(self, key: str, delta_link: str) -> None: ...


class InMemoryCheckpointStore:
    """Reference checkpoint store for tests and bounded development runs."""

    def __init__(self) -> None:
        self._links: dict[str, str] = {}

    def get(self, key: str) -> str | None:
        return self._links.get(key)

    def put(self, key: str, delta_link: str) -> None:
        self._links[key] = delta_link


class GraphProtocolError(ValueError):
    """Graph returned a malformed paging or delta response."""


class GraphRequestError(RuntimeError):
    """Terminal Graph error with safe operational metadata."""

    def __init__(
        self,
        *,
        status: int,
        url: str,
        attempt: int,
        correlation_id: str,
        server_request_id: str | None,
    ) -> None:
        self.metadata = {
            "source": GRAPH_SOURCE,
            "status": status,
            "url": url,
            "attempt": attempt,
            "correlation_id": correlation_id,
            "server_request_id": server_request_id,
        }
        super().__init__(
            f"Microsoft Graph request failed with status {status} "
            f"after attempt {attempt} (correlation_id={correlation_id})"
        )


class GraphClient:
    """Small Graph v1.0 client that keeps identity and HTTP concerns injectable."""

    def __init__(
        self,
        *,
        token_provider: Callable[[], str],
        transport: GraphTransport,
        sleep: Callable[[float], None],
        now: Callable[[], datetime] | None = None,
        correlation_id_factory: Callable[[], str] | None = None,
        base_url: str = DEFAULT_BASE_URL,
        max_attempts: int = 4,
        base_backoff_seconds: float = 1.0,
    ) -> None:
        if max_attempts < 1:
            raise ValueError("max_attempts must be at least 1")
        if base_backoff_seconds < 0:
            raise ValueError("base_backoff_seconds cannot be negative")

        self._token_provider = token_provider
        self._transport = transport
        self._sleep = sleep
        self._now = now or (lambda: datetime.now(timezone.utc))
        self._correlation_id_factory = correlation_id_factory or (
            lambda: str(uuid4())
        )
        self._base_url = base_url.rstrip("/") + "/"
        self._max_attempts = max_attempts
        self._base_backoff_seconds = base_backoff_seconds

    def get_collection(self, path_or_url: str) -> list[Mapping[str, Any]]:
        """Enumerate a collection by following Graph's opaque next links."""

        items, _ = self._walk_pages(self._absolute_url(path_or_url))
        return items

    def sync_delta(
        self,
        *,
        checkpoint_key: str,
        initial_path_or_url: str,
        checkpoint_store: CheckpointStore,
    ) -> list[Mapping[str, Any]]:
        """Resume a delta traversal and persist only Graph's final opaque link."""

        start = checkpoint_store.get(checkpoint_key) or self._absolute_url(
            initial_path_or_url
        )
        items, delta_link = self._walk_pages(start)
        if delta_link is None:
            raise GraphProtocolError("delta response ended without @odata.deltaLink")
        checkpoint_store.put(checkpoint_key, delta_link)
        return items

    def get(self, path_or_url: str) -> Mapping[str, Any]:
        return self._request(self._absolute_url(path_or_url)).body

    def _walk_pages(
        self, start_url: str
    ) -> tuple[list[Mapping[str, Any]], str | None]:
        url = start_url
        items: list[Mapping[str, Any]] = []
        delta_link: str | None = None

        while True:
            body = self._request(url).body
            page_items = body.get("value")
            if not isinstance(page_items, list) or not all(
                isinstance(item, Mapping) for item in page_items
            ):
                raise GraphProtocolError("collection response requires a value array")
            items.extend(page_items)

            next_link = body.get("@odata.nextLink")
            final_delta_link = body.get("@odata.deltaLink")
            if next_link is not None:
                if not isinstance(next_link, str):
                    raise GraphProtocolError("@odata.nextLink must be a string")
                url = self._validated_graph_url(next_link)
                continue
            if final_delta_link is not None:
                if not isinstance(final_delta_link, str):
                    raise GraphProtocolError("@odata.deltaLink must be a string")
                delta_link = self._validated_graph_url(final_delta_link)
            return items, delta_link

    def _request(self, url: str) -> GraphHttpResponse:
        url = self._validated_graph_url(url)
        correlation_id = self._correlation_id_factory()

        for attempt in range(1, self._max_attempts + 1):
            token = self._token_provider()
            if not token:
                raise ValueError("token_provider returned an empty access token")
            response = self._transport.request(
                "GET",
                url,
                {
                    "Accept": "application/json",
                    "Authorization": f"Bearer {token}",
                    "client-request-id": correlation_id,
                    "return-client-request-id": "true",
                },
            )
            if 200 <= response.status < 300:
                return response

            if response.status in {429, 503} and attempt < self._max_attempts:
                self._sleep(self._retry_delay(response.headers, attempt))
                continue

            raise GraphRequestError(
                status=response.status,
                url=url,
                attempt=attempt,
                correlation_id=correlation_id,
                server_request_id=self._header(response.headers, "request-id"),
            )

        raise AssertionError("request loop must return or raise")

    def _retry_delay(self, headers: Mapping[str, str], attempt: int) -> float:
        retry_after = self._header(headers, "retry-after")
        if retry_after is not None:
            try:
                return max(0.0, float(retry_after))
            except ValueError:
                try:
                    retry_at = parsedate_to_datetime(retry_after)
                    if retry_at.tzinfo is None:
                        retry_at = retry_at.replace(tzinfo=timezone.utc)
                    return max(0.0, (retry_at - self._now()).total_seconds())
                except (TypeError, ValueError, OverflowError):
                    pass
        return self._base_backoff_seconds * (2 ** (attempt - 1))

    def _absolute_url(self, path_or_url: str) -> str:
        parsed = urlparse(path_or_url)
        if parsed.scheme or parsed.netloc:
            return self._validated_graph_url(path_or_url)
        return self._validated_graph_url(urljoin(self._base_url, path_or_url.lstrip("/")))

    @staticmethod
    def _validated_graph_url(url: str) -> str:
        parsed = urlparse(url)
        if parsed.scheme != "https" or parsed.hostname != "graph.microsoft.com":
            raise ValueError("Graph URLs must use https://graph.microsoft.com")
        return url

    @staticmethod
    def _header(headers: Mapping[str, str], name: str) -> str | None:
        expected = name.casefold()
        return next(
            (value for key, value in headers.items() if key.casefold() == expected),
            None,
        )
