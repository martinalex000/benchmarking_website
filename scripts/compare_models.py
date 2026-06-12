"""Experiment: compare extraction quality of all available LLM models vs GLM 4.7 baseline.

For each paper that has a GLM 4.7 extraction (the ground-truth baseline), this script
runs every available model using the two-step extraction strategy and measures:

  - hits         : (model, dataset, metric) key found AND value within tolerance
  - value_errors : key found but value differs significantly
  - misses        : key in baseline but model failed to find it
  - hallucinations: key found by model but NOT in baseline (invented results)

Usage::

    # Run all models on all papers with a GLM baseline
    python -m scripts.compare_models

    # Limit to specific papers
    python -m scripts.compare_models --paper 2206.08164 2309.00367

    # Limit to specific models
    python -m scripts.compare_models --model gemma-3-27b-it qwen3.5-27b

    # Skip slow/irrelevant models
    python -m scripts.compare_models --skip-model teuken-7b-instruct-research medgemma-27b-it

    # Interactive paper/model selection
    python -m scripts.compare_models --interactive

    # Parallel processing (default); use --sequential for one job at a time
    python -m scripts.compare_models --workers 4

    # Save detailed per-entry results + conversation logs
    python -m scripts.compare_models --output experiments/model_comparison.json \\
                                     --log-dir experiments/logs
"""

from __future__ import annotations

import argparse
import json
import logging
import random
import re
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import yaml

# Allow running from project root without installing
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from openai import APIConnectionError, APIStatusError, OpenAI, RateLimitError
from rich import box
from rich.console import Console
from rich.syntax import Syntax
from rich.table import Table

from backend.config import cfg
from backend.llm_extractor import CallRecord, ExtractionOutput, LLMExtractor

console = Console()
logger = logging.getLogger(__name__)
_console_lock = threading.Lock()

# ── Tolerance for value matching ──────────────────────────────────────────────
ABS_TOL = 0.005
REL_TOL = 0.01  # 1 %

_BASELINE_MODEL = "glm-4.7"

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

    def __hash__(self) -> int:
        return hash((self.model.lower(), self.dataset.lower(), self.metric.lower()))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, EntryKey):
            return NotImplemented
        return (
            self.model.lower() == other.model.lower()
            and self.dataset.lower() == other.dataset.lower()
            and self.metric.lower() == other.metric.lower()
        )

    def __str__(self) -> str:
        return f"{self.model} / {self.dataset} / {self.metric}"


@dataclass
class PaperComparison:
    arxiv_id: str
    llm_model: str
    baseline_count: int
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
    arxiv_id: str
    paper_title: str
    paper_text: str
    structured_tables: list
    baseline: list[dict]
    latex_paper: Any = None


@dataclass
class _ProcessOptions:
    show_prompts: bool = False
    oneshot: bool = False
    log_dir: Path | None = None
    db_primary_metrics: dict[str, str] | None = None


# ── Helpers ───────────────────────────────────────────────────────────────────


def _safe_print(*args: Any, **kwargs: Any) -> None:
    with _console_lock:
        console.print(*args, **kwargs)


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
            from backend.llm_extractor import _extract_metadata_from_latex_cache

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
        from backend.llm_extractor import fetch_arxiv_metadata

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
) -> list[str] | None:
    """Return selected item ids, [] if nothing selected, None to abort."""
    if not items:
        return []

    table = Table(show_header=True, header_style="bold", box=box.SIMPLE, show_edge=False)
    table.add_column("#", style="dim", justify="right", width=4)
    table.add_column(kind, style="cyan")
    for index, (_item_id, label) in enumerate(items, start=1):
        table.add_row(str(index), label)
    _safe_print(table)
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


def _load_baseline(arxiv_id: str) -> list[dict]:
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
    if data.get("model_used") != _BASELINE_MODEL:
        return []
    return data.get("results", {}).get("results", [])


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


