"""LLM extraction pipeline.

Orchestrates LLM calls to extract from a paper:
    1. Benchmark results (tables → structured YAML)
  2. Main figure identification
  3. Model parameter counts

Saves:
    - papers/{id}/extracted/llm_output.yaml   (raw, gitignored)
  - papers/{id}/extracted/results_human_readable.md  (TRACKED in git)

Usage::
    python -m backend.llm_extractor 2206.08164
    python -m backend.llm_extractor 2206.08164 --model fallback
    python -m backend.llm_extractor 2206.08164 --model minimax
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import subprocess
import tempfile
import textwrap
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from dataclasses import field as dc_field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import defusedxml.ElementTree as ET
import yaml
from openai import APIStatusError, OpenAI, RateLimitError
from pydantic import BaseModel, Field, field_validator
from tenacity import retry, stop_after_attempt, wait_exponential
from thefuzz import fuzz as fuzz_lib
from thefuzz import process as fuzz_process

from backend.config import cfg, normalize_arxiv_id
from backend.dataset_stats_parsing import format_stats_summary, is_statistics_table
from backend.db import session_scope
from backend.json_repair import parse_json_lenient
from backend.llm_model_options import display_name_for_model, extra_body_for_model
from backend.model_metadata import normalize_architecture_type
from backend.models import Paper
from backend.paper_storage import PaperStorage
from backend.qm9_targets import (
    QM9_DEFAULT_METRIC,
    QM9_EXTRACT_TARGET_GROUPS,
    is_qm9_dataset,
    qm9_extract_metric_constraint,
)
from backend.semantic_scholar import fetch_paper_metadata
from backend.text_cleanup import clean_extracted_text

# ParsedTable is imported lazily inside run_extraction to avoid slow startup,
# but type-annotated here for clarity.
try:
    from backend.html_parser import ParsedTable as _ParsedTable
except ImportError:
    _ParsedTable = None  # type: ignore[assignment,misc]

logger = logging.getLogger(__name__)

_QM9_EXTRACT_MAX_TOKENS = 16_384

_ARXIV_API = "https://export.arxiv.org/api/query?id_list={arxiv_id}"
_ARXIV_NS = {"atom": "http://www.w3.org/2005/Atom"}
_TOP_DATASETS_HINT_LIMIT = 50
_DATASET_RG_MATCH_LIMIT = 80
_DATASET_CONTEXT_WINDOW = 80
_DATASET_BENCHMARK_CONTEXT_MARKERS = (
    "dataset",
    "datasets",
    "benchmark",
    "benchmarks",
    "split",
    "splits",
    "accuracy",
    "acc",
    "f1",
    "auc",
    "roc",
    "mae",
    "rmse",
    "mrr",
    "ap",
    "hits@",
    "results",
    "performance",
    "classification",
    "regression",
    "prediction",
    "table",
)


def _title_looks_corrupted(title: str | None) -> bool:
    """Return True when a stored title looks like a degraded metadata fallback.

    The current checks intentionally catch the most common bad states we saw in
    cached metadata: raw `arXiv:` placeholders, stray LaTeX backslashes, broken
    leading punctuation, and duplicated colon fragments from malformed parsing.
    """
    t = (title or "").strip()
    if not t:
        return True
    return (
        t.startswith("arXiv:") or "\\" in t or t.startswith(": ") or " , " in t or t.count(":") > 1
    )


def _get_top_datasets_hint(limit: int = _TOP_DATASETS_HINT_LIMIT) -> str:
    """Return a formatted list of datasets in the DB ordered by result count.

    Includes datasets with zero results (i.e. seeded but not yet extracted) so
    the discovery LLM can match datasets from newly introduced benchmarks.
    Injected into the discovery prompt so the model uses canonical names.
    Returns an empty string when the DB is unavailable.
    """
    try:
        from sqlalchemy import func

        from backend.db import session_scope
        from backend.models import Dataset, DatasetVariant, Result

        with session_scope() as session:
            rows = (
                session.query(Dataset.name, func.count(Result.id).label("cnt"))
                .join(DatasetVariant, DatasetVariant.dataset_id == Dataset.id)
                .outerjoin(Result, Result.dataset_variant_id == DatasetVariant.id)
                .group_by(Dataset.name)
                .order_by(func.count(Result.id).desc())
                .limit(limit)
                .all()
            )
        if not rows:
            return ""
        lines = []
        for r in rows:
            suffix = f" ({r.cnt} results)" if r.cnt else "  [no results yet — new dataset]"
            lines.append(f"  {r.name}{suffix}")
        return "\n".join(lines)
    except Exception as exc:
        logger.debug("Could not query top datasets from DB: %s", exc)
        return ""


_KNOWN_DATASET_NAMES_CACHE: list[str] | None = None


def clear_known_dataset_names_cache() -> None:
    """Clear the cached dataset names. Call after editing config/seed_data.yaml."""
    global _KNOWN_DATASET_NAMES_CACHE
    _KNOWN_DATASET_NAMES_CACHE = None


def _get_known_dataset_names() -> list[str]:
    """Return canonical dataset names from config/seed_data.yaml."""
    global _KNOWN_DATASET_NAMES_CACHE
    if _KNOWN_DATASET_NAMES_CACHE is not None:
        return _KNOWN_DATASET_NAMES_CACHE

    seed_path = Path(__file__).resolve().parents[1] / "config" / "seed_data.yaml"
    try:
        raw = yaml.safe_load(seed_path.read_text(encoding="utf-8")) or {}
    except Exception as exc:
        logger.debug("Could not load canonical dataset names from %s: %s", seed_path, exc)
        _KNOWN_DATASET_NAMES_CACHE = []
        return _KNOWN_DATASET_NAMES_CACHE

    names: list[str] = []
    seen: set[str] = set()
    for benchmark in raw.get("benchmarks", []) or []:
        for dataset in benchmark.get("datasets", []) or []:
            name = str(dataset.get("name", "")).strip()
            if not name:
                continue
            key = name.lower()
            if key in seen:
                continue
            seen.add(key)
            names.append(name)

    _KNOWN_DATASET_NAMES_CACHE = names
    return names


def _get_known_dataset_names_hint(limit: int | None = None) -> str:
    """Return canonical dataset names from seed_data.yaml as a newline list."""
    names = _get_known_dataset_names()
    if limit is not None:
        names = names[:limit]
    if not names:
        return ""
    return "\n".join(f"- {name}" for name in names)


def _ripgrep_dataset_name_hits(
    text: str, source_path: Path | None = None, limit: int = _DATASET_RG_MATCH_LIMIT
) -> list[str]:
    """Return canonical dataset names whose literal strings appear in the text."""
    dataset_names = _get_known_dataset_names()
    if not dataset_names:
        return []

    canonical_by_lower = {name.lower(): name for name in dataset_names}
    target_path = source_path if source_path and source_path.exists() else None

    try:
        with tempfile.TemporaryDirectory(prefix="dataset-rg-") as tmpdir:
            tmp_path = Path(tmpdir)
            patterns_path = tmp_path / "datasets.regex"
            pattern_lines = [
                rf"(?<![A-Za-z0-9-]){re.escape(name)}(?![A-Za-z0-9-])" for name in dataset_names
            ]
            patterns_path.write_text("\n".join(pattern_lines), encoding="utf-8")

            if target_path is None:
                target_path = tmp_path / "input.txt"
                target_path.write_text(text, encoding="utf-8", errors="replace")

            proc = subprocess.run(
                [
                    "rg",
                    "--pcre2",
                    "--no-filename",
                    "--only-matching",
                    "--ignore-case",
                    "--file",
                    str(patterns_path),
                    str(target_path),
                ],
                check=False,
                capture_output=True,
                text=True,
            )
    except FileNotFoundError:
        logger.debug("ripgrep not available; skipping dataset-name precheck")
        return []
    except Exception as exc:
        logger.debug("ripgrep dataset precheck failed: %s", exc)
        return []

    if proc.returncode not in (0, 1):
        logger.debug("ripgrep dataset precheck returned %d: %s", proc.returncode, proc.stderr)
        return []

    text_lower = text.lower()

    def _has_benchmark_context(name: str) -> bool:
        pattern = rf"(?<![A-Za-z0-9-]){re.escape(name)}(?![A-Za-z0-9-])"
        for match in re.finditer(pattern, text, flags=re.IGNORECASE):
            start = max(0, match.start() - _DATASET_CONTEXT_WINDOW)
            end = min(len(text_lower), match.end() + _DATASET_CONTEXT_WINDOW)
            window = text_lower[start:end]
            if any(marker in window for marker in _DATASET_BENCHMARK_CONTEXT_MARKERS):
                return True
        return False

    hits: list[str] = []
    seen_hits: set[str] = set()
    for line in proc.stdout.splitlines():
        canonical = canonical_by_lower.get(line.strip().lower())
        if not canonical or canonical in seen_hits or not _has_benchmark_context(canonical):
            continue
        seen_hits.add(canonical)
        hits.append(canonical)
        if len(hits) >= limit:
            break
    return hits


def _discovery_text_excerpts(text: str, chunk_size: int = 6_000) -> list[str]:
    """Return head/tail excerpts for discovery prompts without dropping appendices."""
    clean = text.strip()
    if not clean:
        return []
    if len(clean) <= chunk_size * 2:
        return [clean]
    return [clean[:chunk_size], clean[-chunk_size:]]


def _noncanonical_dataset_hints(text: str) -> list[str]:
    """Return common non-canonical dataset/task names seen in appendix tables."""
    hints: list[str] = []
    if re.search(r"\bsubgraph counting\b", text, flags=re.IGNORECASE):
        hints.append("subgraph counting")
    if re.search(r"\breddit-bin(?:ary)?\b", text, flags=re.IGNORECASE):
        hints.append("REDDIT-BINARY")
    return hints


def _extract_latex_braced_group(tex: str, open_brace_pos: int) -> str:
    """Return the inner text of a {...} group starting at *open_brace_pos* (the '{')."""
    if open_brace_pos >= len(tex) or tex[open_brace_pos] != "{":
        return ""
    depth = 1
    pos = open_brace_pos + 1
    while pos < len(tex) and depth > 0:
        if tex[pos] == "{":
            depth += 1
        elif tex[pos] == "}":
            depth -= 1
        pos += 1
    return tex[open_brace_pos + 1 : pos - 1]


def _parse_author_names_from_latex(tex: str) -> list[str]:
    """Extract ordered author names from \\author{...} blocks in LaTeX source."""
    from backend.latex_source import _strip_latex

    authors: list[str] = []
    for match in re.finditer(r"\\author\s*(?:\[[^\]]*\])?\s*\{", tex):
        body = _extract_latex_braced_group(tex, match.end() - 1)
        if not body:
            continue
        for part in re.split(r"\\and\b", body):
            clean = _strip_latex(part).strip()
            if clean:
                authors.append(clean)
    return authors


def _extract_metadata_from_latex_cache(latex_dir: Path) -> dict[str, str | list[str]]:
    """Read title, abstract, and authors from a cached expanded.tex without a full parse.

    Used as a free, offline fallback during abstract screening when the DB has
    only a stub entry and no HTML is available or HTML lacks an abstract.
    Returns a dict with 'title', 'abstract', and/or 'authors' keys (may be partial).
    """
    expanded = latex_dir / "expanded.tex"
    if not expanded.exists() or expanded.stat().st_size < 100:
        return {}
    try:
        from backend.latex_source import _expand_user_macros, _strip_latex

        tex = expanded.read_text(encoding="utf-8", errors="replace")[:40_000]
        tex, _ = _expand_user_macros(tex)

        result: dict[str, str | list[str]] = {}

        # Extract \title{...} — handles optional [short] argument
        m = re.search(r"\\title\s*(?:\[[^\]]*\])?\s*\{", tex)
        if m:
            raw_title = _extract_latex_braced_group(tex, m.end() - 1)
            clean = _strip_latex(raw_title)
            if clean:
                result["title"] = clean

        # Extract \begin{abstract}...\end{abstract}
        m = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", tex, re.DOTALL)
        if m:
            raw_abstract = m.group(1)
            clean = _strip_latex(raw_abstract)
            if clean:
                result["abstract"] = clean

        author_names = _parse_author_names_from_latex(tex)
        if author_names:
            result["authors"] = author_names

        return result
    except Exception as exc:
        logger.debug("LaTeX metadata cache read failed: %s", exc)
        return {}


def fetch_arxiv_metadata(arxiv_id: str) -> dict[str, str]:
    """Fetch title, abstract, and published date from the arXiv Atom API.

    Retries up to 10 times with 10-second intervals on any transient failure
    (network error, rate limit 429, server error).  Returns {} after all
    attempts are exhausted.
    """
    _MAX_ATTEMPTS = 10
    _RETRY_INTERVAL = 10  # seconds between attempts

    url = _ARXIV_API.format(arxiv_id=arxiv_id)
    for attempt in range(_MAX_ATTEMPTS):
        try:
            with urllib.request.urlopen(url, timeout=15) as resp:  # nosec B310
                xml_bytes = resp.read()
            root = ET.fromstring(xml_bytes)
            entry = root.find("atom:entry", _ARXIV_NS)
            if entry is None:
                return {}
            title = (entry.find("atom:title", _ARXIV_NS).text or "").replace("\n", " ").strip()
            abstract = clean_extracted_text(
                (entry.find("atom:summary", _ARXIV_NS).text or "").replace("\n", " ").strip()
            )
            published_elem = entry.find("atom:published", _ARXIV_NS)
            published_date = ""
            if published_elem is not None and published_elem.text:
                published_date = published_elem.text[:10]  # "YYYY-MM-DD"
            return {"title": title, "abstract": abstract, "published_date": published_date}
        except urllib.error.HTTPError as exc:
            if exc.code == 429:
                logger.warning(
                    "arXiv API rate-limited (429) for %s — waiting %ds (attempt %d/%d)",
                    arxiv_id,
                    _RETRY_INTERVAL,
                    attempt + 1,
                    _MAX_ATTEMPTS,
                )
            else:
                logger.warning(
                    "arXiv API HTTP error for %s: %s (attempt %d/%d)",
                    arxiv_id,
                    exc,
                    attempt + 1,
                    _MAX_ATTEMPTS,
                )
        except Exception as exc:
            logger.warning(
                "arXiv API request failed for %s: %s (attempt %d/%d)",
                arxiv_id,
                exc,
                attempt + 1,
                _MAX_ATTEMPTS,
            )
        if attempt < _MAX_ATTEMPTS - 1:
            time.sleep(_RETRY_INTERVAL)
    logger.warning("arXiv API gave up after %d attempts for %s", _MAX_ATTEMPTS, arxiv_id)
    return {}


_S2_API_URL = (
    "https://api.semanticscholar.org/graph/v1/paper/ARXIV:{arxiv_id}?fields=publicationDate"
)


def fetch_semantic_scholar_published_date(arxiv_id: str) -> str | None:
    """Fetch exact publication date from Semantic Scholar."""
    metadata = fetch_paper_metadata(arxiv_id)
    published_date = metadata.get("published_date")
    if published_date and re.match(r"^\d{4}-\d{2}-\d{2}$", published_date):
        return published_date
    return None


def _headers_to_dict(headers_obj: Any) -> dict[str, str]:
    """Convert a response header container to a lowercase dict."""
    if headers_obj is None:
        return {}

    try:
        items = headers_obj.items()
    except Exception:
        try:
            return {str(k).lower(): str(v) for k, v in dict(headers_obj).items()}
        except Exception:
            return {}

    return {str(k).lower(): str(v) for k, v in items}


# ── Call logging ───────────────────────────────────────────────────────────────


@dataclass
class CallRecord:
    """One LLM request/response exchange, captured for verbose inspection."""

    call_type: str
    system_prompt: str
    user_content: str
    raw_response: str = ""
    input_chars: int = 0
    output_chars: int = 0
    duration_s: float = 0.0
    ttft_s: float | None = None  # time to first token (streaming only)
    tokens_per_sec: float | None = None  # output tokens per second
    prompt_tokens: int | None = None  # from API usage header
    completion_tokens: int | None = None  # from API usage header
    success: bool = False
    parse_error: str | None = None  # set by _call_json on failure
    parsed_result: Any = dc_field(default=None, repr=False)
    extra: dict = dc_field(default_factory=dict)


def _print_dataset_statistics(rec: CallRecord, *, use_rich: bool, console: Any = None) -> None:
    stat_tables = rec.extra.get("statistics_tables")
    if stat_tables:
        labels = [
            f"Table {item['number']}" + (" [appendix]" if item.get("in_appendix") else "")
            for item in stat_tables
        ]
        line = "Statistics tables: " + ", ".join(labels)
        if use_rich and console is not None:
            _con = console
            _con.print(f"    [dim]{line}[/dim]")
            for item in stat_tables:
                caption = (item.get("caption") or "").strip()
                if caption:
                    _con.print(f"      [dim]↳ Table {item['number']}: {caption[:100]}[/dim]")
        else:
            print(f"    {line}")

    stats = rec.extra.get("dataset_statistics")
    if stats:
        for item in stats:
            name = item.get("name", "?")
            if item.get("statistics_mentioned"):
                sources = ", ".join(item.get("statistics_sources") or []) or "detected"
                stat_table_nums = item.get("statistics_table_numbers") or []
                stat_tables_note = f" stats tables {stat_table_nums}" if stat_table_nums else ""
                if use_rich and console is not None:
                    console.print(
                        f"    [dim]Dataset stats[/dim] [bold]{name}[/bold][dim]:[/dim] "
                        f"[green]yes[/green] [dim]({sources}{stat_tables_note})[/dim]"
                    )
                else:
                    print(f"    Dataset stats {name}: yes ({sources}{stat_tables_note})")
            else:
                if use_rich and console is not None:
                    console.print(
                        f"    [dim]Dataset stats[/dim] [bold]{name}[/bold][dim]:[/dim] [dim]no[/dim]"
                    )
                else:
                    print(f"    Dataset stats {name}: no")

    extracted_details = rec.extra.get("extracted_statistics_details")
    if extracted_details:
        if use_rich and console is not None:
            console.print("    [dim]Extracted dataset statistics:[/dim]")
            for item in extracted_details:
                name = item.get("name", "?")
                summary = format_stats_summary(item)
                source = item.get("source_ref") or ""
                source_note = f" [dim]({source})[/dim]" if source else ""
                console.print(f"      [bold]{name}[/bold][dim]:[/dim] {summary}{source_note}")
        else:
            print("    Extracted dataset statistics:")
            for item in extracted_details:
                name = item.get("name", "?")
                summary = format_stats_summary(item)
                source = item.get("source_ref") or ""
                print(f"      {name}: {summary}" + (f" ({source})" if source else ""))
    elif rec.extra.get("paper_has_statistics"):
        extracted = rec.extra.get("extracted_dataset_statistics")
        if extracted:
            if use_rich and console is not None:
                console.print(
                    "    [dim]Extracted stats:[/dim] "
                    + "  ".join(f"[bold]{name}[/bold]" for name in extracted)
                )
            else:
                print(f"    Extracted stats: {', '.join(extracted)}")


def _print_call_progress(rec: CallRecord, call_index: int) -> None:
    """Print a one-line-plus-details summary of a completed LLM call.

    Uses ``rich`` when available (for colour/bold), falls back to plain print.
    Called as the ``_progress_callback`` on *LLMExtractor* during interactive use.
    """
    try:
        from rich.console import Console as _Console

        _con = _Console()
        _use_rich = True
    except ImportError:
        _use_rich = False

    ttft_str = f"TTFT {rec.ttft_s:.2f}s  " if rec.ttft_s is not None else ""
    tps_str = f"{rec.tokens_per_sec:.0f} tok/s  " if rec.tokens_per_sec else ""
    tok_str = ""
    if rec.prompt_tokens or rec.completion_tokens:
        tok_str = f"prompt={rec.prompt_tokens or '?'}  completion={rec.completion_tokens or '?'}  "

    call_type = rec.call_type or ""
    stage_prefix = ""
    if call_type.startswith("screen_paper"):
        stage_prefix = "[2] "
    elif call_type.startswith("discover_datasets") or call_type.startswith("select_tables"):
        stage_prefix = "[3] "
    elif call_type.startswith("extract_dataset_statistics"):
        stage_prefix = "[3b] "
    elif call_type.startswith("extract_sota_claims"):
        stage_prefix = "[3c] "
    elif call_type.startswith("extract_dataset") or call_type.startswith("extract_section"):
        stage_prefix = "[4] "

    if _use_rich:
        status = "[green]✓[/green]" if rec.success else "[red]✗[/red]"
        _con.print(
            f"  {status} Call {call_index} "
            f"{stage_prefix}[bold cyan]{rec.call_type}[/bold cyan]  "
            f"in={rec.input_chars:,} chars  out={rec.output_chars:,} chars  "
            f"{ttft_str}{tps_str}{tok_str}"
            f"[dim]{rec.duration_s:.1f}s total[/dim]"
        )
        # Discovered datasets
        discovered = rec.extra.get("discovered_datasets")
        if discovered is not None:
            if discovered:
                _con.print(
                    "    [dim]Datasets:[/dim] " + "  ".join(f"[bold]{d}[/bold]" for d in discovered)
                )
            else:
                _con.print("    [yellow]No datasets discovered[/yellow]")

        # Table selection — single-dataset form
        sel_tables = rec.extra.get("selected_tables")
        if sel_tables is not None:
            total_t = rec.extra.get("tables_total", "?")
            _con.print(
                f"    [dim]Tables selected:[/dim] {sel_tables} "
                f"[dim]({len(sel_tables)}/{total_t})[/dim]"
            )
        # Table selection — multi-dataset form
        sel_multi = rec.extra.get("selected_tables_per_dataset")
        if sel_multi is not None:
            total_t = rec.extra.get("tables_total", "?")
            for ds_name, nums in sel_multi.items():
                _con.print(
                    f"    [dim]Tables for[/dim] [bold]{ds_name}[/bold][dim]:[/dim] "
                    f"{nums} [dim]({len(nums)}/{total_t})[/dim]"
                )
        if (
            call_type.startswith("discover_datasets")
            or call_type.startswith("select_tables")
            or call_type.startswith("extract_dataset_statistics")
        ):
            note = rec.extra.get("table_selection_note")
            if note:
                _con.print(f"    [dim]{note}[/dim]")
            _print_dataset_statistics(rec, use_rich=True, console=_con)

        # RAG stats
        rag = rec.extra.get("rag")
        if rag:
            mode_color = "green" if rag["table_selection_mode"] == "caption_match" else "yellow"
            _con.print(
                f"    [dim]RAG:[/dim] "
                f"paragraphs {rag['paragraphs_selected']}/{rag['paragraphs_total']}  "
                f"tables {rag['tables_selected']}/{rag['tables_total']} "
                f"([{mode_color}]{rag['table_selection_mode']}[/{mode_color}])"
            )
            for cap in rag.get("selected_table_captions", [])[:3]:
                _con.print(f"      [dim]↳ {cap}[/dim]")
            excess = len(rag.get("selected_table_captions", [])) - 3
            if excess > 0:
                _con.print(f"      [dim]↳ … +{excess} more[/dim]")

        if rec.extra.get("json_parse_method") == "regex":
            _con.print("    [yellow]⚠ JSON extracted via regex fallback[/yellow]")
        if rec.parse_error:
            _con.print(f"    [red]⚠ Parse error: {rec.parse_error[:120]}[/red]")
    else:
        status = "✓" if rec.success else "✗"
        print(
            f"  {status} Call {call_index} {stage_prefix}{rec.call_type}  "
            f"in={rec.input_chars:,}  out={rec.output_chars:,}  {rec.duration_s:.1f}s"
        )
        discovered = rec.extra.get("discovered_datasets")
        if discovered:
            print(f"    Datasets: {', '.join(discovered)}")
        sel = rec.extra.get("selected_tables") or rec.extra.get("selected_tables_per_dataset")
        if sel:
            print(f"    Tables: {sel}")
        if (
            call_type.startswith("discover_datasets")
            or call_type.startswith("select_tables")
            or call_type.startswith("extract_dataset_statistics")
        ):
            note = rec.extra.get("table_selection_note")
            if note:
                print(f"    {note}")
            _print_dataset_statistics(rec, use_rich=False)


# ── Pydantic models for structured LLM output ─────────────────────────────────


class ProposedModel(BaseModel):
    name: str
    params_millions: float | None = None
    params_exact: int | None = None
    model_type: str | None = None

    @field_validator("model_type", mode="before")
    @classmethod
    def _normalize_model_type(cls, v: Any) -> str | None:
        return normalize_architecture_type(v if v is not None else None)


class BaselineModelInfo(BaseModel):
    name: str
    params_millions: float | None = None
    params_exact: int | None = None
    model_type: str | None = None
    original_paper_hint: str | None = None

    @field_validator("model_type", mode="before")
    @classmethod
    def _normalize_model_type(cls, v: Any) -> str | None:
        return normalize_architecture_type(v if v is not None else None)


class ResultEntry(BaseModel):
    model: str
    is_proposed: bool = False
    dataset: str
    metric: str
    value: float
    std: float | None = None
    higher_is_better: bool = True
    uses_external_data: bool | None = None
    table_ref: str | None = None
    source_ref: str | None = "this paper"

    @field_validator("value", "std", mode="before")
    @classmethod
    def _coerce_numeric(cls, v: Any) -> Any:
        if v is None:
            return v
        if isinstance(v, str):
            v = re.sub(r"[^\d.\-]", "", v)
            if not v:
                return None
        return float(v)


class ExtractionOutput(BaseModel):
    proposed_model: ProposedModel | None = None
    baseline_models: list[BaselineModelInfo] = Field(default_factory=list)
    results: list[ResultEntry] = Field(default_factory=list)
    extraction_confidence: str = "LOW"
    extraction_notes: str = ""
    discovered_datasets: list[DatasetInfo] = Field(default_factory=list)
    paper_has_statistics: bool = False

    @field_validator("proposed_model", mode="before")
    @classmethod
    def _require_model_name(cls, v: Any) -> Any:
        """Discard proposed_model when the LLM returns name=null or name=''."""
        if v is None:
            return None
        if isinstance(v, dict) and not v.get("name"):
            return None
        return v


class ScreenResult(BaseModel):
    has_benchmark_results: bool = False
    has_new_benchmark: bool = False
    datasets_mentioned: list[str] = Field(default_factory=list)
    confidence: float = 0.0
    notes: str = ""


class DatasetInfo(BaseModel):
    name: str
    table_refs: list[str] = Field(default_factory=list)
    primary_metric: str | None = None
    statistics_mentioned: bool = False
    statistics_sources: list[str] = Field(default_factory=list)


class DatasetList(BaseModel):
    datasets: list[DatasetInfo] = Field(default_factory=list)
    notes: str = ""


class DatasetStatisticsEntry(BaseModel):
    name: str
    variant: str | None = None
    num_graphs: int | None = None
    avg_nodes: float | None = None
    avg_edges: float | None = None
    num_classes: int | None = None
    raw_values: dict[str, str] = Field(default_factory=dict)
    precision_hints: dict[str, str] = Field(default_factory=dict)
    extra_stats: dict[str, float | int] = Field(default_factory=dict)
    source_ref: str | None = None
    confidence: str = "medium"


class DatasetStatisticsOutput(BaseModel):
    datasets: list[DatasetStatisticsEntry] = Field(default_factory=list)
    notes: str = ""


class SotaClaimRestriction(BaseModel):
    type: str = "other"
    description: str = ""


class SotaClaimEntry(BaseModel):
    raw_sentence: str
    claim_summary: str = ""
    datasets: list[str] = Field(default_factory=list)
    metrics: list[str] = Field(default_factory=list)
    claim_type: str = "other"
    scope: str = "unclear"
    restrictions: list[SotaClaimRestriction] = Field(default_factory=list)
    source_ref: str | None = None
    confidence: str = "medium"


class SotaClaimOutput(BaseModel):
    claims: list[SotaClaimEntry] = Field(default_factory=list)
    notes: str = ""


def _merge_dataset_lists(*dataset_lists: DatasetList) -> DatasetList:
    """Merge dataset discovery results while preserving first-seen order."""
    merged: list[DatasetInfo] = []
    seen: dict[str, DatasetInfo] = {}
    notes: list[str] = []

    for dataset_list in dataset_lists:
        if dataset_list.notes:
            notes.append(dataset_list.notes)
        for ds in dataset_list.datasets:
            key = ds.name.strip().lower()
            if not key:
                continue
            existing = seen.get(key)
            if existing is None:
                clone = DatasetInfo.model_validate(ds.model_dump())
                merged.append(clone)
                seen[key] = clone
                continue
            if ds.primary_metric and not existing.primary_metric:
                existing.primary_metric = ds.primary_metric
            for table_ref in ds.table_refs:
                if table_ref not in existing.table_refs:
                    existing.table_refs.append(table_ref)
            if ds.statistics_mentioned:
                existing.statistics_mentioned = True
            for src in ds.statistics_sources:
                if src not in existing.statistics_sources:
                    existing.statistics_sources.append(src)

    return DatasetList(datasets=merged, notes="\n".join(note for note in notes if note))


def _apply_statistics_ripgrep_precheck(datasets: DatasetList, text: str) -> DatasetList:
    """Flag statistics_mentioned when stat markers appear near dataset names."""
    from backend.dataset_stats_parsing import ripgrep_stat_markers_near_datasets

    names = [ds.name for ds in datasets.datasets]
    if not names or not text.strip():
        return datasets
    hits = ripgrep_stat_markers_near_datasets(text, names)
    for ds in datasets.datasets:
        if hits.get(ds.name):
            ds.statistics_mentioned = True
    return datasets


def _dataset_statistics_hint_block(datasets: list[DatasetInfo]) -> str:
    lines: list[str] = []
    for ds in datasets:
        if not ds.statistics_mentioned:
            continue
        sources = ", ".join(ds.statistics_sources) if ds.statistics_sources else "paper text"
        lines.append(f"- {ds.name}: structural statistics mentioned in {sources}")
    if not lines:
        return ""
    return (
        "\n\nDATASET STATISTICS HINTS "
        "(awareness only — still exclude stat-only tables from benchmark results):\n"
        + "\n".join(lines)
    )


def _statistics_table_summaries(tables: list) -> list[dict[str, Any]]:
    summaries: list[dict[str, Any]] = []
    for table in tables:
        if not is_statistics_table(table):
            continue
        number = getattr(table, "number", None)
        if number is None:
            continue
        summaries.append(
            {
                "number": int(number),
                "caption": getattr(table, "caption", "") or "",
                "in_appendix": bool(getattr(table, "in_appendix", False)),
            }
        )
    return summaries


def _parse_table_ref_number(source: str) -> int | None:
    match = re.search(r"table\s*(\d+)", source, flags=re.IGNORECASE)
    if not match:
        return None
    return int(match.group(1))


def _dataset_statistics_extra_with_tables(
    datasets: list[DatasetInfo],
    *,
    stat_table_summaries: list[dict[str, Any]] | None = None,
) -> list[dict[str, Any]]:
    stat_numbers = {item["number"] for item in (stat_table_summaries or [])}
    out: list[dict[str, Any]] = []
    for ds in datasets:
        table_nums = sorted(
            {
                num
                for source in ds.statistics_sources
                for num in [_parse_table_ref_number(source)]
                if num is not None and num in stat_numbers
            }
        )
        out.append(
            {
                "name": ds.name,
                "statistics_mentioned": ds.statistics_mentioned,
                "statistics_sources": list(ds.statistics_sources),
                "statistics_table_numbers": table_nums,
            }
        )
    return out


def _enrich_dataset_statistics_from_tables(datasets: DatasetList, tables: list) -> None:
    """Mark datasets with statistics when their names appear in statistics tables."""
    stat_tables = [t for t in tables if is_statistics_table(t)]
    if not stat_tables:
        return

    for ds in datasets.datasets:
        ds_pattern = rf"(?<![A-Za-z0-9-]){re.escape(ds.name)}(?![A-Za-z0-9-])"
        for table in stat_tables:
            number = getattr(table, "number", None)
            caption = (getattr(table, "caption", "") or "").strip()
            body = getattr(table, "markdown", None) or str(table)
            first_col = LLMExtractor._table_first_column(table)
            haystack = f"{caption}\n{body}\n{first_col}"
            if not re.search(ds_pattern, haystack, flags=re.IGNORECASE):
                continue
            ds.statistics_mentioned = True
            ref = f"Table {number}" if number is not None else caption or "statistics table"
            if ref and ref not in ds.statistics_sources:
                ds.statistics_sources.append(ref)


class FigureInfo(BaseModel):
    figure_id: str | None = None
    figure_number: int | None = None
    caption_snippet: str | None = None
    img_src: str | None = None
    page_number: int | None = None
    reason: str | None = None


class ModelSizeEntry(BaseModel):
    model_name: str
    matched_result_name: str | None = None
    params_millions: float | None = None
    params_exact: int | None = None
    source_text: str | None = None


# ── LLMExtractor ──────────────────────────────────────────────────────────────

# Maximum characters of paper text that is sent in a single LLM call.
# ~40k chars ≈ 10k tokens — safe for most models on the academic cloud endpoint.
# Papers exceeding this are handled via table-section chunks, then smart excerpt.
_CHUNK_SIZE = 40_000
# Tighter limit used for table-section chunks (keeps each LLM call ≤ ~2k tokens).
# Primary model (openai-gpt-oss-120b) reliably returns results up to ~8k chars;
# above that it often returns valid JSON but with an empty results list.
_TABLE_SECTION_SIZE = 8_000
# Maximum characters for the tables-only section appended to chunks
_TABLE_CHUNK_SIZE = 16_000
# Smart-excerpt parameters (used when full text > _CHUNK_SIZE)
_SMART_INTRO_CHARS = 3_000
_SMART_TABLES_CHARS = 30_000
_SIZE_FUZZY_MATCH_MIN_SCORE = 88
# How much of the paper intro to include in dataset discovery.
# Larger than _SMART_INTRO_CHARS so that for text-only papers the model can
# see table-of-datasets overviews that appear in the first ~5-6 pages.
_DISCOVERY_INTRO_CHARS = 8_000

# Metric-name split prefixes that must be stripped (case-insensitive).
# "test accuracy" → "accuracy"; "val MAE" → "MAE".
_SPLIT_PREFIXES = re.compile(
    r"^\s*(?:test|train|training|val|valid|validation)\s*[-_/]?\s*",
    re.IGNORECASE,
)
# Any result whose metric still contains one of these words AFTER stripping the
# leading prefix is a non-test split entry (e.g. "training loss") → drop it.
_NON_TEST_PATTERN = re.compile(
    r"\b(?:train|training|val|valid|validation)\b",
    re.IGNORECASE,
)

# Matches \begin{table}…\end{table} (and table*, longtable) so they can be
# stripped from the prose-only RAG text (tables are passed separately).
_TABLE_ENV_RE = re.compile(
    r"\\begin\{(table\*?|longtable)\}.*?\\end\{\1\}",
    re.DOTALL,
)


def _strip_table_environments(text: str) -> str:
    """Remove \\begin{table[*]}…\\end{table[*]} blocks from LaTeX text."""
    return _TABLE_ENV_RE.sub("", text)


def _normalise_metrics(results: list[ResultEntry]) -> list[ResultEntry]:
    """Strip split prefixes from metric names and discard non-test entries.

    Examples:
      "Test F1"   → "F1"      (kept)
      "Val MAE"   → "MAE"     (dropped — non-test after stripping? No — "MAE" has no train/val word)
    Wait — "Val MAE" stripped → "MAE" kept? No: we drop entries whose *original* metric
    contains a train/val word UNLESS it also starts with "test".
    Logic:
      1. If metric starts with a split prefix → strip it.
      2. If the *original* (pre-strip) metric matched a non-test split word → drop entry.
         This catches "train accuracy", "val loss", "training error", etc.
      3. Keep everything else (including already-clean "F1", "AP", "MAE").
    """
    kept: list[ResultEntry] = []
    for r in results:
        original = r.metric.strip()
        original_lower = original.lower()

        # Detect split type from the original name
        is_train_val = bool(_NON_TEST_PATTERN.search(original_lower))
        is_test = bool(re.match(r"^\s*test\b", original_lower))

        if is_train_val and not is_test:
            # e.g. "train F1", "val accuracy", "validation MAE" → drop
            logger.debug("Dropping non-test metric entry: model=%r metric=%r", r.model, original)
            continue

        # Strip leading "test" / "test -" prefix (and "test" if it appears alone)
        clean = _SPLIT_PREFIXES.sub("", original).strip()
        if not clean:
            clean = original  # safety: never produce an empty metric name

        if clean != original:
            logger.debug("Normalised metric %r → %r", original, clean)
            r = r.model_copy(update={"metric": clean})

        kept.append(r)
    return kept


def _dedupe_result_entries(results: list[ResultEntry]) -> list[ResultEntry]:
    """Keep the first result for each (model, dataset, metric) key."""
    seen: set[tuple[str, str, str]] = set()
    unique_results: list[ResultEntry] = []
    for result in results:
        key = (result.model.lower(), result.dataset.lower(), result.metric.lower())
        if key in seen:
            continue
        seen.add(key)
        unique_results.append(result)
    return unique_results


def _dedupe_baselines(baselines: list[BaselineModelInfo]) -> list[BaselineModelInfo]:
    """Keep the first baseline entry for each model name."""
    seen_names: set[str] = set()
    unique_baselines: list[BaselineModelInfo] = []
    for baseline in baselines:
        key = baseline.name.lower()
        if key in seen_names:
            continue
        seen_names.add(key)
        unique_baselines.append(baseline)
    return unique_baselines


def _collapse_confidence_levels(confidence_levels: list[str]) -> str:
    """Return a conservative aggregate confidence across partial extraction calls."""
    if confidence_levels and all(level == "HIGH" for level in confidence_levels):
        return "HIGH"
    if confidence_levels and "LOW" not in confidence_levels:
        return "MEDIUM"
    return "LOW"


def _merge_extraction_outputs(
    *,
    proposed_model: ProposedModel | None,
    baselines: list[BaselineModelInfo],
    results: list[ResultEntry],
    confidence_levels: list[str],
    notes_parts: list[str],
    normalise_metrics: bool = False,
    discovered_datasets: list[DatasetInfo] | None = None,
) -> ExtractionOutput:
    """Build a single ExtractionOutput from partial extraction fragments."""
    merged_results = _normalise_metrics(results) if normalise_metrics else results
    ds_list = discovered_datasets or []
    return ExtractionOutput(
        proposed_model=proposed_model,
        baseline_models=_dedupe_baselines(baselines),
        results=_dedupe_result_entries(merged_results),
        extraction_confidence=_collapse_confidence_levels(confidence_levels),
        extraction_notes="\n".join(notes_parts),
        discovered_datasets=ds_list,
        paper_has_statistics=any(ds.statistics_mentioned for ds in ds_list),
    )


class LLMExtractor:
    """Extracts structured information from a paper using an LLM."""

    def __init__(
        self,
        model_tier: str = "primary",
        streaming: bool = False,
        result_output_format: str = "yaml",
    ) -> None:
        self.model_name = cfg.model_for_tier(model_tier)
        self.streaming = streaming
        self.result_output_format = result_output_format.lower()
        self._call_log: list[CallRecord] = []
        self._progress_callback: Any = None  # called with (CallRecord,) after each LLM call
        self._last_progress_idx: int = -1  # tracks which record was last fired
        self._client = OpenAI(
            api_key=cfg.llm_api_key or "none",
            base_url=cfg.llm_endpoint or None,
            timeout=cfg.llm_timeout,
        )

    # ── Progress callback ────────────────────────────────────────────────

    def _fire_progress(self) -> None:
        """Invoke the progress callback on the latest call record (once per record)."""
        if self._progress_callback and self._call_log:
            idx = len(self._call_log) - 1
            if idx != self._last_progress_idx:
                self._last_progress_idx = idx
                self._progress_callback(self._call_log[idx])

    def _emit_table_selection_summary(
        self,
        datasets: list[DatasetInfo],
        tables: list,
        *,
        selected_per_dataset: dict[str, list[int]],
        note: str,
        stat_table_summaries: list[dict[str, Any]] | None = None,
    ) -> None:
        """Emit verbose progress for table selection when the LLM call is skipped."""
        if not self._progress_callback:
            return
        self._call_log.append(
            CallRecord(
                call_type="select_tables:all",
                system_prompt="",
                user_content="",
                success=True,
                extra={
                    "selected_tables_per_dataset": selected_per_dataset,
                    "tables_total": len(tables),
                    "dataset_statistics": _dataset_statistics_extra_with_tables(
                        datasets,
                        stat_table_summaries=stat_table_summaries,
                    ),
                    "statistics_tables": stat_table_summaries or [],
                    "paper_has_statistics": any(ds.statistics_mentioned for ds in datasets),
                    "table_selection_note": note,
                },
            )
        )
        self._fire_progress()

    def _emit_discovery_statistics_summary(
        self,
        datasets: list[DatasetInfo],
        *,
        stat_table_summaries: list[dict[str, Any]],
    ) -> None:
        """Emit dataset-statistics details after discovery prechecks."""
        if not self._progress_callback:
            return
        if not stat_table_summaries and not any(ds.statistics_mentioned for ds in datasets):
            return
        self._call_log.append(
            CallRecord(
                call_type="discover_datasets:statistics",
                system_prompt="",
                user_content="",
                success=True,
                extra={
                    "dataset_statistics": _dataset_statistics_extra_with_tables(
                        datasets,
                        stat_table_summaries=stat_table_summaries,
                    ),
                    "statistics_tables": stat_table_summaries,
                    "paper_has_statistics": any(ds.statistics_mentioned for ds in datasets),
                },
            )
        )
        self._fire_progress()

    # ── Internal LLM call ─────────────────────────────────────────────────

    def _extra_body(self) -> dict | None:
        """Return model-specific extra_body parameters for chat.completions.create().

        Uses the shared helper so behavior is consistent across scripts.
        """
        return extra_body_for_model(self.model_name)

    def _probe_usage_limits(self) -> dict[str, Any]:
        """Fetch a compact snapshot of endpoint request-limit headers."""
        try:
            raw = self._client.chat.completions.with_raw_response.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant. Respond briefly."},
                    {"role": "user", "content": "Say 'OK' and nothing else."},
                ],
                max_tokens=8,
                temperature=0.0,
                extra_body=self._extra_body(),
            )
            headers = _headers_to_dict(getattr(raw, "headers", None))
        except Exception as exc:
            logger.debug("Usage limit probe failed for %s: %s", self.model_name, exc)
            return {
                "checked_at": datetime.now(UTC).isoformat(),
                "model": self.model_name,
                "note": f"Usage limit probe failed: {exc}",
            }

        windows: dict[str, dict[str, str]] = {}
        for window in ("second", "minute", "hour", "day", "month"):
            limit = headers.get(f"x-ratelimit-limit-{window}")
            remaining = headers.get(f"x-ratelimit-remaining-{window}")
            if limit or remaining:
                windows[window] = {
                    "limit": limit or "?",
                    "remaining": remaining or "?",
                }

        snapshot: dict[str, Any] = {
            "checked_at": datetime.now(UTC).isoformat(),
            "model": self.model_name,
            "windows": windows,
        }
        burst_limit = headers.get("ratelimit-limit")
        burst_remaining = headers.get("ratelimit-remaining")
        if burst_limit or burst_remaining:
            snapshot["burst"] = {
                "limit": burst_limit or "?",
                "remaining": burst_remaining or "?",
                "reset": headers.get("ratelimit-reset") or headers.get("retry-after"),
            }
        if not windows and "burst" not in snapshot:
            snapshot["note"] = (
                "Endpoint did not return explicit rate-limit headers on the probe request."
            )
        return snapshot

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=2, min=5, max=60),
        reraise=True,
    )
    def _call(
        self,
        system_prompt: str,
        user_content: str,
        max_tokens: int | None = None,
        call_type: str = "llm",
        call_extra: dict | None = None,
    ) -> str:
        request_start = time.perf_counter()
        first_token_time: float | None = None
        chunks: list[str] = []
        prompt_tokens: int | None = None
        completion_tokens: int | None = None
        extra_body = self._extra_body()
        try:
            if self.streaming:
                # Streaming path: captures TTFT and tokens/sec
                stream = self._client.chat.completions.create(
                    model=self.model_name,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_content},
                    ],
                    max_tokens=max_tokens or cfg.llm_max_tokens,
                    temperature=cfg.llm_temperature,
                    stream=True,
                    stream_options={"include_usage": True},
                    extra_body=extra_body,
                )
                for chunk in stream:
                    if getattr(chunk, "usage", None) is not None:
                        prompt_tokens = chunk.usage.prompt_tokens
                        completion_tokens = chunk.usage.completion_tokens
                    if not chunk.choices:
                        continue
                    delta = chunk.choices[0].delta.content
                    if delta:
                        if first_token_time is None:
                            first_token_time = time.perf_counter()
                        chunks.append(delta)
                content = "".join(chunks).strip()
            else:
                # Non-streaming path (production default)
                response = self._client.chat.completions.create(
                    model=self.model_name,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_content},
                    ],
                    max_tokens=max_tokens or cfg.llm_max_tokens,
                    temperature=cfg.llm_temperature,
                    extra_body=extra_body,
                )
                choice = response.choices[0]
                content = (choice.message.content or "").strip()
                if response.usage:
                    prompt_tokens = response.usage.prompt_tokens
                    completion_tokens = response.usage.completion_tokens

        except Exception as exc:
            elapsed = time.perf_counter() - request_start
            # Better error classification for debugging
            exc_type = type(exc).__name__
            if isinstance(exc, RateLimitError):
                logger.warning(
                    "LLM request to %r rate limited (429): %s — will retry with backoff",
                    self.model_name,
                    exc,
                )
            elif isinstance(exc, APIStatusError):
                status = exc.status_code
                if status >= 500:
                    logger.warning(
                        "LLM endpoint error (HTTP %d) for %r: %s — will retry",
                        status,
                        self.model_name,
                        exc,
                    )
                else:
                    logger.warning(
                        "LLM API error (HTTP %d) for %r: %s — will retry",
                        status,
                        self.model_name,
                        exc,
                    )
            else:
                logger.warning(
                    "LLM request to %r failed in %.2f s (%s): %s — will retry",
                    self.model_name,
                    elapsed,
                    exc_type,
                    exc,
                )
            raise

        end_time = time.perf_counter()
        total_s = end_time - request_start
        ttft_s = (first_token_time - request_start) if first_token_time else None
        gen_s = (end_time - first_token_time) if first_token_time else total_s

        # Tokens per second: prefer API-reported completion_tokens
        if completion_tokens and gen_s > 0:
            tps: float | None = completion_tokens / gen_s
        elif content and gen_s > 0:
            tps = (len(content) / 4.0) / gen_s  # rough estimate: ~4 chars/token
        else:
            tps = None

        record = CallRecord(
            call_type=call_type,
            system_prompt=system_prompt,
            user_content=user_content,
            raw_response=content,
            input_chars=len(system_prompt) + len(user_content),
            output_chars=len(content),
            duration_s=total_s,
            ttft_s=ttft_s,
            tokens_per_sec=tps,
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            success=bool(content),
            extra=call_extra or {},
        )
        self._call_log.append(record)

        if not content:
            # Some endpoints return HTTP 200 with an empty body when
            # rate-limiting or encountering a transient error.  Raising here
            # allows the @retry decorator on _call() to back off and retry.
            logger.warning(
                "Model %r returned empty content "
                "(input_chars=%d, duration=%.2f s) — likely rate limit or quota issue, will retry",
                self.model_name,
                record.input_chars,
                total_s,
            )
            raise RuntimeError(
                f"Model {self.model_name!r} returned empty content "
                f"(input_chars={record.input_chars}, duration={total_s:.2f}s) — "
                f"likely rate limit or quota exceeded — treating as transient error"
            )
        else:
            logger.debug(
                "Model %r [%s]: %d in → %d out chars | %.2f s total%s",
                self.model_name,
                call_type,
                record.input_chars,
                record.output_chars,
                total_s,
                f" | TTFT {ttft_s:.2f}s | {tps:.0f} tok/s" if ttft_s else "",
            )
        return content

    def _call_json(
        self,
        system_prompt: str,
        user_content: str,
        max_tokens: int | None = None,
        call_type: str = "llm",
        call_extra: dict | None = None,
    ) -> Any:
        """Call LLM, parse JSON from the response.

        Handles:
        - Markdown code fences (```json ... ```)
        - Thinking-model blocks (<think>...</think>, common in DeepSeek/Qwen3)
        - Regex fallback: extracts first JSON object/array if direct parse fails
        """
        raw = self._call(
            system_prompt,
            user_content,
            max_tokens,
            call_type=call_type,
            call_extra=call_extra,
        )
        if not raw:
            raise ValueError(
                f"Model {self.model_name!r} returned an empty response. "
                "The input may be too long — check the model's context-window limit."
            )

        # 1. Strip thinking-model tags (<think>…</think>)
        clean = re.sub(r"<think>.*?</think>", "", raw, flags=re.DOTALL).strip()
        # 2. Strip markdown code fences: ```json ... ``` or ``` ... ```
        clean = re.sub(r"^```(?:json)?\s*", "", clean, flags=re.MULTILINE)
        clean = re.sub(r"\s*```$", "", clean, flags=re.MULTILINE).strip()

        parse_method = "direct"
        try:
            result = json.loads(clean)
        except json.JSONDecodeError:
            # 3. Regex fallback: find first {...} or [...]
            result = None
            for pattern in [r"\{[\s\S]*\}", r"\[[\s\S]*\]"]:
                m = re.search(pattern, clean)
                if m:
                    try:
                        result = json.loads(m.group(0))
                        parse_method = "regex"
                        break
                    except json.JSONDecodeError:
                        pass
            if result is None:
                result = parse_json_lenient(clean)
                if result is not None:
                    parse_method = "lenient_repair"
            if result is None:
                logger.debug("Raw LLM response (first 500 chars): %s", raw[:500])
                logger.error("JSON parse error from %r", self.model_name)
                if self._call_log:
                    self._call_log[-1].parse_error = (
                        f"JSON parse failed — raw (first 200 chars): {raw[:200]}"
                    )
                raise ValueError(  # noqa: B904
                    f"JSON parse error from {self.model_name!r}: could not extract valid JSON"
                )

        if self._call_log:
            self._call_log[-1].parsed_result = result
            if parse_method != "direct":
                self._call_log[-1].extra = {
                    **self._call_log[-1].extra,
                    "json_parse_method": parse_method,
                }
        return result

    # ── Prompt loading ─────────────────────────────────────────────────────

    @staticmethod
    def _read_prompt(filename: str) -> str:
        path = cfg.prompts_dir / filename
        if not path.exists():
            raise FileNotFoundError(f"Prompt not found: {path}")
        return path.read_text(encoding="utf-8").strip()

    def _read_result_prompt(self, full_mode: bool = False) -> str:
        if self.result_output_format == "yaml":
            yaml_name = (
                "full_result_extraction_yaml.txt" if full_mode else "result_extraction_yaml.txt"
            )
            yaml_path = cfg.prompts_dir / yaml_name
            if yaml_path.exists():
                return yaml_path.read_text(encoding="utf-8").strip()
        return self._read_prompt(
            "full_result_extraction.txt" if full_mode else "result_extraction.txt"
        )

    def _parse_structured_response(self, raw: str, output_format: str) -> Any:
        if not raw:
            raise ValueError(
                f"Model {self.model_name!r} returned an empty response. "
                "The input may be too long — check the model's context-window limit."
            )

        clean = re.sub(r"<think>.*?</think>", "", raw, flags=re.DOTALL).strip()
        clean = re.sub(r"^```(?:json|yaml|yml)?\s*", "", clean, flags=re.MULTILINE)
        clean = re.sub(r"\s*```$", "", clean, flags=re.MULTILINE).strip()

        fmt = output_format.lower()
        parse_errors: list[str] = []
        parsers: list[tuple[str, Any]] = []
        if fmt == "yaml":
            parsers = [("yaml", yaml.safe_load), ("json", json.loads)]
        else:
            parsers = [("json", json.loads), ("yaml", yaml.safe_load)]

        for parser_name, parser in parsers:
            try:
                result = parser(clean)
                if self._call_log:
                    self._call_log[-1].parsed_result = result
                    if parser_name != fmt:
                        self._call_log[-1].extra = {
                            **self._call_log[-1].extra,
                            "structured_parse_method": parser_name,
                        }
                return result
            except Exception as exc:
                parse_errors.append(f"{parser_name}: {exc}")

        repaired = parse_json_lenient(clean)
        if repaired is not None:
            if self._call_log:
                self._call_log[-1].parsed_result = repaired
                self._call_log[-1].extra = {
                    **self._call_log[-1].extra,
                    "structured_parse_method": "lenient_repair",
                }
            return repaired

        # Regex fallback for JSON-shaped content embedded in extra prose.
        for pattern in [r"\{[\s\S]*\}", r"\[[\s\S]*\]"]:
            m = re.search(pattern, clean)
            if not m:
                continue
            try:
                result = json.loads(m.group(0))
                if self._call_log:
                    self._call_log[-1].parsed_result = result
                    self._call_log[-1].extra = {
                        **self._call_log[-1].extra,
                        "structured_parse_method": "json_regex",
                    }
                return result
            except Exception as exc:
                parse_errors.append(f"json_regex: {exc}")

        logger.debug("Raw LLM response (first 500 chars): %s", raw[:500])
        if self._call_log:
            self._call_log[-1].parse_error = "; ".join(parse_errors)[:500]
        raise ValueError(
            f"Structured parse error from {self.model_name!r}: could not parse as {output_format}"
        )

    def _call_structured(
        self,
        system_prompt: str,
        user_content: str,
        max_tokens: int | None = None,
        call_type: str = "llm",
        call_extra: dict | None = None,
        output_format: str = "json",
    ) -> Any:
        raw = self._call(
            system_prompt,
            user_content,
            max_tokens,
            call_type=call_type,
            call_extra={**(call_extra or {}), "requested_output_format": output_format},
        )
        return self._parse_structured_response(raw, output_format)

    # ── Extraction tasks ───────────────────────────────────────────────────

    def screen_paper(self, title: str, abstract: str) -> ScreenResult:
        """Stage 1: decide from title+abstract whether a full extraction is warranted."""
        prompt = self._read_prompt("benchmark_check.txt")
        user_content = f"Title: {title}\n\nAbstract:\n{abstract}"
        try:
            raw = self._call_json(prompt, user_content, max_tokens=512, call_type="screen_paper")
            result = ScreenResult.model_validate(raw)
            self._fire_progress()
            return result
        except Exception as exc:
            logger.warning("Abstract screening failed: %s", exc)
            self._fire_progress()
            # Fail open: if screening errors, proceed with full extraction
            return ScreenResult(
                has_benchmark_results=True,
                has_new_benchmark=True,
                confidence=0.0,
                notes=f"Screening failed ({exc}); defaulting to full extraction",
            )

    def discover_datasets(self, paper_text: str, tables_text: str) -> DatasetList:
        """Identify which benchmark datasets have experiments in this paper.

        Context sent to the model:
          - First _DISCOVERY_INTRO_CHARS of the paper (covers abstract + intro)
          - Up to _TABLE_SECTION_SIZE chars of table content (structured markdown
            for HTML papers, or table-section chunks for text-only papers)
        """
        prompt = self._read_prompt("dataset_discovery.txt")
        intro = paper_text[:_DISCOVERY_INTRO_CHARS]
        tables_preview = tables_text[:_TABLE_SECTION_SIZE]
        parts = [f"=== PAPER INTRO / ABSTRACT ===\n{intro}"]
        if tables_preview.strip():
            parts.append(f"=== TABLE PREVIEWS ===\n{tables_preview}")
        precheck_source = "\n\n".join(part for part in [intro, tables_preview] if part.strip())
        precheck_hits = _ripgrep_dataset_name_hits(precheck_source)
        if precheck_hits:
            parts.append(
                "=== RIPGREP PRE-CHECK: CANONICAL DATASET NAMES FOUND IN THE INPUT TEXT ===\n"
                "Use these as candidate dataset names when they correspond to real benchmark results in this paper.\n"
                + "\n".join(f"- {name}" for name in precheck_hits)
            )
        known_hint = _get_known_dataset_names_hint()
        if known_hint:
            parts.append(
                "=== CANONICAL DATASET NAMES ALREADY IN OUR DATABASE ===\n"
                "When the paper uses one of these datasets, return that canonical name exactly instead of inventing a variant spelling.\n"
                f"{known_hint}"
            )
        user_content = "\n\n".join(parts)
        try:
            raw = self._call_json(
                prompt,
                user_content,
                max_tokens=cfg.llm_max_tokens,
                call_type="discover_datasets",
            )
            result = DatasetList.model_validate(raw)
            logger.info(
                "Dataset discovery: found %d dataset(s): %s",
                len(result.datasets),
                [d.name for d in result.datasets],
            )
            if self._call_log:
                self._call_log[-1].extra = {
                    **self._call_log[-1].extra,
                    "discovered_datasets": [d.name for d in result.datasets],
                    "dataset_precheck_hits": precheck_hits,
                }
            self._fire_progress()
            return result
        except Exception as exc:
            logger.warning("Dataset discovery failed: %s", exc)
            self._fire_progress()
            return DatasetList()

    def discover_datasets_from_latex(self, latex_paper: Any) -> DatasetList:
        """Dataset discovery using structured LaTeX source.

        This variant sends all table captions (compact, one-per-line) and
        section headings — much richer signal than raw PDF text.  Tables in
        appendices are included.

        Args:
            latex_paper: a ``LatexPaper`` instance (imported lazily to avoid
                         circular imports — only ``all_table_captions``,
                         ``section_headings``, and ``intro_text`` are accessed).
        """
        prompt = self._read_prompt("dataset_discovery.txt")

        # Build enriched table catalogue: full caption + column headers + first-column values.
        # (Same detail level as the table-selection calls that come later, so the model sees
        #  enough to recognise which tables contain results and which datasets they cover.)
        table_lines: list[str] = []
        for t in latex_paper.tables:
            appendix = " [appendix]" if t.in_appendix else ""
            label = f" ({t.label})" if t.label else ""
            caption = (t.caption or "").strip()  # full caption — no truncation
            header = self._table_header(t)
            first_col = self._table_first_column(t)
            line = f"Table {t.number}{label}{appendix}: {caption}"
            if header:
                line += f"\n  Columns: {header}"
            if first_col:
                line += f"\n  Row values (col 1): {first_col}"
            table_lines.append(line)
        table_catalogue = "\n".join(table_lines)

        parts = [
            f"=== PAPER INTRO ===\n{latex_paper.intro_text}",
            f"=== ALL TABLE CAPTIONS (with column headers and first-column model names) ===\n{table_catalogue}",
            f"=== SECTION HEADINGS ===\n{latex_paper.section_headings}",
        ]
        exp_text = latex_paper.experiment_text
        exp_excerpts = _discovery_text_excerpts(exp_text)
        high_precision_source_parts = [
            latex_paper.all_table_captions,
            table_catalogue,
        ]
        high_precision_source = "\n\n".join(
            part for part in high_precision_source_parts if part.strip()
        )
        precheck_hits = _ripgrep_dataset_name_hits(high_precision_source)
        precheck_hits = list(
            dict.fromkeys(precheck_hits + _noncanonical_dataset_hints(high_precision_source))
        )
        if precheck_hits:
            parts.append(
                "=== RIPGREP PRE-CHECK: CANONICAL DATASET NAMES FOUND IN expanded.tex ===\n"
                "These are exact string hits against the website's canonical dataset list. Use them as candidate "
                "dataset names only when the paper actually reports benchmark results for them.\n"
                + "\n".join(f"- {name}" for name in precheck_hits)
            )
        # Include experiment-section excerpts so the LLM can see dataset names
        # that appear only in the body or appendix (not in intro or captions).
        if exp_excerpts:
            parts.append(f"=== EXPERIMENT SECTION EXCERPT (head) ===\n{exp_excerpts[0]}")
            if len(exp_excerpts) > 1:
                parts.append(f"=== EXPERIMENT SECTION EXCERPT (tail) ===\n{exp_excerpts[1]}")
        # Inject known-dataset hints from the DB so the model matches canonical names.
        known_hint = _get_known_dataset_names_hint()
        if known_hint:
            parts.append(
                "=== CANONICAL DATASET NAMES ALREADY IN OUR DATABASE ===\n"
                "When the paper uses one of these datasets, return that canonical name exactly instead of inventing a variant spelling.\n"
                f"{known_hint}"
            )
        user_content = "\n\n".join(parts)
        try:
            raw = self._call_json(
                prompt,
                user_content,
                max_tokens=cfg.llm_max_tokens,
                call_type="discover_datasets_latex",
            )
            result = DatasetList.model_validate(raw)
            if precheck_hits:
                result = _merge_dataset_lists(
                    result,
                    DatasetList(datasets=[DatasetInfo(name=name) for name in precheck_hits]),
                )
            logger.info(
                "LaTeX dataset discovery: found %d dataset(s): %s",
                len(result.datasets),
                [d.name for d in result.datasets],
            )
            if self._call_log:
                self._call_log[-1].extra = {
                    **self._call_log[-1].extra,
                    "discovered_datasets": [d.name for d in result.datasets],
                    "dataset_precheck_hits": precheck_hits,
                }
            self._fire_progress()
            return result
        except Exception as exc:
            logger.warning("LaTeX dataset discovery failed: %s", exc)
            self._fire_progress()
            return DatasetList()

    def _discover_datasets_from_latex_fallback(
        self,
        latex_paper: Any,
        paper_text: str,
        effective_tables: list[Any],
    ) -> DatasetList:
        """Retry discovery with compact text/table previews when LaTeX discovery misses."""
        fallback_parts = [
            latex_paper.intro_text,
            latex_paper.section_headings,
            latex_paper.experiment_text,
            paper_text,
        ]
        fallback_paper_text = "\n\n".join(part for part in fallback_parts if part and part.strip())
        if effective_tables:
            fallback_tables_text = "\n\n".join(
                f"[{getattr(t, 'caption', '') or ''}]\n{getattr(t, 'markdown', str(t))}"
                for t in effective_tables
            )
        else:
            fallback_tables_text = latex_paper.all_table_captions or ""

        fallback_result = self.discover_datasets(fallback_paper_text, fallback_tables_text)

        exact_hit_source = "\n\n".join(
            part
            for part in [
                latex_paper.intro_text,
                latex_paper.section_headings,
                latex_paper.all_table_captions,
                latex_paper.experiment_text,
                paper_text,
            ]
            if part and part.strip()
        )
        exact_hits = DatasetList(
            datasets=[
                DatasetInfo(name=name) for name in _ripgrep_dataset_name_hits(exact_hit_source)
            ]
        )
        merged = _merge_dataset_lists(fallback_result, exact_hits)
        if merged.datasets:
            logger.info(
                "Fallback dataset discovery recovered %d dataset(s): %s",
                len(merged.datasets),
                [d.name for d in merged.datasets],
            )
        return merged

    @staticmethod
    def _table_header(table: Any) -> str:
        """Extract first data row (column headers) from any supported table type."""
        # LatexTable exposes a .header property
        h = getattr(table, "header", None)
        if h:
            return h
        # ParsedTable / any markdown table: find first non-separator line
        md = getattr(table, "markdown", "") or ""
        for line in md.splitlines():
            stripped = line.strip()
            if stripped.startswith("|") and not re.match(r"^\|[-| :]+\|", stripped):
                cols = [c.strip() for c in stripped.split("|") if c.strip()]
                return " | ".join(cols)[:200]
        return ""

    @staticmethod
    def _table_first_data_row(table: Any) -> str:
        """Return the first non-header data row of a table as a compact string.

        Helps the table-selection LLM recognise result tables by their actual
        values (e.g. "GCN | 501K | 0.2634 | 0.0012") rather than just captions.
        Returns an empty string when the table cannot be parsed.
        """
        md = getattr(table, "markdown", "") or ""
        past_separator = False
        for line in md.splitlines():
            stripped = line.strip()
            if not stripped.startswith("|"):
                continue
            if re.match(r"^\|[-| :]+\|", stripped):
                past_separator = True
                continue
            if past_separator:
                cols = [c.strip() for c in stripped.split("|") if c.strip()]
                return " | ".join(cols)[:200]
        return ""

    @staticmethod
    def _table_first_column(table: Any) -> str:
        """Return the first-column values from all data rows as a compact list.

        This tells the table-selection LLM whether the table's rows are model
        names (e.g. "GCN, GCNII, GIN") or dataset names (e.g. "Cora, CiteSeer")
        rather than just showing captions and column headers.
        Returns an empty string when the table cannot be parsed.
        """
        md = getattr(table, "markdown", "") or ""
        past_separator = False
        values: list[str] = []
        for line in md.splitlines():
            stripped = line.strip()
            if not stripped.startswith("|"):
                continue
            if re.match(r"^\|[-| :]+\|", stripped):
                past_separator = True
                continue
            if past_separator:
                cols = [c.strip() for c in stripped.split("|") if c.strip()]
                if cols:
                    values.append(cols[0])
                if len(values) >= 8:  # cap to keep context compact
                    break
        if not values:
            return ""
        return ", ".join(values[:8])

    @staticmethod
    def _is_real_table(table: Any) -> bool:
        """Return True if the table is likely a genuine data table (not a formula block).

        A LaTeX 'table' environment is considered real when it either:
        - has a non-trivial caption (more than a few characters), OR
        - has more than 3 non-empty lines in its body (enough to contain rows).

        This filters out equation-style table environments that LaTeX authors
        sometimes misuse for alignment of formulae.
        """
        caption = (getattr(table, "caption", "") or "").strip()
        if len(caption) > 5:
            return True
        body = (getattr(table, "markdown", "") or getattr(table, "body", "")).strip()
        non_empty = sum(1 for ln in body.splitlines() if ln.strip())
        return non_empty > 3

    # ── LLM-based table selection ─────────────────────────────────────────

    _TABLE_SELECTION_THRESHOLD = 4  # min tables before we bother with an LLM call

    def select_tables_for_dataset(
        self,
        dataset_name: str,
        tables: list,
        table_refs: list[str] | None = None,
    ) -> list:
        """Ask the LLM to select which tables are relevant for *dataset_name*.

        Sends each table's number, caption, and first-row header to the model.
        Returns a filtered list.  Falls back to the full list on any error.
        Skips the LLM call entirely when there are ≤ _TABLE_SELECTION_THRESHOLD tables.
        """
        if len(tables) <= self._TABLE_SELECTION_THRESHOLD:
            return tables

        entries: list[str] = []
        for t in tables:
            num = getattr(t, "number", None)
            if num is None:
                num = tables.index(t) + 1
            caption = " ".join((getattr(t, "caption", "") or "").split())
            header = self._table_header(t)
            first_row = self._table_first_data_row(t)
            first_col = self._table_first_column(t)
            appendix = " [appendix]" if getattr(t, "in_appendix", False) else ""
            entry = f"Table {num}{appendix}: {caption}"
            if header:
                entry += f"\n  Columns: {header}"
            if first_row:
                entry += f"\n  First row: {first_row}"
            if first_col:
                entry += f"\n  Row values (col 1): {first_col}"
            entries.append(entry)

        prompt = self._read_prompt("table_selection.txt")
        user_content = f'TARGET DATASET: "{dataset_name}"\n\n' + "\n\n".join(entries)
        if table_refs:
            user_content += f"\n\nHINT from discovery step: results likely in {table_refs}"

        try:
            raw = self._call_json(
                prompt,
                user_content,
                max_tokens=512,
                call_type=f"select_tables:{dataset_name}",
            )
            numbers = raw.get("relevant_table_numbers", [])
            if not isinstance(numbers, list) or not numbers:
                logger.warning(
                    "Table selection for %r returned no numbers — using all tables", dataset_name
                )
                self._fire_progress()
                return tables
            num_set = {int(n) for n in numbers}
            selected = [t for t in tables if getattr(t, "number", tables.index(t) + 1) in num_set]
            if not selected:
                self._fire_progress()
                return tables
            if self._call_log:
                self._call_log[-1].extra = {
                    **self._call_log[-1].extra,
                    "selected_tables": sorted(num_set),
                    "tables_total": len(tables),
                }
            logger.info(
                "Table selection for %r: %d/%d tables selected: %s",
                dataset_name,
                len(selected),
                len(tables),
                sorted(num_set),
            )
            self._fire_progress()
            return selected
        except Exception as exc:
            logger.warning(
                "Table selection for %r failed: %s — using all tables", dataset_name, exc
            )
            self._fire_progress()
            return tables

    def select_tables_for_all_datasets(
        self,
        datasets: list[DatasetInfo],
        tables: list,
    ) -> dict[str, list]:
        """One LLM call to select relevant tables for ALL datasets at once.

        Returns a mapping dataset_name → filtered table list.
        Falls back to ``{ds.name: tables}`` for all datasets on any error.
        Skips the LLM call when there are ≤ _TABLE_SELECTION_THRESHOLD tables.
        """
        fallback = {ds.name: tables for ds in datasets}
        if len(tables) <= self._TABLE_SELECTION_THRESHOLD:
            return fallback

        # Build the shared table catalogue (same for all datasets)
        entries: list[str] = []
        for t in tables:
            num = getattr(t, "number", None)
            if num is None:
                num = tables.index(t) + 1
            caption = " ".join((getattr(t, "caption", "") or "").split())
            header = self._table_header(t)
            first_row = self._table_first_data_row(t)
            first_col = self._table_first_column(t)
            appendix = " [appendix]" if getattr(t, "in_appendix", False) else ""
            entry = f"Table {num}{appendix}: {caption}"
            if header:
                entry += f"\n  Columns: {header}"
            if first_row:
                entry += f"\n  First row: {first_row}"
            if first_col:
                entry += f"\n  Row values (col 1): {first_col}"
            entries.append(entry)

        dataset_names = [ds.name for ds in datasets]
        prompt = self._read_prompt("table_selection_multi.txt")
        user_content = (
            "TARGET DATASETS:\n"
            + "\n".join(f"- {n}" for n in dataset_names)
            + _dataset_statistics_hint_block(datasets)
            + "\n\n"
            + "\n\n".join(entries)
        )

        # Token budget: ~20 tokens per dataset name + ~50 per table number → generous
        max_tokens = max(256, len(datasets) * 30 + len(tables) * 20)

        try:
            raw = self._call_json(
                prompt,
                user_content,
                max_tokens=max_tokens,
                call_type="select_tables:all",
            )
            if not isinstance(raw, dict):
                logger.warning("select_tables:all returned non-dict — using all tables")
                self._fire_progress()
                return fallback

            # Build result: for each dataset resolve its table number set → table objects
            num_to_table = {getattr(t, "number", tables.index(t) + 1): t for t in tables}
            result: dict[str, list] = {}
            all_selected: dict[str, list[int]] = {}
            for ds in datasets:
                numbers = raw.get(ds.name, [])
                if not isinstance(numbers, list) or not numbers:
                    result[ds.name] = tables  # fallback to all
                    all_selected[ds.name] = []
                else:
                    num_set = {int(n) for n in numbers}
                    selected = [num_to_table[n] for n in sorted(num_set) if n in num_to_table]
                    result[ds.name] = selected if selected else tables
                    all_selected[ds.name] = sorted(num_set)

            stat_table_summaries = _statistics_table_summaries(tables)
            if self._call_log:
                self._call_log[-1].extra = {
                    **self._call_log[-1].extra,
                    "selected_tables_per_dataset": all_selected,
                    "tables_total": len(tables),
                    "dataset_statistics": _dataset_statistics_extra_with_tables(
                        datasets,
                        stat_table_summaries=stat_table_summaries,
                    ),
                    "statistics_tables": stat_table_summaries,
                    "paper_has_statistics": any(ds.statistics_mentioned for ds in datasets),
                }
            logger.info("select_tables:all → %s", all_selected)
            self._fire_progress()
            return result

        except Exception as exc:
            logger.warning("select_tables:all failed: %s — using all tables", exc)
            self._fire_progress()
            return fallback

    @staticmethod
    def _build_rag_context(
        paper_text: str,
        tables: list,
        dataset_name: str,
        max_text_chars: int = 10_000,
        max_table_chars: int = 10_000,
        already_selected: bool = False,
    ) -> tuple[str, dict]:
        """Build a dataset-focused context for per-dataset extraction.

        Paper text is used as RAG: only paragraphs mentioning the dataset (plus
        adjacent paragraphs for context) are included.  Tables are pasted
        directly.  When ``already_selected`` is True the caller has already
        run LLM-based table selection, so all tables in ``tables`` are used
        as-is; otherwise captions are matched against the dataset name as a
        fallback heuristic.

        Returns (context_str, rag_stats) where rag_stats is a dict describing
        which paragraphs and tables were selected.
        """
        # ── RAG: find paragraphs that mention this dataset ────────────────
        dataset_lower = dataset_name.lower()
        paragraphs = paper_text.split("\n\n")
        selected_indices: set[int] = set()
        for i, para in enumerate(paragraphs):
            if dataset_lower in para.lower():
                # include the paragraph itself plus one before and after
                for j in range(max(0, i - 1), min(len(paragraphs), i + 2)):
                    selected_indices.add(j)

        # Maintain document order and deduplicate
        rag_parts: list[str] = []
        for i in sorted(selected_indices):
            p = paragraphs[i].strip()
            if p:
                rag_parts.append(p)

        rag_text = "\n\n".join(rag_parts)[:max_text_chars]
        rag_text_truncated = len("\n\n".join(rag_parts)) > max_text_chars

        # ── Tables ────────────────────────────────────────────────────────
        table_selection_mode = "none"
        relevant_table_captions: list[str] = []
        if tables:

            def _caption(t: Any) -> str:
                return (getattr(t, "caption", None) or "").lower()

            def _markdown(t: Any) -> str:
                return getattr(t, "markdown", None) or str(t)

            if already_selected:
                # LLM already chose these tables — use all of them directly
                relevant = list(tables)
                table_selection_mode = "llm_preselected"
            else:
                # Heuristic fallback: prefer captions that mention the dataset
                relevant = [t for t in tables if dataset_lower in _caption(t)]
                if relevant:
                    table_selection_mode = "caption_match"
                else:
                    relevant = [t for t in tables if len(_caption(t)) > 20]
                    table_selection_mode = "non_formula_fallback" if relevant else "all_fallback"
                if not relevant:
                    relevant = list(tables)
                    table_selection_mode = "all_fallback"

            relevant_table_captions = [_caption(t)[:80] for t in relevant]

            table_parts = []
            for t in relevant:
                cap = _caption(t)
                md = _markdown(t)
                header = f"[Caption: {cap[:120]}]\n" if cap else ""
                table_parts.append(f"{header}{md}")
            tables_str = "\n\n---\n\n".join(table_parts)[:max_table_chars]
        else:
            tables_str = ""

        parts: list[str] = []
        if rag_text:
            parts.append(f"=== PAPER TEXT (sections mentioning '{dataset_name}') ===\n{rag_text}")
        if tables_str:
            parts.append(f"=== TABLES (directly pasted) ===\n{tables_str}")
        context_str = "\n\n".join(parts)

        rag_stats = {
            "dataset": dataset_name,
            "paragraphs_total": len(paragraphs),
            "paragraphs_selected": len(selected_indices),
            "rag_text_chars": len(rag_text),
            "rag_text_truncated": rag_text_truncated,
            "tables_total": len(tables),
            "tables_selected": len(relevant_table_captions) if tables else 0,
            "table_selection_mode": table_selection_mode,
            "selected_table_captions": relevant_table_captions,
            "context_total_chars": len(context_str),
        }
        return context_str, rag_stats

    def extract_results_two_step(
        self,
        paper_text: str,
        tables: list,
        latex_paper: Any = None,
        paper_title: str = "",
    ) -> ExtractionOutput:
        """Two-step extraction: first discover datasets, then extract per dataset.

        Args:
            paper_text: Full plain-text content of the paper (used for text RAG
                when no latex_paper is provided).
            tables: List of ParsedTable / LatexTable objects.  When latex_paper
                is provided this argument is ignored (latex_paper.tables is used
                instead, which includes appendix tables).
            latex_paper: Optional ``LatexPaper`` from the LaTeX source download.
                When present, it improves both discovery (all table captions +
                section headings) and per-dataset RAG (experiment-section text
                instead of the full paper).
        """
        intro_model_hint = _extract_proposed_model_hint(
            paper_title,
            _paper_intro_text(paper_text, latex_paper),
        )

        # ── Choose tables and text source ─────────────────────────────────
        if latex_paper is not None:
            # Filter out formula/alignment environments masquerading as tables:
            # only keep tables with a real caption OR more than 3 content lines.
            all_tables = latex_paper.tables
            effective_tables = [t for t in all_tables if self._is_real_table(t)]
            n_filtered = len(all_tables) - len(effective_tables)
            if n_filtered:
                logger.info(
                    "Filtered out %d trivial/formula pseudo-tables (no caption, ≤3 lines); "
                    "%d real tables remain",
                    n_filtered,
                    len(effective_tables),
                )
            # Use only experiment-related sections for text RAG — much more
            # focused than the full paper text. Strip table environments so
            # that table bodies are not also present in the prose RAG: tables
            # are handled separately via ds_tables / _build_rag_context.
            rag_text = _strip_table_environments(latex_paper.experiment_text or paper_text)
        elif tables:
            effective_tables = tables
            rag_text = paper_text
        else:
            effective_tables = []
            rag_text = paper_text

        # ── Step 1: discover datasets ──────────────────────────────────────
        if latex_paper is not None:
            datasets = self.discover_datasets_from_latex(latex_paper)
            if not datasets.datasets:
                logger.warning(
                    "LaTeX discovery returned no datasets; retrying with generic discovery fallback"
                )
                datasets = self._discover_datasets_from_latex_fallback(
                    latex_paper, paper_text, effective_tables
                )
        elif effective_tables:
            tables_text = "\n\n".join(
                f"[{getattr(t, 'caption', '') or ''}]\n{getattr(t, 'markdown', str(t))}"
                for t in effective_tables
            )
            datasets = self.discover_datasets(paper_text, tables_text)
        else:
            # No HTML and no LaTeX: synthesise a table preview from table-section
            # chunks in the plain text.
            table_sections = _split_into_table_sections(paper_text, _TABLE_SECTION_SIZE)
            tables_text = "\n\n---\n\n".join(table_sections[1:]) if len(table_sections) > 1 else ""
            datasets = self.discover_datasets(paper_text, tables_text)

        if not datasets.datasets:
            logger.warning("Step 1 returned no datasets after fallback — returning empty result")
            return ExtractionOutput(
                results=[],
                extraction_notes="Dataset discovery returned no datasets.",
                extraction_confidence="low",
            )

        stats_precheck_text = rag_text
        if latex_paper is not None:
            stats_precheck_text = "\n\n".join(
                part
                for part in [
                    latex_paper.intro_text,
                    latex_paper.experiment_text,
                    latex_paper.all_table_captions,
                    rag_text,
                ]
                if part and part.strip()
            )
        datasets = _apply_statistics_ripgrep_precheck(datasets, stats_precheck_text)
        _enrich_dataset_statistics_from_tables(datasets, effective_tables)
        stat_table_summaries = _statistics_table_summaries(effective_tables)
        self._emit_discovery_statistics_summary(
            datasets.datasets,
            stat_table_summaries=stat_table_summaries,
        )

        # Override primary_metric from the DB when available.
        # The discovery LLM may return "Hits@K" for PCQM-Contact while the DB
        # stores the canonical "MRR"; using the DB value ensures the FOCUS
        # instruction in Step 2 requests the correct metric.
        try:
            from backend.db import get_session_factory
            from backend.models import Dataset as _DatasetModel

            _Session = get_session_factory()
            with _Session() as _s:
                _db_metrics = {
                    r.name.lower(): r.primary_metric
                    for r in _s.query(_DatasetModel.name, _DatasetModel.primary_metric).all()
                    if r.primary_metric
                }
            for ds in datasets.datasets:
                db_pm = _db_metrics.get(ds.name.lower())
                if db_pm and db_pm != ds.primary_metric:
                    if is_qm9_dataset(ds.name):
                        ds.primary_metric = QM9_DEFAULT_METRIC
                    else:
                        logger.info(
                            "Overriding primary_metric for %r: %r → %r (from DB)",
                            ds.name,
                            ds.primary_metric,
                            db_pm,
                        )
                        ds.primary_metric = db_pm
                elif is_qm9_dataset(ds.name):
                    ds.primary_metric = QM9_DEFAULT_METRIC
        except Exception as _exc:
            logger.debug("DB primary_metric lookup skipped: %s", _exc)

        # Step 2: per-dataset focused extraction
        prompt = self._read_result_prompt()
        all_results: list[ResultEntry] = []
        proposed: ProposedModel | None = None
        baselines: list[BaselineModelInfo] = []
        notes_parts: list[str] = []
        confidence_levels: list[str] = []

        # One merged LLM call to select tables for ALL datasets at once
        if effective_tables and len(effective_tables) > self._TABLE_SELECTION_THRESHOLD:
            tables_per_dataset = self.select_tables_for_all_datasets(
                datasets.datasets, effective_tables
            )
            llm_selected = True
        else:
            tables_per_dataset = {ds.name: effective_tables for ds in datasets.datasets}
            llm_selected = False
            if effective_tables:
                all_nums = [getattr(t, "number", idx + 1) for idx, t in enumerate(effective_tables)]
                self._emit_table_selection_summary(
                    datasets.datasets,
                    effective_tables,
                    selected_per_dataset={ds.name: all_nums for ds in datasets.datasets},
                    note=(
                        f"Table selection skipped (≤{self._TABLE_SELECTION_THRESHOLD} tables); "
                        "using all tables"
                    ),
                    stat_table_summaries=stat_table_summaries,
                )

        for ds in datasets.datasets:
            ds_tables = tables_per_dataset.get(ds.name, effective_tables)

            context, rag_stats = self._build_rag_context(
                rag_text, ds_tables, ds.name, already_selected=llm_selected
            )
            logger.info(
                "Step 2 RAG [%s]: %d/%d paragraphs, %d/%d tables (%s), context=%d chars",
                ds.name,
                rag_stats["paragraphs_selected"],
                rag_stats["paragraphs_total"],
                rag_stats["tables_selected"],
                rag_stats["tables_total"],
                rag_stats["table_selection_mode"],
                rag_stats["context_total_chars"],
            )
            metric_constraint = ""
            if is_qm9_dataset(ds.name):
                metric_constraint = (
                    "QM9 is a multi-target benchmark. Extract per-target test MAE using "
                    "canonical property keys (gap, mu, alpha, U0, H, G, Cv, S, HOMO, LUMO, "
                    'etc.) as the metric field — never bare "MAE".\n'
                )
            elif ds.primary_metric:
                metric_constraint = (
                    f'PRIMARY METRIC: "{ds.primary_metric}". '
                    f"Focus on this metric as the main benchmark result. "
                    f"Skip purely secondary diagnostics such as R\u00b2, "
                    f"coefficient of determination, or loss values that are "
                    f"not standard benchmark scores.\n"
                )
            user_content = (
                f'FOCUS: Extract results ONLY for the dataset "{ds.name}".\n'
                f"Ignore rows that belong to other datasets.\n"
                f"Use only the STANDARD / DEFAULT configuration of this dataset. "
                f"Skip results for optional variants (e.g. different graph formats, "
                f"SLIC values, or other construction options) if the table shows "
                f"multiple configurations.\n"
                + (
                    f'PROPOSED MODEL HINT: The introduction names the paper\'s main proposed method as "{intro_model_hint}". '
                    f'Use that exact name instead of placeholders like "Ours" when the row refers to the paper\'s method.\n'
                    if intro_model_hint
                    else ""
                )
                + f"{metric_constraint}\n"
                f"{context}"
            )
            logger.info(
                "Step 2: extracting dataset=%r  context=%d chars",
                ds.name,
                len(user_content),
            )
            try:
                if is_qm9_dataset(ds.name):
                    for group_idx, targets in enumerate(QM9_EXTRACT_TARGET_GROUPS):
                        group_content = user_content + "\n" + qm9_extract_metric_constraint(targets)
                        try:
                            out = self._extract_results_chunk(
                                prompt,
                                group_content,
                                call_type=f"extract_dataset:{ds.name}:g{group_idx + 1}",
                                max_tokens=_QM9_EXTRACT_MAX_TOKENS,
                            )
                        except Exception as group_exc:
                            logger.warning(
                                "QM9 target-group extraction failed for %r group %d: %s",
                                ds.name,
                                group_idx + 1,
                                group_exc,
                            )
                            if self._call_log:
                                self._call_log[-1].parse_error = None
                            notes_parts.append(f"[{ds.name} g{group_idx + 1}] failed: {group_exc}")
                            self._fire_progress()
                            continue
                        if self._call_log:
                            self._call_log[-1].extra = {
                                **self._call_log[-1].extra,
                                "rag": rag_stats,
                                "qm9_targets": list(targets),
                            }
                        self._fire_progress()
                        all_results.extend(out.results)
                        if out.proposed_model and proposed is None:
                            proposed = out.proposed_model
                        baselines.extend(out.baseline_models)
                        if out.extraction_notes:
                            notes_parts.append(
                                f"[{ds.name} g{group_idx + 1}] {out.extraction_notes}"
                            )
                        confidence_levels.append(out.extraction_confidence)
                else:
                    out = self._extract_results_chunk(
                        prompt,
                        user_content,
                        call_type=f"extract_dataset:{ds.name}",
                    )
                    # Attach RAG stats to the call record, then fire progress
                    if self._call_log:
                        self._call_log[-1].extra = {
                            **self._call_log[-1].extra,
                            "rag": rag_stats,
                        }
                    self._fire_progress()
                    all_results.extend(out.results)
                    if out.proposed_model and proposed is None:
                        proposed = out.proposed_model
                    baselines.extend(out.baseline_models)
                    if out.extraction_notes:
                        notes_parts.append(f"[{ds.name}] {out.extraction_notes}")
                    confidence_levels.append(out.extraction_confidence)
            except Exception as exc:
                logger.warning("Per-dataset extraction for %r failed: %s", ds.name, exc)
                self._fire_progress()
                notes_parts.append(f"[{ds.name}] failed: {exc}")

        return _merge_extraction_outputs(
            proposed_model=proposed,
            baselines=baselines,
            results=all_results,
            confidence_levels=confidence_levels,
            notes_parts=notes_parts,
            normalise_metrics=True,
            discovered_datasets=list(datasets.datasets),
        )

    def extract_dataset_statistics(
        self,
        discovered_datasets: list[DatasetInfo],
        paper_text: str,
        tables: list | None = None,
        latex_paper: Any = None,
    ) -> DatasetStatisticsOutput:
        """Collectively extract dataset structural statistics when discovery flagged them."""
        stats_datasets = [ds for ds in discovered_datasets if ds.statistics_mentioned]
        if not stats_datasets:
            return DatasetStatisticsOutput()

        prompt = self._read_prompt("dataset_statistics_extraction.txt")
        focus_names = [ds.name for ds in stats_datasets]
        parts: list[str] = [
            "=== FOCUS DATASETS ===\n" + "\n".join(f"- {name}" for name in focus_names),
        ]

        intro_text = (
            latex_paper.intro_text
            if latex_paper is not None
            else paper_text[:_DISCOVERY_INTRO_CHARS]
        )
        parts.append(f"=== PAPER INTRO / EXPERIMENT SECTIONS ===\n{intro_text}")

        if latex_paper is not None:
            exp_text = latex_paper.experiment_text
            if exp_text.strip():
                parts.append(f"=== EXPERIMENT TEXT ===\n{exp_text[:_TABLE_SECTION_SIZE]}")
        elif paper_text.strip():
            parts.append(f"=== PAPER TEXT EXCERPT ===\n{paper_text[:_TABLE_SECTION_SIZE]}")

        stat_table_lines: list[str] = []
        for table in tables or []:
            if not is_statistics_table(table, header=self._table_header(table)):
                continue
            number = getattr(table, "number", "?")
            appendix = " [appendix]" if getattr(table, "in_appendix", False) else ""
            body = getattr(table, "markdown", None) or str(table)
            stat_table_lines.append(
                f"Table {number}{appendix}: {getattr(table, 'caption', '')}\n{body[:4000]}"
            )
        if stat_table_lines:
            parts.append("=== DATASET STATISTICS TABLES ===\n" + "\n\n".join(stat_table_lines))

        for ds in stats_datasets:
            if ds.statistics_sources:
                parts.append(
                    f"=== HINT: statistics for {ds.name} likely in {', '.join(ds.statistics_sources)} ==="
                )

        user_content = "\n\n".join(parts)
        try:
            raw = self._call_json(
                prompt,
                user_content,
                max_tokens=cfg.llm_max_tokens,
                call_type="extract_dataset_statistics",
            )
            result = DatasetStatisticsOutput.model_validate(raw)
            if self._call_log:
                extracted_details = [entry.model_dump() for entry in result.datasets]
                self._call_log[-1].extra = {
                    **self._call_log[-1].extra,
                    "dataset_statistics": _dataset_statistics_extra_with_tables(
                        stats_datasets,
                        stat_table_summaries=_statistics_table_summaries(tables or []),
                    ),
                    "statistics_tables": _statistics_table_summaries(tables or []),
                    "paper_has_statistics": True,
                    "extracted_dataset_statistics": [entry.name for entry in result.datasets],
                    "extracted_statistics_details": extracted_details,
                }
            logger.info(
                "Dataset statistics extraction: %d dataset(s) with stats",
                len(result.datasets),
            )
            self._fire_progress()
            return result
        except Exception as exc:
            logger.warning("Dataset statistics extraction failed: %s", exc)
            if self._call_log:
                self._call_log[-1].parse_error = None
            self._fire_progress()
            return DatasetStatisticsOutput(notes=f"extraction failed: {exc}")

    def extract_sota_claims(
        self,
        scoped_prose: str,
        discovered_datasets: list[DatasetInfo],
    ) -> SotaClaimOutput:
        """Extract SOTA performance claims from pre-appendix prose."""
        from backend.sota_claim_parsing import chunk_prose_for_extraction, merge_claim_dicts

        if not scoped_prose.strip():
            return SotaClaimOutput()

        prompt = self._read_prompt("sota_claim_extraction.txt")
        focus_names = [ds.name for ds in discovered_datasets if ds.name]
        all_claims: list[dict] = []
        notes_parts: list[str] = []
        chunks = chunk_prose_for_extraction(scoped_prose)

        for chunk_index, chunk in enumerate(chunks):
            parts = ["=== FOCUS DATASETS ===\n" + "\n".join(f"- {n}" for n in focus_names)]
            parts.append(f"=== PAPER PROSE (pre-appendix, no tables) ===\n{chunk}")
            user_content = "\n\n".join(parts)
            call_type = (
                "extract_sota_claims"
                if len(chunks) == 1
                else f"extract_sota_claims_chunk_{chunk_index + 1}"
            )
            try:
                raw = self._call_json(
                    prompt,
                    user_content,
                    max_tokens=cfg.llm_max_tokens,
                    call_type=call_type,
                )
                result = SotaClaimOutput.model_validate(raw)
                all_claims.extend(entry.model_dump() for entry in result.claims)
                if result.notes:
                    notes_parts.append(result.notes)
                if self._call_log:
                    self._call_log[-1].extra = {
                        **self._call_log[-1].extra,
                        "sota_claims_found": len(result.claims),
                        "sota_claim_sentences": [entry.raw_sentence for entry in result.claims],
                    }
            except Exception as exc:
                logger.warning("SOTA claim extraction chunk %d failed: %s", chunk_index + 1, exc)
                notes_parts.append(f"Chunk {chunk_index + 1} failed: {exc}")

        merged = merge_claim_dicts(all_claims)
        return SotaClaimOutput(
            claims=[SotaClaimEntry.model_validate(item) for item in merged],
            notes="\n".join(notes_parts).strip(),
        )

    def extract_results(self, paper_text: str, tables_text: str) -> ExtractionOutput:
        """Stage 2: extract all benchmark results from the full paper text.

        Strategy:
          1. Sanitize: strip non-printable chars that cause models to return empty.
          2. If combined text fits in _CHUNK_SIZE: single-shot extraction.
          3. Otherwise: split paper into table-section chunks (_TABLE_SECTION_SIZE)
             and merge results (most reliable for models with ~20k effective limit).
          4. Fallback: smart excerpt (abstract intro + all table sections).
          5. Last resort: fixed-size text chunks across full paper.
        """
        prompt = self._read_result_prompt(full_mode=True)

        # Sanitize: strip control characters that silently break some LLMs
        paper_text = _sanitize_text(paper_text)
        tables_text = _sanitize_text(tables_text)

        tables_section = (
            f"\n\n=== TABLES (deduplicated) ===\n{tables_text[:_TABLE_CHUNK_SIZE]}"
            if tables_text.strip()
            else ""
        )
        combined = paper_text + tables_section

        # 1. Single-shot for papers that fit in the context window
        if len(combined) <= _CHUNK_SIZE:
            logger.info("Full-text extraction in one shot (%d chars)", len(combined))
            return self._extract_results_chunk(prompt, combined, call_type="extract_full")

        # 2. Table-section chunking: split on table headers, send each section
        #    separately. This is the most reliable strategy because each call
        #    focuses on one table and stays well within the effective model limit.
        table_sections = _split_into_table_sections(paper_text, _TABLE_SECTION_SIZE)
        if len(table_sections) > 1:
            logger.info(
                "Paper too long (%d chars); splitting into %d table sections",
                len(combined),
                len(table_sections),
            )
            return self._extract_from_sections(prompt, table_sections, tables_section)

        # 3. Smart excerpt: abstract + all result table sections
        excerpt = _build_smart_excerpt(paper_text, tables_section)
        logger.info(
            "No distinct table sections found; using smart excerpt (%d chars)",
            len(excerpt),
        )
        if len(excerpt) <= _CHUNK_SIZE:
            return self._extract_results_chunk(prompt, excerpt, call_type="extract_smart_excerpt")

        # 4. Last resort: chunked extraction across the full text
        chunks = _split_into_chunks(paper_text, _CHUNK_SIZE - len(tables_section))
        logger.info("Falling back to fixed-size chunked extraction (%d chunks)", len(chunks))

        all_results: list[ResultEntry] = []
        proposed: ProposedModel | None = None
        baselines: list[BaselineModelInfo] = []
        notes_parts: list[str] = []
        confidence_levels = []

        for i, chunk in enumerate(chunks):
            logger.debug("Extracting chunk %d/%d", i + 1, len(chunks))
            try:
                chunk_out = self._extract_results_chunk(
                    prompt, chunk + tables_section, call_type=f"extract_chunk:{i + 1}"
                )
                all_results.extend(chunk_out.results)
                if chunk_out.proposed_model and proposed is None:
                    proposed = chunk_out.proposed_model
                baselines.extend(chunk_out.baseline_models)
                if chunk_out.extraction_notes:
                    notes_parts.append(f"[Chunk {i + 1}] {chunk_out.extraction_notes}")
                confidence_levels.append(chunk_out.extraction_confidence)
            except Exception as exc:
                logger.warning("Chunk %d extraction failed: %s", i + 1, exc)
                notes_parts.append(f"[Chunk {i + 1}] Extraction failed: {exc}")

        return _merge_extraction_outputs(
            proposed_model=proposed,
            baselines=baselines,
            results=all_results,
            confidence_levels=confidence_levels,
            notes_parts=notes_parts,
        )

    def _extract_results_chunk(
        self,
        prompt: str,
        text: str,
        call_type: str = "extract_results",
        max_tokens: int | None = None,
    ) -> ExtractionOutput:
        tried_formats: list[str] = []
        parse_errors: list[str] = []
        preferred = self.result_output_format or "json"
        fallback = "yaml" if preferred != "yaml" else "json"
        for output_format in (preferred, fallback):
            if output_format in tried_formats:
                continue
            tried_formats.append(output_format)
            try:
                raw = self._call_structured(
                    prompt,
                    text,
                    call_type=call_type,
                    output_format=output_format,
                    max_tokens=max_tokens,
                )
                raw = _expand_extraction_payload(raw)
                raw = _sanitize_extraction_payload(raw)
                if not isinstance(raw, dict):
                    logger.warning(
                        "Malformed structured output from %r (%s): %s — treating as empty extraction",
                        self.model_name,
                        call_type,
                        type(raw).__name__,
                    )
                    raw = {
                        "proposed_model": None,
                        "baseline_models": [],
                        "results": [],
                        "extraction_confidence": "LOW",
                        "extraction_notes": (
                            "Model returned malformed structured output without the required "
                            "top-level object; no rows extracted."
                        ),
                    }
                return ExtractionOutput.model_validate(raw)
            except Exception as exc:
                parse_errors.append(f"{output_format}: {exc}")
                logger.warning(
                    "%s extraction failed using %s: %s",
                    call_type,
                    output_format,
                    exc,
                )

        raise ValueError(f"Structured extraction failed for {call_type}: {'; '.join(parse_errors)}")

    def _extract_from_sections(
        self, prompt: str, sections: list[str], tables_section: str
    ) -> ExtractionOutput:
        """Run extraction on each table section independently and merge results.

        Each section is sent in a separate LLM call, keeping the user content
        small enough that even models with a low effective context limit respond.
        """
        all_results: list[ResultEntry] = []
        proposed: ProposedModel | None = None
        baselines: list[BaselineModelInfo] = []
        notes_parts: list[str] = []
        confidence_levels: list[str] = []

        # Append the HTML-extracted tables to the last section so that
        # cleaned table markup is always present in at least one call.
        for i, section in enumerate(sections):
            content = section
            if i == len(sections) - 1 and tables_section:
                content = section + tables_section
            logger.debug("Extracting section %d/%d (%d chars)", i + 1, len(sections), len(content))
            try:
                out = self._extract_results_chunk(
                    prompt, content, call_type=f"extract_section:{i + 1}"
                )
                all_results.extend(out.results)
                if out.proposed_model and proposed is None:
                    proposed = out.proposed_model
                baselines.extend(out.baseline_models)
                if out.extraction_notes:
                    notes_parts.append(f"[Section {i + 1}] {out.extraction_notes}")
                confidence_levels.append(out.extraction_confidence)
            except Exception as exc:
                logger.warning("Section %d extraction failed: %s", i + 1, exc)
                notes_parts.append(f"[Section {i + 1}] failed: {exc}")

        return _merge_extraction_outputs(
            proposed_model=proposed,
            baselines=baselines,
            results=all_results,
            confidence_levels=confidence_levels,
            notes_parts=notes_parts,
        )

    def detect_figure(self, paper_text: str, figures_list: list[dict]) -> FigureInfo:
        """Identify the main architecture figure (text-based heuristic).

        Sends paper intro + figure captions to the LLM as a text-only fallback.
        """
        prompt = self._read_prompt("figure_detection.txt")
        figures_summary = "\n".join(
            f"Figure {i + 1}: {f.get('caption', '')[:120]} [src={f.get('src', 'N/A')}]"
            for i, f in enumerate(figures_list[:30])
        )
        user_content = (
            f"Paper text (first 8000 chars):\n{paper_text[:8000]}\n\n"
            f"Available figures:\n{figures_summary}"
        )
        try:
            raw = self._call_json(prompt, user_content, max_tokens=512, call_type="detect_figure")
            return FigureInfo.model_validate(raw)
        except Exception as exc:
            logger.warning("Figure detection failed: %s", exc)
            return FigureInfo()

    def extract_model_sizes(
        self,
        paper_text: str,
        model_names: list[str] | None = None,
    ) -> list[ModelSizeEntry]:
        """Extract model parameter counts from a targeted paper excerpt."""
        prompt = self._read_prompt("model_size.txt")
        excerpt = _build_model_size_excerpt(paper_text)
        user_content = excerpt
        if model_names:
            user_content += "\n\nTARGET MODEL LIST:\n" + "\n".join(
                f"- {name}" for name in model_names
            )
        try:
            raw = self._call_structured(
                prompt,
                user_content,
                max_tokens=2048,
                call_type="model_sizes" if not model_names else "model_sizes_guided",
                output_format=self.result_output_format,
            )
            if isinstance(raw, list):
                return [ModelSizeEntry.model_validate(item) for item in raw]
        except Exception as exc:
            logger.warning("Model size extraction failed: %s", exc)
        return []

    # ── Full paper extraction ──────────────────────────────────────────────

    def process_paper(
        self,
        arxiv_id: str,
        paper_text: str,
        tables_text: str,
        figures_list: list[dict],
        paper_title: str = "",
        paper_abstract: str = "",
        structured_tables: list | None = None,
        latex_paper: Any = None,
        extraction_strategy: str = "auto",
        experiment_label: str | None = None,
    ) -> dict:
        """Run all extraction tasks and save outputs.

        When *latex_paper* (a ``LatexPaper``) is provided it is used for the
        two-step extraction path; its tables and experiment-section text give
        much higher recall than PDF-derived plain text.  When only
        *structured_tables* (HTML ``ParsedTable`` objects) are provided, those
        are used instead.  If neither is given, the legacy single-shot / chunked
        strategy is used.

        Returns a combined dict with all extraction results.
        """
        storage = PaperStorage(arxiv_id)
        storage.extracted_dir.mkdir(parents=True, exist_ok=True)

        logger.info("Extracting results for arXiv:%s with model=%s", arxiv_id, self.model_name)

        strategy = extraction_strategy.lower()

        # Task 1: Results — prefer LaTeX source, then HTML tables, then legacy path
        if strategy == "full":
            results_out = self.extract_results(paper_text, tables_text)
        elif latex_paper is not None:
            results_out = self.extract_results_two_step(
                paper_text,
                [],
                latex_paper=latex_paper,
                paper_title=paper_title,
            )
        elif structured_tables is not None:
            results_out = self.extract_results_two_step(
                paper_text,
                structured_tables,
                paper_title=paper_title,
            )
        else:
            results_out = self.extract_results(paper_text, tables_text)

        # Task 1b: Dataset statistics — separate workspace from benchmark results
        stats_out = DatasetStatisticsOutput()
        if results_out.paper_has_statistics:
            stats_tables = (
                list(latex_paper.tables) if latex_paper is not None else (structured_tables or [])
            )
            stats_out = self.extract_dataset_statistics(
                results_out.discovered_datasets,
                paper_text,
                tables=stats_tables,
                latex_paper=latex_paper,
            )
            if stats_out.datasets:
                from backend.dataset_stats_storage import DatasetStatsStorage

                ds_storage = DatasetStatsStorage()
                for entry in stats_out.datasets:
                    ds_storage.save_paper_stats(
                        entry.name,
                        arxiv_id,
                        DatasetStatsStorage.build_payload(
                            arxiv_id=arxiv_id,
                            paper_title=paper_title,
                            dataset_entry=entry.model_dump(),
                            extraction_model=display_name_for_model(self.model_name),
                        ),
                    )

        # Task 1c: SOTA claims — pre-appendix prose only
        from backend.sota_claim_parsing import main_body_prose_text, text_has_sota_markers

        sota_out = SotaClaimOutput()
        scoped_prose = main_body_prose_text(paper_text=paper_text, latex_paper=latex_paper)
        if text_has_sota_markers(scoped_prose):
            sota_out = self.extract_sota_claims(
                scoped_prose,
                results_out.discovered_datasets,
            )
            if sota_out.claims:
                sota_claims_path = storage.extracted_dir / "sota_claims.yaml"
                sota_claims_path.write_text(
                    yaml.safe_dump(
                        {
                            "arxiv_id": arxiv_id,
                            "paper_title": paper_title,
                            "extracted_at": datetime.now(UTC).isoformat(),
                            "extraction_model": display_name_for_model(self.model_name),
                            "claims": [entry.model_dump() for entry in sota_out.claims],
                            "notes": sota_out.notes,
                        },
                        allow_unicode=True,
                        sort_keys=False,
                    ),
                    encoding="utf-8",
                )

        # Task 2: Main figure — always use the title page (first figure from list or PDF page 0).
        if figures_list:
            figure_out = FigureInfo(
                img_src=figures_list[0].get("src"),
                reason="title page (first figure)",
            )
        elif storage.pdf_path.exists():
            figure_out = FigureInfo(page_number=0, reason="title page (PDF page 1)")
        else:
            figure_out = FigureInfo()

        # Task 3: Model sizes — broad pass then guided pass for result-table names
        sizes = self.extract_model_sizes(paper_text)
        model_names = sorted({r.model for r in results_out.results if r.model})
        if model_names:
            guided_sizes = self.extract_model_sizes(paper_text, model_names=model_names)
            sizes = _merge_size_entries(sizes, guided_sizes)
        _apply_sizes(results_out, sizes)
        intro_model_hint = _extract_proposed_model_hint(
            paper_title,
            _paper_intro_text(paper_text, latex_paper),
        )
        _rename_generic_proposed_rows(results_out, intro_model_hint)
        if intro_model_hint:
            note = f"Intro-derived proposed-model hint: {intro_model_hint}."
            results_out.extraction_notes = f"{results_out.extraction_notes}\n{note}".strip()
        _stabilize_model_names(results_out, paper_title=paper_title)

        repository_out = {
            "verified_url": None,
            "confidence": 0.0,
            "reason": "",
            "verification_model": "",
            "source_kind": "none",
            "candidate_urls": [],
            "checked_candidates": [],
        }
        try:
            from backend.repository_linking import find_verified_repository_link

            repo_source_text = latex_paper.main_tex if latex_paper is not None else paper_text
            repo_source_kind = "latex" if latex_paper is not None else "paper_text"
            if repo_source_text.strip():
                repo_verifier = (
                    LLMExtractor(model_tier="small", streaming=self.streaming)
                    if cfg.llm_endpoint and cfg.llm_api_key
                    else None
                )
                repository_out = find_verified_repository_link(
                    llm_verifier=repo_verifier,
                    arxiv_id=arxiv_id,
                    paper_title=paper_title,
                    paper_abstract=paper_abstract,
                    source_text=repo_source_text,
                    source_kind=repo_source_kind,
                )
                if repo_verifier is not None:
                    self._call_log.extend(repo_verifier._call_log)
                storage_updates = {"repository": repository_out}
                if repository_out.get("verified_url"):
                    storage_updates["codebase_url"] = repository_out["verified_url"]
                storage.update_metadata(storage_updates)
        except Exception as exc:
            logger.warning("Repository verification failed for %s: %s", arxiv_id, exc)

        usage_summary = _summarize_call_usage(self._call_log, self._probe_usage_limits())

        # Compose full output
        output = {
            "arxiv_id": arxiv_id,
            "model_used": display_name_for_model(self.model_name),
            "extracted_at": datetime.now(UTC).isoformat(),
            "experiment": {
                "label": experiment_label,
                "strategy": strategy,
                "result_output_format": self.result_output_format,
            },
            "results": results_out.model_dump(),
            "sota_claims": sota_out.model_dump(),
            "figure": figure_out.model_dump(),
            "repository": repository_out,
            "model_sizes": [s.model_dump() for s in sizes],
            "usage": usage_summary,
        }

        if experiment_label:
            artifact_dir = storage.extracted_dir / "experiments" / _slugify_label(experiment_label)
        else:
            artifact_dir = storage.extracted_dir
        artifact_dir.mkdir(parents=True, exist_ok=True)
        llm_output_path = artifact_dir / "llm_output.yaml"
        human_readable_path = artifact_dir / "results_human_readable.md"
        call_log_path = artifact_dir / "llm_calls.yaml"

        # Save raw YAML
        llm_output_path.write_text(
            yaml.safe_dump(output, allow_unicode=True, sort_keys=False), encoding="utf-8"
        )
        call_log_path.write_text(
            yaml.safe_dump(
                [
                    {
                        "call_type": rec.call_type,
                        "input_chars": rec.input_chars,
                        "output_chars": rec.output_chars,
                        "duration_s": rec.duration_s,
                        "ttft_s": rec.ttft_s,
                        "tokens_per_sec": rec.tokens_per_sec,
                        "prompt_tokens": rec.prompt_tokens,
                        "completion_tokens": rec.completion_tokens,
                        "success": rec.success,
                        "parse_error": rec.parse_error,
                        "extra": rec.extra,
                    }
                    for rec in self._call_log
                ],
                allow_unicode=True,
                sort_keys=False,
            ),
            encoding="utf-8",
        )

        # Save human-readable markdown
        md = _render_human_readable(
            arxiv_id=arxiv_id,
            title=paper_title,
            model_name=self.model_name,
            results_out=results_out,
            figure_out=figure_out,
            extraction_strategy=strategy,
            result_output_format=self.result_output_format,
            experiment_label=experiment_label,
            usage_summary=usage_summary,
        )
        human_readable_path.write_text(md, encoding="utf-8")
        logger.info("Saved human-readable extraction to %s", human_readable_path)

        return output


# ── Helpers ───────────────────────────────────────────────────────────────────


def _sanitize_text(text: str) -> str:
    """Strip control characters that silently cause some LLMs to return empty.

    Keeps newlines, tabs, and carriage returns; removes everything else in the
    C0/C1 control range (ord < 32 except \\n \\t \\r, and ord 127-159).
    These characters appear in PDF-extracted text (form feeds, DC2/DC3, etc.)
    and reliably break openai-gpt-oss-120b responses.
    """
    return re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]", "", text)


def _sanitize_extraction_payload(raw: Any) -> Any:
    """Drop incomplete result rows before validating an extraction payload."""
    if not isinstance(raw, dict):
        return raw

    results = raw.get("results")
    if not isinstance(results, list):
        return raw

    cleaned_results: list[Any] = []
    dropped_rows = 0
    for entry in results:
        if not isinstance(entry, dict):
            dropped_rows += 1
            continue

        required_fields = [entry.get("model"), entry.get("dataset"), entry.get("metric")]
        if any(value in (None, "") for value in required_fields) or entry.get("value") in (
            None,
            "",
        ):
            dropped_rows += 1
            continue

        cleaned_results.append(entry)

    if not dropped_rows:
        return raw

    note = str(raw.get("extraction_notes") or "").strip()
    extra_note = f"Dropped {dropped_rows} incomplete result row(s) before validation."
    return {
        **raw,
        "results": cleaned_results,
        "extraction_notes": f"{note}\n{extra_note}".strip(),
    }


def _expand_extraction_payload(raw: Any) -> Any:
    """Expand compact or partially wrapped extraction payloads into the full schema."""
    if isinstance(raw, list):
        if raw and all(isinstance(item, dict) for item in raw):
            sample = raw[0]
            if {"model", "dataset", "metric", "value"}.issubset(sample):
                return {
                    "proposed_model": None,
                    "baseline_models": [],
                    "results": raw,
                    "extraction_confidence": "LOW",
                    "extraction_notes": "Wrapped bare result list into extraction object.",
                }
            if {"m", "d", "k", "v"}.issubset(sample):
                return {
                    "proposed_model": None,
                    "baseline_models": [],
                    "results": [_expand_compact_result_entry(item) for item in raw],
                    "extraction_confidence": "LOW",
                    "extraction_notes": "Wrapped bare compact result list into extraction object.",
                }
            if "name" in sample:
                return {
                    "proposed_model": None,
                    "baseline_models": raw,
                    "results": [],
                    "extraction_confidence": "LOW",
                    "extraction_notes": "Wrapped bare baseline-model list into extraction object.",
                }
        return raw

    if not isinstance(raw, dict):
        return raw

    if "proposed_model_name" not in raw and not any(k in raw for k in ("confidence", "notes")):
        return raw

    baseline_names = raw.get("baseline_model_names") or []
    baseline_types = raw.get("baseline_model_types") or {}
    baseline_params = raw.get("baseline_params_millions") or {}
    proposed_name = raw.get("proposed_model_name")
    proposed: dict[str, Any] | None = None
    if proposed_name:
        proposed = {
            "name": proposed_name,
            "model_type": normalize_architecture_type(raw.get("proposed_model_type")),
            "params_millions": raw.get("proposed_params_millions"),
        }
    baseline_models: list[dict[str, Any]] = []
    for name in baseline_names:
        if not name:
            continue
        baseline_models.append(
            {
                "name": name,
                "model_type": normalize_architecture_type(baseline_types.get(name)),
                "params_millions": baseline_params.get(name),
                "params_exact": None,
                "original_paper_hint": None,
            }
        )
    return {
        "proposed_model": proposed,
        "baseline_models": baseline_models,
        "results": [_expand_compact_result_entry(item) for item in raw.get("results", [])],
        "extraction_confidence": raw.get("confidence", "LOW"),
        "extraction_notes": raw.get("notes", ""),
    }


def _expand_compact_result_entry(entry: Any) -> Any:
    if not isinstance(entry, dict):
        return entry
    if "model" in entry:
        return entry
    return {
        "model": entry.get("m"),
        "is_proposed": entry.get("p", False),
        "dataset": entry.get("d"),
        "metric": entry.get("k"),
        "value": entry.get("v"),
        "std": entry.get("s"),
        "higher_is_better": entry.get("h", True),
        "uses_external_data": entry.get("e"),
        "table_ref": entry.get("t"),
        "source_ref": entry.get("r", "this paper"),
    }


def _split_into_table_sections(text: str, max_section_size: int) -> list[str]:
    """Split paper text into sections anchored at table headers.

    Each section starts just before a "Table N" header and runs until the
    next table header (or end of text).  Sections that exceed max_section_size
    are further split at paragraph boundaries.

    Returns at least one section (the full text if no tables found).
    """
    # Find all table-header positions
    positions: list[int] = [0]  # always start with a section from position 0
    for m in re.finditer(r"\bTable\s+\d+[\.:]\s", text, re.IGNORECASE):
        start = max(0, m.start() - 200)  # include ~200 chars of lead-in
        if start > positions[-1] + 500:  # avoid micro-sections
            positions.append(start)

    if len(positions) <= 1:
        return [text]  # no distinct tables found

    # Build raw sections
    raw_sections: list[str] = []
    for i, pos in enumerate(positions):
        end = positions[i + 1] if i + 1 < len(positions) else len(text)
        raw_sections.append(text[pos:end])

    # Sub-split sections that are still too long
    final: list[str] = []
    for sec in raw_sections:
        if len(sec) <= max_section_size:
            final.append(sec)
        else:
            final.extend(_split_into_chunks(sec, max_section_size))

    return final


def _split_into_chunks(text: str, chunk_size: int) -> list[str]:
    """Split text at paragraph boundaries into chunks of at most chunk_size chars."""
    paragraphs = text.split("\n\n")
    chunks: list[str] = []
    current = []
    current_len = 0

    for para in paragraphs:
        if current_len + len(para) > chunk_size and current:
            chunks.append("\n\n".join(current))
            current = []
            current_len = 0
        current.append(para)
        current_len += len(para) + 2  # +2 for "\n\n"

    if current:
        chunks.append("\n\n".join(current))
    return chunks


def _build_smart_excerpt(paper_text: str, tables_section: str) -> str:
    """Build a focused excerpt for papers that exceed the single-shot limit.

    Combines:
    - The intro/abstract (first _SMART_INTRO_CHARS chars) for context.
    - All paragraphs that look like result tables or baseline comparisons
      (up to _SMART_TABLES_CHARS chars starting from the first result table).
    - The tables_section (HTML-extracted markdown tables if available).
    """
    intro = paper_text[:_SMART_INTRO_CHARS]

    # Find where the first result table starts. Look for "Table N:" followed
    # by content that includes numeric values (results).
    table_start = -1
    for pattern in [
        r"Table\s+\d+[:\.].*(?:baseline|result|performance|experiment)",
        r"Table\s+[3-9][:\.]",  # Tables 3+ are usually results in ML papers
        r"Table\s+[1-2][0-9][:\.]",  # Tables 10+
    ]:
        m = re.search(pattern, paper_text, re.IGNORECASE)
        if m:
            table_start = m.start()
            break

    if table_start == -1:
        # No table found — fall back to latter half of paper
        table_start = len(paper_text) // 2

    results_section = paper_text[table_start : table_start + _SMART_TABLES_CHARS]

    parts = [
        f"=== ABSTRACT / INTRODUCTION ===\n{intro}",
        f"\n\n=== RESULTS SECTION ===\n{results_section}",
    ]
    if tables_section:
        parts.append(tables_section)

    return "\n".join(parts)


def _build_model_size_excerpt(paper_text: str) -> str:
    """Build a paper excerpt likely to contain parameter counts."""
    intro = paper_text[:_SMART_INTRO_CHARS]
    methods_chunks: list[str] = []
    for pattern in (
        r"(?im)^(?:#+\s*)?(?:\d+\.?\s*)?(?:method|implementation|architecture|model)\b",
        r"(?im)^(?:appendix|[AB]\.\s)",
    ):
        for match in re.finditer(pattern, paper_text):
            start = match.start()
            methods_chunks.append(paper_text[start : start + 15_000])

    param_sections: list[str] = []
    for match in re.finditer(
        r"(?i)(?:#+\s*param|parameters|model size|#params|\d+\.?\d*\s*[Mm]\b|million params)",
        paper_text,
    ):
        start = max(0, match.start() - 500)
        param_sections.append(paper_text[start : start + 8000])

    tail = paper_text[-20_000:] if len(paper_text) > 20_000 else ""

    parts = [f"=== INTRO ===\n{intro}"]
    if methods_chunks:
        parts.append("=== METHODS / IMPLEMENTATION ===\n" + "\n---\n".join(methods_chunks[:3]))
    if param_sections:
        parts.append("=== PARAM MENTIONS ===\n" + "\n---\n".join(param_sections[:5]))
    if tail:
        parts.append(f"=== APPENDIX / TAIL ===\n{tail}")

    return "\n\n".join(parts)[:_CHUNK_SIZE]


def _size_lookup_key(entry: ModelSizeEntry) -> str:
    return (entry.matched_result_name or entry.model_name).strip().lower()


def _lookup_size_entry(name: str, size_map: dict[str, ModelSizeEntry]) -> ModelSizeEntry | None:
    key = name.strip().lower()
    if key in size_map:
        return size_map[key]
    if not size_map:
        return None
    best_match, score = fuzz_process.extractOne(
        key, list(size_map.keys()), scorer=fuzz_lib.token_sort_ratio
    )
    if score >= _SIZE_FUZZY_MATCH_MIN_SCORE:
        return size_map.get(best_match)
    return None


def _merge_size_entries(
    primary: list[ModelSizeEntry], secondary: list[ModelSizeEntry]
) -> list[ModelSizeEntry]:
    merged: dict[str, ModelSizeEntry] = {}
    for entry in primary + secondary:
        key = _size_lookup_key(entry)
        if not key:
            continue
        existing = merged.get(key)
        if existing is None:
            merged[key] = entry
            continue
        if existing.params_millions is None and entry.params_millions is not None:
            existing.params_millions = entry.params_millions
        if existing.params_exact is None and entry.params_exact is not None:
            existing.params_exact = entry.params_exact
    return list(merged.values())


def _apply_size_to_model_info(
    info: ProposedModel | BaselineModelInfo,
    size_map: dict[str, ModelSizeEntry],
) -> None:
    matched = _lookup_size_entry(info.name, size_map)
    if matched is None:
        return
    if info.params_millions is None:
        info.params_millions = matched.params_millions
    if info.params_exact is None:
        info.params_exact = matched.params_exact


def _apply_sizes(extraction: ExtractionOutput, sizes: list[ModelSizeEntry]) -> None:
    """Merge model size data back into the extraction output."""
    if not sizes:
        return
    size_map = {_size_lookup_key(s): s for s in sizes if _size_lookup_key(s)}

    if extraction.proposed_model is not None:
        _apply_size_to_model_info(extraction.proposed_model, size_map)

    for baseline in extraction.baseline_models:
        _apply_size_to_model_info(baseline, size_map)


def _normalise_model_name_text(name: str) -> str:
    """Clean light LaTeX/math wrappers from extracted model names."""
    clean = name.strip()
    if not clean:
        return clean

    clean = re.sub(r"\\mathrm\{([^}]*)\}", r"\1", clean)
    clean = clean.replace("$^{*}$", "*")
    clean = clean.replace("$^*$", "*")
    clean = clean.replace("$^*", "*")
    clean = clean.replace("^{*}", "*")
    clean = clean.replace("^*", "*")
    clean = clean.replace("$", "")
    clean = clean.replace("\\text{-}", "-")
    clean = re.sub(r"\\textsubscript\{([^}]*)\}", r"-\1", clean)
    greek_map = {
        r"\alpha": "α",
        r"\beta": "β",
        r"\gamma": "γ",
        r"\delta": "δ",
        r"\Delta": "Δ",
        r"\kappa": "κ",
        r"\lambda": "λ",
        r"\mu": "μ",
        r"\Sigma": "Σ",
        r"\sigma": "σ",
        r"\ell": "ℓ",
    }
    for latex, unicode_value in greek_map.items():
        clean = clean.replace(latex, unicode_value)
    clean = clean.replace("{}", "")
    clean = re.sub(r"\s+", " ", clean)
    return clean.strip()


_INTRO_METHOD_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(
        r"(?P<long>[A-Z][A-Za-z0-9+\-/ ]{2,100})\s*\((?P<short>[A-Z][A-Za-z0-9+\-]{1,30})\)"
    ),
    re.compile(
        r"which we name(?: as)?\s+(?:the\s+resulting\s+model\s+)?(?P<name>[A-Z][^.;:\n]{1,120})",
        re.IGNORECASE,
    ),
    re.compile(
        r"we (?:propose|introduce|develop|present|call|name)\s+(?:an?\s+|our\s+)?(?:model|method|architecture|framework)?\s*(?P<name>[A-Z][^.;:\n]{1,120})",
        re.IGNORECASE,
    ),
)
_TITLE_METHOD_PREFIX_RE = re.compile(r"^([A-Z][A-Za-z0-9+\-]{2,40})\s*:")


def _paper_intro_text(paper_text: str, latex_paper: Any = None) -> str:
    if latex_paper is not None and getattr(latex_paper, "intro_text", ""):
        return latex_paper.intro_text
    return (paper_text or "")[:8_000]


def _clean_intro_model_candidate(value: str | None) -> str | None:
    if not value:
        return None
    candidate = _normalise_model_name_text(value)
    candidate = re.split(
        r"\b(?:takes advantage|that|which|for graph|for node|for molecular|to reduce|with|on the)\b",
        candidate,
        maxsplit=1,
        flags=re.IGNORECASE,
    )[0]
    candidate = candidate.strip(" .,;:()[]{}")
    if not candidate:
        return None
    if _is_generic_proposed_name(candidate):
        return None
    if len(candidate.split()) > 8:
        return None
    return candidate


def _extract_proposed_model_hint(paper_title: str, intro_text: str) -> str | None:
    title_match = _TITLE_METHOD_PREFIX_RE.match((paper_title or "").strip())
    if title_match:
        candidate = _clean_intro_model_candidate(title_match.group(1))
        if candidate:
            return candidate

    # Authors often define a short abbreviation in the abstract/intro.
    # e.g. "Fully Product-Stereographic Transformer (FPS-T)"
    # Prefer that over a long descriptive title phrase.
    source = _normalise_model_name_text(intro_text or "")
    for pattern in _INTRO_METHOD_PATTERNS:
        for match in pattern.finditer(source[:8_000]):
            short_name = match.groupdict().get("short")
            if short_name:
                candidate = _clean_intro_model_candidate(short_name)
                if candidate:
                    return candidate

    # Fallback: long descriptive phrase from the title (e.g. "... Transformers")
    normalized_title = _normalise_model_name_text(paper_title or "")
    title_phrase_match = re.search(
        r"([A-Za-z][A-Za-z0-9+\-]*(?:\s+[A-Za-z][A-Za-z0-9+\-]*){0,5}\s+"
        r"(?:ConvNets?|GCNs?|GATs?|GNNs?|Transformers?|GraphSAGE|Graphormer))",
        normalized_title,
        flags=re.IGNORECASE,
    )
    if title_phrase_match:
        candidate = _clean_intro_model_candidate(title_phrase_match.group(1))
        if candidate:
            return candidate

    # Final fallback: non-abbreviated names from the intro text
    for pattern in _INTRO_METHOD_PATTERNS:
        for match in pattern.finditer(source[:8_000]):
            group_name = "name" if "name" in match.groupdict() else "long"
            candidate = _clean_intro_model_candidate(match.group(group_name))
            if candidate:
                return candidate
    return None


def _proposed_name_aliases(name: str) -> set[str]:
    normalized = _normalise_model_name_text(name)
    aliases: set[str] = set()
    full_key = _canonical_model_name_key(normalized)
    if full_key:
        aliases.add(full_key)

    for token in re.split(r"[^A-Za-z0-9]+", normalized):
        token = token.strip()
        if len(token) < 3:
            continue
        token_key = _canonical_model_name_key(token)
        if token_key and not _is_generic_proposed_name(token):
            aliases.add(token_key)
        m = re.match(
            r"(?P<prefix>[A-Za-z0-9]{2,})(?:GNNs?|GCN|GAT|GIN|SAGE)$", token, re.IGNORECASE
        )
        if m:
            aliases.add(_canonical_model_name_key(m.group("prefix")))

    paren = re.search(r"\(([^)]{2,30})\)", normalized)
    if paren:
        paren_key = _canonical_model_name_key(paren.group(1))
        if paren_key:
            aliases.add(paren_key)

    return {alias for alias in aliases if alias}


def _matches_proposed_model_name(row_name: str, proposed_name: str) -> bool:
    row_norm = _normalise_model_name_text(row_name)
    row_key = _canonical_model_name_key(row_norm)
    if not row_key:
        return False
    for alias in _proposed_name_aliases(proposed_name):
        if row_key == alias:
            return True
        if len(alias) >= 4 and alias in row_key:
            return True
        row_tokens = {token for token in re.split(r"[^a-z0-9]+", row_key) if token}
        if alias in row_tokens:
            return True
    return False


def _rename_generic_model_name(name: str, proposed_hint: str) -> str | None:
    clean = _normalise_model_name_text(name or "")
    if not clean:
        return None
    lowered = clean.lower()
    if clean == "\\modelname{}" or lowered == "ours":
        return proposed_hint
    if lowered.startswith("ours("):
        return proposed_hint + clean[4:]
    if lowered.startswith("ours "):
        remainder = clean[5:].strip()
        if remainder.startswith("(") and remainder.endswith(")"):
            inner = remainder[1:-1].strip()
            if inner and _canonical_model_name_key(inner) == _canonical_model_name_key(
                proposed_hint
            ):
                return proposed_hint
        return f"{proposed_hint} {remainder}".strip()
    return None


def _rename_generic_proposed_rows(extraction: ExtractionOutput, proposed_hint: str | None) -> None:
    if not proposed_hint:
        return
    for result in extraction.results:
        if not result.is_proposed:
            continue
        renamed = _rename_generic_model_name(result.model, proposed_hint)
        if renamed:
            result.model = renamed

    if extraction.proposed_model is None:
        extraction.proposed_model = ProposedModel(name=proposed_hint)
        return

    renamed = _rename_generic_model_name(extraction.proposed_model.name, proposed_hint)
    if renamed:
        extraction.proposed_model.name = renamed
    elif _is_generic_proposed_name(extraction.proposed_model.name):
        extraction.proposed_model.name = proposed_hint


def _stabilize_model_names(extraction: ExtractionOutput, paper_title: str = "") -> None:
    """Normalise model names, drop ablations, and stabilize the main proposed model."""
    if extraction.proposed_model is not None:
        extraction.proposed_model.name = _normalise_model_name_text(extraction.proposed_model.name)

    for baseline in extraction.baseline_models:
        baseline.name = _normalise_model_name_text(baseline.name)

    filtered_results: list[ResultEntry] = []
    dropped_ablation_rows = 0
    for result in extraction.results:
        result.model = _normalise_model_name_text(result.model)
        if _looks_like_ablation_model(result.model):
            dropped_ablation_rows += 1
            continue
        filtered_results.append(result)
    extraction.results = filtered_results

    extraction.baseline_models = [
        baseline
        for baseline in extraction.baseline_models
        if not _looks_like_ablation_model(baseline.name)
    ]

    if dropped_ablation_rows:
        note = f"Dropped {dropped_ablation_rows} ablation/diagnostic row(s)."
        extraction.extraction_notes = f"{extraction.extraction_notes}\n{note}".strip()

    proposed_rows = [r.model for r in extraction.results if r.is_proposed and r.model]
    proposed_name = _choose_primary_proposed_model_name(
        extraction=extraction,
        proposed_rows=proposed_rows,
        paper_title=paper_title,
    )
    if not proposed_name:
        extraction.proposed_model = None
        for result in extraction.results:
            result.is_proposed = False
        return

    proposed_key = _canonical_model_name_key(proposed_name)
    exact_name = proposed_name
    matched_exact = False
    for result in extraction.results:
        result.is_proposed = _canonical_model_name_key(result.model) == proposed_key
        if not result.is_proposed and _matches_proposed_model_name(result.model, proposed_name):
            result.is_proposed = True
        if result.is_proposed and _canonical_model_name_key(result.model) == proposed_key:
            exact_name = result.model
            matched_exact = True

    if extraction.proposed_model is None:
        extraction.proposed_model = ProposedModel(name=exact_name)
    else:
        extraction.proposed_model.name = exact_name if matched_exact else proposed_name

    extraction.baseline_models = [
        baseline
        for baseline in extraction.baseline_models
        if _canonical_model_name_key(baseline.name) != proposed_key
    ]


def _choose_primary_proposed_model_name(
    extraction: ExtractionOutput,
    proposed_rows: list[str],
    paper_title: str,
) -> str | None:
    title_lower = paper_title.lower()
    is_benchmarking_title = _title_looks_like_benchmarking_study(title_lower)
    {_canonical_model_name_key(name) for name in proposed_rows if name}
    if (
        extraction.proposed_model is not None
        and not _is_generic_proposed_name(extraction.proposed_model.name)
        and (
            not is_benchmarking_title
            or _model_name_appears_in_title(extraction.proposed_model.name, title_lower)
        )
    ):
        return extraction.proposed_model.name

    title_matches = [
        name
        for name in sorted(set(proposed_rows))
        if _model_name_appears_in_title(name, title_lower)
    ]
    if title_matches:
        return title_matches[0]

    if is_benchmarking_title:
        return None

    if proposed_rows:
        return max(set(proposed_rows), key=lambda name: (proposed_rows.count(name), len(name)))

    if extraction.proposed_model is not None:
        return extraction.proposed_model.name
    return None


def _model_name_appears_in_title(name: str, title_lower: str) -> bool:
    base = _normalise_model_name_text(name).replace("*", "").strip().lower()
    return bool(base) and base in title_lower


def _is_generic_proposed_name(name: str) -> bool:
    lower = _normalise_model_name_text(name).lower()
    generic_terms = (
        "gnn",
        "gnns",
        "model",
        "method",
        "approach",
        "novel approach",
        "new approach",
        "our approach",
        "framework",
        "architecture",
        "baseline",
        "graph neural network",
        "graph neural networks",
        "ours",
        "our model",
        "our method",
        "proposed model",
        "proposed method",
    )
    return any(
        lower == term
        or lower.startswith(term + " ")
        or (term in {"gnn", "gnns"} and lower.startswith(term))
        for term in generic_terms
    )


def _title_looks_like_benchmarking_study(title_lower: str) -> bool:
    hints = ("baseline", "benchmark", "reassess", "comparison", "empirical", "study")
    return any(hint in title_lower for hint in hints)


def _canonical_model_name_key(name: str) -> str:
    clean = _normalise_model_name_text(name).lower().strip()
    clean = clean.rstrip("*")
    clean = re.sub(r"\s*\([^)]*\)\s*$", "", clean)
    clean = re.sub(r"[^a-z0-9]+", "", clean)
    return clean


def _looks_like_ablation_model(name: str) -> bool:
    lower = _normalise_model_name_text(name).lower()
    if "w/o" in lower or "without" in lower or "ablation" in lower:
        return True
    return bool(
        re.search(
            r"\((?:[^)]*dropout|[^)]*normalization|[^)]*normalisation|[^)]*residual|[^)]*remove|[^)]*minus|\s*-[^)]+)\)",
            lower,
        )
    )


def _render_human_readable(
    arxiv_id: str,
    title: str,
    model_name: str,
    results_out: ExtractionOutput,
    figure_out: FigureInfo,
    extraction_strategy: str,
    result_output_format: str,
    experiment_label: str | None,
    usage_summary: dict[str, Any] | None,
) -> str:
    """Render a Markdown verification report."""
    now = datetime.now(UTC).strftime("%Y-%m-%d")
    lines: list[str] = []

    lines.append(f"# Extraction: {title or arxiv_id}")
    lines.append(
        f"**Model used**: `{model_name}`  **Date**: {now}  **Confidence**: {results_out.extraction_confidence}"
    )
    details = [
        f"Strategy: `{extraction_strategy}`",
        f"Result format: `{result_output_format}`",
    ]
    if experiment_label:
        details.append(f"Experiment: `{experiment_label}`")
    lines.append("**Run details**: " + "  ".join(details))
    lines.append("")

    if usage_summary:
        lines.append("## Usage")
        lines.append("")
        lines.append(
            "- "
            f"Extraction calls: {usage_summary.get('total_calls', 0)} total, "
            f"{usage_summary.get('successful_calls', 0)} successful, "
            f"{usage_summary.get('failed_calls', 0)} failed"
        )
        lines.append(
            "- "
            f"Token usage: prompt {usage_summary.get('prompt_tokens', 0)}, "
            f"completion {usage_summary.get('completion_tokens', 0)}, "
            f"total {usage_summary.get('total_tokens', 0)}"
        )
        quota = usage_summary.get("quota_snapshot") or {}
        windows = quota.get("windows") or {}
        if windows:
            quota_bits = []
            for window in ("second", "minute", "hour", "day", "month"):
                values = windows.get(window)
                if not values:
                    continue
                quota_bits.append(
                    f"{window} {values.get('remaining', '?')}/{values.get('limit', '?')} remaining"
                )
            if quota_bits:
                lines.append("- Endpoint request limits at end of run: " + "; ".join(quota_bits))
        burst = quota.get("burst") or {}
        if burst:
            reset = burst.get("reset")
            reset_text = f", resets in {reset}s" if reset else ""
            lines.append(
                "- "
                f"Burst window: {burst.get('remaining', '?')}/{burst.get('limit', '?')} remaining{reset_text}"
            )
        if quota.get("note"):
            lines.append(f"- {quota['note']}")
        lines.append("")

    if results_out.proposed_model:
        pm = results_out.proposed_model
        params_str = f" ({pm.params_millions:.1f}M params)" if pm.params_millions else ""
        lines.append(f"## Proposed Model: {pm.name}{params_str}")
        if pm.model_type:
            lines.append(f"- Type: {pm.model_type}")
        lines.append("")

    if figure_out.figure_id:
        lines.append(f"## Main Figure: {figure_out.figure_id}")
        if figure_out.caption_snippet:
            lines.append(f"> {figure_out.caption_snippet}")
        if figure_out.reason:
            lines.append(f"- {figure_out.reason}")
        lines.append("")

    # Group results by dataset
    datasets: dict[str, list[ResultEntry]] = {}
    for r in results_out.results:
        datasets.setdefault(r.dataset, []).append(r)

    if datasets:
        lines.append("## Results")
        lines.append("")
        for dataset, entries in sorted(datasets.items()):
            metric = entries[0].metric if entries else ""
            direction = "↑" if entries[0].higher_is_better else "↓"
            lines.append(f"### {dataset} — {metric} {direction}")
            lines.append("")
            lines.append("| Model | Value | ±Std | Baseline? | Source | Table |")
            lines.append("|-------|-------|------|-----------|--------|-------|")
            for e in entries:
                std_str = f"{e.std:.4f}" if e.std is not None else "—"
                baseline_str = "Yes" if not e.is_proposed else "No"
                source = e.source_ref or "this paper"
                tbl = e.table_ref or "—"
                lines.append(
                    f"| {e.model} | {e.value:.4f} | {std_str} | {baseline_str} | {source} | {tbl} |"
                )
            lines.append("")

    if results_out.baseline_models:
        lines.append("## Baseline Models Identified")
        lines.append("")
        for bm in results_out.baseline_models:
            hint = f" (from: {bm.original_paper_hint})" if bm.original_paper_hint else ""
            params = f", {bm.params_millions:.1f}M params" if bm.params_millions else ""
            lines.append(f"- **{bm.name}**{params}{hint}")
        lines.append("")

    if results_out.extraction_notes:
        lines.append("## Extraction Notes")
        lines.append("")
        lines.append(textwrap.fill(results_out.extraction_notes, width=100))
        lines.append("")

    lines.append("---")
    lines.append("*This file is auto-generated. Edit `overrides.yaml` to correct errors.*")

    return "\n".join(lines)


def _summarize_call_usage(
    call_log: list[CallRecord],
    quota_snapshot: dict[str, Any] | None,
) -> dict[str, Any]:
    """Summarize per-call usage for the saved extraction artifact."""
    prompt_tokens = sum(rec.prompt_tokens or 0 for rec in call_log)
    completion_tokens = sum(rec.completion_tokens or 0 for rec in call_log)
    successful_calls = sum(1 for rec in call_log if rec.success)
    failed_calls = len(call_log) - successful_calls
    return {
        "total_calls": len(call_log),
        "successful_calls": successful_calls,
        "failed_calls": failed_calls,
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
        "total_tokens": prompt_tokens + completion_tokens,
        "total_input_chars": sum(rec.input_chars for rec in call_log),
        "total_output_chars": sum(rec.output_chars for rec in call_log),
        "total_duration_s": round(sum(rec.duration_s for rec in call_log), 2),
        "quota_snapshot": quota_snapshot or {},
    }


# ── Standalone runner ─────────────────────────────────────────────────────────


def run_extraction(
    arxiv_id: str,
    model_tier: str = "primary",
    screen_first: bool = True,
    fallback_on_failure: bool = True,
    allow_cached_fallback_skip: bool = True,
    extraction_strategy: str = "auto",
    result_output_format: str = "yaml",
    experiment_label: str | None = None,
    verbose: bool = True,
    phase_transition_callback=None,
) -> bool:
    """Compatibility wrapper for the extraction runner module."""
    from backend.extraction_runner import run_extraction as _run_extraction

    return _run_extraction(
        arxiv_id=arxiv_id,
        model_tier=model_tier,
        screen_first=screen_first,
        fallback_on_failure=fallback_on_failure,
        allow_cached_fallback_skip=allow_cached_fallback_skip,
        extraction_strategy=extraction_strategy,
        result_output_format=result_output_format,
        experiment_label=experiment_label,
        verbose=verbose,
        phase_transition_callback=phase_transition_callback,
    )


def run_figure_detection(arxiv_id: str, model_tier: str = "primary") -> bool:
    """Compatibility wrapper for the extraction runner module."""
    from backend.extraction_runner import run_figure_detection as _run_figure_detection

    return _run_figure_detection(arxiv_id=arxiv_id, model_tier=model_tier)


def _update_status(paper_id: int, status: str) -> None:
    with session_scope() as session:
        p = session.get(Paper, paper_id)
        if p:
            p.extraction_status = status


# ── CLI ───────────────────────────────────────────────────────────────────────


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Run LLM extraction on a downloaded paper")
    p.add_argument("arxiv_ids", nargs="+", metavar="ARXIV_ID")
    p.add_argument(
        "--model",
        "-m",
        default="primary",
        help="Model tier (primary/fallback/small) or explicit model name (default: primary)",
    )
    p.add_argument(
        "--strategy",
        choices=["auto", "two-step", "full"],
        default="auto",
        help="Extraction strategy: auto/two-step/full (default: auto)",
    )
    p.add_argument(
        "--result-output-format",
        choices=["yaml"],
        default="yaml",
        help="Structured result format requested from the model (default: yaml)",
    )
    p.add_argument(
        "--experiment-label",
        default=None,
        help="Optional label for experiment artifacts under extracted/experiments/",
    )
    return p


def _slugify_label(label: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9._-]+", "-", label.strip()).strip("-._")
    return slug or "experiment"


def main(argv: list[str] | None = None) -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    args = _build_parser().parse_args(argv)

    ok = total = 0
    for arxiv_id in args.arxiv_ids:
        arxiv_id = normalize_arxiv_id(arxiv_id)
        total += 1
        if run_extraction(
            arxiv_id,
            model_tier=args.model,
            extraction_strategy=args.strategy,
            result_output_format=args.result_output_format,
            experiment_label=args.experiment_label,
        ):
            ok += 1

    print(f"Extracted {ok}/{total} papers.")


if __name__ == "__main__":
    main()
