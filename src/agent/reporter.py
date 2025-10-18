from __future__ import annotations

import datetime as dt
from pathlib import Path
from typing import Dict, List, Optional


def _slug(s: str) -> str:
    return "".join(ch.lower() if ch.isalnum() else "-" for ch in s).strip("-")


def render_markdown(
    *,
    profile_name: str,
    jd_source: str,
    result: Dict[str, List[str]],
    recommendations: List[str],
    generated_at: Optional[dt.datetime] = None,
) -> str:
    """
    Generates the Markdown content for report v0.1.0.
    Sections: matched, gaps, extra, recommendations.
    """
    ts = (generated_at or dt.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
    jd_disp = Path(jd_source).name or jd_source

    def _mk_list(items: List[str]) -> str:
        if not items:
            return "- (none)"
        return "\n".join(f"- {it}" for it in items)

    md = f"""# SkillScan Report

**Candidate:** {profile_name}
**JD source:** {jd_disp}
**Generated at:** {ts}

---

## 🟢 Matched Skills

{_mk_list(result.get("matched", []))}

## 🔴 Gaps (Missing Skills)

{_mk_list(result.get("gaps", []))}

## ⚪ Extra (Profile-only Skills)

{_mk_list(result.get("extra", []))}

## 💡 Recommendations

{_mk_list(recommendations)}
"""
    return md


def write_report(markdown: str, out_dir: str | Path, filename_base: str) -> Path:
    """
    Writes the .md report to `out_dir`.
    Returns the final file path.
    """
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    ts = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"{_slug(filename_base)}-{ts}.md"
    final = out_path / filename
    final.write_text(markdown, encoding="utf-8")
    return final


def generate_report_file(
    *,
    profile: Dict,
    jd_path: str | Path,
    compare_result: Dict[str, List[str]],
    recommendations: List[str],
    out_dir: str | Path = "reports",
) -> Path:
    """
    High-level function: renders and writes the report.
    """
    md = render_markdown(
        profile_name=str(profile.get("name", "Unknown")),
        jd_source=str(jd_path),
        result=compare_result,
        recommendations=recommendations,
    )
    base = f"skillscan-{profile.get('name', 'candidate')}-{Path(jd_path).stem}"
    return write_report(md, out_dir, base)
