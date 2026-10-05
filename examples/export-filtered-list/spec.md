# Export contract

Source: [intent](intent.md). **Conditional design example, not an accepted product decision.**

## Observable behavior

- The “Export current page” button saves a snapshot of the rows visible at the moment of the click.
- Produce a UTF-8 JSON array, with only `id`, `title`, and `status` per item, preserving visible order.
- An empty list produces `[]`. The file name is `tasks.json`.
- Use the existing list view's authorization-filtered data; do not make a new network request. Do not indiscriminately serialize entire data objects.
- If starting the download fails, show an understandable error and leave the list unchanged. Handing a download to the browser does not establish successful saving to disk.

## Constraint and open question

Examine the existing list view's access controls first. Permission to view data does not by itself establish permission to export it; the export policy decision remains open. Do not introduce a new production data flow before resolving this.

## Verification examples

| Case | Expected result |
| --- | --- |
| Filtered, sorted list | Downloaded JSON contains exactly the visible rows in their order. |
| Empty list | A valid, empty JSON array. |
| Accented characters and quotation marks in a title | Text is unchanged after reading the file back. |
| Internal field in list data | The field is absent from the file. |
| Failure to start the download | An error message, with no false success indication. |

M1 requires an automated smoke/E2E test checking the filtered list's actual file output; data and access baselines are prerequisites. M2 also requires relevant negative and failure paths.

## Performance and recovery

Early sanity check: are the list's actual page size and object size bounded? If the limit is unknown, measure or define an explicit limit first. Set the M3 measurement target from the target project's device profile and UX budget; this example does not invent a universal time limit.

No data writes or migrations are involved. On failure, disable or remove the export entry point and run list-view regression checks.
