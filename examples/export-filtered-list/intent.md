# Export a filtered list

**Synthetic learning example.** No implementation, user approval, or test run exists behind it.

## Goal and scope

The user wants to save the currently visible rows of an open task list as a JSON file to attach to a bug report.

One slice: export the current page, preserving its filter and ordering. Exporting all pages, making a new query, background jobs, CSV, and a new authorization system are out of scope.

## Acceptance example

A filter shows two of five rows. After export, the file contains exactly those two rows in screen order, with only the identifier, title, and status fields. Hidden rows and internal fields must not be included.

## State and risk

- Value decision: open; the example does not constitute acceptance.
- Maturity: unverified; exposure: no implementation.
- Risk: data export; the target project's data classification and export policy still need to be checked.
- Owner, WORK start, and expiry: unassigned because no real work has started.

## Open decision

Does the target project allow local export of these three fields? Clarify before implementing for production. The [specification](spec.md) offers a conditional proposal.
