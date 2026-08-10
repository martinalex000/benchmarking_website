"""Regenerate local paper screenshots and site assets from database context.

This script does not run full LLM extraction. It uses the database to select
papers, downloads the corresponding arXiv assets when needed, then recreates the
main figure from existing per-paper extraction metadata.
"""

from __future__ import annotations

import argparse
import logging
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from tqdm import tqdm

_project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_project_root))

from backend.arxiv_downloader import download_paper  # noqa: E402
from backend.config import cfg, normalize_arxiv_id  # noqa: E402
from backend.db import init_db, session_scope  # noqa: E402
from backend.export_to_hugo import _copy_main_figure_if_newer  # noqa: E402
from backend.figure_extractor import extract_main_figure  # noqa: E402
from backend.html_parser import parse_html_paper  # noqa: E402
from backend.models import Paper  # noqa: E402
from backend.paper_storage import PaperStorage  # noqa: E402

logger = logging.getLogger(__name__)


@dataclass
class FigureResult:
    arxiv_id: str
    status: str
    detail: str = ""


def _paper_ids(arxiv_ids: list[str] | None, *, only_with_results: bool) -> list[str]:
    if arxiv_ids:
        return [normalize_arxiv_id(arxiv_id) for arxiv_id in arxiv_ids]

    with session_scope() as session:
        query = session.query(Paper.arxiv_id).filter(Paper.arxiv_id.isnot(None))
        if only_with_results:
            query = query.filter(Paper.results.any())
        ids = [row[0] for row in query.order_by(Paper.published_date.desc(), Paper.arxiv_id).all()]
    return [arxiv_id for arxiv_id in ids if arxiv_id]


def _has_downloaded_assets(storage: PaperStorage) -> bool:
    return (
        storage.pdf_path.exists()
        or storage.html_index_path.exists()
        or (storage.latex_dir / "expanded.tex").exists()
    )


def _figure_info_from_existing_output(storage: PaperStorage) -> dict[str, Any]:
    output = storage.load_llm_output()
    figure = output.get("figure")
    return figure if isinstance(figure, dict) else {}


def _fallback_figure_info(storage: PaperStorage) -> dict[str, Any]:
    if storage.html_index_path.exists():
        try:
            parsed = parse_html_paper(storage.html_index_path)
        except Exception as exc:
            logger.warning("HTML parse failed for arXiv:%s: %s", storage.arxiv_id, exc)
        else:
            if parsed.figures:
                return {
                    "img_src": parsed.figures[0].src,
                    "reason": "first HTML figure",
                }

    if storage.pdf_path.exists():
        return {
            "page_number": 0,
            "reason": "title page (PDF page 1)",
        }

    return {}


def _copy_site_figure(arxiv_id: str, figure_path: Path) -> Path:
    dest = cfg.site_dir / "static" / "figures" / arxiv_id / figure_path.name
    _copy_main_figure_if_newer(figure_path, dest)
    return dest


def regenerate_one(
    arxiv_id: str,
    *,
    force_download: bool,
    force_extract: bool,
    detect_missing_figures: bool,
    copy_to_site: bool,
    dry_run: bool,
) -> FigureResult:
    storage = PaperStorage(arxiv_id)

    if not _has_downloaded_assets(storage) or force_download:
        if dry_run:
            return FigureResult(arxiv_id, "would-download")
        if not download_paper(arxiv_id, force=force_download):
            return FigureResult(arxiv_id, "download-failed")

    existing = storage.main_figure_path
    if existing and existing.exists() and not force_extract:
        if copy_to_site:
            if dry_run:
                return FigureResult(arxiv_id, "would-copy-site", existing.name)
            dest = _copy_site_figure(arxiv_id, existing)
            return FigureResult(arxiv_id, "copied-site", str(dest.relative_to(cfg.project_root)))
        return FigureResult(arxiv_id, "exists", existing.name)

    figure_info = _figure_info_from_existing_output(storage)
    if (
        not figure_info.get("img_src")
        and figure_info.get("page_number") is None
        and detect_missing_figures
    ):
        figure_info = _fallback_figure_info(storage)

    if not figure_info.get("img_src") and figure_info.get("page_number") is None:
        return FigureResult(arxiv_id, "missing-figure-metadata")

    if dry_run:
        return FigureResult(arxiv_id, "would-extract")

    figure_path = extract_main_figure(storage, figure_info)
    if not figure_path:
        return FigureResult(arxiv_id, "extract-failed")

    if copy_to_site:
        dest = _copy_site_figure(arxiv_id, figure_path)
        return FigureResult(arxiv_id, "extracted-site", str(dest.relative_to(cfg.project_root)))

    return FigureResult(arxiv_id, "extracted", figure_path.name)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("arxiv_ids", nargs="*", help="Specific arXiv IDs; defaults to DB papers")
    parser.add_argument(
        "--all-db-papers",
        action="store_true",
        help="Process all DB papers instead of only papers with benchmark results",
    )
    parser.add_argument("--force-download", action="store_true", help="Re-download arXiv assets")
    parser.add_argument("--force-extract", action="store_true", help="Recreate existing figures")
    parser.add_argument(
        "--detect-missing-figures",
        action="store_true",
        help="Fallback to first HTML figure or PDF title page when extraction metadata is missing",
    )
    parser.add_argument(
        "--no-site-copy",
        action="store_true",
        help="Only regenerate papers/{arxiv_id}/figures, not site/static/figures",
    )
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s %(message)s",
    )
    init_db()

    ids = _paper_ids(args.arxiv_ids or None, only_with_results=not args.all_db_papers)
    results: list[FigureResult] = []
    for arxiv_id in tqdm(ids, desc="Regenerating figures", unit="paper"):
        results.append(
            regenerate_one(
                arxiv_id,
                force_download=args.force_download,
                force_extract=args.force_extract,
                detect_missing_figures=args.detect_missing_figures,
                copy_to_site=not args.no_site_copy,
                dry_run=args.dry_run,
            )
        )

    counts: dict[str, int] = {}
    for result in results:
        counts[result.status] = counts.get(result.status, 0) + 1
    for status, count in sorted(counts.items()):
        print(f"{status}: {count}")

    failures = [r for r in results if r.status.endswith("failed")]
    missing = [r for r in results if r.status == "missing-figure-metadata"]
    if missing:
        print(f"missing metadata examples: {', '.join(r.arxiv_id for r in missing[:10])}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
