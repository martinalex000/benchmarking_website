"""Figure extractor — saves the main figure identified by the LLM.

For HTML papers: downloads the <img> src.
For PDF papers: renders the identified page/region to a PNG at 300 dpi.
TikZ / vector figures in PDF are handled by rendering the full page to PNG.
"""
from __future__ import annotations

import logging
import shutil
from pathlib import Path
from urllib.parse import urljoin

import requests

from backend.paper_storage import PaperStorage

logger = logging.getLogger(__name__)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (compatible; GraphBenchBot/1.0; "
        "+https://github.com/benchmarking-website)"
    )
}


def extract_from_html(
    storage: PaperStorage,
    img_src: str,
    base_url: str = "",
) -> Path | None:
    """Download the figure image from the HTML paper.

    img_src can be:
      - a relative path (e.g. "x1.png")  → resolved against the html/ dir
      - a full URL                        → downloaded directly
    """
    figures_dir = storage.figures_dir
    figures_dir.mkdir(parents=True, exist_ok=True)
    dest = figures_dir / "main_figure_raw"

    # First check if the asset was already downloaded alongside the HTML
    local_candidate = storage.html_dir / img_src
    if local_candidate.exists():
        suffix = local_candidate.suffix.lower()
        final = figures_dir / f"main_figure{suffix}"
        shutil.copy2(local_candidate, final)
        logger.info("Copied local asset %s → %s", local_candidate.name, final.name)
        return final

    # Try downloading from absolute or composed URL
    if base_url:
        url = urljoin(base_url, img_src)
    else:
        url = img_src

    if not url.startswith("http"):
        logger.warning("Cannot resolve img src '%s' for arXiv:%s", img_src, storage.arxiv_id)
        return None

    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
        resp.raise_for_status()
        content_type = resp.headers.get("Content-Type", "")
        ext = _ext_from_content_type(content_type) or Path(url).suffix.lower() or ".png"
        final = figures_dir / f"main_figure{ext}"
        final.write_bytes(resp.content)
        logger.info("Downloaded main figure from %s → %s", url, final.name)
        return final
    except Exception as exc:
        logger.error("Failed to download figure %s: %s", url, exc)
        return None


def extract_from_pdf(
    storage: PaperStorage,
    page_number: int,           # 0-indexed
    dpi: int = 300,
    clip_rect: tuple[float, float, float, float] | None = None,
) -> Path | None:
    """Render a PDF page (or a clipped region) to PNG at the given DPI.

    This handles TikZ and other vector figures by rasterising the page.
    clip_rect: (x0, y0, x1, y1) in PDF points; if None the full page is rendered.
    """
    try:
        import fitz  # PyMuPDF
    except ImportError as exc:
        raise RuntimeError("PyMuPDF not installed") from exc

    if not storage.pdf_path.exists():
        logger.error("PDF not found for arXiv:%s", storage.arxiv_id)
        return None

    storage.figures_dir.mkdir(parents=True, exist_ok=True)
    dest = storage.figures_dir / "main_figure.png"

    try:
        doc = fitz.open(str(storage.pdf_path))
        if page_number >= len(doc):
            logger.error("Page %d out of range for arXiv:%s (%d pages)", page_number, storage.arxiv_id, len(doc))
            doc.close()
            return None

        page = doc[page_number]
        matrix = fitz.Matrix(dpi / 72, dpi / 72)

        if clip_rect is not None:
            rect = fitz.Rect(*clip_rect)
            pix = page.get_pixmap(matrix=matrix, clip=rect)
        else:
            pix = page.get_pixmap(matrix=matrix)

        pix.save(str(dest))
        doc.close()
        logger.info("Rendered PDF page %d for arXiv:%s → %s", page_number, storage.arxiv_id, dest.name)
        return dest
    except Exception as exc:
        logger.error("Failed to render PDF page for arXiv:%s: %s", storage.arxiv_id, exc)
        return None


def extract_main_figure(
    storage: PaperStorage,
    llm_figure_info: dict,
) -> Path | None:
    """High-level wrapper: choose HTML or PDF extraction based on availability.

    llm_figure_info dict (from LLM extraction) may contain:
      - "img_src": str        (HTML src attribute of the figure image)
      - "page_number": int    (0-indexed PDF page, for PDF-only papers)
      - "clip_rect": [x0,y0,x1,y1]  (optional crop rectangle)
    """
    has_html = storage.html_index_path.exists()
    img_src = llm_figure_info.get("img_src")
    page_num = llm_figure_info.get("page_number")

    if has_html and img_src:
        result = extract_from_html(storage, img_src)
        if result is not None:
            return result

    if storage.pdf_path.exists() and page_num is not None:
        clip = llm_figure_info.get("clip_rect")
        return extract_from_pdf(storage, page_num, clip_rect=tuple(clip) if clip else None)

    logger.warning("Could not extract main figure for arXiv:%s — insufficient info", storage.arxiv_id)
    return None


def _ext_from_content_type(ct: str) -> str:
    ct = ct.lower().split(";")[0].strip()
    mapping = {
        "image/png": ".png",
        "image/jpeg": ".jpg",
        "image/gif": ".gif",
        "image/svg+xml": ".svg",
        "image/webp": ".webp",
    }
    return mapping.get(ct, "")
