# AGENTS.md — AI agent operating policy

## Remote CI is not a phase gate

This repository follows a user-level operating rule for all AI agents.

- The availability or execution of remote CI (GitHub Actions or equivalent) is not a prerequisite for completing a task, closing a development phase, committing authorized work, or reporting local readiness.
- Do not block progress solely because remote CI did not start, is queued/cancelled, or is unavailable because of free-tier minute exhaustion, billing/spending limits, rate limits, provider outages, or similar infrastructure constraints.
- Do not retry or consume limited/paid CI merely to obtain a ceremonial green check unless the current user explicitly asks for it.
- When remote CI is unavailable, run the relevant local equivalents when feasible and report exactly what was executed, exit codes/results, and what remains unverified.
- Never claim remote CI passed if it did not run.
- If CI actually runs and reveals a genuine test/build/security defect, treat the underlying defect as evidence that must be investigated; this policy removes CI availability as a blocker, not real failures.
- Checks that can only run remotely may be recorded as `REMOTE_CI_NOT_RUN` / `UNVERIFIED_REMOTE` without blocking phase progression, unless the current user explicitly makes that remote check mandatory.

If another repository document says a phase/task cannot close only because remote CI has not run or is not green, this section overrides that requirement. Local correctness, relevant tests, review, security constraints, and truthful reporting still apply.
