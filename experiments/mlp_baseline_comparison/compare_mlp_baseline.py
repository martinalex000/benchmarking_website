#!/usr/bin/env python3
"""Regenerate the MLP comparison data and figures in this directory."""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from backend.mlp_comparison import (  # noqa: E402
    compare_results,
    load_comparison_results,
    write_comparison_figures,
    write_comparison_outputs,
)


def main() -> None:
    output_dir = Path(__file__).resolve().parent
    comparisons = compare_results(load_comparison_results())
    outputs = write_comparison_outputs(comparisons, output_dir)
    figures = write_comparison_figures(comparisons, output_dir)
    print(f"Eligible datasets: {len(comparisons)}")
    for path in (*outputs, *figures):
        print(path)


if __name__ == "__main__":
    main()
