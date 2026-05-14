from src.models import UserContext, ToolDefinition, ToolRequest
from src.policy_engine import evaluate_request


def test_denies_when_role_is_not_allowed() -> None:
    request = ToolRequest(
        user=UserContext(user_id="u-1", roles=("viewer",)),
        tool=ToolDefinition(
            name="close_incident",
            allowed_roles=("security_manager",),
            action_type="write",
            requires_approval=True,
        ),
        target="incident-100",
    )
    decision = evaluate_request(request)
    assert decision.outcome == "DENY"


def test_requires_approval_for_sensitive_write_action() -> None:
    request = ToolRequest(
        user=UserContext(user_id="u-2", roles=("security_analyst",)),
        tool=ToolDefinition(
            name="create_ticket",
            allowed_roles=("security_analyst", "security_manager"),
            action_type="write",
            requires_approval=True,
        ),
        target="incident-200",
    )
    decision = evaluate_request(request)
    assert decision.outcome == "REQUIRE_APPROVAL"


def test_allows_authorised_read_action() -> None:
    request = ToolRequest(
        user=UserContext(user_id="u-3", roles=("security_analyst",)),
        tool=ToolDefinition(
            name="search_logs",
            allowed_roles=("security_analyst",),
            action_type="read",
            requires_approval=False,
        ),
        target="workspace-01",
    )
    decision = evaluate_request(request)
    assert decision.outcome == "ALLOW"
