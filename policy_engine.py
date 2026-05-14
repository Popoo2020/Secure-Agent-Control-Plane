from __future__ import annotations

from .models import PolicyDecision, ToolRequest


def evaluate_request(request: ToolRequest) -> PolicyDecision:
    matched_roles = tuple(
        role for role in request.user.roles if role in request.tool.allowed_roles
    )

    if not matched_roles:
        return PolicyDecision(
            outcome="DENY",
            reason="No user role is authorised for the requested tool.",
            matched_roles=(),
        )

    if request.tool.action_type == "write" and request.tool.requires_approval:
        return PolicyDecision(
            outcome="REQUIRE_APPROVAL",
            reason="Sensitive write action requires explicit human approval.",
            matched_roles=matched_roles,
        )

    return PolicyDecision(
        outcome="ALLOW",
        reason="Role is authorised and no additional approval gate applies.",
        matched_roles=matched_roles,
    )
