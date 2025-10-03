# Contributing Guide

Thanks for your interest in contributing! Please read this guide before opening issues or pull requests.

## Scope & principles

- This project analyzes a Job Description (JD) (TXT or **text-based** PDF) against a candidate profile (JSON) and outputs a Markdown report.
- Offline-by-default; **no external network calls** in v0.1.0.
- **No OCR**: scanned/image-only PDFs are not supported in v0.1.0. See [0001-offline-and-pdf-policy.md](../adrs/0001-offline-and-pdf-policy.md).

- Keep contributions within the current scope (see `project-brief.md`).

## How to run locally

1- Python 3.11+

2- Install deps:

```bash
   pip install -r requirements.txt
```

3- Run example:

**Linux/macOS (bash/zsh):**

```bash
python -m agent.runner run   --jd ./samples/jd.txt   --profile ./samples/profile.json   --out ./reports   --verbose
```

**Windows PowerShell:**

```powershell
python -m agent.runner run
  --jd ./samples/jd.txt
  --profile ./samples/profile.json
  --out ./reports
  --verbose
```

**Windows CMD:**

```cmd
python -m agent.runner run ^
  --jd .\samples\jd.txt ^
  --profile .\samples\profile.json ^
  --out .\reports ^
  --verbose
```

**Single line (any shell):**

```bash
python -m agent.runner run --jd ./samples/jd.txt --profile ./samples/profile.json --out ./reports --verbose
```

## Issues

- Use labels: `bug`, `enhancement`, `good first issue`, `help wanted`.
- For **bugs**, include OS, Python version, steps to reproduce, and relevant logs.
- For **enhancements**, explain motivation, alternatives considered, and acceptance criteria.

## Pull requests

- Keep PRs small and focused.
- Checklist:
  - [ ] Tests updated/added when touching core logic.
  - [ ] `README.md` updated if behavior changes.
  - [ ] No breaking changes without a migration note.
  - [ ] Aligned with ADR-0001 (offline-by-default; PDF must contain selectable text).
- At least **one approval** is required to merge.

## Commit messages (Angular Conventional Commits)

Examples that match this repository's style:

```text
docs(readme): add quick-start and usage examples.
feat(agent): add JD TXT/PDF parsing with keyword heuristics.
fix(parser): handle empty PDF pages gracefully.
chore(config): add EditorConfig and markdownlint config.
```

## Code style & tests

- Python 3.11+, `pytest` for tests.
- (Optional) If using ruff/black, run lint/format before pushing.

## Agent guardrails (anti-hallucination)

- Do not introduce external network calls without a new ADR.
- Keep keyword extraction deterministic; avoid unverifiable AI outputs in v0.1.0.
- Errors must be explicit and actionable (see `project-brief.md` Error handling).

## Governance

- Semantic Versioning (SemVer) for tags/releases and a maintained `CHANGELOG.md`.
- Community conduct: be respectful and constructive.
