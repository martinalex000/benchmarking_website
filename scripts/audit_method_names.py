#!/usr/bin/env python3
"""List papers whose extracted method names deserve manual review."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from backend.method_name_audit import audit_method_names


def _format_names(names: list[str], limit: int = 4) -> str:
    if not names:
        return "-"
    display = names[:limit]
    suffix = "" if len(names) <= limit else f" (+{len(names) - limit} more)"
    return ", ".join(display) + suffix


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Audit stored extractions for suspicious method names",
    )
    parser.add_argument(
        "--paper",
        "-p",
        nargs="+",
        metavar="ARXIV_ID",
        help="Specific papers to inspect (default: scan all stored papers)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=30,
        help="Maximum number of suspicious papers to print (default: 30)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable JSON instead of a text report",
    )
    args = parser.parse_args(argv)

    findings = audit_method_names(paper_ids=args.paper)
    if args.limit > 0:
        findings = findings[: args.limit]

    if args.json:
        json.dump([item.to_dict() for item in findings], sys.stdout, indent=2, ensure_ascii=False)
        sys.stdout.write("\n")
        return 0

    if not findings:
        print("No suspicious method-name cases found.")
        return 0

    print(f"Suspicious method-name cases: {len(findings)}")
    for finding in findings:
        print()
        print(f"{finding.arxiv_id}  {finding.title}")
        print(f"  Proposed:  {finding.proposed_name or '-'}")
        if finding.suggested_name and finding.suggested_name != finding.proposed_name:
            print(f"  Suggest:   {finding.suggested_name}")
        print(
            f"  Candidates:{' ' if finding.candidate_names else ''}{_format_names(finding.candidate_names)}"
        )
        if finding.suspicious_result_names:
            print(f"  Row names:  {_format_names(finding.suspicious_result_names)}")
        print(f"  Reasons:    {'; '.join(finding.reasons)}")
        print(f"  Overrides:  {'has model_renames' if finding.has_model_renames else 'none'}")
        print(f"  Re-run:     uv run python scripts/run_manual.py {finding.arxiv_id} --force")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
