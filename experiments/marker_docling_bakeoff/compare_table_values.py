#!/usr/bin/env python3
"""Compare numeric table content from PDF-to-Markdown output with local LaTeX.

This is a cheap, deterministic pre-screen for PDF converters. It does not claim
semantic equivalence: configurations that pass should still be compared through
the normal benchmark extraction and manually audited before ingestion.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from backend.guided_table import _latex_rows  # noqa: E402
from backend.latex_source import _parse_expanded  # noqa: E402

_MARKDOWN_SEPARATOR_RE = re.compile(
    r"^\s*\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)+\|?\s*$"
)
_NUMBER_RE = re.compile(
    r"(?<![\w.])[-+]?(?:\d{1,3}(?:,\d{3})+|\d+|\.\d+)(?:\.\d+)?(?:[eE][-+]?\d+)?%?"
)


@dataclass(frozen=True)
class TableValueStats:
    reference_tables: int
    candidate_tables: int
    reference_values: int
    candidate_values: int
    matched_values: int

    @property
    def recall(self) -> float:
        return self.matched_values / self.reference_values if self.reference_values else 1.0

    @property
    def precision(self) -> float:
        return self.matched_values / self.candidate_values if self.candidate_values else 1.0


def _normalize_number(raw: str) -> str | None:
    text = raw.replace(",", "")
    is_percent = text.endswith("%")
    if is_percent:
        text = text[:-1]
    try:
        value = Decimal(text)
    except InvalidOperation:
        return None
    normalized = format(value.normalize(), "f")
    if normalized == "-0":
        normalized = "0"
    return f"{normalized}%" if is_percent else normalized


def _numbers(text: str) -> Counter[str]:
    values: Counter[str] = Counter()
    for match in _NUMBER_RE.finditer(text):
        normalized = _normalize_number(match.group())
        if normalized is not None:
            values[normalized] += 1
    return values


def latex_table_values(arxiv_id: str, expanded_tex: Path) -> tuple[int, Counter[str]]:
    paper = _parse_expanded(arxiv_id, expanded_tex.read_text(encoding="utf-8", errors="replace"))
    values: Counter[str] = Counter()
    parsed_tables = 0
    for table in paper.tables:
        rows = _latex_rows(table.body)
        if not rows:
            continue
        parsed_tables += 1
        for row in rows:
            for cell in row:
                values.update(_numbers(cell))
    return parsed_tables, values


def markdown_tables(markdown: str) -> list[list[str]]:
    """Return pipe-table blocks containing a Markdown separator row."""
    blocks: list[list[str]] = []
    current: list[str] = []
    for line in [*markdown.splitlines(), ""]:
        if "|" in line and line.strip():
            current.append(line)
            continue
        if current and any(_MARKDOWN_SEPARATOR_RE.match(row) for row in current):
            blocks.append(current)
        current = []
    return blocks


def compare(arxiv_id: str, expanded_tex: Path, markdown_path: Path) -> TableValueStats:
    reference_tables, reference_values = latex_table_values(arxiv_id, expanded_tex)
    candidate_tables = markdown_tables(markdown_path.read_text(encoding="utf-8", errors="replace"))
    candidate_values: Counter[str] = Counter()
    for table in candidate_tables:
        candidate_values.update(_numbers("\n".join(table)))
    matched = reference_values & candidate_values
    return TableValueStats(
        reference_tables=reference_tables,
        candidate_tables=len(candidate_tables),
        reference_values=reference_values.total(),
        candidate_values=candidate_values.total(),
        matched_values=matched.total(),
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("arxiv_id")
    parser.add_argument("markdown", type=Path)
    parser.add_argument("--papers-dir", type=Path, default=Path("papers"))
    args = parser.parse_args()

    expanded_tex = args.papers_dir / args.arxiv_id / "latex" / "expanded.tex"
    stats = compare(args.arxiv_id, expanded_tex, args.markdown)
    print(
        f"{args.arxiv_id}: tables={stats.candidate_tables}/{stats.reference_tables} "
        f"values={stats.matched_values}/{stats.reference_values} "
        f"recall={stats.recall:.1%} precision={stats.precision:.1%} "
        f"candidate_values={stats.candidate_values}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
