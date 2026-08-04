#!/usr/bin/env python3
"""Measure the share of Semantic Scholar conference papers with an arXiv ID.

Examples:
    uv run python scripts/measure_ss_arxiv_share.py
    uv run python scripts/measure_ss_arxiv_share.py --venue NeurIPS --years 2023-2025
    uv run python scripts/measure_ss_arxiv_share.py --venue NeurIPS --venue ICML --year 2025

The experiment is read-only and uses only Semantic Scholar metadata. It does not access the local
database, paper workspace, arXiv, or OpenReview.
"""

from __future__ import annotations

import argparse
import contextlib
import json
import os
import re
import sys
import tempfile
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
from typing import Any

_PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from backend.semantic_scholar import (  # noqa: E402
    SemanticScholarBulkPage,
    fetch_papers_bulk,
    iter_papers_bulk,
)

_YEAR_RANGE_RE = re.compile(r"^(\d{4})-(\d{4})$")
_DEFAULT_VENUES = ("NeurIPS",)
_DEFAULT_YEARS = (2025,)
_DEFAULT_CACHE_PATH = _PROJECT_ROOT / ".cache" / "ss_arxiv_share.json"
_CACHE_VERSION = 1


@dataclass(frozen=True)
class ShareResult:
    """One venue/year arXiv-share measurement."""

    venue: str
    year: int
    paper_count: int
    arxiv_count: int

    @property
    def percentage(self) -> float | None:
        """Return the arXiv share as a percentage, or None for an empty result."""
        if not self.paper_count:
            return None
        return self.arxiv_count / self.paper_count * 100


def has_arxiv_external_id(paper: dict[str, Any]) -> bool:
    """Return whether a paper has a non-empty arXiv external ID in S2 metadata."""
    external_ids = paper.get("externalIds")
    if not isinstance(external_ids, dict):
        return False
    return any(
        str(key).strip().lower() == "arxiv" and str(value or "").strip()
        for key, value in external_ids.items()
    )


def _query_key(venue: str, year: int) -> str:
    return json.dumps([venue, year], separators=(",", ":"))


def _load_cache(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"version": _CACHE_VERSION, "queries": {}}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"could not read cache {path}: {exc}") from exc
    if (
        not isinstance(payload, dict)
        or payload.get("version") != _CACHE_VERSION
        or not isinstance(payload.get("queries"), dict)
    ):
        raise ValueError(f"cache has an unsupported format: {path}")
    return payload


def _save_cache(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp_path: str | None = None
    try:
        fd, temp_path = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, ensure_ascii=False)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_path, path)
        temp_path = None
    finally:
        if temp_path:
            with contextlib.suppress(FileNotFoundError):
                os.unlink(temp_path)


def _new_cache_entry(venue: str, year: int) -> dict[str, Any]:
    return {
        "venue": venue,
        "year": year,
        "papers": [],
        "page_count": 0,
        "next_token": None,
        "estimated_total": None,
        "complete": False,
    }


def _progress_line(
    venue: str,
    year: int,
    *,
    page: int,
    paper_count: int,
    estimated_total: int | None,
) -> None:
    if estimated_total and estimated_total > 0:
        fraction = min(paper_count / estimated_total, 1.0)
        filled = round(24 * fraction)
        meter = "[" + "#" * filled + "." * (24 - filled) + "]"
        total = str(estimated_total)
    else:
        meter = "[papers]"
        total = "?"
    print(
        f"\r{venue} {year} {meter} {paper_count}/{total} papers (page {page})",
        end="",
        flush=True,
    )


def _measure_cached(
    venue: str,
    year: int,
    *,
    cache: dict[str, Any],
    cache_path: Path,
    show_progress: bool,
) -> ShareResult:
    queries = cache["queries"]
    key = _query_key(venue, year)
    entry = queries.get(key)
    if entry is None:
        entry = _new_cache_entry(venue, year)
        queries[key] = entry
    if not isinstance(entry, dict) or not isinstance(entry.get("papers"), list):
        raise ValueError(f"cache entry is malformed for {venue} {year}")

    papers = entry["papers"]
    if any(not isinstance(paper, dict) for paper in papers):
        raise ValueError(f"cache entry contains malformed papers for {venue} {year}")

    if entry.get("complete"):
        if show_progress:
            print(f"{venue} {year}: [cached] {len(papers)} papers")
        return ShareResult(venue, year, len(papers), sum(has_arxiv_external_id(p) for p in papers))

    next_token = str(entry.get("next_token") or "").strip() or None
    seen_paper_ids = {
        str(paper.get("paperId") or "").strip() for paper in papers if paper.get("paperId")
    }
    starting_page = int(entry.get("page_count") or 0)
    _save_cache(cache_path, cache)

    try:
        pages: Iterable[SemanticScholarBulkPage] = iter_papers_bulk(
            venue,
            year,
            continuation_token=next_token,
            seen_paper_ids=seen_paper_ids,
            starting_page=starting_page,
        )
        for page in pages:
            papers.extend(page.papers)
            entry["page_count"] = page.page_number
            entry["next_token"] = page.next_token or None
            entry["estimated_total"] = page.estimated_total
            entry["complete"] = not page.next_token
            _save_cache(cache_path, cache)
            if show_progress:
                _progress_line(
                    venue,
                    year,
                    page=page.page_number,
                    paper_count=len(papers),
                    estimated_total=page.estimated_total,
                )
    finally:
        if show_progress:
            print()

    return ShareResult(venue, year, len(papers), sum(has_arxiv_external_id(p) for p in papers))


