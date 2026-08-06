"""Run the fixed, dataset-only extraction validation cohort.

Every model receives the manifest-defined dataset list.  Paper jobs run in
parallel, with a separate concurrency limit for each language model.
"""

from __future__ import annotations

import argparse
import json
import sys
import threading
from concurrent.futures import Future, ThreadPoolExecutor, as_completed
from contextlib import ExitStack
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from backend.extraction_validation import (
    ValidationManifest,
    ValidationPaper,
    load_manifest,
    normalized_entries,
    pairwise_disagreements,
    render_report,
    values_match,
)
from backend.llm_backends import ModelRoute, configured_backends, fetch_model_routes
from backend.llm_tasks import _slugify_label
from backend.llm_types import CallRecord, ExtractionOutput
from backend.paper_storage import PaperStorage
from backend.results_parser import normalize_dataset_alias
from experiments.extraction import compare_models as cm


@dataclass(frozen=True)
class PaperInputs:
    paper: ValidationPaper
    paper_text: str
    structured_tables: list[Any]
    latex_paper: Any
    title: str


@dataclass(frozen=True)
class JobResult:
    arxiv_id: str
    model: str
    output: ExtractionOutput | None
    artifact: Path | None
    source: str
    duration_s: float
    usage: dict[str, Any]
    calls: tuple[CallRecord, ...]
    error: str | None = None


def _validation_label(manifest: ValidationManifest, model: str) -> str:
    return f"extraction-validation/{manifest.digest}/{model}"


def _validation_artifact(manifest: ValidationManifest, arxiv_id: str, model: str) -> Path:
    return (
        PaperStorage(arxiv_id).extracted_dir
        / "experiments"
        / _slugify_label(_validation_label(manifest, model))
    )


def _read_output(path: Path) -> tuple[dict[str, Any] | None, ExtractionOutput | None]:
    data = cm._read_llm_output_file(path)
    return (data, cm._parse_extraction_output(data)) if data else (None, None)


def _load_cached(
    manifest: ValidationManifest,
    arxiv_id: str,
    model: str,
    *,
    force: bool,
) -> tuple[ExtractionOutput, dict[str, Any], Path, str] | None:
    """Load only artifacts carrying the current manifest/revision digest."""
    if force:
        return None
    artifact = _validation_artifact(manifest, arxiv_id, model)
    data, output = _read_output(artifact)
    if output is None or data is None:
        return None
    experiment = data.get("experiment") or {}
    if experiment.get("label") != _validation_label(manifest, model):
        return None
    return output, data, artifact, "cached-validation"


def _manual_review_markdown(
    arxiv_id: str, outputs: dict[str, ExtractionOutput], artifacts: dict[str, Path]
) -> str:
    entries = {
        model: cm._dedupe_result_entries(output.results) for model, output in outputs.items()
    }
    rows: dict[tuple[str, str, str], dict[str, object]] = {}
    for model, values in entries.items():
        for value in values:
            key = (value.model, value.dataset, value.metric)
            rows.setdefault(key, {})[model] = value
    models = sorted(outputs)
    lines = [
        f"# Manual extraction review: {arxiv_id}",
        "",
        "Each linked artifact is a full human-readable extraction table. The matrix below "
        "highlights the per-model values to inspect.",
        "",
    ]
    for model in models:
        lines.append(f"- `{model}`: `{artifacts[model] / 'results_human_readable.md'}`")
    lines.extend(
        [
            "",
            "| Extracted model | Dataset | Metric | " + " | ".join(models) + " |",
            "|---|---|---|" + "---|" * len(models),
        ]
    )
    for key in sorted(rows, key=lambda item: tuple(x.lower() for x in item)):
        values = []
        for model in models:
            item = rows[key].get(model)
            values.append("—" if item is None else str(item.value))
        lines.append("| " + " | ".join((*key, *values)) + " |")
    return "\n".join(lines)


def _atomic_write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(content, encoding="utf-8")
    temporary.replace(path)


def _atomic_write_json(path: Path, payload: dict[str, Any]) -> None:
    _atomic_write_text(path, json.dumps(payload, indent=2))


