# Contributor notice

> We welcome sincere, human contributions that align with our [guidelines](../CONTRIBUTING.md). All contributions, including pull requests, issues, and comments, are governed by our [code of conduct](../CODE_OF_CONDUCT.md). AI-generated pull requests will be reported as spam and closed without comment.

## Summary

<!-- What does this PR change and why? Keep it brief but specific. -->

## Type of change

- [ ] feat: New feature
- [ ] fix: Bug fix
- [ ] docs: Documentation only
- [ ] refactor: Code change that neither fixes a bug nor adds a feature
- [ ] perf: Performance improvement
- [ ] test: Add or fix tests
- [ ] chore/build/ci: Tooling, config, or pipeline

## Scope
<!-- Which part of the project is affected? e.g., CLI, analyzer, docs -->

## Screenshots / Demos (optional)
<!-- If UI or CLI output changed, add before/after or a short gif/text sample -->

## How to test
<!-- Exact steps/commands a reviewer should run locally -->
1.
2.
3.

## Breaking changes

- [ ] This change introduces breaking behavior.
If checked, describe here:

## Documentation

- [ ] README updated (usage, examples, troubleshooting as needed).
- [ ] CHANGELOG updated (Unreleased section).
- [ ] `context/tech-context.md` updated **if** stack/constraints/I/O changed.
- [ ] Related ADR linked (if applicable).

## Architecture & constraints (must confirm)

- [ ] **Offline-by-default** preserved (no external calls).
- [ ] **PDFs with selectable text only** (no OCR introduced).
- [ ] Accepted inputs unchanged: `JD (.txt | .pdf with text)` and `profile.json`.
- [ ] Outputs unchanged: console and/or Markdown report.

## Security & quality

- [ ] No secrets/keys in code or history.
- [ ] Tests added/updated and pass locally.
- [ ] Lint/format run locally (if applicable).

## Related issues/ADRs
<!-- Link issue IDs and ADRs (e.g., ADR-0001) -->

## Checklist (Conventional Commits)

- [ ] PR title follows **Conventional Commits (Angular)** and is clear.
  <!-- Example: feat(cli): add profile.json validation. -->

## Notes for reviewers
<!-- Anything that you want to tell the people who are going to review your pull request. -->
