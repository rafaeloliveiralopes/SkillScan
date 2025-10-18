#!/usr/bin/env python3
from __future__ import annotations

import os
import sys

# Ensure we can import from src/ before importing our package
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
SRC_DIR = os.path.join(PROJECT_ROOT, "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from agent.parser import load_jd_text, load_profile  # noqa: E402


def main() -> None:
    jd_path = os.environ.get("JD_PATH", os.path.join(SRC_DIR, "samples", "jd.txt"))
    profile_path = os.environ.get(
        "PROFILE_PATH", os.path.join(SRC_DIR, "samples", "profile.json")
    )

    print(load_jd_text(jd_path)[:200])
    print(load_profile(profile_path))


if __name__ == "__main__":
    main()
