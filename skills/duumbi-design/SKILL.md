---
name: duumbi-design
description: "Develop spec.md from a development intent or existing intent.md. Use to design observable behavior, data and interface contracts, failure paths, risks, and verification criteria. Does not implement code."
license: MIT
---

# Define the solution contract

Create `spec.md` for the requested slice. Start from acceptance examples and the actual system.

## Workflow

1. Read `intent.md` if it exists, applicable project rules, code, and prior decisions. If there is no intent document but the request is sufficiently clear, work from it; do not make another skill a mandatory prerequisite.
2. Describe externally observable behavior, non-goals, failure paths, and data and access boundaries.
3. Prefer existing patterns, native capabilities, and simple solutions. A new abstraction or dependency requires a concrete need.
4. Record risk, verification examples, and relevant performance/UX targets. Do not invent universal thresholds.
5. Mark decisions, proposals, and implementation blockers separately. For consequential decisions that are hard to reverse, use a decision record following project conventions.
6. Write or update `spec.md` in the designated slice directory using the [spec template](assets/spec.md), then read it back.

The stages require deeper evidence over time: a working example and security baseline in WORK; correctness and operability in RIGHT; relevant measurements in FAST. Testing is continuous; do not defer a necessary check solely because of a stage name.

During a rewrite, the behavioral goal may remain, but verification of the old implementation does not establish the new code's correctness. A specification alone is not product, merge, or release approval. Modify code only within a separately requested implementation scope.
