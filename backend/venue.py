"""Helpers for publication venue strings."""

from __future__ import annotations

import re

_ARXIV_VENUE_ONLY_RE = re.compile(
    r"^(?:arxiv(?:\s*(?:org|e-prints?|preprints?|preprint))?|corr(?:\s*/\s*arxiv)?)$",
    re.IGNORECASE,
)

_LOG_IN_JOURNAL_ISSNS = frozenset({"0720-8642", "1547-4690", "0024-5798"})

_LOG_YEAR_RE = re.compile(r"\blog\s*20\d{2}\b", re.IGNORECASE)

_CONFERENCE_ALIASES: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("NeurIPS", ("neurips", "nips", "neural information processing systems")),
    ("ICLR", ("iclr", "international conference on learning representations")),
    (
        "TMLR",
        ("tmlr", "transactions on machine learning research", "trans. mach. learn. res."),
    ),
    ("JMLR", ("jmlr", "journal of machine learning research", "j. mach. learn. res.")),
    ("ICML", ("icml", "international conference on machine learning")),
    (
        "LoG",
        (
            "learning on graphs and geometry",
            "learning on graphs and geometry conference",
            "learning on graphs conference",
            "second learning on graphs conference",
            "graph learning conference",
            "proceedings of the",
        ),
    ),
    (
        "WWW",
        (
            "www",
            "the web conference",
            "world wide web conference",
            "world-wide web conference",
        ),
    ),
    ("AAAI", ("aaai", "association for the advancement of artificial intelligence")),
    ("KDD", ("kdd", "sigkdd", "knowledge discovery and data mining")),
    ("IJCAI", ("ijcai", "international joint conference on artificial intelligence")),
)

_SHORT_CONFERENCE_ALIASES = frozenset(
    alias for _label, aliases in _CONFERENCE_ALIASES for alias in aliases if len(alias) <= 5
)

_LOG_CANONICAL_NAME = "Learning on Graphs Conference"


def _slug(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.strip().lower()).strip("-")


def is_arxiv_only_venue(venue: str | None) -> bool:
    """Return True when *venue* is only an arXiv / CoRR label, not a real publication venue."""
    raw = " ".join(str(venue or "").split()).strip()
    if not raw:
        return False
    if _ARXIV_VENUE_ONLY_RE.match(raw):
        return True
    lowered = raw.lower()
    remainder = re.sub(r"\barxiv\b", "", lowered)
    remainder = re.sub(r"\b(?:org|e-prints?|preprints?|preprint|corr)\b", "", remainder)
    remainder = re.sub(r"[^a-z0-9]+", "", remainder)
    return remainder == ""


def _is_log_in_journal_name(name: str) -> bool:
    return re.fullmatch(r"log\s+in", name.strip(), flags=re.IGNORECASE) is not None


def is_untrusted_s2_publication_venue(pub_venue: object) -> bool:
    """Return True when S2 ``publicationVenue`` metadata points at the LOG IN school journal."""
    if not isinstance(pub_venue, dict):
        return _is_log_in_journal_name(str(pub_venue or ""))
    name = str(pub_venue.get("name") or pub_venue.get("venue") or "").strip()
    if not _is_log_in_journal_name(name):
        return False
    venue_type = str(pub_venue.get("type") or "").strip().lower()
    if venue_type == "journal":
        return True
    issn_values: list[str] = []
    for key in ("issn", "alternate_issns"):
        raw = pub_venue.get(key)
        if isinstance(raw, str) and raw.strip():
            issn_values.append(raw.strip())
        elif isinstance(raw, list):
            issn_values.extend(str(item).strip() for item in raw if str(item).strip())
    if any(issn in _LOG_IN_JOURNAL_ISSNS for issn in issn_values):
        return True
    url_values: list[str] = []
    for key in ("url", "alternate_urls"):
        raw = pub_venue.get(key)
        if isinstance(raw, str) and raw.strip():
            url_values.append(raw.strip().lower())
        elif isinstance(raw, list):
            url_values.extend(str(item).strip().lower() for item in raw if str(item).strip())
    return any("log-in-verlag.de" in url for url in url_values)


