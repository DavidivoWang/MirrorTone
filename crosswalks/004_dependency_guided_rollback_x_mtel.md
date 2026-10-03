# Crosswalk 004 — Dependency-Guided Rollback Repair × MirrorTone / MTEL

**External work:** From Faulty Memories to Corrected Actions: Dependency-Guided Rollback Repair for Memory-Augmented Agents  
**Status:** VERIFIED_EXTERNAL_MAPPING  
**Scope:** post-failure recovery / rollback-governance crosswalk; no claim of implementation equivalence

## What the external work isolates

Dependency-Guided Rollback Repair studies what happens after a diagnosed faulty memory has already influenced an agent's reasoning, plans, tool actions, answers, or later memory writes.

Its central problem is not fault detection. It is post-failure recovery:

- identify the propagated consequences of the fault;
- preserve state that remains independently justified;
- deactivate unsupported persistent state;
- invalidate unsupported execution nodes;
- selectively replay only affected answer-relevant computation;
- repair both the final answer and active memory state.

The paper explicitly argues that deleting the faulty source or revising the final answer is insufficient after the fault has propagated.

It evaluates the method on 150 controlled tool-use cases plus a 50-case trajectory-derived stress test. Reported recovery reaches 85.3% on the controlled benchmark versus 77.3% for the strongest competing method, and 68.0% on the adapted stress test versus 54.0% for the next best method.

## MTEL mapping

| External concept | MTEL interpretation | Governance question |
|---|---|---|
| Diagnosed faulty memory | Fault source | Which state first lost evidentiary support? |
| Memory-to-action graph | Dependency trace | Which claims, plans, actions, observations, or memories inherited the fault? |
| Independent-support checking | Preservation gate | Which affected-looking states remain valid from separate trusted evidence? |
| Unsupported-state invalidation | Authority withdrawal | Which descendants must lose decision or action authority? |
| Selective replay | Scoped rebind / recomputation | Which affected paths must be regenerated before execution continues? |
| Repaired active store | Recovery state | What state is admissible after repair? |
| Side-effecting tool limitation | Compensation boundary | Can the effect be reversed, or does it require compensation / containment? |

## Structural overlap

The external work's core observation aligns closely with the MTEL rollback problem:

```text
fault detected
      ↓
source invalidated
      ↓
affected dependencies traced
      ↓
independent support preserved
      ↓
unsupported descendants lose authority
      ↓
revert / replay / compensate / contain
      ↓
repaired state verified
```

The useful invariant is that **fault acknowledgement and source deletion are not equivalent to state recovery**.

## Where MTEL extends the question

The paper focuses on instrumented memory-augmented agents and explicitly assumes a diagnosed fault plus runtime provenance. MTEL adds several governance questions around the recovery boundary:

- Who is authorized to perform the recovery action?
- Which recovery surfaces are safe to mutate?
- When is literal rollback invalid because concurrent or external state has changed?
- When must a compensating action replace direct reversal?
- Which completion claims must be withdrawn while recovery is incomplete?
- What readback proves that the post-recovery state is acceptable?
- Which irreversible consequences must remain visible in the audit trail even after compensation?

This broadens rollback from a memory-repair operator into a consequence-governance problem.

## Relationship to Public Exit 005

Public Exit 005 expresses the public-facing form:

> **Rollback is not apology.**

MTEL-RB-001 turns that distinction into a paired recovery test: one case supports safe reversal, while the other requires compensation or forward repair because direct undo would be unsafe or impossible.

## What this crosswalk does **not** claim

- Dependency-Guided Rollback Repair is not a MirrorTone benchmark.
- MirrorTone / MTEL is not claimed to outperform the method or benchmark in the paper.
- The external method assumes instrumented provenance and a diagnosed faulty-memory set; MTEL does not claim those prerequisites are always available.
- The external method explicitly does not undo irreversible external side effects; compensation remains domain-specific.
- MTEL-RB-001 remains a candidate fixture until rerunnable evidence exists.

## External source

- From Faulty Memories to Corrected Actions: Dependency-Guided Rollback Repair for Memory-Augmented Agents  
  https://arxiv.org/abs/2608.10502

## Derived repo artifacts

- [`Public Exit 005 — Rollback Is Not Apology`](../public-exit/005_rollback_is_not_apology.md)
- [`MTEL-RB-001 — Consequence Reconciliation Pair`](../benchmark/MTEL-RB-001_consequence_reconciliation_pair.md)
