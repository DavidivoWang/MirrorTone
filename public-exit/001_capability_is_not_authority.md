# Public Exit 001 — Capability Is Not Authority

**Status:** PUBLIC_PROBE  
**Evidence level:** externally anchored + internally synthesized  
**Claim ceiling:** governance research framing; not a production-runtime claim

## Public probe

An AI agent can be fully capable of completing a task and still be unqualified to act.

That distinction matters more as agents gain tools, persistence, memory, and autonomy.

A useful benchmark therefore cannot ask only:

> Can the agent do the task?

It must also ask:

> Does the agent know when its authority is insufficient, conflicting, stale, or absent — and can it stop before crossing that boundary?

This is the gap captured by the MirrorTone / MTEL principle:

> **Capability is not authority.**

## MTEL probe

**If task success and valid authority can diverge, what evidence must an agent possess before capability is allowed to become action?**

## Why this is now a public candidate

Recent frontier reviews repeatedly converged on the same structural split: stronger execution does not automatically solve state admission, action authority, or independent verification.

AgentAbstain provides a concrete external anchor. Its paired-task design tests both when an agent should act and when it should abstain. Across 17 frontier models and 263 paired tasks, the best reported paired accuracy is 59.5%, and the paper reports that abstention capability is largely independent of general task-solving capability.

That does not prove the full MirrorTone / MTEL governance model. It does support the narrower proposition that **competence and restraint are separable evaluation dimensions**.

## Governance mapping

```text
Capability
    ↓
Authority check
    ↓
Evidence of permission / boundary
    ↓
Act OR abstain
    ↓
Completion / rollback
```

A system that acts correctly for the wrong authorization reason is still a governance failure.

## Evidence

- AgentAbstain: Do LLM Agents Know When Not to Act? — arXiv:2607.10059
  https://arxiv.org/abs/2607.10059
- Project page and benchmark details
  https://agentabstain.github.io/

## Non-claims

This note does not claim that MirrorTone / MTEL has solved agentic abstention in general.

It also does not claim that all authority failures reduce to abstention. The public use of this case is narrower: it is a strong external example showing why task capability alone is an incomplete governance criterion.
