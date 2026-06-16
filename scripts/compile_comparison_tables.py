#!/usr/bin/env python3
"""Compile per-dataset comparison tables from compare_models artifacts."""
from __future__ import annotations

import json
from pathlib import Path
from collections import defaultdict


def load_comparison(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def extract_model_name(path: Path) -> str:
    p = path.parent.name
    prefix = "compare-models-"
    if p.startswith(prefix):
        return p[len(prefix):]
    return p


def compile_paper(paper_id: str) -> dict:
    base = Path(f"papers/{paper_id}/extracted/experiments")
    comparisons = {}
    models = []
    for child in sorted(base.iterdir()):
        if not child.is_dir():
            continue
        cmp_path = child / "comparison.json"
        if not cmp_path.exists():
            continue
        model_name = extract_model_name(cmp_path)
        models.append(model_name)
        comparisons[model_name] = load_comparison(cmp_path)

    # Gather all dataset keys (model / dataset / metric)
    all_keys = set()
    for model, data in comparisons.items():
        for entry in data["details"].get("hits", []):
            all_keys.add(entry["key"])
        for entry in data["details"].get("value_errors", []):
            all_keys.add(entry["key"])
        for entry in data["details"].get("misses", []):
            all_keys.add(entry["key"])
        for entry in data["details"].get("hallucinations", []):
            all_keys.add(entry["key"])

    # Group by dataset
    by_dataset = defaultdict(list)
    for key in sorted(all_keys, key=lambda k: (k.split(" / ")[1], k)):
        model, dataset, metric = key.split(" / ")
        by_dataset[dataset].append((model, dataset, metric))

    return comparisons, models, by_dataset


def build_tables(paper_id: str, comparisons: dict, models: list, by_dataset: dict) -> str:
    lines = [f"# {paper_id} — Per-Dataset Model Comparison\n"]
    lines.append(f"**Models evaluated:** {', '.join(models)}\n")
    lines.append("Legend: baseline value in parens if known; "
                 "✓=hit, ✗=miss, H=hllcn, VE=value error\n")

    for dataset in sorted(by_dataset):
        lines.append(f"## Dataset: {dataset}\n")
        rows = defaultdict(dict)  # (model, metric) -> status dict
        for model in models:
            data = comparisons[model]
            for entry in data["details"].get("hits", []):
                m, d, metric = entry["key"].split(" / ")
                if d == dataset:
                    rows[(m, metric)][model] = ("✓", entry["candidate"], entry["baseline"])
            for entry in data["details"].get("value_errors", []):
                m, d, metric = entry["key"].split(" / ")
                if d == dataset:
                    rows[(m, metric)][model] = ("VE", entry["candidate"], entry["baseline"])
            for entry in data["details"].get("misses", []):
                m, d, metric = entry["key"].split(" / ")
                if d == dataset:
                    rows[(m, metric)][model] = ("✗", None, entry["baseline_value"])
            for entry in data["details"].get("hallucinations", []):
                m, d, metric = entry["key"].split(" / ")
                if d == dataset:
                    rows[(m, metric)][model] = ("H", entry["candidate_value"], None)

        # Print table header
        lines.append("| Model | Metric | " + " | ".join(models) + " |")
        lines.append("|" + "|".join(["------"] * (2 + len(models))) + "|")

        for (m_name, metric) in sorted(rows):
            row = [m_name, metric]
            for model in models:
                if model not in rows[(m_name, metric)]:
                    row.append("—")
                else:
                    status, cand, base = rows[(m_name, metric)][model]
                    if status == "✓":
                        cell = f"✓ {cand:.4f}"
                    elif status == "VE":
                        cell = f"VE {cand} (want {base})"
                    elif status == "✗":
                        cell = f"✗ (want {base})"
                    elif status == "H":
                        cell = f"H {cand}"
                    else:
                        cell = status
                    row.append(cell)
            lines.append("| " + " | ".join(row) + " |")
        lines.append("")

    return "\n".join(lines)


def main():
    base = Path(f"{Path(__file__).parent.parent}")
    out = base / "experiments/comparison_tables.md"
    out.parent.mkdir(parents=True, exist_ok=True)

    all_lines = ["# Model Comparison Tables\n"]
    for paper_id in ("2206.08164", "2406.08993"):
        comparisons, models, by_dataset = compile_paper(paper_id)
        all_lines.append(build_tables(paper_id, comparisons, models, by_dataset))
        all_lines.append("\n---\n")

    out.write_text("\n".join(all_lines), encoding="utf-8")
    print(f"Tables written to {out}")


if __name__ == "__main__":
    main()
