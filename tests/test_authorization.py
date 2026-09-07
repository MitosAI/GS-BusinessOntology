from __future__ import annotations

import pytest

from gensigma_br import (
    AuthorizationDenied,
    BusinessRealityKernel,
    ContractRegistry,
    ReferencePolicyDecisionPoint,
    UnknownEvidence,
)


NOW = "2026-09-06T00:00:00Z"


def context(**overrides: object) -> dict:
    value = {
        "actor_id": "actor:alice",
        "actor_type": "human",
        "principal_refs": [],
        "role_refs": [],
        "delegation_refs": [],
        "requested_at": NOW,
    }
    value.update(overrides)
    return value


def descriptor(**overrides: object) -> dict:
    value = {
        "classification": "Normal Business",
        "policy_refs": ["policy:read"],
        "source_acl_refs": [],
        "allowed_principals_or_scopes": [],
        "denied_principals_or_scopes": [],
        "property_restrictions": [],
        "evidence_restrictions": [],
    }
    value.update(overrides)
    return value


def resource(*, security: dict | None = None) -> dict:
    return {
        "id": "org-secure",
        "type": "Organization",
        "model_owner": "business_reality",
        "contract_version": "0.1",
        "display_name": "Visible",
        "secret": "must not leak",
        "recorded_at": NOW,
        "effective_time": {
            "valid_from": NOW,
            "valid_to": None,
            "precision": "exact",
        },
        "provenance_refs": ["evidence:one"],
        "security": security or descriptor(),
    }


def kernel_with(
    pdp: ReferencePolicyDecisionPoint | None,
    *,
    item: dict | None = None,
) -> BusinessRealityKernel:
    kernel = BusinessRealityKernel(policy_decision_point=pdp)
    kernel._canonical_history["org-secure"] = [item or resource()]
    return kernel


def authorization_request(
    *,
    security_context: dict | None = None,
    security_descriptor: dict | None = None,
) -> dict:
    return {
        "contract_version": "0.1",
        "security_context": security_context or context(),
        "operation": "read",
        "resource": {
            "id": "org-secure",
            "kind": "canonical",
            "type": "Organization",
            "model_owner": "business_reality",
            "contract_version": "0.1",
        },
        "security_descriptor": security_descriptor or descriptor(),
        "projection_kind": "canonical_resource",
        "resource_properties": ["display_name", "secret"],
        "evidence_refs": ["evidence:one"],
        "temporal_context": {"as_of": None, "temporal_mode": None},
        "request_context": {},
    }


def evaluate(
    pdp: ReferencePolicyDecisionPoint,
    *,
    security_context: dict | None = None,
    security_descriptor: dict | None = None,
) -> dict:
    return pdp.evaluate(
        authorization_request(
            security_context=security_context,
            security_descriptor=security_descriptor,
        )
    )


def test_authorization_contract_instances_validate() -> None:
    contracts = ContractRegistry("contracts")
    request = authorization_request()
    decision = evaluate(
        ReferencePolicyDecisionPoint(policy_decisions={"policy:read": True})
    )
    contracts.validate(
        "schemas/kernel/authorization-request.schema.json", request
    )
    contracts.validate(
        "schemas/kernel/authorization-decision.schema.json", decision
    )


@pytest.mark.parametrize(
    ("field", "subject"),
    [
        ("actor_id", "actor:alice"),
        ("principal_refs", "principal:finance"),
        ("role_refs", "role:reviewer"),
        ("delegation_refs", "delegation:temporary"),
    ],
)
def test_every_subject_reference_class_can_satisfy_a_nonempty_allowlist(
    field: str, subject: str
) -> None:
    security_context = context()
    if field == "actor_id":
        security_context[field] = subject
    else:
        security_context[field] = [subject]
    decision = evaluate(
        ReferencePolicyDecisionPoint(policy_decisions={"policy:read": True}),
        security_context=security_context,
        security_descriptor=descriptor(
            allowed_principals_or_scopes=[subject]
        ),
    )
    assert decision["decision"] == "allow"


def test_empty_allowlist_is_not_itself_a_grant() -> None:
    decision = evaluate(
        ReferencePolicyDecisionPoint(),
        security_descriptor=descriptor(policy_refs=[]),
    )
    assert (decision["decision"], decision["reason_code"]) == (
        "deny",
        "no_authorizing_policy",
    )


def test_explicit_deny_overrides_allow() -> None:
    decision = evaluate(
        ReferencePolicyDecisionPoint(policy_decisions={"policy:read": True}),
        security_descriptor=descriptor(
            allowed_principals_or_scopes=["actor:alice"],
            denied_principals_or_scopes=["actor:alice"],
        ),
    )
    assert (decision["decision"], decision["reason_code"]) == (
        "deny",
        "explicit_deny",
    )


