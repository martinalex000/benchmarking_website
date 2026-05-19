"""LLM extraction pipeline.

Orchestrates LLM calls to extract from a paper:
  1. Benchmark results (tables → structured JSON)
  2. Main figure identification
  3. Model parameter counts

Saves:
  - papers/{id}/extracted/llm_output.json   (raw, gitignored)
  - papers/{id}/extracted/results_human_readable.md  (TRACKED in git)

Usage::
    python -m backend.llm_extractor 2206.08164
    python -m backend.llm_extractor 2206.08164 --model fallback
    python -m backend.llm_extractor 2206.08164 --model minimax
"""

from __future__ import annotations

import argparse
import json
import time
import logging
import re
import textwrap
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field as dc_field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from openai import OpenAI, RateLimitError, APIStatusError
from pydantic import BaseModel, Field, field_validator
from tenacity import retry, stop_after_attempt, wait_exponential

from backend.config import cfg
from backend.db import init_db, session_scope
from backend.llm_model_options import display_name_for_model, extra_body_for_model
from backend.models import Paper, PipelineRun
from backend.paper_storage import PaperStorage

# ParsedTable is imported lazily inside run_extraction to avoid slow startup,
# but type-annotated here for clarity.
try:
    from backend.html_parser import ParsedTable as _ParsedTable
except ImportError:
    _ParsedTable = None  # type: ignore[assignment,misc]

logger = logging.getLogger(__name__)

_ARXIV_API = "https://export.arxiv.org/api/query?id_list={arxiv_id}"
_ARXIV_NS = {"atom": "http://www.w3.org/2005/Atom"}


def _title_looks_corrupted(title: str | None) -> bool:
    t = (title or "").strip()
    if not t:
        return True
    return (
        t.startswith("arXiv:") or "\\" in t or t.startswith(": ") or " , " in t or t.count(":") > 1
    )


def _get_top_datasets_hint(limit: int = 50) -> str:
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


def _extract_metadata_from_latex_cache(latex_dir: "Path") -> "dict[str, str]":
    """Read title and abstract from a cached expanded.tex without a full parse.

    Used as a free, offline fallback during abstract screening when the DB has
    only a stub entry and no HTML is available or HTML lacks an abstract.
    Returns a dict with 'title' and/or 'abstract' keys (may be partial).
    """
    expanded = latex_dir / "expanded.tex"
    if not expanded.exists() or expanded.stat().st_size < 100:
        return {}
    try:
        from backend.latex_source import _expand_user_macros, _strip_latex

        tex = expanded.read_text(encoding="utf-8", errors="replace")[:40_000]
        tex, _ = _expand_user_macros(tex)

        result: dict[str, str] = {}

        # Extract \title{...} — handles optional [short] argument
        m = re.search(r"\\title\s*(?:\[[^\]]*\])?\s*\{", tex)
        if m:
            # Walk forward to find the matching closing brace
            start = m.end()
            depth = 1
            pos = start
            while pos < len(tex) and depth > 0:
                if tex[pos] == "{":
                    depth += 1
                elif tex[pos] == "}":
                    depth -= 1
                pos += 1
            raw_title = tex[start : pos - 1]
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
            with urllib.request.urlopen(url, timeout=15) as resp:
                xml_bytes = resp.read()
            root = ET.fromstring(xml_bytes)
            entry = root.find("atom:entry", _ARXIV_NS)
            if entry is None:
                return {}
            title = (entry.find("atom:title", _ARXIV_NS).text or "").replace("\n", " ").strip()
            abstract = (entry.find("atom:summary", _ARXIV_NS).text or "").replace("\n", " ").strip()
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


def _print_call_progress(rec: "CallRecord", call_index: int) -> None:
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
        tok_str = (
            f"prompt={rec.prompt_tokens or '?'}  " f"completion={rec.completion_tokens or '?'}  "
        )

    if _use_rich:
        status = "[green]✓[/green]" if rec.success else "[red]✗[/red]"
        _con.print(
            f"  {status} Call {call_index} "
            f"[bold cyan]{rec.call_type}[/bold cyan]  "
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
            f"  {status} Call {call_index} {rec.call_type}  "
            f"in={rec.input_chars:,}  out={rec.output_chars:,}  {rec.duration_s:.1f}s"
        )
        discovered = rec.extra.get("discovered_datasets")
        if discovered:
            print(f"    Datasets: {', '.join(discovered)}")
        sel = rec.extra.get("selected_tables") or rec.extra.get("selected_tables_per_dataset")
        if sel:
            print(f"    Tables: {sel}")


# ── Pydantic models for structured LLM output ─────────────────────────────────


class ProposedModel(BaseModel):
    name: str
    params_millions: float | None = None
    params_exact: int | None = None
    model_type: str | None = None


class BaselineModelInfo(BaseModel):
    name: str
    params_millions: float | None = None
    original_paper_hint: str | None = None


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


class DatasetList(BaseModel):
    datasets: list[DatasetInfo] = Field(default_factory=list)
    notes: str = ""


class FigureInfo(BaseModel):
    figure_id: str | None = None
    figure_number: int | None = None
    caption_snippet: str | None = None
    img_src: str | None = None
    page_number: int | None = None
    reason: str | None = None


class ModelSizeEntry(BaseModel):
    model_name: str
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


def _normalise_metrics(results: "list[ResultEntry]") -> "list[ResultEntry]":
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


