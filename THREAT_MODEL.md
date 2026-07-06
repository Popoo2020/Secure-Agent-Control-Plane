# Threat Model

## Scope

This threat model covers the policy-as-code demonstration for governing agentic tool access. The repository currently models users, roles, tool definitions, policy loading, policy decisions and audit events. It does not execute real tools.

## Assets

- Policy YAML files and tool definitions.
- User role context.
- Approval requirements for write actions.
- Policy decisions and audit events.
- CI workflows and dependency manifests.

## Trust boundaries

1. Policy YAML input to typed `ToolDefinition` objects.
2. User role context to policy evaluation.
3. Policy decision to any future tool-execution layer.
4. Audit event creation to storage/logging.
5. Repository changes to CI validation.

## Primary risks and controls

| Risk | Impact | Existing control | Additional note |
|---|---|---|---|
| Policy file tampering | Unauthorised access decisions | YAML schema validation and duplicate tool rejection | Protect policy files with code review in production. |
| Over-permissive roles | Users receive broader access than intended | Deny by default when no role matches | Add negative tests for every sensitive tool. |
| Approval bypass | Sensitive write action executes without review | `REQUIRE_APPROVAL` outcome for write actions that require approval | Future execution layer must enforce the decision, not just log it. |
| Unsafe YAML parsing | Arbitrary object loading | `yaml.safe_load` is used by the loader | Keep unsafe loaders out of the codebase. |
| Audit gaps | Poor forensic visibility | Structured audit model and tests | Production deployments should use append-only storage. |
| CI regression | Policy logic changes without validation | ruff, pytest, Bandit, pip-audit and CodeQL | Keep workflows required before merging. |

## Security invariants

- Requests without an authorised role must be denied.
- Sensitive write actions marked as requiring approval must not be allowed directly.
- Policy loading must reject malformed or duplicate tool definitions.
- Audit records must not be treated as enforcement by themselves.
- The future execution layer must enforce policy outcomes before running tools.

## Out of scope

- Real identity-provider integration.
- Durable enterprise approval workflows.
- Execution of external tools.
- Production-grade audit-log immutability.
