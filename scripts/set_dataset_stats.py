#!/usr/bin/env python3
"""Set dataset statistics in the database.

Stats for LRGB datasets sourced from:
https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.LRGBDataset.html

Usage::
    uv run python scripts/set_dataset_stats.py
    uv run python scripts/set_dataset_stats.py --export   # also re-export Hugo content
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import requests
from bs4 import BeautifulSoup

sys.path.insert(0, str(Path(__file__).parent.parent))

from backend.dataset_stats_parsing import header_role, parse_number
from backend.db import init_db, session_scope
from backend.models import Dataset

# Dataset name → (num_graphs, avg_nodes, avg_edges, num_classes, source_url)
# Columns from PyG STATS table: #Graphs | Avg. #Nodes | Avg. #Edges | Output Dim
STATS: dict[str, tuple] = {
    "PascalVOC-SP": (
        11_355,
        479.40,
        2710.48,
        21,
        "https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.LRGBDataset.html",
    ),
    "COCO-SP": (
        123_286,
        476.88,
        2693.67,
        81,
        "https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.LRGBDataset.html",
    ),
    "PCQM-Contact": (
        529_434,
        30.14,
        61.09,
        1,
        "https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.LRGBDataset.html",
    ),
    "Peptides-func": (
        15_535,
        150.94,
        307.30,
        10,
        "https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.LRGBDataset.html",
    ),
    "Peptides-struct": (
        15_535,
        150.94,
        307.30,
        11,
        "https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.LRGBDataset.html",
    ),
}


def _norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", (text or "").strip().lower())


def _match_dataset_row(dataset_name: str, rows: list[dict]) -> dict | None:
    if not rows:
        return None

    wanted = _norm(dataset_name)

    # Try exact/substring match against dataset/name column first.
    candidates: list[dict] = []
    for row in rows:
        ds_col = row.get("dataset")
        if not ds_col:
            continue
        got = _norm(ds_col)
        if got == wanted or wanted in got or got in wanted:
            candidates.append(row)
    if candidates:
        # Prefer the shortest matching dataset token (usually most specific row).
        candidates.sort(key=lambda r: len(str(r.get("dataset", ""))))
        return candidates[0]

    # If table has only one data row and no dataset column, treat it as dataset-specific page.
    if len(rows) == 1:
        return rows[0]

    return None


def _extract_rows_from_table(table) -> list[dict]:
    rows: list[dict] = []
    hdr_cells = table.select("thead tr th")
    if not hdr_cells:
        # Some docs pages place headers in first tbody row.
        first = table.select_one("tr")
        hdr_cells = first.select("th, td") if first else []
    headers = [c.get_text(" ", strip=True) for c in hdr_cells]
    roles = [header_role(h) for h in headers]
    if not any(r in {"num_graphs", "avg_nodes", "avg_edges", "num_classes"} for r in roles):
        return rows

    for tr in table.select("tbody tr"):
        cells = tr.select("td, th")
        if not cells:
            continue
        row: dict = {}
        for i, cell in enumerate(cells):
            if i >= len(roles):
                break
            role = roles[i]
            if role is None:
                continue
            txt = cell.get_text(" ", strip=True)
            if role == "dataset":
                row["dataset"] = txt
            else:
                row[role] = parse_number(txt)
        rows.append(row)
    return rows


def _fetch_stats_from_pyg(dataset_name: str, pyg_url: str) -> dict | None:
    if not pyg_url:
        return None
    try:
        resp = requests.get(pyg_url, timeout=15)
        resp.raise_for_status()
    except Exception:
        return None

    soup = BeautifulSoup(resp.text, "lxml")
    tables = soup.select("table")
    all_rows: list[dict] = []
    for table in tables:
        all_rows.extend(_extract_rows_from_table(table))

    match = _match_dataset_row(dataset_name, all_rows)
    if not match:
        return None

    result = {
        "num_graphs": match.get("num_graphs"),
        "avg_nodes": match.get("avg_nodes"),
        "avg_edges": match.get("avg_edges"),
        "num_classes": match.get("num_classes"),
    }
    if any(v is not None for v in result.values()):
        return result
    return None


def main() -> None:
    parser = argparse.ArgumentParser(description="Populate dataset statistics in the DB")
    parser.add_argument("--export", action="store_true", help="Re-export Hugo content after update")
    parser.add_argument(
        "--pyg",
        action="store_true",
        help="Also fetch missing stats from each dataset's PyG documentation URL",
    )
    args = parser.parse_args()

    init_db()
    updated: list[str] = []
    updated_from_pyg: list[str] = []
    with session_scope() as session:
        for ds in session.query(Dataset).all():
            if ds.name in STATS:
                num_graphs, avg_nodes, avg_edges, num_classes, _ = STATS[ds.name]
                ds.num_graphs = num_graphs
                ds.avg_nodes = avg_nodes
                ds.avg_edges = avg_edges
                ds.num_classes = num_classes
                updated.append(ds.name)

        if args.pyg:
            for ds in session.query(Dataset).all():
                needs_stats = any(
                    x is None for x in [ds.num_graphs, ds.avg_nodes, ds.avg_edges, ds.num_classes]
                )
                if not needs_stats or not ds.pyg_url:
                    continue
                found = _fetch_stats_from_pyg(ds.name, ds.pyg_url)
                if not found:
                    continue

                if ds.num_graphs is None and found.get("num_graphs") is not None:
                    ds.num_graphs = int(found["num_graphs"])
                if ds.avg_nodes is None and found.get("avg_nodes") is not None:
                    ds.avg_nodes = float(found["avg_nodes"])
                if ds.avg_edges is None and found.get("avg_edges") is not None:
                    ds.avg_edges = float(found["avg_edges"])
                if ds.num_classes is None and found.get("num_classes") is not None:
                    ds.num_classes = int(found["num_classes"])
                updated_from_pyg.append(ds.name)

    print(f"Updated stats for: {', '.join(updated)}")
    if args.pyg:
        print(f"Updated from PyG docs: {', '.join(sorted(set(updated_from_pyg)))}")

    if args.export:
        from backend.export_to_hugo import export_all

        export_all()
        print("Re-exported Hugo content.")


if __name__ == "__main__":
    main()
