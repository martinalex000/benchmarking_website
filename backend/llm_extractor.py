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
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from openai import OpenAI
from pydantic import BaseModel, Field, field_validator
from tenacity import retry, stop_after_attempt, wait_exponential

from backend.config import cfg
from backend.db import init_db, session_scope
from backend.models import Paper, PipelineRun
from backend.paper_storage import PaperStorage

logger = logging.getLogger(__name__)

_ARXIV_API = "https://export.arxiv.org/api/query?id_list={arxiv_id}"
_ARXIV_NS = {"atom": "http://www.w3.org/2005/Atom"}


def fetch_arxiv_metadata(arxiv_id: str) -> dict[str, str]:
    """Fetch title, abstract, and published date from the arXiv Atom API. Returns {} on failure."""
    try:
        url = _ARXIV_API.format(arxiv_id=arxiv_id)
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
    except Exception as exc:
        logger.warning("Could not fetch arXiv metadata for %s: %s", arxiv_id, exc)
        return {}


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


class LLMExtractor:
    """Extracts structured information from a paper using an LLM."""

    def __init__(self, model_tier: str = "primary") -> None:
        self.model_name = cfg.model_for_tier(model_tier)
        self._client = OpenAI(
            api_key=cfg.llm_api_key or "none",
            base_url=cfg.llm_endpoint or None,
            timeout=cfg.llm_timeout,
        )

    # ── Internal LLM call ─────────────────────────────────────────────────

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=2, min=5, max=60),
        reraise=True,
    )
    def _call(self, system_prompt: str, user_content: str, max_tokens: int | None = None) -> str:
        start = time.perf_counter()
        try:
            response = self._client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_content},
                ],
                max_tokens=max_tokens or cfg.llm_max_tokens,
                temperature=cfg.llm_temperature,
            )
        except Exception as exc:
            elapsed = time.perf_counter() - start
            logger.warning(
                "LLM request to %r failed in %.2f s: %s — will retry (tenacity/backoff applies)",
                self.model_name,
                elapsed,
                exc,
            )
            raise

        choice = response.choices[0]
        content = (choice.message.content or "").strip()
        elapsed = time.perf_counter() - start
        if not content:
            logger.debug(
                "Model %r returned empty content (finish_reason=%r, input_chars=sys:%d+user:%d, duration=%.2f s)",
                self.model_name,
                choice.finish_reason,
                len(system_prompt),
                len(user_content),
                elapsed,
            )
        else:
            logger.debug(
                "Model %r call completed in %.2f s; response length=%d chars",
                self.model_name,
                elapsed,
                len(content),
            )
        return content

    def _call_json(
        self, system_prompt: str, user_content: str, max_tokens: int | None = None
    ) -> Any:
        """Call LLM and parse JSON from the response. Strips markdown code fences."""
        start = time.perf_counter()
        raw = self._call(system_prompt, user_content, max_tokens)
        elapsed = time.perf_counter() - start
        if not raw:
            raise ValueError(
                f"Model {self.model_name!r} returned an empty response after {elapsed:.2f} s. "
                "The input may be too long — check the model's context-window limit."
            )
        logger.info("LLM %r responded in %.2f s; raw length=%d", self.model_name, elapsed, len(raw))

        # Strip markdown code fences: ```json ... ``` or ``` ... ```
        clean = re.sub(r"^```(?:json)?\s*", "", raw, flags=re.MULTILINE).rstrip("`").strip()
        try:
            return json.loads(clean)
        except json.JSONDecodeError as exc:
            logger.debug("Raw LLM response (first 500 chars): %s", raw[:500])
            logger.error("JSON parse error from %r after %.2f s: %s", self.model_name, elapsed, exc)
            raise ValueError(f"JSON parse error from {self.model_name!r}: {exc}") from exc

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
            raw = self._call_json(prompt, user_content, max_tokens=512)
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
            return self._extract_results_chunk(prompt, combined)

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
            return self._extract_results_chunk(prompt, excerpt)

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
                chunk_out = self._extract_results_chunk(prompt, chunk + tables_section)
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

    def _extract_results_chunk(self, prompt: str, text: str) -> ExtractionOutput:
        raw = self._call_json(prompt, text)
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
                out = self._extract_results_chunk(prompt, content)
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
        """Identify the main architecture figure."""
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
            raw = self._call_json(prompt, user_content, max_tokens=512)
            return FigureInfo.model_validate(raw)
        except Exception as exc:
            logger.warning("Figure detection failed: %s", exc)
            return FigureInfo()

    def extract_model_sizes(self, paper_text: str) -> list[ModelSizeEntry]:
        """Extract model parameter counts."""
        prompt = self._read_prompt("model_size.txt")
        try:
            raw = self._call_json(prompt, paper_text[:_CHUNK_SIZE], max_tokens=1024)
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
    ) -> dict:
        """Run all extraction tasks and save outputs.

        Returns a combined dict with all extraction results.
        """
        storage = PaperStorage(arxiv_id)
        storage.extracted_dir.mkdir(parents=True, exist_ok=True)

        logger.info("Extracting results for arXiv:%s with model=%s", arxiv_id, self.model_name)

        # Task 1: Results
        results_out = self.extract_results(paper_text, tables_text)

        # Task 2: Main figure
        figure_out = self.detect_figure(paper_text, figures_list)

        # Task 3: Model sizes (merge back into results_out)
        sizes = self.extract_model_sizes(paper_text)
        _apply_sizes(results_out, sizes)

        # Compose full output
        output = {
            "arxiv_id": arxiv_id,
            "model_used": self.model_name,
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
    """
    from backend.html_parser import parse_html_paper, save_text as html_save
    from backend.pdf_parser import parse_pdf_paper, save_text as pdf_save

    init_db()
    storage = PaperStorage(arxiv_id)

    # Check paper is downloaded
    if not storage.pdf_path.exists() and not storage.html_index_path.exists():
        logger.error("No downloaded content for arXiv:%s — run downloader first", arxiv_id)
        return False

    with session_scope() as session:
        paper = session.query(Paper).filter_by(arxiv_id=arxiv_id).first()
        paper_id = paper.id if paper else None
        paper_title = paper.title if paper else ""
        paper_abstract = paper.abstract if paper else ""

    # ── Stage 1: abstract screening ─────────────────────────────────────
    if screen_first:
        # Prefer stored abstract; fall back to fetching from arXiv API
        if not paper_abstract or paper_title.startswith("arXiv:"):
            logger.info("Fetching metadata from arXiv API for %s", arxiv_id)
            meta = fetch_arxiv_metadata(arxiv_id)
            paper_title = meta.get("title", paper_title)
            paper_abstract = meta.get("abstract", paper_abstract)
            # Persist to DB if we got fresh data
            if paper_id and meta.get("title"):
                with session_scope() as session:
                    p = session.get(Paper, paper_id)
                    if p:
                        if p.title.startswith("arXiv:"):
                            p.title = meta["title"]
                        if not p.abstract:
                            p.abstract = meta.get("abstract", "")

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
            return False

    # ── Stage 2: full paper text extraction ─────────────────────────────
    # Parse text from HTML (preferred) or PDF
    paper_text = ""
    tables_text = ""
    figures_list = []

    if storage.html_index_path.exists():
        logger.info("Parsing HTML for arXiv:%s", arxiv_id)
        parsed = parse_html_paper(storage.html_index_path)
        html_save(parsed, storage.text_path)
        paper_text = parsed.full_text
        tables_text = "\n\n".join(t.markdown for t in parsed.tables)
        figures_list = [
            {"caption": f.caption, "src": f.src, "element_id": f.element_id} for f in parsed.figures
        ]
    elif storage.pdf_path.exists():
        logger.info("Parsing PDF for arXiv:%s", arxiv_id)
        parsed_pdf = parse_pdf_paper(storage.pdf_path, images_dir=storage.figures_dir)
        pdf_save(parsed_pdf, storage.text_path)
        paper_text = parsed_pdf.full_text

    if not paper_text:
        logger.error("No text extracted for arXiv:%s", arxiv_id)
        return False

    logger.info(
        "Text extracted: %d chars%s",
        len(paper_text),
        f" + {len(tables_text)} chars in tables" if tables_text else "",
    )

    # Run LLM extraction — try primary tier, auto-fall back to fallback tier on failure
    extractor = LLMExtractor(model_tier=model_tier)
    try:
        output = extractor.process_paper(
            arxiv_id=arxiv_id,
            paper_text=paper_text,
            tables_text=tables_text,
            figures_list=figures_list,
            paper_title=paper_title,
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
            )
        logger.error("LLM extraction failed for arXiv:%s: %s", arxiv_id, exc)
        if paper_id:
            with session_scope() as session:
                session.add(
                    PipelineRun(
                        paper_id=paper_id,
                        stage="extract",
                        status="failed",
                        model_used=cfg.model_for_tier(model_tier),
                        error_message=str(exc),
                    )
                )
            _update_status(paper_id, "failed")
        return False

    if paper_id:
        with session_scope() as session:
            p = session.get(Paper, paper_id)
            if p:
                p.extraction_status = "extracted"
                p.extraction_model = cfg.model_for_tier(model_tier)
            session.add(
                PipelineRun(
                    paper_id=paper_id,
                    stage="extract",
                    status="success",
                    model_used=cfg.model_for_tier(model_tier),
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
