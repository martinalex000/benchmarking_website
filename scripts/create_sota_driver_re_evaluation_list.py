#!/usr/bin/env python3
"""Create a queue list from the source-audited SOTA concentration report.

The report deliberately keeps one row per dataset/driver/model. Re-evaluation
is paper-scoped, so this command extracts and de-duplicates every arXiv ID in
the audited-driver section before handing the list to
``mark_reextract_papers.py``.
"""

from __future__ import annotations

import argparse
import re
from datetime import UTC, datetime
from pathlib import Path

_ARXIV_ID = re.compile(r"(?<!\d)(\d{4}\.\d{4,5})(?!\d)")
_DRIVER_SECTION = "## Source-audited driver rows"
_END_SECTION = "## Confirmed and high-priority findings"
_DEFAULT_REPORT = Path("experiments/dataset_sota_concentration_audit.md")
_DEFAULT_OUTPUT = Path("config/re_evaluate_sota_drivers.txt")


def driver_paper_ids(report: Path) -> list[str]:
    text = report.read_text(encoding="utf-8")
    if _DRIVER_SECTION not in text or _END_SECTION not in text:
        raise ValueError(f"Report does not contain the expected driver section: {report}")
    section = text.split(_DRIVER_SECTION, 1)[1].split(_END_SECTION, 1)[0]
    return sorted(set(_ARXIV_ID.findall(section)))


def write_list(report: Path, output: Path) -> int:
    ids = driver_paper_ids(report)
    generated_at = datetime.now(UTC).isoformat()
    lines = [
        "# Papers from the dataset SOTA concentration source audit.",
        f"# Source: {report}",
        "# Mark with: uv run python scripts/mark_reextract_papers.py mark-list "
        f"--file {output} --yes --requeue --reason dataset_sota_concentration_audit",
        f"# Generated at: {generated_at}",
        "",
        *ids,
        "",
    ]
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8")
    return len(ids)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, default=_DEFAULT_REPORT)
    parser.add_argument("--output", type=Path, default=_DEFAULT_OUTPUT)
    args = parser.parse_args()
    count = write_list(args.report, args.output)
    print(f"Wrote {count} unique driver paper ID(s) to {args.output}")


if __name__ == "__main__":
    main()
