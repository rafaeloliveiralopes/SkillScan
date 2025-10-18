from __future__ import annotations
import sys
from pathlib import Path

# ensure src/ is on sys.path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from agent.parser import load_jd_text, load_profile  # noqa: E402
from agent.comparator import compare_profile_to_jd, simple_recommendations  # noqa: E402
from agent.reporter import generate_report_file  # noqa: E402


def main() -> None:
    jd_path = SRC_DIR / "samples" / "jd.txt"
    profile_path = SRC_DIR / "samples" / "profile.json"
    out_dir = PROJECT_ROOT / "reports"

    jd_text = load_jd_text(str(jd_path))
    profile = load_profile(str(profile_path))

    result = compare_profile_to_jd(profile, jd_text)
    recs = simple_recommendations(result)

    out_file = generate_report_file(
        profile=profile,
        jd_path=str(jd_path),
        compare_result=result,
        recommendations=recs,
        out_dir=str(out_dir),
    )

    print(f"Report written to: {out_file}")


if __name__ == "__main__":
    main()
