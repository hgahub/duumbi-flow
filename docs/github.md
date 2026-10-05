# GitHub implementation proposal

This is a proposal for the target project. duumbi-flow's own CI checks the documentation and skill package; it does not install product development gates.

## One slice, one record

Keep the slice's four documents in the versioned `docs/changes/<slice-id>/` directory. The Project item links to the intent and PR.

For a pilot, use one designated slice record protected by review as the source of decisions, such as a metadata section in `intent.md`. Include: owner, WORK start and expiry; value decision; verified maturity; user exposure; code disposition; evidence and verified commit; feature flag and removal deadline, if applicable. Leave unknown data open; do not fill it with invented decisions.

Mirrored Project fields provide filterable views. [Single-select fields](https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-single-select-fields) suit discrete states. WORK/RIGHT/FAST is a derived view based on the methodology's rules; GitHub does not calculate this custom rule automatically. Documented manual updates are sufficient for a pilot; event-driven synchronization may be justified later.

## CI and release

| Point | Proposed checks |
| --- | --- |
| Every PR | Build, static checks, affected regressions, security baseline. |
| M1 target | Smoke/E2E checking a real output, isolation, and early architecture checks. |
| M2 target | Relevant negative and failure paths, access control, compatibility, operability. |
| M3 target | Representative measurements and risk-justified deep testing tied to a specific build. |
| Release | Fresh evidence, designated approval, gradual enablement, and stop conditions. |

The target project's Actions workflow should select tests from versioned requirements. An editable issue label must not bypass a required check. `main` [branch protection](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) can require relevant status checks and reviews. Passing CI does not replace the value decision.

A daily read-only check can flag expiry. Only a mechanism designed and tested in the target project should disable product functionality automatically. Feature-flag removal and hotfix follow-up checks must be tracked tasks, not verbal promises.

## This package's CI

The [Validate workflow](../.github/workflows/validate.yml) checks skill metadata, local inline Markdown links, standalone installation boundaries, and validator failure cases. It does not assess model decisions, external URL availability, or methodology productivity.