class LLMExtractor:
    """Extracts structured information from a paper using an LLM."""

    def __init__(self, model_tier: str = "primary", streaming: bool = False) -> None:
        self.model_name = cfg.model_for_tier(model_tier)
        self.streaming = streaming
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

    # ── Internal LLM call ─────────────────────────────────────────────────

    def _extra_body(self) -> dict | None:
        """Return model-specific extra_body parameters for chat.completions.create().

        Uses the shared helper so behavior is consistent across scripts.
        """
        return extra_body_for_model(self.model_name)

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
                "Model %r [%s]: %d in → %d out chars | %.2f s total" "%s",
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
                logger.debug("Raw LLM response (first 500 chars): %s", raw[:500])
                logger.error("JSON parse error from %r", self.model_name)
                if self._call_log:
                    self._call_log[-1].parse_error = (
                        f"JSON parse failed — raw (first 200 chars): {raw[:200]}"
                    )
                raise ValueError(
                    f"JSON parse error from {self.model_name!r}: " "could not extract valid JSON"
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

    # ── Extraction tasks ───────────────────────────────────────────────────

    def screen_paper(self, title: str, abstract: str) -> ScreenResult:
        """Stage 1: decide from title+abstract whether a full extraction is warranted."""
        prompt = self._read_prompt("benchmark_check.txt")
        user_content = f"Title: {title}\n\nAbstract:\n{abstract}"
        try:
            raw = self._call_json(prompt, user_content, max_tokens=512, call_type="screen_paper")
            return ScreenResult.model_validate(raw)
        except Exception as exc:
            logger.warning("Abstract screening failed: %s", exc)
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
        known_hint = _get_top_datasets_hint(50)
        if known_hint:
            parts.append(
                f"=== DATASETS ALREADY IN OUR DATABASE (most common, for reference) ===\n"
                f"Match these names exactly when the paper uses the same dataset:\n{known_hint}"
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
        # Include a snippet of experiment-section text so the LLM can see dataset
        # names that appear only in the body (not in intro or table captions).
        exp_text = latex_paper.experiment_text
        if exp_text:
            parts.append(
                f"=== EXPERIMENT SECTION EXCERPT (first 6000 chars) ===\n{exp_text[:6000]}"
            )
        # Inject known-dataset hints from the DB so the model matches canonical names.
        known_hint = _get_top_datasets_hint(50)
        if known_hint:
            parts.append(
                f"=== DATASETS ALREADY IN OUR DATABASE (most common, for reference) ===\n"
                f"Match these names exactly when the paper uses the same dataset:\n{known_hint}"
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
            logger.info(
                "LaTeX dataset discovery: found %d dataset(s): %s",
                len(result.datasets),
                [d.name for d in result.datasets],
            )
            if self._call_log:
                self._call_log[-1].extra = {
                    **self._call_log[-1].extra,
                    "discovered_datasets": [d.name for d in result.datasets],
                }
            self._fire_progress()
            return result
        except Exception as exc:
            logger.warning("LaTeX dataset discovery failed: %s", exc)
            self._fire_progress()
            return DatasetList()

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
        datasets: "list[DatasetInfo]",
        tables: list,
    ) -> "dict[str, list]":
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

            if self._call_log:
                self._call_log[-1].extra = {
                    **self._call_log[-1].extra,
                    "selected_tables_per_dataset": all_selected,
                    "tables_total": len(tables),
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
            logger.warning("Step 1 returned no datasets — returning empty result (no fallback)")
            return ExtractionOutput(
                results=[],
                extraction_notes="Dataset discovery returned no datasets.",
                extraction_confidence="low",
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
                    logger.info(
                        "Overriding primary_metric for %r: %r → %r (from DB)",
                        ds.name,
                        ds.primary_metric,
                        db_pm,
                    )
                    ds.primary_metric = db_pm
        except Exception as _exc:
            logger.debug("DB primary_metric lookup skipped: %s", _exc)

        # Step 2: per-dataset focused extraction
        prompt = self._read_prompt("result_extraction.txt")
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
            metric_constraint = (
                f'PRIMARY METRIC: "{ds.primary_metric}". '
                f"Focus on this metric as the main benchmark result. "
                f"Skip purely secondary diagnostics such as R\u00b2, "
                f"coefficient of determination, or loss values that are "
                f"not standard benchmark scores.\n"
                if ds.primary_metric
                else ""
            )
            user_content = (
                f'FOCUS: Extract results ONLY for the dataset "{ds.name}".\n'
                f"Ignore rows that belong to other datasets.\n"
                f"Use only the STANDARD / DEFAULT configuration of this dataset. "
                f"Skip results for optional variants (e.g. different graph formats, "
                f"SLIC values, or other construction options) if the table shows "
                f"multiple configurations.\n"
                f"{metric_constraint}\n"
                f"{context}"
            )
            logger.info(
                "Step 2: extracting dataset=%r  context=%d chars",
                ds.name,
                len(user_content),
            )
            try:
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

        # Normalise metric names: strip split prefixes and drop non-test results
        all_results = _normalise_metrics(all_results)

        # Deduplicate results by (model, dataset, metric) key
        seen: set[tuple] = set()
        unique_results: list[ResultEntry] = []
        for r in all_results:
            key = (r.model.lower(), r.dataset.lower(), r.metric.lower())
            if key not in seen:
                seen.add(key)
                unique_results.append(r)

        # Deduplicate baselines by name
        seen_b: set[str] = set()
        unique_baselines = [
            b
            for b in baselines
            if not (b.name.lower() in seen_b or seen_b.add(b.name.lower()))  # type: ignore[func-returns-value]
        ]

        final_confidence = (
            "HIGH"
            if confidence_levels and all(c == "HIGH" for c in confidence_levels)
            else "MEDIUM" if confidence_levels and "LOW" not in confidence_levels else "LOW"
        )

        return ExtractionOutput(
            proposed_model=proposed,
            baseline_models=unique_baselines,
            results=unique_results,
            extraction_confidence=final_confidence,
            extraction_notes="\n".join(notes_parts),
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
        prompt = self._read_prompt("result_extraction.txt")

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
                    prompt, chunk + tables_section, call_type=f"extract_chunk:{i+1}"
                )
                all_results.extend(chunk_out.results)
                if chunk_out.proposed_model and proposed is None:
                    proposed = chunk_out.proposed_model
                baselines.extend(chunk_out.baseline_models)
                if chunk_out.extraction_notes:
                    notes_parts.append(f"[Chunk {i+1}] {chunk_out.extraction_notes}")
                confidence_levels.append(chunk_out.extraction_confidence)
            except Exception as exc:
                logger.warning("Chunk %d extraction failed: %s", i + 1, exc)
                notes_parts.append(f"[Chunk {i+1}] Extraction failed: {exc}")

        # Deduplicate results
        seen: set[tuple] = set()
        unique_results: list[ResultEntry] = []
        for r in all_results:
            key = (r.model.lower(), r.dataset.lower(), r.metric.lower())
            if key not in seen:
                seen.add(key)
                unique_results.append(r)

        # Deduplicate baselines
        seen_baselines: set[str] = set()
        unique_baselines: list[BaselineModelInfo] = []
        for b in baselines:
            if b.name.lower() not in seen_baselines:
                seen_baselines.add(b.name.lower())
                unique_baselines.append(b)

        # Pick lowest confidence (most conservative)
        final_confidence = "LOW"
        for level in ["HIGH", "MEDIUM", "LOW"]:
            if level not in confidence_levels:
                continue
            if level == "HIGH" and all(c == "HIGH" for c in confidence_levels):
                final_confidence = "HIGH"
            elif level in ("HIGH", "MEDIUM") and "LOW" not in confidence_levels:
                final_confidence = "MEDIUM"
            break

        return ExtractionOutput(
            proposed_model=proposed,
            baseline_models=unique_baselines,
            results=unique_results,
            extraction_confidence=final_confidence,
            extraction_notes="\n".join(notes_parts),
        )

    def _extract_results_chunk(
        self, prompt: str, text: str, call_type: str = "extract_results"
    ) -> ExtractionOutput:
        raw = self._call_json(prompt, text, call_type=call_type)
        return ExtractionOutput.model_validate(raw)

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
                    prompt, content, call_type=f"extract_section:{i+1}"
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

        # Deduplicate results
        seen: set[tuple] = set()
        unique_results: list[ResultEntry] = []
        for r in all_results:
            key = (r.model.lower(), r.dataset.lower(), r.metric.lower())
            if key not in seen:
                seen.add(key)
                unique_results.append(r)

        # Deduplicate baselines
        seen_b: set[str] = set()
        unique_baselines = [
            b for b in baselines if not (b.name.lower() in seen_b or seen_b.add(b.name.lower()))  # type: ignore[func-returns-value]
        ]

        final_confidence = (
            "HIGH"
            if confidence_levels and all(c == "HIGH" for c in confidence_levels)
            else "MEDIUM" if confidence_levels and "LOW" not in confidence_levels else "LOW"
        )

        return ExtractionOutput(
            proposed_model=proposed,
            baseline_models=unique_baselines,
            results=unique_results,
            extraction_confidence=final_confidence,
            extraction_notes="\n".join(notes_parts),
        )

    def detect_figure(self, paper_text: str, figures_list: list[dict]) -> FigureInfo:
        """Identify the main architecture figure (text-based heuristic).

        Sends paper intro + figure captions to the LLM.  Prefer
        ``detect_figure_vlm()`` when a vision-capable model is configured —
        this text-only fallback is used when no images are available.
        """
        prompt = self._read_prompt("figure_detection.txt")
        figures_summary = "\n".join(
            f"Figure {i+1}: {f.get('caption', '')[:120]} [src={f.get('src', 'N/A')}]"
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

    def detect_figure_vlm(
        self,
        storage: "PaperStorage",
        figures_list: list[dict],
        max_pages: int = 6,
    ) -> FigureInfo:
        """Vision-based main figure detection.

        Renders the first *max_pages* pages of the PDF (or collects HTML images)
        to JPEG, then sends them to the VLM with a short prompt asking which is
        the primary architecture/overview figure.

        Requires:
          - The configured model to support vision inputs (e.g. qwen3.6, gpt-4o).
          - PyMuPDF (``fitz``) for PDF rendering.

        Falls back silently to ``FigureInfo()`` if the model or libraries are
        not available.
        """
        import base64

        images: list[dict] = []  # [{data: b64, media_type: str, label: str}]

        # ── Collect images ────────────────────────────────────────────────
        if storage.html_index_path.exists() and figures_list:
            # For HTML papers: use the local HTML image assets (already downloaded)
            html_dir = storage.html_dir
            for i, fig in enumerate(figures_list[:max_pages]):
                src = fig.get("src", "")
                if not src:
                    continue
                candidate = html_dir / src
                if candidate.exists():
                    data = candidate.read_bytes()
                    suffix = candidate.suffix.lower().lstrip(".")
                    media_type = f"image/{'jpeg' if suffix in ('jpg', 'jpeg') else suffix or 'png'}"
                    images.append(
                        {
                            "data": base64.b64encode(data).decode(),
                            "media_type": media_type,
                            "label": f"Figure {i+1} (src={src}): {fig.get('caption','')[:80]}",
                        }
                    )
        elif storage.pdf_path.exists():
            # For PDF papers: render pages to JPEG at 96 dpi (low-res for speed)
            try:
                import fitz  # PyMuPDF
            except ImportError:
                logger.warning("PyMuPDF not installed — VLM figure detection skipped")
                return FigureInfo()

            try:
                doc = fitz.open(str(storage.pdf_path))
                for page_idx in range(min(max_pages, len(doc))):
                    page = doc[page_idx]
                    mat = fitz.Matrix(96 / 72, 96 / 72)
                    pix = page.get_pixmap(matrix=mat)
                    jpeg_bytes = pix.tobytes("jpeg")
                    images.append(
                        {
                            "data": base64.b64encode(jpeg_bytes).decode(),
                            "media_type": "image/jpeg",
                            "label": f"Page {page_idx + 1}",
                        }
                    )
                doc.close()
            except Exception as exc:
                logger.warning("PDF rendering for VLM failed: %s", exc)
                return FigureInfo()

        if not images:
            logger.debug("VLM figure detection: no images to send")
            return FigureInfo()

        # ── Build multimodal message ──────────────────────────────────────
        content: list[dict] = [
            {
                "type": "text",
                "text": (
                    "You are analyzing a machine learning paper. "
                    "Your task: identify the MAIN figure — an overview diagram, architecture "
                    "illustration, or method pipeline figure that visually explains the paper's "
                    "core contribution.\n\n"
                    "CRITICAL RULES:\n"
                    "  1. You MUST select an image that is clearly a FIGURE (diagram, illustration, "
                    "flowchart, graph, photo). Do NOT select math equations, formula blocks, or "
                    "text even if they describe the model.\n"
                    "  2. Prefer the EARLIEST figure that qualifies (lowest page/figure number).\n"
                    "  3. If no clear architecture/overview figure exists, pick the earliest "
                    "figure that is not a plain results table.\n"
                    "  4. Never select a page or image that is only text or mathematical notation.\n\n"
                    "Reply with ONLY a JSON object (no markdown fences):\n"
                    '{"figure_label": "<exact label from the list below>", '
                    '"caption_snippet": "<first ~15 words of its caption>", '
                    '"reason": "<one sentence>"}\n\n'
                    "Images provided:\n" + "\n".join(f"  - {img['label']}" for img in images)
                ),
            }
        ]
        for img in images:
            content.append(
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:{img['media_type']};base64,{img['data']}",
                    },
                }
            )

        extra_body = self._extra_body()
        # Always use the dedicated VLM tier for vision calls — the fallback and
        # small models typically lack vision support.
        vlm_model = cfg.model_vlm or self.model_name
        try:
            response = self._client.chat.completions.create(
                model=vlm_model,
                messages=[{"role": "user", "content": content}],
                max_tokens=256,
                temperature=0.0,
                extra_body=extra_body,
            )
            raw = (response.choices[0].message.content or "").strip()
        except Exception as exc:
            logger.warning("VLM figure detection API call failed (model=%s): %s", vlm_model, exc)
            return FigureInfo()

        # Parse the JSON response
        try:
            clean = re.sub(r"<think>.*?</think>", "", raw, flags=re.DOTALL).strip()
            clean = re.sub(r"^```(?:json)?\s*", "", clean, flags=re.MULTILINE)
            clean = re.sub(r"\s*```$", "", clean, flags=re.MULTILINE).strip()
            parsed = json.loads(clean)
        except Exception:
            m = re.search(r"\{[\s\S]*\}", raw)
            if m:
                try:
                    parsed = json.loads(m.group(0))
                except Exception:
                    logger.warning("VLM figure response parse failed: %s", raw[:200])
                    return FigureInfo()
            else:
                logger.warning("VLM figure response has no JSON: %s", raw[:200])
                return FigureInfo()

        label: str = parsed.get("figure_label", "")
        caption_snippet: str = parsed.get("caption_snippet", "")
        reason: str = parsed.get("reason", "")

        # Map label back to a FigureInfo (img_src for HTML or page_number for PDF)
        img_src: str | None = None
        page_number: int | None = None

        if storage.html_index_path.exists() and figures_list:
            # Find the matching figure by label (e.g. "Figure 2 (src=x3.png): …")
            for i, fig in enumerate(figures_list[:max_pages]):
                expected_label = f"Figure {i+1} (src={fig.get('src','')}):"
                if label.startswith(f"Figure {i+1}"):
                    img_src = fig.get("src")
                    break
        else:
            # Extract page number from label "Page N"
            m = re.search(r"Page\s+(\d+)", label)
            if m:
                page_number = int(m.group(1)) - 1  # convert to 0-indexed

        result = FigureInfo(
            img_src=img_src,
            page_number=page_number,
            caption_snippet=caption_snippet,
            reason=reason,
        )
        logger.info(
            "VLM figure detection: label=%r img_src=%r page=%s reason=%s",
            label,
            img_src,
            page_number,
            reason,
        )
        return result

    def extract_model_sizes(self, paper_text: str) -> list[ModelSizeEntry]:
        """Extract model parameter counts."""
        prompt = self._read_prompt("model_size.txt")
        try:
            raw = self._call_json(
                prompt, paper_text[:_CHUNK_SIZE], max_tokens=1024, call_type="model_sizes"
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
        structured_tables: list | None = None,
        latex_paper: Any = None,
        use_two_step: bool = True,
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

        # Task 1: Results — prefer LaTeX source, then HTML tables, then legacy path
        if not use_two_step:
            results_out = self.extract_results(paper_text, tables_text)
        elif latex_paper is not None:
            results_out = self.extract_results_two_step(paper_text, [], latex_paper=latex_paper)
        elif structured_tables is not None:
            results_out = self.extract_results_two_step(paper_text, structured_tables)
        else:
            results_out = self.extract_results(paper_text, tables_text)

        # Task 2: Main figure — always use the title page (first figure from list or PDF page 0).
        # VLM-based detection was unreliable and has been removed.
        if figures_list:
            figure_out = FigureInfo(
                img_src=figures_list[0].get("src"),
                reason="title page (first figure)",
            )
        elif storage.pdf_path.exists():
            figure_out = FigureInfo(page_number=0, reason="title page (PDF page 1)")
        else:
            figure_out = FigureInfo()

        # Task 3: Model sizes (merge back into results_out)
        sizes = self.extract_model_sizes(paper_text)
        _apply_sizes(results_out, sizes)

        # Compose full output
        output = {
            "arxiv_id": arxiv_id,
            "model_used": display_name_for_model(self.model_name),
            "extracted_at": datetime.now(timezone.utc).isoformat(),
            "results": results_out.model_dump(),
            "figure": figure_out.model_dump(),
            "model_sizes": [s.model_dump() for s in sizes],
        }

        # Save raw JSON
        storage.llm_output_path.write_text(
            json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8"
        )

        # Save human-readable markdown
        md = _render_human_readable(
            arxiv_id=arxiv_id,
            title=paper_title,
            model_name=self.model_name,
            results_out=results_out,
            figure_out=figure_out,
        )
        storage.human_readable_path.write_text(md, encoding="utf-8")
        logger.info("Saved human-readable extraction to %s", storage.human_readable_path)

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


def _apply_sizes(extraction: ExtractionOutput, sizes: list[ModelSizeEntry]) -> None:
    """Merge model size data back into the extraction output."""
    if extraction.proposed_model is None:
        return
    size_map = {s.model_name.lower(): s for s in sizes}

    proposed_key = extraction.proposed_model.name.lower()
    if proposed_key in size_map:
        s = size_map[proposed_key]
        if extraction.proposed_model.params_millions is None:
            extraction.proposed_model.params_millions = s.params_millions
        if extraction.proposed_model.params_exact is None:
            extraction.proposed_model.params_exact = s.params_exact


def _render_human_readable(
    arxiv_id: str,
    title: str,
    model_name: str,
    results_out: ExtractionOutput,
    figure_out: FigureInfo,
) -> str:
    """Render a Markdown verification report."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    lines: list[str] = []

    lines.append(f"# Extraction: {title or arxiv_id}")
    lines.append(
        f"**Model used**: `{model_name}`  **Date**: {now}  **Confidence**: {results_out.extraction_confidence}"
    )
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


# ── Standalone runner ─────────────────────────────────────────────────────────


def run_extraction(
    arxiv_id: str,
    model_tier: str = "primary",
    screen_first: bool = True,
    fallback_on_failure: bool = True,
    two_step: bool = True,
    verbose: bool = True,
) -> bool:
    """Two-stage extraction for a single paper already downloaded to storage.

    Stage 1 (cheap, small model): screens title+abstract from arXiv to confirm
    this paper contains benchmark results worth extracting.
    Stage 2 (full model): sends the complete paper text to the LLM.

    Args:
        arxiv_id: arXiv ID (no 'arXiv:' prefix).
        model_tier: tier name or explicit model name to use for stage 2.
        screen_first: if False, skip stage 1 and always run stage 2.
        fallback_on_failure: if True (default) and primary fails, auto-retry with fallback tier.
            Set to False when explicitly testing a specific tier (e.g. --compare-models).
        two_step: if False, use the legacy single-shot extraction path (no dataset
            discovery step). Useful for debugging or when the paper has no LaTeX source.
        verbose: if True (default), print live per-call progress to the console using
            rich formatting (same style as compare_models.py).  Set to False in batch
            pipelines where this output would clutter logs.
    """
    from backend.html_parser import parse_html_paper, save_text as html_save
    from backend.pdf_parser import parse_pdf_paper, save_text as pdf_save

    init_db()
    storage = PaperStorage(arxiv_id)

    # Check paper is downloaded (LaTeX, PDF, or legacy HTML)
    has_latex = (storage.latex_dir / "expanded.tex").exists()
    if not storage.pdf_path.exists() and not storage.html_index_path.exists() and not has_latex:
        logger.error("No downloaded content for arXiv:%s — run downloader first", arxiv_id)
        return False

    # Protect existing fallback results: if the current llm_output.json was produced by
    # the fallback model, never overwrite it with a different (usually weaker) model.
    # To explicitly re-process with a different model, pass model_tier="fallback".
    fallback_model_name = cfg.model_for_tier("fallback")
    if model_tier != "fallback" and storage.llm_output_path.exists():
        try:
            existing = json.loads(storage.llm_output_path.read_text(encoding="utf-8"))
            if existing.get("model_used") == fallback_model_name:
                logger.info(
                    "Fallback results already exist for %s (model=%s) — skipping. "
                    "Use model_tier='fallback' to re-run with the fallback model.",
                    arxiv_id,
                    fallback_model_name,
                )
                return True
        except Exception:
            pass  # corrupt JSON or unreadable — proceed normally

    with session_scope() as session:
        paper = session.query(Paper).filter_by(arxiv_id=arxiv_id).first()
        paper_id = paper.id if paper else None
        paper_title = paper.title if paper else ""
        paper_abstract = paper.abstract if paper else ""

    # ── Stage 1: abstract screening ─────────────────────────────────────
    if screen_first:
        # Only call the arXiv API when we genuinely lack a real title/abstract.
        # If the DB already has them (set during a prior run), skip the network call.
        need_meta = not paper_abstract or _title_looks_corrupted(paper_title)
        if need_meta:
            # Try extracting from local HTML first — free, no rate-limit risk
            if storage.html_index_path.exists():
                try:
                    _parsed_meta = parse_html_paper(storage.html_index_path)
                    if _parsed_meta.title:
                        paper_title = _parsed_meta.title
                    if _parsed_meta.abstract:
                        paper_abstract = _parsed_meta.abstract
                    need_meta = not paper_abstract or _title_looks_corrupted(paper_title)
                except Exception:
                    pass

            # Try cached LaTeX (expanded.tex) — always present when previously processed
            if need_meta and storage.latex_dir.exists():
                latex_meta = _extract_metadata_from_latex_cache(storage.latex_dir)
                if latex_meta.get("title"):
                    paper_title = latex_meta["title"]
                if latex_meta.get("abstract"):
                    paper_abstract = latex_meta["abstract"]
                need_meta = not paper_abstract or _title_looks_corrupted(paper_title)

            if need_meta:
                logger.info("Fetching metadata from arXiv API for %s", arxiv_id)
                meta = fetch_arxiv_metadata(arxiv_id)
                paper_title = meta.get("title", paper_title)
                paper_abstract = meta.get("abstract", paper_abstract)
            else:
                meta = {}

            # Persist to DB if we improved on the stub title
            if paper_id and not _title_looks_corrupted(paper_title):
                with session_scope() as session:
                    p = session.get(Paper, paper_id)
                    if p:
                        if _title_looks_corrupted(p.title):
                            p.title = paper_title
                        if not p.abstract:
                            p.abstract = paper_abstract

        if paper_title and not _title_looks_corrupted(paper_title):
            logger.info("Paper: %s", paper_title)

        screener = LLMExtractor(model_tier="small")
        screen = screener.screen_paper(paper_title, paper_abstract)
        if screen.has_benchmark_results or screen.has_new_benchmark:
            datasets_str = (
                ", ".join(screen.datasets_mentioned) if screen.datasets_mentioned else "—"
            )
            logger.info(
                "Stage 1 PASS (conf=%.2f) — datasets: %s%s",
                screen.confidence,
                datasets_str,
                f" | {screen.notes}" if screen.notes else "",
            )
        else:
            logger.warning(
                "Stage 1 REJECT (conf=%.2f): no benchmark results detected in abstract. "
                "Notes: %s. Skipping full extraction.",
                screen.confidence,
                screen.notes or "none",
            )
            # Record rejection in paper_candidates so the dev page shows it
            try:
                from backend.models import PaperCandidate as _PC

                with session_scope() as _s:
                    cand = _s.query(_PC).filter_by(arxiv_id=arxiv_id).first()
                    if cand is None:
                        cand = _PC(
                            arxiv_id=arxiv_id,
                            title=paper_title or f"arXiv:{arxiv_id}",
                            abstract=paper_abstract,
                            discovery_source="run_extraction",
                            discovery_detail="llm_extractor.run_extraction stage1",
                        )
                        _s.add(cand)
                    cand.stage1_passed = 0
                    cand.stage1_confidence = screen.confidence
                    cand.stage1_reason = screen.notes or ""
                    cand.final_status = "rejected_stage1"
            except Exception as _exc:
                logger.debug("Could not record stage1 rejection in paper_candidates: %s", _exc)
            return False

    # ── Stage 2: full paper text extraction ─────────────────────────────
    # Parse text from HTML (preferred) or PDF
    paper_text = ""
    tables_text = ""
    structured_tables: list = []  # list[ParsedTable] when HTML is available
    latex_paper = None  # LatexPaper when LaTeX source is available
    figures_list = []

    # Try LaTeX source first — download/parse it before HTML/PDF so we know whether
    # PDF parsing can be skipped (LaTeX text is always preferred for extraction).
    try:
        from backend.latex_source import download_and_parse as latex_download

        latex_paper = latex_download(arxiv_id, storage.latex_dir)
        if latex_paper:
            n_tables = len(latex_paper.tables)
            n_sections = len(latex_paper.sections)
            n_exp = len(latex_paper.experiment_sections)
            logger.info(
                "LaTeX source loaded for %s: %d tables (%d in appendix), "
                "%d sections (%d experiment-related)",
                arxiv_id,
                n_tables,
                sum(1 for t in latex_paper.tables if t.in_appendix),
                n_sections,
                n_exp,
            )
        else:
            logger.debug("LaTeX source not available for %s — will use PDF text", arxiv_id)
    except Exception as exc:
        logger.warning("LaTeX source download failed for %s: %s", arxiv_id, exc)

    if latex_paper is not None:
        # LaTeX available (preferred) — use its intro text as the paper body; skip PDF parse
        logger.info("Using LaTeX text for arXiv:%s (skipping PDF parse)", arxiv_id)
        paper_text = latex_paper.intro_text or latex_paper.main_tex[:20_000]
        if storage.text_path.exists():
            # Re-use previously saved text if present
            paper_text = storage.text_path.read_text(encoding="utf-8") or paper_text
    elif storage.pdf_path.exists():
        logger.info("Parsing PDF for arXiv:%s", arxiv_id)
        parsed_pdf = parse_pdf_paper(storage.pdf_path, images_dir=storage.figures_dir)
        pdf_save(parsed_pdf, storage.text_path)
        paper_text = parsed_pdf.full_text
    elif storage.html_index_path.exists():
        # Legacy: HTML still present from a previous download — use it as fallback
        logger.info("Parsing HTML (legacy) for arXiv:%s", arxiv_id)
        parsed = parse_html_paper(storage.html_index_path)
        html_save(parsed, storage.text_path)
        paper_text = parsed.full_text
        structured_tables = list(parsed.tables)
        tables_text = "\n\n".join(t.markdown for t in parsed.tables)
        figures_list = [
            {"caption": f.caption, "src": f.src, "element_id": f.element_id} for f in parsed.figures
        ]
        if not paper_title or paper_title.startswith("arXiv:"):
            if parsed.title:
                paper_title = parsed.title
        if not paper_abstract and parsed.abstract:
            paper_abstract = parsed.abstract

    if not paper_text:
        logger.error("No text extracted for arXiv:%s", arxiv_id)
        return False

    # LaTeX source provides the richest table structure (appendix tables, explicit
    # captions, column headers) and is always preferred when available.  The
    # cached expanded.tex is loaded above; here we just log the final text stats.
    logger.info(
        "Text extracted: %d chars%s",
        len(paper_text),
        f" + {len(tables_text)} chars in tables" if tables_text else "",
    )

    # Run LLM extraction — try primary tier, auto-fall back to fallback tier on failure
    extractor = LLMExtractor(model_tier=model_tier)
    if verbose:
        _call_counter: list[int] = [0]

        def _on_call(rec: CallRecord) -> None:
            _call_counter[0] += 1
            _print_call_progress(rec, _call_counter[0])

        extractor._progress_callback = _on_call
        extractor.streaming = True  # enable TTFT / tok/s measurements
    try:
        output = extractor.process_paper(
            arxiv_id=arxiv_id,
            paper_text=paper_text,
            tables_text=tables_text,
            structured_tables=structured_tables,
            latex_paper=latex_paper,
            figures_list=figures_list,
            paper_title=paper_title,
            use_two_step=two_step,
        )
    except Exception as exc:
        # If primary model fails (e.g. context-window too small), retry with fallback
        if model_tier == "primary" and fallback_on_failure:
            fallback = cfg.model_fallback
            logger.warning("Primary model failed (%s); retrying with fallback=%s", exc, fallback)
            return run_extraction(
                arxiv_id,
                model_tier="fallback",
                screen_first=False,
                fallback_on_failure=False,
                two_step=two_step,
                verbose=verbose,
            )
        logger.error("LLM extraction failed for arXiv:%s: %s", arxiv_id, exc)
        # Write an error log + Markdown conversation log to the extracted/ folder
        _write_extraction_error_log(
            storage, arxiv_id, cfg.model_for_tier(model_tier), exc, extractor._call_log
        )
        if paper_id:
            with session_scope() as session:
                session.add(
                    PipelineRun(
                        paper_id=paper_id,
                        stage="extract",
                        status="failed",
                        model_used=display_name_for_model(cfg.model_for_tier(model_tier)),
                        error_message=str(exc),
                    )
                )
            _update_status(paper_id, "failed")
        return False

    actual_model_used = output.get("model_used") or display_name_for_model(
        cfg.model_for_tier(model_tier)
    )

    if paper_id:
        with session_scope() as session:
            p = session.get(Paper, paper_id)
            if p:
                p.extraction_status = "extracted"
                p.extraction_model = actual_model_used
            session.add(
                PipelineRun(
                    paper_id=paper_id,
                    stage="extract",
                    status="success",
                    model_used=actual_model_used,
                )
            )

    # ── Figure extraction ─────────────────────────────────────────────
    figure_info = output.get("figure") or {}
    if figure_info.get("page_number") is not None or figure_info.get("img_src"):
        from backend.figure_extractor import extract_main_figure as _extract_fig

        fig_path = _extract_fig(storage, figure_info)
        if fig_path:
            logger.info("Main figure saved: %s", fig_path.name)
        else:
            logger.warning("Main figure extraction failed for arXiv:%s", arxiv_id)

    return True


def run_figure_detection(arxiv_id: str, model_tier: str = "vlm") -> bool:
    """Re-extract the main figure for an already-extracted paper (--figure-only mode).

    Always uses the title page (first figure in the list or PDF page 0).  The
    *model_tier* parameter is accepted for CLI compatibility but unused.

    Requires the paper to be already downloaded.  Does NOT re-run the full
    results extraction.
    """
    from backend.html_parser import parse_html_paper

    init_db()
    storage = PaperStorage(arxiv_id)

    if (
        not storage.pdf_path.exists()
        and not storage.html_index_path.exists()
        and not (storage.latex_dir / "expanded.tex").exists()
    ):
        logger.error("No downloaded content for arXiv:%s — run downloader first", arxiv_id)
        return False

    if not storage.llm_output_path.exists():
        logger.error("No existing extraction for arXiv:%s — run full extraction first", arxiv_id)
        return False

    # Collect figure list from HTML (if available)
    figures_list: list[dict] = []
    if storage.html_index_path.exists():
        try:
            parsed = parse_html_paper(storage.html_index_path)
            figures_list = [
                {"caption": f.caption, "src": f.src, "element_id": f.element_id}
                for f in parsed.figures
            ]
        except Exception as exc:
            logger.warning("HTML parse failed during figure detection: %s", exc)

    # Always use title page
    if figures_list:
        figure_out = FigureInfo(
            img_src=figures_list[0].get("src"),
            reason="title page (first figure)",
        )
    elif storage.pdf_path.exists():
        figure_out = FigureInfo(page_number=0, reason="title page (PDF page 1)")
    else:
        logger.error("No images or PDF available for figure detection")
        return False

    # Update llm_output.json in-place
    try:
        output = json.loads(storage.llm_output_path.read_text(encoding="utf-8"))
        output["figure"] = figure_out.model_dump()
        storage.llm_output_path.write_text(
            json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8"
        )
        logger.info("Updated figure info in %s", storage.llm_output_path.name)
    except Exception as exc:
        logger.error("Could not update llm_output.json: %s", exc)
        return False

    # Extract / copy the actual figure file
    figure_info = figure_out.model_dump()
    if figure_info.get("page_number") is not None or figure_info.get("img_src"):
        from backend.figure_extractor import extract_main_figure as _extract_fig

        fig_path = _extract_fig(storage, figure_info)
        if fig_path:
            logger.info("Main figure saved: %s", fig_path.name)
            return True
        else:
            logger.warning("Figure asset extraction failed for arXiv:%s", arxiv_id)
            return False
    else:
        logger.warning("No figure identified for arXiv:%s", arxiv_id)
        return False


def _write_extraction_error_log(
    storage: "PaperStorage",
    arxiv_id: str,
    model_name: str,
    exc: BaseException,
    call_log: "list[CallRecord]",
) -> None:
    """Write errors.log and a Markdown conversation log to the extracted/ folder.

    This runs after a fatal extraction failure so the operator can diagnose what
    went wrong without having to re-run in a debugger.  If writing fails, we
    just warn rather than raising (the original failure is already recorded).
    """
    extracted_dir = storage.extracted_dir
    extracted_dir.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc)
    now_str = now.strftime("%Y-%m-%d %H:%M UTC")

    # ── errors.log — one-liner appended each time ─────────────────────────
    error_log = extracted_dir / "errors.log"
    try:
        with error_log.open("a", encoding="utf-8") as fh:
            fh.write(f"[{now_str}] model={model_name}  error={exc!r}\n")
    except OSError as write_exc:
        logger.warning("Could not write errors.log for %s: %s", arxiv_id, write_exc)

    # ── Full conversation log as Markdown ──────────────────────────────────
    lines: list[str] = []
    lines.append(f"# Extraction error log: `{arxiv_id}`")
    lines.append(f"**Model**: `{model_name}`  **Time**: {now_str}")
    lines.append("")
    lines.append(f"## Error")
    lines.append("")
    lines.append(f"```\n{exc!r}\n```")
    lines.append("")
    lines.append(f"## Calls ({len(call_log)} completed before failure)")
    lines.append("")

    for i, rec in enumerate(call_log, 1):
        ttft_str = f"  TTFT={rec.ttft_s:.2f}s" if rec.ttft_s is not None else ""
        tps_str = f"  {rec.tokens_per_sec:.0f} tok/s" if rec.tokens_per_sec else ""
        tok_str = ""
        if rec.prompt_tokens or rec.completion_tokens:
            tok_str = (
                f"  prompt_tokens={rec.prompt_tokens}"
                f"  completion_tokens={rec.completion_tokens}"
            )
        status = "✓" if rec.success else "✗ FAILED"

        lines.append(f"### Call {i}: `{rec.call_type}` {status}")
        lines.append("")
        lines.append(
            f"**Input chars:** {rec.input_chars:,}  "
            f"**Output chars:** {rec.output_chars:,}  "
            f"**Duration:** {rec.duration_s:.1f}s"
            f"{ttft_str}{tps_str}{tok_str}"
        )
        lines.append("")

        # Discovered datasets
        discovered = rec.extra.get("discovered_datasets")
        if discovered is not None:
            lines.append(f"**Datasets discovered:** {', '.join(discovered) or '(none)'}")
            lines.append("")

        # Table selection
        sel = rec.extra.get("selected_tables")
        if sel is not None:
            lines.append(f"**Tables selected:** {sel}")
            lines.append("")
        sel_multi = rec.extra.get("selected_tables_per_dataset")
        if sel_multi is not None:
            for ds_name, nums in sel_multi.items():
                lines.append(f"**Tables for {ds_name}:** {nums}")
            lines.append("")

        # RAG stats
        rag = rec.extra.get("rag")
        if rag:
            lines.append(
                f"**RAG:** paragraphs {rag['paragraphs_selected']}/{rag['paragraphs_total']}  "
                f"tables {rag['tables_selected']}/{rag['tables_total']} "
                f"(`{rag['table_selection_mode']}`)"
            )
            for cap in rag.get("selected_table_captions", []):
                lines.append(f"  - {cap}")
            lines.append("")

        if rec.extra.get("json_parse_method") == "regex":
            lines.append("> ⚠️ JSON extracted via regex fallback")
            lines.append("")
        if rec.parse_error:
            lines.append(f"> ⚠️ Parse error: {rec.parse_error[:300]}")
            lines.append("")

        lines.append("<details>")
        lines.append(f"<summary>System prompt ({len(rec.system_prompt)} chars)</summary>")
        lines.append("")
        lines.append("```text")
        lines.append(rec.system_prompt)
        lines.append("```")
        lines.append("")
        lines.append("</details>")
        lines.append("")

        lines.append("<details>")
        lines.append(f"<summary>User content ({len(rec.user_content)} chars)</summary>")
        lines.append("")
        lines.append("```text")
        lines.append(rec.user_content)
        lines.append("```")
        lines.append("")
        lines.append("</details>")
        lines.append("")

        lines.append("<details>")
        lines.append(f"<summary>Raw response ({len(rec.raw_response)} chars)</summary>")
        lines.append("")
        lines.append("```text")
        lines.append(rec.raw_response)
        lines.append("```")
        lines.append("")
        lines.append("</details>")
        lines.append("")

    md_content = "\n".join(lines)
    ts = now.strftime("%Y%m%d_%H%M%S")
    md_path = extracted_dir / f"extraction_error_{ts}.md"
    try:
        md_path.write_text(md_content, encoding="utf-8")
        logger.info("Extraction error log written to %s", md_path)
    except OSError as write_exc:
        logger.warning("Could not write Markdown error log for %s: %s", arxiv_id, write_exc)


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
    return p


def main(argv: list[str] | None = None) -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    args = _build_parser().parse_args(argv)

    ok = total = 0
    for arxiv_id in args.arxiv_ids:
        arxiv_id = arxiv_id.strip().lstrip("arXiv:").split("v")[0]
        total += 1
        if run_extraction(arxiv_id, model_tier=args.model):
            ok += 1

    print(f"Extracted {ok}/{total} papers.")


if __name__ == "__main__":
    main()
