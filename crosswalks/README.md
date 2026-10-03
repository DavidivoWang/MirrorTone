# MTEL Crosswalks

Crosswalks translate external AI systems into a small set of governance questions without forcing unlike systems into the same architecture.

A crosswalk is not a product ranking and does not assume that MirrorTone / MTEL and the external system occupy the same layer.

## Current crosswalks

- [`001 — STALE × MirrorTone / MTEL`](001_stale_x_mtel.md) — memory invalidation, state admission, premise resistance, and downstream rebind

## Minimal crosswalk template

For each system or capability, examine:

| Dimension | Question |
|---|---|
| Capability | What new capability or execution surface is introduced? |
| Authority | How is permission granted, scoped, delegated, or revoked? |
| Evidence | What evidence is accepted for state, action, or claim formation? |
| Rollback | What can be reversed, withdrawn, corrected, or contained? |
| Completion | What qualifies the action or task as actually complete? |

## Verdict vocabulary

Use only when supported by evidence:

- **Addressed** — the relevant governance problem is explicitly handled.
- **Partially addressed** — some mechanism exists, but the boundary or guarantee is incomplete.
- **Gap observed** — available evidence exposes a concrete governance gap.
- **Unknown** — current evidence is insufficient.

## Evidence rule

Vendor documentation can support what a vendor officially states about its system. It does not automatically verify disputed behavior, production state, causal claims, or comparative superiority.

Every crosswalk should preserve the distinction between:

```text
verified surface
working interpretation
candidate integration
```

The purpose is to make differences inspectable, not to manufacture symmetry.
