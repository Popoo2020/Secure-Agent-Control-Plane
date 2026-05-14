from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

ActionType = Literal["read", "write"]
DecisionOutcome = Literal["ALLOW", "DENY", "REQUIRE_APPROVAL"]


@dataclass(frozen=True)
class UserContext:
    user_id: str
    roles: tuple[str, ...]


@dataclass(frozen=True)
class ToolDefinition:
    name: str
    allowed_roles: tuple[str, ...]
    action_type: ActionType
    requires_approval: bool = False


@dataclass(frozen=True)
class ToolRequest:
    user: UserContext
    tool: ToolDefinition
    target: str


@dataclass(frozen=True)
class PolicyDecision:
    outcome: DecisionOutcome
    reason: str
    matched_roles: tuple[str, ...]
