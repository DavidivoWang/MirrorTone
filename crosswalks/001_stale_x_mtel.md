# Crosswalk 001 — STALE × MirrorTone / MTEL

**External work:** STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?  
**Status:** VERIFIED_EXTERNAL_MAPPING  
**Scope:** conceptual / benchmark crosswalk; no claim of implementation equivalence

## What STALE tests

STALE evaluates whether an agent can revise behavior when later evidence invalidates an earlier memory, including implicit rather than explicitly stated conflicts.

Its three evaluation dimensions are:

1. **State Resolution** — detect that an earlier belief is no longer current.
2. **Premise Resistance** — resist a query that presupposes the stale state.
3. **Implicit Policy Adaptation** — apply the updated state in downstream behavior.

The paper reports 400 expert-validated conflict scenarios, 1,200 evaluation queries, contexts up to 150K tokens, and a best evaluated overall accuracy of 55.2%.

## MTEL mapping

| STALE dimension | MTEL interpretation | Governance question |
|---|---|---|
| State Resolution | Evidence / state admission | Which observation is qualified to define the current state? |
| Premise Resistance | Evidence + authority boundary | Can a stale premise be prevented from acquiring decision authority? |
| Implicit Policy Adaptation | State rebind → execution | Do downstream actions update after the state changes? |

## Structural overlap

Both views reject a simplistic memory model in which successful retrieval is enough.

STALE shows the behavioral problem: an agent may possess newer evidence yet fail to revise the operative state.

MirrorTone / MTEL frames the same gap as a governance transition:

```text
retrieved information
        ↓
qualified evidence
        ↓
current-state admission
        ↓
decision / action authority
        ↓
downstream rebind
```

The useful invariant is not "better memory" alone. It is whether the system can prevent stale information from retaining control after contradictory evidence becomes available.

## Where MTEL extends the question

STALE primarily evaluates state-aware memory behavior. MTEL asks several additional engineering questions around that behavior:

- Which surface is authoritative for the current mutable state?
- What freshness or version condition makes a source admissible?
- Which dependent conclusions must be withdrawn after state change?
- Which actions must be blocked until readback occurs?
- What rollback or compensation is required if stale state already crossed into execution?

These are extensions of the governance framing, not claims that STALE itself evaluates all five MTEL primitives.

## What this crosswalk does **not** claim

- STALE is not a MirrorTone benchmark.
- MirrorTone / MTEL is not claimed to outperform the systems evaluated by STALE.
- Similarity of failure structure does not establish shared architecture or implementation.
- This crosswalk does not show that MTEL-SE-001 is qualified; it remains a candidate fixture.

## External source

- STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?  
  https://arxiv.org/abs/2605.06527

## Derived repo artifacts

- [`Public Exit 002 — Retrieval Is Not Current State`](../public-exit/002_retrieval_is_not_current_state.md)
- [`MTEL-SE-001 — Fresh-State Admission Pair`](../benchmark/MTEL-SE-001_fresh_state_admission_pair.md)
