from __future__ import annotations

import pytest

from gensigma_br import (
    AmbiguousTemporalState,
    BusinessRealityKernel,
    PermissiveTestPolicyDecisionPoint,
    TemporalQueryError,
    TemporalStateNotFound,
    UnsupportedTemporalPrecision,
)


JAN_1 = "2026-01-01T00:00:00Z"
FEB_1 = "2026-02-01T00:00:00Z"
FEB_15 = "2026-02-15T00:00:00Z"
FEB_20 = "2026-02-20T00:00:00Z"
FEB_25 = "2026-02-25T00:00:00Z"
MAR_1 = "2026-03-01T00:00:00Z"


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


def security_context() -> dict:
    return {
        "actor_id": "test:actor",
        "actor_type": "human",
        "principal_refs": [],
        "role_refs": [],
        "delegation_refs": [],
        "requested_at": JAN_1,
    }


def raw_evidence() -> dict:
    return {
        "evidence_id": "ev-temporal-001",
        "source_system": "outlook",
        "source_record_id": "msg-temporal-001",
        "acquired_time": JAN_1,
        "security": security(),
        "ingestion_run_id": "run-temporal-001",
    }


def candidate() -> dict:
    return {
        "candidate_id": "cand-temporal-001",
        "candidate_type": "entity",
        "proposed_semantic_type": "Organization",
        "subject_refs": [],
        "context_refs": [],
        "observation_ids": [],
        "source_evidence_ids": ["ev-temporal-001"],
        "epistemic_status": "unresolved",
        "resolution_status": "proposed",
        "security": security(),
        "created_at": JAN_1,
    }


def organization(
    name: str,
    *,
    valid_from: str | None = JAN_1,
    valid_to: str | None = None,
    recorded_at: str = JAN_1,
    discovered_at: str | None = JAN_1,
    precision: str = "exact",
) -> dict:
    return {
        "id": "org-temporal",
        "type": "Organization",
        "model_owner": "business_reality",
        "contract_version": "0.1",
        "display_name": name,
        "lifecycle_state": "active",
        "effective_time": {
            "valid_from": valid_from,
            "valid_to": valid_to,
            "precision": precision,
        },
        "source_time": valid_from,
        "recorded_at": recorded_at,
        "discovered_at": discovered_at,
        "epistemic_status": "accepted",
        "provenance_refs": [],
        "security": security(),
        "source_mappings": [],
        "aliases": [],
        "audit": {
            "created_by": "test",
            "created_at": recorded_at,
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


def prepared_kernel(initial: dict | None = None) -> BusinessRealityKernel:
    kernel = BusinessRealityKernel(
        policy_decision_point=PermissiveTestPolicyDecisionPoint()
    )
    kernel.append_raw_evidence(raw_evidence())
    kernel.propose_candidate(candidate())
    kernel.promote_candidate(
        "cand-temporal-001",
        initial or organization("Initial interpretation"),
        actor="test",
        reason="Initial accepted state",
    )
    return kernel


def correct(kernel: BusinessRealityKernel, replacement: dict) -> None:
    kernel.correct_canonical_state(
        "org-temporal",
        replacement,
        actor="reviewer",
        reason="Correct temporal interpretation",
    )


def test_temporal_modes_do_not_project_later_knowledge_backward() -> None:
    kernel = prepared_kernel()
    correct(
        kernel,
        organization(
            "Retroactively corrected",
            valid_from=FEB_1,
            recorded_at=MAR_1,
            discovered_at=FEB_20,
        ),
    )

    effective = kernel.get_state(
        "org-temporal",
        as_of=FEB_15,
        security_context=security_context(),
        temporal_mode="effective_using_current_knowledge",
    )
    recorded = kernel.get_state(
        "org-temporal",
        as_of=FEB_15,
        security_context=security_context(),
        temporal_mode="accepted_as_recorded_at_time",
    )
    discovered_but_not_recorded = kernel.get_state(
        "org-temporal",
        as_of=FEB_25,
        security_context=security_context(),
        temporal_mode="accepted_as_recorded_at_time",
    )

    assert effective["canonical_name"] == "Retroactively corrected"
    assert recorded["canonical_name"] == "Initial interpretation"
    assert discovered_but_not_recorded["canonical_name"] == "Initial interpretation"


def test_exact_effective_intervals_are_half_open() -> None:
    kernel = prepared_kernel(
        organization("Before boundary", valid_to=MAR_1, recorded_at=JAN_1)
    )
    correct(kernel, organization("At boundary", valid_from=MAR_1, recorded_at=FEB_1))

    assert kernel.get_state(
        "org-temporal", as_of=FEB_15, security_context=security_context()
    )["canonical_name"] == "Before boundary"
    assert kernel.get_state(
        "org-temporal", as_of=MAR_1, security_context=security_context()
    )["canonical_name"] == "At boundary"


@pytest.mark.parametrize(
    ("as_of", "mode"),
    [
        ("2026-02-15T00:00:00", "effective_using_current_knowledge"),
        ("not-a-timestamp", "effective_using_current_knowledge"),
        (FEB_15, "invented_mode"),
    ],
)
def test_invalid_temporal_queries_fail_clearly(as_of: str, mode: str) -> None:
    with pytest.raises(TemporalQueryError):
        prepared_kernel().get_state(
            "org-temporal",
            as_of=as_of,
            security_context=security_context(),
            temporal_mode=mode,
        )


def test_no_applicable_temporal_state_fails_clearly() -> None:
    kernel = prepared_kernel(organization("Future", valid_from=MAR_1))
    with pytest.raises(TemporalStateNotFound):
        kernel.get_state(
            "org-temporal", as_of=FEB_15, security_context=security_context()
        )


def test_non_exact_precision_is_not_guessed() -> None:
    kernel = prepared_kernel(organization("Approximate", precision="approximate"))
    with pytest.raises(UnsupportedTemporalPrecision):
        kernel.get_state(
            "org-temporal", as_of=FEB_15, security_context=security_context()
        )


def test_irreducible_overlap_is_reported_as_ambiguous() -> None:
    kernel = prepared_kernel()
    correct(kernel, organization("Conflicting interpretation", recorded_at=JAN_1))
    with pytest.raises(AmbiguousTemporalState):
        kernel.get_state(
            "org-temporal", as_of=FEB_15, security_context=security_context()
        )


def test_temporal_reads_and_current_compatibility_return_copies() -> None:
    kernel = prepared_kernel()
    historical = kernel.get_state(
        "org-temporal", as_of=FEB_15, security_context=security_context()
    )
    historical["canonical_name"] = "mutated by caller"
    assert kernel.get_object(
        "org-temporal", security_context=security_context()
    )["canonical_name"] == "Initial interpretation"
