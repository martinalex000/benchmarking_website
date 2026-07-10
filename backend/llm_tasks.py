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
import logging
import re
from datetime import UTC, datetime
from typing import Any

import yaml
from openai import OpenAI

from backend.config import cfg, normalize_arxiv_id
from backend.dataset_stats_parsing import format_stats_summary, is_statistics_table
from backend.db import session_scope
from backend.json_repair import parse_json_lenient
from backend.llm_backends import client_params_for_model
from backend.llm_client import LLMClientMixin
from backend.llm_metadata import (
    _discovery_text_excerpts,
    _get_known_dataset_names_hint,
    _noncanonical_dataset_hints,
    _ripgrep_dataset_name_hits,
)
from backend.llm_model_options import (
    context_limits_for_model,
    display_name_for_model,
    extraction_max_tokens_for_model,
    is_gpt_oss_model,
)
from backend.llm_postprocessing import (
    _apply_metadata_enrichment,
    _apply_sizes,
    _build_model_size_excerpt,
    _build_smart_excerpt,
    _expand_extraction_payload,
    _extract_proposed_model_hint,
    _merge_extraction_outputs,
    _merge_size_entries,
    _paper_intro_text,
    _rename_generic_proposed_rows,
    _render_human_readable,
    _sanitize_extraction_payload,
    _sanitize_text,
    _split_into_chunks,
    _split_into_table_sections,
    _stabilize_model_names,
    _strip_table_environments,
    _summarize_call_usage,
)
from backend.llm_types import (
    BaselineModelInfo,
    CallRecord,
    DatasetInfo,
    DatasetList,
    DatasetStatisticsOutput,
    ExtractionOutput,
    FigureInfo,
    ModelMetadataEnrichmentEntry,
    ModelMetadataEnrichmentOutput,
    ModelSizeEntry,
    ProposedModel,
    ResultEntry,
    ScreenResult,
    SotaClaimEntry,
    SotaClaimOutput,
)
from backend.models import Paper
from backend.paper_storage import PaperStorage
from backend.qm9_targets import (
    QM9_DEFAULT_METRIC,
    QM9_EXTRACT_TARGET_GROUPS,
    is_qm9_dataset,
    qm9_extract_metric_constraint,
)

# ParsedTable is imported lazily inside run_extraction to avoid slow startup,
# but type-annotated here for clarity.
try:
    from backend.html_parser import ParsedTable as _ParsedTable
except ImportError:
    _ParsedTable = None  # type: ignore[assignment,misc]

logger = logging.getLogger(__name__)

_QM9_EXTRACT_MAX_TOKENS = 16_384

# ── Call logging ───────────────────────────────────────────────────────────────


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


