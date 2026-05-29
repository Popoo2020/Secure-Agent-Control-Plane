# Security Policy

## Purpose

This repository is a portfolio-grade security architecture lab for governing agentic AI systems. It demonstrates role-aware access control, approval gates, tool allowlists and auditability before sensitive actions are executed.

## Supported use

Use this project only for:

- educational review,
- authorised security architecture discussion,
- local demonstrations,
- portfolio evaluation,
- controlled internal experiments.

It is not a production identity provider, policy engine or tool-execution broker.

## Security posture

The project is designed around conservative defaults:

- deny by default when roles are not explicitly authorised,
- require approval for sensitive write actions,
- separate policy decisions from tool execution,
- record structured audit events for reviewability,
- keep examples deterministic and testable.

## Reporting security issues

If you find a security-relevant issue, open a GitHub issue with:

1. the affected file or behaviour,
2. why the behaviour could create risk,
3. a minimal reproduction example,
4. whether the issue affects documentation, tests or runtime logic.

Do not include real credentials, private tokens, personal data or sensitive third-party information in reports.

## Known limitations

- This is not a production-grade access-control system.
- It does not integrate with a real identity provider yet.
- It does not execute real tools.
- Approval states are implemented for demonstration and testing, not as durable enterprise workflow records.
