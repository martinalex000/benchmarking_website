#!/usr/bin/env python3
"""Report research metadata coverage in config/seed_data.yaml."""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
from typing import Any

import yaml

REQUIRED_DETAIL_SECTIONS = (
    "task",
    "data",
    "features",
    "splits_and_evaluation",
    "quirks_and_pitfalls",
)


def audit_dataset(dataset: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    description = str(dataset.get("description") or "").strip()
    details = dataset.get("detailed_description")
    sources = dataset.get("sources")

    if not description:
        issues.append("missing concise description")
    elif len(description) > 280:
        issues.append("concise description exceeds 280 characters")

    if not isinstance(details, dict):
        issues.append("missing detailed description")
    else:
        for section in REQUIRED_DETAIL_SECTIONS:
            if not str(details.get(section) or "").strip():
                issues.append(f"missing detail section: {section}")

    if not isinstance(sources, list) or not sources:
        issues.append("missing sources")
    else:
        for index, source in enumerate(sources, start=1):
            if not isinstance(source, dict):
                issues.append(f"source {index} is not a mapping")
                continue
            if not str(source.get("title") or "").strip():
                issues.append(f"source {index} is missing a title")
            if not (source.get("url") or source.get("arxiv_id")):
                issues.append(f"source {index} is missing a URL or arXiv ID")
    return issues


def load_datasets(path: Path) -> list[tuple[str, dict[str, Any]]]:
    loaded = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return [
        (benchmark["name"], dataset)
        for benchmark in loaded.get("benchmarks", [])
        for dataset in benchmark.get("datasets", [])
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, default=Path("config/seed_data.yaml"))
    parser.add_argument("--strict", action="store_true", help="Fail when any issue is found")
    args = parser.parse_args()

    rows = load_datasets(args.path)
    findings = [(benchmark, dataset["name"], audit_dataset(dataset)) for benchmark, dataset in rows]
    complete = sum(not issues for _, _, issues in findings)
    issue_counts = Counter(issue for _, _, issues in findings for issue in issues)

    print("Dataset metadata research audit")
    print(f"  datasets: {len(rows)}")
    print(f"  complete: {complete}")
    print(f"  incomplete: {len(rows) - complete}")
    if issue_counts:
        print("\nIssue summary")
        for issue, count in issue_counts.most_common():
            print(f"  {count:3}  {issue}")
        print("\nIncomplete datasets")
        for benchmark, name, issues in findings:
            if issues:
                print(f"  [{benchmark}] {name}: {'; '.join(issues)}")

    return 1 if args.strict and complete != len(rows) else 0


if __name__ == "__main__":
    raise SystemExit(main())
