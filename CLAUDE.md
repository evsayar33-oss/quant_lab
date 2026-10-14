# Task Observer activation

Invoke the `task-observer` skill before the FIRST tool call of every session, and before writing or proposing a plan.

- Workspace folder (pinned): `/home/claude/quant_lab/.claude`
- Observation log: `/home/claude/quant_lab/.claude/skill-observations/observation-log/`
- Substitute this path for `[ABSOLUTE PATH]` in every skill snippet. Keep it in double quotes. Run snippets with bash.
- Commit new observation files to the repo so they persist between sessions.

# quant_lab rules

This repo is the decision center for every trading bot of the owner.

- A bot acts on a strategy only when `decisions/registry.json` has `verdict: ACCEPT` for it (read through `lab/client.py`).
- Every new idea is a hypothesis: add it to `hypotheses/registry.yaml` with a new id. Never reuse an id.
- Never loosen `validation.GATE` to make a hypothesis pass. Any gate change needs a line in `hypotheses/CHANGELOG.md` with the reason.
- New strategies go in `lab/strategies/__init__.py` with `@strategy(...)`, a parameter grid and the source paper. Weights must use data up to close t only.
- Run `python tests/test_core.py` before every commit. All tests must pass.
- Data and tools must be free (no paid API). The owner works only from an Android phone and GitHub Actions.
