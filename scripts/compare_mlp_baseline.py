#!/usr/bin/env python3
"""Write descriptive comparisons between eligible node methods and plain MLPs."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from backend.mlp_comparison import (
    compare_results,
    load_comparison_results,
    write_comparison_figures,
    write_comparison_outputs,
)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("experiments/mlp_baseline_comparison"),
    )
    args = parser.parse_args()

    comparisons = compare_results(load_comparison_results())
    paths = write_comparison_outputs(comparisons, args.output_dir)
    figure_paths = write_comparison_figures(comparisons, args.output_dir)
    print(f"Eligible datasets: {len(comparisons)}")
    for path in (*paths, *figure_paths):
        print(path)


if __name__ == "__main__":
    main()
