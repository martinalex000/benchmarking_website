"""Summarize the global guided-table JSONL diagnostics for agent review."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

from backend.config import cfg


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--path", type=Path, default=cfg.logs_dir / "guided_table_errors.jsonl")
    args = parser.parse_args()
    counts: Counter[str] = Counter()
    papers: Counter[str] = Counter()
    if not args.path.exists():
        print("No guided-table diagnostics found.")
        return
    for line in args.path.read_text(encoding="utf-8").splitlines():
        try:
            item = json.loads(line)
        except json.JSONDecodeError:
            counts["invalid_json"] += 1
            continue
        counts[str(item.get("kind", "unknown"))] += 1
        papers[str(item.get("arxiv_id", "unknown"))] += 1
    print("Error categories:")
    for kind, count in counts.most_common():
        print(f"  {kind}: {count}")
    print("Papers with diagnostics:")
    for arxiv_id, count in papers.most_common():
        print(f"  {arxiv_id}: {count}")


if __name__ == "__main__":
    main()
