---
name: duumbi-build
description: "Prepare a plan.md execution plan for a specification and carry out user-requested implementation in small, verifiable changes. Use for duumbi-flow build tasks. For planning-only requests, produce only the plan; does not replace a separate review or release authorization."
license: MIT
---

# Plan and implement

The build step's plan is `plan.md`. First determine whether the user requested a plan, implementation, or both. Do not modify product code for a planning-only request.

## Workflow

1. Read the request, project rules, relevant `intent.md` and `spec.md`, code, and current workspace state. Protect existing user changes.
2. Use the [plan template](assets/plan.md) to define the smallest evaluable steps, verification, and recovery. Flag a missing required contract; do not invent business decisions.
3. For implementation requests, follow the project's branching and worktree conventions. Do not create long-lived WORK/RIGHT/FAST branches.
4. Prefer existing code, the standard library, and native capabilities. Preserve necessary error handling, security, and accessibility.
5. Run checks appropriate to the change's risk and target gate. Distinguish completed, failed, and omitted steps in the plan. Issuing a command does not establish successful completion.
6. Compare the result with the contract. For material deviations, update related documentation within the authorized scope or identify the decision needed.

## Maturity boundaries

- A feature slice targeting M1 requires at least one automated happy-path smoke/E2E test checking a real outcome. The security baseline and existing regression checks remain throughout.
- At M2, verify relevant negative and failure paths, access controls, compatibility, and recovery. The target project's gates govern.
- At M3, measure in the predefined environment and load conditions. Optimize only demonstrated shortfalls; a satisfactory result does not require a rewrite.
- Do not silently relax targets after a test or measurement fails. If safe progress is impossible, preserve the state and report the blocker.
- Refresh affected evidence for a new build. Unknown change impact requires broader checks.

End WORK with a value decision and a justified discard/evolve/rewrite decision. Do not infer approved maturity or user release from implementation completion.

The task alone does not authorize external messaging, publication, or production changes. The user's assignment and target project rules govern those actions. Finish implementation with a brief account of the change, verification, and residual risk.
