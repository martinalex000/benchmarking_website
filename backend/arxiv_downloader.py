"""ArXiv paper downloader — HTML preferred, PDF always downloaded.

HTML version gives cleaner table structure for extraction.
PDF is always downloaded too because it is needed for TikZ/vector figure rendering.

Usage::
    python -m backend.arxiv_downloader 2206.08164
    python -m backend.arxiv_downloader 2206.08164 2512.04475 --force
"""

from __future__ import annotations

import argparse
import logging
import re
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from tenacity import retry, stop_after_attempt, wait_exponential

from backend.config import cfg
from backend.db import init_db, session_scope
from backend.models import Paper, PipelineRun
from backend.paper_storage import PaperStorage

logger = logging.getLogger(__name__)

ARXIV_HTML_URL = "https://arxiv.org/html/{arxiv_id}"
ARXIV_PDF_URL = "https://arxiv.org/pdf/{arxiv_id}"
ARXIV_ABS_URL = "https://arxiv.org/abs/{arxiv_id}"

# Only download these asset types from the HTML page
ASSET_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (compatible; GraphBenchBot/1.0; " "+https://github.com/benchmarking-website)"
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


def _download_html(arxiv_id: str, storage: PaperStorage) -> bool:
    """Download the arXiv HTML version and its linked image assets.

    Returns True if HTML was available, False if not.
    """
    url = ARXIV_HTML_URL.format(arxiv_id=arxiv_id)
    try:
        resp = _get(url)
    except requests.HTTPError as exc:
        if exc.response is not None and exc.response.status_code in (404, 403):
            logger.info("No HTML version available for arXiv:%s", arxiv_id)
            return False
        raise

    storage.html_dir.mkdir(parents=True, exist_ok=True)
    storage.html_index_path.write_bytes(resp.content)
    logger.info("Downloaded HTML for arXiv:%s (%d bytes)", arxiv_id, len(resp.content))

    # Download linked image assets
    soup = BeautifulSoup(resp.content, "lxml")
    base_url = resp.url
    downloaded_assets = 0

    for img_tag in soup.find_all("img", src=True):
        src = img_tag["src"]
        asset_url = urljoin(base_url, src)
        parsed = urlparse(asset_url)
        suffix = Path(parsed.path).suffix.lower()
        if suffix not in ASSET_EXTENSIONS:
            continue
        asset_name = Path(parsed.path).name
        dest = storage.html_dir / asset_name
        if dest.exists():
            continue
        try:
            asset_resp = _get(asset_url, timeout=30)
            dest.write_bytes(asset_resp.content)
            downloaded_assets += 1
            time.sleep(0.3)
        except Exception as exc:
            logger.debug("Could not download asset %s: %s", asset_url, exc)

    logger.info("Downloaded %d image assets for arXiv:%s", downloaded_assets, arxiv_id)
    return True


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
    """Download a paper (HTML + PDF) and update the database.

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

        if not force and paper.extraction_status not in ("pending", "failed"):
            logger.info("Skipping arXiv:%s (status=%s)", arxiv_id, paper.extraction_status)
            return True

        paper_id = paper.id

    # Initialise folder and tracking files
    storage.init_paper({"arxiv_id": arxiv_id, "status": "downloading"})

    html_available = False
    version = None
    success = True

    try:
        # Always download PDF first
        version = _download_pdf(arxiv_id, storage)
        time.sleep(3)

        # Attempt HTML download
        html_available = _download_html(arxiv_id, storage)
        time.sleep(1)

    except Exception as exc:
        logger.error("Download failed for arXiv:%s: %s", arxiv_id, exc)
        success = False
        _record_run(paper_id, "download", "failed", str(exc))
        _update_paper_status(paper_id, "failed")
        return False

    # Update DB
    with session_scope() as session:
        paper = session.get(Paper, paper_id)
        if paper:
            paper.arxiv_version = version
            paper.pdf_path = str(storage.pdf_path.relative_to(cfg.project_root))
            if html_available:
                paper.html_path = str(storage.html_index_path.relative_to(cfg.project_root))
            paper.extraction_status = "downloaded"

    storage.update_metadata(
        {
            "arxiv_version": version,
            "html_available": html_available,
            "pdf_path": str(storage.pdf_path),
            "html_path": str(storage.html_index_path) if html_available else None,
            "status": "downloaded",
        }
    )

    _record_run(paper_id, "download", "success", None)
    logger.info("arXiv:%s downloaded (html=%s, version=%s)", arxiv_id, html_available, version)
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
        arxiv_id = arxiv_id.strip().lstrip("arXiv:").split("v")[0]
        total += 1
        if download_paper(arxiv_id, force=args.force):
            ok += 1

    print(f"Downloaded {ok}/{total} papers.")


if __name__ == "__main__":
    main()
