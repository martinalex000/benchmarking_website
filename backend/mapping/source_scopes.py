"""Source-scope helpers staged for the next frozen mapping revision.

The active validation keeps its original guards. These helpers separate actual
competing cells from unit repairs and avoid borrowing uncertainty from earlier tables.
"""

from __future__ import annotations

import re

from backend.mapping.source import active_source_lines, name_key, printed_matches, printed_numbers
from backend.repetition_metadata import table_inventory


def uncertainty_context(source: str, table: dict) -> tuple[str, int]:
    lines = active_source_lines(source)
    before = max(0, table["start_line"] - 31)
    previous = [
        t["end_line"]
        for t in table_inventory(source)
        if t["end_line"] < table["start_line"]
        and re.search(
            r"\\begin\{(?:table\*?|wraptable|longtable|sidewaystable\*?)\}",
            lines[t["start_line"] - 1],
        )
    ]
    if previous:
        before = max(before, max(previous))
    headings = [
        number
        for number in range(before, table["start_line"] - 1)
        if re.search(r"\\(?:section|subsection|subsubsection)\*?\s*\{", lines[number])
    ]
    if headings:
        before = max(before, headings[-1])
    return "\n".join(lines[before : table["end_line"]]), before + 1


def competing_old_value_lines(row: dict, source: str, table: dict) -> list[int]:
    candidate = row["selected_candidate"]
    column = candidate.get("cell_column_index")
    if column is None or row.get("std") is None:
        return []
    selected_line = candidate["cell_evidence"]["start_line"]
    lines = active_source_lines(source)
    conflicts = []

    def matches(cell):
        return any(
            all(
                printed_matches(value * scale, value, scale, cell)
                for value in (row["value"], row["std"])
            )
            for scale in (1, 100)
        )

    for number in range(table["start_line"], table["end_line"] + 1):
        cells = re.split(r"(?<!\\)&", lines[number - 1])
        if number == selected_line:
            if (
                cells
                and name_key(row["dataset"]) in name_key(cells[0])
                and any(matches(cell) for index, cell in enumerate(cells[1:], 1) if index != column)
            ):
                conflicts.append(number)
            # The selected physical cell matching the old *literal* units is a
            # possible scale repair, not evidence of a second configuration.
            continue
        if (
            len(cells) > column
            and name_key(row["model"]) in name_key(cells[0])
            and matches(cells[column])
        ):
            conflicts.append(number)
    return conflicts


def fractional_percentage_column_lines(source: str, table: dict, column: int) -> list[int]:
    """Flag conflicting unit cues for review, never choose units from score magnitude.

    A percentage caption plus several exclusively fractional mean/std cells can
    indicate a caption error. Genuine sub-one-percent results are also possible,
    so this is feedback for source review, not permission to rescale automatically.
    Only the selected physical column participates; other metrics cannot vote.
    """
    if column < 1 or not re.search(r"\\%|\(%\)|percent(?:age)?", table["caption"], re.I):
        return []
    lines = active_source_lines(source)
    fractional = []
    for number in range(table["start_line"], table["end_line"] + 1):
        cells = re.split(r"(?<!\\)&", lines[number - 1])
        if len(cells) <= column or not cells[0].strip():
            continue
        cell = cells[column]
        if not re.search(r"\\pm|±", cell):
            continue
        numbers = printed_numbers(cell)
        # Footnotes, sample sizes, ranges, and malformed cells require their own
        # interpretation; do not turn those numbers into a unit vote.
        if len(numbers) != 2:
            continue
        mean, std = map(float, numbers)
        if not 0 <= mean <= 1 or not 0 <= std <= 1:
            return []
        fractional.append(number)
    return fractional if len(fractional) >= 3 else []


def uncertainty_review_hints(source: str, table: dict, protocol_evidence: list[dict]) -> list[dict]:
    """Locate explicit non-std cues for verification, not automatic conversion.

    A global experimental setup can apply across subsection boundaries. Include
    protocol evidence supplied for this cell as well as the bounded local context;
    the independent verifier still has to establish scope and resolve conflicts.
    """
    context, first = uncertainty_context(source, table)
    selected = {first + offset for offset, _ in enumerate(context.splitlines())}
    lines = active_source_lines(source)
    for span in protocol_evidence:
        start, end = span.get("start_line"), span.get("end_line")
        if type(start) is int and type(end) is int and 1 <= start <= end <= len(lines):
            selected.update(range(start, end + 1))
    patterns = {
        "standard_error": r"\bstandard\s+errors?\b",
        "confidence_interval": r"\b(?:confidence|credible)\s+intervals?\b",
        "variance": r"\bmean\s+and\s+variance\b",
    }
    return [
        {"kind": kind, "start_line": number, "end_line": number, "requires_scope_review": True}
        for number in sorted(selected)
        for kind, pattern in patterns.items()
        if re.search(pattern, lines[number - 1], re.I)
    ]
