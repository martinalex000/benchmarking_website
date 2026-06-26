#!/usr/bin/env uv run python3
"""Merge all OGB arxiv ID JSON fragments into config/arxiv_ids.csv and config/arxiv_ids.txt."""
import csv
import json
from pathlib import Path

CONFIG = Path(__file__).parent.parent / "config"

SOURCES = [
    CONFIG / "arxiv_ids_corrected.json",
    CONFIG / "arxiv_ids_ogbn_products_proteins.json",
    CONFIG / "arxiv_ids_ogbn_arxiv_mag.json",
    CONFIG / "arxiv_ids_ogbl.json",
]

OUTPUT_CSV = CONFIG / "arxiv_ids.csv"
OUTPUT_TXT = CONFIG / "arxiv_ids.txt"
OUTPUT_MISSING = CONFIG / "papers_missing_arxiv.txt"


def load_source(path: Path) -> tuple[dict, list]:
    if not path.exists():
        return {}, []
    data = json.loads(path.read_text())
    if "methods" in data:
        methods = data["methods"]
        missing = data.get("missing", [])
    else:
        methods = {}
        missing = []
        for k, v in data.items():
            if isinstance(v, dict) and "arxiv_id" in v:
                methods[k] = v
            elif k == "missing":
                missing = v if isinstance(v, list) else []
    return methods, missing


def main():
    all_methods: dict[str, dict] = {}
    all_missing: list[dict] = []

    for src in SOURCES:
        methods, missing = load_source(src)
        for name, info in methods.items():
            arxiv = (info.get("arxiv_id") or "").strip()
            if arxiv:
                all_methods[name] = {
                    "arxiv_id": arxiv,
                    "title": info.get("title", ""),
                    "year": info.get("year", ""),
                }
        all_missing.extend(missing if isinstance(missing, list) else [])

    # Write CSV
    with OUTPUT_CSV.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["method", "arxiv_id", "title", "year"])
        for name in sorted(all_methods):
            info = all_methods[name]
            title = str(info.get("title", "")).replace('"', "'")
            w.writerow([name, info["arxiv_id"], title, info.get("year", "")])

    # Write unique arxiv IDs, one per line
    unique_ids = sorted({m["arxiv_id"] for m in all_methods.values() if m["arxiv_id"]})
    OUTPUT_TXT.write_text("\n".join(unique_ids) + "\n")

    print(f"Methods with arxiv: {len(all_methods)}")
    print(f"Unique arxiv IDs: {len(unique_ids)}")
    print(f"Missing entries: {len(all_missing)}")
    print(f"Wrote {OUTPUT_CSV}")
    print(f"Wrote {OUTPUT_TXT}")


if __name__ == "__main__":
    main()
