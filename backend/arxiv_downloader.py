"""ArXiv paper downloader — LaTeX source first, then PDF.

Download order:
  1. LaTeX source tarball (arxiv.org/src/) — best for extraction (structured tables).
  2. PDF (arxiv.org/pdf/) — always downloaded as fallback and for figure rendering.

Usage::
    python -m backend.arxiv_downloader 2206.08164
    python -m backend.arxiv_downloader 2206.08164 2512.04475 --force
"""

from __future__ import annotations

import argparse
import logging
import re
import time

import requests
from tenacity import retry, stop_after_attempt, wait_exponential

from backend.config import cfg, normalize_arxiv_id
from backend.db import init_db, session_scope
from backend.models import Paper, PipelineRun
from backend.paper_storage import PaperStorage

logger = logging.getLogger(__name__)

ARXIV_PDF_URL = "https://arxiv.org/pdf/{arxiv_id}"
ARXIV_ABS_URL = "https://arxiv.org/abs/{arxiv_id}"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (compatible; GraphBenchBot/1.0; +https://github.com/benchmarking-website)"
    )
}


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=2, min=5, max=60), reraise=True)
def _get(url: str, stream: bool = False, timeout: int = 60) -> requests.Response:
    resp = requests.get(url, headers=HEADERS, stream=stream, timeout=timeout, allow_redirects=True)
    resp.raise_for_status()
    return resp


def _detect_version(response: requests.Response) -> int | None:
    """Try to read arXiv version from the response URL or headers."""
    final_url = response.url
    m = re.search(r"v(\d+)$", final_url.rstrip("/").split("?")[0])
    if m:
        return int(m.group(1))
    return None


def _download_latex(arxiv_id: str, storage: PaperStorage) -> bool:
    """Download and expand the arXiv LaTeX source tarball.

    Returns True when the expanded.tex was successfully cached, False otherwise.
    """
    try:
        from backend.latex_source import download_and_parse

        result = download_and_parse(arxiv_id, storage.latex_dir)
        if result is not None:
            logger.info(
                "LaTeX source cached for arXiv:%s (%d chars)",
                arxiv_id,
                len(
                    (storage.latex_dir / "expanded.tex").read_text(errors="replace")
                    if (storage.latex_dir / "expanded.tex").exists()
                    else ""
                ),
            )
            return True
        logger.info("No LaTeX source available for arXiv:%s", arxiv_id)
        return False
    except Exception as exc:
        logger.warning("LaTeX download failed for arXiv:%s: %s", arxiv_id, exc)
        return False


def _download_pdf(arxiv_id: str, storage: PaperStorage) -> int | None:
    """Download the arXiv PDF. Returns detected version number or None."""
    url = ARXIV_PDF_URL.format(arxiv_id=arxiv_id)
    resp = _get(url, stream=True)
    version = _detect_version(resp)

    storage.root.mkdir(parents=True, exist_ok=True)
    with storage.pdf_path.open("wb") as fh:
        for chunk in resp.iter_content(chunk_size=8192):
            fh.write(chunk)

    size_kb = storage.pdf_path.stat().st_size // 1024
    logger.info("Downloaded PDF for arXiv:%s (%d KB, version=%s)", arxiv_id, size_kb, version)
    return version


def download_paper(arxiv_id: str, force: bool = False) -> bool:
    """Download a paper (LaTeX source + PDF) and update the database.

    Download order:
      1. LaTeX source (best for extraction — skipped silently if unavailable).
      2. PDF (always downloaded; used for figure rendering and as text fallback).

    Returns True on success, False on failure.
    """
    init_db()
    storage = PaperStorage(arxiv_id)

    with session_scope() as session:
        paper = session.query(Paper).filter_by(arxiv_id=arxiv_id).first()
        if paper is None:
            logger.warning("arXiv:%s not found in database — inserting stub", arxiv_id)
            paper = Paper(
                arxiv_id=arxiv_id,
                title=f"arXiv:{arxiv_id}",
                extraction_status="pending",
                discovery_source="manual",
            )
            session.add(paper)
            session.flush()

        # Only skip if files actually exist on disk — a paper can have
        # status=extracted but be missing from disk (deleted/moved).
        has_files = storage.pdf_path.exists() or (storage.latex_dir / "expanded.tex").exists()
        if not force and paper.extraction_status not in ("pending", "failed"):
            if has_files:
                logger.info(
                    "Skipping arXiv:%s (status=%s, files present)",
                    arxiv_id,
                    paper.extraction_status,
                )
                return True
            logger.info(
                "Resetting arXiv:%s status=%s — files missing, forcing re-download",
                arxiv_id,
                paper.extraction_status,
            )
            paper.extraction_status = "pending"

        paper_id = paper.id

    # Initialise folder and tracking files
    storage.init_paper({"arxiv_id": arxiv_id, "status": "downloading"})

    version = None
    latex_available = False

    try:
        # Step 1: LaTeX source (best for extraction; silently skipped if unavailable)
        latex_available = _download_latex(arxiv_id, storage)
        time.sleep(1)

        # Step 2: PDF (always; needed for figure rendering and text fallback)
        version = _download_pdf(arxiv_id, storage)

    except Exception as exc:
        logger.error("Download failed for arXiv:%s: %s", arxiv_id, exc)
        _record_run(paper_id, "download", "failed", str(exc))
        _update_paper_status(paper_id, "failed")
        return False

    # Update DB
    with session_scope() as session:
        paper = session.get(Paper, paper_id)
        if paper:
            paper.arxiv_version = version
            paper.pdf_path = str(storage.pdf_path.relative_to(cfg.project_root))
            paper.extraction_status = "downloaded"

    storage.update_metadata(
        {
            "arxiv_version": version,
            "latex_available": latex_available,
            "pdf_path": str(storage.pdf_path),
            "status": "downloaded",
        }
    )

    _record_run(paper_id, "download", "success", None)
    logger.info(
        "arXiv:%s downloaded (latex=%s, version=%s)",
        arxiv_id,
        latex_available,
        version,
    )
    return True


def _update_paper_status(paper_id: int, status: str) -> None:
    with session_scope() as session:
        paper = session.get(Paper, paper_id)
        if paper:
            paper.extraction_status = status


def _record_run(paper_id: int, stage: str, status: str, error: str | None) -> None:
    with session_scope() as session:
        session.add(
            PipelineRun(
                paper_id=paper_id,
                stage=stage,
                status=status,
                error_message=error,
            )
        )


# ── CLI ───────────────────────────────────────────────────────────────────────


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Download arXiv papers (HTML + PDF)")
    p.add_argument("arxiv_ids", nargs="+", metavar="ARXIV_ID", help="arXiv IDs to download")
    p.add_argument("--force", action="store_true", help="Re-download even if already downloaded")
    return p


def main(argv: list[str] | None = None) -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    args = _build_parser().parse_args(argv)

    ok = total = 0
    for arxiv_id in args.arxiv_ids:
        arxiv_id = normalize_arxiv_id(arxiv_id)
        total += 1
        if download_paper(arxiv_id, force=args.force):
            ok += 1

    print(f"Downloaded {ok}/{total} papers.")


if __name__ == "__main__":
    main()
