import re
from pathlib import Path

from agent.reporter import render_markdown, write_report


def test_write_report_filename_format(tmp_path: Path):
    md = "# Report\n"
    out = write_report(md, tmp_path, "Carol Danvers")

    # Expect YYYY-MM-DD_carol-danvers_report.md
    assert out.exists()
    assert re.match(r"\d{4}-\d{2}-\d{2}_carol-danvers_report\.md$", out.name)


def test_render_markdown_sections(tmp_path: Path):
    md = render_markdown(
        profile_name="Carol",
        jd_source="job.txt",
        result={
            "matched": ["python"],
            "gaps": ["kubernetes"],
            "extra": ["docker"],
        },
        recommendations=["Study 'kubernetes'."],
    )

    assert "Matched Skills" in md
    assert "Gaps (Missing Skills)" in md
    assert "Extra (Profile-only Skills)" in md
    assert "Recommendations" in md
