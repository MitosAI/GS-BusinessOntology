from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import ValidationError
from referencing import Registry, Resource


class ContractViolation(ValueError):
    """Raised when an object violates a GenSigma semantic contract."""


class ContractRegistry:
    """Loads the repository's JSON Schema contracts without choosing a runtime database."""

    def __init__(self, contracts_root: str | Path = "contracts") -> None:
        self.root = Path(contracts_root)
        self._schemas_by_path: dict[str, dict[str, Any]] = {}
        self._registry = Registry()
        self._load()

    def _load(self) -> None:
        if not self.root.exists():
            raise FileNotFoundError(f"Contract root not found: {self.root}")

        resources: list[tuple[str, Resource[Any]]] = []
        for path in sorted(self.root.rglob("*.schema.json")):
            schema = json.loads(path.read_text(encoding="utf-8"))
            rel = path.relative_to(self.root).as_posix()
            self._schemas_by_path[rel] = schema
            schema_id = schema.get("$id")
            if schema_id:
                resources.append((schema_id, Resource.from_contents(schema)))

        self._registry = self._registry.with_resources(resources)

    def schema(self, relative_path: str) -> dict[str, Any]:
        try:
            return self._schemas_by_path[relative_path]
        except KeyError as exc:
            raise KeyError(f"Unknown contract schema: {relative_path}") from exc

    def validate(self, relative_path: str, instance: dict[str, Any]) -> None:
        schema = self.schema(relative_path)
        validator = Draft202012Validator(
            schema,
            registry=self._registry,
            format_checker=FormatChecker(),
        )
        try:
            validator.validate(instance)
        except ValidationError as exc:
            location = ".".join(str(part) for part in exc.absolute_path) or "<root>"
            raise ContractViolation(
                f"{relative_path} violation at {location}: {exc.message}"
            ) from exc
