from src.audit import build_audit_event
from src.models import PolicyDecision, ToolDefinition, ToolRequest, UserContext


def test_audit_event_contains_core_fields() -> None:
    request = ToolRequest(
        user=UserContext(user_id="u-9", roles=("security_manager",)),
        tool=ToolDefinition(
            name="close_incident",
            allowed_roles=("security_manager",),
            action_type="write",
            requires_approval=True,
        ),
        target="incident-999",
    )
    decision = PolicyDecision(
        outcome="REQUIRE_APPROVAL",
        reason="Sensitive write action requires explicit human approval.",
        matched_roles=("security_manager",),
    )
    event = build_audit_event(request, decision)

    assert event["user_id"] == "u-9"
    assert event["tool"] == "close_incident"
    assert event["decision"] == "REQUIRE_APPROVAL"
    assert event["matched_roles"] == ["security_manager"]