def measure_share(
    venue: str,
    year: int,
    *,
    cache: dict[str, Any] | None = None,
    cache_path: Path | None = None,
    show_progress: bool = False,
) -> ShareResult:
    """Fetch and count all Semantic Scholar papers for one venue/year pair."""
    if cache is not None:
        if cache_path is None:
            raise ValueError("cache_path is required when caching is enabled")
        return _measure_cached(
            venue, year, cache=cache, cache_path=cache_path, show_progress=show_progress
        )

    papers = fetch_papers_bulk(venue, year)
    return ShareResult(
        venue=venue,
        year=year,
        paper_count=len(papers),
        arxiv_count=sum(has_arxiv_external_id(paper) for paper in papers),
    )


def _parse_year_range(raw: str) -> list[int]:
    match = _YEAR_RANGE_RE.fullmatch(raw.strip())
    if not match:
        raise ValueError("year range must use YYYY-YYYY, for example 2023-2025")
    start, end = (int(value) for value in match.groups())
    if start > end:
        raise ValueError("year range start must not be after its end")
    return list(range(start, end + 1))


def _resolve_years(args: argparse.Namespace) -> list[int]:
    if args.year and args.years:
        raise ValueError("--year and --years cannot be used together")
    years = args.year or (_parse_year_range(args.years) if args.years else list(_DEFAULT_YEARS))
    if any(year < 1900 or year > 2100 for year in years):
        raise ValueError("years must be between 1900 and 2100")
    return list(dict.fromkeys(years))


def _format_percentage(value: float | None) -> str:
    return "n/a" if value is None else f"{value:.1f}%"


def _print_results(results: Iterable[ShareResult]) -> None:
    rows = [
        (
            result.venue,
            str(result.year),
            str(result.paper_count),
            str(result.arxiv_count),
            _format_percentage(result.percentage),
        )
        for result in results
    ]
    headers = ("venue", "year", "S2 papers", "with arXiv", "share")
    widths = [
        max(len(header), *(len(row[index]) for row in rows)) for index, header in enumerate(headers)
    ]
    print("  ".join(header.ljust(widths[index]) for index, header in enumerate(headers)))
    print("  ".join("-" * width for width in widths))
    for row in rows:
        print("  ".join(value.ljust(widths[index]) for index, value in enumerate(row)))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Measure the share of Semantic Scholar conference papers with an arXiv ID"
    )
    parser.add_argument(
        "--venue",
        action="append",
        dest="venues",
        help="Semantic Scholar venue filter; repeat for multiple venues (default: NeurIPS)",
    )
    parser.add_argument(
        "--year",
        action="append",
        type=int,
        help="Conference year; repeat for multiple years",
    )
    parser.add_argument(
        "--years",
        help="Inclusive year range in YYYY-YYYY form, for example 2023-2025",
    )
    parser.add_argument(
        "--cache",
        type=Path,
        default=_DEFAULT_CACHE_PATH,
        help=f"Checkpoint cache path (default: {_DEFAULT_CACHE_PATH})",
    )
    parser.add_argument(
        "--refresh",
        action="store_true",
        help="Ignore cached results for the selected venue/year queries",
    )
    args = parser.parse_args(argv)

    try:
        venues = [venue.strip() for venue in (args.venues or _DEFAULT_VENUES) if venue.strip()]
        if not venues:
            raise ValueError("at least one non-empty venue is required")
        years = _resolve_years(args)
        cache = _load_cache(args.cache)
        results = []
        for venue in venues:
            for year in years:
                if args.refresh:
                    cache["queries"].pop(_query_key(venue, year), None)
                results.append(
                    measure_share(
                        venue,
                        year,
                        cache=cache,
                        cache_path=args.cache,
                        show_progress=True,
                    )
                )
    except KeyboardInterrupt:
        print(f"\ninterrupted; completed pages remain in {args.cache}", file=sys.stderr)
        return 130
    except (ValueError, RuntimeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    _print_results(results)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
