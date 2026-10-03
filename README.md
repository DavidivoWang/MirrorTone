# MirrorTone / MTEL

**A governance layer for agentic AI.**

AI systems are becoming more capable, more persistent, and more autonomous. MirrorTone / MTEL focuses on a different question:

> **Capability is not authority.**

What matters is not only what an AI system *can* do, but how its actions are authorized, evidenced, reversible, and judged complete.

This repository is the public canonical entry for that work.

## Five governance primitives

MirrorTone / MTEL uses five recurring questions to examine agentic systems:

1. **Capability** — What can the system do?
2. **Authority** — Who or what authorizes the system to do it, and within what boundary?
3. **Evidence** — What evidence supports the system's state, decision, or claim?
4. **Rollback** — What happens when the system is wrong, overreaches, or needs to reverse course?
5. **Completion** — Who or what is qualified to decide that the task is actually complete?

These are not a scorecard by themselves. They are a compact way to expose governance gaps that raw capability benchmarks often miss.

## Why this repository exists

Most AI discussion starts from capability: better reasoning, longer autonomy, more tools, more agents, more memory.

MirrorTone / MTEL asks what happens **after capability increases**.

A system may retrieve a source without obtaining runtime authority.  
It may generate a plausible completion without satisfying the actual completion criterion.  
It may remember a prior state while failing to rebind after correction.  
It may execute correctly while lacking a safe rollback path.

Those failures are governance failures, not merely model-performance failures.

## Public research flow

This repository grows from verified frontier observations rather than from a fixed taxonomy imposed in advance.

```text
Frontier signal
    ↓
Verification
    ↓
MirrorTone / MTEL mapping
    ↓
Public probe
    ↓
Repeated failure pattern
    ↓
Benchmark candidate
    ↓
Crosswalk / regression case / adapter
```

Not every new AI development belongs here. A signal only enters the public layer when it exposes a sufficiently supported and reusable governance problem.

## Repository map

- [`governance-primitives/`](governance-primitives/) — the five recurring governance primitives
- [`crosswalks/`](crosswalks/) — compact comparisons between external AI systems and the MTEL governance frame
- [`benchmark/`](benchmark/) — candidate regression and benchmark cases derived from repeated, verifiable failure patterns
- [`public-exit/`](public-exit/) — short public probes distilled from frontier research

## Start here

### 001 — Capability → Authority

- [`Public Exit 001 — Capability Is Not Authority`](public-exit/001_capability_is_not_authority.md)
- [`MTEL-CA-001 — Authority Boundary Pair`](benchmark/MTEL-CA-001_authority_boundary_pair.md) — candidate benchmark fixture; not yet qualified

### 002 — Retrieval → Current State

- [`Public Exit 002 — Retrieval Is Not Current State`](public-exit/002_retrieval_is_not_current_state.md)
- [`Crosswalk 001 — STALE × MirrorTone / MTEL`](crosswalks/001_stale_x_mtel.md)
- [`MTEL-SE-001 — Fresh-State Admission Pair`](benchmark/MTEL-SE-001_fresh_state_admission_pair.md) — candidate benchmark fixture; not yet qualified

The second line introduces **state admission**: retrieved information can be relevant evidence without automatically becoming current action-bearing state.

## Current status

This repository is a **public-facing research entry point**, not a declaration that every MirrorTone / MTEL component is production-ready or formally released.

Claims should remain traceable to their evidence surface. Raw signals, popularity, vendor statements, and single examples do not automatically become verified findings or benchmark truth.

## Working principle

> **Don't market MirrorTone by attaching the name to every new AI development. Make new AI developments generate questions that MirrorTone / MTEL can test, clarify, and engineer.**

The goal is a small, reusable governance vocabulary that becomes more useful as agentic systems become more capable.
