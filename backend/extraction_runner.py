"""Operational runner functions for extraction and figure refresh workflows."""

from __future__ import annotations

import logging
from collections.abc import Callable
from datetime import UTC, datetime

from openai import APIStatusError, RateLimitError

from backend.config import cfg
from backend.db import init_db, session_scope
from backend.llm_metadata import (
    _extract_metadata_from_latex_cache,
    _title_looks_corrupted,
    fetch_arxiv_metadata,
)
from backend.llm_model_options import display_name_for_model
from backend.llm_tasks import LLMExtractor, _print_call_progress, _update_status
from backend.llm_types import CallRecord, FigureInfo
from backend.models import Paper, PipelineRun
from backend.paper_storage import PaperStorage
from backend.text_cleanup import abstract_has_latex_artifacts, clean_extracted_text

logger = logging.getLogger(__name__)


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
    phase_transition_callback: Callable[[str], None] | None = None,
) -> bool:
    """Two-stage extraction for a single paper already downloaded to storage."""
    from backend.html_parser import parse_html_paper
    from backend.html_parser import save_text as html_save
    from backend.pdf_parser import parse_pdf_paper
    from backend.pdf_parser import save_text as pdf_save

    init_db()
    storage = PaperStorage(arxiv_id)

    has_latex = (storage.latex_dir / "expanded.tex").exists()
    if not storage.pdf_path.exists() and not storage.html_index_path.exists() and not has_latex:
        logger.error("No downloaded content for arXiv:%s — run downloader first", arxiv_id)
        return False

    fallback_model_name = cfg.model_for_tier("fallback")
    requested_model_name = cfg.model_for_tier(model_tier)
    if (
        allow_cached_fallback_skip
        and experiment_label is None
        and model_tier != "fallback"
        and requested_model_name != fallback_model_name
        and storage.llm_output_path.exists()
    ):
        try:
            existing = storage.load_llm_output()
            if existing.get("model_used") == fallback_model_name:
                logger.info(
                    "Fallback results already exist for %s (model=%s) — skipping. "
                    "Use model_tier='fallback' to re-run with the fallback model.",
                    arxiv_id,
                    fallback_model_name,
                )
                return True
        except (ValueError, OSError) as exc:
            logger.error("Corrupted fallback cache for %s: %s", arxiv_id, exc)

    with session_scope() as session:
        paper = session.query(Paper).filter_by(arxiv_id=arxiv_id).first()
        paper_id = paper.id if paper else None
        paper_title = paper.title if paper else ""
        raw_paper_abstract = paper.abstract if paper else ""
        paper_abstract = clean_extracted_text(raw_paper_abstract)
        abstract_has_artifacts = abstract_has_latex_artifacts(raw_paper_abstract)

    def _fetch_best_metadata(allow_arxiv_api: bool = True) -> dict[str, str]:
        meta: dict[str, str] = {}
        try:
            from backend.semantic_scholar import fetch_paper_metadata as _fetch_s2

            meta = _fetch_s2(arxiv_id)
        except Exception:
            meta = {}

        if (
            (meta.get("title") and meta.get("abstract"))
            or not allow_arxiv_api
            or cfg.semantic_scholar_api_key
        ):
            return meta

        try:
            arxiv_meta = fetch_arxiv_metadata(arxiv_id)
        except Exception:
            return meta

        return {
            "title": meta.get("title") or arxiv_meta.get("title", ""),
            "abstract": meta.get("abstract") or arxiv_meta.get("abstract", ""),
            "published_date": meta.get("published_date") or arxiv_meta.get("published_date", ""),
            "venue": meta.get("venue") or arxiv_meta.get("venue", ""),
        }

    if screen_first:
        need_meta = (
            not paper_abstract or abstract_has_artifacts or _title_looks_corrupted(paper_title)
        )
        if need_meta:
            if storage.html_index_path.exists():
                try:
                    parsed_meta = parse_html_paper(storage.html_index_path)
                    if parsed_meta.title:
                        paper_title = parsed_meta.title
                    if parsed_meta.abstract:
                        paper_abstract = parsed_meta.abstract
                        abstract_has_artifacts = abstract_has_latex_artifacts(parsed_meta.abstract)
                    need_meta = (
                        not paper_abstract
                        or abstract_has_artifacts
                        or _title_looks_corrupted(paper_title)
                    )
                except (ValueError, OSError) as exc:
                    logger.warning("HTML parse failed for metadata: %s", exc)

            if need_meta and storage.latex_dir.exists():
                latex_meta = _extract_metadata_from_latex_cache(storage.latex_dir)
                if latex_meta.get("title"):
                    paper_title = latex_meta["title"]
                if latex_meta.get("abstract"):
                    paper_abstract = latex_meta["abstract"]
                    abstract_has_artifacts = abstract_has_latex_artifacts(latex_meta["abstract"])
                need_meta = (
                    not paper_abstract
                    or abstract_has_artifacts
                    or _title_looks_corrupted(paper_title)
                )

            if need_meta:
                logger.info("Fetching metadata from Semantic Scholar for %s", arxiv_id)
                meta = _fetch_best_metadata()
                paper_title = meta.get("title", paper_title)
                paper_abstract = meta.get("abstract", paper_abstract)

            if paper_id and not _title_looks_corrupted(paper_title):
                with session_scope() as session:
                    p = session.get(Paper, paper_id)
                    if p:
                        if _title_looks_corrupted(p.title):
                            p.title = paper_title
                        if not p.abstract or abstract_has_latex_artifacts(p.abstract):
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
            try:
                from backend.models import PaperCandidate as _PC

                with session_scope() as pending_session:
                    cand = pending_session.query(_PC).filter_by(arxiv_id=arxiv_id).first()
                    if cand is None:
                        cand = _PC(
                            arxiv_id=arxiv_id,
                            title=paper_title or f"arXiv:{arxiv_id}",
                            abstract=paper_abstract,
                            discovery_source="run_extraction",
                            discovery_detail="llm_extractor.run_extraction stage1",
                        )
                        pending_session.add(cand)
                    cand.stage1_passed = 0
                    cand.stage1_confidence = screen.confidence
                    cand.stage1_reason = screen.notes or ""
                    cand.final_status = "rejected_stage1"
            except Exception as exc:
                logger.debug("Could not record stage1 rejection in paper_candidates: %s", exc)
            return False

    paper_text = ""
    tables_text = ""
    structured_tables: list = []
    latex_paper = None
    figures_list = []

    try:
        from backend.latex_source import download_and_parse as latex_download

        latex_paper = latex_download(arxiv_id, storage.latex_dir)
        if latex_paper:
            logger.info(
                "LaTeX source loaded for %s: %d tables (%d in appendix), %d sections (%d experiment-related)",
                arxiv_id,
                len(latex_paper.tables),
                sum(1 for t in latex_paper.tables if t.in_appendix),
                len(latex_paper.sections),
                len(latex_paper.experiment_sections),
            )
        else:
            logger.debug("LaTeX source not available for %s — will use PDF text", arxiv_id)
    except Exception as exc:
        logger.warning("LaTeX source download failed for %s: %s", arxiv_id, exc)

    if latex_paper is not None:
        logger.info("Using LaTeX text for arXiv:%s (skipping PDF parse)", arxiv_id)
        if extraction_strategy == "full":
            paper_text = latex_paper.main_tex
        else:
            paper_text = latex_paper.intro_text or latex_paper.main_tex[:20_000]
        if extraction_strategy != "full" and storage.text_path.exists():
            paper_text = storage.text_path.read_text(encoding="utf-8") or paper_text
    elif storage.pdf_path.exists():
        logger.info("Parsing PDF for arXiv:%s", arxiv_id)
        parsed_pdf = parse_pdf_paper(storage.pdf_path, images_dir=storage.figures_dir)
        pdf_save(parsed_pdf, storage.text_path)
        paper_text = parsed_pdf.full_text
    elif storage.html_index_path.exists():
        logger.info("Parsing HTML (legacy) for arXiv:%s", arxiv_id)
        parsed = parse_html_paper(storage.html_index_path)
        html_save(parsed, storage.text_path)
        paper_text = parsed.full_text
        structured_tables = list(parsed.tables)
        tables_text = "\n\n".join(t.markdown for t in parsed.tables)
        figures_list = [
            {"caption": f.caption, "src": f.src, "element_id": f.element_id} for f in parsed.figures
        ]
        if (not paper_title or paper_title.startswith("arXiv:")) and parsed.title:
            paper_title = parsed.title
        if (not paper_abstract or abstract_has_latex_artifacts(paper_abstract)) and parsed.abstract:
            paper_abstract = parsed.abstract

    if not paper_text:
        logger.error("No text extracted for arXiv:%s", arxiv_id)
        return False

    logger.info(
        "Text extracted: %d chars%s",
        len(paper_text),
        f" + {len(tables_text)} chars in tables" if tables_text else "",
    )

    extractor = LLMExtractor(model_tier=model_tier, result_output_format=result_output_format)
    if verbose:
        call_counter: list[int] = [0]
        phase_state: dict[str, str | None] = {"current": None}

        def _call_phase(call_type: str) -> str | None:
            if call_type.startswith("discover_datasets") or call_type.startswith("select_tables"):
                return "discovery"
            if call_type == "extract_dataset_statistics":
                return "dataset_statistics"
            if call_type.startswith("extract_dataset") or call_type.startswith("extract_section"):
                return "dataset_extraction"
            return None

        def _on_call(rec: CallRecord) -> None:
            phase = _call_phase(rec.call_type or "")
            if (
                phase is not None
                and phase_transition_callback is not None
                and phase_state["current"] != phase
            ):
                phase_state["current"] = phase
                phase_transition_callback(phase)
            call_counter[0] += 1
            _print_call_progress(rec, call_counter[0])

        extractor._progress_callback = _on_call
        extractor.streaming = True
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
        )
    except KeyboardInterrupt:
        _update_status(paper_id, "failed")
        raise
    except (OSError, FileNotFoundError) as exc:
        logger.error("System error during extraction for %s: %s", arxiv_id, exc)
        write_extraction_error_log(
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
        raise
    except (RateLimitError, APIStatusError) as exc:
        if model_tier == "primary" and fallback_on_failure:
            fallback = cfg.model_fallback
            logger.warning("Primary model failed (%s); retrying with fallback=%s", exc, fallback)
            return run_extraction(
                arxiv_id,
                model_tier="fallback",
                screen_first=False,
                fallback_on_failure=False,
                extraction_strategy=extraction_strategy,
                result_output_format=result_output_format,
                experiment_label=experiment_label,
                verbose=verbose,
            )
        logger.error("LLM extraction failed for arXiv:%s: %s", arxiv_id, exc)
        write_extraction_error_log(
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
    except Exception as exc:
        logger.error("Unexpected error during extraction for arXiv:%s: %s", arxiv_id, exc)
        write_extraction_error_log(
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
        raise

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

    figure_info = output.get("figure") or {}
    if figure_info.get("page_number") is not None or figure_info.get("img_src"):
        from backend.figure_extractor import extract_main_figure as _extract_fig

        fig_path = _extract_fig(storage, figure_info)
        if fig_path:
            logger.info("Main figure saved: %s", fig_path.name)
        else:
            logger.warning("Main figure extraction failed for arXiv:%s", arxiv_id)

    return True


def run_figure_detection(arxiv_id: str, model_tier: str = "primary") -> bool:
    """Re-extract the main figure for an already-extracted paper (--figure-only mode)."""
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

    if figures_list:
        figure_out = FigureInfo(
            img_src=figures_list[0].get("src"), reason="title page (first figure)"
        )
    elif storage.pdf_path.exists():
        figure_out = FigureInfo(page_number=0, reason="title page (PDF page 1)")
    else:
        logger.error("No images or PDF available for figure detection")
        return False

    try:
        output = storage.load_llm_output()
        output["figure"] = figure_out.model_dump()
        storage.save_llm_output(output)
        logger.info("Updated figure info in %s", storage.llm_output_path.name)
    except Exception as exc:
        logger.error("Could not update extraction output: %s", exc)
        return False

    figure_info = figure_out.model_dump()
    if figure_info.get("page_number") is not None or figure_info.get("img_src"):
        from backend.figure_extractor import extract_main_figure as _extract_fig

        fig_path = _extract_fig(storage, figure_info)
        if fig_path:
            logger.info("Main figure saved: %s", fig_path.name)
            return True
        logger.warning("Figure asset extraction failed for arXiv:%s", arxiv_id)
        return False

    logger.warning("No figure identified for arXiv:%s", arxiv_id)
    return False


def write_extraction_error_log(
    storage: PaperStorage,
    arxiv_id: str,
    model_name: str,
    exc: BaseException,
    call_log: list[CallRecord],
) -> None:
    """Write errors.log and a Markdown conversation log to the extracted/ folder."""
    extracted_dir = storage.extracted_dir
    extracted_dir.mkdir(parents=True, exist_ok=True)
    now = datetime.now(UTC)
    now_str = now.strftime("%Y-%m-%d %H:%M UTC")

    error_log = extracted_dir / "errors.log"
    try:
        with error_log.open("a", encoding="utf-8") as fh:
            fh.write(f"[{now_str}] model={model_name}  error={exc!r}\n")
    except OSError as write_exc:
        logger.warning("Could not write errors.log for %s: %s", arxiv_id, write_exc)

    lines: list[str] = []
    lines.append(f"# Extraction error log: `{arxiv_id}`")
    lines.append(f"**Model**: `{model_name}`  **Time**: {now_str}")
    lines.append("")
    lines.append("## Error")
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
                f"  prompt_tokens={rec.prompt_tokens}  completion_tokens={rec.completion_tokens}"
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

        discovered = rec.extra.get("discovered_datasets")
        if discovered is not None:
            lines.append(f"**Datasets discovered:** {', '.join(discovered) or '(none)'}")
            lines.append("")

        sel = rec.extra.get("selected_tables")
        if sel is not None:
            lines.append(f"**Tables selected:** {sel}")
            lines.append("")
        sel_multi = rec.extra.get("selected_tables_per_dataset")
        if sel_multi is not None:
            for ds_name, nums in sel_multi.items():
                lines.append(f"**Tables for {ds_name}:** {nums}")
            lines.append("")

        if (rec.call_type or "").startswith(("discover_datasets", "select_tables")):
            stats = rec.extra.get("statistics_tables")
            if stats:
                lines.append(
                    "**Statistics tables:** "
                    + ", ".join(
                        f"Table {item['number']}"
                        + (" [appendix]" if item.get("in_appendix") else "")
                        for item in stats
                    )
                )
                lines.append("")
            note = rec.extra.get("table_selection_note")
            if note:
                lines.append(f"**Table selection note:** {note}")
                lines.append("")
            stats = rec.extra.get("dataset_statistics")
            if stats:
                lines.append("**Dataset statistics (discovery):**")
                for item in stats:
                    name = item.get("name", "?")
                    if item.get("statistics_mentioned"):
                        sources = ", ".join(item.get("statistics_sources") or []) or "detected"
                        lines.append(f"- {name}: yes ({sources})")
                    else:
                        lines.append(f"- {name}: no")
                lines.append("")

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