def _load_inputs(manifest: ValidationManifest) -> tuple[list[PaperInputs], list[dict[str, Any]]]:
    inputs: list[PaperInputs] = []
    failures: list[dict[str, Any]] = []
    for paper in manifest.papers:
        paper_text, structured_tables, latex_paper = cm._load_paper_inputs(paper.arxiv_id)
        if not paper_text and latex_paper is None:
            for model in manifest.models:
                failures.append(
                    {
                        "arxiv_id": paper.arxiv_id,
                        "model": model.model_id,
                        "role": model.role,
                        "status": "failed",
                        "source": "missing-input",
                        "result_count": 0,
                        "expected_dataset_count": len(paper.datasets),
                        "extracted_dataset_count": 0,
                        "missing_datasets": list(paper.datasets),
                        "duration_s": 0.0,
                        "total_tokens": 0,
                        "parse_errors": 0,
                        "artifact_path": "",
                        "error": "no local paper input",
                    }
                )
            continue
        inputs.append(
            PaperInputs(
                paper=paper,
                paper_text=paper_text,
                structured_tables=structured_tables,
                latex_paper=latex_paper,
                title=cm._resolve_paper_title(paper.arxiv_id),
            )
        )
    return inputs, failures


def _run_job(
    manifest: ValidationManifest,
    paper_inputs: PaperInputs,
    model: str,
    route: ModelRoute,
    *,
    force: bool,
) -> JobResult:
    arxiv_id = paper_inputs.paper.arxiv_id
    cached = _load_cached(manifest, arxiv_id, model, force=force)
    if cached:
        output, data, artifact, source = cached
        usage = data.get("usage") or {}
        return JobResult(
            arxiv_id,
            model,
            output,
            artifact,
            source,
            float(usage.get("total_duration_s") or 0.0),
            usage,
            (),
        )

    worker = threading.current_thread().name
    output, duration, error, calls, artifact, _at = cm._run_full_extraction(
        arxiv_id,
        model,
        paper_inputs.paper_text,
        paper_inputs.structured_tables,
        paper_inputs.latex_paper,
        paper_inputs.title,
        output_prefix=f"[{model} / {arxiv_id} / {worker}] ",
        endpoint=route.backend.endpoint,
        api_key=route.backend.api_key,
        experiment_label=_validation_label(manifest, model),
        extraction_strategy="two-step",
        known_datasets=paper_inputs.paper.dataset_info(),
        extraction_only=True,
    )
    data, persisted_output = _read_output(artifact) if artifact else (None, None)
    if output is None:
        output = persisted_output
    return JobResult(
        arxiv_id,
        model,
        output,
        artifact,
        "fresh" if output is not None else "failed",
        duration,
        (data or {}).get("usage") or {},
        tuple(calls),
        error,
    )


def _job_row(result: JobResult, role: str, expected_datasets: tuple[str, ...]) -> dict[str, Any]:
    parse_errors = sum(1 for call in result.calls if call.parse_error)
    expected = {normalize_dataset_alias(dataset).lower() for dataset in expected_datasets}
    extracted = {
        normalize_dataset_alias(item.dataset).lower()
        for item in (result.output.results if result.output else [])
    }
    return {
        "arxiv_id": result.arxiv_id,
        "model": result.model,
        "role": role,
        "status": "ok" if result.output is not None and not result.error else "failed",
        "source": result.source,
        "result_count": len(result.output.results) if result.output else 0,
        "expected_dataset_count": len(expected),
        "extracted_dataset_count": len(expected & extracted),
        "missing_datasets": sorted(expected - extracted),
        "duration_s": result.duration_s,
        "total_tokens": int(result.usage.get("total_tokens") or 0),
        "prompt_tokens": int(result.usage.get("prompt_tokens") or 0),
        "completion_tokens": int(result.usage.get("completion_tokens") or 0),
        "parse_errors": parse_errors,
        "artifact_path": str(result.artifact or ""),
        "error": result.error,
    }


def _checkpoint(
    path: Path,
    *,
    run_id: str,
    manifest: ValidationManifest,
    rows: list[dict[str, Any]],
    expected_jobs: int,
) -> None:
    _atomic_write_json(
        path,
        {
            "run_id": run_id,
            "manifest_digest": manifest.digest,
            "validation_revision": manifest.revision,
            "completed_jobs": len(rows),
            "expected_jobs": expected_jobs,
            "rows": sorted(rows, key=lambda row: (row["arxiv_id"], row["model"])),
        },
    )


