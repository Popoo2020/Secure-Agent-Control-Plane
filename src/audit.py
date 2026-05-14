from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from .models import PolicyDecision, ToolRequest


def build_audit_event(request: ToolRequest, decision: PolicyDecision) -> dict[str, Any]:
    """Build a structured audit event for a policy evaluation outcome."""
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "user_id": request.user.user_id,
        "roles": list(request.user.roles),
        "tool": request.tool.name,
        "action_type": request.tool.action_type,
        "target": request.target,
        "decision": decision.outcome,
        "reason": decision.reason,
        "matched_roles": list(decision.matched_roles),
    }
