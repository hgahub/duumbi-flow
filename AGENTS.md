# duumbi-flow

This is a documentation and skill package, not an application or agent runtime.

- Keep all repository content in English, including documentation, skills, templates, examples, diagrams, metadata, and commit messages. Translate in conversations when needed; do not add translated copies to the repository.
- Preserve the mapping: plan → intent.md, design → spec.md, build → plan.md, review → review.md.
- Do not conflate work steps with WORK/RIGHT/FAST development focuses or M1/M2/M3 maturity.
- Use synthetic public examples; do not bring in private knowledge-base data.
- Skills under skills/ must be independently installable. Other skills or MCP servers are not mandatory dependencies.
- Create only necessary files. After changes, run: python3 scripts/validate.py and python3 -m unittest discover -s tests -v.
- For skill changes, perform behavioral checks when warranted in addition to structural validation.
- Do not claim publication, completed tests, or approval without evidence.
