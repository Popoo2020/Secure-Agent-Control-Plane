# Policy-as-Code Example

This document shows a simple external policy structure for governing AI-agent requests.

| Capability | Roles | Category | Review required |
|---|---|---|---|
| view_item | reviewer; lead | read | false |
| draft_item_change | reviewer; lead | change | true |
| approve_item_change | lead | change | true |

## Purpose

The policy illustrates that an AI agent should not decide its own authority. Access should be defined outside the prompt and evaluated before the system continues.

## Next implementation step

A future implementation can load this policy from a structured file and convert each row into an internal definition object before calling the policy engine.
