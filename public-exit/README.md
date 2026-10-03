# Frontier → MTEL Public Exit

This directory is the public-facing exit from verified frontier research.

It does not replace intake, verification, or internal research. It only receives a signal after those stages have produced enough support to justify a reusable public question or engineering candidate.

## Current public exits

- [`001 — Capability Is Not Authority`](001_capability_is_not_authority.md)
- [`002 — Retrieval Is Not Current State`](002_retrieval_is_not_current_state.md)
- [`003 — Correction Is Not Rebind`](003_correction_is_not_rebind.md)
- [`004 — Completion Is Not Self-Declared Success`](004_completion_is_not_self_declared_success.md)

## Three outputs

### PUBLIC_EXIT
A short, clean public probe that can stand on its own.

Prefer a question that exposes one structural tension in Capability / Authority / Evidence / Rollback / Completion. Avoid promotional language and avoid forcing the MirrorTone / MTEL name into the probe.

### MTEL_PROBE
One high-leverage question only.

The goal is to expose the most load-bearing structural difference, not to deliver a lecture or a full framework explanation.

### BENCHMARK_CANDIDATE
Only when the observed failure pattern is repeatable, verifiable, and sufficiently generalizable.

Record:

```text
candidate type
minimal test skeleton
failure criterion
supporting evidence surface
```

Otherwise use `NONE`.

## Admission boundary

Do not promote the following directly into public claims or benchmark truth:

- raw intake
- news heat
- community consensus
- a single anecdote
- unverified interpretation
- vendor self-description beyond what it actually supports

## Intended flow

```text
Weekly frontier research
        ↓
Verified high-value observation
        ↓
PUBLIC_EXIT / MTEL_PROBE
        ↓
Repeated pattern
        ↓
BENCHMARK_CANDIDATE
        ↓
Qualified benchmark / crosswalk / adapter
```

If all three outputs are `NONE`, that is a valid result. The public layer should remain sparse enough to preserve signal.
