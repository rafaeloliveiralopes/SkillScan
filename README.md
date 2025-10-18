# Agentic AI Skills Scan

A local CLI agent that analyzes a Job Description (JD), compares it to a candidate profile, and generates a Markdown report with matched skills, gaps, and actionable recommendations.

> Runs **offline by default** and supports **text-based** JDs in `.txt` or `.pdf` (no OCR in v0.1.0).
> See `0001-offline-and-pdf-policy.md` for the offline/PDF policy.

---

## quick start

### requirements

- Python **6.+**
- pip

### install

```bash
pip install -r requirements.txt
```

### run (example)

```bash
python -m agent.runner run   --jd ./src/samples/jd.txt   --profile ./src/samples/profile.json   --out ./reports   --verbose
```

If installed as a package, you can also use the console script:

```bash
skillscan run --jd ./src/samples/jd.txt --profile ./src/samples/profile.json --out ./reports --verbose
```

---

## inputs

- **JD**: `.txt` or **text-selectable** `.pdf` (exported from a text editor).
  _Scanned/image-only PDFs are not supported in v0.1.0._

- **Profile** (`.json`):

```json
{
  "name": "Rafael",
  "skills": ["Python", "Flask", "PostgreSQL", "Git", "Docker"],
  "languages": ["Portuguese", "English (basic)"]
}
```

## outputs

```text
2025-10-02_rafael_report.md
The report contains the required sections `Matched Skills`, `Gaps (Missing Skills)`,
and `Recommendations`. It may also include an optional `Extra (Profile-only Skills)`
section when your profile lists skills that don't appear in the JD.
```

---

## standard errors

- `ERROR: JD not found at <path>.`
- `ERROR: Could not extract text from PDF (page X).`
- `ERROR: profile.json is invalid (e.g., "skills" must be a list of strings).`
- `WARNING: No skills identified in the JD.`

Exit codes: `0` success, `1` failure.

---

## scope & limitations (v0.1.0)

- **Offline-by-default**; no external calls.
- JD parsing from `.txt` and **text-based** `.pdf` (no OCR).
- Simple **keyword heuristics** for skill extraction (PT/EN).
- CLI only (no Web UI / API yet).

For technical scope, I/O and Definition of Done, see `project-brief.md`.
For purpose, problems and personas, see `product-context.md`.
For the offline/PDF policy, see ADR `0001-offline-and-pdf-policy.md`.

---

## Contributing

We welcome contributions! Please read our [Contributing Guide](./CONTRIBUTING.md) before opening issues or pull requests.

---

## license

[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)

<hr>
