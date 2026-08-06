#!/usr/bin/env python3
"""Analyze miss/hallucination disagreements between models and a GLM baseline."""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from pathlib import Path

_ENTRY_RE = re.compile(
    r"^- `([^`]+)`(?: "
    r"\((?:baseline value|value): ([+-]?\d*\.?\d+(?:[eE][+-]?\d+)?)\)"
    r"|\s+baseline=([+-]?\d*\.?\d+(?:[eE][+-]?\d+)?)\s+candidate=([+-]?\d*\.?\d+(?:[eE][+-]?\d+)?)"
    r")"
)
_DEFAULT_EXPERIMENT_DIR = Path("experiments/extraction")


def _parse_log_section(text: str, heading: str) -> list[tuple[str, float]]:
    entries: list[tuple[str, float]] = []
    in_section = False
    for line in text.splitlines():
        if line.strip() == f"### {heading}":
            in_section = True
            continue
        if in_section and line.startswith("### "):
            break
        if in_section:
            m = _ENTRY_RE.match(line.strip())
            if m:
                raw = m.group(2) or m.group(3) or m.group(4)
                if raw is not None:
                    entries.append((m.group(1), float(raw)))
    return entries


def _normalize_key(key: str) -> str:
    return key.replace("poked", "pokec").strip().lower()


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("arxiv_id")
    p.add_argument(
        "--log-dir",
        type=Path,
        default=_DEFAULT_EXPERIMENT_DIR / "logs",
        help="Directory containing model comparison logs",
    )
    p.add_argument("--models", nargs="+", required=True)
    p.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output report path (default: experiments/extraction/)",
    )
    args = p.parse_args()
    output = args.output or _DEFAULT_EXPERIMENT_DIR / f"baseline_disagreements_{args.arxiv_id}.md"

    model_data: dict[str, dict] = {}
    for model in args.models:
        safe = model.replace("/", "_")
        path = args.log_dir / f"{safe}__{args.arxiv_id}.md"
        text = path.read_text(encoding="utf-8")
        model_data[model] = {
            "misses": {
                _normalize_key(k): v
                for k, v in _parse_log_section(text, "Missed entries (in baseline, not extracted)")
            },
            "hallucinations": {
                _normalize_key(k): v
                for k, v in _parse_log_section(
                    text, "Hallucinations (extracted but not in baseline)"
                )
            },
            "value_errors": _parse_log_section(text, "Value errors (found but wrong number)"),
        }

    all_miss = [set(d["misses"]) for d in model_data.values()]
    all_hall = [set(d["hallucinations"]) for d in model_data.values()]
    both_miss = set.intersection(*all_miss) if all_miss else set()
    both_hall_agree = set.intersection(*all_hall) if all_hall else set()

    only: dict[str, dict[str, list[str]]] = defaultdict(lambda: defaultdict(list))
    for model, data in model_data.items():
        for k in data["misses"]:
            if k not in both_miss:
                only[model]["misses"].append(k)
        for k in data["hallucinations"]:
            if k not in both_hall_agree:
                only[model]["hallucinations"].append(k)

    lines = [
        f"# Baseline disagreement analysis: {args.arxiv_id}",
        "",
        f"Models: {', '.join(args.models)}",
        "",
        "## Summary",
        "",
    ]
    for model, data in model_data.items():
        lines.append(
            f"- **{model}**: {len(data['misses'])} misses, "
            f"{len(data['hallucinations'])} hallucinations, "
            f"{len(data['value_errors'])} value errors"
        )
    lines.extend(
        [
            "",
            f"- **Both models miss (same GLM keys)**: {len(both_miss)} — likely GLM over-extraction or legitimately hard/secondary rows",
            f"- **Both models hallucinate (same keys)**: {len(both_hall_agree)} — strong signal GLM baseline missed real table rows",
            "",
            "## Both models miss (GLM has, neither extracted)",
            "",
        ]
    )
    for key in sorted(both_miss):
        vals = [model_data[m]["misses"][key] for m in args.models]
        lines.append(f"- `{key}` (GLM baseline values: {vals})")

    lines.extend(["", "## Both models hallucinate (neither in GLM baseline)", ""])
    for key in sorted(both_hall_agree):
        vals = {m: model_data[m]["hallucinations"][key] for m in args.models}
        lines.append(f"- `{key}` — extracted values: {vals}")

    lines.extend(["", "## Per-model-only disagreements", ""])
    for model in args.models:
        lines.append(f"### {model}")
        lines.append("")
        om = only[model]["misses"]
        oh = only[model]["hallucinations"]
        if om:
            lines.append(
                f"**Misses only ({len(om)})** — GLM likely correct, this model under-extracted:"
            )
            for k in sorted(om)[:30]:
                lines.append(f"- `{k}` (GLM={model_data[model]['misses'][k]})")
            if len(om) > 30:
                lines.append(f"- … +{len(om) - 30} more")
        if oh:
            lines.append(f"**Hallucinations only ({len(oh)})**:")
            for k in sorted(oh):
                lines.append(f"- `{k}`")
        lines.append("")

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
