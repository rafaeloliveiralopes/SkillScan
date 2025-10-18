from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Any

from .errors import (
    error_jd_not_found,
    error_pdf_extract,
    error_profile_invalid,
)

# Lightweight offline dependency for PDFs:
# pip install pypdf
from pypdf import PdfReader


def _read_txt(path: Path) -> str:
    if not path.exists():
        error_jd_not_found(str(path))
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        # simple fallback for texts in other common encodings
        return path.read_text(encoding="latin-1")


def _read_pdf_text(path: Path) -> str:
    if not path.exists():
        error_jd_not_found(str(path))

    reader = PdfReader(str(path))
    chunks: List[str] = []
    has_any_text = False

    for idx, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        # Normalize spaces broken by PDFs
        text = " ".join(text.split())
        if text.strip():
            has_any_text = True
            chunks.append(text)
        else:
            # If a page has no text, emit the standard error for that page
            # (aligned with ADR-0001 and README)
            error_pdf_extract(idx + 1)  # 1-based for UX

    if not has_any_text:
        # Entire PDF without selectable text
        error_pdf_extract(1)

    return "\n".join(chunks)


def load_jd_text(jd_path: str | Path) -> str:
    """
    Reads the JD from .txt or .pdf (only PDFs with selectable text).
    Errors follow the documented standard.
    """
    path = Path(jd_path)
    suffix = path.suffix.lower()

    if suffix == ".txt":
        return _read_txt(path)
    if suffix == ".pdf":
        return _read_pdf_text(path)

    # For v0.1.0 we accept only .txt and .pdf
    error_jd_not_found(str(path))  # keep default message


def load_profile(profile_path: str | Path) -> Dict[str, Any]:
    """
    Read and validate profile.json with a minimal schema:
      - name: str
      - skills: list[str]
      - languages: list[str]
    """
    path = Path(profile_path)
    if not path.exists():
        error_profile_invalid()

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        error_profile_invalid()

    if not isinstance(data, dict):
        error_profile_invalid()

    # minimal validations
    name = data.get("name")
    skills = data.get("skills")
    languages = data.get("languages")

    if not isinstance(name, str):
        error_profile_invalid()

    if not (isinstance(skills, list) and all(isinstance(s, str) for s in skills)):
        error_profile_invalid()

    if not (
        isinstance(languages, list) and all(isinstance(lang, str) for lang in languages)
    ):
        error_profile_invalid()

    return {
        "name": name.strip(),
        "skills": [s.strip() for s in skills],
        "languages": [lang.strip() for lang in languages],
    }
