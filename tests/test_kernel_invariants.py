from __future__ import annotations

import copy

import pytest

from gensigma_br import (
    BusinessRealityKernel,
    CandidateSemanticTypeMismatch,
    CanonicalResourceConflict,
    ContractViolation,
    EvidenceConflict,
    RelationshipInvariantViolation,
    UnknownEvidence,
    UnknownSemanticType,
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


def raw_evidence() -> dict:
    return {
        "evidence_id": "ev-001",
        "source_system": "outlook",
        "source_tenant": "gensigma.com",
        "source_container": "vijayt@gensigma.com/inbox",
        "source_record_id": "msg-001",
        "source_version": None,
        "source_reference": "outlook://msg-001",
        "source_created_time": NOW,
        "source_modified_time": NOW,
        "acquired_time": NOW,
        "content_hash": "sha256:abc",
        "content_pointer": "evidence://ev-001",
        "security": security(),
        "parent_evidence_id": None,
        "origin_evidence_id": None,
        "ingestion_run_id": "run-001",
    }


def candidate() -> dict:
    return {
        "candidate_id": "cand-org-001",
        "candidate_type": "entity",
        "proposed_semantic_type": "Organization",
        "subject_refs": [],
        "context_refs": [],
        "observation_ids": [],
        "source_evidence_ids": ["ev-001"],
        "epistemic_status": "unresolved",
        "resolution_status": "proposed",
        "security": security(),
        "created_at": NOW,
    }


def organization(name: str = "San Francisco International Airport") -> dict:
    return {
        "id": "org-sfo",
        "type": "Organization",
        "model_owner": "business_reality",
        "contract_version": "0.1",
        "display_name": name,
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
        "canonical_name": name,
        "organization_kind": "customer",
        "website_domain": None,
        "external_identifiers": [],
        "operational_status": "active",
    }


def test_raw_evidence_replay_is_idempotent_and_mutation_is_rejected() -> None:
    kernel = BusinessRealityKernel()
    evidence = raw_evidence()

    assert kernel.append_raw_evidence(evidence) is True
    assert kernel.append_raw_evidence(copy.deepcopy(evidence)) is False

    changed = copy.deepcopy(evidence)
    changed["content_hash"] = "sha256:different"
    with pytest.raises(EvidenceConflict):
        kernel.append_raw_evidence(changed)


def test_candidate_must_reference_existing_evidence() -> None:
    kernel = BusinessRealityKernel()
    with pytest.raises(UnknownEvidence):
        kernel.propose_candidate(candidate())


def test_canonical_promotion_preserves_evidence_lineage() -> None:
    kernel = BusinessRealityKernel()
    kernel.append_raw_evidence(raw_evidence())
    kernel.propose_candidate(candidate())

    record = kernel.promote_candidate(
        "cand-org-001",
        organization(),
        actor="ca-test",
        reason="Accepted after identity reconciliation",
    )

    assert record.resource_id == "org-sfo"
    assert record.candidate_id == "cand-org-001"
    assert record.evidence_ids == ("ev-001",)
    assert kernel.get_object("org-sfo")["canonical_name"] == "San Francisco International Airport"


def test_candidate_semantic_type_mismatch_is_rejected_before_promotion() -> None:
    kernel = BusinessRealityKernel()
    kernel.append_raw_evidence(raw_evidence())
    kernel.propose_candidate(candidate())

    mismatched = organization()
    mismatched["type"] = "Agreement"

    with pytest.raises(CandidateSemanticTypeMismatch, match="proposes 'Organization'"):
        kernel.promote_candidate(
            "cand-org-001",
            mismatched,
            actor="ca-test",
            reason="Should fail semantic type compatibility",
        )


@pytest.mark.parametrize(
    ("semantic_type", "expected_path"),
    [
        ("Event", "schemas/kernel/event.schema.json"),
        ("Decision", "schemas/kernel/decision.schema.json"),
        ("Action", "schemas/kernel/action.schema.json"),
        ("Outcome", "schemas/kernel/outcome.schema.json"),
    ],
)
def test_kernel_canonical_semantic_types_resolve_without_moving_contracts(
    semantic_type: str, expected_path: str
) -> None:
    kernel = BusinessRealityKernel()
    assert kernel.contracts.semantic_schema_path(semantic_type) == expected_path


def test_unknown_semantic_type_fails_clearly() -> None:
    kernel = BusinessRealityKernel()
    with pytest.raises(UnknownSemanticType, match="No promotable semantic contract"):
        kernel.contracts.semantic_schema_path("ImaginaryType")


def test_wrong_business_shape_is_rejected_by_contract() -> None:
    kernel = BusinessRealityKernel()
    kernel.append_raw_evidence(raw_evidence())
    kernel.propose_candidate(candidate())

    invalid = organization()
    del invalid["canonical_name"]
    with pytest.raises(ContractViolation):
        kernel.promote_candidate(
            "cand-org-001",
            invalid,
            actor="ca-test",
            reason="Should fail",
        )


def test_correction_preserves_prior_interpretation() -> None:
    kernel = BusinessRealityKernel()
    kernel.append_raw_evidence(raw_evidence())
    kernel.propose_candidate(candidate())
    kernel.promote_candidate(
        "cand-org-001",
        organization("SF Airport"),
        actor="ca-test",
        reason="Initial accepted interpretation",
    )

    corrected = organization("San Francisco International Airport")
    corrected["audit"]["last_changed_by"] = "reviewer-001"
    corrected["audit"]["last_changed_at"] = NOW
    corrected["audit"]["change_reason"] = "Canonical-name correction"
    corrected["audit"]["correction_type"] = "state_correction"
    corrected["audit"]["effective_correction_time"] = NOW
    corrected["audit"]["recorded_correction_time"] = NOW

    kernel.correct_canonical_state(
        "org-sfo",
        corrected,
        actor="reviewer-001",
        reason="Correct canonical display name",
    )

    history = kernel.get_history("org-sfo")
    assert len(history) == 2
    assert history[0]["canonical_name"] == "SF Airport"
    assert history[1]["canonical_name"] == "San Francisco International Airport"


def canonical_ref(resource: dict) -> dict:
    return {
        "id": resource["id"],
        "type": resource["type"],
        "model_owner": resource["model_owner"],
        "contract_version": resource["contract_version"],
        "projection_version": None,
    }


def add_organization(
    kernel: BusinessRealityKernel, resource_id: str, name: str
) -> dict:
    evidence = raw_evidence()
    evidence["evidence_id"] = f"ev-{resource_id}"
    evidence["source_record_id"] = f"msg-{resource_id}"
    evidence["source_reference"] = f"outlook://msg-{resource_id}"
    evidence["content_hash"] = f"sha256:{resource_id}"
    evidence["content_pointer"] = f"evidence://ev-{resource_id}"
    kernel.append_raw_evidence(evidence)

    proposed = candidate()
    proposed["candidate_id"] = f"cand-{resource_id}"
    proposed["source_evidence_ids"] = [evidence["evidence_id"]]
    kernel.propose_candidate(proposed)

    resource = organization(name)
    resource["id"] = resource_id
    kernel.promote_candidate(
        proposed["candidate_id"],
        resource,
        actor="relationship-test",
        reason="Create relationship endpoint",
    )
    return resource


def relationship_candidate(kernel: BusinessRealityKernel) -> dict:
    evidence = raw_evidence()
    evidence["evidence_id"] = "ev-rel-001"
    evidence["source_record_id"] = "msg-rel-001"
    evidence["source_reference"] = "outlook://msg-rel-001"
    evidence["content_hash"] = "sha256:rel-001"
    evidence["content_pointer"] = "evidence://ev-rel-001"
    kernel.append_raw_evidence(evidence)

    proposed = candidate()
    proposed["candidate_id"] = "cand-rel-001"
    proposed["candidate_type"] = "relationship"
    proposed["proposed_semantic_type"] = "BusinessRelationship"
    proposed["source_evidence_ids"] = ["ev-rel-001"]
    kernel.propose_candidate(proposed)
    return proposed


def business_relationship(
    left: dict, right: dict, scope: dict
) -> dict:
    return {
        "id": "rel-partner-001",
        "type": "BusinessRelationship",
        "model_owner": "business_reality",
        "contract_version": "0.1",
        "display_name": "Scoped teaming relationship",
        "lifecycle_state": "active",
        "effective_time": {
            "valid_from": NOW,
            "valid_to": None,
            "precision": "exact",
        },
        "source_time": NOW,
        "recorded_at": NOW,
        "discovered_at": NOW,
        "epistemic_status": "accepted",
        "provenance_refs": [],
        "security": security(),
        "source_mappings": [],
        "aliases": [],
        "audit": {
            "created_by": "relationship-test",
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
        "relationship_family": "Commercial",
        "relationship_type": "partner_in",
        "participants": [
            {
                "participant_ref": canonical_ref(left),
                "contextual_role": "TeamingPartner",
                "role_qualifier": None,
            },
            {
                "participant_ref": canonical_ref(right),
                "contextual_role": "PrimeContractor",
                "role_qualifier": None,
            },
        ],
        "scope_refs": [canonical_ref(scope)],
        "relationship_state": "active",
    }


def setup_relationship_kernel() -> tuple[
    BusinessRealityKernel, dict, dict, dict, dict
]:
    kernel = BusinessRealityKernel()
    left = add_organization(kernel, "org-partner", "Northstar Consulting")
    right = add_organization(kernel, "org-gensigma", "GenSigma")
    unrelated = add_organization(kernel, "org-unrelated", "Unrelated Organization")
    relationship_candidate(kernel)
    relationship = business_relationship(left, right, right)
    return kernel, left, right, unrelated, relationship


def test_business_relationship_is_promoted_and_traversable_from_either_participant() -> None:
    kernel, left, right, _, relationship = setup_relationship_kernel()

    record = kernel.promote_candidate(
        "cand-rel-001",
        relationship,
        actor="relationship-reviewer",
        reason="Evidence supports scoped teaming relationship",
    )

    assert record.evidence_ids == ("ev-rel-001",)
    assert kernel.get_relationships(left["id"]) == [relationship]
    assert kernel.get_relationships(right["id"]) == [relationship]


def test_relationship_query_filters_type_and_scope_without_inferring_other_scope() -> None:
    kernel, left, right, unrelated, relationship = setup_relationship_kernel()
    kernel.promote_candidate(
        "cand-rel-001",
        relationship,
        actor="relationship-reviewer",
        reason="Evidence supports scoped teaming relationship",
    )

    assert kernel.get_relationships(
        left["id"], relationship_type="partner_in", scope_id=right["id"]
    ) == [relationship]
    assert kernel.get_relationships(
        left["id"], relationship_type="customer_of"
    ) == []
    assert kernel.get_relationships(
        left["id"], scope_id=unrelated["id"]
    ) == []


def test_relationship_rejects_unknown_or_incompatible_canonical_references() -> None:
    kernel, left, right, _, relationship = setup_relationship_kernel()
    relationship["participants"][0]["participant_ref"]["id"] = "org-missing"
    with pytest.raises(RelationshipInvariantViolation, match="is not canonical"):
        kernel.promote_candidate(
            "cand-rel-001",
            relationship,
            actor="relationship-reviewer",
            reason="Should fail missing participant",
        )

    relationship = business_relationship(left, right, right)
    relationship["participants"][0]["participant_ref"]["type"] = "Person"
    with pytest.raises(RelationshipInvariantViolation, match="incompatible type"):
        kernel.promote_candidate(
            "cand-rel-001",
            relationship,
            actor="relationship-reviewer",
            reason="Should fail incompatible reference",
        )


def test_relationship_rejects_duplicate_participant_role_tuple() -> None:
    kernel, left, right, _, relationship = setup_relationship_kernel()
    relationship["participants"][1] = copy.deepcopy(relationship["participants"][0])

    with pytest.raises(RelationshipInvariantViolation, match="cannot repeat"):
        kernel.promote_candidate(
            "cand-rel-001",
            relationship,
            actor="relationship-reviewer",
            reason="Should fail duplicate participant role",
        )


def test_business_relationship_requires_relationship_candidate() -> None:
    kernel, left, right, _, relationship = setup_relationship_kernel()
    entity_candidate = candidate()
    entity_candidate["candidate_id"] = "cand-entity-rel"
    entity_candidate["proposed_semantic_type"] = "BusinessRelationship"
    entity_candidate["source_evidence_ids"] = ["ev-rel-001"]
    kernel.propose_candidate(entity_candidate)

    with pytest.raises(RelationshipInvariantViolation, match="relationship candidate"):
        kernel.promote_candidate(
            "cand-entity-rel",
            relationship,
            actor="relationship-reviewer",
            reason="Should fail candidate category",
        )


def test_relationship_correction_preserves_history_and_updates_current_traversal() -> None:
    kernel, left, right, _, relationship = setup_relationship_kernel()
    kernel.promote_candidate(
        "cand-rel-001",
        relationship,
        actor="relationship-reviewer",
        reason="Initial relationship interpretation",
    )

    corrected = copy.deepcopy(relationship)
    corrected["relationship_type"] = "subcontractor_in"
    corrected["participants"][0]["contextual_role"] = "Subcontractor"
    corrected["audit"]["last_changed_by"] = "relationship-reviewer"
    corrected["audit"]["last_changed_at"] = NOW
    corrected["audit"]["change_reason"] = "Correct contextual relationship"
    corrected["audit"]["correction_type"] = "relationship_correction"
    corrected["audit"]["effective_correction_time"] = NOW
    corrected["audit"]["recorded_correction_time"] = NOW

    kernel.correct_canonical_state(
        relationship["id"],
        corrected,
        actor="relationship-reviewer",
        reason="Correct partner role to subcontractor",
    )

    history = kernel.get_history(relationship["id"])
    assert [item["relationship_type"] for item in history] == [
        "partner_in",
        "subcontractor_in",
    ]
    assert kernel.get_relationships(
        left["id"], relationship_type="subcontractor_in"
    ) == [corrected]
    assert kernel.get_relationships(
        left["id"], relationship_type="partner_in"
    ) == []


def test_second_promotion_cannot_bypass_canonical_correction_history() -> None:
    kernel, _, _, _, relationship = setup_relationship_kernel()
    kernel.promote_candidate(
        "cand-rel-001",
        relationship,
        actor="relationship-reviewer",
        reason="Initial relationship interpretation",
    )

    second_candidate = candidate()
    second_candidate["candidate_id"] = "cand-rel-002"
    second_candidate["candidate_type"] = "relationship"
    second_candidate["proposed_semantic_type"] = "BusinessRelationship"
    second_candidate["source_evidence_ids"] = ["ev-rel-001"]
    kernel.propose_candidate(second_candidate)

    with pytest.raises(CanonicalResourceConflict, match="use the correction path"):
        kernel.promote_candidate(
            "cand-rel-002",
            relationship,
            actor="relationship-reviewer",
            reason="Should not bypass correction history",
        )
