"""Backfill author metadata from LaTeX caches with S2 ORCID enrichment.

Only targets papers that have already been processed (have benchmark results)
but are missing author records.

Usage::
    uv run python scripts/backfill_authors.py --dry-run
    uv run python scripts/backfill_authors.py --limit 100
    uv run python scripts/backfill_authors.py --probe
"""

from __future__ import annotations

import argparse
import random
import sys
import time
from pathlib import Path

from sqlalchemy import or_
from tqdm import tqdm

_project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_project_root))

from backend.config import cfg  # noqa: E402
from backend.db import init_db, session_scope  # noqa: E402
from backend.llm_extractor import _extract_metadata_from_latex_cache  # noqa: E402
from backend.models import Paper, Result  # noqa: E402
from backend.paper_storage import PaperStorage  # noqa: E402
from backend.semantic_scholar import resolve_paper_authors  # noqa: E402
from backend.text_cleanup import authors_look_broken  # noqa: E402

_PROCESSED_STATUSES = {"extracted", "quarantined_yaml_parse", "quarantined_method_name"}


def _latex_dir_for(arxiv_id: str) -> Path:
    return cfg.papers_dir / arxiv_id / "latex"


def _needs_backfill(paper: Paper) -> bool:
    return not paper.authors or authors_look_broken(paper.authors)


def _papers_needing_backfill(session, *, with_results_only: bool) -> list[Paper]:
    query = session.query(Paper).filter(Paper.extraction_status.in_(_PROCESSED_STATUSES))
    if with_results_only:
        query = (
            query.join(Paper.results)
            .filter(or_(Result.is_problematic.is_(None), Result.is_problematic == 0))
            .distinct()
        )
    return [paper for paper in query.all() if _needs_backfill(paper)]


def _authors_for_paper(arxiv_id: str) -> list[dict[str, str | None]] | None:
    latex_names: list[str] | None = None
    latex_dir = _latex_dir_for(arxiv_id)
    if latex_dir.exists():
        latex_meta = _extract_metadata_from_latex_cache(latex_dir)
        raw_names = latex_meta.get("authors")
        if isinstance(raw_names, list) and raw_names:
            latex_names = [str(name) for name in raw_names if str(name).strip()]
    try:
        authors = resolve_paper_authors(arxiv_id, latex_names=latex_names)
        if authors and not authors_look_broken(authors):
            return authors
    except Exception:
        return None
    return None


def probe(sample_size: int = 50, *, with_results_only: bool = True) -> None:
    init_db()
    with session_scope() as session:
        papers = _papers_needing_backfill(session, with_results_only=with_results_only)
        if not papers:
            print("No processed papers with missing or broken authors found.")
            return
        if len(papers) > sample_size:
            random.shuffle(papers)
            papers = papers[:sample_size]

        latex_ok = s2_match = orcid_hits = 0
        for paper in papers:
            if not paper.arxiv_id:
                continue
            latex_dir = _latex_dir_for(paper.arxiv_id)
            latex_meta = _extract_metadata_from_latex_cache(latex_dir) if latex_dir.exists() else {}
            latex_names = latex_meta.get("authors")
            if not isinstance(latex_names, list) or not latex_names:
                continue
            latex_ok += 1
            authors = _authors_for_paper(paper.arxiv_id)
            if not authors:
                continue
            if any(entry.get("s2_author_id") for entry in authors):
                s2_match += 1
            if any(entry.get("orcid") for entry in authors):
                orcid_hits += 1
            time.sleep(1.1)

        total = len(papers)
        print(f"Sampled {total} processed paper(s) needing author repair in DB")
        print(f"  LaTeX authors parseable: {latex_ok}/{total}")
        print(f"  S2 authorId matched:     {s2_match}/{latex_ok or 1}")
        print(f"  At least one ORCID:      {orcid_hits}/{latex_ok or 1}")


def backfill(
    dry_run: bool = False,
    limit: int = 0,
    *,
    with_results_only: bool = True,
) -> None:
    init_db()
    updated = 0
    skipped = 0

    with session_scope() as session:
        papers = _papers_needing_backfill(session, with_results_only=with_results_only)
        total_needed = len(papers)
        scope = "with benchmark results" if with_results_only else "processed"
        if limit > 0:
            print(f"Found {total_needed} {scope} paper(s) needing authors — limited to {limit}")
            random.shuffle(papers)
            papers = papers[:limit]
        elif total_needed:
            print(f"Found {total_needed} {scope} paper(s) needing author backfill")

        with tqdm(total=len(papers), desc="0 updated, 0 skipped", unit="paper") as pbar:
            for paper in papers:
                if not paper.arxiv_id:
                    skipped += 1
                    pbar.set_description(f"{updated} updated, {skipped} skipped, no arxiv_id")
                else:
                    authors = _authors_for_paper(paper.arxiv_id)
                    if authors:
                        paper.authors = authors
                        PaperStorage(paper.arxiv_id).update_metadata({"authors": authors})
                        updated += 1
                        pbar.set_description(f"{updated} updated, {skipped} skipped, success")
                    else:
                        skipped += 1
                        pbar.set_description(
                            f"{updated} updated, {skipped} skipped, unresolved authors"
                        )
                pbar.update()
                time.sleep(1.1)

        if dry_run:
            session.rollback()

    print(f"Done — updated: {updated}, skipped/unchanged: {skipped}")


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description="Backfill author metadata from LaTeX with S2 ORCID enrichment"
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Print changes without writing to DB"
    )
    parser.add_argument(
        "--limit", type=int, default=0, help="Process at most N papers (0 = unlimited)"
    )
    parser.add_argument(
        "--include-all",
        action="store_true",
        help="Include processed papers without benchmark results",
    )
    parser.add_argument(
        "--probe",
        action="store_true",
        help="Sample papers and report LaTeX/S2/ORCID coverage (no DB writes)",
    )
    parser.add_argument(
        "--probe-sample",
        type=int,
        default=50,
        help="Number of papers to sample for --probe (default: 50)",
    )
    args = parser.parse_args(argv)

    if args.probe:
        probe(sample_size=args.probe_sample, with_results_only=not args.include_all)
        return

    backfill(
        dry_run=args.dry_run,
        limit=args.limit,
        with_results_only=not args.include_all,
    )


if __name__ == "__main__":
    main()
