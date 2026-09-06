from __future__ import annotations

import copy

import pytest

from gensigma_br import BusinessRealityKernel, ContractViolation, EvidenceConflict, UnknownEvidence


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
