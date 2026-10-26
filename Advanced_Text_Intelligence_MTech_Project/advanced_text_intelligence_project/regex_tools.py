"""Regular-expression utilities for extracting common text patterns."""
import re

EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
URL_RE = re.compile(r"https?://[^\s<>()]+", re.IGNORECASE)
NUMBER_RE = re.compile(r"(?<!\w)[+-]?\d+(?:\.\d+)?(?!\w)")

def extract_emails(text: str) -> list[str]:
    return EMAIL_RE.findall(text)

def extract_urls(text: str) -> list[str]:
    return URL_RE.findall(text)

def extract_numbers(text: str) -> list[str]:
    return NUMBER_RE.findall(text)

def find_pattern(text: str, pattern: str, ignore_case: bool = False) -> list[dict]:
    flags = re.IGNORECASE if ignore_case else 0
    try:
        compiled = re.compile(pattern, flags)
    except re.error as exc:
        raise ValueError(f"Invalid regular expression: {exc}") from exc
    return [{"match": m.group(), "start": m.start(), "end": m.end()} for m in compiled.finditer(text)]
