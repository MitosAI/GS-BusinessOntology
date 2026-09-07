from __future__ import annotations

import pytest

from gensigma_br import BusinessRealityKernel, UnknownSemanticType


def test_business_relationship_is_the_only_promotable_material_relationship_type() -> None:
    kernel = BusinessRealityKernel()

    assert kernel.contracts.semantic_schema_path("BusinessRelationship") == (
        "schemas/business/business-relationship.schema.json"
    )
    with pytest.raises(UnknownSemanticType):
        kernel.contracts.semantic_schema_path("TypedRelationship")


def test_typed_relationship_remains_a_reusable_registered_schema() -> None:
    kernel = BusinessRealityKernel()

    schema = kernel.contracts.schema("schemas/kernel/typed-relationship.schema.json")
    assert schema["title"] == "Typed Relationship"
