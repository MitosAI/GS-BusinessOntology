"""Allowlisted SharePoint drive delta sensor for non-authoritative evidence capture."""

from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime, timezone
from hashlib import sha256
from typing import Any
from urllib.parse import quote

from .graph import CheckpointStore, GraphClient, GraphProtocolError, GraphRequestError, InMemoryCheckpointStore


SHAREPOINT_SOURCE = "microsoft-graph-sharepoint"


@dataclass(frozen=True)
class SharePointScope:
    site_id: str
    drive_id: str
    library_id: str
    source_acl_refs: tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.site_id or not self.drive_id or not self.library_id:
            raise ValueError("site_id, drive_id, and library_id are required")
        if not self.source_acl_refs:
            raise ValueError("source_acl_refs must preserve the configured library boundary")


@dataclass(frozen=True)
class SharePointSensorConfig:
    tenant_id: str
    allowed_scopes: tuple[SharePointScope, ...]
    connector_version: str = "0.1"

    def __post_init__(self) -> None:
        if not self.tenant_id:
            raise ValueError("tenant_id is required")
        if not self.allowed_scopes:
            raise ValueError("allowed_scopes must contain at least one configured library")
        keys = [(scope.site_id, scope.drive_id) for scope in self.allowed_scopes]
        if len(keys) != len(set(keys)):
            raise ValueError("allowed_scopes cannot repeat a site/drive pair")


@dataclass(frozen=True)
class SharePointSyncResult:
    envelopes: tuple[Mapping[str, Any], ...]
    emitted_count: int
    duplicate_count: int
    tombstone_count: int
    checkpoint_keys: tuple[str, ...]


class SharePointSensorError(RuntimeError):
    """Structured sensor error that excludes authorization and document content."""

    def __init__(self, category: str, *, status: int | None = None, operation: str, correlation_id: str | None = None, server_request_id: str | None = None) -> None:
        self.metadata = {
            "source": SHAREPOINT_SOURCE,
            "category": category,
            "status": status,
            "operation": operation,
            "correlation_id": correlation_id,
            "server_request_id": server_request_id,
        }
        super().__init__(f"SharePoint acquisition failed ({category}, operation={operation})")


