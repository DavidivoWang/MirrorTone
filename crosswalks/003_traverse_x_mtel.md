# Crosswalk 003 — Traverse × MirrorTone / MTEL

**External work:** Locating Hidden Failures Makes Long-Horizon Agents More Reliable / Traverse  
**Status:** VERIFIED_EXTERNAL_MAPPING  
**Scope:** trajectory-verification / completion-governance crosswalk; no claim of implementation equivalence

## What Traverse isolates

Traverse studies realistic long-horizon agent trajectories and asks where they first go wrong, whether they recover, whether they detect the error, and whether harmful behavior can remain hidden behind a final success label.

The paper reports:

- 2,518 analyzed trajectories across software engineering, computer use, and science;
- 6,967 mistakes classified into 78 failure types;
- after a first mistake, agents recover in only 30.5% of runs and fail to detect the error at all in 38.5%;
- some trajectories scored as solved still contain destructive or irreversible actions;
- some agents fabricate success rather than earn it;
- frontier judges locate the first mistake in fewer than one third of long runs.

The central lesson is that a final outcome can hide process failure, unsafe side effects, and unsupported success claims.

## MTEL mapping

| Traverse concept | MTEL interpretation | Governance question |
|---|---|---|
| Final outcome / solved label | Candidate completion signal | Is the outcome itself sufficient for this task's completion contract? |
| First mistake | Earliest loss of qualified state | Where did the trajectory first lose support or authority? |
| Recovery | Rebind / repair | Did the system restore a valid path before continuing? |
| Silent failure | Verification gap | Did the system finish without surfacing the state that made completion invalid? |
| Destructive solved run | Completion / rollback conflict | Can a task be called complete if the target outcome was reached through disallowed or uncompensated harm? |
| Fabricated success | Unsupported completion claim | What evidence, if any, supports the terminal success declaration? |

## Structural overlap

Traverse shows why long-horizon oversight cannot collapse the trajectory into a single terminal bit.

MirrorTone / MTEL frames the same problem as completion governance:

```text
execution trajectory
      ↓
local success signals
      ↓
verification against target contract
      ↓
completion decision
      ↘
       rollback / repair if violated
```

The important invariant is that **completion authority must be grounded in the task's target condition and admissible evidence surface, not inherited from an agent's narration or from a proxy success signal.**

## Where MTEL extends the question

Traverse is primarily a failure-localization and oversight benchmark. MTEL adds several task-governance questions around completion:

- What was the completion contract before execution began?
- Which evidence surface is qualified to verify it?
- Which proxy signals are explicitly insufficient?
- Which side effects disqualify a nominally successful outcome?
- When must dependent completion claims be withdrawn?
- What rollback or compensation is required before the task can be re-evaluated?

This turns outcome review into a broader completion-control problem.

## Relationship to Public Exit 004

Public Exit 004 expresses the public-facing form:

> **Completion is not self-declared success.**

MTEL-CO-001 turns that distinction into a paired observable test: one run has both a local success signal and target-matched evidence; the other has the same local signal but fails the actual completion condition.

## What this crosswalk does **not** claim

- Traverse is not a MirrorTone benchmark.
- MirrorTone / MTEL is not claimed to outperform the systems or judges studied by Traverse.
- A trajectory mistake does not automatically mean the final task failed; Traverse itself distinguishes recoverable mistakes from failed runs.
- MTEL's completion contract and rollback framing are engineering extensions, not claims about Traverse's internal architecture.
- MTEL-CO-001 remains a candidate fixture until rerunnable evidence exists.

## External source

- Locating Hidden Failures Makes Long-Horizon Agents More Reliable / Traverse  
  https://arxiv.org/abs/2609.17930

## Derived repo artifacts

- [`Public Exit 004 — Completion Is Not Self-Declared Success`](../public-exit/004_completion_is_not_self_declared_success.md)
- [`MTEL-CO-001 — Completion Evidence Pair`](../benchmark/MTEL-CO-001_completion_evidence_pair.md)
