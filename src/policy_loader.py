from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from .models import ToolDefinition

VALID_ACTION_TYPES = {"read", "write"}


def _require_string(value: Any, field_name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} must be a non-empty string")
    return value


def _require_string_list(value: Any, field_name: str) -> tuple[str, ...]:
    if not isinstance(value, list) or not value:
        raise ValueError(f"{field_name} must be a non-empty list")
    if not all(isinstance(item, str) and item.strip() for item in value):
        raise ValueError(f"{field_name} must only contain non-empty strings")
    return tuple(value)


def load_tool_policy(path: Path) -> dict[str, ToolDefinition]:
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ValueError("policy file must contain a YAML object")

    tools = raw.get("tools")
    if not isinstance(tools, list) or not tools:
        raise ValueError("policy file must contain a non-empty tools list")

    definitions: dict[str, ToolDefinition] = {}
    for item in tools:
        if not isinstance(item, dict):
            raise ValueError("each tool entry must be a YAML object")

        name = _require_string(item.get("name"), "tool.name")
        allowed_roles = _require_string_list(item.get("allowed_roles"), "tool.allowed_roles")
        action_type = _require_string(item.get("action_type"), "tool.action_type")
        if action_type not in VALID_ACTION_TYPES:
            raise ValueError(f"invalid action_type for tool {name}: {action_type}")

        requires_approval = item.get("requires_approval", False)
        if not isinstance(requires_approval, bool):
            raise ValueError(f"requires_approval for tool {name} must be boolean")

        if name in definitions:
            raise ValueError(f"duplicate tool definition: {name}")

        definitions[name] = ToolDefinition(
            name=name,
            allowed_roles=allowed_roles,
            action_type=action_type,  # type: ignore[arg-type]
            requires_approval=requires_approval,
        )

    return definitions
