#!/usr/bin/env python3
"""Run focused, baseline-free protocol extractions in parallel."""

from __future__ import annotations

import argparse
import json
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import UTC, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from backend.llm_backends import configured_backends
from backend.llm_tasks import _slugify_label
from backend.llm_types import DatasetInfo
from experiments.extraction.compare_models import _load_paper_inputs, _run_full_extraction


def _parse_paper_target(value: str) -> tuple[str, str]:
    paper_id, separator, dataset = value.partition("=")
    if not separator or not paper_id.strip() or not dataset.strip():
        raise argparse.ArgumentTypeError("expected ARXIV_ID=DATASET")
    return paper_id.strip(), dataset.strip()


def _run_target(
    paper_id: str,
    dataset: str,
    *,
    model: str,
    endpoint: str,
    api_key: str,
) -> dict:
    paper_text, latex_paper = _load_paper_inputs(paper_id)
    label = f"protocol-review-{_slugify_label(model)}-{_slugify_label(dataset)}"
    output, duration, error, _calls, artifact_dir, extracted_at = _run_full_extraction(
        paper_id,
        model,
        paper_text,
        latex_paper=latex_paper,
        endpoint=endpoint,
        api_key=api_key,
        experiment_label=label,
        target_datasets={dataset},
        known_datasets=[DatasetInfo(name=dataset)],
        extraction_only=True,
        output_prefix=f"{model} @ {paper_id}/{dataset}",
    )
    notes = output.extraction_notes if output is not None else ""
    coverage = output.coverage_assessment if output is not None else "unknown"
    incomplete = bool(
        error
        or output is None
        or str(coverage).casefold() != "complete"
        or "failed:" in notes.casefold()
    )
    return {
        "arxiv_id": paper_id,
        "dataset": dataset,
        "model": model,
        "duration_s": round(duration, 1),
        "error": error,
        "result_count": len(output.results) if output is not None else 0,
        "coverage_assessment": coverage,
        "incomplete": incomplete,
        "extraction_notes": notes,
        "artifact_path": str(artifact_dir) if artifact_dir else None,
        "extracted_at": extracted_at,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paper_targets", nargs="+", type=_parse_paper_target)
    parser.add_argument("--model", required=True)
    parser.add_argument("--backend", default="external")
    parser.add_argument("--workers", type=int, default=10)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)

    backends = {backend.label: backend for backend in configured_backends()}
    backend = backends.get(args.backend)
    if backend is None:
        parser.error(f"configured backend not found: {args.backend}")

    targets = list(dict.fromkeys(args.paper_targets))
    rows: list[dict] = []
    with ThreadPoolExecutor(max_workers=max(1, min(args.workers, len(targets)))) as executor:
        futures = {
            executor.submit(
                _run_target,
                paper_id,
                dataset,
                model=args.model,
                endpoint=backend.endpoint,
                api_key=backend.api_key,
            ): (paper_id, dataset)
            for paper_id, dataset in targets
        }
        for future in as_completed(futures):
            paper_id, dataset = futures[future]
            try:
                row = future.result()
            except Exception as exc:
                row = {
                    "arxiv_id": paper_id,
                    "dataset": dataset,
                    "model": args.model,
                    "duration_s": 0.0,
                    "error": str(exc),
                    "result_count": 0,
                    "coverage_assessment": "unknown",
                    "incomplete": True,
                    "extraction_notes": "",
                    "artifact_path": None,
                    "extracted_at": None,
                }
            rows.append(row)
            status = "ok" if not row["error"] else f"error: {row['error']}"
            print(f"{paper_id} {dataset}: {status}", flush=True)

    rows.sort(key=lambda row: (row["arxiv_id"], row["dataset"].casefold()))
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(
            json.dumps(
                {
                    "run_at": datetime.now(UTC).isoformat(),
                    "model": args.model,
                    "backend": args.backend,
                    "results": rows,
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )

    return 1 if all(row["error"] for row in rows) else 0


if __name__ == "__main__":
    raise SystemExit(main())
