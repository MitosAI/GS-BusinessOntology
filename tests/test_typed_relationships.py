from __future__ import annotations

import copy

import pytest

from gensigma_br import (
    BusinessRealityKernel,
    CandidateSemanticTypeMismatch,
    ContractViolation,
)


NOW = "2026-09-06T00:00:00Z"


def security() -> dict:
    return {
        "classification": "Normal Business",
        "policy_refs": [],
        "source_acl_refs": [],
        "allowed_principals_or_scopes": [],
        "denied_principals_or_scopes": [],
        "property_restrictions": [],
        "evidence_restrictions": [],
    }


def canonical_ref(resource_id: str, semantic_type: str) -> dict:
    return {
        "id": resource_id,
        "type": semantic_type,
        "model_owner": "business_reality",
        "contract_version": "0.1",
    }


def raw_evidence() -> dict:
    return {
        "evidence_id": "ev-relationship-001",
        "source_system": "sharepoint",
        "source_record_id": "relationship-source-001",
        "acquired_time": NOW,
        "security": security(),
        "ingestion_run_id": "run-001",
    }


def relationship_candidate() -> dict:
    return {
        "candidate_id": "cand-relationship-001",
        "candidate_type": "relationship",
        "proposed_semantic_type": "TypedRelationship",
        "subject_refs": [],
        "context_refs": [],
        "observation_ids": [],
        "source_evidence_ids": ["ev-relationship-001"],
        "epistemic_status": "unresolved",
        "resolution_status": "proposed",
        "security": security(),
        "created_at": NOW,
    }


def typed_relationship() -> dict:
    return {
        "id": "relationship-001",
        "type": "TypedRelationship",
        "model_owner": "business_reality",
        "contract_version": "0.1",
        "display_name": "SFO uses ServiceNow",
        "lifecycle_state": "active",
        "effective_time": {"valid_from": NOW, "valid_to": None, "precision": "exact"},
        "source_time": NOW,
        "recorded_at": NOW,
        "discovered_at": NOW,
        "epistemic_status": "accepted",
        "provenance_refs": [],
        "security": security(),
        "source_mappings": [],
        "aliases": [],
        "audit": {
            "created_by": "test",
            "created_at": NOW,
            "last_changed_by": None,
            "last_changed_at": None,
            "change_reason": None,
            "change_request_id": None,
            "approval_ref": None,
            "correlation_id": None,
            "supersedes_ids": [],
            "superseded_by_ids": [],
            "correction_type": None,
            "effective_correction_time": None,
            "recorded_correction_time": None,
        },
        "extensions": {},
        "relationship_family": "technology_usage",
        "relationship_type": "uses_platform",
        "participants": [
            {
                "party_ref": canonical_ref("org-sfo", "Organization"),
                "contextual_role": "user_organization",
                "role_qualifier": None,
            },
            {
                "party_ref": canonical_ref("org-servicenow", "Organization"),
                "contextual_role": "platform_provider",
                "role_qualifier": None,
            },
        ],
        "scope_refs": [canonical_ref("opp-001", "Opportunity")],
        "relationship_state": "active",
    }


def prepared_kernel() -> BusinessRealityKernel:
    kernel = BusinessRealityKernel()
    kernel.append_raw_evidence(raw_evidence())
    kernel.propose_candidate(relationship_candidate())
    return kernel


def test_typed_relationship_contract_is_promotable() -> None:
    kernel = prepared_kernel()

    record = kernel.promote_candidate(
        "cand-relationship-001",
        typed_relationship(),
        actor="koe-test",
        reason="Accepted relationship evidence",
    )

    assert kernel.contracts.semantic_schema_path("TypedRelationship") == (
        "schemas/kernel/typed-relationship.schema.json"
    )
    assert record.evidence_ids == ("ev-relationship-001",)
    assert kernel.get_object("relationship-001")["relationship_state"] == "active"


@pytest.mark.parametrize(
    ("path", "value"),
    [
        (("participants", 0, "contextual_role"), ""),
        (("relationship_state",), "invented"),
        (("participants",), [typed_relationship()["participants"][0]]),
    ],
)
def test_invalid_typed_relationship_shapes_are_rejected(path: tuple, value: object) -> None:
    resource = typed_relationship()
    target = resource
    for part in path[:-1]:
        target = target[part]
    target[path[-1]] = value

    with pytest.raises(ContractViolation):
        prepared_kernel().promote_candidate(
            "cand-relationship-001",
            resource,
            actor="koe-test",
            reason="Should fail contract validation",
        )


def test_typed_relationship_candidate_type_mismatch_is_rejected() -> None:
    resource = typed_relationship()
    resource["type"] = "Organization"

    with pytest.raises(CandidateSemanticTypeMismatch):
        prepared_kernel().promote_candidate(
            "cand-relationship-001",
            resource,
            actor="koe-test",
            reason="Should fail semantic type compatibility",
        )


def test_typed_relationship_correction_preserves_history() -> None:
    kernel = prepared_kernel()
    original = typed_relationship()
    kernel.promote_candidate(
        "cand-relationship-001",
        original,
        actor="koe-test",
        reason="Initial interpretation",
    )

    corrected = copy.deepcopy(original)
    corrected["relationship_state"] = "terminated"
    corrected["audit"]["last_changed_by"] = "koe-reviewer"
    corrected["audit"]["last_changed_at"] = NOW
    corrected["audit"]["change_reason"] = "Relationship ended"
    corrected["audit"]["correction_type"] = "relationship_correction"
    corrected["audit"]["effective_correction_time"] = NOW
    corrected["audit"]["recorded_correction_time"] = NOW

    kernel.correct_canonical_state(
        "relationship-001",
        corrected,
        actor="koe-reviewer",
        reason="Preserve terminated relationship history",
    )

    assert [item["relationship_state"] for item in kernel.get_history("relationship-001")] == [
        "active",
        "terminated",
    ]
