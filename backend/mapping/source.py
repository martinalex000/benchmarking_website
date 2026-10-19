from __future__ import annotations

import math
import re
import sqlite3

from backend.mapping.schema import (
    Span,
)
from backend.repetition_storage import name_key as name_key


def method_key(name: str) -> str:
    """Normalize spelling without merging modified or rerun method identities."""
    return re.sub(r"[^a-z0-9+*]", "", name.casefold())


def evidence_text(spans: list[Span], source: str) -> str:
    lines = source.splitlines()
    if not spans or any(not 1 <= s.start_line <= s.end_line <= len(lines) for s in spans):
        return ""
    return "\n".join("\n".join(lines[s.start_line - 1 : s.end_line]) for s in spans)


def printed_numbers(text: str) -> list[str]:
    # Formatting arguments are not visible scores (e.g. HTML color 000000).
    text = re.sub(
        r"\\(?:color|cellcolor|rowcolor|columncolor)(?:\[[^\]]*\])?\{[^{}]*\}",
        " ",
        text,
    )
    text = re.sub(
        r"\\(?:multirow|multicolumn|fontsize|rule)(?:\[[^\]]*\])?\{[^{}]*\}\{[^{}]*\}",
        " ",
        text,
    )
    text = re.sub(r"\\[A-Za-z]+", " ", text)
    # Means often have a trailing LaTeX uncertainty subscript: 55.69_{\\pm 5.74}.
    return re.findall(r"(?<![\w.])-?\d+(?:\.\d+)?(?![^\W_]|[.])", text)


def printed_matches(displayed: float | None, stored: float | None, divisor: int, text: str) -> bool:
    if stored is None:
        return True  # Missing stored std is not proof that the source has no std.
    if displayed is None:
        return False
    for number in printed_numbers(text):
        if not math.isclose(float(number), displayed, rel_tol=0, abs_tol=1e-10):
            continue
        decimals = len(number.split(".")[1]) if "." in number else 0
        if abs(displayed / divisor - stored) <= 0.5 * 10 ** (-decimals) / divisor + 1e-10:
            return True
    return False


def earlier_matches(db: sqlite3.Connection, pid: str, rows: list[dict]) -> list[dict]:
    """Exact earlier DB coincidences are hints, not verified copying evidence."""
    target = db.execute("SELECT published_date FROM papers WHERE arxiv_id=?", (pid,)).fetchone()
    if not target or not target[0]:
        return []
    hints = []
    for row in rows:
        matches = db.execute(
            "SELECT p.arxiv_id,p.title,p.published_date,r.id,coalesce(r.model_name_override,m.name),"
            "r.metric_value,r.metric_std,v.name FROM results r "
            "JOIN papers p ON p.id=r.paper_id JOIN models m ON m.id=r.model_id "
            "JOIN dataset_variants v ON v.id=r.dataset_variant_id "
            "JOIN datasets d ON d.id=v.dataset_id "
            "WHERE p.published_date < ? AND p.arxiv_id != ? AND d.name=? "
            "AND lower(r.metric_name)=lower(?) AND abs(r.metric_value-?)<1e-8 "
            "ORDER BY p.published_date,r.id",
            (target[0], pid, row["dataset"], row["metric"], row["value"]),
        ).fetchall()
        filtered = [m for m in matches if method_key(m[4]) == method_key(row["model"])]
        if filtered:
            hints.append(
                {
                    "result_id": row["result_id"],
                    "warning": "Earlier database coincidence, NOT verified source or proof of copying",
                    "matches": [
                        {
                            "arxiv_id": m[0],
                            "title": m[1],
                            "published_date": m[2],
                            "result_id": m[3],
                            "model": m[4],
                            "value": m[5],
                            "std": m[6],
                            "variant": m[7],
                            "pdf": f"https://arxiv.org/pdf/{m[0]}",
                        }
                        for m in filtered[:5]
                    ],
                }
            )
    return hints


def compact_protocols(metadata: dict) -> list[dict]:
    accepted = {(x["table_id"], x["name"]) for x in metadata["validated"].get("accepted", [])}
    verdicts = {(x["table_id"], x["name"]): x for x in metadata["verification"]["methods"]}
    return [
        {
            "table_id": table["table_id"],
            "table_role": table["role"],
            "method": method,
            "previous_verdict": verdicts.get((table["table_id"], method["name"])),
            "previous_count_accepted": (table["table_id"], method["name"]) in accepted,
        }
        for table in metadata["facts"]["tables"]
        for method in table["methods"]
    ]


def active_source_lines(source: str) -> list[str]:
    """Drop unescaped LaTeX comments without changing source line numbering."""
    lines = []
    for line in source.splitlines():
        for index, character in enumerate(line):
            if character != "%":
                continue
            slashes = len(line[:index]) - len(line[:index].rstrip("\\"))
            if slashes % 2 == 0:
                line = line[:index]
                break
        lines.append(line)
    return lines
