from typing import NoReturn


def error_jd_not_found(path: str) -> NoReturn:
    # Standardized per README/ADR
    raise FileNotFoundError(f"ERROR: JD not found at {path}.")


def error_pdf_extract(page_index: int) -> NoReturn:
    # Standardized per README/ADR
    raise ValueError(f"ERROR: Could not extract text from PDF (page {page_index}).")


def error_profile_invalid() -> NoReturn:
    # Standardized per README/ADR
    raise ValueError(
        "ERROR: profile.json is invalid (e.g., 'skills' must be a list of strings)."
    )
