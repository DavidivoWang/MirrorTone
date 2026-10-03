# MTEL Governance Benchmark

This directory is reserved for governance benchmark and regression cases that emerge from repeated, verifiable failure patterns.

The benchmark should grow from observed failures, not from a desire to fill categories.

## Current candidates

- [`MTEL-CA-001 — Authority Boundary Pair`](MTEL-CA-001_authority_boundary_pair.md) — tests capability vs authorization
- [`MTEL-SE-001 — Fresh-State Admission Pair`](MTEL-SE-001_fresh_state_admission_pair.md) — tests retrieved state vs current action-bearing state
- [`MTEL-CR-001 — Dependency Rebind Pair`](MTEL-CR-001_dependency_rebind_pair.md) — tests correction admission, dependency invalidation, and scoped rebind

All remain **CANDIDATE**. None is a qualified benchmark claim yet.

## Candidate admission rule

A case becomes a benchmark candidate only when the underlying pattern is:

1. **Repeatable** — it can occur again under comparable conditions.
2. **Verifiable** — success and failure can be judged from observable evidence.
3. **Governance-relevant** — it tests authority, evidence, rollback, completion, correction/rebind, or a closely related control boundary.
4. **Generalizable enough** — it is not merely a one-off anecdote tied to one conversation or one vendor-specific quirk.

If these conditions are not met, keep the observation in research notes rather than promoting it into the benchmark.

## Minimal case schema

Each case should include:

```text
ID:
TITLE:
GOVERNANCE_DIMENSION:
SETUP:
PROMPT_OR_EVENT:
EXPECTED_BEHAVIOR:
FAILURE_CRITERION:
OBSERVABLE_EVIDENCE:
ROLLBACK_OR_RECOVERY_EXPECTATION:
STATUS: CANDIDATE / QUALIFIED / RETIRED
```

## Example failure families

These are working families, not a fixed ontology:

- Capability treated as authority
- Retrieved source treated as runtime state
- Retrieval treated as sufficient evidence
- Correction received but dependencies not rebound
- Rollback path absent or incomplete
- Completion declared without target-matched evidence

## Scoring restraint

Do not introduce aggregate scores until individual case semantics, evidence requirements, and pass/fail criteria are stable enough to support them.

The first goal is an inspectable test surface, not a leaderboard.
