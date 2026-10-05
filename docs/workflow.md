# Workflow and file conventions

Keep intent, implementation planning, and verification evidence in separate documents. File names are fixed:

```text
docs/changes/<slice-id>/
  intent.md
  spec.md
  plan.md
  review.md
```

This is the recommended location for new projects. Follow an existing project's documented root; do not create parallel records. Use a stable, lowercase, hyphenated `slice-id`.

## What do the four steps mean?

- **plan → intent.md:** user problem, desired outcome, non-goals, acceptance examples, risks, and open questions. Here, “plan” names the step that clarifies intent.
- **design → spec.md:** observable behavior, boundaries, data and interface contracts, failure paths, and verification. A solution that has not been decided remains a proposal.
- **build → plan.md:** small implementation steps, dependencies, verification, and recovery. Write code only within the requested execution scope. Thus, `plan.md` is the execution plan.
- **review → review.md:** the examined version, findings, completed and omitted checks, and a proposed decision. A plan or checklist is not execution evidence.

For a small task, these can be brief and produced in one session. Four handoffs or approval rounds are not required. Editing one designated document does not require regenerating the others.

## How do they relate to maturity?

| Focus | Role of the four documents |
| --- | --- |
| WORK | Clarify intent and hypotheses; plan the experiment; record functional and user evidence; decide what happens to the code. |
| RIGHT | Stabilize the same contract and implementation; address failure paths, security, migration, and review. |
| FAST | Measure predefined targets; optimize where justified; collect release evidence. |

A `review.md` can be produced at any stage. Creating a file does not advance maturity. The target project's single record holds the value decision, verified maturity, and user exposure; documents refer to that record.

## Minimum operating rules

1. Each slice must have an independently observable outcome.
2. Do not invent user approval; mark open decisions.
3. M1 requires at least one happy-path test that checks a real outcome. Existing regression checks and invariants remain in force throughout.
4. Risk and the target project determine the next gate's criteria. At M3, a satisfactory measurement is sufficient; optimization is not mandatory.
5. Uncertain or hazardous experiments remain in a sandbox. Only verified changes enter product code.
6. Prototype quality does not justify ignoring data loss, access-control failures, or the security baseline.
7. A review finding is a recommendation; it does not itself authorize a merge or release.

## Post-release review

The value decision accepted in WORK supports proceeding; it does not establish lasting business value. During the pilot, also examine actual usability and operating cost. The outcome may be to retain, improve, or retire the feature.
