# Public Exit 002 — Retrieval Is Not Current State

**Status:** PUBLIC_PROBE  
**Evidence level:** externally anchored + internally synthesized  
**Claim ceiling:** governance research framing; not a claim that every task requires live readback

## Public probe

An AI agent can retrieve a fact correctly and still act on the wrong state.

The problem appears when the retrieved fact was true when it was stored, but the world changed afterward.

So for mutable state, a useful question is not only:

> Did the agent retrieve the right memory or source?

It is also:

> What makes that information valid **now** for the action the agent is about to take?

This is the distinction captured by a MirrorTone / MTEL rule:

> **Retrieval is not current state. A source can supply evidence without becoming runtime authority.**

## MTEL probe

**When an action depends on mutable state, what fresh evidence is required before retrieved context is admitted as current?**

## Why this is now a public candidate

The 2026 STALE benchmark directly studies memory invalidation. It contains 400 expert-validated conflict scenarios and 1,200 evaluation queries, including cases where later observations implicitly invalidate earlier memories.

The benchmark separates three capabilities: State Resolution, Premise Resistance, and Implicit Policy Adaptation. Its reported results expose a particularly important gap: agents may retrieve newer evidence yet still continue acting on an outdated state. The best evaluated model reaches 55.2% overall accuracy.

Anthropic's long-horizon agent work independently reinforces the systems distinction. Their Managed Agents architecture separates the append-only session log, the harness, and the sandbox execution environment; the session itself is not the model's context window. Their context-engineering guidance also treats retrieval and working context as curated views over a changing environment rather than as automatic ground truth.

Together, these observations support a narrow governance proposition: **stored history, retrieved context, and current executable state are different surfaces.**

## Governance mapping

```text
Stored source / memory
        ↓
Retrieved candidate evidence
        ↓
Fresh authority-surface readback when state is mutable
        ↓
Current-state admission
        ↓
Action / decision
        ↓
Completion check
        ↘
         Rollback / dependent-claim withdrawal when stale
```

The critical transition is **state admission**. Retrieval makes information available; it does not by itself certify that the information is current enough to authorize an action or a current-state claim.

## Evidence

- STALE: Can LLM Agents Know When Their Memories Are No Longer Valid? — arXiv:2605.06527  
  https://arxiv.org/abs/2605.06527
- Anthropic — Scaling Managed Agents: Decoupling the brain from the hands  
  https://www.anthropic.com/engineering/managed-agents
- Anthropic — Effective context engineering for AI agents  
  https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

## Non-claims

This note does not claim that every retrieved fact requires a live external check. Immutable documents, historical facts, and task-local state may have different freshness requirements.

It also does not claim that memory is unreliable by definition. The narrower claim is that **freshness and authority are properties of the current claim/action relationship, not properties automatically inherited from successful retrieval.**
