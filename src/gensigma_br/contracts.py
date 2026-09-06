from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import ValidationError
from referencing import Registry, Resource


class ContractViolation(ValueError):
    """Raised when an object violates a GenSigma semantic contract."""


class UnknownSemanticType(ValueError):
    """Raised when no promotable canonical contract exists for a semantic type."""


def _schema_name(semantic_type: str) -> str:
    # LegalEntity -> legal-entity, Organization -> organization.
    return re.sub(r"(?<!^)(?=[A-Z])", "-", semantic_type).lower()


class ContractRegistry:
    """Loads the repository's JSON Schema contracts without choosing a runtime database."""

    _KERNEL_CANONICAL_TYPES = frozenset(
        {"Event", "Assessment", "Decision", "Approval", "Action", "Outcome"}
    )

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

    def semantic_schema_path(self, semantic_type: str) -> str:
        """Resolve a canonical semantic type to its governing promotable schema.

        Business Reality object contracts live under ``schemas/business``. A bounded
        set of first-class kernel resources (Event, Assessment, Decision, Approval,
        Action, Outcome) live under ``schemas/kernel``. Helper/kernel component schemas
        are deliberately not made promotable merely because a file exists.
        """
        if not isinstance(semantic_type, str) or not semantic_type.strip():
            raise UnknownSemanticType("Semantic type must be a non-empty string")

        schema_name = _schema_name(semantic_type)
        business_path = f"schemas/business/{schema_name}.schema.json"
        if business_path in self._schemas_by_path:
            return business_path

        if semantic_type in self._KERNEL_CANONICAL_TYPES:
            kernel_path = f"schemas/kernel/{schema_name}.schema.json"
            if kernel_path in self._schemas_by_path:
                return kernel_path

        raise UnknownSemanticType(
            f"No promotable semantic contract is registered for type {semantic_type!r}"
        )

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

    def validate_semantic_resource(
        self, semantic_type: str, instance: dict[str, Any]
    ) -> None:
        self.validate(self.semantic_schema_path(semantic_type), instance)
