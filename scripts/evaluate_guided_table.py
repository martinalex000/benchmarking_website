"""Evaluate guided-table outputs against a reviewed paper manifest.

The manifest is intentionally external to the extraction code so an agent can
refresh the reviewed corpus without changing parser behavior.

Usage::

    uv run python scripts/evaluate_guided_table.py --manifest config/guided_table_evaluation.yaml
"""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
from typing import Any

import yaml

from backend.paper_storage import PaperStorage


def _load_manifest(path: Path) -> list[dict[str, Any]]:
    payload = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    papers = payload.get("papers", []) if isinstance(payload, dict) else []
    if not isinstance(papers, list):
        raise ValueError("Manifest 'papers' must be a list")
    return [item for item in papers if isinstance(item, dict)]


def _output_for(arxiv_id: str) -> dict[str, Any]:
    return PaperStorage(arxiv_id).load_llm_output()


def evaluate(manifest_path: Path, *, min_papers: int = 30, min_entries: int = 20) -> int:
    papers = _load_manifest(manifest_path)
    if len(papers) < min_papers:
        raise ValueError(
            f"Manifest contains {len(papers)} papers; at least {min_papers} are required"
        )

    status_counts: Counter[str] = Counter()
    total_results = 0
    for item in papers:
        arxiv_id = str(item.get("arxiv_id", "")).strip()
        expected = int(item.get("minimum_results", min_entries))
        output = _output_for(arxiv_id)
        results = (output.get("results") or {}).get("results") or []
        actual = len(results)
        strategy = (output.get("experiment") or {}).get("strategy", "missing")
        status = "ok" if strategy == "guided-table" and actual >= expected else "review"
        status_counts[status] += 1
        total_results += actual
        print(
            f"{arxiv_id:>14} {status:>6} strategy={strategy:<13} results={actual:>4} expected>={expected}"
        )

    print(f"papers={len(papers)} total_results={total_results} statuses={dict(status_counts)}")
    return 0 if status_counts["review"] == 0 else 1


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--min-papers", type=int, default=30)
    parser.add_argument("--min-entries", type=int, default=20)
    args = parser.parse_args()
    raise SystemExit(
        evaluate(args.manifest, min_papers=args.min_papers, min_entries=args.min_entries)
    )


if __name__ == "__main__":
    main()
