"""Bounded Outlook message-delta sensor emitting non-authoritative evidence envelopes."""

from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime, timezone
from hashlib import sha256
from typing import Any
from urllib.parse import quote, urlencode

from .graph import CheckpointStore, GraphClient, GraphProtocolError, GraphRequestError, InMemoryCheckpointStore


OUTLOOK_SOURCE = "microsoft-graph-outlook"
FOLDERS = ("inbox", "sentitems")


@dataclass(frozen=True)
class OutlookSensorConfig:
    tenant_id: str
    mailbox_id: str
    source_acl_refs: tuple[str, ...]
    connector_version: str = "0.1"

    def __post_init__(self) -> None:
        if not self.tenant_id or not self.mailbox_id:
            raise ValueError("tenant_id and mailbox_id are required")
        if not self.source_acl_refs:
            raise ValueError("source_acl_refs must preserve the mailbox access boundary")


@dataclass(frozen=True)
class OutlookSyncResult:
    envelopes: tuple[Mapping[str, Any], ...]
    emitted_count: int
    duplicate_count: int
    tombstone_count: int
    checkpoint_keys: tuple[str, ...]


class OutlookSensorError(RuntimeError):
    """Structured sensor error that deliberately excludes credentials and payloads."""

    def __init__(self, category: str, *, status: int | None = None, operation: str, correlation_id: str | None = None, server_request_id: str | None = None) -> None:
        self.metadata = {
            "source": OUTLOOK_SOURCE,
            "category": category,
            "status": status,
            "operation": operation,
            "correlation_id": correlation_id,
            "server_request_id": server_request_id,
        }
        super().__init__(f"Outlook acquisition failed ({category}, operation={operation})")


