# Crosswalk 002 — Supersede × MirrorTone / MTEL

**External work:** Supersede: Diagnosing and Training the Memory-Update Gap in LLM Agents  
**Status:** VERIFIED_EXTERNAL_MAPPING  
**Scope:** conceptual / benchmark crosswalk; no claim of implementation equivalence

## What Supersede isolates

Supersede studies long-horizon interactions in which previously stored facts are later changed, updated, or retracted. It asks whether a bounded self-maintained memory can preserve the current value rather than continue answering from superseded state.

The paper reports several useful isolation results:

- on the knowledge-update subset of LongMemEval, a frontier model drops from 92% with full context to 77% with bounded self-maintained memory;
- the supersession gap persists across model scale;
- when conversation length increases 24×, reported accuracy falls from 68% to 28%;
- increasing memory proportionally does not measurably recover that loss in the reported setting;
- a reinforcement-learning environment with a supersession-aware reward improves held-out update accuracy on the trained small model, suggesting the gap is trainable rather than merely descriptive.

The paper's central distinction is therefore not simple recall. It is whether obsolete values are actually displaced by current ones in an agent's maintained state.

## MTEL mapping

| Supersede concept | MTEL interpretation | Governance question |
|---|---|---|
| Superseded fact | Premise authority loss | When does the old premise stop being eligible to support downstream state? |
| Current value maintenance | State rebind | Which active states must now point to the replacement value? |
| Bounded self-maintained memory | Controlled working state | Can a compact state surface preserve supersession semantics, not just relevant content? |
| Supersession-aware reward | Verifiable update criterion | Can training or evaluation directly reward current-value correctness rather than proxy task success? |

## Structural overlap

Supersede shows that a system can understand an updated fact in full context yet fail when it must maintain that update through its own bounded memory.

MirrorTone / MTEL interprets this as a dependency-governance problem:

```text
old premise P0
      ↓
derived state D*

new qualified premise P1
      ↓
P0 loses authority
      ↓
identify affected D*
      ↓
invalidate / recompute / rebind
      ↓
continue from qualified state
```

The important invariant is **supersession propagation**: replacing the stored value is insufficient if states derived from the old value continue to steer later action.

## Where MTEL extends the question

Supersede primarily measures whether the maintained memory preserves the current value. MTEL adds several governance questions around that transition:

- Was the new correction or update qualified before replacing the old premise?
- Which conclusions, plans, or tool choices depended materially on the superseded premise?
- Which dependents must be invalidated, and which can safely remain?
- Did rebind occur before the next action acquired authority?
- If stale state already crossed into execution, which dependent claims or actions require rollback?

This creates a narrower engineering target than global reset: **dependency-scoped invalidation and rebind**.

## Relationship to Public Exit 003

Public Exit 003 expresses the public-facing version of the same problem:

> **Correction is not rebind.**

A system can acknowledge the new value while continuing from old dependent state. The benchmark candidate MTEL-CR-001 turns that distinction into an observable paired test.

## What this crosswalk does **not** claim

- Supersede is not a MirrorTone benchmark.
- MirrorTone / MTEL is not claimed to outperform Supersede or the systems it evaluates.
- Supersede does not itself require an explicit dependency graph.
- The MTEL dependency-rebind framing is an engineering extension, not a claim about Supersede's internal architecture.
- MTEL-CR-001 remains a candidate fixture until rerunnable evidence exists.

## External source

- Supersede: Diagnosing and Training the Memory-Update Gap in LLM Agents  
  https://arxiv.org/abs/2606.27472

## Derived repo artifacts

- [`Public Exit 003 — Correction Is Not Rebind`](../public-exit/003_correction_is_not_rebind.md)
- [`MTEL-CR-001 — Dependency Rebind Pair`](../benchmark/MTEL-CR-001_dependency_rebind_pair.md)
