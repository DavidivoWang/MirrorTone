# Public Exit 003 — Correction Is Not Rebind

**Status:** PUBLIC_PROBE  
**Evidence level:** externally anchored + internally synthesized  
**Claim ceiling:** governance research framing; not a claim that every correction requires global recomputation

## Public probe

An AI agent can accept a correction and still continue reasoning from the premise that the correction replaced.

That is a different failure from simply ignoring the update.

A correction may change one fact, preference, plan, constraint, or target. But if downstream conclusions, subgoals, tool choices, or completion criteria were derived from the old value, updating the local sentence is not enough.

So the important question is not only:

> Did the agent accept the correction?

It is also:

> Which dependent states lost their support when that premise changed, and were they rebound before the agent continued?

This is the distinction captured by a MirrorTone / MTEL rule:

> **Correction is not rebind. Updating a premise does not automatically invalidate or rebuild its dependents.**

## MTEL probe

**When a material premise changes, can the agent identify and rebind the downstream states that depended on it before those states regain action authority?**

## Why this is now a public candidate

Recent long-horizon memory work makes the supersession gap directly measurable.

Supersede isolates cases where a fact is later revised — for example, a user moves, a price changes, or a plan is updated — and shows that bounded self-maintained memory loses substantial accuracy on knowledge-update tasks even when the underlying model can understand the full context. On a frontier model reported in the paper, accuracy falls from 92% with full context to 77% with bounded self-managed memory. The paper also reports that increasing the available memory does not by itself close the gap as conversations scale.

STALE exposes a related downstream problem: models may retrieve newer evidence yet fail to apply the updated state consistently in later behavior, and they struggle when a change in one part of the state should invalidate related memories.

A separate correction-selectivity benchmark, SycoBench-600, adds an important admission boundary: a reliable system should accept correct corrections without capitulating to incorrect user pressure.

Together these results support a two-stage governance problem:

```text
Correction candidate
        ↓
Correction admission
  (is the update qualified?)
        ↓
Dependency invalidation
  (what old conclusions lost support?)
        ↓
Rebind / recompute affected state
        ↓
Action authority restored only where justified
```

The critical transition is **dependency-aware rebind**.

## Governance mapping

```text
Old premise P0
   ↓
Derived states D1, D2, D3

Correction P0 → P1
   ↓
Validate correction
   ↓
Invalidate dependents supported only by P0
   ↓
Re-evaluate / rebind affected dependents
   ↓
Continue from qualified state
```

A final answer can mention the correction correctly while the internal task trajectory still remains bound to the old premise. For agentic systems, the observable question is whether downstream actions and decisions changed in the right places before execution continued.

## Evidence

- Supersede: Diagnosing and Training the Memory-Update Gap in LLM Agents — arXiv:2606.27472  
  https://arxiv.org/abs/2606.27472
- STALE: Can LLM Agents Know When Their Memories Are No Longer Valid? — arXiv:2605.06527  
  https://arxiv.org/abs/2605.06527
- SycoBench-600: Measuring Sycophancy and Correction Selectivity in LLM Assistants — Findings of ACL 2026  
  https://aclanthology.org/2026.findings-acl.1759/

## Non-claims

This note does not claim that every correction should trigger a global reset. Rebinding should be dependency-scoped: unaffected state can remain intact.

It also does not claim that every user correction is authoritative. Some corrections require verification, clarification, or conflict resolution before they can replace the current premise.

The narrower claim is that **once a material correction is admitted, dependent state cannot inherit authority from a premise that has been withdrawn.**
