"""Use English for Registry mechanism link labels and page headings only.

This module does not translate scientific content or modify the submitted
equations, estimands, or source-language name. Legacy display translations
are curated data rather than paper-specific parser logic.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

_CJK = re.compile(r'[\u3400-\u9fff]')
_LEGACY = json.loads(Path(__file__).with_name("english_titles.json").read_text(encoding="utf-8"))


def display_title(record):
    mechanism = record.get("mechanism") or {}
    rid = str(record.get("record_id") or "unknown")
    title_en = mechanism.get("title_en")
    if isinstance(title_en, str) and title_en.strip() and not _CJK.search(title_en):
        return title_en.strip()
    curated = _LEGACY.get(rid)
    if curated:
        return curated
    original = mechanism.get("name")
    if isinstance(original, str) and original.strip() and not _CJK.search(original):
        return original.strip()
    return "DGP " + rid + " (English title required)"
