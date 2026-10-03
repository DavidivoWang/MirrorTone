# Governance Primitives

This directory contains the compact public vocabulary used to examine agentic AI systems.

The current working set is:

## 1. Capability
What can the system do?

Capability describes available competence, tools, reach, persistence, or autonomy. It does **not** by itself grant permission to act.

## 2. Authority
Who or what authorizes the action, decision, state transition, or claim?

Authority should be explicit enough to identify its scope, boundary, and revocation condition.

## 3. Evidence
What evidence supports the system's claim, state, decision, or completion status?

Retrieval, vendor statements, memory, popularity, and prior state are not automatically equivalent to qualified evidence for the current claim.

## 4. Rollback
What happens when an action is wrong, stale, over-scoped, or no longer authorized?

Rollback includes withdrawal of dependent conclusions, state correction, reversal where possible, and a clear boundary when reversal is not possible.

## 5. Completion
Who or what is qualified to decide that the task is complete?

A generated answer, successful tool call, commit, deployment signal, or self-declared success does not necessarily satisfy the task's actual completion criterion.

---

## Relationship

These primitives are most useful as a chain rather than as isolated labels:

```text
Capability
    ↓
Authority
    ↓
Evidence
    ↓
Execution / decision
    ↓
Completion check
    ↘
     Rollback when required
```

They are a public research vocabulary, not a replacement for the full MirrorTone / MTEL runtime governance system.
