from __future__ import annotations

import copy
from collections.abc import Mapping
from typing import Any, Protocol


class PolicyDecisionPoint(Protocol):
    """Technology-neutral policy decision point."""

    def evaluate(self, request: dict[str, Any]) -> dict[str, Any]: ...


def _decision(
    value: str,
    reason_code: str,
    *,
    permitted_properties: list[str] | None = None,
    denied_properties: list[str] | None = None,
    evidence_access: str = "none",
    permitted_evidence_refs: list[str] | None = None,
    obligations: list[str] | None = None,
    evaluated_references: list[dict[str, str]] | None = None,
    disclose_existence: bool = False,
) -> dict[str, Any]:
    return {
        "contract_version": "0.1",
        "decision": value,
        "reason_code": reason_code,
        "permitted_properties": permitted_properties or [],
        "denied_or_redacted_properties": denied_properties or [],
        "evidence_access": evidence_access,
        "permitted_evidence_refs": permitted_evidence_refs or [],
        "obligations": obligations or [],
        "evaluated_references": evaluated_references or [],
        "disclose_existence": disclose_existence,
    }


class DenyAllPolicyDecisionPoint:
    """Fail-closed default used when no policy decision point is configured."""

    def evaluate(self, request: dict[str, Any]) -> dict[str, Any]:
        del request
        return _decision("deny", "pdp_not_configured")


class PermissiveTestPolicyDecisionPoint:
    """Explicit test-only evaluator for tests where authorization is not the subject."""

    def evaluate(self, request: dict[str, Any]) -> dict[str, Any]:
        return _decision(
            "allow",
            "explicit_test_allow",
            permitted_properties=["*"],
            evidence_access="full",
            evaluated_references=[
                {
                    "reference": "test:pdp:permissive",
                    "kind": "policy",
                    "status": "allow",
                }
            ],
        )


class ReferencePolicyDecisionPoint:
    """Deterministic v0.1 evaluator for contract and non-leakage tests.

    Boolean maps stand in for external policy and source-ACL resolvers. A missing
    or false entry denies. Descriptor allow/deny entries are exact opaque subject
    references, and explicit deny always wins.
    """

    def __init__(
        self,
        *,
        policy_decisions: Mapping[str, bool] | None = None,
        source_acl_decisions: Mapping[str, bool] | None = None,
        disclose_existence_for: frozenset[str] | None = None,
    ) -> None:
        self._policy_decisions = dict(policy_decisions or {})
        self._source_acl_decisions = dict(source_acl_decisions or {})
        self._disclose_existence_for = disclose_existence_for or frozenset()

    def evaluate(self, request: dict[str, Any]) -> dict[str, Any]:
        context = request["security_context"]
        descriptor = request["security_descriptor"]
        subjects = {
            context["actor_id"],
            *context["principal_refs"],
            *context["role_refs"],
            *context["delegation_refs"],
        }
        disclose = bool(subjects & self._disclose_existence_for)
        properties = request["resource_properties"]
        denied_properties = descriptor.get("property_restrictions", [])

        if subjects & set(descriptor.get("denied_principals_or_scopes", [])):
            return _decision(
                "deny",
                "explicit_deny",
                denied_properties=properties,
                disclose_existence=disclose,
            )

        allowed = descriptor.get("allowed_principals_or_scopes", [])
        if allowed and not subjects.intersection(allowed):
            return _decision(
                "deny",
                "allowlist_no_match",
                denied_properties=properties,
                disclose_existence=disclose,
            )

        evaluated: list[dict[str, str]] = []
        for reference in descriptor.get("source_acl_refs", []):
            resolved = self._source_acl_decisions.get(reference)
            status = "allow" if resolved is True else "deny" if resolved is False else "unresolved"
            evaluated.append({"reference": reference, "kind": "source_acl", "status": status})
            if status != "allow":
                return _decision(
                    "deny",
                    "source_acl_denied" if status == "deny" else "source_acl_unresolved",
                    denied_properties=properties,
                    evaluated_references=evaluated,
                    disclose_existence=disclose,
                )

        for reference in descriptor.get("policy_refs", []):
            resolved = self._policy_decisions.get(reference)
            status = "allow" if resolved is True else "deny" if resolved is False else "unresolved"
            evaluated.append({"reference": reference, "kind": "policy", "status": status})
            if status != "allow":
                return _decision(
                    "deny",
                    "policy_denied" if status == "deny" else "policy_unresolved",
                    denied_properties=properties,
                    evaluated_references=evaluated,
                    disclose_existence=disclose,
                )

        if not evaluated:
            return _decision(
                "deny",
                "no_authorizing_policy",
                denied_properties=properties,
                disclose_existence=disclose,
            )

        permitted = [name for name in properties if name not in denied_properties]
        evidence_restrictions = descriptor.get("evidence_restrictions", [])
        evidence_access = "full"
        permitted_evidence_refs: list[str] = ["*"]
        if "*" in evidence_restrictions:
            evidence_access = "none"
            permitted_evidence_refs = []
        elif evidence_restrictions:
            evidence_access = "filtered"
            permitted_evidence_refs = [
                ref
                for ref in request.get("evidence_refs", [])
                if ref not in evidence_restrictions
            ]

        return _decision(
            "allow",
            "all_applicable_policies_allow",
            permitted_properties=permitted,
            denied_properties=list(denied_properties),
            evidence_access=evidence_access,
            permitted_evidence_refs=permitted_evidence_refs,
            evaluated_references=evaluated,
            disclose_existence=disclose,
        )


def project_properties(
    resource: dict[str, Any], decision: dict[str, Any]
) -> dict[str, Any]:
    """Apply the PDP property projection before returning data to a caller."""
    permitted = decision["permitted_properties"]
    projected = copy.deepcopy(resource)
    if "*" not in permitted:
        projected = {key: value for key, value in projected.items() if key in permitted}
    for key in decision["denied_or_redacted_properties"]:
        projected.pop(key, None)
    return projected
