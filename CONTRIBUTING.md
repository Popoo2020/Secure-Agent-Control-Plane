# Contributing

Thanks for your interest in improving **Secure-Agent-Control-Plane**.

This repository is intentionally small and reviewable. Contributions should strengthen the security-control model rather than add broad, ungoverned agent capabilities.

## Good contribution areas

- clearer policy-engine tests,
- additional deny-by-default scenarios,
- richer approval-gate examples,
- audit-event consistency checks,
- documentation improvements,
- architecture diagrams or threat-model notes.

## Contribution rules

Before opening a pull request:

1. keep examples non-destructive,
2. do not include real credentials or private data,
3. avoid adding live tool execution without a policy gate,
4. add or update tests for behaviour changes,
5. keep documentation aligned with implemented functionality.

## Local validation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

## Security expectations

Pull requests that introduce broad tool access, bypass approval checks, or weaken deny-by-default behaviour should include a clear explanation and tests showing why the change is safe.
