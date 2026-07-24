"""Helpers for fixed-cohort, dataset-only extraction validation."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from backend.llm_types import DatasetInfo, ExtractionOutput
from backend.results_parser import (
    normalize_dataset_alias,
    normalize_dataset_scaled_metric,
    normalize_percentage_metric,
)

ABS_TOL = 0.005
REL_TOL = 0.01
VALID_MODEL_ROLES = frozenset({"reference", "advanced", "local", "weak_baseline"})


@dataclass(frozen=True)
class ValidationModel:
    model_id: str
    role: str


@dataclass(frozen=True)
class ValidationPaper:
    arxiv_id: str
    datasets: tuple[str, ...]

    def dataset_info(self) -> list[DatasetInfo]:
        return [DatasetInfo(name=name) for name in self.datasets]


@dataclass(frozen=True)
class ValidationManifest:
    revision: str
    models: tuple[ValidationModel, ...]
    papers: tuple[ValidationPaper, ...]
    manual_review_papers: tuple[str, ...]
    digest: str

    @property
    def reference_model(self) -> str:
        return next(model.model_id for model in self.models if model.role == "reference")

    @property
    def disagreement_models(self) -> list[str]:
        return [
            model.model_id
            for model in self.models
            if model.role in {"reference", "advanced", "local"}
        ]


def load_manifest(path: Path) -> ValidationManifest:
    """Load and validate the fixed validation cohort."""
    raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    revision = str(raw.get("revision") or "").strip()
    if not revision:
        raise ValueError("Validation manifest requires a non-empty revision")

    models_raw = raw.get("models")
    if not isinstance(models_raw, list) or not models_raw:
        raise ValueError("Validation manifest requires a non-empty models list")
    models: list[ValidationModel] = []
    seen_models: set[str] = set()
    for item in models_raw:
        if not isinstance(item, dict):
            raise ValueError("Each validation model must be a mapping")
        model_id = str(item.get("model_id") or "").strip()
        role = str(item.get("role") or "").strip()
        if not model_id or model_id in seen_models:
            raise ValueError(f"Invalid or duplicate model id: {model_id!r}")
        if role not in VALID_MODEL_ROLES:
            raise ValueError(f"Invalid role for {model_id}: {role!r}")
        seen_models.add(model_id)
        models.append(ValidationModel(model_id, role))
    references = [model for model in models if model.role == "reference"]
    if len(references) != 1:
        raise ValueError("Validation manifest requires exactly one reference model")

    papers_raw = raw.get("papers")
    if not isinstance(papers_raw, list) or not papers_raw:
        raise ValueError("Validation manifest requires a non-empty papers list")

    papers: list[ValidationPaper] = []
    seen: set[str] = set()
    for item in papers_raw:
        if not isinstance(item, dict):
            raise ValueError("Each validation paper must be a mapping")
        arxiv_id = str(item.get("arxiv_id") or "").strip()
        datasets = item.get("datasets")
        if not arxiv_id or arxiv_id in seen:
            raise ValueError(f"Invalid or duplicate arXiv id: {arxiv_id!r}")
        if (
            not isinstance(datasets, list)
            or not datasets
            or not all(isinstance(x, str) and x for x in datasets)
        ):
            raise ValueError(f"{arxiv_id} requires a non-empty dataset list")
        seen.add(arxiv_id)
        papers.append(ValidationPaper(arxiv_id, tuple(datasets)))

    manual = tuple(str(x) for x in raw.get("manual_review_papers", []))
    if not set(manual).issubset(seen):
        raise ValueError("manual_review_papers must be included in papers")
    digest = hashlib.sha256(json.dumps(raw, sort_keys=True).encode()).hexdigest()[:12]
    return ValidationManifest(revision, tuple(models), tuple(papers), manual, digest)


def normalized_entries(output: ExtractionOutput) -> dict[str, dict[str, Any]]:
    """Build the comparison lookup used for baseline and pairwise checks."""
    entries: dict[str, dict[str, Any]] = {}
    for result in output.results:
        dataset = normalize_dataset_alias(result.dataset)
        metric = result.metric.strip()
        value, _ = normalize_percentage_metric(metric, result.value, None)
        value, _ = normalize_dataset_scaled_metric(dataset, metric, value, None)
        key = " / ".join((result.model.strip().lower(), dataset.lower(), metric.lower()))
        candidate = {
            "model": result.model,
            "dataset": dataset,
            "metric": metric,
            "value": value,
            "raw_value": result.value,
            "std": result.std,
            "table_ref": result.table_ref,
            "source_ref": result.source_ref,
            "is_proposed": result.is_proposed,
            "evaluation_task": result.evaluation_task,
            "protocol_decision": result.protocol_decision,
        }
        previous = entries.get(key)
        if previous is None or value > previous["value"]:
            entries[key] = candidate
    return entries


def values_match(left: float, right: float) -> bool:
    return abs(left - right) <= max(ABS_TOL, max(abs(left), abs(right)) * REL_TOL)


def pairwise_disagreements(
    outputs: dict[str, ExtractionOutput],
    advanced_models: list[str],
) -> list[dict[str, Any]]:
    """Return every substantive disagreement between pairs of advanced models."""
    disagreements: list[dict[str, Any]] = []
    for index, left_model in enumerate(advanced_models):
        left = normalized_entries(outputs[left_model])
        for right_model in advanced_models[index + 1 :]:
            right = normalized_entries(outputs[right_model])
            for key in sorted(set(left) | set(right)):
                left_entry, right_entry = left.get(key), right.get(key)
                if (
                    left_entry
                    and right_entry
                    and values_match(left_entry["value"], right_entry["value"])
                ):
                    continue
                disagreements.append(
                    {
                        "models": [left_model, right_model],
                        "key": key,
                        "left": left_entry,
                        "right": right_entry,
                        "kind": "value" if left_entry and right_entry else "presence",
                    }
                )
    return disagreements


def render_report(
    *,
    manifest: ValidationManifest,
    run_id: str,
    model_rows: list[dict[str, Any]],
    disagreements: list[dict[str, Any]],
    manual_reviews: dict[str, dict[str, str]],
) -> str:
    """Render a compact audit report; detailed data remains in the JSON sibling."""
    lines = [
        "# Dataset-only extraction validation",
        "",
        f"Run: `{run_id}`  ",
        f"Manifest: `{manifest.digest}`  ",
        f"Validation revision: `{manifest.revision}`  ",
        f"Papers: {len(manifest.papers)}  ",
        f"Paper–dataset combinations: {sum(len(p.datasets) for p in manifest.papers)}",
        "",
        "## Model summary",
        "",
        "| Paper | Model | Role | Status | Source | Dataset coverage | Rows | Recall | Precision | Tokens | Parse errors | Duration | Artifact |",
        "|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in model_rows:
        lines.append(
            "| {paper} | {model} | {role} | {status} | {source} | {coverage} | {rows} | {recall} | {precision} | {tokens} | {parse_errors} | {duration:.1f}s | `{artifact}` |".format(
                paper=row["arxiv_id"],
                model=row["model"],
                role=row["role"],
                status=row.get("status", "ok"),
                source=row["source"],
                coverage=(
                    f"{row.get('extracted_dataset_count', 0)}/"
                    f"{row.get('expected_dataset_count', 0)}"
                ),
                rows=row["result_count"],
                recall=row.get("recall", "reference"),
                precision=row.get("precision", "reference"),
                tokens=row.get("total_tokens", 0),
                parse_errors=row.get("parse_errors", 0),
                duration=row["duration_s"],
                artifact=row.get("artifact_path") or "",
            )
        )

    failures = [row for row in model_rows if row.get("status") == "failed"]
    if failures:
        lines.extend(["", "## Failed jobs", ""])
        for row in failures:
            lines.append(
                f"- `{row['arxiv_id']} / {row['model']}`: {row.get('error') or 'unknown error'}"
            )

    lines.extend(["", "## Advanced-model disagreements", ""])
    if not disagreements:
        lines.append("No missing, extra, or out-of-tolerance normalized result rows.")
    else:
        lines.extend(
            [
                "| Paper | Models | Key | Difference | Left | Right | Consensus | Reference judgment |",
                "|---|---|---|---|---|---|---|---|",
            ]
        )
        for item in disagreements:
            left = item["left"]
            right = item["right"]
            left_text = "—" if left is None else _format_disagreement_entry(left)
            right_text = "—" if right is None else _format_disagreement_entry(right)
            lines.append(
                f"| {item.get('arxiv_id', '—')} | {' vs '.join(item['models'])} | `{item['key']}` | {item['kind']} | {left_text} | {right_text} | {item.get('consensus', '—')} | {item.get('reference_judgment', '—')} |"
            )

    lines.extend(["", "## Manual review tables", ""])
    for arxiv_id, links in manual_reviews.items():
        lines.append(f"### {arxiv_id}")
        lines.append("")
        for model, path in sorted(links.items()):
            lines.append(f"- `{model}`: `{path}`")
        lines.append("")
    return "\n".join(lines)


def _format_disagreement_entry(entry: dict[str, Any]) -> str:
    value = entry.get("raw_value", entry["value"])
    normalized = entry["value"]
    value_text = str(value) if value == normalized else f"{value} → {normalized}"
    refs = ", ".join(str(ref) for ref in (entry.get("table_ref"), entry.get("source_ref")) if ref)
    return f"{value_text} ({refs or '?'})"
