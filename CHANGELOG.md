# Changelog

## [Unreleased]

### Planned

- Improved keyword heuristics (synonyms/stemming, weighting/priorities)
- Local API (FastAPI) and simple Web UI (Next.js)
- Optional embeddings/vector integrations (opt-in), keeping offline-by-default

## [0.1.0] - 2025-10-19

Initial public release.

### Added

- CLI (`skillscan`) to compare a Job Description with a candidate profile
  - Subcommands: `run`, `version`
  - Exit codes: `0` success, `1` error, `130` keyboard interrupt
- Parser for inputs
  - JD: `.txt` and text-selectable `.pdf` (no OCR); standardized errors
  - Profile: `.json` with minimal schema validation (`name`, `skills[]`, `languages[]`)
- Comparator
  - Offline, deterministic keyword heuristics (PT/EN) via regex against a default lexicon
  - Canonicalization map (e.g., `Postgres` → `PostgreSQL`, `Node` → `Node.js`)
  - Case-insensitive extraction, deduplication and sorted outputs
- Reporter
  - Markdown report with sections: Matched, Gaps, Extra (optional), Recommendations
  - Filenames: `YYYY-MM-DD_{slug(name)}_report.md`
- Minimal logging
  - Local JSONL log at `memory/log.json` with structured events (`run_start`, `report_written`, `error`, `summary`)
  - Simple rotation policy (keeps last N entries)
- Tests and CI
  - Pytest suite for parser, comparator, reporter, CLI, and logging (10 tests)
  - GitHub Actions workflow to run tests on pushes and PRs

### Docs

- README with quick start, usage examples and PDF limitations
- ADR `0001-offline-and-pdf-policy.md` for offline/PDF constraints
- Project Brief and Product Context
- Contributing Guide and Code of Conduct
