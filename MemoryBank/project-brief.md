# Project Brief — Agentic AI Skills Scan

## What it is

A local, CLI-based Python agent that analyzes a Job Description (JD), compares it to a candidate profile, and produces a concise Markdown report showing matched skills, gaps, and actionable recommendations.

## Primary objective

Maintain a clear-scoped, open-source, public-utility tool that delivers an objective JD-vs-profile analysis offline in v0.1.0.

## Initial scope (v0.1.0)

- CLI execution.
- JD parsing from `.txt` and text extraction from `.pdf`.
- Candidate profile comparison from `.json`.
- Markdown report with: matched skills, prioritized gaps, and recommendations.
- Basic unit tests; minimal run log in `memory/log.json`.

## Out of scope (for now)

- ATS integrations, large-scale scraping, or high-volume matching.
- Web UI and public API (planned for later versions).
- Any outbound data transfer by default.
- OCR for scanned PDFs (only text-selectable PDFs in v0.1.0).

## Interaction flow (technical summary)

1. Inputs: `--jd <.txt|.pdf>`, `--profile <.json>`, `--out <dir?>`.
2. Fixed steps: `parse_jd → compare_profile → generate_report`.
3. Outputs: `reports/YYYY-MM-DD_<name>_report.md` + minimal log.

## Interfaces / I/O / formats

- JD: `.txt`, `.pdf` (must contain selectable text).
- Profile: `.json` with `name: str`, `skills: str[]`, `languages: str[]`.
- Report: `.md`.
- Useful flags: `--verbose`, `--max-steps`.

## Error handling (standard messages)

- `ERROR: JD not found at <path>.`
- `ERROR: Could not extract text from PDF (page X).`
- `ERROR: profile.json is invalid (e.g., "skills" must be a list of strings).`
- `WARNING: No skills identified in the JD.`
- Exit codes: `0` success, `1` failure.

## Definition of Done (v0.1.0)

- Runs locally with valid `.txt`/`.pdf` JD and `.json` profile.
- Produces `.md` report with the three required sections (matched, gaps, recommendations).
- Minimal tests pass for parser, comparison, and reporter.
- README includes install and usage examples.
- No external calls by default.

## Assumptions & constraints

- Requires **Python 3.11+** and runs **offline** (no network dependency).
- Understands **Portuguese/English** plain text; skill extraction uses **simple keyword heuristics** (no heavy NLP in v0.1.0).
- **PDFs must contain selectable text**; **scanned PDFs are not supported** in this version (use `.txt` or a native/text PDF).

## Open-source governance (minimal)

- Issue/PR labels: `bug`, `enhancement`, `good first issue`, `help wanted`.
- PRs must include a clear description, a small quality checklist, and at least **one approval**.
- Semantic Versioning (**SemVer**) and a maintained **CHANGELOG.md**.

## Roadmap (high level)

- **v0.2.0**: better heuristics (synonyms/stemming), basic weighting/prioritization.
- **v0.3.0**: local API (FastAPI) + simple Web UI (Next.js).
- **v0.4.0+**: optional integrations (embeddings/vector DB) while preserving offline mode.
