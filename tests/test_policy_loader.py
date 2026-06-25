from pathlib import Path

import pytest

from src.policy_loader import load_tool_policy


def test_load_tool_policy_from_yaml_file():
    policy = load_tool_policy(Path("policies/tools.yml"))

    assert set(policy) == {"read_incident", "create_ticket", "close_incident"}
    assert policy["read_incident"].action_type == "read"
    assert policy["create_ticket"].requires_approval is True
    assert policy["close_incident"].allowed_roles == ("security_manager",)


def test_load_tool_policy_rejects_duplicate_names(tmp_path):
    policy_file = tmp_path / "tools.yml"
    policy_file.write_text(
        """
tools:
  - name: duplicate
    allowed_roles: [security_analyst]
    action_type: read
  - name: duplicate
    allowed_roles: [security_manager]
    action_type: write
""".strip(),
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="duplicate tool definition"):
        load_tool_policy(policy_file)


def test_load_tool_policy_rejects_invalid_action_type(tmp_path):
    policy_file = tmp_path / "tools.yml"
    policy_file.write_text(
        """
tools:
  - name: bad_tool
    allowed_roles: [security_analyst]
    action_type: admin
""".strip(),
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="invalid action_type"):
        load_tool_policy(policy_file)