def _run_extraction(
    arxiv_id: str,
    model_name: str,
    paper_text: str,
    structured_tables: list,
    latex_paper: Any = None,
    output_prefix: str = "",
) -> tuple[ExtractionOutput | None, float, str | None, list[CallRecord]]:
    """Run extraction with one model; returns (output, duration_s, error, call_log)."""
    extractor = LLMExtractor.__new__(LLMExtractor)
    extractor.model_name = model_name
    extractor.streaming = True  # enables TTFT + tok/s measurement
    extractor.result_output_format = "yaml"
    extractor._call_log = []
    extractor._last_progress_idx = -1
    extractor._client = OpenAI(
        api_key=cfg.llm_api_key or "none",
        base_url=cfg.llm_endpoint or None,
        timeout=cfg.llm_timeout,
    )
    # Print each call's summary live as it completes
    _call_counter: list[int] = [0]

    def _on_call(rec: CallRecord) -> None:
        _call_counter[0] += 1
        _print_call_verbose(rec, _call_counter[0], output_prefix=output_prefix)

    extractor._progress_callback = _on_call

    start = time.perf_counter()
    try:
        out = extractor.extract_results_two_step(
            paper_text, structured_tables, latex_paper=latex_paper
        )
        duration = time.perf_counter() - start
        return out, duration, None, extractor._call_log
    except RateLimitError as exc:
        duration = time.perf_counter() - start
        error_msg = f"RATE_LIMIT_ERROR: {exc.message} (HTTP {exc.status_code})"
        return None, duration, error_msg, extractor._call_log
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
        return None, duration, error_msg, extractor._call_log
    except APIConnectionError as exc:
        duration = time.perf_counter() - start
        error_msg = f"CONNECTION_ERROR: Could not connect to LLM endpoint — {exc}"
        return None, duration, error_msg, extractor._call_log
    except Exception as exc:
        duration = time.perf_counter() - start
        exc_type = type(exc).__name__
        error_msg = f"{exc_type}: {str(exc)}"
        return None, duration, error_msg, extractor._call_log


def _run_oneshot_extraction(
    arxiv_id: str,
    model_name: str,
    paper_text: str,
    structured_tables: list,
    latex_paper: Any = None,
    output_prefix: str = "",
) -> tuple[ExtractionOutput | None, float, str | None, list[CallRecord]]:
    """Run the legacy single-step extraction for comparison."""
    extractor = LLMExtractor.__new__(LLMExtractor)
    extractor.model_name = model_name
    extractor.streaming = True
    extractor.result_output_format = "yaml"
    extractor._call_log = []
    extractor._last_progress_idx = -1
    extractor._client = OpenAI(
        api_key=cfg.llm_api_key or "none",
        base_url=cfg.llm_endpoint or None,
        timeout=cfg.llm_timeout,
    )
    _call_counter: list[int] = [0]

    def _on_call(rec: CallRecord) -> None:
        _call_counter[0] += 1
        _safe_print("  [dim](1-shot)[/dim] ", end="")
        _print_call_verbose(rec, _call_counter[0], output_prefix=output_prefix)

    extractor._progress_callback = _on_call

    # Build tables_text for the 1-shot path
    if latex_paper:
        tables_text = "\n\n".join(
            f"[Caption: {t.caption[:120]}]\n{t.body}" for t in latex_paper.tables
        )
        full_text = paper_text or latex_paper.main_tex[:40_000]
    elif structured_tables:
        tables_text = "\n\n".join(
            f"[{getattr(t, 'caption', '') or ''}]\n{getattr(t, 'markdown', str(t))}"
            for t in structured_tables
        )
        full_text = paper_text
    else:
        tables_text = ""
        full_text = paper_text

    start = time.perf_counter()
    try:
        out = extractor.extract_results(full_text, tables_text)
        duration = time.perf_counter() - start
        return out, duration, None, extractor._call_log
    except Exception as exc:
        duration = time.perf_counter() - start
        return None, duration, str(exc), extractor._call_log


