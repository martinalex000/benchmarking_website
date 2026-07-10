"""Payload normalization and extraction-result post-processing helpers."""

from __future__ import annotations

import logging
import re
import textwrap
from datetime import UTC, datetime
from typing import Any

from thefuzz import fuzz as fuzz_lib
from thefuzz import process as fuzz_process

from backend.llm_types import (
    BaselineModelInfo,
    CallRecord,
    DatasetInfo,
    ExtractionOutput,
    FigureInfo,
    ModelMetadataEnrichmentEntry,
    ModelMetadataEnrichmentOutput,
    ModelSizeEntry,
    ProposedModel,
    ResultEntry,
)
from backend.model_metadata import normalize_architecture_type
from backend.model_name_resolution import normalize_model_name_for_resolution

logger = logging.getLogger(__name__)

_CHUNK_SIZE = 40_000
_SMART_INTRO_CHARS = 3_000
_SMART_TABLES_CHARS = 30_000
_SIZE_FUZZY_MATCH_MIN_SCORE = 88

_SPLIT_PREFIXES = re.compile(
    r"^\s*(?:test|train|training|val|valid|validation)\s*[-_/]?\s*",
    re.IGNORECASE,
)
_NON_TEST_PATTERN = re.compile(
    r"\b(?:train|training|val|valid|validation)\b",
    re.IGNORECASE,
)

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
    """Keep one result per (model identity, dataset, metric), preferring the better value."""
    best: dict[tuple[str, str, str], ResultEntry] = {}
    for result in results:
        key = (
            _canonical_model_name_key(result.model),
            result.dataset.lower(),
            result.metric.lower(),
        )
        existing = best.get(key)
        if existing is None:
            best[key] = result
            continue
        hib = result.higher_is_better
        if hib and result.value > existing.value or not hib and result.value < existing.value:
            best[key] = result
    return list(best.values())


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


def _apply_metadata_enrichment(
    extraction: ExtractionOutput,
    enrichment: ModelMetadataEnrichmentOutput,
) -> None:
    """Merge architecture and external-data enrichment into extraction output."""
    if not enrichment.models:
        return

    by_name: dict[str, ModelMetadataEnrichmentEntry] = {}
    for entry in enrichment.models:
        key = entry.name.strip().lower()
        if key:
            by_name[key] = entry

    if extraction.proposed_model is not None:
        matched = by_name.get(extraction.proposed_model.name.strip().lower())
        if matched is not None and extraction.proposed_model.model_type is None:
            extraction.proposed_model.model_type = matched.model_type

    for baseline in extraction.baseline_models:
        matched = by_name.get(baseline.name.strip().lower())
        if matched is not None and baseline.model_type is None:
            baseline.model_type = matched.model_type

    for result in extraction.results:
        matched = by_name.get(result.model.strip().lower())
        if matched is None:
            continue
        if result.uses_external_data is None and matched.uses_external_data is not None:
            result.uses_external_data = matched.uses_external_data


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


def _apply_table_caption_policies(extraction: ExtractionOutput, tables: list) -> None:
    """Merge model rows when table captions explain footnote markers."""
    from backend.table_caption_interpretation import (
        build_table_caption_policy_map,
        combined_merge_policy,
        is_ablation_table_ref,
        policy_for_table_ref,
        resolve_model_name_for_policy,
    )

    policies = build_table_caption_policy_map(tables)
    default_policy = combined_merge_policy(policies)

    dropped_ablation_tables = 0
    kept_results: list[ResultEntry] = []
    for result in extraction.results:
        if is_ablation_table_ref(result.table_ref, policies):
            dropped_ablation_tables += 1
            continue
        kept_results.append(result)
    extraction.results = kept_results

    if dropped_ablation_tables:
        note = (
            f"Dropped {dropped_ablation_tables} row(s) from ablation/diagnostic tables (caption)."
        )
        extraction.extraction_notes = f"{extraction.extraction_notes}\n{note}".strip()

    if default_policy is None:
        return

    merged_rows = 0
    for result in extraction.results:
        policy = policy_for_table_ref(result.table_ref, policies, default_policy)
        if policy is None:
            continue
        raw = _normalise_model_name_text(result.model)
        resolved = resolve_model_name_for_policy(raw, policy)
        if resolved != raw:
            merged_rows += 1
        result.model = resolved

    for baseline in extraction.baseline_models:
        raw = _normalise_model_name_text(baseline.name)
        resolved = resolve_model_name_for_policy(raw, default_policy)
        if resolved != raw:
            baseline.name = resolved

    if merged_rows:
        note = (
            f"Merged {merged_rows} model row(s) using table caption footnotes "
            f"({default_policy.notes or 'equivalent variants'})."
        )
        extraction.extraction_notes = f"{extraction.extraction_notes}\n{note}".strip()


def _stabilize_model_names(
    extraction: ExtractionOutput,
    paper_title: str = "",
    tables: list | None = None,
) -> None:
    """Normalise model names, drop ablations, and stabilize the main proposed model."""
    if tables:
        _apply_table_caption_policies(extraction, tables)

    if extraction.proposed_model is not None:
        extraction.proposed_model.name = normalize_model_name_for_resolution(
            _normalise_model_name_text(extraction.proposed_model.name)
        )

    for baseline in extraction.baseline_models:
        baseline.name = normalize_model_name_for_resolution(
            _normalise_model_name_text(baseline.name)
        )

    filtered_results: list[ResultEntry] = []
    dropped_ablation_rows = 0
    for result in extraction.results:
        result.model = normalize_model_name_for_resolution(_normalise_model_name_text(result.model))
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

    extraction.results = _dedupe_result_entries(extraction.results)

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
        extraction.results = _dedupe_result_entries(extraction.results)
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

    before_dedupe = len(extraction.results)
    extraction.results = _dedupe_result_entries(extraction.results)
    dropped_variants = before_dedupe - len(extraction.results)
    if dropped_variants:
        note = (
            f"Collapsed {dropped_variants} duplicate variant row(s) for the same "
            "model identity; kept best score per (model, dataset, metric)."
        )
        extraction.extraction_notes = f"{extraction.extraction_notes}\n{note}".strip()


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
