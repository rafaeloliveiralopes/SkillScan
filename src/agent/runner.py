from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Optional

from . import __version__
from .parser import load_jd_text, load_profile
from .comparator import compare_profile_to_jd, simple_recommendations
from .reporter import generate_report_file
from .logger import append_run_log


def _eprint(*args, **kwargs) -> None:
    print(*args, file=sys.stderr, **kwargs)


def _resolve(path_str: str) -> Path:
    return Path(path_str).expanduser().resolve()


def _cmd_run(
    *,
    jd_path: str,
    profile_path: str,
    out_dir: Optional[str],
    verbose: bool,
) -> int:
    # 1) inputs
    jd_file = _resolve(jd_path)
    profile_file = _resolve(profile_path)

    if verbose:
        print(f"[info] loading JD from: {jd_file}")
        print(f"[info] loading profile from: {profile_file}")

    # 2) parse
    jd_text = load_jd_text(str(jd_file))
    profile = load_profile(str(profile_file))

    # 3) compare
    result = compare_profile_to_jd(profile, jd_text)
    recs = simple_recommendations(result)

    if verbose and not result["jd_skills"]:
        print("WARNING: No skills identified in the JD.")

    # 4) console summary
    if verbose:
        print("\n=== SkillScan Summary ===")
    print(f"candidate: {profile.get('name')}")
    print(f"jd skills: {len(result['jd_skills'])}")
    print(f"matched : {len(result['matched'])} -> {result['matched']}")
    print(f"gaps    : {len(result['gaps'])} -> {result['gaps']}")
    print(f"extra   : {len(result['extra'])} -> {result['extra']}")

    # 5) optional report
    if out_dir:
        out = generate_report_file(
            profile=profile,
            jd_path=str(jd_file),
            compare_result=result,
            recommendations=recs,
            out_dir=str(_resolve(out_dir)),
        )
        print(f"\nreport written to: {out}")

    # 6) minimal local log (JSONL)
    try:
        append_run_log(
            {
                "jd_path": str(jd_file),
                "profile_path": str(profile_file),
                "out_dir": str(out_dir or ""),
                "matched": len(result.get("matched", [])),
                "gaps": len(result.get("gaps", [])),
                "extra": len(result.get("extra", [])),
                "wrote_report": bool(out_dir),
            }
        )
    except Exception:
        # Logging must never break the CLI; ignore any local I/O failure silently.
        pass

    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="skillscan",
        description="Compare a Job Description with a candidate profile and generate a Markdown report.",
    )

    sub = p.add_subparsers(dest="command", required=True)

    # subcommand: run
    run = sub.add_parser(
        "run", help="run a comparison (and optionally write a report)."
    )
    run.add_argument(
        "--jd",
        required=True,
        help="Path to the Job Description (.txt or selectable-text .pdf).",
    )
    run.add_argument("--profile", required=True, help="Path to profile.json.")
    run.add_argument(
        "--out",
        default=None,
        help="Directory to write the Markdown report. If omitted, prints summary only.",
    )
    run.add_argument(
        "--verbose",
        action="store_true",
        help="Print additional execution details.",
    )

    # subcommand: version
    ver = sub.add_parser("version", help="show version and exit.")
    ver.set_defaults(version=True)

    return p


def main(argv: Optional[list[str]] = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    parser = build_parser()
    args = parser.parse_args(argv)

    if getattr(args, "version", False):
        print(__version__)
        return 0

    try:
        if args.command == "run":
            return _cmd_run(
                jd_path=args.jd,
                profile_path=args.profile,
                out_dir=args.out,
                verbose=args.verbose,
            )
        _eprint("unknown command.")
        return 2
    except (FileNotFoundError, ValueError) as e:
        _eprint(str(e))
        return 1
    except KeyboardInterrupt:
        _eprint("aborted by user.")
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