class SharePointDeltaSensor:
    def __init__(self, *, graph: GraphClient, checkpoint_store: CheckpointStore, config: SharePointSensorConfig, clock: Callable[[], datetime] | None = None) -> None:
        self._graph = graph
        self._checkpoints = checkpoint_store
        self._config = config
        self._clock = clock or (lambda: datetime.now(timezone.utc))

    def sync(self, *, ingestion_run_id: str, emit: Callable[[Mapping[str, Any]], bool] | None = None) -> SharePointSyncResult:
        if not ingestion_run_id:
            raise ValueError("ingestion_run_id is required")
        envelopes: list[Mapping[str, Any]] = []
        emitted = duplicates = tombstones = 0
        keys: list[str] = []
        for scope in self._config.allowed_scopes:
            result = self.sync_scope(scope, ingestion_run_id=ingestion_run_id, emit=emit)
            envelopes.extend(result.envelopes)
            emitted += result.emitted_count
            duplicates += result.duplicate_count
            tombstones += result.tombstone_count
            keys.extend(result.checkpoint_keys)
        return SharePointSyncResult(tuple(envelopes), emitted, duplicates, tombstones, tuple(keys))

    def sync_scope(self, scope: SharePointScope, *, ingestion_run_id: str, emit: Callable[[Mapping[str, Any]], bool] | None = None) -> SharePointSyncResult:
        if scope not in self._config.allowed_scopes:
            raise ValueError("scope is not present in the configured allowlist")
        checkpoint_key = f"sharepoint:{self._config.tenant_id}:{scope.site_id}:drive:{scope.drive_id}"
        staged = InMemoryCheckpointStore()
        if saved := self._checkpoints.get(checkpoint_key):
            staged.put(checkpoint_key, saved)
        try:
            changes = self._graph.sync_delta(
                checkpoint_key=checkpoint_key,
                initial_path_or_url=self._delta_path(scope),
                checkpoint_store=staged,
            )
            envelopes = self._normalize_changes(changes, scope=scope, ingestion_run_id=ingestion_run_id)
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
            return SharePointSyncResult(tuple(envelopes), emitted, duplicates, tombstones, (checkpoint_key,))
        except SharePointSensorError:
            raise
        except GraphRequestError as exc:
            raise self._request_error(exc, operation=f"sync:{scope.site_id}:{scope.drive_id}") from exc
        except (GraphProtocolError, KeyError, TypeError, ValueError) as exc:
            raise SharePointSensorError("malformed_response", operation=f"sync:{scope.site_id}:{scope.drive_id}") from exc

    def _normalize_changes(self, changes: Sequence[Mapping[str, Any]], *, scope: SharePointScope, ingestion_run_id: str) -> list[Mapping[str, Any]]:
        unique: dict[str, Mapping[str, Any]] = {}
        for item in changes:
            item_id = _required_string(item, "id")
            _item_version(item)
            unique[item_id] = item
        return [
            self._envelope(
                _evidence_id(
                    self._config.tenant_id,
                    scope.site_id,
                    scope.drive_id,
                    item_id,
                    _item_version(item),
                ),
                item,
                scope,
                ingestion_run_id,
            )
            for item_id, item in unique.items()
        ]

    def _envelope(self, evidence_id: str, item: Mapping[str, Any], scope: SharePointScope, ingestion_run_id: str) -> Mapping[str, Any]:
        item_id = _required_string(item, "id")
        version = _item_version(item)
        deleted = "deleted" in item
        file_facet = _optional_mapping(item, "file")
        folder_facet = _optional_mapping(item, "folder")
        if not deleted and file_facet is None and folder_facet is None:
            raise GraphProtocolError("driveItem requires file, folder, or deleted facet")
        parent = _optional_mapping(item, "parentReference")
        path = _item_path(parent, _optional_string(item, "name"))
        object_kind = "drive_item_tombstone" if deleted else "file" if file_facet is not None else "folder"
        return {
            "evidence_id": evidence_id,
            "source_system": SHAREPOINT_SOURCE,
            "source_tenant": self._config.tenant_id,
            "source_container": f"{scope.site_id}/{scope.library_id}/{scope.drive_id}",
            "source_record_id": item_id,
            "source_version": version,
            "source_reference": f"graph://sites/{quote(scope.site_id, safe='')}/drives/{quote(scope.drive_id, safe='')}/items/{quote(item_id, safe='')}?version={quote(version, safe='')}",
            "source_created_time": _optional_string(item, "createdDateTime"),
            "source_modified_time": _optional_string(item, "lastModifiedDateTime"),
            "acquired_time": self._clock().astimezone(timezone.utc).isoformat().replace("+00:00", "Z"),
            "content_hash": _preferred_hash(file_facet),
            "content_pointer": None,
            "security": self._security(scope, item_id),
            "parent_evidence_id": None,
            "origin_evidence_id": None,
            "ingestion_run_id": ingestion_run_id,
            "object_kind": object_kind,
            "change_type": "deleted" if deleted else "upsert",
            "connector_version": self._config.connector_version,
            "metadata": {} if deleted else {
                "site_id": scope.site_id,
                "drive_id": scope.drive_id,
                "library_id": scope.library_id,
                "name": _optional_string(item, "name"),
                "path": path,
                "size": item.get("size") if isinstance(item.get("size"), int) else None,
                "etag": _optional_string(item, "eTag"),
                "ctag": _optional_string(item, "cTag"),
                "content_type": _optional_string(file_facet or {}, "mimeType"),
                "hashes": _safe_hashes(file_facet),
                "created_by": _safe_identity(item.get("createdBy")),
                "last_modified_by": _safe_identity(item.get("lastModifiedBy")),
                "sharepoint_ids": _safe_string_mapping(item.get("sharepointIds")),
                "web_url": _optional_string(item, "webUrl"),
                "child_count": folder_facet.get("childCount") if folder_facet and isinstance(folder_facet.get("childCount"), int) else None,
            },
        }

    def _security(self, scope: SharePointScope, item_id: str) -> Mapping[str, Any]:
        permission_ref = f"graph://drives/{quote(scope.drive_id, safe='')}/items/{quote(item_id, safe='')}/permissions"
        return {
            "classification": None,
            "policy_refs": ["policy:source-acl-intersection"],
            "source_acl_refs": [*scope.source_acl_refs, permission_ref],
            "allowed_principals_or_scopes": [],
            "denied_principals_or_scopes": [],
            "property_restrictions": [],
            "evidence_restrictions": ["source-acl-required"],
        }

    @staticmethod
    def _delta_path(scope: SharePointScope) -> str:
        drive = quote(scope.drive_id, safe="")
        select = "id,name,size,eTag,cTag,createdDateTime,lastModifiedDateTime,createdBy,lastModifiedBy,parentReference,file,folder,deleted,sharepointIds,webUrl"
        return f"drives/{drive}/root/delta?$select={select}"

    @staticmethod
    def _request_error(exc: GraphRequestError, *, operation: str) -> SharePointSensorError:
        status = int(exc.metadata["status"])
        category = "auth" if status == 401 else "permission" if status == 403 else "throttled" if status == 429 else "retry_exhausted" if status in {503, 504} else "terminal"
        return SharePointSensorError(category, status=status, operation=operation, correlation_id=str(exc.metadata.get("correlation_id") or "") or None, server_request_id=str(exc.metadata.get("server_request_id") or "") or None)