def is_untrusted_venue(venue: str | None) -> bool:
    """Return True for venue strings that should be treated as missing/unreliable."""
    raw = " ".join(str(venue or "").split()).strip()
    if not raw:
        return False
    return _is_log_in_journal_name(raw)


def venue_needs_resolution(venue: str | None) -> bool:
    """Return True when a stored venue should be overwritten during enrichment."""
    raw = " ".join(str(venue or "").split()).strip()
    if not raw:
        return True
    return is_arxiv_only_venue(raw) or is_untrusted_venue(raw)


def venue_from_openreview_fields(venue: str | None, venueid: str | None = None) -> str:
    """Map OpenReview venue / venueid strings to a canonical venue name."""
    venue_text = " ".join(str(venue or "").split()).strip()
    venueid_text = str(venueid or "").strip().lower()
    if venueid_text and "log/" in venueid_text and "logconference.io" in venueid_text:
        return _LOG_CANONICAL_NAME
    if venue_text:
        return venue_from_arxiv_comment(venue_text)
    return ""


def venue_from_arxiv_comment(comment: str | None) -> str:
    """Map arXiv comment / journal-ref text to a canonical venue string."""
    raw = " ".join(str(comment or "").split()).strip()
    if not raw:
        return ""
    if is_untrusted_venue(raw):
        return ""
    if _LOG_YEAR_RE.search(raw):
        return _LOG_CANONICAL_NAME
    short = normalize_conference_short(raw)
    if short == "LoG":
        return _LOG_CANONICAL_NAME
    if short:
        return raw
    return ""


def normalize_conference_short(venue: str | None) -> str:
    """Return a short conference label such as ``LoG`` or ``NeurIPS``."""
    raw = " ".join(str(venue or "").split()).strip()
    if not raw or is_arxiv_only_venue(raw) or is_untrusted_venue(raw):
        return ""
    lowered = raw.lower()
    if _LOG_YEAR_RE.search(lowered):
        return "LoG"
    for label, aliases in _CONFERENCE_ALIASES:
        for alias in aliases:
            if alias in _SHORT_CONFERENCE_ALIASES:
                if alias == "www":
                    if re.search(r"\bwww(?:\s*[-/]?\s*\d{4})?\b", lowered):
                        return label
                elif re.search(rf"\b{re.escape(alias)}\b", lowered):
                    return label
            elif alias == "proceedings of the":
                if alias in lowered and "learning on graphs" in lowered:
                    return label
            elif alias in lowered:
                return label
    return ""


def publication_year(published_date: str | None) -> str:
    raw = (published_date or "").strip()
    if len(raw) >= 4 and raw[:4].isdigit():
        year = int(raw[:4])
        if 1990 <= year <= 2100:
            return str(year)
    return ""


def conference_export_fields(venue: str | None, published_date: str | None) -> dict[str, str]:
    if is_arxiv_only_venue(venue) or is_untrusted_venue(venue):
        venue = None
    short = normalize_conference_short(venue)
    if not short:
        return {
            "published_conference": "",
            "published_conference_short": "",
            "published_conference_slug": "",
        }
    year = publication_year(published_date)
    label = f"{short} {year}" if year else short
    return {
        "published_conference": label,
        "published_conference_short": short,
        "published_conference_slug": _slug(short),
    }


def resolve_canonical_venue(venue: str | None) -> str:
    """Return a canonical venue string safe to store, or empty when untrusted/unrecognized."""
    raw = " ".join(str(venue or "").split()).strip()
    if not raw or is_arxiv_only_venue(raw) or is_untrusted_venue(raw):
        return ""
    short = normalize_conference_short(raw)
    if short == "LoG":
        return _LOG_CANONICAL_NAME
    if short:
        return raw
    return raw


def export_published_venue(venue: str | None, published_date: str | None = None) -> str:
    """Normalized conference label safe for Hugo export and conference-badge fallbacks."""
    fields = conference_export_fields(venue, published_date)
    return fields["published_conference"]
