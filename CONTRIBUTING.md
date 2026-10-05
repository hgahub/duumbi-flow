# Contributing

Keep all repository content in English: documentation, skills, templates, examples, diagram labels, metadata, and commit messages. Use lowercase English names with hyphens for files and skills. Translate during conversations when needed; do not maintain localized copies in this repository.

Each change should solve a concrete problem. For a skill correction, provide a reproducible request and expected behavior. Do not turn one special case into a universal rule.

- A skill must depend only on resources within its own directory.
- Preserve the user's scope and the limits of the evidence.
- New publication, installation, or external messaging automation requires a separate decision.
- Do not commit real customer data, secrets, or personal environment paths.
- Run the [development checks](docs/installation.md).
- Before committing, run `pre-commit run --all-files`. Follow the `.gitmessage` template.

A PR should briefly describe the problem, the change, and verification. State when behavioral tests have not run. Preserve required licenses and attribution for material taken from external sources.