class OutlookDeltaSensor:
    def __init__(self, *, graph: GraphClient, checkpoint_store: CheckpointStore, config: OutlookSensorConfig, clock: Callable[[], datetime] | None = None) -> None:
        self._graph = graph
        self._checkpoints = checkpoint_store
        self._config = config
        self._clock = clock or (lambda: datetime.now(timezone.utc))

    def sync(
        self,
        *,
        ingestion_run_id: str,
        emit: Callable[[Mapping[str, Any]], bool] | None = None,
        received_after: datetime | None = None,
    ) -> OutlookSyncResult:
        if not ingestion_run_id:
            raise ValueError("ingestion_run_id is required")
        if emit is None:
            raise ValueError(
                "emit is required when syncing multiple folders so completed "
                "folder checkpoints cannot outlive undelivered envelopes"
            )
        all_envelopes: list[Mapping[str, Any]] = []
        emitted = duplicates = tombstones = 0
        keys: list[str] = []
        for folder in FOLDERS:
            result = self.sync_folder(
                folder,
                ingestion_run_id=ingestion_run_id,
                emit=emit,
                received_after=received_after,
            )
            all_envelopes.extend(result.envelopes)
            emitted += result.emitted_count
            duplicates += result.duplicate_count
            tombstones += result.tombstone_count
            keys.extend(result.checkpoint_keys)
        return OutlookSyncResult(tuple(all_envelopes), emitted, duplicates, tombstones, tuple(keys))

    def sync_folder(
        self,
        folder: str,
        *,
        ingestion_run_id: str,
        emit: Callable[[Mapping[str, Any]], bool] | None = None,
        received_after: datetime | None = None,
    ) -> OutlookSyncResult:
        if not ingestion_run_id:
            raise ValueError("ingestion_run_id is required")
        if folder not in FOLDERS:
            raise ValueError(f"folder must be one of {FOLDERS}")
        checkpoint_key = f"outlook:{self._config.tenant_id}:{self._config.mailbox_id}:folder:{folder}"
        staged = InMemoryCheckpointStore()
        if saved := self._checkpoints.get(checkpoint_key):
            staged.put(checkpoint_key, saved)
        path = self._delta_path(folder, received_after=received_after)
        try:
            changes = self._graph.sync_delta(checkpoint_key=checkpoint_key, initial_path_or_url=path, checkpoint_store=staged)
            envelopes = self._normalize_changes(changes, folder=folder, ingestion_run_id=ingestion_run_id)
            emitted = duplicates = 0
            for envelope in envelopes:
                if emit is None or emit(envelope):
                    emitted += 1
                else:
                    duplicates += 1
            final_link = staged.get(checkpoint_key)
            if final_link is None:
                raise GraphProtocolError("delta traversal did not stage a completed checkpoint")
            self._checkpoints.put(checkpoint_key, final_link)
            tombstones = sum(1 for item in envelopes if item["change_type"] == "deleted")
            return OutlookSyncResult(tuple(envelopes), emitted, duplicates, tombstones, (checkpoint_key,))
        except OutlookSensorError:
            raise
        except GraphRequestError as exc:
            raise self._request_error(exc, operation=f"sync:{folder}") from exc
        except (AttributeError, GraphProtocolError, KeyError, TypeError, ValueError) as exc:
            raise OutlookSensorError("malformed_response", operation=f"sync:{folder}") from exc

    def _normalize_changes(self, changes: Sequence[Mapping[str, Any]], *, folder: str, ingestion_run_id: str) -> list[Mapping[str, Any]]:
        by_id: dict[str, Mapping[str, Any]] = {}
        for change in changes:
            message_id = _required_string(change, "id")
            if "@removed" in change and not isinstance(change["@removed"], Mapping):
                raise GraphProtocolError("@removed must be an object")
            _message_version(change)
            by_id[message_id] = change

        envelopes: list[Mapping[str, Any]] = []
        for message_id, message in by_id.items():
            deleted = "@removed" in message
            version = _message_version(message)
            evidence_id = _evidence_id(
                self._config.tenant_id,
                self._config.mailbox_id,
                "message",
                message_id,
                version,
            )
            message_envelope = self._message_envelope(evidence_id, message, folder, version, ingestion_run_id, deleted)
            envelopes.append(message_envelope)
            has_attachments = message.get("hasAttachments", False)
            if not isinstance(has_attachments, bool):
                raise GraphProtocolError("hasAttachments must be a boolean")
            if not deleted and has_attachments:
                attachments = message.get("attachments")
                if attachments is None:
                    attachments = self._graph.get_collection(self._attachment_path(message_id))
                if not isinstance(attachments, list) or not all(isinstance(item, Mapping) for item in attachments):
                    raise GraphProtocolError("message attachments must be an array")
                for attachment in _dedupe_attachments(attachments):
                    envelopes.append(self._attachment_envelope(attachment, message_envelope, folder, ingestion_run_id))
        return envelopes

    def _message_envelope(self, evidence_id: str, message: Mapping[str, Any], folder: str, version: str, ingestion_run_id: str, deleted: bool) -> Mapping[str, Any]:
        message_id = _required_string(message, "id")
        return {
            "evidence_id": evidence_id,
            "source_system": OUTLOOK_SOURCE,
            "source_tenant": self._config.tenant_id,
            "source_container": f"{self._config.mailbox_id}/{folder}",
            "source_record_id": message_id,
            "source_version": version,
            "source_reference": f"graph://users/{quote(self._config.mailbox_id, safe='')}/messages/{quote(message_id, safe='')}?version={quote(version, safe='')}",
            "source_created_time": _optional_string(message, "createdDateTime"),
            "source_modified_time": _optional_string(message, "lastModifiedDateTime"),
            "acquired_time": self._clock().astimezone(timezone.utc).isoformat().replace("+00:00", "Z"),
            "content_hash": None,
            "content_pointer": None,
            "security": self._security(),
            "parent_evidence_id": None,
            "origin_evidence_id": None,
            "ingestion_run_id": ingestion_run_id,
            "object_kind": "message_tombstone" if deleted else "message",
            "change_type": "deleted" if deleted else "upsert",
            "connector_version": self._config.connector_version,
            "metadata": {} if deleted else {
                "internet_message_id": _optional_string(message, "internetMessageId"),
                "conversation_id": _optional_string(message, "conversationId"),
                "conversation_index": _optional_string(message, "conversationIndex"),
                "subject": _optional_string(message, "subject"),
                "sender": _safe_party(message.get("sender")),
                "from": _safe_party(message.get("from")),
                "to_recipients": _safe_parties(message.get("toRecipients")),
                "cc_recipients": _safe_parties(message.get("ccRecipients")),
                "bcc_recipients": _safe_parties(message.get("bccRecipients")),
                "sent_time": _optional_string(message, "sentDateTime"),
                "received_time": _optional_string(message, "receivedDateTime"),
                "has_attachments": message.get("hasAttachments", False),
            },
        }

    def _attachment_envelope(self, attachment: Mapping[str, Any], parent: Mapping[str, Any], folder: str, ingestion_run_id: str) -> Mapping[str, Any]:
        attachment_id = _required_string(attachment, "id")
        version = _optional_string(attachment, "lastModifiedDateTime") or str(parent["source_version"])
        evidence_id = _evidence_id(self._config.tenant_id, self._config.mailbox_id, "attachment", str(parent["source_record_id"]), attachment_id, version)
        return {
            "evidence_id": evidence_id,
            "source_system": OUTLOOK_SOURCE,
            "source_tenant": self._config.tenant_id,
            "source_container": f"{self._config.mailbox_id}/{folder}",
            "source_record_id": attachment_id,
            "source_version": version,
            "source_reference": f"{parent['source_reference']}#attachment={quote(attachment_id, safe='')}",
            "source_created_time": None,
            "source_modified_time": _optional_string(attachment, "lastModifiedDateTime"),
            "acquired_time": parent["acquired_time"],
            "content_hash": None,
            "content_pointer": None,
            "security": self._security(),
            "parent_evidence_id": parent["evidence_id"],
            "origin_evidence_id": None,
            "ingestion_run_id": ingestion_run_id,
            "object_kind": "attachment",
            "change_type": "upsert",
            "connector_version": self._config.connector_version,
            "metadata": {
                "name": _optional_string(attachment, "name"),
                "content_type": _optional_string(attachment, "contentType"),
                "size": attachment.get("size") if isinstance(attachment.get("size"), int) else None,
                "is_inline": bool(attachment.get("isInline")),
                "attachment_type": _optional_string(attachment, "@odata.type"),
            },
        }

    def _security(self) -> Mapping[str, Any]:
        return {
            "classification": None,
            "policy_refs": ["policy:source-acl-intersection"],
            "source_acl_refs": list(self._config.source_acl_refs),
            "allowed_principals_or_scopes": [],
            "denied_principals_or_scopes": [],
            "property_restrictions": [],
            "evidence_restrictions": ["source-acl-required"],
        }

    def _delta_path(
        self, folder: str, *, received_after: datetime | None = None
    ) -> str:
        mailbox = quote(self._config.mailbox_id, safe="")
        select = "id,changeKey,internetMessageId,conversationId,conversationIndex,subject,sender,from,toRecipients,ccRecipients,bccRecipients,createdDateTime,lastModifiedDateTime,sentDateTime,receivedDateTime,hasAttachments"
        query = {"$select": select}
        if received_after is not None:
            if received_after.tzinfo is None or received_after.utcoffset() is None:
                raise ValueError("received_after must be timezone-aware")
            timestamp = (
                received_after.astimezone(timezone.utc)
                .isoformat()
                .replace("+00:00", "Z")
            )
            query["$filter"] = f"receivedDateTime ge {timestamp}"
            query["$orderby"] = "receivedDateTime desc"
        return (
            f"users/{mailbox}/mailFolders/{folder}/messages/delta?"
            f"{urlencode(query)}"
        )

    def _attachment_path(self, message_id: str) -> str:
        mailbox = quote(self._config.mailbox_id, safe="")
        message = quote(message_id, safe="")
        return f"users/{mailbox}/messages/{message}/attachments?$select=id,name,contentType,size,isInline,lastModifiedDateTime"

    @staticmethod
    def _request_error(exc: GraphRequestError, *, operation: str) -> OutlookSensorError:
        status = int(exc.metadata["status"])
        category = "auth" if status == 401 else "permission" if status == 403 else "throttled" if status == 429 else "retry_exhausted" if status in {503, 504} else "terminal"
        return OutlookSensorError(category, status=status, operation=operation, correlation_id=str(exc.metadata.get("correlation_id") or "") or None, server_request_id=str(exc.metadata.get("server_request_id") or "") or None)


