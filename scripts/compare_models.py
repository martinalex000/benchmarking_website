"""Experiment: compare extraction quality of all available LLM models vs a baseline.

For each paper with a baseline extraction, runs models using the same full
``process_paper`` path as ``run_manual`` (two-step by default), persists artifacts
under ``papers/<id>/extracted/`` or ``papers/<id>/extracted/experiments/``, and
scores hits / misses / value errors / hallucinations.

Cached experiment artifacts are reused automatically (including in ``--interactive``
mode). Pass ``--force`` to re-run models even when cached artifacts exist.

Usage::

    python -m scripts.compare_models
    python -m scripts.compare_models --paper 2206.08164
    python -m scripts.compare_models --model gemma-3-27b-it --force
    python -m scripts.compare_models --interactive
    python -m scripts.compare_models --no-output
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Literal

import yaml

# Allow running from project root without installing
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from openai import APIConnectionError, APIStatusError, OpenAI, RateLimitError
from rich import box
from rich.console import Console
from rich.syntax import Syntax
from rich.table import Table

from backend.config import cfg
from backend.llm_backends import (
    LEGACY_COMPARE_BASELINE,
    ModelRoute,
    baseline_model_route,
    configured_backends,
    fetch_model_routes,
    is_local_model,
    resolve_baseline_model_id,
    resolve_model_route,
    sort_models_local_first,
)
from backend.llm_extractor import (
    CallRecord,
    DatasetInfo,
    ExtractionOutput,
    LLMExtractor,
    ResultEntry,
)
from backend.llm_postprocessing import _dedupe_result_entries
from backend.llm_tasks import _slugify_label
from backend.model_name_resolution import (
    normalize_model_name_for_resolution,
    strip_implementation_marker,
)
from backend.paper_storage import PaperStorage
from backend.results_parser import (
    normalize_dataset_alias,
    normalize_dataset_scaled_metric,
    normalize_percentage_metric,
)

console = Console()
logger = logging.getLogger(__name__)
_console_lock = threading.Lock()
_baseline_cache: dict[str, list[dict]] = {}

_COMPARE_EXPERIMENT_PREFIX = "compare-models"
_COMPARE_RESULT_OUTPUT_FORMAT = "json"
_DEFAULT_EXPERIMENT_DIR = Path("experiments/extraction")
CompareSource = Literal["fresh", "cached", "auto_included"]

# ── Tolerance for value matching ──────────────────────────────────────────────
ABS_TOL = 0.005
REL_TOL = 0.01  # 1 %

# No models are skipped by default — pass --skip-model to exclude specific ones.
_DEFAULT_SKIP: frozenset[str] = frozenset(
    [
        "apertus-70b-instruct-2509",
        "llama-3.3-70b-instruct",
        "deepseek-r1-distill-llama-70b",
        "black-forest-labs/FLUX.2-dev",
        "alias-reasoning",
        "stabilityai/stable-diffusion-3.5-large-turbo",
        "BAAI/bge-reranker-v2-m3",
        "black-forest-labs/FLUX.2-klein-9B",
        "openai/whisper-large-v3",
        "alias-vision",
        "meta-llama/Llama-3.3-70B-Instruct",
        "alias-huge-no-thinking",
        "Qwen/Qwen3-Embedding-4B",
        "alias-image-generation",
        "alias-code",
        "alias-huge",
        "alias-ha",
        "tts-1-hd",
        "Kokoro-82M",
    ]
)


# ── Data structures ───────────────────────────────────────────────────────────


@dataclass
class EntryKey:
    model: str
    dataset: str
    metric: str

    @property
    def _model_key(self) -> str:
        resolved = normalize_model_name_for_resolution(self.model)
        canonical = strip_implementation_marker(resolved) or resolved
        return canonical.lower()

    def __hash__(self) -> int:
        return hash((self._model_key, self.dataset.lower(), self.metric.lower()))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, EntryKey):
            return NotImplemented
        return (
            self._model_key == other._model_key
            and self.dataset.lower() == other.dataset.lower()
            and self.metric.lower() == other.metric.lower()
        )

    def __str__(self) -> str:
        return f"{normalize_model_name_for_resolution(self.model)} / {self.dataset} / {self.metric}"


@dataclass
class PaperComparison:
    arxiv_id: str
    llm_model: str
    baseline_count: int
    backend: str = "external"
    hits: int = 0
    value_errors: int = 0
    misses: int = 0
    hallucinations: int = 0
    duration_s: float = 0.0
    error: str | None = None
    call_log: list[CallRecord] = field(default_factory=list)
    hit_keys: list[dict] = field(default_factory=list)
    value_error_keys: list[dict] = field(default_factory=list)
    miss_keys: list[dict] = field(default_factory=list)
    hallucinated_keys: list[dict] = field(default_factory=list)
    source: CompareSource = "fresh"
    artifact_path: Path | None = None
    extracted_at: str | None = None

    @property
    def precision(self) -> float:
        extracted = self.hits + self.value_errors + self.hallucinations
        return self.hits / extracted if extracted > 0 else 0.0

    @property
    def recall(self) -> float:
        return self.hits / self.baseline_count if self.baseline_count > 0 else 0.0

    @property
    def hallucination_rate(self) -> float:
        extracted = self.hits + self.value_errors + self.hallucinations
        return self.hallucinations / extracted if extracted > 0 else 0.0


@dataclass
class CompareJob:
    model: str
    endpoint: str
    api_key: str
    backend: str
    arxiv_id: str
    paper_title: str
    paper_text: str
    structured_tables: list
    baseline: list[dict]
    latex_paper: Any = None


@dataclass
class _BaselineContext:
    """Tracks baseline generation failures."""

    failed: set[str] = field(default_factory=set)


@dataclass
class _CompareExtractionResult:
    job: CompareJob
    out: ExtractionOutput | None
    duration_s: float
    error: str | None
    call_log: list[CallRecord]
    source: CompareSource = "fresh"
    artifact_path: Path | None = None
    extracted_at: str | None = None


@dataclass
class _ProcessOptions:
    show_prompts: bool = False
    oneshot: bool = False
    log_dir: Path | None = None
    db_primary_metrics: dict[str, str] | None = None
    classify_errors: bool = False
    ensure_baseline: bool = True
    model_routes: dict[str, ModelRoute] | None = None
    baseline_model_id: str = ""
    baseline_ctx: _BaselineContext | None = None
    force_all: bool = False
    forced_models: set[str] = field(default_factory=set)
    persist: bool = True


@dataclass
class _RunPlanRow:
    model: str
    arxiv_id: str
    paper_title: str
    source: CompareSource
    action: str
    artifact_path: Path | None = None


@dataclass
class _BaselineJob:
    arxiv_id: str
    paper_title: str
    paper_text: str
    structured_tables: list
    latex_paper: Any
    model: str
    endpoint: str
    api_key: str
    backend: str


# ── Helpers ───────────────────────────────────────────────────────────────────


def _safe_print(*args: Any, **kwargs: Any) -> None:
    with _console_lock:
        console.print(*args, **kwargs)
        sys.stdout.flush()


def _safe_rule(title: str, **kwargs: Any) -> None:
    with _console_lock:
        console.rule(title, **kwargs)


def _truncate_title(title: str, max_len: int = 72) -> str:
    title = title.strip()
    if len(title) <= max_len:
        return title
    return title[: max_len - 1] + "…"


def _resolve_paper_title(arxiv_id: str) -> str:
    """Best-effort paper title from DB, local cache, or arXiv API."""
    try:
        from backend.db import init_db, session_scope
        from backend.models import Paper

        init_db()
        with session_scope() as session:
            paper = session.query(Paper).filter_by(arxiv_id=arxiv_id).first()
            if paper and paper.title and not paper.title.startswith("arXiv:"):
                return paper.title.strip()
    except Exception as exc:
        logger.debug("DB title lookup failed for %s: %s", arxiv_id, exc)

    from backend.paper_storage import PaperStorage

    storage = PaperStorage(arxiv_id)
    if storage.metadata_path.exists():
        try:
            metadata = json.loads(storage.metadata_path.read_text(encoding="utf-8"))
            title = str(metadata.get("title") or "").strip()
            if title:
                return title
        except (OSError, json.JSONDecodeError):
            pass

    if storage.latex_dir.exists():
        try:
            from backend.llm_metadata import _extract_metadata_from_latex_cache

            meta = _extract_metadata_from_latex_cache(storage.latex_dir)
            title = str(meta.get("title") or "").strip()
            if title:
                return title
        except Exception:
            pass

    if storage.html_index_path.exists():
        try:
            from backend.html_parser import parse_html_paper

            parsed = parse_html_paper(storage.html_index_path)
            if parsed.title:
                return parsed.title.strip()
        except Exception:
            pass

    try:
        from backend.llm_metadata import fetch_arxiv_metadata

        meta = fetch_arxiv_metadata(arxiv_id)
        title = str(meta.get("title") or "").strip()
        if title and not title.startswith("arXiv:"):
            return title
    except Exception:
        pass

    return ""


def _format_paper_header(arxiv_id: str, paper_title: str) -> str:
    if paper_title:
        return f"{arxiv_id} — {_truncate_title(paper_title)}"
    return arxiv_id


def _interactive_pick(
    items: list[tuple[str, str]],
    *,
    kind: str,
    extra_columns: list[tuple[str, list[str]]] | None = None,
    footer: str | None = None,
) -> list[str] | None:
    """Return selected item ids, [] if nothing selected, None to abort."""
    if not items:
        return []

    table = Table(show_header=True, header_style="bold", box=box.SIMPLE, show_edge=False)
    table.add_column("#", style="dim", justify="right", width=4)
    table.add_column(kind, style="cyan")
    if extra_columns:
        for header, _values in extra_columns:
            table.add_column(header)
    for index, (_item_id, label) in enumerate(items, start=1):
        row: list[str] = [str(index), label]
        if extra_columns:
            for _header, values in extra_columns:
                row.append(values[index - 1])
        table.add_row(*row)
    _safe_print(table)
    if footer:
        _safe_print(footer)
    _safe_print(
        f"\nSelect {kind.lower()} to process "
        f"(space/comma-separated numbers, [bold]a[/bold] for all, [bold]q[/bold] to quit):"
    )
    try:
        raw = input("> ").strip()
    except (EOFError, KeyboardInterrupt):
        return None

    if not raw or raw.lower() == "q":
        return []
    if raw.lower() == "a":
        return [item_id for item_id, _ in items]

    selected: list[str] = []
    for token in re.split(r"[\s,]+", raw):
        token = token.strip()
        if not token:
            continue
        try:
            index = int(token) - 1
            if 0 <= index < len(items):
                selected.append(items[index][0])
            else:
                _safe_print(f"[yellow]  Index {token} out of range — skipped[/yellow]")
        except ValueError:
            _safe_print(f"[yellow]  Not a number: {token!r} — skipped[/yellow]")
    return selected


def _values_match(a: float, b: float) -> bool:
    return abs(a - b) <= ABS_TOL or (b != 0 and abs(a - b) / abs(b) <= REL_TOL)


def _normalize_baseline_entries(entries: list[dict]) -> list[dict]:
    """Collapse implementation-marker variants (e.g. GCN vs GCN*) before scoring."""
    parsed: list[ResultEntry] = []
    for entry in entries:
        model = entry.get("model", "")
        stripped = strip_implementation_marker(model) or model
        val = entry.get("value")
        if val is None:
            continue
        parsed.append(
            ResultEntry(
                model=stripped,
                dataset=entry.get("dataset", ""),
                metric=entry.get("metric", ""),
                value=float(val),
            )
        )
    return [
        {
            "model": row.model,
            "dataset": row.dataset,
            "metric": row.metric,
            "value": row.value,
        }
        for row in _dedupe_result_entries(parsed)
    ]


def _load_baseline(arxiv_id: str, baseline_model_id: str) -> list[dict]:
    yaml_path = cfg.papers_dir / arxiv_id / "extracted" / "llm_output.yaml"
    json_path = cfg.papers_dir / arxiv_id / "extracted" / "llm_output.json"
    path = yaml_path if yaml_path.exists() else json_path
    if not path.exists():
        return []
    try:
        text = path.read_text(encoding="utf-8")
        data = yaml.safe_load(text) if path.suffix == ".yaml" else json.loads(text)
    except (OSError, json.JSONDecodeError, yaml.YAMLError) as exc:
        logger.warning("Could not load baseline for %s: %s", arxiv_id, exc)
        return []
    model_used = data.get("model_used")
    accepted = {baseline_model_id, LEGACY_COMPARE_BASELINE}
    if model_used not in accepted:
        return []
    rows = data.get("results", {}).get("results", [])
    return _normalize_baseline_entries(rows)


def _get_cached_baseline(arxiv_id: str, baseline_model_id: str) -> list[dict]:
    cached = _baseline_cache.get(arxiv_id)
    if cached:
        return cached
    on_disk = _load_baseline(arxiv_id, baseline_model_id)
    if on_disk:
        _baseline_cache[arxiv_id] = on_disk
    return on_disk


def _extraction_output_to_baseline(output: ExtractionOutput) -> list[dict]:
    return [
        {
            "model": entry.model,
            "dataset": entry.dataset,
            "metric": entry.metric,
            "value": entry.value,
        }
        for entry in output.results
    ]


def _warm_baseline_cache(paper_ids: list[str], baseline_model_id: str) -> None:
    for arxiv_id in paper_ids:
        _get_cached_baseline(arxiv_id, baseline_model_id)


def _slugify_compare_model(model_id: str) -> str:
    return _slugify_label(model_id)


def _compare_experiment_label(model_id: str, *, oneshot: bool = False) -> str:
    slug = _slugify_compare_model(model_id)
    if oneshot:
        return f"{_COMPARE_EXPERIMENT_PREFIX}/{slug}-oneshot"
    return f"{_COMPARE_EXPERIMENT_PREFIX}/{slug}"


def _compare_artifact_dir(arxiv_id: str, model_id: str, *, oneshot: bool = False) -> Path:
    label = _compare_experiment_label(model_id, oneshot=oneshot)
    return PaperStorage(arxiv_id).extracted_dir / "experiments" / _slugify_label(label)


def _read_llm_output_file(artifact_dir: Path) -> dict | None:
    yaml_path = artifact_dir / "llm_output.yaml"
    json_path = artifact_dir / "llm_output.json"
    path = yaml_path if yaml_path.exists() else json_path
    if not path.exists():
        return None
    try:
        text = path.read_text(encoding="utf-8")
        data = yaml.safe_load(text) if path.suffix == ".yaml" else json.loads(text)
        return data if isinstance(data, dict) else None
    except (OSError, json.JSONDecodeError, yaml.YAMLError) as exc:
        logger.warning("Could not read %s: %s", path, exc)
        return None


def _parse_extraction_output(data: dict) -> ExtractionOutput | None:
    results_block = data.get("results")
    if not isinstance(results_block, dict):
        return None
    try:
        return ExtractionOutput.model_validate(results_block)
    except Exception as exc:
        logger.warning("Could not parse ExtractionOutput: %s", exc)
        return None


def _call_records_from_dicts(records: list[dict] | None) -> list[CallRecord]:
    if not records:
        return []
    out: list[CallRecord] = []
    for item in records:
        if not isinstance(item, dict):
            continue
        out.append(
            CallRecord(
                call_type=str(item.get("call_type") or ""),
                system_prompt=str(item.get("system_prompt") or ""),
                user_content=str(item.get("user_content") or ""),
                raw_response=str(item.get("raw_response") or ""),
                input_chars=int(item.get("input_chars") or 0),
                output_chars=int(item.get("output_chars") or 0),
                duration_s=float(item.get("duration_s") or 0.0),
                ttft_s=item.get("ttft_s"),
                tokens_per_sec=item.get("tokens_per_sec"),
                prompt_tokens=item.get("prompt_tokens"),
                completion_tokens=item.get("completion_tokens"),
                success=bool(item.get("success")),
                parse_error=item.get("parse_error"),
                extra=dict(item.get("extra") or {}),
            )
        )
    return out


def _load_call_log_from_artifact(artifact_dir: Path) -> list[CallRecord]:
    calls_path = artifact_dir / "llm_calls.yaml"
    if not calls_path.exists():
        return []
    try:
        loaded = yaml.safe_load(calls_path.read_text(encoding="utf-8")) or []
    except (OSError, yaml.YAMLError) as exc:
        logger.warning("Could not load call log from %s: %s", calls_path, exc)
        return []
    return _call_records_from_dicts(loaded if isinstance(loaded, list) else [])


def _is_valid_compare_cache(artifact_dir: Path, expected_label: str | None = None) -> bool:
    data = _read_llm_output_file(artifact_dir)
    if not data:
        return False
    experiment = data.get("experiment") or {}
    label = experiment.get("label")
    if expected_label is not None and label != expected_label:
        return False
    if expected_label is None and label:
        prefix = f"{_COMPARE_EXPERIMENT_PREFIX}/"
        if not str(label).startswith(prefix):
            return False
    out = _parse_extraction_output(data)
    return out is not None and bool(out.results)


def _model_id_from_artifact(data: dict) -> str | None:
    model_used = data.get("model_used")
    if isinstance(model_used, str) and model_used.strip():
        return model_used.strip()
    return None


def _discover_cached_models_for_paper(arxiv_id: str) -> dict[str, Path]:
    """Return {model_id: artifact_dir} for valid compare-models caches on one paper."""
    experiments_root = PaperStorage(arxiv_id).extracted_dir / "experiments"
    if not experiments_root.is_dir():
        return {}
    found: dict[str, Path] = {}
    for child in sorted(experiments_root.iterdir()):
        if not child.is_dir():
            continue
        if not child.name.startswith(f"{_slugify_label(_COMPARE_EXPERIMENT_PREFIX)}-"):
            continue
        if child.name.endswith("-oneshot"):
            continue
        experiment = _read_llm_output_file(child)
        if not experiment:
            continue
        label = (experiment.get("experiment") or {}).get("label")
        if not isinstance(label, str) or not label.startswith(f"{_COMPARE_EXPERIMENT_PREFIX}/"):
            continue
        if not _is_valid_compare_cache(child, label):
            continue
        model_id = _model_id_from_artifact(experiment)
        if model_id:
            found[model_id] = child
    return found


def _resolve_result_backend(model_id: str, model_routes: dict[str, ModelRoute]) -> str:
    route = model_routes.get(model_id)
    if route is not None:
        return route.backend.label
    return "local" if is_local_model(model_id, model_routes) else "external"


def _model_is_forced(model_id: str, opts: _ProcessOptions) -> bool:
    if opts.force_all:
        return True
    return model_id in opts.forced_models


def _cache_hit(model_id: str, arxiv_id: str, *, oneshot: bool = False) -> Path | None:
    artifact_dir = _compare_artifact_dir(arxiv_id, model_id, oneshot=oneshot)
    expected = _compare_experiment_label(model_id, oneshot=oneshot)
    if _is_valid_compare_cache(artifact_dir, expected):
        return artifact_dir
    return None


def _load_cached_compare_extraction(
    arxiv_id: str,
    model_id: str,
    paper_title: str,
    model_routes: dict[str, ModelRoute],
    *,
    oneshot: bool = False,
    source: CompareSource = "cached",
) -> _CompareExtractionResult | None:
    artifact_dir = _cache_hit(model_id, arxiv_id, oneshot=oneshot)
    if artifact_dir is None:
        return None
    data = _read_llm_output_file(artifact_dir)
    if data is None:
        return None
    out = _parse_extraction_output(data)
    if out is None:
        return None
    call_log = _load_call_log_from_artifact(artifact_dir)
    duration_s = float((data.get("usage") or {}).get("total_duration_s") or 0.0)
    backend = _resolve_result_backend(model_id, model_routes)
    route = model_routes.get(model_id)
    job = CompareJob(
        model=model_id,
        endpoint=route.backend.endpoint if route else (cfg.llm_endpoint or ""),
        api_key=route.backend.api_key if route else cfg.llm_api_key,
        backend=backend,
        arxiv_id=arxiv_id,
        paper_title=paper_title,
        paper_text="",
        structured_tables=[],
        baseline=[],
        latex_paper=None,
    )
    return _CompareExtractionResult(
        job=job,
        out=out,
        duration_s=duration_s,
        error=None,
        call_log=call_log,
        source=source,
        artifact_path=artifact_dir,
        extracted_at=data.get("extracted_at"),
    )


def _comparison_to_dict(cmp: PaperComparison, baseline_model_id: str) -> dict[str, Any]:
    return {
        "arxiv_id": cmp.arxiv_id,
        "model": cmp.llm_model,
        "baseline_model": baseline_model_id,
        "baseline_count": cmp.baseline_count,
        "hits": cmp.hits,
        "value_errors": cmp.value_errors,
        "misses": cmp.misses,
        "hallucinations": cmp.hallucinations,
        "recall": round(cmp.recall, 4),
        "precision": round(cmp.precision, 4),
        "hallucination_rate": round(cmp.hallucination_rate, 4),
        "duration_s": round(cmp.duration_s, 1),
        "error": cmp.error,
        "source": cmp.source,
        "extracted_at": cmp.extracted_at,
        "artifact_path": str(cmp.artifact_path) if cmp.artifact_path else None,
        "details": {
            "hits": cmp.hit_keys,
            "value_errors": cmp.value_error_keys,
            "misses": cmp.miss_keys,
            "hallucinations": cmp.hallucinated_keys,
        },
    }


def _write_comparison_json(
    artifact_dir: Path,
    cmp: PaperComparison,
    baseline_model_id: str,
) -> None:
    artifact_dir.mkdir(parents=True, exist_ok=True)
    path = artifact_dir / "comparison.json"
    path.write_text(
        json.dumps(_comparison_to_dict(cmp, baseline_model_id), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def _format_source_badge(source: CompareSource) -> str:
    if source == "fresh":
        return "[bold green][fresh][/bold green]"
    if source == "cached":
        return "[dim cyan][cached][/dim cyan]"
    return "[dim yellow][auto-included][/dim yellow]"


def _plan_compare_jobs(
    paper_inputs: dict[str, tuple[str, list, list[dict], Any, str]],
    test_models: list[str],
    model_routes: dict[str, ModelRoute],
    opts: _ProcessOptions,
) -> tuple[list[CompareJob], list[_CompareExtractionResult], list[_RunPlanRow]]:
    """Split work into LLM jobs, cached extractions, and a human-readable plan."""
    llm_jobs: list[CompareJob] = []
    cached: list[_CompareExtractionResult] = []
    plan_rows: list[_RunPlanRow] = []
    cached_by_pair: set[tuple[str, str]] = set()

    for pid, (
        paper_text,
        structured_tables,
        baseline,
        latex_paper,
        paper_title,
    ) in paper_inputs.items():
        for model in test_models:
            forced = _model_is_forced(model, opts)
            hit = None if forced else _cache_hit(model, pid)
            if hit is not None:
                loaded = _load_cached_compare_extraction(
                    pid,
                    model,
                    paper_title,
                    model_routes,
                    source="cached",
                )
                if loaded is not None:
                    cached.append(loaded)
                    cached_by_pair.add((model, pid))
                    plan_rows.append(
                        _RunPlanRow(
                            model=model,
                            arxiv_id=pid,
                            paper_title=paper_title,
                            source="cached",
                            action="reuse artifact",
                            artifact_path=hit,
                        )
                    )
                    continue
            route = model_routes.get(model)
            if route is None:
                continue
            llm_jobs.append(
                CompareJob(
                    model=model,
                    endpoint=route.backend.endpoint,
                    api_key=route.backend.api_key,
                    backend=route.backend.label,
                    arxiv_id=pid,
                    paper_title=paper_title,
                    paper_text=paper_text,
                    structured_tables=structured_tables,
                    baseline=baseline,
                    latex_paper=latex_paper,
                )
            )
            plan_rows.append(
                _RunPlanRow(
                    model=model,
                    arxiv_id=pid,
                    paper_title=paper_title,
                    source="fresh",
                    action="LLM (run_manual path)",
                )
            )

        discovered = _discover_cached_models_for_paper(pid)
        for model_id, artifact_dir in sorted(discovered.items()):
            if model_id in test_models:
                continue
            if (model_id, pid) in cached_by_pair:
                continue
            loaded = _load_cached_compare_extraction(
                pid,
                model_id,
                paper_title,
                model_routes,
                source="auto_included",
            )
            if loaded is None:
                continue
            cached.append(loaded)
            cached_by_pair.add((model_id, pid))
            plan_rows.append(
                _RunPlanRow(
                    model=model_id,
                    arxiv_id=pid,
                    paper_title=paper_title,
                    source="auto_included",
                    action="reuse (not in test list)",
                    artifact_path=artifact_dir,
                )
            )

    return llm_jobs, cached, plan_rows


def _render_run_plan_table(
    plan_rows: list[_RunPlanRow], model_routes: dict[str, ModelRoute]
) -> None:
    if not plan_rows:
        return
    table = Table(title="Run plan", box=box.SIMPLE, show_header=True)
    table.add_column("Model", style="cyan")
    table.add_column("Paper", style="dim")
    table.add_column("Title")
    table.add_column("Source")
    table.add_column("Action")
    for row in sorted(plan_rows, key=lambda r: (r.arxiv_id, r.model)):
        backend = _resolve_result_backend(row.model, model_routes)
        model_label = _format_model_display(row.model, backend)
        title = _truncate_title(row.paper_title, max_len=40) or "—"
        table.add_row(
            model_label,
            row.arxiv_id,
            title,
            _format_source_badge(row.source),
            row.action,
        )
    _safe_print(table)
    fresh_n = sum(1 for r in plan_rows if r.source == "fresh")
    cached_n = sum(1 for r in plan_rows if r.source == "cached")
    auto_n = sum(1 for r in plan_rows if r.source == "auto_included")
    _safe_print(
        f"[dim]Plan:[/dim] {fresh_n} fresh LLM job(s), "
        f"{cached_n} reused from disk, "
        f"{auto_n} auto-included cached result(s)"
    )
    _safe_print()


def _count_cached_papers(model_id: str, paper_ids: list[str]) -> int:
    return len(_cached_paper_ids_for_model(model_id, paper_ids))


def _cached_paper_ids_for_model(model_id: str, paper_ids: list[str]) -> list[str]:
    """Return paper IDs that already have a valid compare-models artifact for *model_id*."""
    return [pid for pid in paper_ids if _cache_hit(model_id, pid) is not None]


def _format_cached_traces_column(paper_ids: list[str], cached_paper_ids: list[str]) -> str:
    """Render the Traces column for interactive model selection."""
    if not cached_paper_ids:
        return "[dim]—[/dim]"
    if len(paper_ids) == 1:
        return "[green]yes[/green]"
    if len(cached_paper_ids) == len(paper_ids):
        return f"[green]all {len(cached_paper_ids)}[/green]"
    return ", ".join(cached_paper_ids)


def _baseline_for_paper(
    arxiv_id: str,
    baseline_model_id: str,
    ctx: _BaselineContext | None,
) -> list[dict]:
    if ctx is not None and arxiv_id in ctx.failed:
        return []
    return _get_cached_baseline(arxiv_id, baseline_model_id)


def _print_baseline_job_rule(job: _BaselineJob, job_index: int, total_jobs: int) -> None:
    paper = _format_paper_header(job.arxiv_id, job.paper_title)
    model_label = _format_model_display(job.model, job.backend)
    _safe_print()
    _safe_rule(
        f"[baseline {job_index}/{total_jobs}] generating {model_label} for [bold]{paper}[/bold]"
    )


def _process_baseline_job(
    job: _BaselineJob,
    job_index: int,
    total_jobs: int,
    ctx: _BaselineContext,
) -> None:
    try:
        _print_baseline_job_rule(job, job_index, total_jobs)
        prefix = (
            f"baseline/{job.model} @ "
            f"{_format_paper_header(job.arxiv_id, job.paper_title)} [{job.backend}]"
        )
        out, duration, err, call_log, artifact_dir, extracted_at = _run_full_extraction(
            job.arxiv_id,
            job.model,
            job.paper_text,
            job.structured_tables,
            latex_paper=job.latex_paper,
            paper_title=job.paper_title,
            output_prefix=prefix,
            endpoint=job.endpoint,
            api_key=job.api_key,
            experiment_label=None,
            extraction_strategy="auto",
        )
        if err or out is None:
            ctx.failed.add(job.arxiv_id)
            _safe_print(
                f"  [red]✗ Baseline generation failed for {job.arxiv_id}:[/red] "
                f"{err or 'no output'}"
            )
            _safe_print()
            return

        baseline = _normalize_baseline_entries(_extraction_output_to_baseline(out))
        _baseline_cache[job.arxiv_id] = baseline
        if artifact_dir is not None:
            _safe_print(f"  [dim]Saved → {artifact_dir}[/dim]")
        _safe_print(
            f"  [green]✓ Baseline ready[/green]  "
            f"entries={len(baseline)}  "
            f"[dim]{duration:.1f}s[/dim]"
        )
        _safe_print()
    except Exception:
        ctx.failed.add(job.arxiv_id)
        raise


def _process_compare_extraction(
    job: CompareJob,
    opts: _ProcessOptions,
    job_index: int,
    total_jobs: int,
) -> _CompareExtractionResult:
    """Run model extraction only; metrics are computed after all jobs finish."""
    _print_job_rule(job, job_index, total_jobs)
    prefix = _job_output_prefix(job)
    out, duration, err, call_log, artifact_dir, extracted_at = _run_full_extraction(
        job.arxiv_id,
        job.model,
        job.paper_text,
        job.structured_tables,
        latex_paper=job.latex_paper,
        paper_title=job.paper_title,
        output_prefix=prefix,
        endpoint=job.endpoint,
        api_key=job.api_key,
        experiment_label=_compare_experiment_label(job.model),
        extraction_strategy="auto",
    )

    if opts.show_prompts:
        for _idx, rec in enumerate(call_log, 1):
            with _console_lock:
                _print_call_full_prompt(rec)

    if err or out is None:
        _safe_print(f"  [red]✗ EXTRACTION FAILED:[/red] {err or 'no output'}")
    else:
        _safe_print(f"  [green]✓ Extraction complete[/green]  [dim]{duration:.1f}s[/dim]")
        if artifact_dir is not None:
            _safe_print(f"  [dim]Saved → {artifact_dir}[/dim]")
    _safe_print()
    return _CompareExtractionResult(
        job=job,
        out=out,
        duration_s=duration,
        error=err,
        call_log=call_log,
        source="fresh",
        artifact_path=artifact_dir,
        extracted_at=extracted_at,
    )


def _finalize_compare_result(
    extraction: _CompareExtractionResult,
    opts: _ProcessOptions,
) -> PaperComparison:
    """Score one extraction against the baseline (no LLM calls)."""
    job = extraction.job
    baseline = _baseline_for_paper(job.arxiv_id, opts.baseline_model_id, opts.baseline_ctx)
    if not baseline:
        return PaperComparison(
            arxiv_id=job.arxiv_id,
            llm_model=job.model,
            baseline_count=0,
            backend=job.backend,
            duration_s=extraction.duration_s,
            error="no baseline available",
            call_log=extraction.call_log,
        )

    err = extraction.error
    out = extraction.out
    call_log = extraction.call_log
    duration = extraction.duration_s

    if err or out is None:
        return PaperComparison(
            arxiv_id=job.arxiv_id,
            llm_model=job.model,
            baseline_count=len(baseline),
            backend=job.backend,
            duration_s=duration,
            error=err or "no output",
            call_log=call_log,
        )

    cmp = _compare(
        job.arxiv_id,
        job.model,
        baseline,
        out,
        call_log,
        opts.db_primary_metrics,
    )
    cmp.backend = job.backend
    cmp.duration_s = duration
    cmp.source = extraction.source
    cmp.artifact_path = extraction.artifact_path
    cmp.extracted_at = extraction.extracted_at

    paper = _format_paper_header(job.arxiv_id, job.paper_title)
    model_label = _format_model_display(job.model, job.backend)
    if extraction.source == "cached":
        _safe_print(
            f"  {_format_source_badge('cached')} Reused {extraction.artifact_path} — "
            f"hits=[green]{cmp.hits}[/green]  "
            f"recall=[bold]{_pct(cmp.recall)}[/bold]  "
            f"prec=[bold]{_pct(cmp.precision)}[/bold]"
        )
    elif extraction.source == "auto_included":
        _safe_print(
            f"  {_format_source_badge('auto_included')} {model_label} on [bold]{paper}[/bold] — "
            f"hits=[green]{cmp.hits}[/green]  "
            f"recall=[bold]{_pct(cmp.recall)}[/bold]  "
            f"prec=[bold]{_pct(cmp.precision)}[/bold]"
        )
    else:
        _safe_print(
            f"  [bold]Scores[/bold] {model_label} on [bold]{paper}[/bold]:  "
            f"hits=[green]{cmp.hits}[/green]  "
            f"val_err=[yellow]{cmp.value_errors}[/yellow]  "
            f"miss=[red]{cmp.misses}[/red]  "
            f"halluc=[magenta]{cmp.hallucinations}[/magenta]  "
            f"recall=[bold]{_pct(cmp.recall)}[/bold]  "
            f"prec=[bold]{_pct(cmp.precision)}[/bold]"
        )
    if cmp.miss_keys:
        _safe_print(
            f"  [red]Missed ({len(cmp.miss_keys)}):[/red] "
            + "  ".join(f"[dim]{m['key']}[/dim]" for m in cmp.miss_keys[:5])
            + ("  …" if len(cmp.miss_keys) > 5 else "")
        )
    if cmp.hallucinated_keys:
        _safe_print(
            f"  [magenta]Hallucinated ({len(cmp.hallucinated_keys)}):[/magenta] "
            + "  ".join(f"[dim]{h['key']}[/dim]" for h in cmp.hallucinated_keys[:5])
            + ("  …" if len(cmp.hallucinated_keys) > 5 else "")
        )
    if cmp.value_error_keys:
        _safe_print(f"  [yellow]Value errors ({len(cmp.value_error_keys)}):[/yellow]")
        for ve in cmp.value_error_keys[:5]:
            _safe_print(
                f"    [dim]{ve['key']}[/dim]  "
                f"baseline={ve['baseline']}  candidate={ve['candidate']}"
            )
        if len(cmp.value_error_keys) > 5:
            _safe_print(f"    [dim]… +{len(cmp.value_error_keys) - 5} more[/dim]")
    if opts.classify_errors:
        _print_error_classification(_classify_comparison_errors(cmp, call_log))

    artifact_dir = extraction.artifact_path or _compare_artifact_dir(job.arxiv_id, job.model)
    if opts.persist and extraction.out is not None and not err:
        _write_comparison_json(artifact_dir, cmp, opts.baseline_model_id)

    if opts.oneshot:
        prefix = _job_output_prefix(job)
        _safe_print("  [dim]Running 1-shot (legacy) extraction for comparison…[/dim]")
        os_out, os_dur, os_err, os_log, os_dir, _os_at = _run_full_extraction(
            job.arxiv_id,
            job.model,
            job.paper_text,
            job.structured_tables,
            latex_paper=job.latex_paper,
            paper_title=job.paper_title,
            output_prefix=prefix,
            endpoint=job.endpoint,
            api_key=job.api_key,
            experiment_label=_compare_experiment_label(job.model, oneshot=True),
            extraction_strategy="full",
        )
        if os_err or os_out is None:
            _safe_print(f"  [red]✗ 1-shot FAILED:[/red] {os_err}")
        else:
            os_cmp = _compare(
                job.arxiv_id,
                job.model,
                baseline,
                os_out,
                os_log,
                opts.db_primary_metrics,
            )
            os_cmp.source = "fresh"
            os_cmp.artifact_path = os_dir
            if os_dir is not None:
                _write_comparison_json(os_dir, os_cmp, opts.baseline_model_id)
            _safe_print(
                f"  [dim]1-shot:[/dim]  "
                f"hits=[green]{os_cmp.hits}[/green]  "
                f"val_err=[yellow]{os_cmp.value_errors}[/yellow]  "
                f"miss=[red]{os_cmp.misses}[/red]  "
                f"halluc=[magenta]{os_cmp.hallucinations}[/magenta]  "
                f"recall=[bold]{_pct(os_cmp.recall)}[/bold]  "
                f"prec=[bold]{_pct(os_cmp.precision)}[/bold]  "
                f"[dim]{os_dur:.1f}s[/dim]"
            )

    if opts.log_dir and call_log:
        safe_model = job.model.replace("/", "_")
        log_path = opts.log_dir / f"{safe_model}__{job.arxiv_id}.md"
        md = _render_log_markdown(job.arxiv_id, job.model, call_log, cmp)
        log_path.write_text(md, encoding="utf-8")
        _safe_print(f"  [bold green]Log saved →[/bold green] {log_path}")

    return cmp


def _store_compare_extraction_result(
    extraction: _CompareExtractionResult,
    opts: _ProcessOptions,
    *,
    pending: list[_CompareExtractionResult],
    results: list[PaperComparison],
) -> None:
    """Write comparison artifacts as soon as the baseline for this paper is available."""
    job = extraction.job
    needs_baseline = extraction.out is not None and not extraction.error
    if needs_baseline and not _baseline_for_paper(
        job.arxiv_id,
        opts.baseline_model_id,
        opts.baseline_ctx,
    ):
        pending.append(extraction)
        return
    results.append(_finalize_compare_result(extraction, opts))


def _flush_pending_for_paper(
    arxiv_id: str,
    opts: _ProcessOptions,
    *,
    pending: list[_CompareExtractionResult],
    results: list[PaperComparison],
) -> None:
    """Finalize compare results that were waiting on a baseline for *arxiv_id*."""
    if not pending:
        return
    still_pending: list[_CompareExtractionResult] = []
    for extraction in pending:
        if extraction.job.arxiv_id == arxiv_id:
            results.append(_finalize_compare_result(extraction, opts))
        else:
            still_pending.append(extraction)
    pending[:] = still_pending


def _run_experiment_jobs(
    baseline_jobs: list[_BaselineJob],
    compare_jobs: list[CompareJob],
    cached_extractions: list[_CompareExtractionResult],
    opts: _ProcessOptions,
    *,
    sequential: bool,
    workers: int,
) -> list[PaperComparison]:
    """Run baseline and model extractions; persist each result as soon as it is ready."""
    ctx = opts.baseline_ctx or _BaselineContext()
    opts.baseline_ctx = ctx

    pool: list[tuple[str, _BaselineJob | CompareJob]] = [("baseline", job) for job in baseline_jobs]
    for job in compare_jobs:
        pool.append(("compare", job))

    total_jobs = len(pool)
    if total_jobs == 0 and not cached_extractions:
        return []

    results: list[PaperComparison] = []
    pending: list[_CompareExtractionResult] = []
    for cached in cached_extractions:
        _store_compare_extraction_result(cached, opts, pending=pending, results=results)

    if sequential:
        for job_index, (kind, job) in enumerate(pool, 1):
            if kind == "baseline":
                baseline_job = job  # type: ignore[assignment]
                _process_baseline_job(baseline_job, job_index, total_jobs, ctx)
                _flush_pending_for_paper(
                    baseline_job.arxiv_id,
                    opts,
                    pending=pending,
                    results=results,
                )
            else:
                extraction = _process_compare_extraction(
                    job, opts, job_index, total_jobs  # type: ignore[arg-type]
                )
                _store_compare_extraction_result(
                    extraction,
                    opts,
                    pending=pending,
                    results=results,
                )
    else:
        worker_count = max(1, min(workers, total_jobs))
        baseline_count = len(baseline_jobs)
        compare_count = len(compare_jobs)
        _safe_print(
            f"[dim]Running {total_jobs} job(s) in parallel with {worker_count} worker(s): "
            f"{baseline_count} baseline, {compare_count} extraction[/dim]\n"
        )

        with ThreadPoolExecutor(max_workers=worker_count) as executor:
            baseline_futures: list[Any] = []
            baseline_future_to_arxiv: dict[Any, str] = {}
            compare_futures: list[Any] = []
            for job_index, (kind, job) in enumerate(pool, 1):
                if kind == "baseline":
                    baseline_job = job  # type: ignore[assignment]
                    future = executor.submit(
                        _process_baseline_job,
                        baseline_job,
                        job_index,
                        total_jobs,
                        ctx,
                    )
                    baseline_futures.append(future)
                    baseline_future_to_arxiv[future] = baseline_job.arxiv_id
                else:
                    compare_futures.append(
                        executor.submit(
                            _process_compare_extraction,
                            job,
                            opts,
                            job_index,
                            total_jobs,
                        )
                    )

            for future in as_completed(baseline_futures + compare_futures):
                if future in baseline_future_to_arxiv:
                    future.result()
                    _flush_pending_for_paper(
                        baseline_future_to_arxiv[future],
                        opts,
                        pending=pending,
                        results=results,
                    )
                else:
                    extraction = future.result()
                    _store_compare_extraction_result(
                        extraction,
                        opts,
                        pending=pending,
                        results=results,
                    )

    if pending:
        _safe_rule("[bold]Scoring remaining extractions against baseline[/bold]")
        for extraction in pending:
            results.append(_finalize_compare_result(extraction, opts))
        pending.clear()

    return results


def _load_paper_inputs(arxiv_id: str) -> tuple[str, list, Any]:
    """Load paper content.  Returns (paper_text, structured_tables, latex_paper).

    Priority:
      1. LaTeX source (best: all tables incl. appendix, section-aware text)
      2. HTML (structured tables + clean text)
      3. text.txt (PDF-extracted plain text, poorest for table extraction)
    """
    from backend.latex_source import download_and_parse as latex_download
    from backend.paper_storage import PaperStorage

    storage = PaperStorage(arxiv_id)
    structured_tables: list = []
    paper_text = ""
    latex_paper = None

    if storage.html_index_path.exists():
        from backend.html_parser import parse_html_paper

        parsed = parse_html_paper(storage.html_index_path)
        paper_text = parsed.full_text
        structured_tables = list(parsed.tables)
    elif storage.text_path.exists():
        paper_text = storage.text_path.read_text(encoding="utf-8", errors="replace")

    # Always try LaTeX source; it augments/replaces structured_tables
    try:
        latex_paper = latex_download(arxiv_id, storage.latex_dir)
    except Exception as exc:
        logger.warning("LaTeX source load failed for %s: %s", arxiv_id, exc)

    return paper_text, structured_tables, latex_paper


def _load_extraction_context(
    arxiv_id: str,
    paper_text: str,
    structured_tables: list,
    latex_paper: Any,
    paper_title: str,
) -> tuple[str, str, list, list[dict], str, str]:
    """Return (paper_text, tables_text, structured_tables, figures_list, title, abstract)."""
    from backend.paper_storage import PaperStorage as _PS

    storage = _PS(arxiv_id)
    figures_list: list[dict] = []
    tables_text = ""

    if latex_paper is not None:
        if not paper_text and storage.text_path.exists():
            paper_text = storage.text_path.read_text(encoding="utf-8") or paper_text
    elif storage.html_index_path.exists():
        from backend.html_parser import parse_html_paper

        parsed = parse_html_paper(storage.html_index_path)
        if not paper_text:
            paper_text = parsed.full_text
        if not structured_tables:
            structured_tables = list(parsed.tables)
        tables_text = "\n\n".join(t.markdown for t in parsed.tables)
        figures_list = [
            {"caption": f.caption, "src": f.src, "element_id": f.element_id} for f in parsed.figures
        ]
        if (not paper_title or paper_title.startswith("arXiv:")) and parsed.title:
            paper_title = parsed.title
    elif structured_tables:
        tables_text = "\n\n".join(
            f"[{getattr(t, 'caption', '') or ''}]\n{getattr(t, 'markdown', str(t))}"
            for t in structured_tables
        )

    paper_abstract = ""
    if storage.metadata_path.exists():
        try:
            meta = json.loads(storage.metadata_path.read_text(encoding="utf-8"))
            paper_abstract = str(meta.get("abstract") or "").strip()
        except (OSError, json.JSONDecodeError):
            pass

    return paper_text, tables_text, structured_tables, figures_list, paper_title, paper_abstract


def _run_full_extraction(
    arxiv_id: str,
    model_name: str,
    paper_text: str,
    structured_tables: list,
    latex_paper: Any = None,
    paper_title: str = "",
    output_prefix: str = "",
    *,
    endpoint: str | None = None,
    api_key: str | None = None,
    experiment_label: str | None = None,
    extraction_strategy: str = "auto",
    known_datasets: list[DatasetInfo] | None = None,
    extraction_only: bool = False,
) -> tuple[
    ExtractionOutput | None,
    float,
    str | None,
    list[CallRecord],
    Path | None,
    str | None,
]:
    """Run full process_paper extraction (same persistence as run_manual)."""
    (
        paper_text,
        tables_text,
        structured_tables,
        figures_list,
        paper_title,
        paper_abstract,
    ) = _load_extraction_context(arxiv_id, paper_text, structured_tables, latex_paper, paper_title)

    extractor = LLMExtractor.__new__(LLMExtractor)
    extractor.model_name = model_name
    extractor.streaming = True
    extractor.result_output_format = _COMPARE_RESULT_OUTPUT_FORMAT
    extractor._call_log = []
    extractor._last_progress_idx = -1
    extractor._client = OpenAI(
        api_key=api_key or cfg.llm_api_key or "none",
        base_url=endpoint or cfg.llm_endpoint or None,
        timeout=cfg.llm_timeout,
    )
    _call_counter: list[int] = [0]

    def _on_call(rec: CallRecord) -> None:
        _call_counter[0] += 1
        _print_call_verbose(rec, _call_counter[0], output_prefix=output_prefix)

    extractor._progress_callback = _on_call

    start = time.perf_counter()
    try:
        output = extractor.process_paper(
            arxiv_id=arxiv_id,
            paper_text=paper_text,
            tables_text=tables_text,
            structured_tables=structured_tables,
            latex_paper=latex_paper,
            figures_list=figures_list,
            paper_title=paper_title,
            paper_abstract=paper_abstract,
            extraction_strategy=extraction_strategy,
            experiment_label=experiment_label,
            known_datasets=known_datasets,
            extraction_only=extraction_only,
        )
        duration = time.perf_counter() - start
        out = _parse_extraction_output(output)
        if out is None:
            return (
                None,
                duration,
                "could not parse extraction output",
                extractor._call_log,
                None,
                None,
            )
        if experiment_label:
            artifact_dir = (
                PaperStorage(arxiv_id).extracted_dir
                / "experiments"
                / _slugify_label(experiment_label)
            )
        else:
            artifact_dir = PaperStorage(arxiv_id).extracted_dir
        return (
            out,
            duration,
            None,
            extractor._call_log,
            artifact_dir,
            output.get("extracted_at"),
        )
    except RateLimitError as exc:
        duration = time.perf_counter() - start
        error_msg = f"RATE_LIMIT_ERROR: {exc.message} (HTTP {exc.status_code})"
        return None, duration, error_msg, extractor._call_log, None, None
    except APIStatusError as exc:
        duration = time.perf_counter() - start
        status = exc.status_code
        if status == 429:
            error_msg = f"RATE_LIMIT_ERROR (HTTP 429): {exc.message}"
        elif status in (401, 403):
            error_msg = f"AUTH_ERROR (HTTP {status}): Invalid or expired API key"
        elif status >= 500:
            error_msg = f"SERVER_ERROR (HTTP {status}): API service may be down"
        else:
            error_msg = f"API_ERROR (HTTP {status}): {exc.message}"
        return None, duration, error_msg, extractor._call_log, None, None
    except APIConnectionError as exc:
        duration = time.perf_counter() - start
        error_msg = f"CONNECTION_ERROR: Could not connect to LLM endpoint — {exc}"
        return None, duration, error_msg, extractor._call_log, None, None
    except Exception as exc:
        duration = time.perf_counter() - start
        exc_type = type(exc).__name__
        error_msg = f"{exc_type}: {str(exc)}"
        return None, duration, error_msg, extractor._call_log, None, None


def _run_discovery_only(
    model_name: str,
    paper_text: str,
    structured_tables: list,
    latex_paper: Any = None,
    output_prefix: str = "",
    *,
    endpoint: str | None = None,
    api_key: str | None = None,
) -> tuple[float, str | None, list[CallRecord]]:
    """Run only the dataset discovery step (Step 1) and return timing."""
    extractor = LLMExtractor.__new__(LLMExtractor)
    extractor.model_name = model_name
    extractor.streaming = True
    extractor.result_output_format = "yaml"
    extractor._call_log = []
    extractor._last_progress_idx = -1
    extractor._client = OpenAI(
        api_key=api_key or cfg.llm_api_key or "none",
        base_url=endpoint or cfg.llm_endpoint or None,
        timeout=cfg.llm_timeout,
    )
    _call_counter: list[int] = [0]

    def _on_call(rec: CallRecord) -> None:
        _call_counter[0] += 1
        _print_call_verbose(rec, _call_counter[0], output_prefix=output_prefix)

    extractor._progress_callback = _on_call

    start = time.perf_counter()
    try:
        if latex_paper is not None:
            extractor.discover_datasets_from_latex(latex_paper)
        elif structured_tables:
            tables_text = "\n\n".join(
                f"[{getattr(t, 'caption', '') or ''}]\n{getattr(t, 'markdown', str(t))}"
                for t in structured_tables
            )
            extractor.discover_datasets(paper_text, tables_text)
        else:
            extractor.discover_datasets(paper_text, "")
        duration = time.perf_counter() - start
        return duration, None, extractor._call_log
    except Exception as exc:
        duration = time.perf_counter() - start
        return duration, str(exc), extractor._call_log


def _normalise_metric(metric: str, dataset_name: str, db_primary: dict[str, str]) -> str:
    """Return the canonical metric name for a (metric, dataset) pair.

    If the DB knows a primary_metric for this dataset and the candidate metric
    is a close variant (case-insensitive, or one is a substring of the other),
    return the DB version so that "macro F1" and "F1" collapse to the same key.
    Otherwise return metric unchanged.
    """
    canonical = db_primary.get(dataset_name.lower())
    if canonical is None:
        return metric
    m_lower = metric.lower().replace(" ", "")
    c_lower = canonical.lower().replace(" ", "")
    if m_lower == c_lower or m_lower in c_lower or c_lower in m_lower:
        return canonical
    return metric


def _compare(
    arxiv_id: str,
    model_name: str,
    baseline: list[dict],
    candidate: ExtractionOutput,
    call_log: list[CallRecord],
    db_primary_metrics: dict[str, str] | None = None,
) -> PaperComparison:
    db_primary: dict[str, str] = db_primary_metrics or {}
    result = PaperComparison(
        arxiv_id=arxiv_id,
        llm_model=model_name,
        baseline_count=len(baseline),
        call_log=call_log,
    )

    baseline_lookup: dict[EntryKey, float] = {}
    for entry in baseline:
        ds = normalize_dataset_alias(entry.get("dataset", ""))
        metric = _normalise_metric(entry.get("metric", ""), ds, db_primary)
        key = EntryKey(
            model=entry.get("model", ""),
            dataset=ds,
            metric=metric,
        )
        val = entry.get("value")
        if val is not None:
            fval = float(val)
            # Symmetric normalisation: baseline may also contain percentage-scale
            # or dataset-specific-scaled values that were not yet divided.
            fval, _ = normalize_percentage_metric(metric, fval, None)
            fval, _ = normalize_dataset_scaled_metric(ds, metric, fval, None)
            existing = baseline_lookup.get(key)
            if existing is None or fval > existing:
                baseline_lookup[key] = fval

    candidate_lookup: dict[EntryKey, float] = {}
    for entry in candidate.results:
        ds = normalize_dataset_alias(entry.dataset)
        metric = _normalise_metric(entry.metric, ds, db_primary)
        key = EntryKey(model=entry.model, dataset=ds, metric=metric)
        val = entry.value
        # Apply the same percentage/dataset-scale normalisation the parser uses,
        # so that a candidate reporting 53.1 instead of 0.531 is scored as a hit.
        val, _ = normalize_percentage_metric(metric, val, None)
        val, _ = normalize_dataset_scaled_metric(ds, metric, val, None)
        existing = candidate_lookup.get(key)
        if existing is None or val > existing:
            candidate_lookup[key] = val

    for key, bval in baseline_lookup.items():
        if key in candidate_lookup:
            cval = candidate_lookup[key]
            if _values_match(bval, cval):
                result.hits += 1
                result.hit_keys.append({"key": str(key), "baseline": bval, "candidate": cval})
            else:
                result.value_errors += 1
                result.value_error_keys.append(
                    {"key": str(key), "baseline": bval, "candidate": cval}
                )
        else:
            result.misses += 1
            result.miss_keys.append({"key": str(key), "baseline_value": bval})

    for key, cval in candidate_lookup.items():
        if key not in baseline_lookup:
            result.hallucinations += 1
            result.hallucinated_keys.append({"key": str(key), "candidate_value": cval})

    return result


def _ratio_near(a: float, b: float, factor: float, rel_tol: float = 0.05) -> bool:
    if b == 0:
        return False
    scaled = b * factor
    return abs(a - scaled) <= max(ABS_TOL, abs(scaled) * rel_tol)


def _classify_comparison_errors(
    cmp: PaperComparison,
    call_log: list[CallRecord],
) -> dict[str, Any]:
    """Heuristic root-cause tags for misses, value errors, and hallucinations."""
    empty_extract_calls = 0
    truncated_context_calls = 0
    truncated_completion_calls = 0
    regex_parse_calls = 0
    for rec in call_log:
        if not rec.call_type.startswith("extract_dataset"):
            continue
        parsed = rec.parsed_result
        if isinstance(parsed, dict) and not parsed.get("results"):
            empty_extract_calls += 1
        rag = rec.extra.get("rag") or {}
        if rag.get("rag_text_truncated") or rag.get("tables_truncated"):
            truncated_context_calls += 1
        if rec.extra.get("completion_truncated"):
            truncated_completion_calls += 1
        parse_method = rec.extra.get("structured_parse_method") or rec.extra.get(
            "json_parse_method"
        )
        if parse_method in {"json_regex", "lenient_repair"}:
            regex_parse_calls += 1

    scale_value_errors: list[dict] = []
    for item in cmp.value_error_keys:
        bval = float(item["baseline"])
        cval = float(item["candidate"])
        tags: list[str] = []
        if _ratio_near(cval, bval, 100.0) or _ratio_near(cval, bval, 0.01):
            tags.append("E_scale_normalization")
        scale_value_errors.append({**item, "tags": tags})

    name_variant_hallucinations = 0
    for hall in cmp.hallucinated_keys:
        hkey = str(hall["key"]).lower()
        hval = float(hall["candidate_value"])
        for miss in cmp.miss_keys:
            mkey = str(miss["key"]).lower()
            mval = float(miss["baseline_value"])
            if _values_match(mval, hval) and mkey != hkey:
                name_variant_hallucinations += 1
                break

    return {
        "empty_extract_calls": empty_extract_calls,
        "truncated_context_calls": truncated_context_calls,
        "truncated_completion_calls": truncated_completion_calls,
        "regex_parse_calls": regex_parse_calls,
        "scale_value_errors": scale_value_errors,
        "name_variant_hallucination_pairs": name_variant_hallucinations,
        "miss_count": cmp.misses,
        "value_error_count": cmp.value_errors,
        "hallucination_count": cmp.hallucinations,
    }


def _print_error_classification(classification: dict[str, Any]) -> None:
    _safe_print("  [dim]Error classification:[/dim]")
    _safe_print(
        f"    empty extract calls={classification['empty_extract_calls']}  "
        f"truncated context={classification['truncated_context_calls']}  "
        f"truncated completion={classification['truncated_completion_calls']}  "
        f"regex/lenient parse={classification['regex_parse_calls']}"
    )
    if classification["name_variant_hallucination_pairs"]:
        _safe_print(
            f"    name-variant pairs (miss+halluc same value)="
            f"{classification['name_variant_hallucination_pairs']}"
        )
    scale_tags = [item for item in classification["scale_value_errors"] if item.get("tags")]
    if scale_tags:
        _safe_print(f"    scale-like value errors={len(scale_tags)}")


def _normalize_disagreement_key(key: str) -> str:
    """Normalize result keys for cross-model comparison."""
    return key.replace("poked", "pokec").strip().lower()


def _comparison_disagreement_sets(
    cmp: PaperComparison,
) -> tuple[dict[str, float], dict[str, float]]:
    misses = {
        _normalize_disagreement_key(item["key"]): float(item["baseline_value"])
        for item in cmp.miss_keys
    }
    hallucinations = {
        _normalize_disagreement_key(item["key"]): float(item["candidate_value"])
        for item in cmp.hallucinated_keys
    }
    return misses, hallucinations


def _looks_like_ablation_row(key: str) -> bool:
    lowered = key.lower()
    return "(-)" in lowered or "ablation" in lowered or " w/o " in lowered


def analyze_multi_model_baseline(
    paper_results: list[PaperComparison],
) -> dict[str, Any] | None:
    """Cross-model disagreement analysis when >=2 models ran on the same paper.

    Inspection rules (GLM baseline is fallible):
      - Both models miss the same key → GLM likely over-extracted (ablations etc.)
      - Both models hallucinate the same key → GLM likely missed a real table row
      - Model-only miss → GLM likely correct; that model under-extracted
      - Model-only hallucination → model-specific false positive or naming variant
    """
    ok = [r for r in paper_results if r.error is None]
    if len(ok) < 2:
        return None

    models = [r.llm_model for r in ok]
    baseline_count = ok[0].baseline_count

    model_misses: dict[str, dict[str, float]] = {}
    model_hallucinations: dict[str, dict[str, float]] = {}
    for result in ok:
        misses, hallucinations = _comparison_disagreement_sets(result)
        model_misses[result.llm_model] = misses
        model_hallucinations[result.llm_model] = hallucinations

    miss_sets = [set(data.keys()) for data in model_misses.values()]
    hallucination_sets = [set(data.keys()) for data in model_hallucinations.values()]
    both_miss = set.intersection(*miss_sets) if miss_sets else set()
    both_hallucinate = set.intersection(*hallucination_sets) if hallucination_sets else set()

    both_miss_ablation_like = sorted(key for key in both_miss if _looks_like_ablation_row(key))

    per_model_only: dict[str, dict[str, Any]] = {}
    adjusted_metrics: dict[str, dict[str, Any]] = {}
    for result in ok:
        model = result.llm_model
        only_misses = sorted(key for key in model_misses[model] if key not in both_miss)
        only_hallucinations = sorted(
            key for key in model_hallucinations[model] if key not in both_hallucinate
        )
        per_model_only[model] = {
            "misses": only_misses,
            "misses_count": len(only_misses),
            "hallucinations": only_hallucinations,
            "hallucinations_count": len(only_hallucinations),
        }

        glm_likely_over_extracted = len(both_miss)
        glm_likely_missed = len(both_hallucinate)
        effective_hits = result.hits + glm_likely_missed
        effective_baseline = max(baseline_count - glm_likely_over_extracted, 1)
        extracted = result.hits + result.value_errors + result.hallucinations
        adjusted_metrics[model] = {
            "raw_recall": round(result.recall, 4),
            "adjusted_recall": round(effective_hits / effective_baseline, 4),
            "raw_precision": round(result.precision, 4),
            "adjusted_precision": round(effective_hits / max(extracted, 1), 4),
            "glm_likely_over_extracted": glm_likely_over_extracted,
            "glm_likely_missed": glm_likely_missed,
            "model_only_misses": len(only_misses),
            "model_only_hallucinations": len(only_hallucinations),
        }

    return {
        "models": models,
        "baseline_count": baseline_count,
        "both_models_miss": {
            "count": len(both_miss),
            "ablation_like_count": len(both_miss_ablation_like),
            "interpretation": (
                "GLM likely over-extracted or rows both models correctly skipped "
                "(e.g. ablations)"
            ),
            "keys": [
                {
                    "key": key,
                    "ablation_like": _looks_like_ablation_row(key),
                    "baseline_values": {model: model_misses[model].get(key) for model in models},
                }
                for key in sorted(both_miss)
            ],
        },
        "both_models_hallucinate": {
            "count": len(both_hallucinate),
            "interpretation": "Strong signal GLM baseline missed real table rows",
            "keys": [
                {
                    "key": key,
                    "candidate_values": {
                        model: model_hallucinations[model].get(key) for model in models
                    },
                }
                for key in sorted(both_hallucinate)
            ],
        },
        "per_model_only": per_model_only,
        "adjusted_metrics": adjusted_metrics,
    }


def _print_multi_model_baseline_analysis(
    arxiv_id: str,
    analysis: dict[str, Any],
) -> None:
    _safe_print()
    _safe_print(
        f"[bold]Baseline quality analysis[/bold] — {arxiv_id} " f"({', '.join(analysis['models'])})"
    )
    both_miss = analysis["both_models_miss"]
    both_hall = analysis["both_models_hallucinate"]
    _safe_print(
        f"  both miss={both_miss['count']} "
        f"(ablation-like={both_miss['ablation_like_count']}) → "
        f"[dim]{both_miss['interpretation']}[/dim]"
    )
    _safe_print(
        f"  both hallucinate={both_hall['count']} → " f"[dim]{both_hall['interpretation']}[/dim]"
    )
    for model, metrics in analysis["adjusted_metrics"].items():
        _safe_print(
            f"  [cyan]{model}[/cyan]: "
            f"recall {metrics['raw_recall']:.0%} → "
            f"[bold]{metrics['adjusted_recall']:.0%}[/bold] adj  "
            f"prec {metrics['raw_precision']:.0%} → "
            f"[bold]{metrics['adjusted_precision']:.0%}[/bold] adj  "
            f"only-miss={metrics['model_only_misses']}  "
            f"only-halluc={metrics['model_only_hallucinations']}"
        )


def _collect_baseline_quality_analyses(
    all_results: list[PaperComparison],
) -> dict[str, dict[str, Any]]:
    by_paper: dict[str, list[PaperComparison]] = {}
    for result in all_results:
        by_paper.setdefault(result.arxiv_id, []).append(result)

    analyses: dict[str, dict[str, Any]] = {}
    for arxiv_id, paper_results in sorted(by_paper.items()):
        analysis = analyze_multi_model_baseline(paper_results)
        if analysis is not None:
            analyses[arxiv_id] = analysis
            _print_multi_model_baseline_analysis(arxiv_id, analysis)
    return analyses


def _fetch_db_primary_metrics() -> dict[str, str]:
    """Return {dataset_name_lower: primary_metric} from the local DB.

    Used to normalise metric names across models (e.g. "macro F1" → "F1").
    Returns an empty dict if the DB is not initialised or the table is empty.
    """
    try:
        from backend.db import get_session_factory
        from backend.models import Dataset

        Session = get_session_factory()
        with Session() as session:
            rows = session.query(Dataset.name, Dataset.primary_metric).all()
        return {name.lower(): pm for name, pm in rows if pm}
    except Exception as exc:
        logger.debug("Could not load DB primary metrics: %s", exc)
        return {}


def _find_papers_with_baseline() -> list[str]:
    accepted = {cfg.model_fallback, LEGACY_COMPARE_BASELINE}
    ids = []
    for p in sorted(cfg.papers_dir.iterdir()):
        if not p.is_dir():
            continue
        yaml_path = p / "extracted" / "llm_output.yaml"
        json_path = p / "extracted" / "llm_output.json"
        path = yaml_path if yaml_path.exists() else json_path
        if not path.exists():
            continue
        try:
            text = path.read_text(encoding="utf-8")
            data = yaml.safe_load(text) if path.suffix == ".yaml" else json.loads(text)
            if data.get("model_used") in accepted:
                ids.append(p.name)
        except (OSError, json.JSONDecodeError, yaml.YAMLError):
            pass
    return ids


# ── Verbose console printing ──────────────────────────────────────────────────


def _print_call_verbose(
    rec: CallRecord,
    call_index: int,
    total_calls: int | None = None,
    *,
    output_prefix: str = "",
) -> None:
    """Print a rich-formatted summary of one LLM call."""
    prefix = f"[dim]{output_prefix}[/dim] " if output_prefix else ""
    # ── Header line ────────────────────────────────────────────────────
    ttft_str = f"TTFT {rec.ttft_s:.2f}s  " if rec.ttft_s is not None else ""
    tps_str = f"{rec.tokens_per_sec:.0f} tok/s  " if rec.tokens_per_sec else ""
    tok_str = ""
    if rec.prompt_tokens or rec.completion_tokens:
        tok_str = (
            f"prompt={rec.prompt_tokens or '?'}  " f"completion={rec.completion_tokens or '?'}  "
        )
    status = (
        "[yellow]⚠[/yellow]"
        if rec.parse_error
        else ("[green]✓[/green]" if rec.success else "[red]✗[/red]")
    )
    call_label = f"Call {call_index}" if total_calls is None else f"Call {call_index}/{total_calls}"
    _safe_print(
        f"  {prefix}{status} {call_label} "
        f"[bold cyan]{rec.call_type}[/bold cyan]  "
        f"in={rec.input_chars:,} chars  "
        f"out={rec.output_chars:,} chars  "
        f"{ttft_str}{tps_str}{tok_str}"
        f"[dim]{rec.duration_s:.1f}s total[/dim]"
    )

    # ── Discovered datasets (discovery calls) ─────────────────────────────
    discovered = rec.extra.get("discovered_datasets")
    if discovered is not None:
        if discovered:
            _safe_print(
                f"    {prefix}[dim]Datasets:[/dim] "
                + "  ".join(f"[bold]{d}[/bold]" for d in discovered)
            )
        else:
            _safe_print(f"    {prefix}[yellow]No datasets discovered[/yellow]")

    # ── Table selection (select_tables calls) ─────────────────────────────
    # Single-dataset form (legacy): selected_tables = [1, 3, 5]
    sel_tables = rec.extra.get("selected_tables")
    if sel_tables is not None:
        total_t = rec.extra.get("tables_total", "?")
        _safe_print(
            f"    {prefix}[dim]Tables selected:[/dim] {sel_tables} "
            f"[dim]({len(sel_tables)}/{total_t})[/dim]"
        )
    # Multi-dataset form: selected_tables_per_dataset = {"DS-A": [1,3], "DS-B": [3]}
    sel_multi = rec.extra.get("selected_tables_per_dataset")
    if sel_multi is not None:
        total_t = rec.extra.get("tables_total", "?")
        for ds_name, nums in sel_multi.items():
            _safe_print(
                f"    {prefix}[dim]Tables for[/dim] [bold]{ds_name}[/bold][dim]:[/dim] "
                f"{nums} [dim]({len(nums)}/{total_t})[/dim]"
            )

    # ── RAG stats (for extract_dataset calls) ─────────────────────────────
    rag = rec.extra.get("rag")
    if rag:
        mode_color = "green" if rag["table_selection_mode"] == "caption_match" else "yellow"
        _safe_print(
            f"    {prefix}[dim]RAG:[/dim] "
            f"paragraphs {rag['paragraphs_selected']}/{rag['paragraphs_total']}  "
            f"tables {rag['tables_selected']}/{rag['tables_total']} "
            f"([{mode_color}]{rag['table_selection_mode']}[/{mode_color}])"
        )
        if rag.get("selected_table_captions"):
            for cap in rag["selected_table_captions"][:3]:
                _safe_print(f"      {prefix}[dim]↳ {cap}[/dim]")
            if len(rag["selected_table_captions"]) > 3:
                _safe_print(
                    f"      {prefix}[dim]↳ … +{len(rag['selected_table_captions']) - 3} more[/dim]"
                )

    # ── JSON parse method note ─────────────────────────────────────────────
    if rec.extra.get("json_parse_method") == "regex":
        _safe_print(f"    {prefix}[yellow]⚠ JSON extracted via regex fallback[/yellow]")
    if rec.parse_error:
        _safe_print(f"    {prefix}[red]⚠ Parse error: {rec.parse_error[:120]}[/red]")


def _print_call_full_prompt(rec: CallRecord) -> None:
    """Print the full system prompt and user content for one call."""
    console.print()
    console.rule(f"[dim]SYSTEM PROMPT ({len(rec.system_prompt)} chars)[/dim]", style="dim")
    console.print(Syntax(rec.system_prompt, "text", word_wrap=True, theme="monokai"))
    console.rule(f"[dim]USER CONTENT ({len(rec.user_content)} chars)[/dim]", style="dim")
    console.print(Syntax(rec.user_content, "text", word_wrap=True, theme="monokai"))
    console.rule(f"[dim]RAW RESPONSE ({len(rec.raw_response)} chars)[/dim]", style="dim")
    console.print(Syntax(rec.raw_response, "text", word_wrap=True, theme="monokai"))


# ── Markdown log generation ───────────────────────────────────────────────────


def _render_log_markdown(
    arxiv_id: str,
    model_name: str,
    call_log: list[CallRecord],
    comparison: PaperComparison | None,
) -> str:
    """Render a full conversation log as Markdown."""
    lines: list[str] = []
    now = datetime.now(UTC).strftime("%Y-%m-%d %H:%M UTC")

    lines.append(f"# Conversation Log: `{model_name}` on `{arxiv_id}`")
    lines.append(f"*Generated: {now}*")
    lines.append("")

    # ── Summary ───────────────────────────────────────────────────────────
    if comparison:
        lines.append("## Summary")
        lines.append("")
        lines.append("| Metric | Value |")
        lines.append("|--------|-------|")
        lines.append(f"| Baseline entries | {comparison.baseline_count} |")
        lines.append(f"| Hits | {comparison.hits} |")
        lines.append(f"| Value errors | {comparison.value_errors} |")
        lines.append(f"| Misses | {comparison.misses} |")
        lines.append(f"| Hallucinations | {comparison.hallucinations} |")
        lines.append(f"| Recall | {comparison.recall * 100:.0f}% |")
        lines.append(f"| Precision | {comparison.precision * 100:.0f}% |")
        lines.append(f"| Total time | {comparison.duration_s:.1f}s |")
        lines.append("")

        if comparison.miss_keys:
            lines.append("### Missed entries (in baseline, not extracted)")
            lines.append("")
            for m in comparison.miss_keys:
                lines.append(f"- `{m['key']}` (baseline value: {m['baseline_value']})")
            lines.append("")

        if comparison.value_error_keys:
            lines.append("### Value errors (found but wrong number)")
            lines.append("")
            for v in comparison.value_error_keys:
                lines.append(
                    f"- `{v['key']}`  baseline={v['baseline']}  candidate={v['candidate']}"
                )
            lines.append("")

        if comparison.hallucinated_keys:
            lines.append("### Hallucinations (extracted but not in baseline)")
            lines.append("")
            for h in comparison.hallucinated_keys:
                lines.append(f"- `{h['key']}` (value: {h['candidate_value']})")
            lines.append("")

    # ── Per-call detail ───────────────────────────────────────────────────
    lines.append(f"## Calls ({len(call_log)} total)")
    lines.append("")

    for i, rec in enumerate(call_log, 1):
        ttft_str = f"TTFT={rec.ttft_s:.2f}s  " if rec.ttft_s is not None else ""
        tps_str = f"{rec.tokens_per_sec:.0f} tok/s" if rec.tokens_per_sec else ""
        tok_str = ""
        if rec.prompt_tokens or rec.completion_tokens:
            tok_str = (
                f"  prompt_tokens={rec.prompt_tokens}  "
                f"completion_tokens={rec.completion_tokens}"
            )
        status = "✓" if rec.success else "✗ FAILED"

        lines.append(f"### Call {i}: `{rec.call_type}` {status}")
        lines.append("")
        lines.append(
            f"**Input chars:** {rec.input_chars:,}  "
            f"**Output chars:** {rec.output_chars:,}  "
            f"**Duration:** {rec.duration_s:.1f}s  "
            f"{ttft_str}{tps_str}{tok_str}"
        )
        lines.append("")

        # RAG stats
        rag = rec.extra.get("rag")
        if rag:
            lines.append("**RAG context:**")
            lines.append("")
            lines.append(
                f"- Paragraphs selected: {rag['paragraphs_selected']}/{rag['paragraphs_total']}"
                f" ({rag['rag_text_chars']:,} chars"
                + (" — truncated" if rag.get("rag_text_truncated") else "")
                + ")"
            )
            lines.append(
                f"- Tables: {rag['tables_selected']}/{rag['tables_total']}"
                f" (mode: `{rag['table_selection_mode']}`)"
            )
            if rag.get("selected_table_captions"):
                lines.append("- Selected table captions:")
                for cap in rag["selected_table_captions"]:
                    lines.append(f"  - {cap}")
            lines.append(f"- Total context: {rag['context_total_chars']:,} chars")
            lines.append("")

        if rec.extra.get("json_parse_method") == "regex":
            lines.append("> ⚠️ JSON extracted via regex fallback")
            lines.append("")
        if rec.parse_error:
            lines.append(f"> ⚠️ Parse error: {rec.parse_error[:200]}")
            lines.append("")

        # System prompt
        lines.append("<details>")
        lines.append(f"<summary>System prompt ({len(rec.system_prompt)} chars)</summary>")
        lines.append("")
        lines.append("```text")
        lines.append(rec.system_prompt)
        lines.append("```")
        lines.append("")
        lines.append("</details>")
        lines.append("")

        # User content
        lines.append("<details>")
        lines.append(f"<summary>User content ({len(rec.user_content)} chars)</summary>")
        lines.append("")
        lines.append("```text")
        lines.append(rec.user_content)
        lines.append("```")
        lines.append("")
        lines.append("</details>")
        lines.append("")

        # Raw response
        lines.append("<details>")
        lines.append(f"<summary>Raw response ({len(rec.raw_response)} chars)</summary>")
        lines.append("")
        lines.append("```text")
        lines.append(rec.raw_response if rec.raw_response else "(empty)")
        lines.append("```")
        lines.append("")
        lines.append("</details>")
        lines.append("")

        # Parsed result (compact JSON)
        if rec.parsed_result is not None:
            lines.append("<details>")
            lines.append("<summary>Parsed result (JSON)</summary>")
            lines.append("")
            lines.append("```json")
            lines.append(json.dumps(rec.parsed_result, indent=2, ensure_ascii=False))
            lines.append("```")
            lines.append("")
            lines.append("</details>")
            lines.append("")

        lines.append("---")
        lines.append("")

    return "\n".join(lines)


# ── Formatting ────────────────────────────────────────────────────────────────


def _pct(n: float) -> str:
    return f"{n * 100:.0f}%"


def _format_model_display(model: str, backend: str) -> str:
    if backend == "local":
        return f"[bold green]{model}[/bold green] [green]local[/green]"
    return f"[cyan]{model}[/cyan] [dim]external[/dim]"


def _format_backend_badge(backend: str) -> str:
    if backend == "local":
        return "[bold green]local vLLM[/bold green]"
    return "[cyan]external[/cyan]"


def _print_models_grouped(
    model_ids: list[str], routes: dict[str, ModelRoute], *, title: str
) -> None:
    local_models = [m for m in model_ids if is_local_model(m, routes)]
    external_models = [m for m in model_ids if m in routes and not is_local_model(m, routes)]

    _safe_print(f"\n[bold]{title} ({len(model_ids)}):[/bold]")
    if local_models:
        _safe_print(f"  [bold green]Local[/bold green] ({len(local_models)})")
        for model in local_models:
            _safe_print(f"    [bold green]{model}[/bold green]")
    if external_models:
        _safe_print(f"  [cyan]External[/cyan] ({len(external_models)})")
        for model in external_models:
            _safe_print(f"    [cyan]{model}[/cyan]")
    if not local_models and not external_models:
        for model in model_ids:
            _safe_print(f"  {model}")


def _summary_model_sort_key(model: str, rows: list[PaperComparison]) -> tuple[int, float]:
    backend = rows[0].backend if rows else "external"
    papers_ok = [r for r in rows if r.error is None]
    avg_recall = -sum(r.recall for r in papers_ok) / max(len(papers_ok), 1)
    return (0 if backend == "local" else 1, avg_recall)


def _render_summary_table(all_results: list[PaperComparison], *, baseline_model_id: str) -> None:
    by_model: dict[str, list[PaperComparison]] = {}
    for r in all_results:
        by_model.setdefault(r.llm_model, []).append(r)

    table = Table(
        title=f"Model Extraction Quality vs {baseline_model_id} Baseline",
        box=box.ROUNDED,
        show_lines=True,
    )
    table.add_column("Model", style="cyan", no_wrap=True)
    table.add_column("Papers", justify="right")
    table.add_column("Baseline\nEntries", justify="right")
    table.add_column("Hits", justify="right", style="green")
    table.add_column("Val\nErrors", justify="right", style="yellow")
    table.add_column("Misses", justify="right", style="red")
    table.add_column("Halluci-\nnations", justify="right", style="magenta")
    table.add_column("Recall", justify="right")
    table.add_column("Precision", justify="right")
    table.add_column("Halluc.\nRate", justify="right")
    table.add_column("Source", justify="left")
    table.add_column("Avg\nTime", justify="right", style="dim")

    model_order = sorted(
        by_model.keys(),
        key=lambda m: _summary_model_sort_key(m, by_model[m]),
    )

    for model in model_order:
        rows = by_model[model]
        backend = rows[0].backend if rows else "external"
        model_label = _format_model_display(model, backend)
        papers_ok = [r for r in rows if r.error is None]
        n_papers = len(papers_ok)
        if n_papers == 0:
            error_msg = (rows[0].error or "unknown") if rows else "unknown"
            table.add_row(
                model_label,
                str(len(rows)),
                "—",
                "—",
                "—",
                "—",
                "—",
                "—",
                "—",
                "—",
                "—",
                f"[red]{error_msg[:40]}[/red]",
            )
            continue

        total_baseline = sum(r.baseline_count for r in papers_ok)
        total_hits = sum(r.hits for r in papers_ok)
        total_val_err = sum(r.value_errors for r in papers_ok)
        total_misses = sum(r.misses for r in papers_ok)
        total_halluc = sum(r.hallucinations for r in papers_ok)
        avg_recall = sum(r.recall for r in papers_ok) / n_papers
        avg_precision = sum(r.precision for r in papers_ok) / n_papers
        avg_halluc = sum(r.hallucination_rate for r in papers_ok) / n_papers
        avg_time = sum(r.duration_s for r in papers_ok) / n_papers
        fresh_n = sum(1 for r in papers_ok if r.source == "fresh")
        cached_n = sum(1 for r in papers_ok if r.source == "cached")
        auto_n = sum(1 for r in papers_ok if r.source == "auto_included")
        if auto_n == n_papers:
            source_summary = "[auto-included]"
        elif cached_n == n_papers:
            source_summary = "all cached"
        elif fresh_n == n_papers:
            source_summary = "all fresh"
        else:
            parts = []
            if fresh_n:
                parts.append(f"{fresh_n} fresh")
            if cached_n:
                parts.append(f"{cached_n} cached")
            if auto_n:
                parts.append(f"{auto_n} auto")
            source_summary = ", ".join(parts)

        table.add_row(
            model_label,
            str(n_papers),
            str(total_baseline),
            str(total_hits),
            str(total_val_err),
            str(total_misses),
            str(total_halluc),
            _pct(avg_recall),
            _pct(avg_precision),
            _pct(avg_halluc),
            source_summary,
            f"{avg_time:.0f}s",
        )

    console.print(table)


def _job_output_prefix(job: CompareJob) -> str:
    paper = _format_paper_header(job.arxiv_id, job.paper_title)
    backend_tag = "local" if job.backend == "local" else "external"
    return f"{job.model} @ {paper} [{backend_tag}]"


def _print_job_rule(job: CompareJob, job_index: int, total_jobs: int) -> None:
    paper = _format_paper_header(job.arxiv_id, job.paper_title)
    model_label = _format_model_display(job.model, job.backend)
    _safe_rule(f"[{job_index}/{total_jobs}] {model_label} on [bold]{paper}[/bold]")


@dataclass
class _DiscoveryResult:
    model: str
    backend: str
    arxiv_id: str
    paper_title: str
    duration: float
    ttft: float | None
    tps: float | None
    datasets_found: str
    err: str | None


def _process_discovery_job(
    job: CompareJob,
    job_index: int,
    total_jobs: int,
) -> _DiscoveryResult:
    _print_job_rule(job, job_index, total_jobs)
    prefix = _job_output_prefix(job)
    duration, err, call_log = _run_discovery_only(
        job.model,
        job.paper_text,
        job.structured_tables,
        latex_paper=job.latex_paper,
        output_prefix=prefix,
        endpoint=job.endpoint,
        api_key=job.api_key,
    )
    ttft: float | None = None
    tps: float | None = None
    datasets_found = ""
    for rec in call_log:
        if rec.ttft_s is not None:
            ttft = rec.ttft_s
        if rec.tokens_per_sec is not None:
            tps = rec.tokens_per_sec
        ds_list = rec.extra.get("discovered_datasets")
        if ds_list is not None:
            datasets_found = ", ".join(ds_list)
    _safe_print()
    return _DiscoveryResult(
        model=job.model,
        backend=job.backend,
        arxiv_id=job.arxiv_id,
        paper_title=job.paper_title,
        duration=duration,
        ttft=ttft,
        tps=tps,
        datasets_found=datasets_found,
        err=err,
    )


def _run_discovery_jobs(
    jobs: list[CompareJob],
    *,
    sequential: bool,
    workers: int,
) -> list[_DiscoveryResult]:
    total_jobs = len(jobs)
    if total_jobs == 0:
        return []

    if sequential:
        return [_process_discovery_job(job, index, total_jobs) for index, job in enumerate(jobs, 1)]

    worker_count = max(1, min(workers, total_jobs))
    _safe_print(
        f"[dim]Running {total_jobs} discovery job(s) in parallel "
        f"with {worker_count} worker(s)[/dim]\n"
    )
    results: list[_DiscoveryResult | None] = [None] * total_jobs
    with ThreadPoolExecutor(max_workers=worker_count) as pool:
        future_map = {
            pool.submit(_process_discovery_job, job, index, total_jobs): index - 1
            for index, job in enumerate(jobs, 1)
        }
        for future in as_completed(future_map):
            slot = future_map[future]
            results[slot] = future.result()
    return [result for result in results if result is not None]


def _render_per_paper_table(all_results: list[PaperComparison]) -> None:
    table = Table(title="Per-Paper Results", box=box.SIMPLE)
    table.add_column("Paper", style="dim")
    table.add_column("Title")
    table.add_column("Model", style="cyan")
    table.add_column("BL", justify="right")
    table.add_column("Hits", justify="right", style="green")
    table.add_column("ValErr", justify="right", style="yellow")
    table.add_column("Miss", justify="right", style="red")
    table.add_column("Halluc", justify="right", style="magenta")
    table.add_column("Recall", justify="right")
    table.add_column("Source")
    table.add_column("Time", justify="right", style="dim")

    title_cache: dict[str, str] = {}

    for r in sorted(
        all_results,
        key=lambda x: (x.arxiv_id, 0 if x.backend == "local" else 1, x.llm_model),
    ):
        if r.arxiv_id not in title_cache:
            title_cache[r.arxiv_id] = _resolve_paper_title(r.arxiv_id)
        title = _truncate_title(title_cache[r.arxiv_id], max_len=48) or "—"
        model_label = _format_model_display(r.llm_model, r.backend)
        if r.error:
            table.add_row(
                r.arxiv_id,
                title,
                model_label,
                "—",
                "—",
                "—",
                "—",
                "—",
                "—",
                "—",
                "[red]ERR[/red]",
            )
        else:
            time_str = f"{r.duration_s:.0f}s" if r.source == "fresh" else "—"
            table.add_row(
                r.arxiv_id,
                title,
                model_label,
                str(r.baseline_count),
                str(r.hits),
                str(r.value_errors),
                str(r.misses),
                str(r.hallucinations),
                _pct(r.recall),
                _format_source_badge(r.source),
                time_str,
            )
    console.print(table)


# ── Main ──────────────────────────────────────────────────────────────────────


def main(argv: list[str] | None = None) -> int:
    logging.basicConfig(level=logging.WARNING)

    p = argparse.ArgumentParser(
        description="Compare LLM extraction quality against a configured baseline model"
    )
    p.add_argument(
        "--paper",
        nargs="+",
        metavar="ARXIV_ID",
        help="Limit to specific papers (default: all with an on-disk baseline)",
    )
    p.add_argument(
        "--model",
        nargs="+",
        metavar="MODEL",
        help="Test only these models (default: all available minus skip list)",
    )
    p.add_argument(
        "--skip-model",
        nargs="+",
        metavar="MODEL",
        default=[],
        help="Skip these models (added to the built-in skip list)",
    )
    p.add_argument(
        "--include-skipped", action="store_true", help="Also test models in the default skip list"
    )
    p.add_argument("--output", metavar="PATH", help="Save aggregate results to this JSON file")
    p.add_argument(
        "--no-output",
        action="store_true",
        help="Skip writing aggregate JSON (paper artifacts are still saved on full runs)",
    )
    p.add_argument(
        "--force",
        action="store_true",
        help="Re-run LLM extraction for all planned models (ignore on-disk cache)",
    )
    p.add_argument(
        "--log-dir",
        metavar="DIR",
        default=str(_DEFAULT_EXPERIMENT_DIR / "logs"),
        help="Directory to save per-(model,paper) conversation logs as Markdown "
        "(default: experiments/extraction/logs)",
    )
    p.add_argument("--no-logs", action="store_true", help="Disable conversation log file saving")
    p.add_argument(
        "--per-paper", action="store_true", help="Also print a per-paper breakdown table"
    )
    p.add_argument(
        "--show-prompts",
        action="store_true",
        help="Print full system prompts and user content for every call",
    )
    p.add_argument(
        "--oneshot",
        action="store_true",
        help="Also run legacy single-step extraction and compare side-by-side",
    )
    p.add_argument(
        "--classify-errors",
        action="store_true",
        help="Print heuristic root-cause tags for misses and value errors",
    )
    p.add_argument(
        "--discovery-only",
        action="store_true",
        help="Run only Step 1 (dataset discovery) to benchmark model speed/quality "
        "without full extraction (much faster)",
    )
    p.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Show debug logging from the extraction pipeline",
    )
    p.add_argument(
        "--interactive",
        "-i",
        action="store_true",
        help="Interactively select models (and papers unless --paper is given)",
    )
    p.add_argument(
        "--sequential",
        action="store_true",
        help="Process one (model, paper) job at a time (default: parallel)",
    )
    p.add_argument(
        "--workers",
        type=int,
        default=10,
        metavar="N",
        help="Max parallel workers when not using --sequential (default: 10)",
    )
    p.add_argument(
        "--no-ensure-baseline",
        action="store_true",
        help="Skip auto-generating a baseline when one is missing on disk",
    )
    args = p.parse_args(argv)

    if args.verbose:
        logging.getLogger().setLevel(logging.INFO)

    backends = configured_backends()
    if not backends:
        console.print(
            "[red]No LLM backend configured.[/red] "
            "Set [bold]LLM_ENDPOINT[/bold] and/or [bold]LLM_LOCAL_ENDPOINT[/bold] in .env"
        )
        return 1

    console.print("[bold]LLM backends:[/bold]")
    for backend in backends:
        console.print(f"  {_format_backend_badge(backend.label)}  {backend.endpoint}")
    console.print()

    log_dir: Path | None = None
    # Never write logs for discovery-only runs — they produce no extraction output.
    if not args.no_logs and not args.discovery_only:
        log_dir = Path(args.log_dir)
        log_dir.mkdir(parents=True, exist_ok=True)

    # ── Resolve papers ────────────────────────────────────────────────────
    candidate_paper_ids = list(args.paper) if args.paper else _find_papers_with_baseline()
    if not candidate_paper_ids:
        console.print("[yellow]No papers with a stored baseline found.[/yellow]")
        return 0

    if args.interactive and not args.paper:
        console.print(f"\n[bold]Papers with stored baseline ({len(candidate_paper_ids)}):[/bold]")
        paper_choices = [
            (
                pid,
                f"{pid} — {_truncate_title(_resolve_paper_title(pid)) or '(title unknown)'}",
            )
            for pid in candidate_paper_ids
        ]
        picked_papers = _interactive_pick(paper_choices, kind="Paper")
        if picked_papers is None:
            console.print("[yellow]Aborted.[/yellow]")
            return 0
        if not picked_papers:
            console.print("[yellow]No papers selected.[/yellow]")
            return 0
        paper_ids = picked_papers
    else:
        paper_ids = candidate_paper_ids
        console.print("[bold]Papers:[/bold]")
        for pid in paper_ids:
            title = _resolve_paper_title(pid)
            console.print(f"  {pid} — {_truncate_title(title) or '(title unknown)'}")

    # ── Resolve models ────────────────────────────────────────────────────
    console.print("Fetching available models from configured backends…")
    model_routes = fetch_model_routes(backends)
    if not model_routes:
        console.print("[red]No models found on any configured backend.[/red]")
        return 1

    local_count = sum(1 for route in model_routes.values() if route.backend.label == "local")
    external_count = len(model_routes) - local_count
    console.print(
        f"[dim]{len(model_routes)} model(s):[/dim] "
        f"[bold green]{local_count} local[/bold green], "
        f"[cyan]{external_count} external[/cyan]"
    )

    baseline_model_id = resolve_baseline_model_id(model_routes)
    baseline_route = baseline_model_route(model_routes)
    if baseline_route:
        console.print(
            f"[bold]Comparison baseline:[/bold] "
            f"{_format_model_display(baseline_model_id, baseline_route.backend.label)}"
        )
    else:
        console.print(
            f"[bold]Comparison baseline:[/bold] [yellow]{baseline_model_id}[/yellow] "
            f"[red](not available on any backend)[/red]"
        )
    console.print()

    skip_set = set(args.skip_model)
    if not args.include_skipped:
        skip_set |= _DEFAULT_SKIP

    if args.model:
        test_models: list[str] = []
        missing: list[str] = []
        for requested in args.model:
            route = resolve_model_route(requested, model_routes, allow_fallback=True)
            if route is None:
                missing.append(requested)
                continue
            if route.model_id != requested:
                console.print(
                    f"[yellow]{requested!r} not found; using fallback "
                    f"{_format_model_display(route.model_id, route.backend.label)}[/yellow]"
                )
            if route.model_id not in test_models:
                test_models.append(route.model_id)
        if missing:
            console.print(f"[yellow]Models not found on any backend:[/yellow] {missing}")
        test_models = sort_models_local_first(test_models, model_routes)
    else:
        test_models = sort_models_local_first(
            [m for m in model_routes if m not in skip_set],
            model_routes,
        )

    if not test_models:
        console.print("[yellow]No models to test.[/yellow]")
        return 0

    forced_models: set[str] = set()
    force_all = bool(args.force)

    if args.interactive:
        console.print(f"\n[bold]Available models ({len(test_models)}):[/bold]")
        trace_cells = [
            _format_cached_traces_column(
                paper_ids,
                _cached_paper_ids_for_model(model, paper_ids),
            )
            for model in test_models
        ]
        model_choices = [
            (
                model,
                _format_model_display(model, model_routes[model].backend.label),
            )
            for model in test_models
        ]
        traces_header = f"Traces ({paper_ids[0]})" if len(paper_ids) == 1 else "Traces (papers)"
        trace_footer = None
        if any(cell != "[dim]—[/dim]" for cell in trace_cells):
            trace_footer = (
                "[dim]Models with traces reuse cached artifacts; add --force to re-run them.[/dim]"
            )
        picked_models = _interactive_pick(
            model_choices,
            kind="Model",
            extra_columns=[(traces_header, trace_cells)],
            footer=trace_footer,
        )
        if picked_models is None:
            console.print("[yellow]Aborted.[/yellow]")
            return 0
        if not picked_models:
            console.print("[yellow]No models selected.[/yellow]")
            return 0
        test_models = sort_models_local_first(picked_models, model_routes)
    else:
        if not args.model:
            _print_models_grouped(test_models, model_routes, title="Models to test")
            console.print()
            try:
                answer = input("Proceed? [y/N] ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                answer = ""
            if answer not in ("y", "yes"):
                console.print("[yellow]Aborted.[/yellow]")
                return 0
            console.print()
        else:
            labels = [
                _format_model_display(model, model_routes[model].backend.label)
                for model in test_models
            ]
            console.print(f"[bold]Models to test ({len(test_models)}):[/bold] {', '.join(labels)}")
            console.print()

    if log_dir:
        console.print(f"[bold]Log dir:[/bold] {log_dir}")

    sequential = args.sequential or args.show_prompts
    if args.show_prompts and not args.sequential:
        console.print(
            "[yellow]--show-prompts forces sequential processing "
            "(parallel output would be unreadable).[/yellow]"
        )

    workers = max(1, args.workers)
    if not sequential:
        console.print(f"[bold]Processing mode:[/bold] parallel ({workers} workers max)")
    else:
        console.print("[bold]Processing mode:[/bold] sequential")

    ensure_baseline = not args.no_ensure_baseline
    if ensure_baseline and baseline_route is None:
        console.print(
            "[red]Cannot generate baselines: comparison baseline model is not "
            "available on any configured backend.[/red]"
        )
        return 1

    # ── Pre-load paper inputs ─────────────────────────────────────────────
    paper_inputs: dict[str, tuple[str, list, list[dict], Any, str]] = {}
    for pid in paper_ids:
        baseline = _load_baseline(pid, baseline_model_id)
        paper_title = _resolve_paper_title(pid)
        paper_label = _format_paper_header(pid, paper_title)
        if not baseline and not ensure_baseline:
            console.print(
                f"  [yellow]skip[/yellow] {paper_label} — no {baseline_model_id} baseline"
            )
            continue
        paper_text, structured_tables, latex_paper = _load_paper_inputs(pid)
        if not paper_text and not latex_paper:
            console.print(f"  [yellow]skip[/yellow] {paper_label} — no paper text or LaTeX source")
            continue
        paper_inputs[pid] = (paper_text, structured_tables, baseline, latex_paper, paper_title)
        source = "HTML" if structured_tables else ("LaTeX" if latex_paper else "text.txt")
        baseline_note = (
            f"baseline={len(baseline)} entries"
            if baseline
            else "[yellow]baseline will be generated[/yellow]"
        )
        latex_info = (
            (
                f"  [dim]latex: {len(latex_paper.tables)} tables "
                f"({sum(1 for t in latex_paper.tables if t.in_appendix)} appendix), "
                f"{len(latex_paper.experiment_sections)} experiment sections[/dim]"
            )
            if latex_paper
            else ""
        )
        console.print(
            f"  [green]loaded[/green] {paper_label}  "
            f"text={len(paper_text):,} chars  "
            f"tables={len(structured_tables)}  "
            f"{baseline_note}  "
            f"({source})"
        )
        if latex_info:
            console.print(latex_info)

    if not paper_inputs:
        console.print("[red]No valid papers to process.[/red]")
        return 1

    baseline_jobs: list[_BaselineJob] = []
    if ensure_baseline and baseline_route is not None:
        for pid, (
            paper_text,
            structured_tables,
            baseline,
            latex_paper,
            paper_title,
        ) in paper_inputs.items():
            if baseline:
                continue
            baseline_jobs.append(
                _BaselineJob(
                    arxiv_id=pid,
                    paper_title=paper_title,
                    paper_text=paper_text,
                    structured_tables=structured_tables,
                    latex_paper=latex_paper,
                    model=baseline_route.model_id,
                    endpoint=baseline_route.backend.endpoint,
                    api_key=baseline_route.backend.api_key,
                    backend=baseline_route.backend.label,
                )
            )

    console.print()

    baseline_ctx = _BaselineContext()
    _warm_baseline_cache(list(paper_inputs.keys()), baseline_model_id)

    # ── DB lookup: primary metric per dataset name ────────────────────────
    db_primary_metrics = _fetch_db_primary_metrics()
    if db_primary_metrics:
        console.print(
            f"[dim]DB primary metrics loaded for {len(db_primary_metrics)} datasets[/dim]"
        )

    process_opts = _ProcessOptions(
        show_prompts=args.show_prompts,
        oneshot=args.oneshot,
        log_dir=log_dir,
        db_primary_metrics=db_primary_metrics,
        classify_errors=args.classify_errors,
        ensure_baseline=ensure_baseline,
        model_routes=model_routes,
        baseline_model_id=baseline_model_id,
        baseline_ctx=baseline_ctx,
        force_all=force_all,
        forced_models=forced_models,
        persist=not args.discovery_only,
    )

    cached_extractions: list[_CompareExtractionResult] = []
    plan_rows: list[_RunPlanRow] = []
    if args.discovery_only:
        compare_jobs = [
            CompareJob(
                model=model,
                endpoint=model_routes[model].backend.endpoint,
                api_key=model_routes[model].backend.api_key,
                backend=model_routes[model].backend.label,
                arxiv_id=pid,
                paper_title=paper_title,
                paper_text=paper_text,
                structured_tables=structured_tables,
                baseline=baseline,
                latex_paper=latex_paper,
            )
            for model in test_models
            for pid, (paper_text, structured_tables, baseline, latex_paper, paper_title) in (
                paper_inputs.items()
            )
        ]
    else:
        compare_jobs, cached_extractions, plan_rows = _plan_compare_jobs(
            paper_inputs,
            test_models,
            model_routes,
            process_opts,
        )
        _render_run_plan_table(plan_rows, model_routes)
        console.print()

    if args.discovery_only:
        console.rule("[bold]Discovery-Only Speed Benchmark[/bold]")
        disc_rows = _run_discovery_jobs(
            compare_jobs,
            sequential=sequential,
            workers=workers,
        )
        disc_rows.sort(
            key=lambda r: (
                r.err is not None,
                0 if r.backend == "local" else 1,
                -(r.tps or 0),
            )
        )

        disc_table = Table(
            box=box.ROUNDED,
            show_lines=True,
            title="Dataset Discovery Timing (Step 1 only) — local first, then tok/s",
        )
        disc_table.add_column("Model")
        disc_table.add_column("Paper", style="dim")
        disc_table.add_column("Title")
        disc_table.add_column("Time", justify="right")
        disc_table.add_column("TTFT", justify="right")
        disc_table.add_column("tok/s", justify="right", style="bold")
        disc_table.add_column("Datasets found")
        disc_table.add_column("Status")
        for row in disc_rows:
            ttft_str = f"{row.ttft:.2f}s" if row.ttft is not None else "—"
            tps_str = f"{row.tps:.0f}" if row.tps is not None else "—"
            title = _truncate_title(row.paper_title, max_len=48) or "—"
            model_label = _format_model_display(row.model, row.backend)
            if row.err:
                disc_table.add_row(
                    model_label,
                    row.arxiv_id,
                    title,
                    f"{row.duration:.1f}s",
                    ttft_str,
                    tps_str,
                    "—",
                    f"[red]{row.err[:40]}[/red]",
                )
            else:
                disc_table.add_row(
                    model_label,
                    row.arxiv_id,
                    title,
                    f"{row.duration:.1f}s",
                    ttft_str,
                    tps_str,
                    row.datasets_found or "[dim]none[/dim]",
                    "[green]✓[/green]",
                )
        console.print(disc_table)
        return 0

    # ── Run baseline + comparison jobs in one parallel pool ───────────────
    all_results = _run_experiment_jobs(
        baseline_jobs,
        compare_jobs,
        cached_extractions,
        process_opts,
        sequential=sequential,
        workers=workers,
    )

    # ── Print summary tables ──────────────────────────────────────────────
    console.rule("[bold]Final Results[/bold]")
    _render_summary_table(all_results, baseline_model_id=baseline_model_id)

    if args.per_paper:
        console.print()
        _render_per_paper_table(all_results)

    baseline_quality = _collect_baseline_quality_analyses(all_results)

    # ── Save JSON output ──────────────────────────────────────────────────
    out_path: Path | None = None
    if not args.no_output:
        out_path = (
            Path(args.output)
            if args.output
            else (_DEFAULT_EXPERIMENT_DIR / f"{datetime.now(UTC).strftime('%Y%m%dT%H%M%SZ')}.json")
        )
    if out_path is not None:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "run_at": datetime.now(UTC).isoformat(),
            "baseline_model": baseline_model_id,
            "papers": paper_ids,
            "abs_tolerance": ABS_TOL,
            "rel_tolerance": REL_TOL,
            "results": [
                {
                    "arxiv_id": r.arxiv_id,
                    "model": r.llm_model,
                    "baseline_count": r.baseline_count,
                    "hits": r.hits,
                    "value_errors": r.value_errors,
                    "misses": r.misses,
                    "hallucinations": r.hallucinations,
                    "recall": round(r.recall, 4),
                    "precision": round(r.precision, 4),
                    "hallucination_rate": round(r.hallucination_rate, 4),
                    "duration_s": round(r.duration_s, 1),
                    "error": r.error,
                    "source": r.source,
                    "artifact_path": str(r.artifact_path) if r.artifact_path else None,
                    "extracted_at": r.extracted_at,
                    "calls": [
                        {
                            "call_type": c.call_type,
                            "input_chars": c.input_chars,
                            "output_chars": c.output_chars,
                            "duration_s": round(c.duration_s, 2),
                            "ttft_s": round(c.ttft_s, 3) if c.ttft_s else None,
                            "tokens_per_sec": (
                                round(c.tokens_per_sec, 1) if c.tokens_per_sec else None
                            ),
                            "prompt_tokens": c.prompt_tokens,
                            "completion_tokens": c.completion_tokens,
                            "success": c.success,
                            "parse_error": c.parse_error,
                            "rag": c.extra.get("rag"),
                        }
                        for c in r.call_log
                    ],
                    "details": {
                        "hits": r.hit_keys,
                        "value_errors": r.value_error_keys,
                        "misses": r.miss_keys,
                        "hallucinations": r.hallucinated_keys,
                    },
                }
                for r in all_results
            ],
        }
        if baseline_quality:
            payload["baseline_quality_analysis"] = baseline_quality
        out_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
        console.print(f"\nAggregate results saved to [cyan]{out_path}[/cyan]")

    return 0


if __name__ == "__main__":
    sys.exit(main())
