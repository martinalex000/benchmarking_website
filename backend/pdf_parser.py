"""PDF paper parser — extracts text from PDFs using PyMuPDF.

Handles two-column layouts by sorting text blocks by position.
Also extracts embedded raster images (stored temporarily for figure identification).
"""
from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from pathlib import Path

logger = logging.getLogger(__name__)


@dataclass
class ParsedPDFPaper:
    full_text: str = ""
    pages: list[str] = field(default_factory=list)
    image_paths: list[Path] = field(default_factory=list)   # extracted raster images


def parse_pdf_paper(pdf_path: Path, images_dir: Path | None = None) -> ParsedPDFPaper:
    """Parse a PDF and return text + extracted images.

    Two-column layout is handled by splitting each page into left/right halves
    and sorting text blocks accordingly.
    """
    try:
        import fitz  # PyMuPDF
    except ImportError as exc:
        raise RuntimeError("PyMuPDF is not installed. Run: uv add pymupdf") from exc

    result = ParsedPDFPaper()

    doc = fitz.open(str(pdf_path))
    page_texts: list[str] = []

    for page_num, page in enumerate(doc):
        width = page.rect.width
        midpoint = width / 2

        blocks = page.get_text("blocks")  # (x0, y0, x1, y1, text, block_no, block_type)
        # block_type: 0=text, 1=image
        text_blocks = [(b[0], b[1], b[4]) for b in blocks if b[6] == 0 and b[4].strip()]

        # Two-column heuristic: if text blocks span less than 60% of page width on average,
        # assume two-column and sort left column before right column.
        avg_width = (
            sum(b[2] - b[0] for b in [(b[0], b[1], b[2]) for b in blocks if b[6] == 0] or [(0, 0, width)])
            / max(len([b for b in blocks if b[6] == 0]), 1)
        )
        is_two_column = avg_width < (width * 0.55)

        if is_two_column:
            left = sorted(
                [(y, txt) for x, y, txt in text_blocks if x < midpoint],
                key=lambda t: t[0],
            )
            right = sorted(
                [(y, txt) for x, y, txt in text_blocks if x >= midpoint],
                key=lambda t: t[0],
            )
            ordered = [txt for _, txt in left] + [txt for _, txt in right]
        else:
            ordered = [txt for _, _, txt in sorted(text_blocks, key=lambda b: (b[1], b[0]))]

        page_text = "\n".join(ordered)
        page_texts.append(page_text)

        # Extract embedded images
        if images_dir is not None:
            images_dir.mkdir(parents=True, exist_ok=True)
            image_list = page.get_images(full=True)
            for img_idx, img_info in enumerate(image_list):
                xref = img_info[0]
                try:
                    base_image = doc.extract_image(xref)
                    img_bytes = base_image["image"]
                    ext = base_image["ext"]
                    img_path = images_dir / f"page{page_num + 1:03d}_img{img_idx:02d}.{ext}"
                    img_path.write_bytes(img_bytes)
                    result.image_paths.append(img_path)
                except Exception as exc:
                    logger.debug("Could not extract image xref=%d on page %d: %s", xref, page_num + 1, exc)

    doc.close()

    result.pages = page_texts
    full = "\n\n".join(page_texts)
    # Clean up excessive whitespace
    result.full_text = re.sub(r"\n{3,}", "\n\n", full).strip()
    return result


def save_text(paper: ParsedPDFPaper, dest: Path) -> None:
    """Write extracted text to dest."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(paper.full_text, encoding="utf-8")
