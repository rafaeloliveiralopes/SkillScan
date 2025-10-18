from typing import NoReturn


def error_jd_not_found(path: str) -> NoReturn:
    raise FileNotFoundError(f"Errror: Job description file not found at path: {path}.")


def error_pdf_extract(page_index: int) -> NoReturn:
    raise FileNotFoundError(
        f"Error: Could not extract text from PDF (page {page_index})."
    )


def error_profile_invalid() -> NoReturn:
    raise ValueError(
        "Error: profile.json is invalid (e.g., 'skills' must be a list of strings)."
    )
