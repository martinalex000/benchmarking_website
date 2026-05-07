"""HTML paper parser — extracts text, tables (as Markdown), and figure info from arXiv HTML.

ArXiv HTML papers (ar5iv format) have well-structured HTML with identifiable
sections, figure captions, and result tables.
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from pathlib import Path

from bs4 import BeautifulSoup, Tag

logger = logging.getLogger(__name__)

# ── Data classes ──────────────────────────────────────────────────────────────


@dataclass
class ParsedTable:
    caption: str
    markdown: str
    element_id: str | None = None
    section: str | None = None


@dataclass
class ParsedFigure:
    caption: str
    src: str | None = None  # relative src of the <img>
    element_id: str | None = None
    section: str | None = None


@dataclass
class ParsedPaper:
    title: str = ""
    abstract: str = ""
    sections: list[tuple[str, str]] = field(default_factory=list)  # (heading, text)
    tables: list[ParsedTable] = field(default_factory=list)
    figures: list[ParsedFigure] = field(default_factory=list)
    references: list[str] = field(default_factory=list)
    full_text: str = ""


# ── Helpers ───────────────────────────────────────────────────────────────────


def _tag_text(tag: Tag) -> str:
    return tag.get_text(separator=" ", strip=True)


def _table_to_markdown(table_tag: Tag) -> str:
    """Convert an HTML <table> to a Markdown table string."""
    rows: list[list[str]] = []
    for tr in table_tag.find_all("tr"):
        cells = []
        for cell in tr.find_all(["th", "td"]):
            text = cell.get_text(separator=" ", strip=True)
            # Collapse internal whitespace
            text = re.sub(r"\s+", " ", text).replace("|", "\\|")
            colspan = int(cell.get("colspan", 1))
            cells.extend([text] + [""] * (colspan - 1))
        if cells:
            rows.append(cells)

    if not rows:
        return ""

    # Normalise column count
    ncols = max(len(r) for r in rows)
    rows = [r + [""] * (ncols - len(r)) for r in rows]

    lines = []
    for i, row in enumerate(rows):
        lines.append("| " + " | ".join(row) + " |")
        if i == 0:
            lines.append("| " + " | ".join(["---"] * ncols) + " |")

    return "\n".join(lines)


# ── Main parser ───────────────────────────────────────────────────────────────


def parse_html_paper(html_path: Path) -> ParsedPaper:
    """Parse an arXiv HTML paper and return a structured ParsedPaper."""
    raw = html_path.read_text(encoding="utf-8", errors="replace")
    soup = BeautifulSoup(raw, "lxml")
    result = ParsedPaper()

    # Title
    title_tag = soup.find("title") or soup.find("h1", class_=re.compile(r"title", re.I))
    if title_tag:
        result.title = _tag_text(title_tag)

    # Abstract
    abstract_tag = (
        soup.find("div", id=re.compile(r"abstract", re.I))
        or soup.find("blockquote", class_=re.compile(r"abstract", re.I))
        or soup.find("section", id=re.compile(r"abstract", re.I))
    )
    if abstract_tag:
        result.abstract = _tag_text(abstract_tag)

    # Sections — look for <section> or heading-based structure
    current_section = "Introduction"
    section_texts: dict[str, list[str]] = {}
    text_blocks: list[str] = []

    for tag in soup.find_all(["h1", "h2", "h3", "h4", "section", "p", "table", "figure"]):
        if tag.name in ("h1", "h2", "h3", "h4"):
            current_section = _tag_text(tag)
        elif tag.name == "p":
            text = _tag_text(tag)
            if text:
                section_texts.setdefault(current_section, []).append(text)
                text_blocks.append(text)

    result.sections = [
        (heading, "\n".join(paragraphs)) for heading, paragraphs in section_texts.items()
    ]

    # Tables
    for table in soup.find_all("table"):
        cap_tag = table.find_previous_sibling("caption") or table.find("caption")
        if cap_tag is None:
            # Look for a nearby figcaption or p.caption
            parent = table.parent
            cap_tag = parent.find("figcaption") if parent else None
        caption = _tag_text(cap_tag) if cap_tag else ""
        md = _table_to_markdown(table)
        if md:
            # Guess enclosing section
            sec = _find_enclosing_section(table, soup)
            result.tables.append(
                ParsedTable(
                    caption=caption,
                    markdown=md,
                    element_id=table.get("id"),
                    section=sec,
                )
            )

    # Figures
    for fig in soup.find_all("figure"):
        cap_tag = fig.find("figcaption")
        caption = _tag_text(cap_tag) if cap_tag else ""
        img_tag = fig.find("img")
        src = img_tag.get("src") if img_tag else None
        sec = _find_enclosing_section(fig, soup)
        result.figures.append(
            ParsedFigure(
                caption=caption,
                src=src,
                element_id=fig.get("id"),
                section=sec,
            )
        )

    # Full text (flat, for LLM ingestion)
    body = soup.find("body") or soup
    full = body.get_text(separator="\n", strip=True)
    # Collapse excessive blank lines
    result.full_text = re.sub(r"\n{3,}", "\n\n", full)

    # References (just text, for completeness)
    ref_section = soup.find(id=re.compile(r"references?", re.I)) or soup.find(
        "section", string=re.compile(r"references?", re.I)
    )
    if ref_section:
        for li in ref_section.find_all("li"):
            ref_text = _tag_text(li)
            if ref_text:
                result.references.append(ref_text)

    return result


def _find_enclosing_section(tag: Tag, _soup: BeautifulSoup) -> str | None:
    """Walk up the DOM to find the nearest section heading."""
    parent = tag.parent
    while parent and parent.name not in ("html", "[document]"):
        heading = parent.find(re.compile(r"^h[1-4]$"))
        if heading:
            return _tag_text(heading)
        parent = parent.parent
    return None


def save_text(paper: ParsedPaper, dest: Path) -> None:
    """Write structured plain text to dest (used as LLM input)."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    lines = []
    if paper.title:
        lines += [f"# {paper.title}", ""]
    if paper.abstract:
        lines += ["## Abstract", paper.abstract, ""]

    for heading, text in paper.sections:
        lines += [f"## {heading}", text, ""]

    if paper.tables:
        lines += ["## Tables", ""]
        for i, tbl in enumerate(paper.tables, 1):
            lines += [f"### Table {i}: {tbl.caption}", tbl.markdown, ""]

    if paper.figures:
        lines += ["## Figures", ""]
        for i, fig in enumerate(paper.figures, 1):
            lines += [f"### Figure {i}: {fig.caption}", ""]

    dest.write_text("\n".join(lines), encoding="utf-8")