def _consensus_for_key(outputs: dict[str, ExtractionOutput], models: list[str], key: str) -> str:
    present: list[tuple[str, float]] = []
    missing: list[str] = []
    for model in models:
        entry = normalized_entries(outputs[model]).get(key)
        if entry is None:
            missing.append(model)
        else:
            present.append((model, entry["value"]))
    groups: list[list[tuple[str, float]]] = []
    for item in present:
        for group in groups:
            if values_match(item[1], group[0][1]):
                group.append(item)
                break
        else:
            groups.append([item])
    groups.sort(key=len, reverse=True)
    summary = "; ".join(
        f"{group[0][1]}: {', '.join(model for model, _value in group)}" for group in groups
    )
    if missing:
        summary += ("; " if summary else "") + f"missing: {', '.join(missing)}"
    return summary


def _build_reports(
    *,
    manifest: ValidationManifest,
    run_id: str,
    manifest_path: Path,
    output_dir: Path,
    report_rows: list[dict[str, Any]],
    all_outputs: dict[str, dict[str, ExtractionOutput]],
    artifacts: dict[str, dict[str, Path]],
) -> None:
    reference_model = manifest.reference_model
    for arxiv_id, outputs in all_outputs.items():
        reference_output = outputs.get(reference_model)
        if reference_output is None:
            continue
        reference = cm._extraction_output_to_baseline(reference_output)
        for row in report_rows:
            if (
                row["arxiv_id"] != arxiv_id
                or row["model"] == reference_model
                or row["model"] not in outputs
            ):
                continue
            comparison = cm._compare(arxiv_id, row["model"], reference, outputs[row["model"]], [])
            row.update(
                {
                    "hits": comparison.hits,
                    "misses": comparison.misses,
                    "value_errors": comparison.value_errors,
                    "hallucinations": comparison.hallucinations,
                    "recall": f"{comparison.recall:.1%}",
                    "precision": f"{comparison.precision:.1%}",
                }
            )

    disagreements: list[dict[str, Any]] = []
    for arxiv_id, outputs in all_outputs.items():
        models = [model for model in manifest.disagreement_models if model in outputs]
        if reference_model not in outputs:
            continue
        for item in pairwise_disagreements(outputs, models):
            reference = normalized_entries(outputs[reference_model]).get(item["key"])
            item["reference"] = reference
            values = [entry for entry in (item["left"], item["right"]) if entry is not None]
            if reference is None:
                item["reference_judgment"] = "Reference has no matching row"
            elif any(values_match(entry["value"], reference["value"]) for entry in values):
                item["reference_judgment"] = "At least one model matches the reference"
            else:
                item["reference_judgment"] = "Neither model matches the reference"
            item["consensus"] = _consensus_for_key(outputs, models, item["key"])
            item["arxiv_id"] = arxiv_id
            item["artifact_paths"] = {
                model: str(artifacts[arxiv_id][model] / "results_human_readable.md")
                for model in item["models"]
            }
            disagreements.append(item)

    manual_reviews: dict[str, dict[str, str]] = {}
    for arxiv_id in manifest.manual_review_papers:
        outputs = all_outputs.get(arxiv_id)
        if not outputs:
            continue
        review_path = output_dir / f"manual_review_{arxiv_id}.md"
        _atomic_write_text(
            review_path,
            _manual_review_markdown(arxiv_id, outputs, artifacts[arxiv_id]),
        )
        manual_reviews[arxiv_id] = {
            model: str(path / "results_human_readable.md")
            for model, path in artifacts[arxiv_id].items()
        }

    payload = {
        "run_id": run_id,
        "manifest": str(manifest_path),
        "manifest_digest": manifest.digest,
        "validation_revision": manifest.revision,
        "baseline_model": reference_model,
        "models": [{"model_id": model.model_id, "role": model.role} for model in manifest.models],
        "rows": sorted(report_rows, key=lambda row: (row["arxiv_id"], row["model"])),
        "advanced_model_disagreements": disagreements,
        "manual_reviews": manual_reviews,
    }
    _atomic_write_json(output_dir / "report.json", payload)
    _atomic_write_text(
        output_dir / "report.md",
        render_report(
            manifest=manifest,
            run_id=run_id,
            model_rows=payload["rows"],
            disagreements=disagreements,
            manual_reviews=manual_reviews,
        ),
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run fixed dataset-only extraction validation")
    parser.add_argument("--manifest", type=Path, default=Path("config/extraction_validation.yaml"))
    parser.add_argument("--output-dir", type=Path, default=None)
    parser.add_argument("--force", action="store_true", help="Ignore current validation artifacts")
    parser.add_argument(
        "--preflight-only",
        action="store_true",
        help="Validate the manifest and required model routes without running extraction",
    )
    parser.add_argument(
        "--workers-per-model",
        type=int,
        default=3,
        metavar="N",
        help="Concurrent paper jobs for each model (default: 3)",
    )
    args = parser.parse_args(argv)
    if args.workers_per_model < 1:
        parser.error("--workers-per-model must be >= 1")

    manifest = load_manifest(args.manifest)
    routes = fetch_model_routes(configured_backends())
    required_models = [model.model_id for model in manifest.models]
    missing_models = [model for model in required_models if model not in routes]
    if missing_models:
        print(
            "Required validation models are unreachable: " + ", ".join(missing_models),
            file=sys.stderr,
        )
        return 1
    print("Validation models:")
    for model in manifest.models:
        print(f"  {model.model_id} ({model.role}, {routes[model.model_id].backend.label})")
    if args.preflight_only:
        return 0

    run_id = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    output_dir = args.output_dir or Path("experiments/extraction_validation") / run_id
    output_dir.mkdir(parents=True, exist_ok=True)
    paper_inputs, report_rows = _load_inputs(manifest)
    expected_jobs = len(manifest.papers) * len(manifest.models)

    all_outputs: dict[str, dict[str, ExtractionOutput]] = {}
    artifacts: dict[str, dict[str, Path]] = {}
    role_by_model = {model.model_id: model.role for model in manifest.models}
    datasets_by_paper = {inputs.paper.arxiv_id: inputs.paper.datasets for inputs in paper_inputs}
    futures: dict[Future[JobResult], tuple[str, str]] = {}
    with ExitStack() as stack:
        for model in required_models:
            executor = stack.enter_context(
                ThreadPoolExecutor(
                    max_workers=args.workers_per_model,
                    thread_name_prefix=f"validation-{_slugify_label(model)}",
                )
            )
            for inputs in paper_inputs:
                future = executor.submit(
                    _run_job,
                    manifest,
                    inputs,
                    model,
                    routes[model],
                    force=args.force,
                )
                futures[future] = (model, inputs.paper.arxiv_id)

        print(
            f"Running {len(futures)} jobs across {len(required_models)} models "
            f"with {args.workers_per_model} workers per model."
        )
        for future in as_completed(futures):
            model, arxiv_id = futures[future]
            try:
                result = future.result()
            except Exception as exc:  # preserve the rest of a long experiment
                result = JobResult(
                    arxiv_id,
                    model,
                    None,
                    None,
                    "failed",
                    0.0,
                    {},
                    (),
                    f"{type(exc).__name__}: {exc}",
                )
            row = _job_row(result, role_by_model[model], datasets_by_paper[arxiv_id])
            report_rows.append(row)
            if result.output is not None and result.artifact is not None:
                all_outputs.setdefault(arxiv_id, {})[model] = result.output
                artifacts.setdefault(arxiv_id, {})[model] = result.artifact
            status = "OK" if row["status"] == "ok" else f"FAILED: {row['error']}"
            print(f"[{len(report_rows)}/{expected_jobs}] {model} / {arxiv_id}: {status}")
            _checkpoint(
                output_dir / "run_state.json",
                run_id=run_id,
                manifest=manifest,
                rows=report_rows,
                expected_jobs=expected_jobs,
            )

    _build_reports(
        manifest=manifest,
        run_id=run_id,
        manifest_path=args.manifest,
        output_dir=output_dir,
        report_rows=report_rows,
        all_outputs=all_outputs,
        artifacts=artifacts,
    )
    failures = [row for row in report_rows if row.get("status") == "failed"]
    print(f"Validation report written to {output_dir}")
    if failures:
        print(f"Validation completed with {len(failures)} failed job(s).", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
