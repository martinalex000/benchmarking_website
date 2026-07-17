"""Exercise the production result prompt against protocol-mismatch excerpts.

Usage::

    uv run python scripts/validate_protocol_guard_models.py \
      google/gemma-4-31B-it Qwen/Qwen3-Coder-30B-A3B-Instruct \
      zai-org/GLM-5.2-FP8 openai/gpt-oss-120b
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from backend.config import cfg
from backend.llm_tasks import LLMExtractor
from backend.results_parser import source_indicates_incompatible_protocol


def _lines(arxiv_id: str, start: int, end: int) -> str:
    path = cfg.papers_dir / arxiv_id / "latex" / "expanded.tex"
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    return "\n".join(lines[start - 1 : end])


def _adversarial_context(*, brief: bool = False) -> str:
    if brief:
        return (
            'FOCUS: Extract results ONLY for the dataset "Cora".\n'
            'CANONICAL DATASET RECORD: task_type="node_classification"\n'
            "EXPERIMENT: We perform link prediction, not node classification, on a custom "
            "80/10/10 edge split with random negative edges. The reported AUC is not a "
            "standard Cora node-classification result.\n"
        )
    link_prediction = _lines("2402.14802", 438, 495)
    all_node_fit = _lines("2308.16800", 427, 450)
    return (
        'FOCUS: Extract results ONLY for the dataset "Cora".\n'
        'CANONICAL DATASET RECORD: task_type="node_classification"\n'
        'primary_metric="Accuracy"\n'
        "Reject results for a different task or a non-standard protocol.\n\n"
        "=== LINK-PREDICTION EXPERIMENT EXCERPT ===\n"
        f"{link_prediction}\n\n"
        "=== ALL-NODE-FITTING EXPERIMENT EXCERPT ===\n"
        f"{all_node_fit}\n"
    )


class _Variant:
    class dataset:
        task_type = "node_classification"


def validate(model: str, *, brief: bool = False) -> tuple[int, int]:
    extractor = LLMExtractor(model_tier="primary", result_output_format="json")
    extractor.model_name = model
    prompt = extractor._read_result_prompt()
    if brief:
        prompt = (
            "Return JSON only with a `results` list. Every row must include model, dataset, metric, "
            "value, evaluation_task, uses_standard_protocol, and protocol_note. "
            "Set uses_standard_protocol=false for a non-canonical task or custom split."
        )
    output = extractor._extract_results_chunk(
        prompt,
        _adversarial_context(brief=brief),
        call_type="protocol_guard_validation",
        max_tokens=512,
    )
    context = _adversarial_context(brief=brief)
    unsafe = [
        result
        for result in output.results
        if result.evaluation_task == "node_classification"
        and result.uses_standard_protocol is True
        and not source_indicates_incompatible_protocol(result.model_dump(), _Variant(), context)
    ]
    if unsafe:
        names = ", ".join(result.model for result in unsafe)
        raise AssertionError(f"unsafe standard node-classification rows: {names}")
    return len(output.results), len(extractor._call_log)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("models", nargs="+", metavar="MODEL")
    parser.add_argument(
        "--brief", action="store_true", help="Use a concise explicit mismatch excerpt"
    )
    args = parser.parse_args(argv)
    for model in args.models:
        rows, calls = validate(model, brief=args.brief)
        print(f"PASS model={model} rows={rows} calls={calls}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