def _run_discovery_only(
    model_name: str,
    paper_text: str,
    structured_tables: list,
    latex_paper: Any = None,
    output_prefix: str = "",
) -> tuple[float, str | None, list[CallRecord]]:
    """Run only the dataset discovery step (Step 1) and return timing."""
    extractor = LLMExtractor.__new__(LLMExtractor)
    extractor.model_name = model_name
    extractor.streaming = True
    extractor.result_output_format = "yaml"
    extractor._call_log = []
    extractor._last_progress_idx = -1
    extractor._client = OpenAI(
        api_key=cfg.llm_api_key or "none",
        base_url=cfg.llm_endpoint or None,
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
        ds = entry.get("dataset", "")
        metric = _normalise_metric(entry.get("metric", ""), ds, db_primary)
        key = EntryKey(
            model=entry.get("model", ""),
            dataset=ds,
            metric=metric,
        )
        val = entry.get("value")
        if val is not None:
            baseline_lookup[key] = float(val)

    candidate_lookup: dict[EntryKey, float] = {}
    for entry in candidate.results:
        metric = _normalise_metric(entry.metric, entry.dataset, db_primary)
        key = EntryKey(model=entry.model, dataset=entry.dataset, metric=metric)
        candidate_lookup[key] = entry.value

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


def _fetch_model_ids(endpoint: str, api_key: str) -> list[str]:
    client = OpenAI(base_url=endpoint, api_key=api_key or "none", timeout=30)
    # Iterate the paged response (not just .data) so all pages are fetched.
    return sorted(m.id for m in client.models.list())


def _find_papers_with_baseline() -> list[str]:
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
            if data.get("model_used") == _BASELINE_MODEL:
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
    status = "[green]✓[/green]" if rec.success else "[red]✗[/red]"
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


def _render_summary_table(all_results: list[PaperComparison]) -> None:
    by_model: dict[str, list[PaperComparison]] = {}
    for r in all_results:
        by_model.setdefault(r.llm_model, []).append(r)

    table = Table(
        title="Model Extraction Quality vs GLM 4.7 Baseline",
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
    table.add_column("Avg\nTime", justify="right", style="dim")

    model_order = sorted(
        by_model.keys(),
        key=lambda m: -sum(r.recall for r in by_model[m]) / max(len(by_model[m]), 1),
    )

    for model in model_order:
        rows = by_model[model]
        papers_ok = [r for r in rows if r.error is None]
        n_papers = len(papers_ok)
        if n_papers == 0:
            error_msg = (rows[0].error or "unknown") if rows else "unknown"
            table.add_row(
                model,
                str(len(rows)),
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

        table.add_row(
            model,
            str(n_papers),
            str(total_baseline),
            str(total_hits),
            str(total_val_err),
            str(total_misses),
            str(total_halluc),
            _pct(avg_recall),
            _pct(avg_precision),
            _pct(avg_halluc),
            f"{avg_time:.0f}s",
        )

    console.print(table)


def _job_output_prefix(job: CompareJob) -> str:
    paper = _format_paper_header(job.arxiv_id, job.paper_title)
    return f"{job.model} @ {paper}"


def _print_job_rule(job: CompareJob, job_index: int, total_jobs: int) -> None:
    paper = _format_paper_header(job.arxiv_id, job.paper_title)
    _safe_print()
    _safe_rule(
        f"[{job_index}/{total_jobs}] [cyan bold]{job.model}[/cyan bold] on [bold]{paper}[/bold]"
    )


def _process_compare_job(
    job: CompareJob,
    opts: _ProcessOptions,
    job_index: int,
    total_jobs: int,
) -> PaperComparison:
    _print_job_rule(job, job_index, total_jobs)
    prefix = _job_output_prefix(job)

    out, duration, err, call_log = _run_extraction(
        job.arxiv_id,
        job.model,
        job.paper_text,
        job.structured_tables,
        latex_paper=job.latex_paper,
        output_prefix=prefix,
    )

    if opts.show_prompts:
        for _idx, rec in enumerate(call_log, 1):
            with _console_lock:
                _print_call_full_prompt(rec)

    if err or out is None:
        _safe_print(f"  [red]✗ EXTRACTION FAILED:[/red] {err}")
        cmp = PaperComparison(
            arxiv_id=job.arxiv_id,
            llm_model=job.model,
            baseline_count=len(job.baseline),
            duration_s=duration,
            error=err or "no output",
            call_log=call_log,
        )
    else:
        cmp = _compare(
            job.arxiv_id,
            job.model,
            job.baseline,
            out,
            call_log,
            opts.db_primary_metrics,
        )
        cmp.duration_s = duration
        _safe_print(
            f"  [bold]Result:[/bold]  "
            f"hits=[green]{cmp.hits}[/green]  "
            f"val_err=[yellow]{cmp.value_errors}[/yellow]  "
            f"miss=[red]{cmp.misses}[/red]  "
            f"halluc=[magenta]{cmp.hallucinations}[/magenta]  "
            f"recall=[bold]{_pct(cmp.recall)}[/bold]  "
            f"prec=[bold]{_pct(cmp.precision)}[/bold]  "
            f"[dim]{duration:.1f}s[/dim]"
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

    if opts.oneshot:
        _safe_print("  [dim]Running 1-shot (legacy) extraction for comparison…[/dim]")
        os_out, os_dur, os_err, os_log = _run_oneshot_extraction(
            job.arxiv_id,
            job.model,
            job.paper_text,
            job.structured_tables,
            latex_paper=job.latex_paper,
            output_prefix=prefix,
        )
        if os_err or os_out is None:
            _safe_print(f"  [red]✗ 1-shot FAILED:[/red] {os_err}")
        else:
            os_cmp = _compare(
                job.arxiv_id,
                job.model,
                job.baseline,
                os_out,
                os_log,
                opts.db_primary_metrics,
            )
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
        md = _render_log_markdown(
            job.arxiv_id,
            job.model,
            call_log,
            cmp if not err else None,
        )
        log_path.write_text(md, encoding="utf-8")
        _safe_print(f"  [bold green]Log saved →[/bold green] {log_path}")

    _safe_print()
    return cmp


def _run_compare_jobs(
    jobs: list[CompareJob],
    opts: _ProcessOptions,
    *,
    sequential: bool,
    workers: int,
) -> list[PaperComparison]:
    total_jobs = len(jobs)
    if total_jobs == 0:
        return []

    if sequential:
        return [
            _process_compare_job(job, opts, index, total_jobs) for index, job in enumerate(jobs, 1)
        ]

    worker_count = max(1, min(workers, total_jobs))
    _safe_print(
        f"[dim]Running {total_jobs} job(s) in parallel " f"with {worker_count} worker(s)[/dim]\n"
    )
    results: list[PaperComparison | None] = [None] * total_jobs
    with ThreadPoolExecutor(max_workers=worker_count) as pool:
        future_map = {
            pool.submit(_process_compare_job, job, opts, index, total_jobs): index - 1
            for index, job in enumerate(jobs, 1)
        }
        for future in as_completed(future_map):
            slot = future_map[future]
            results[slot] = future.result()
    return [result for result in results if result is not None]


@dataclass
class _DiscoveryResult:
    model: str
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
    table.add_column("Time", justify="right", style="dim")

    title_cache: dict[str, str] = {}

    for r in sorted(all_results, key=lambda x: (x.arxiv_id, x.llm_model)):
        if r.arxiv_id not in title_cache:
            title_cache[r.arxiv_id] = _resolve_paper_title(r.arxiv_id)
        title = _truncate_title(title_cache[r.arxiv_id], max_len=48) or "—"
        if r.error:
            table.add_row(
                r.arxiv_id,
                title,
                r.llm_model,
                "—",
                "—",
                "—",
                "—",
                "—",
                "—",
                "[red]ERR[/red]",
            )
        else:
            table.add_row(
                r.arxiv_id,
                title,
                r.llm_model,
                str(r.baseline_count),
                str(r.hits),
                str(r.value_errors),
                str(r.misses),
                str(r.hallucinations),
                _pct(r.recall),
                f"{r.duration_s:.0f}s",
            )
    console.print(table)


# ── Main ──────────────────────────────────────────────────────────────────────


def main(argv: list[str] | None = None) -> int:
    logging.basicConfig(level=logging.WARNING)

    p = argparse.ArgumentParser(
        description="Compare LLM extraction quality against the GLM 4.7 baseline"
    )
    p.add_argument(
        "--paper",
        nargs="+",
        metavar="ARXIV_ID",
        help="Limit to specific papers (default: all with GLM baseline)",
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
        "--log-dir",
        metavar="DIR",
        default="experiments/logs",
        help="Directory to save per-(model,paper) conversation logs as Markdown "
        "(default: experiments/logs)",
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
        help="Interactively select papers and models from numbered lists",
    )
    p.add_argument(
        "--sequential",
        action="store_true",
        help="Process one (model, paper) job at a time (default: parallel)",
    )
    p.add_argument(
        "--workers",
        type=int,
        default=8,
        metavar="N",
        help="Max parallel workers when not using --sequential (default: 8)",
    )
    args = p.parse_args(argv)

    if args.verbose:
        logging.getLogger().setLevel(logging.INFO)

    if not cfg.llm_endpoint:
        console.print("[red]No LLM endpoint configured.[/red] Set LLM_ENDPOINT in .env")
        return 1

    log_dir: Path | None = None
    # Never write logs for discovery-only runs — they produce no extraction output.
    if not args.no_logs and not args.discovery_only:
        log_dir = Path(args.log_dir)
        log_dir.mkdir(parents=True, exist_ok=True)

    # ── Resolve papers ────────────────────────────────────────────────────
    candidate_paper_ids = list(args.paper) if args.paper else _find_papers_with_baseline()
    if not candidate_paper_ids:
        console.print("[yellow]No papers with GLM 4.7 baseline found.[/yellow]")
        return 0

    if args.interactive:
        console.print(f"\n[bold]Papers with GLM 4.7 baseline ({len(candidate_paper_ids)}):[/bold]")
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
    console.print("\nFetching available models…")
    all_models = _fetch_model_ids(cfg.llm_endpoint, cfg.llm_api_key)
    skip_set = set(args.skip_model)
    if not args.include_skipped:
        skip_set |= _DEFAULT_SKIP

    if args.model:
        candidate_models = [m for m in args.model if m in all_models]
        missing = [m for m in args.model if m not in all_models]
        if missing:
            console.print(f"[yellow]Models not found on endpoint:[/yellow] {missing}")
    else:
        candidate_models = [m for m in all_models if m not in skip_set]
        random.shuffle(candidate_models)

    if not candidate_models:
        console.print("[yellow]No models to test.[/yellow]")
        return 0

    if args.interactive:
        console.print(f"\n[bold]Available models ({len(candidate_models)}):[/bold]")
        model_choices = [(model, model) for model in candidate_models]
        picked_models = _interactive_pick(model_choices, kind="Model")
        if picked_models is None:
            console.print("[yellow]Aborted.[/yellow]")
            return 0
        if not picked_models:
            console.print("[yellow]No models selected.[/yellow]")
            return 0
        test_models = picked_models
    else:
        test_models = candidate_models
        if not args.model:
            console.print(f"\n[bold]Models to test ({len(test_models)}):[/bold]")
            for model in test_models:
                console.print(f"  {model}")
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
            console.print(
                f"[bold]Models to test ({len(test_models)}):[/bold] {', '.join(test_models)}"
            )
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

    # ── Pre-load paper inputs ─────────────────────────────────────────────
    paper_inputs: dict[str, tuple[str, list, list[dict], Any, str]] = {}
    for pid in paper_ids:
        baseline = _load_baseline(pid)
        paper_title = _resolve_paper_title(pid)
        paper_label = _format_paper_header(pid, paper_title)
        if not baseline:
            console.print(f"  [yellow]skip[/yellow] {paper_label} — no GLM 4.7 baseline")
            continue
        paper_text, structured_tables, latex_paper = _load_paper_inputs(pid)
        if not paper_text and not latex_paper:
            console.print(f"  [yellow]skip[/yellow] {paper_label} — no paper text or LaTeX source")
            continue
        paper_inputs[pid] = (paper_text, structured_tables, baseline, latex_paper, paper_title)
        source = "HTML" if structured_tables else ("LaTeX" if latex_paper else "text.txt")
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
            f"baseline={len(baseline)} entries  "
            f"({source})"
        )
        if latex_info:
            console.print(latex_info)

    if not paper_inputs:
        console.print("[red]No valid papers to process.[/red]")
        return 1

    jobs = [
        CompareJob(
            model=model,
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

    console.print()

    # ── DB lookup: primary metric per dataset name ────────────────────────
    db_primary_metrics = _fetch_db_primary_metrics()
    if db_primary_metrics:
        console.print(
            f"[dim]DB primary metrics loaded for {len(db_primary_metrics)} datasets[/dim]"
        )

    # ── Discovery-only speed benchmark ───────────────────────────────────
    if args.discovery_only:
        console.rule("[bold]Discovery-Only Speed Benchmark[/bold]")
        disc_rows = _run_discovery_jobs(
            jobs,
            sequential=sequential,
            workers=workers,
        )
        disc_rows.sort(key=lambda r: (r.err is not None, -(r.tps or 0)))

        disc_table = Table(
            box=box.ROUNDED,
            show_lines=True,
            title="Dataset Discovery Timing (Step 1 only) — sorted by tok/s",
        )
        disc_table.add_column("Model", style="cyan")
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
            if row.err:
                disc_table.add_row(
                    row.model,
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
                    row.model,
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

    # ── Run extraction per (model, paper) ─────────────────────────────────
    process_opts = _ProcessOptions(
        show_prompts=args.show_prompts,
        oneshot=args.oneshot,
        log_dir=log_dir,
        db_primary_metrics=db_primary_metrics,
    )
    all_results = _run_compare_jobs(
        jobs,
        process_opts,
        sequential=sequential,
        workers=workers,
    )

    # ── Print summary tables ──────────────────────────────────────────────
    console.rule("[bold]Final Results[/bold]")
    _render_summary_table(all_results)

    if args.per_paper:
        console.print()
        _render_per_paper_table(all_results)

    # ── Save JSON output ──────────────────────────────────────────────────
    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "run_at": datetime.now(UTC).isoformat(),
            "baseline_model": _BASELINE_MODEL,
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
        out_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
        console.print(f"\nAggregate results saved to [cyan]{out_path}[/cyan]")

    return 0


if __name__ == "__main__":
    sys.exit(main())