def graph_client_for_outlook(**kwargs: Any) -> GraphClient:
    """Construct the shared Graph client with immutable Outlook IDs enabled."""
    return GraphClient(request_headers={"Prefer": 'IdType="ImmutableId"'}, **kwargs)


def _message_version(message: Mapping[str, Any]) -> str:
    if "@removed" in message:
        return "tombstone"
    return _optional_string(message, "changeKey") or _optional_string(message, "lastModifiedDateTime") or _raise_protocol("message requires changeKey or lastModifiedDateTime")


def _dedupe_attachments(items: Sequence[Mapping[str, Any]]) -> list[Mapping[str, Any]]:
    unique: dict[str, Mapping[str, Any]] = {}
    for item in items:
        item_id = _required_string(item, "id")
        _optional_string(item, "lastModifiedDateTime")
        unique[item_id] = item
    return list(unique.values())


def _evidence_id(*parts: str) -> str:
    material = "\x1f".join(parts).encode("utf-8")
    return f"outlook:{sha256(material).hexdigest()}"


def _required_string(value: Mapping[str, Any], key: str) -> str:
    result = value.get(key)
    if not isinstance(result, str) or not result:
        raise GraphProtocolError(f"{key} must be a non-empty string")
    return result


def _optional_string(value: Mapping[str, Any], key: str) -> str | None:
    result = value.get(key)
    if result is None:
        return None
    if not isinstance(result, str):
        raise GraphProtocolError(f"{key} must be a string when present")
    return result


def _safe_party(value: Any) -> Mapping[str, str | None] | None:
    if value is None:
        return None
    if not isinstance(value, Mapping):
        raise GraphProtocolError("party must be an object")
    email = value.get("emailAddress")
    if not isinstance(email, Mapping):
        raise GraphProtocolError("party.emailAddress must be an object")
    return {"name": email.get("name") if isinstance(email.get("name"), str) else None, "address": email.get("address") if isinstance(email.get("address"), str) else None}


def _safe_parties(value: Any) -> list[Mapping[str, str | None]]:
    if value is None:
        return []
    if not isinstance(value, list):
        raise GraphProtocolError("recipients must be an array")
    return [party for item in value if (party := _safe_party(item)) is not None]


def _raise_protocol(message: str) -> str:
    raise GraphProtocolError(message)
