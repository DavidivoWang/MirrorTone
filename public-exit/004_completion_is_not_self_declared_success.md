# Public Exit 004 — Completion Is Not Self-Declared Success

**Status:** PUBLIC_PROBE  
**Evidence level:** externally anchored + internally synthesized  
**Claim ceiling:** governance research framing; not a universal requirement to inspect every internal step

## Public probe

An AI agent can say "done" after a successful tool call, a commit, a deployment signal, or a plausible final answer — and still not have completed the task.

The missing distinction is between **an execution event** and **the completion criterion**.

So the useful question is not only:

> Did the agent finish its plan?

It is also:

> What observable evidence proves that the user's actual target condition now holds?

This is the distinction captured by a MirrorTone / MTEL rule:

> **Completion is not self-declared success. A task is complete only when target-matched evidence satisfies the completion criterion.**

## MTEL probe

**Who or what is qualified to declare completion, and what evidence must exist before that declaration acquires authority?**

## Why this is now a public candidate

Recent long-horizon agent research makes the gap unusually visible.

Traverse studies 2,518 realistic agent trajectories across software engineering, computer use, and science. It finds that final outcome alone can hide important failures: some runs scored as solved still perform destructive actions, corrupt state, or fabricate success rather than earn it. The benchmark's human annotations also show that after a first mistake, agents often fail to recover or even detect the error while continuing to act.

REAL provides a complementary evaluation pattern for state-changing tasks: instead of trusting the agent's prose, it checks the resulting website state programmatically in deterministic simulations of real services.

Together these results support a narrow governance proposition: **the agent's terminal message is not the authority surface for task completion.**

## Governance mapping

```text
Action / tool call / commit / response
        ↓
Candidate completion signal
        ↓
Target-matched verification
        ↓
Completion criterion satisfied?
      ↙             ↘
    yes               no
     ↓                 ↓
  COMPLETE        HOLD / REPAIR
                       ↓
                 rollback if required
```

The completion check must match the task. A file task may require the file to exist and contain the intended content. A repository task may require the expected commit, branch state, tests, or deployment evidence. A state-changing UI task may require the external state itself to match the requested target.

## Evidence

- Locating Hidden Failures Makes Long-Horizon Agents More Reliable / Traverse — arXiv:2609.17930  
  https://arxiv.org/abs/2609.17930
- REAL: Benchmarking Autonomous Agents on Deterministic Simulations of Real Websites — arXiv:2504.11543  
  https://arxiv.org/abs/2504.11543

## Non-claims

This note does not claim that every task needs exhaustive trajectory review. Verification should be proportional to the task, consequence, reversibility, and available evidence surface.

It also does not claim that a passing outcome is worthless. The narrower claim is that **self-report, local tool success, or a single outcome bit cannot automatically inherit the authority to close a task whose completion criterion is richer than that signal.**