def _item_version(item: Mapping[str, Any]) -> str:
    if "deleted" in item:
        return "tombstone"
    return _optional_string(item, "eTag") or _optional_string(item, "cTag") or _optional_string(item, "lastModifiedDateTime") or _raise_protocol("driveItem requires eTag, cTag, or lastModifiedDateTime")


def _evidence_id(*parts: str) -> str:
    return f"sharepoint:{sha256(chr(31).join(parts).encode('utf-8')).hexdigest()}"


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


def _optional_mapping(value: Mapping[str, Any], key: str) -> Mapping[str, Any] | None:
    result = value.get(key)
    if result is None:
        return None
    if not isinstance(result, Mapping):
        raise GraphProtocolError(f"{key} must be an object when present")
    return result


def _item_path(parent: Mapping[str, Any] | None, name: str | None) -> str | None:
    parent_path = _optional_string(parent or {}, "path")
    if parent_path is None:
        return name
    return f"{parent_path.rstrip('/')}/{name}" if name else parent_path


def _safe_hashes(file_facet: Mapping[str, Any] | None) -> Mapping[str, str]:
    hashes = (file_facet or {}).get("hashes")
    if hashes is None:
        return {}
    if not isinstance(hashes, Mapping):
        raise GraphProtocolError("file.hashes must be an object")
    allowed = {"quickXorHash", "sha1Hash", "crc32Hash"}
    return {key: value for key, value in hashes.items() if key in allowed and isinstance(value, str)}


def _preferred_hash(file_facet: Mapping[str, Any] | None) -> str | None:
    hashes = _safe_hashes(file_facet)
    for key, prefix in (("quickXorHash", "quickxor"), ("sha1Hash", "sha1"), ("crc32Hash", "crc32")):
        if value := hashes.get(key):
            return f"{prefix}:{value}"
    return None


def _safe_identity(value: Any) -> Mapping[str, str | None] | None:
    if value is None:
        return None
    if not isinstance(value, Mapping):
        raise GraphProtocolError("identitySet must be an object")
    user = value.get("user")
    if user is None:
        return None
    if not isinstance(user, Mapping):
        raise GraphProtocolError("identitySet.user must be an object")
    return {
        "id": user.get("id") if isinstance(user.get("id"), str) else None,
        "display_name": user.get("displayName") if isinstance(user.get("displayName"), str) else None,
    }


def _safe_string_mapping(value: Any) -> Mapping[str, str]:
    if value is None:
        return {}
    if not isinstance(value, Mapping):
        raise GraphProtocolError("sharepointIds must be an object")
    return {key: item for key, item in value.items() if isinstance(key, str) and isinstance(item, str)}


def _raise_protocol(message: str) -> str:
    raise GraphProtocolError(message)
