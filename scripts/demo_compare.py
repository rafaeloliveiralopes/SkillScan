#!/usr/bin/env python3
from __future__ import annotations
import os, sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
SRC_DIR = os.path.join(PROJECT_ROOT, "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from agent.parser import load_jd_text, load_profile  # noqa: E402
from agent.comparator import compare_profile_to_jd, simple_recommendations  # noqa: E402


def main() -> None:
    jd = load_jd_text(os.path.join(SRC_DIR, "samples", "jd.txt"))
    profile = load_profile(os.path.join(SRC_DIR, "samples", "profile.json"))

    result = compare_profile_to_jd(profile, jd)
    print("JD skills:", result["jd_skills"])
    print("Profile skills:", result["profile_skills"])
    print("Matched:", result["matched"])
    print("Gaps:", result["gaps"])
    print("Extra:", result["extra"])
    print("Recommendations:", simple_recommendations(result))


if __name__ == "__main__":
    main()
