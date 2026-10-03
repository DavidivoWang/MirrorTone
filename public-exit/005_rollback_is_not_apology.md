# Public Exit 005 — Rollback Is Not Apology

**Status:** PUBLIC_PROBE  
**Evidence level:** externally anchored + internally synthesized  
**Claim ceiling:** governance research framing; rollback may require reversal, compensation, containment, or forward repair rather than literal undo

## Public probe

An AI agent can correctly admit that it made a mistake and still leave the world in the wrong state.

An apology repairs the narrative. It does not automatically repair:

- a changed external state;
- a dependent plan or claim;
- a derived memory;
- a committed tool action;
- a side effect that has already propagated.

So the useful question is not only:

> Did the agent notice and acknowledge the error?

It is also:

> Which consequences of that error are still active, and what observable recovery action returns the system to an acceptable state?

This is the distinction captured by a MirrorTone / MTEL rule:

> **Rollback is not apology. Error acknowledgement does not restore affected state or withdraw downstream consequences.**

## MTEL probe

**After a failure is admitted, can the agent identify the unsupported consequences, preserve independently valid state, and execute the right recovery path before continuing?**

## Why this is now a public candidate

Recent agent-recovery research makes this distinction unusually explicit.

Dependency-Guided Rollback Repair studies persistent-memory agents after a diagnosed fault has already influenced reasoning, tool use, answers, and later memory writes. The paper argues that deleting the faulty source or revising the final response is insufficient because propagated claims, actions, and derived memories can remain active. Its recovery method traces downstream dependencies, preserves state with independent trusted support, invalidates unsupported descendants, and selectively replays affected computation.

On a 150-case controlled benchmark, the method reports 85.3% recovery versus 77.3% for the strongest competing recovery method; on a 50-case trajectory-derived stress test, it reports 68.0% versus 54.0%. The authors explicitly limit the claim: rollback of agent-maintained state cannot undo an irreversible external side effect, which instead requires a resettable interface or domain-specific compensating action.

R2Act provides a complementary systems result. In 302 quality-audited Kubernetes incidents, strong LLM-based methods can identify root-cause services with high accuracy while still selecting invalid recovery actions at much higher rates. Correct diagnosis therefore does not automatically imply valid remediation.

Together these results support a narrow governance proposition: **error recognition, state recovery, and consequence repair are separate stages.**

## Governance mapping

```text
Failure detected / admitted
        ↓
Fault source identified
        ↓
Affected consequences traced
        ↓
Independently supported state preserved
        ↓
Unsupported state invalidated
        ↓
Recovery route selected
   ↙        ↓          ↘
revert   compensate   contain / forward-repair
        ↓
Recovery action executed
        ↓
Target-state readback
        ↓
Continue only from repaired state
```

The central transition is **consequence reconciliation**. A verbal correction can be accurate while the operational state remains wrong.

## Evidence

- From Faulty Memories to Corrected Actions: Dependency-Guided Rollback Repair for Memory-Augmented Agents — arXiv:2608.10502  
  https://arxiv.org/abs/2608.10502
- Can LLMs Really Recover Microservice Failures? A Recovery-Aware Evaluation of Diagnosis-to-Action Reasoning (R2Act) — Microsoft Research / arXiv, 2026  
  https://www.microsoft.com/en-us/research/publication/can-llms-really-recover-microservice-failures-a-recovery-aware-evaluation-of-diagnosis-to-action-reasoning/

## Non-claims

This note does not claim that rollback always means restoring an exact previous snapshot. In concurrent or externally consequential systems, literal undo may be impossible or unsafe.

It also does not claim that every failure requires full replay. Unaffected state should remain intact when it has independent valid support.

The narrower claim is that **acknowledgement closes no operational loop by itself: recovery must reconcile the consequences that remain active after the fault is known.**