class LLMExtractor(LLMClientMixin):
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
        endpoint, api_key, self._model_route = client_params_for_model(self.model_name)
        self._client = OpenAI(
            api_key=api_key or "none",
            base_url=endpoint or None,
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

        # Token budget: allow enough room for all dataset→table mappings.
        max_tokens = max(1024, len(datasets) * 50 + len(tables) * 30)

        try:
            raw = self._call_json(
                prompt,
                user_content,
                max_tokens=max_tokens,
                call_type="select_tables:all",
            )
            if not isinstance(raw, dict) and self._call_log:
                repaired = parse_json_lenient(self._call_log[-1].raw_response or "")
                if isinstance(repaired, dict):
                    raw = repaired
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
        paper_text = _sanitize_text(paper_text)

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
        tables_truncated = False
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
            tables_truncated = False
            for t in relevant:
                cap = _caption(t)
                md = _sanitize_text(_markdown(t))
                header = f"[Caption: {cap[:120]}]\n" if cap else ""
                table_parts.append(f"{header}{md}")
            joined_tables = "\n\n---\n\n".join(table_parts)
            tables_truncated = len(joined_tables) > max_table_chars
            tables_str = joined_tables[:max_table_chars]
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
            "tables_truncated": tables_truncated if tables else False,
            "context_total_chars": len(context_str),
        }
        return context_str, rag_stats

    @staticmethod
    def _build_tables_only_context(tables: list, max_table_chars: int) -> str:
        """Build a tables-only context block for empty-result retries."""
        if not tables:
            return ""
        parts: list[str] = []
        for t in tables:
            cap = (getattr(t, "caption", None) or "").strip()
            md = _sanitize_text(getattr(t, "markdown", None) or str(t))
            header = f"[Caption: {cap[:120]}]\n" if cap else ""
            parts.append(f"{header}{md}")
        joined = "\n\n---\n\n".join(parts)
        if len(joined) <= max_table_chars:
            return f"=== TABLES (directly pasted) ===\n{joined}"
        return f"=== TABLES (directly pasted) ===\n{joined[:max_table_chars]}"

    @staticmethod
    def _build_single_table_context(table: Any, max_table_chars: int) -> str:
        cap = (getattr(table, "caption", None) or "").strip()
        md = _sanitize_text(getattr(table, "markdown", None) or str(table))
        header = f"[Caption: {cap[:120]}]\n" if cap else ""
        body = f"{header}{md}"[:max_table_chars]
        return f"=== TABLE (directly pasted) ===\n{body}"

    def _dataset_focus_prefix(
        self,
        dataset_name: str,
        *,
        intro_model_hint: str | None,
        metric_constraint: str,
    ) -> str:
        return (
            f'FOCUS: Extract results ONLY for the dataset "{dataset_name}".\n'
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
        )

    def _extract_dataset_with_retries(
        self,
        prompt: str,
        *,
        dataset_name: str,
        ds_tables: list,
        focus_prefix: str,
        full_context: str,
        rag_stats: dict,
        call_type: str,
        max_tokens: int | None = None,
        max_table_chars: int,
    ) -> ExtractionOutput:
        """Extract one dataset with tables-only and per-table retries on empty output."""
        effective_max = max_tokens or extraction_max_tokens_for_model(self.model_name)
        tables_only = self._build_tables_only_context(ds_tables, max_table_chars)

        def _run(content: str, suffix: str) -> ExtractionOutput:
            out = self._extract_results_chunk(
                prompt,
                content,
                call_type=f"{call_type}{suffix}",
                max_tokens=effective_max,
            )
            if self._call_log:
                self._call_log[-1].extra = {**self._call_log[-1].extra, "rag": rag_stats}
            self._fire_progress()
            return out

        attempts: list[tuple[str, str]] = []
        if is_gpt_oss_model(self.model_name) and tables_only:
            # gpt-oss degrades on large prose+table context — prefer tables first.
            attempts.append((":tables_first", tables_only))
            attempts.append(("", full_context))
        else:
            attempts.append(("", full_context))
            if tables_only:
                attempts.append((":tables_only", tables_only))

        out = ExtractionOutput(results=[])
        for suffix, ctx in attempts:
            out = _run(_sanitize_text(focus_prefix + ctx), suffix)
            if out.results and not self._completion_likely_truncated(effective_max):
                return out

        if len(ds_tables) > 1:
            merged_results: list[ResultEntry] = []
            proposed: ProposedModel | None = None
            baselines: list[BaselineModelInfo] = []
            notes_parts: list[str] = []
            confidence_levels: list[str] = []
            for idx, table in enumerate(ds_tables):
                single_ctx = self._build_single_table_context(table, max_table_chars)
                try:
                    table_out = _run(
                        _sanitize_text(focus_prefix + single_ctx),
                        f":table{getattr(table, 'number', idx + 1)}",
                    )
                except Exception as exc:
                    notes_parts.append(f"[table {idx + 1}] failed: {exc}")
                    continue
                merged_results.extend(table_out.results)
                if table_out.proposed_model and proposed is None:
                    proposed = table_out.proposed_model
                baselines.extend(table_out.baseline_models)
                if table_out.extraction_notes:
                    notes_parts.append(table_out.extraction_notes)
                confidence_levels.append(table_out.extraction_confidence)
            if merged_results:
                if self._call_log:
                    self._call_log[-1].extra = {
                        **self._call_log[-1].extra,
                        "empty_result_retry": "per_table",
                    }
                return _merge_extraction_outputs(
                    proposed_model=proposed,
                    baselines=baselines,
                    results=merged_results,
                    confidence_levels=confidence_levels,
                    notes_parts=notes_parts,
                )

        return out

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

        from backend.sota_claim_parsing import main_body_prose_text

        setup_prose = main_body_prose_text(paper_text=paper_text, latex_paper=latex_paper)
        setup_prose_excerpt = ""
        if setup_prose.strip():
            setup_prose_excerpt = (
                "\n\n=== PAPER METHOD & SETUP PROSE (main body, pre-appendix — "
                "use for model_type and uses_external_data) ===\n"
                f"{setup_prose[:12_000]}\n"
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

        rag_text = _sanitize_text(rag_text)
        max_text_chars, max_table_chars = context_limits_for_model(self.model_name)

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
                rag_text,
                ds_tables,
                ds.name,
                max_text_chars=max_text_chars,
                max_table_chars=max_table_chars,
                already_selected=llm_selected,
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
            focus_prefix = self._dataset_focus_prefix(
                ds.name,
                intro_model_hint=intro_model_hint,
                metric_constraint=metric_constraint,
            )
            dataset_context = context + setup_prose_excerpt
            logger.info(
                "Step 2: extracting dataset=%r  context=%d chars",
                ds.name,
                len(focus_prefix) + len(dataset_context),
            )
            extract_max_tokens = extraction_max_tokens_for_model(self.model_name)
            try:
                if is_qm9_dataset(ds.name):
                    base_user_content = _sanitize_text(focus_prefix + dataset_context)
                    for group_idx, targets in enumerate(QM9_EXTRACT_TARGET_GROUPS):
                        group_content = (
                            base_user_content + "\n" + qm9_extract_metric_constraint(targets)
                        )
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
                    out = self._extract_dataset_with_retries(
                        prompt,
                        dataset_name=ds.name,
                        ds_tables=ds_tables,
                        focus_prefix=focus_prefix,
                        full_context=dataset_context,
                        rag_stats=rag_stats,
                        call_type=f"extract_dataset:{ds.name}",
                        max_tokens=extract_max_tokens,
                        max_table_chars=max_table_chars,
                    )
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

        merged = _merge_extraction_outputs(
            proposed_model=proposed,
            baselines=baselines,
            results=all_results,
            confidence_levels=confidence_levels,
            notes_parts=notes_parts,
            normalise_metrics=True,
            discovered_datasets=list(datasets.datasets),
        )
        _stabilize_model_names(merged, paper_title=paper_title, tables=effective_tables)
        return merged

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

    def enrich_model_metadata(
        self,
        scoped_prose: str,
        extraction: ExtractionOutput,
    ) -> ModelMetadataEnrichmentOutput:
        """Infer architecture type and external-data flags from main-body prose."""
        from backend.sota_claim_parsing import chunk_prose_for_extraction

        model_names: list[str] = []
        seen: set[str] = set()
        if extraction.proposed_model and extraction.proposed_model.name:
            key = extraction.proposed_model.name.strip().lower()
            if key and key not in seen:
                seen.add(key)
                model_names.append(extraction.proposed_model.name)
        for baseline in extraction.baseline_models:
            if baseline.name:
                key = baseline.name.strip().lower()
                if key and key not in seen:
                    seen.add(key)
                    model_names.append(baseline.name)
        for result in extraction.results:
            if result.model:
                key = result.model.strip().lower()
                if key and key not in seen:
                    seen.add(key)
                    model_names.append(result.model)

        if not scoped_prose.strip() or not model_names:
            return ModelMetadataEnrichmentOutput()

        prompt = self._read_prompt("model_metadata_enrichment.txt")
        target_block = "=== TARGET MODEL LIST ===\n" + "\n".join(f"- {n}" for n in model_names)
        merged_entries: dict[str, ModelMetadataEnrichmentEntry] = {}
        notes_parts: list[str] = []
        chunks = chunk_prose_for_extraction(scoped_prose)

        for chunk_index, chunk in enumerate(chunks):
            user_content = (
                f"{target_block}\n\n"
                f"=== PAPER PROSE (main body, pre-appendix, no tables) ===\n{chunk}"
            )
            call_type = (
                "enrich_model_metadata"
                if len(chunks) == 1
                else f"enrich_model_metadata_chunk_{chunk_index + 1}"
            )
            try:
                raw = self._call_json(
                    prompt,
                    user_content,
                    max_tokens=cfg.llm_max_tokens,
                    call_type=call_type,
                )
                result = ModelMetadataEnrichmentOutput.model_validate(raw)
                for entry in result.models:
                    key = entry.name.strip().lower()
                    if not key:
                        continue
                    existing = merged_entries.get(key)
                    if existing is None:
                        merged_entries[key] = entry
                        continue
                    if existing.model_type is None and entry.model_type is not None:
                        existing.model_type = entry.model_type
                    if existing.uses_external_data is None and entry.uses_external_data is not None:
                        existing.uses_external_data = entry.uses_external_data
                if result.notes:
                    notes_parts.append(result.notes)
            except Exception as exc:
                logger.warning(
                    "Model metadata enrichment chunk %d failed: %s", chunk_index + 1, exc
                )
                notes_parts.append(f"Chunk {chunk_index + 1} failed: {exc}")

        return ModelMetadataEnrichmentOutput(
            models=list(merged_entries.values()),
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

    def _completion_likely_truncated(self, max_tokens: int) -> bool:
        if not self._call_log:
            return False
        rec = self._call_log[-1]
        if not rec.completion_tokens or max_tokens <= 0:
            return False
        return rec.completion_tokens >= int(max_tokens * 0.95)

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
        effective_max = max_tokens or extraction_max_tokens_for_model(self.model_name)
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
                    max_tokens=effective_max,
                )
                if self._call_log and self._completion_likely_truncated(effective_max):
                    self._call_log[-1].extra = {
                        **self._call_log[-1].extra,
                        "completion_truncated": True,
                    }
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

        metadata_enrichment_out = ModelMetadataEnrichmentOutput()
        if scoped_prose.strip():
            metadata_enrichment_out = self.enrich_model_metadata(scoped_prose, results_out)
            _apply_metadata_enrichment(results_out, metadata_enrichment_out)
            if metadata_enrichment_out.notes:
                results_out.extraction_notes = (
                    f"{results_out.extraction_notes}\n[metadata] {metadata_enrichment_out.notes}"
                ).strip()

        intro_model_hint = _extract_proposed_model_hint(
            paper_title,
            _paper_intro_text(paper_text, latex_paper),
        )
        _rename_generic_proposed_rows(results_out, intro_model_hint)
        if intro_model_hint:
            note = f"Intro-derived proposed-model hint: {intro_model_hint}."
            results_out.extraction_notes = f"{results_out.extraction_notes}\n{note}".strip()
        caption_tables: list = []
        if latex_paper is not None:
            caption_tables = list(latex_paper.tables)
        elif structured_tables is not None:
            caption_tables = list(structured_tables)
        _stabilize_model_names(
            results_out,
            paper_title=paper_title,
            tables=caption_tables,
        )

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