@pytest.mark.parametrize(
    ("pdp", "reason"),
    [
        (
            ReferencePolicyDecisionPoint(),
            "policy_unresolved",
        ),
        (
            ReferencePolicyDecisionPoint(policy_decisions={"policy:read": False}),
            "policy_denied",
        ),
        (
            ReferencePolicyDecisionPoint(
                policy_decisions={"policy:read": True}
            ),
            "source_acl_unresolved",
        ),
    ],
)
def test_denied_and_unresolved_references_fail_closed(
    pdp: ReferencePolicyDecisionPoint, reason: str
) -> None:
    security_descriptor = descriptor()
    if reason == "source_acl_unresolved":
        security_descriptor["source_acl_refs"] = ["acl:source"]
    decision = evaluate(pdp, security_descriptor=security_descriptor)
    assert (decision["decision"], decision["reason_code"]) == ("deny", reason)


def test_denied_and_missing_canonical_reads_are_indistinguishable() -> None:
    denied = kernel_with(ReferencePolicyDecisionPoint())
    missing = kernel_with(ReferencePolicyDecisionPoint())
    with pytest.raises(KeyError) as denied_error:
        denied.get_object("org-secure", security_context=context())
    with pytest.raises(KeyError) as missing_error:
        missing.get_object("org-missing", security_context=context())
    assert str(denied_error.value).replace("org-secure", "org-missing") == str(
        missing_error.value
    )


def test_diagnostic_authority_may_disclose_an_explicit_denial() -> None:
    kernel = kernel_with(
        ReferencePolicyDecisionPoint(
            disclose_existence_for=frozenset({"role:security-diagnostic"})
        )
    )
    with pytest.raises(AuthorizationDenied, match="policy_unresolved"):
        kernel.get_object(
            "org-secure",
            security_context=context(role_refs=["role:security-diagnostic"]),
        )


def test_property_projection_is_applied_before_return() -> None:
    secured = resource(
        security=descriptor(property_restrictions=["secret"])
    )
    kernel = kernel_with(
        ReferencePolicyDecisionPoint(policy_decisions={"policy:read": True}),
        item=secured,
    )
    projected = kernel.get_object("org-secure", security_context=context())
    assert projected["display_name"] == "Visible"
    assert "secret" not in projected


def test_evidence_access_is_independent_of_canonical_visibility() -> None:
    security = descriptor(evidence_restrictions=["*"])
    kernel = kernel_with(
        ReferencePolicyDecisionPoint(policy_decisions={"policy:read": True}),
        item=resource(security=security),
    )
    kernel._raw_evidence["evidence:one"] = {
        "evidence_id": "evidence:one",
        "security": security,
    }
    assert kernel.get_object(
        "org-secure", security_context=context()
    )["display_name"] == "Visible"
    with pytest.raises(UnknownEvidence):
        kernel.get_raw_evidence(
            "evidence:one", security_context=context()
        )


def test_filtered_evidence_cannot_return_an_excluded_evidence_item() -> None:
    security = descriptor(evidence_restrictions=["evidence:one"])
    kernel = kernel_with(
        ReferencePolicyDecisionPoint(policy_decisions={"policy:read": True})
    )
    kernel._raw_evidence["evidence:one"] = {
        "evidence_id": "evidence:one",
        "security": security,
    }
    with pytest.raises(UnknownEvidence):
        kernel.get_raw_evidence(
            "evidence:one", security_context=context()
        )


def test_hidden_temporal_state_is_authorized_before_precision_is_examined() -> None:
    hidden = resource()
    hidden["effective_time"]["precision"] = "approximate"
    kernel = kernel_with(ReferencePolicyDecisionPoint(), item=hidden)
    with pytest.raises(KeyError):
        kernel.get_state(
            "org-secure",
            as_of=NOW,
            security_context=context(),
        )


@pytest.mark.parametrize(
    "method_name", ["get_promotion_records", "get_correction_records"]
)
def test_audit_record_reads_use_the_same_policy_enforcement_point(
    method_name: str,
) -> None:
    kernel = kernel_with(ReferencePolicyDecisionPoint())
    with pytest.raises(KeyError):
        getattr(kernel, method_name)(
            "org-secure", security_context=context()
        )


def test_unconfigured_kernel_has_no_implicit_allow_fallback() -> None:
    kernel = kernel_with(None)
    with pytest.raises(KeyError):
        kernel.get_object("org-secure", security_context=context())
