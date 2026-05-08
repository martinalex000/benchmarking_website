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
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

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


def main() -> None:
    parser = argparse.ArgumentParser(description="Populate dataset statistics in the DB")
    parser.add_argument("--export", action="store_true", help="Re-export Hugo content after update")
    args = parser.parse_args()

    init_db()
    updated: list[str] = []
    with session_scope() as session:
        for ds in session.query(Dataset).all():
            if ds.name in STATS:
                num_graphs, avg_nodes, avg_edges, num_classes, _ = STATS[ds.name]
                ds.num_graphs = num_graphs
                ds.avg_nodes = avg_nodes
                ds.avg_edges = avg_edges
                ds.num_classes = num_classes
                updated.append(ds.name)

    print(f"Updated stats for: {', '.join(updated)}")

    if args.export:
        from backend.export_to_hugo import export_all

        export_all()
        print("Re-exported Hugo content.")


if __name__ == "__main__":
    main()
