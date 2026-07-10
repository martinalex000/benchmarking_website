"""Alternative paper downloader for non-arXiv papers (OpenReview, ACM, IEEE, etc.).

Attempts a best-effort download of the PDF given a URL.
Marks the download_source in paper metadata.

Usage::
    python -m backend.alternative_downloader --paper-id 42 --url https://openreview.net/pdf?id=XYZ
"""

from __future__ import annotations

import argparse
import logging
import time
from urllib.parse import urljoin

import requests
from tenacity import retry, stop_after_attempt, wait_exponential

from backend.config import cfg
from backend.db import init_db, session_scope
from backend.models import Paper, PipelineRun
from backend.paper_storage import PaperStorage
from backend.url_safety import UnsafeUrlError, validate_public_http_url

logger = logging.getLogger(__name__)
MAX_PDF_BYTES = 200 * 1024 * 1024
_MAX_REDIRECTS = 5

# Rotate user agents to reduce blocking on publisher sites
_USER_AGENTS = [
    "Mozilla/5.0 (X11; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15",
]
_ua_idx = 0


def _next_ua() -> str:
    global _ua_idx
    ua = _USER_AGENTS[_ua_idx % len(_USER_AGENTS)]
    _ua_idx += 1
    return ua


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=2, min=5, max=60), reraise=True)
def _get_pdf(url: str) -> bytes:
    headers = {"User-Agent": _next_ua()}
    resp = _safe_get(url, headers)

    content_type = resp.headers.get("Content-Type", "")
    if "pdf" not in content_type.lower() and not url.lower().endswith(".pdf"):
        # Check first few bytes for PDF magic number
        first_bytes = b""
        for chunk in resp.iter_content(1024):
            first_bytes = chunk
            break
        if not first_bytes.startswith(b"%PDF"):
            raise ValueError(f"URL does not appear to serve a PDF (Content-Type: {content_type})")
        # Reset by re-requesting — simpler than buffering
        resp = _safe_get(url, headers)

    chunks: list[bytes] = []
    total = 0
    for chunk in resp.iter_content(chunk_size=8192):
        total += len(chunk)
        if total > MAX_PDF_BYTES:
            raise ValueError(f"PDF exceeds {MAX_PDF_BYTES // (1024 * 1024)} MB limit")
        chunks.append(chunk)
    return b"".join(chunks)


def _safe_get(url: str, headers: dict[str, str]) -> requests.Response:
    current = validate_public_http_url(url)
    for _ in range(_MAX_REDIRECTS + 1):
        resp = requests.get(
            current,
            headers=headers,
            timeout=90,
            allow_redirects=False,
            stream=True,
        )
        if not resp.is_redirect:
            resp.raise_for_status()
            content_length = resp.headers.get("Content-Length")
            if content_length and _parse_content_length(content_length) > MAX_PDF_BYTES:
                raise ValueError(f"PDF exceeds {MAX_PDF_BYTES // (1024 * 1024)} MB limit")
            return resp
        location = resp.headers.get("Location")
        if not location:
            raise UnsafeUrlError("Redirect response has no Location header")
        current = validate_public_http_url(urljoin(current, location))
    raise UnsafeUrlError(f"Too many redirects while fetching {url!r}")


def _parse_content_length(raw: str) -> int:
    try:
        return int(raw)
    except (TypeError, ValueError):
        return 0


def _detect_source(url: str) -> str:
    url_lower = url.lower()
    if "openreview.net" in url_lower:
        return "openreview"
    if "dl.acm.org" in url_lower or "acm.org" in url_lower:
        return "acm"
    if "ieeexplore.ieee.org" in url_lower:
        return "ieee"
    if "papers.nips.cc" in url_lower or "proceedings.neurips.cc" in url_lower:
        return "neurips"
    if "proceedings.mlr.press" in url_lower:
        return "pmlr"
    return "other"


def download_alternative(paper_id: int, url: str) -> bool:
    """Download PDF from an alternative source and store it.

    Returns True on success.
    """
    init_db()

    with session_scope() as session:
        paper = session.get(Paper, paper_id)
        if paper is None:
            logger.error("Paper ID %d not found", paper_id)
            return False
        arxiv_id = paper.arxiv_id or f"noid_{paper_id}"

    storage = PaperStorage(arxiv_id)
    storage.init_paper({"paper_id": paper_id, "alternative_url": url})

    source = _detect_source(url)
    logger.info("Downloading from %s: %s", source, url)

    try:
        pdf_bytes = _get_pdf(url)
        time.sleep(2)
    except Exception as exc:
        logger.error("Failed to download alternative PDF: %s", exc)
        with session_scope() as session:
            session.add(
                PipelineRun(
                    paper_id=paper_id, stage="download", status="failed", error_message=str(exc)
                )
            )
        return False

    storage.root.mkdir(parents=True, exist_ok=True)
    storage.pdf_path.write_bytes(pdf_bytes)
    size_kb = len(pdf_bytes) // 1024
    logger.info("Saved PDF for paper %d (%d KB) from %s", paper_id, size_kb, source)

    with session_scope() as session:
        paper = session.get(Paper, paper_id)
        if paper:
            paper.pdf_path = str(storage.pdf_path.relative_to(cfg.project_root))
            paper.extraction_status = "downloaded"

    storage.update_metadata(
        {
            "download_source": source,
            "download_url": url,
            "pdf_path": str(storage.pdf_path),
            "html_available": False,
            "status": "downloaded",
        }
    )

    with session_scope() as session:
        session.add(PipelineRun(paper_id=paper_id, stage="download", status="success"))

    return True


# ── CLI ───────────────────────────────────────────────────────────────────────


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Download a paper PDF from an alternative source")
    p.add_argument("--paper-id", type=int, required=True, help="Database paper ID")
    p.add_argument("--url", required=True, help="Direct URL to the PDF")
    return p


def main(argv: list[str] | None = None) -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    args = _build_parser().parse_args(argv)
    ok = download_alternative(args.paper_id, args.url)
    print("Success" if ok else "Failed")


if __name__ == "__main__":
    main()
