"""Development/admin Hugo export helpers."""

from __future__ import annotations

import json
import logging
import time
from collections.abc import Iterator
from contextlib import contextmanager
from dataclasses import dataclass
from typing import Any

from sqlalchemy.orm import Session, joinedload

from backend.config import cfg
from backend.dataset_discovery import classify_dataset_info
from backend.dataset_stats_parsing import format_stats_summary
from backend.db import session_scope
from backend.export_helpers import sanitize_title
from backend.models import (
    Dataset,
    Paper,
    PaperCandidate,
    PaperDatasetStatistics,
    PaperSotaClaim,
    PendingDataset,
    TodoPaper,
)
from backend.pending_datasets import discovery_payload_dict
from backend.sota_claim_verifier import is_unrestricted_claim, verify_unrestricted_claims

logger = logging.getLogger(__name__)

TODO_EXPORT_LIMIT = 500


@dataclass
class DevExportSnapshot:
    """Rows shared by development summaries and pages in one export run."""

    papers: list[Paper]
    stage1_skipped: list[PaperCandidate]
    stage2_skipped: list[PaperCandidate]
    todo_rows: list[TodoPaper]

    @classmethod
    def load(cls, session: Session) -> DevExportSnapshot:
        return cls(
            papers=session.query(Paper).all(),
            stage1_skipped=session.query(PaperCandidate)
            .filter(PaperCandidate.stage1_passed == 0)
            .all(),
            stage2_skipped=session.query(PaperCandidate)
            .filter(PaperCandidate.stage2_passed == 0)
            .all(),
            todo_rows=session.query(TodoPaper)
            .order_by(TodoPaper.is_manually_important.desc(), TodoPaper.seen_count.desc())
            .all(),
        )


def _dev_line_start(text: str) -> None:
    import sys

    sys.stdout.write(f"\n{text}")
    sys.stdout.flush()


def _dev_line_done(text: str) -> None:
    import sys

    sys.stdout.write(f"\r{text}\n")
    sys.stdout.flush()


@contextmanager
def _dev_export_step(label: str, *, indent: int = 2) -> Iterator[dict[str, str]]:
    """Log a development-export sub-step on one line, extended with done + elapsed time."""
    prefix = " " * indent
    meta = {"suffix": ""}
    _dev_line_start(f"{prefix}{label}...")
    t0 = time.perf_counter()
    try:
        yield meta
    finally:
        elapsed = time.perf_counter() - t0
        _dev_line_done(f"{prefix}{label}... done ({elapsed:.1f}s){meta['suffix']}")


def export_development_data(*, session: Session | None = None) -> dict[str, int]:
    """Write development data files for debugging/admin purposes."""
    from backend import export_to_hugo as hugo

    hugo._DATA_DIR.mkdir(parents=True, exist_ok=True)
    hugo._CONTENT.mkdir(parents=True, exist_ok=True)

    def _run(sess: Session) -> dict[str, int]:
        return _export_development_data_impl(sess, hugo)

    if session is not None:
        return _run(session)
    with session_scope() as scoped:
        return _run(scoped)


def _export_development_data_impl(session: Session, hugo: Any) -> dict[str, int]:
    data_files = 0
    snapshot = DevExportSnapshot.load(session)
    with _dev_export_step("development JSON"):
        status_counts: dict[str, int] = {}
        papers = snapshot.papers
        for paper in papers:
            status_counts[paper.extraction_status] = (
                status_counts.get(paper.extraction_status, 0) + 1
            )

        skipped_papers = snapshot.stage1_skipped
        stage2_skipped = snapshot.stage2_skipped

        missing_daily = sum(
            1 for p in papers if not p.published_date or len(p.published_date.strip()) < 10
        )

        dev_data = {
            "paper_status": {"total": len(papers), "by_status": status_counts},
            "skipped": {
                "stage1_count": len(skipped_papers),
                "stage2_count": len(stage2_skipped),
            },
            "date_refinement": {
                "missing_daily_count": missing_daily,
            },
        }

        (hugo._DATA_DIR / "development.json").write_text(
            json.dumps(dev_data, indent=2, ensure_ascii=False), encoding="utf-8"
        )
        data_files += 1

        try:
            todo_rows = snapshot.todo_rows[:TODO_EXPORT_LIMIT]
            todo_list = []
            for row in todo_rows:
                todo_list.append(
                    {
                        "arxiv_id": row.arxiv_id,
                        "title": sanitize_title(row.title),
                        "status": row.status,
                        "seen_count": int(row.seen_count or 0),
                        "is_manually_important": bool(row.is_manually_important),
                        "seen_from": json.loads(row.seen_from) if row.seen_from else [],
                        "first_seen_at": row.first_seen_at,
                    }
                )
            (hugo._DATA_DIR / "todo_papers.json").write_text(
                json.dumps(
                    {
                        "total_count": len(snapshot.todo_rows),
                        "exported_count": len(todo_list),
                        "limit": TODO_EXPORT_LIMIT,
                        "papers": todo_list,
                    },
                    indent=2,
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            data_files += 1
        except Exception:
            logger.exception("Failed to export todo_papers.json")

    pages = create_dev_pages(session=session, snapshot=snapshot)
    return {"pages": pages, "data_files": data_files}


def create_dev_pages(
    *, session: Session | None = None, snapshot: DevExportSnapshot | None = None
) -> int:
    """Generate development/admin pages. Returns number of markdown pages written."""
    from backend import export_to_hugo as hugo

    content_dev = hugo._CONTENT / "dev"
    content_dev.mkdir(parents=True, exist_ok=True)

    def _run(sess: Session) -> int:
        with _dev_export_step("development pages"):
            return _create_dev_pages_impl(
                sess, hugo, content_dev, snapshot or DevExportSnapshot.load(sess)
            )

    if session is not None:
        return _run(session)
    with session_scope() as scoped:
        return _run(scoped)


def _write_problematic_latex_papers_page(hugo: Any, content_dev: Any) -> None:
    """Render Development → Problematic Papers from scan JSON."""
    json_path = hugo._DATA_DIR / "problematic_latex_papers.json"
    payload: dict[str, Any] = {}
    if json_path.is_file():
        try:
            payload = json.loads(json_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            logger.warning("Could not read %s: %s", json_path, exc)

    papers = payload.get("papers") or []
    scanned_at = payload.get("scanned_at") or "—"
    lines = [
        "## Problematic Papers (LaTeX table coverage)",
        "",
        "Papers whose LaTeX source may have benchmark tables that were invisible to "
        "the extractor: `wraptable`, `sidewaystable`, or tabular rows with multiple "
        "`&` separators outside parsed table environments.",
        "",
        "Regenerate this list on the server with:",
        "",
        "```bash",
        "uv run python scripts/scan_latex_table_issues.py --write-list --export-json",
        "uv run python -m backend.export_to_hugo",
        "```",
        "",
        "Re-extraction runbook: `config/latex_table_reextract_server.txt` in the repo.",
        "",
        f"**Last scan:** {scanned_at}",
        f"**Flagged papers:** {len(papers)}",
        "",
    ]

    if not papers:
        lines.extend(
            [
                "No scan data yet. Run the scan script above on a machine that has "
                "`papers/<id>/latex/expanded.tex` downloads, then re-export.",
                "",
            ]
        )
    else:
        lines.append("| ArXiv | Title | Issues | Explanation | Sample unparsed line |")
        lines.append("|-------|-------|--------|-------------|----------------------|")
        for entry in papers:
            arxiv_id = entry.get("arxiv_id") or "—"
            title = hugo._truncate_words(entry.get("title") or "—", 10)
            issues = entry.get("issues") or []
            kinds = ", ".join(sorted({str(item.get("kind") or "") for item in issues if item}))
            details = " ".join(
                hugo._truncate_words(str(item.get("detail") or ""), 18) for item in issues[:2]
            )
            sample = "—"
            for item in issues:
                samples = item.get("sample_lines") or []
                if samples:
                    sample = hugo._truncate_words(str(samples[0]), 12)
                    break
            paper_link = hugo._paper_site_link(arxiv_id, title) if arxiv_id != "—" else title
            lines.append(f"| {paper_link} | {title} | {kinds} | {details} | {sample} |")
        lines.append("")

    hugo._write_md(
        content_dev / "problematic-papers.md",
        {
            "title": "Problematic Papers",
            "type": "dev",
            "description": "LaTeX table-parser blind spots requiring re-extraction",
        },
        "\n".join(lines),
    )


def create_conferences_page(*, session: Session | None = None) -> int:
    """Generate the public conferences overview section."""
    from backend import export_to_hugo as hugo

    hugo._CONTENT.mkdir(parents=True, exist_ok=True)
    content_conferences = hugo._CONTENT / "conferences"
    content_conferences.mkdir(parents=True, exist_ok=True)

    stale = hugo._CONTENT / "dev" / "conferences.md"
    if stale.exists():
        stale.unlink()

    hugo._write_md(
        content_conferences / "_index.md",
        {
            "title": "Conferences",
            "description": "Venue coverage and publication trends for exported papers.",
        },
        "Conference venues represented in the exported paper set.",
    )
    return 1


def _create_dev_pages_impl(
    session: Session, hugo: Any, content_dev: Any, snapshot: DevExportSnapshot
) -> int:
    pages_written = 0
    primary_metric_results: list[Any] | None = None
    hugo._write_md(content_dev / "_index.md", {"title": "Development", "type": "dev"}, "")
    pages_written += 1

    papers = snapshot.papers
    by_status: dict[str, list[Paper]] = {}
    for paper in papers:
        by_status.setdefault(paper.extraction_status, []).append(paper)

    lines = [
        "## Paper Extraction Status",
        "",
        f"**Total:** {len(papers)} papers",
        "",
        "This page tracks the extraction pipeline status for all papers in the benchmarking dataset. "
        "Each paper goes through several stages: first it must be downloaded from arXiv, then the full text "
        "is extracted and parsed (either from HTML, LaTeX source, or PDF), and finally results are extracted "
        "using an LLM. The extraction model shown indicates which LLM (if any) was used to extract results.",
        "",
    ]
    for status in sorted(by_status.keys()):
        count = len(by_status[status])
        lines.append(f"### {status.capitalize()} ({count})")
        lines.append("")
        if status == "pending":
            lines.append("Papers that have been identified but not yet downloaded from arXiv.")
            lines.append("")
        elif status == "downloaded":
            lines.append("Papers that have been downloaded but not yet processed for extraction.")
            lines.append("")
        elif status == "extracted":
            lines.append(
                "Papers with successfully extracted results. These papers contribute to the leaderboards."
            )
            lines.append("")
        elif status == "failed":
            lines.append(
                "Papers where extraction failed. These may have parsing errors, missing datasets, or LLM errors."
            )
            lines.append("")

        if by_status[status]:
            lines.append("| ArXiv | Title | Model |")
            lines.append("|-------|-------|-------|")
            for paper in sorted(by_status[status], key=lambda item: item.arxiv_id):
                title = hugo._truncate_words(paper.title, 8)
                model = paper.extraction_model or "—"
                lines.append(f"| {paper.arxiv_id} | {title} | {model} |")
            lines.append("")

    hugo._write_md(
        content_dev / "paper-status.md",
        {
            "title": "Paper Extraction Status",
            "type": "dev",
            "description": "Overview of extraction status",
        },
        "\n".join(lines),
    )

    skipped_s1 = snapshot.stage1_skipped
    skipped_s2 = snapshot.stage2_skipped

    zero_dataset_candidates = []
    for candidate in skipped_s2:
        raw = candidate.stage2_datasets or ""
        ds_list: list[str] = []
        if raw:
            try:
                parsed = json.loads(raw)
                if isinstance(parsed, list):
                    ds_list = [str(item).strip() for item in parsed if str(item).strip()]
            except Exception:
                ds_list = []
        if not ds_list:
            zero_dataset_candidates.append(candidate)

    lines = [
        "## Skipped Papers",
        "",
        "This page shows papers that were identified but rejected by the LLM screening pipeline. "
        "The screening happens in two stages: Stage 1 filters for general relevance to graph neural network "
        "research, and Stage 2 checks whether the paper evaluates results on known benchmarks. Papers that pass "
        "both stages proceed to full result extraction.",
        "",
        f"### Stage 1 Rejections: {len(skipped_s1)}",
        "",
        "Stage 1 rejects papers that are deemed not relevant to graph neural networks. These are typically papers "
        "in unrelated fields that happened to mention GNNs or graph concepts, but don't focus on benchmarking graph neural network models.",
        "",
    ]
    if skipped_s1:
        lines.append("| ArXiv | Title | Reason |")
        lines.append("|-------|-------|--------|")
        for candidate in skipped_s1:
            reason = (candidate.stage1_reason or "—")[:80]
            title = hugo._truncate_words(candidate.title, 8)
            lines.append(f"| {candidate.arxiv_id or '—'} | {title} | {reason} |")
    lines.append("")
    lines.append(f"### Stage 2 Rejections: {len(skipped_s2)}")
    lines.append("")
    lines.append(
        "Stage 2 rejects papers that are relevant to GNNs but don't evaluate models on any known benchmarks. "
        "This includes position papers, theoretical papers, survey papers, or papers that only propose new "
        "datasets without evaluating existing models. The 'Datasets Found' column shows how many benchmark datasets "
        "the LLM detected in the paper (if any)."
    )
    lines.append("")
    if skipped_s2:
        lines.append("| ArXiv | Title | Datasets Found | Reason |")
        lines.append("|-------|-------|----------------|--------|")
        for candidate in skipped_s2:
            reason = (candidate.stage2_reason or "—")[:80]
            ds_count = 0
            raw = candidate.stage2_datasets or ""
            if raw:
                try:
                    parsed = json.loads(raw)
                    if isinstance(parsed, list):
                        ds_count = len([item for item in parsed if str(item).strip()])
                except Exception:
                    ds_count = 0
            title = hugo._truncate_words(candidate.title, 8)
            lines.append(f"| {candidate.arxiv_id or '—'} | {title} | {ds_count} | {reason} |")

    lines.append("")
    lines.append(f"### No Datasets/Results Discovered: {len(zero_dataset_candidates)}")
    lines.append("")
    lines.append(
        "These papers passed Stage 2 screening (were deemed relevant and benchmarking-focused) but the extraction "
        "pipeline was unable to discover any benchmark datasets or results. This could mean: the paper's results are "
        "too noisy for extraction, the datasets used have non-standard names, or the extraction model failed to parse "
        "the paper format. These papers may still be worth investigating manually."
    )
    lines.append("")
    if zero_dataset_candidates:
        lines.append("| ArXiv | Title | Stage 2 Reason |")
        lines.append("|-------|-------|----------------|")
        for candidate in zero_dataset_candidates:
            title = hugo._truncate_words(candidate.title, 10)
            reason = (candidate.stage2_reason or "—")[:96]
            lines.append(f"| {candidate.arxiv_id or '—'} | {title} | {reason} |")

    hugo._write_md(
        content_dev / "skipped-papers.md",
        {
            "title": "Skipped Papers",
            "type": "dev",
            "description": "Papers rejected by LLM screening",
        },
        "\n".join(lines),
    )

    pending_rows = session.query(PendingDataset).all()
    unresolved_entries: list[dict[str, Any]] = []
    covered_entries: list[dict[str, Any]] = []
    for row in pending_rows:
        review_status = str(row.status or "pending")
        payload = discovery_payload_dict(row)
        try:
            from backend.llm_types import DatasetInfo

            info = DatasetInfo.model_validate(payload)
        except (TypeError, ValueError):
            info = DatasetInfo(name=str(row.dataset_name or ""), metrics_seen=row.metrics_seen_list)
        resolution = classify_dataset_info(session, info)
        dataset = info.name
        paper = str(row.arxiv_id or "")
        metrics = ", ".join(info.metrics_seen or row.metrics_seen_list)
        if resolution.tracked:
            covered_entries.append(
                {
                    "status": review_status,
                    "dataset": dataset,
                    "paper": paper,
                    "metrics": metrics,
                    "resolved_dataset": resolution.dataset.name,
                    "resolved_variant": resolution.variant.name,
                }
            )
            continue
        unresolved_entries.append(
            {
                "status": review_status,
                "dataset": dataset,
                "paper": paper,
                "metrics": metrics,
                "description": info.description or "",
                "expected_model_count": info.expected_model_count or "",
                "task_type": info.task_type or "",
                "variant_hint": info.variant_hint or "",
                "statistics": ", ".join(
                    f"{label}={getattr(info, field_name)}"
                    for label, field_name in (
                        ("graphs", "num_graphs"),
                        ("avg nodes", "avg_nodes"),
                        ("avg edges", "avg_edges"),
                        ("classes", "num_classes"),
                    )
                    if getattr(info, field_name) is not None
                ),
                "resolution_status": resolution.status,
                "resolution_reason": resolution.reason,
            }
        )

    unresolved_entries.sort(
        key=lambda item: (
            0 if item["status"] == "pending" else 1,
            item["dataset"].lower(),
            item["paper"],
        )
    )
    covered_entries.sort(key=lambda item: (item["dataset"].lower(), item["paper"]))

    lines = [
        "## Datasets Still Missing From The DB",
        "",
        "This page distinguishes between entries that are truly unresolved and stale pending rows that already resolve against the current benchmark database.",
        "",
        "Source: pending_datasets table in benchmarks.db",
        "",
        f"**Tracked entries in DB:** {len(pending_rows)}",
        f"**Still unresolved:** {len(unresolved_entries)}",
        f"**Already covered now:** {len(covered_entries)}",
        "",
    ]
    if unresolved_entries:
        lines.append("### Still unresolved")
        lines.append("")
        lines.append(
            "| Status | Resolution | Dataset | Paper | Description | Models | Task | Metrics | Variant hint | Statistics | Reason |"
        )
        lines.append(
            "|--------|------------|---------|-------|-------------|--------|------|---------|--------------|------------|--------|"
        )
        for entry in unresolved_entries:
            lines.append(
                f"| {entry['status']} | {entry['resolution_status']} | {entry['dataset']} | {entry['paper']} | "
                f"{entry['description']} | {entry['expected_model_count']} | {entry['task_type']} | "
                f"{entry['metrics']} | {entry['variant_hint']} | {entry['statistics']} | {entry['resolution_reason']} |"
            )
    if covered_entries:
        lines.extend(
            [
                "",
                "### Already covered now",
                "",
                "These rows remain in pending_datasets, but they already resolve against the current DB and should not be treated as missing coverage.",
                "",
                "| Pending Name | Paper | Resolves To | Variant | Pending Status |",
                "|--------------|-------|-------------|---------|----------------|",
            ]
        )
        for entry in covered_entries:
            lines.append(
                f"| {entry['dataset']} | {entry['paper']} | {entry['resolved_dataset']} | {entry['resolved_variant']} | {entry['status']} |"
            )

    hugo._write_md(
        content_dev / "missing-datasets.md",
        {
            "title": "Missing Datasets",
            "type": "dev",
            "description": "Datasets detected in extraction but not yet mapped into DB",
        },
        "\n".join(lines),
    )

    try:
        with _dev_export_step("dev page: extraction-anomalies"):
            anomalies = hugo._collect_result_anomalies(session)
        by_paper = {item["arxiv_id"] for item in anomalies}
        lines = [
            "## Post-Extraction Anomalies",
            "",
            "This page flags suspicious stored results after overrides are applied.",
            "",
            "Checks currently included:",
            "",
            "- bounded metrics such as Accuracy/AP/AUC/F1/MRR/Hits@K must not exceed 1",
            "- values roughly 20x away from the dataset-metric median are flagged as likely scale issues",
            "",
            f"**Flagged papers:** {len(by_paper)}",
            f"**Flagged rows:** {len(anomalies)}",
            "",
        ]
        if anomalies:
            lines.append(
                "| ArXiv | Title | Dataset | Metric | Model | Value | Dataset Median | Reason |"
            )
            lines.append(
                "|-------|-------|---------|--------|-------|------:|---------------:|--------|"
            )
            for item in anomalies:
                median = "—" if item["median"] is None else f"{item['median']:.6g}"
                lines.append(
                    f"| {item['arxiv_id']} | {item['title'][:48]} | {item['dataset']} | {item['metric']} | {item['model']} | {item['value']:.6g} | {median} | {'; '.join(item['reasons'])} |"
                )

        hugo._write_md(
            content_dev / "extraction-anomalies.md",
            {
                "title": "Extraction Anomalies",
                "type": "dev",
                "description": "Post-extraction anomaly checks over stored results",
            },
            "\n".join(lines),
        )
    except Exception:
        logger.exception("Failed to create extraction-anomalies dev page")

    try:
        with _dev_export_step("dev page: problematic-papers"):
            _write_problematic_latex_papers_page(hugo, content_dev)
    except Exception:
        logger.exception("Failed to create problematic-papers dev page")

    try:
        with _dev_export_step("dev page: page-of-shame"):
            primary_metric_results = hugo._primary_metric_results(session)
            mismatches = hugo._collect_model_value_mismatches(
                session, results=primary_metric_results
            )
        by_paper: dict[str, dict[str, Any]] = {}
        shame_counts = {
            "worse_than_at_pub": 0,
            "surpassed_since_pub_only": 0,
            "at_pub_differs_from_today": 0,
            "at_pub_same_as_today": 0,
            "baseline_rows": 0,
        }
        today_timing_counts = {
            "already-known": 0,
            "published-later": 0,
            "same-paper": 0,
            "unknown": 0,
        }
        for item in mismatches:
            if item.get("is_baseline"):
                shame_counts["baseline_rows"] += 1
            if item.get("worse_than_at_pub"):
                shame_counts["worse_than_at_pub"] += 1
            elif item.get("surpassed_since_pub"):
                shame_counts["surpassed_since_pub_only"] += 1
            if item.get("at_pub_differs_from_today"):
                shame_counts["at_pub_differs_from_today"] += 1
            elif (item.get("at_pub_source_arxiv") or "").strip() and (
                item.get("at_pub_source_arxiv") or ""
            ).strip() == (item.get("source_arxiv_id") or "").strip():
                shame_counts["at_pub_same_as_today"] += 1
            today_timing_counts[item.get("source_timing") or "unknown"] += 1

            bucket = by_paper.setdefault(
                item["arxiv_id"],
                {
                    "title": item["title"],
                    "rows": 0,
                    "worst_rank_delta": 0,
                    "already_known_rows": 0,
                    "published_later_rows": 0,
                    "unknown_timing_rows": 0,
                    "worse_than_at_pub_rows": 0,
                    "surpassed_since_pub_rows": 0,
                    "at_pub_differs_rows": 0,
                    "datasets": set(),
                    "models": set(),
                },
            )
            bucket["rows"] += 1
            bucket["worst_rank_delta"] = max(
                bucket["worst_rank_delta"], abs(item.get("rank_delta") or 0)
            )
            bucket["datasets"].add(item["dataset"])
            bucket["models"].add(item["model"])
            if item.get("source_timing") == "already-known":
                bucket["already_known_rows"] += 1
            elif item.get("source_timing") == "published-later":
                bucket["published_later_rows"] += 1
            elif item.get("source_timing") == "unknown":
                bucket["unknown_timing_rows"] += 1
            if item.get("worse_than_at_pub"):
                bucket["worse_than_at_pub_rows"] += 1
            elif item.get("surpassed_since_pub"):
                bucket["surpassed_since_pub_rows"] += 1
            if item.get("at_pub_differs_from_today"):
                bucket["at_pub_differs_rows"] += 1

        by_dataset: dict[str, dict[str, Any]] = {}
        by_model: dict[str, dict[str, Any]] = {}
        for item in mismatches:
            dataset_bucket = by_dataset.setdefault(
                item["dataset"],
                {
                    "rows": 0,
                    "papers": set(),
                    "models": set(),
                    "worst_rank_delta": 0,
                    "already_known_rows": 0,
                    "worse_than_at_pub_rows": 0,
                    "surpassed_since_pub_rows": 0,
                },
            )
            dataset_bucket["rows"] += 1
            dataset_bucket["papers"].add(item["arxiv_id"])
            dataset_bucket["models"].add(item["model"])
            dataset_bucket["worst_rank_delta"] = max(
                dataset_bucket["worst_rank_delta"], abs(item.get("rank_delta") or 0)
            )
            if item.get("source_timing") == "already-known":
                dataset_bucket["already_known_rows"] += 1
            if item.get("worse_than_at_pub"):
                dataset_bucket["worse_than_at_pub_rows"] += 1
            elif item.get("surpassed_since_pub"):
                dataset_bucket["surpassed_since_pub_rows"] += 1

            model_bucket = by_model.setdefault(
                item["model"],
                {
                    "rows": 0,
                    "papers": set(),
                    "datasets": set(),
                    "worst_rank_delta": 0,
                    "already_known_rows": 0,
                    "worse_than_at_pub_rows": 0,
                    "surpassed_since_pub_rows": 0,
                },
            )
            model_bucket["rows"] += 1
            model_bucket["papers"].add(item["arxiv_id"])
            model_bucket["datasets"].add(item["dataset"])
            model_bucket["worst_rank_delta"] = max(
                model_bucket["worst_rank_delta"], abs(item.get("rank_delta") or 0)
            )
            if item.get("source_timing") == "already-known":
                model_bucket["already_known_rows"] += 1
            if item.get("worse_than_at_pub"):
                model_bucket["worse_than_at_pub_rows"] += 1
            elif item.get("surpassed_since_pub"):
                model_bucket["surpassed_since_pub_rows"] += 1

        paper_rows = sorted(
            [
                {
                    "arxiv_id": arxiv_id,
                    "title": info["title"],
                    "rows": info["rows"],
                    "worst_rank_delta": info["worst_rank_delta"],
                    "already_known_rows": info["already_known_rows"],
                    "published_later_rows": info["published_later_rows"],
                    "unknown_timing_rows": info["unknown_timing_rows"],
                    "worse_than_at_pub_rows": info["worse_than_at_pub_rows"],
                    "surpassed_since_pub_rows": info["surpassed_since_pub_rows"],
                    "at_pub_differs_rows": info["at_pub_differs_rows"],
                    "datasets": sorted(info["datasets"]),
                    "models": sorted(info["models"]),
                }
                for arxiv_id, info in by_paper.items()
            ],
            key=lambda item: (-item["rows"], -item["worst_rank_delta"], item["arxiv_id"]),
        )

        dataset_rows = sorted(
            [
                {
                    "dataset": name,
                    "rows": info["rows"],
                    "paper_count": len(info["papers"]),
                    "model_count": len(info["models"]),
                    "worst_rank_delta": info["worst_rank_delta"],
                    "already_known_rows": info["already_known_rows"],
                    "worse_than_at_pub_rows": info["worse_than_at_pub_rows"],
                    "surpassed_since_pub_rows": info["surpassed_since_pub_rows"],
                }
                for name, info in by_dataset.items()
            ],
            key=lambda item: (-item["rows"], -item["worst_rank_delta"], item["dataset"]),
        )
        model_rows = sorted(
            [
                {
                    "model": name,
                    "rows": info["rows"],
                    "paper_count": len(info["papers"]),
                    "dataset_count": len(info["datasets"]),
                    "worst_rank_delta": info["worst_rank_delta"],
                    "already_known_rows": info["already_known_rows"],
                    "worse_than_at_pub_rows": info["worse_than_at_pub_rows"],
                    "surpassed_since_pub_rows": info["surpassed_since_pub_rows"],
                }
                for name, info in by_model.items()
            ],
            key=lambda item: (-item["rows"], -item["worst_rank_delta"], item["model"]),
        )

        def _shame_source_link(arxiv_id: str, title: str, word_limit: int = 8) -> str:
            if arxiv_id:
                return hugo._paper_site_link(arxiv_id, hugo._truncate_words(title, word_limit))
            return hugo._truncate_words(title, word_limit) if title else "—"

        lines = [
            "## Page of Shame: Papers Using Wrong Model Values",
            "",
            "This page lists papers whose reported primary-metric value for a model disagrees with "
            "**best reported** performance (today's global best on the leaderboard) by more than the reported "
            "std, or differs at all when no std is given.",
            "",
            "Each row also compares against the **best known at publication** (best result for that "
            "model on or before the viewing paper's publish date). That split matches the paper pages:",
            "",
            "- **Best at pub** — reported value was already worse than the best known when "
            "the paper came out (fair criticism; red on paper pages).",
            "- **Best today** (surpassed since publication only) — OK vs the at-publication best, but "
            "today's leaderboard best is better (orange on paper pages).",
            "- **Best reported performance** — current leaderboard best (used for rank and the green value).",
            "",
            "### Summary",
            "",
            "| Statistic | Count |",
            "|---|---:|",
            f"| Flagged papers | {len(paper_rows)} |",
            f"| Flagged rows | {len(mismatches)} |",
            f"| Baseline rows | {shame_counts['baseline_rows']} |",
            f"| Best at pub | {shame_counts['worse_than_at_pub']} |",
            f"| Best today only (not best at pub) | {shame_counts['surpassed_since_pub_only']} |",
            f"| At-pub best ≠ today's best (different source papers) | {shame_counts['at_pub_differs_from_today']} |",
            f"| At-pub best = today's best (same source paper) | {shame_counts['at_pub_same_as_today']} |",
            "",
            "### Today's best source timing",
            "",
            "When the **best reported** holder published relative to the viewing paper:",
            "",
            "| Timing | Rows |",
            "|---|---:|",
            f"| Already known at publication | {today_timing_counts['already-known']} |",
            f"| Published later (field moved on) | {today_timing_counts['published-later']} |",
            f"| Same paper | {today_timing_counts['same-paper']} |",
            f"| Unknown date | {today_timing_counts['unknown']} |",
            "",
        ]
        if dataset_rows:
            lines.extend(
                [
                    "### Most affected datasets",
                    "",
                    "| Dataset | Wrong Rows | Best at pub | Best today only | Papers | Models | Worst Rank Δ |",
                    "|---|---:|---:|---:|---:|---:|---:|",
                ]
            )
            for item in dataset_rows[:25]:
                lines.append(
                    f"| {item['dataset']} | {item['rows']} | {item['worse_than_at_pub_rows']} | {item['surpassed_since_pub_rows']} | {item['paper_count']} | {item['model_count']} | {item['worst_rank_delta']} |"
                )
            lines.append("")
        if model_rows:
            lines.extend(
                [
                    "### Most affected models",
                    "",
                    "| Model | Wrong Rows | Best at pub | Best today only | Papers | Datasets | Worst Rank Δ |",
                    "|---|---:|---:|---:|---:|---:|---:|",
                ]
            )
            for item in model_rows[:25]:
                lines.append(
                    f"| {item['model']} | {item['rows']} | {item['worse_than_at_pub_rows']} | {item['surpassed_since_pub_rows']} | {item['paper_count']} | {item['dataset_count']} | {item['worst_rank_delta']} |"
                )
            lines.append("")
        if paper_rows:
            lines.append(
                "| ArXiv | Title | Wrong Rows | Best at pub | Best today only | Diff sources | Worst Rank Δ | Datasets | Models |"
            )
            lines.append("|---|---|---:|---:|---:|---:|---:|---|---|")
            for item in paper_rows:
                lines.append(
                    f"| {hugo._paper_site_link(item['arxiv_id'])} | {hugo._paper_site_link(item['arxiv_id'], hugo._truncate_words(item['title'], 10))} | {item['rows']} | {item['worse_than_at_pub_rows']} | {item['surpassed_since_pub_rows']} | {item['at_pub_differs_rows']} | {item['worst_rank_delta']} | {', '.join(item['datasets'][:4])} | {', '.join(item['models'][:4])} |"
                )

        lines.extend(["", "### Flagged Rows", ""])
        if mismatches:
            lines.append(
                "| ArXiv | Dataset | Model | True perf | At-pub best | Paper | Best at pub | Best today only | At-pub source | Best today source | Rank Δ |"
            )
            lines.append("|---|---|---|---:|---:|---:|---|---|---|---:|")
            for item in mismatches[:500]:
                at_pub_val = item.get("at_pub_value")
                at_pub_cell = f"{at_pub_val:.4f}" if at_pub_val is not None else "—"
                behind_label = "yes" if item.get("worse_than_at_pub") else "no"
                surpassed_label = (
                    "yes"
                    if item.get("surpassed_since_pub") and not item.get("worse_than_at_pub")
                    else "no"
                )
                at_pub_link = _shame_source_link(
                    item.get("at_pub_source_arxiv", ""),
                    item.get("at_pub_source_title", ""),
                )
                today_link = _shame_source_link(
                    item.get("source_arxiv_id", ""),
                    item.get("source_title", ""),
                )
                if item.get("at_pub_differs_from_today"):
                    today_link = f"{today_link} *"
                lines.append(
                    f"| {hugo._paper_site_link(item['arxiv_id'])} | {item['dataset']} | {item['model']} | {item['true_value']:.4f} | {at_pub_cell} | {item['paper_value']:.4f} | {behind_label} | {surpassed_label} | {at_pub_link} | {today_link} | {abs(item.get('rank_delta') or 0)} |"
                )
            if any(item.get("at_pub_differs_from_today") for item in mismatches[:500]):
                lines.append("")
                lines.append(
                    "*Today's best source differs from the at-publication best for that model."
                )

        hugo._write_md(
            content_dev / "page-of-shame.md",
            {
                "title": "Page of Shame",
                "type": "dev",
                "description": "Papers whose reported model values disagree with best reported performance (today) and at-publication bests",
            },
            "\n".join(lines),
        )
    except Exception:
        logger.exception("Failed to create page-of-shame dev page")

    try:
        core_missing, mlp_missing = hugo._collect_missing_baselines(session)
        lines = [
            "## Baseline Coverage Gaps",
            "",
            "Datasets in this report are missing one of the baseline families we usually want on the leaderboard for context.",
            "",
            f"### No GCN/GIN/GraphSAGE Baseline ({len(core_missing)})",
            "",
        ]
        if core_missing:
            lines.append("| Benchmark | Dataset | Task | Metric | Results | Present Families |")
            lines.append("|-----------|---------|------|--------|--------:|------------------|")
            for item in core_missing:
                lines.append(
                    f"| {item['benchmark']} | {item['dataset']} | {item['task_type']} | {item['primary_metric']} | {item['result_count']} | {item['present_families']} |"
                )
        lines.append("")
        lines.append(f"### No MLP Baseline ({len(mlp_missing)})")
        lines.append("")
        if mlp_missing:
            lines.append("| Benchmark | Dataset | Task | Metric | Results | Present Families |")
            lines.append("|-----------|---------|------|--------|--------:|------------------|")
            for item in mlp_missing:
                lines.append(
                    f"| {item['benchmark']} | {item['dataset']} | {item['task_type']} | {item['primary_metric']} | {item['result_count']} | {item['present_families']} |"
                )

        hugo._write_md(
            content_dev / "baseline-coverage.md",
            {
                "title": "Baseline Coverage Gaps",
                "type": "dev",
                "description": "Datasets missing common GNN or MLP baseline families",
            },
            "\n".join(lines),
        )
    except Exception:
        logger.exception("Failed to create baseline-coverage dev page")

    try:
        with _dev_export_step("dev page: baseline-improvements"):
            if primary_metric_results is None:
                primary_metric_results = hugo._primary_metric_results(session)
            improvements = hugo._collect_at_pub_improvements(
                session, results=primary_metric_results
            )

        def _improvement_source_link(arxiv_id: str, title: str, word_limit: int = 8) -> str:
            if not arxiv_id:
                return title[:48] if title else "—"
            label = hugo._truncate_words(title, word_limit) if title else arxiv_id
            return hugo._paper_site_link(arxiv_id, label)

        sig_count = sum(1 for item in improvements if item.get("significant"))
        insig_count = sum(1 for item in improvements if item.get("insignificant"))
        surpassed_count = sum(1 for item in improvements if item.get("later_surpassed"))

        lines = [
            "## At-Publication Improvements",
            "",
            "Papers that reported a result better than the best known for that model and dataset "
            "when they were published (baseline and proposed rows).",
            "",
            f"**Total rows:** {len(improvements)}",
            f"**Significant:** {sig_count}",
            f"**Within uncertainty (not highlighted on paper pages):** {insig_count}",
            f"**Later surpassed by another paper:** {surpassed_count}",
            "",
        ]
        if improvements:
            lines.extend(
                [
                    "| Paper | Type | Dataset | Model | Δ at pub | Significant | Later surpassed | "
                    "Prior best | Prior year | Prior conf. | Paper year | Paper conf. |",
                    "|-------|------|---------|-------|--------:|:-----------:|:---------------:|"
                    "-----------|----------:|------------|----------:|------------|",
                ]
            )
            for item in improvements[:500]:
                row_type = "baseline" if item.get("is_baseline") else "proposed"
                sig_label = "yes" if item.get("significant") else "no"
                surpassed_label = "yes" if item.get("later_surpassed") else "no"
                prior_link = _improvement_source_link(
                    item.get("at_pub_source_arxiv", ""),
                    item.get("at_pub_source_title", ""),
                )
                lines.append(
                    f"| {hugo._paper_site_link(item['arxiv_id'])} | {row_type} | {item['dataset']} | "
                    f"{item['model']} | {item['gap_vs_at_pub']:.4f} | {sig_label} | {surpassed_label} | "
                    f"{prior_link} | {item.get('at_pub_year') or '—'} | "
                    f"{item.get('at_pub_conference') or '—'} | {item.get('paper_year') or '—'} | "
                    f"{item.get('paper_conference') or '—'} |"
                )

        hugo._write_md(
            content_dev / "baseline-improvements.md",
            {
                "title": "Baseline Improvements",
                "type": "dev",
                "description": (
                    "Papers whose reported results improved over the prior at-publication best "
                    "(includes baseline and proposed methods)"
                ),
            },
            "\n".join(lines),
        )
    except Exception:
        logger.exception("Failed to create baseline-improvements dev page")

    try:
        todo_rows = snapshot.todo_rows
        lines = ["## Todo Papers (priority queue)", ""]
        lines.append(f"**Total:** {len(todo_rows)} entries")
        lines.append("")
        lines.append("| arXiv | imp | seen_count | status | title |")
        lines.append("|---|---:|---:|---|---")
        for row in todo_rows[:TODO_EXPORT_LIMIT]:
            title = sanitize_title(row.title)
            imp = "yes" if row.is_manually_important else ""
            lines.append(
                f"| {row.arxiv_id or ''} | {imp} | {int(row.seen_count or 0)} | {row.status or ''} | {title} |"
            )

        try:
            import sqlite3 as _sqlite3

            db_path = cfg.data_dir / "benchmarks.db"
            if db_path.exists():
                conn = _sqlite3.connect(str(db_path))
                cur = conn.cursor()
                cur.execute(
                    "SELECT name FROM sqlite_master WHERE type='table' AND name='s2_crawl_state'"
                )
                if cur.fetchone():
                    cur.execute("SELECT COUNT(*) FROM s2_crawl_state")
                    crawled_count = int((cur.fetchone() or [0])[0] or 0)
                    cur.execute("SELECT COUNT(*) FROM papers WHERE arxiv_id IS NOT NULL")
                    total_db_papers = int((cur.fetchone() or [0])[0] or 0)
                    cur.execute(
                        "SELECT COUNT(*) FROM s2_crawl_state WHERE citations_capped = 1 OR references_capped = 1"
                    )
                    capped_count = int((cur.fetchone() or [0])[0] or 0)
                    conn.close()
                    lines.extend(
                        [
                            "",
                            "### Semantic Scholar crawl summary",
                            "",
                            "The standalone S2 crawl page was removed to keep the development surface smaller. These counts retain the only high-signal summary from that page.",
                            "",
                            f"**DB papers total:** {total_db_papers}",
                            f"**Crawled:** {crawled_count}",
                            f"**Uncrawled:** {max(total_db_papers - crawled_count, 0)}",
                            f"**Hit crawl limits:** {capped_count}",
                        ]
                    )
        except Exception:
            logger.exception("Failed to add crawl summary to todo page")

        hugo._write_md(
            content_dev / "todo.md", {"title": "Todo Papers", "type": "dev"}, "\n".join(lines)
        )
    except Exception:
        logger.exception("Failed to create dev todo page")

    try:
        with _dev_export_step("dev page: statistics-sources"):
            _export_statistics_sources_page(session, hugo, content_dev)
    except Exception:
        logger.exception("Failed to create statistics-sources dev page")

    try:
        with _dev_export_step("dev page: sota-claims"):
            _export_sota_claims_page(session, hugo, content_dev)
    except Exception:
        logger.exception("Failed to create sota-claims dev page")

    return len(list(content_dev.glob("*.md")))


def _format_stats_cell(
    num_graphs: int | None,
    avg_nodes: float | None,
    avg_edges: float | None,
    num_classes: int | None,
    extra_stats: dict | None,
    raw_values: dict | None,
) -> str:
    return format_stats_summary(
        num_graphs=num_graphs,
        avg_nodes=avg_nodes,
        avg_edges=avg_edges,
        num_classes=num_classes,
        extra_stats=extra_stats if isinstance(extra_stats, dict) else None,
        raw_values=raw_values if isinstance(raw_values, dict) else None,
        separator="; ",
    )


def _export_statistics_sources_page(session: Session, hugo: Any, content_dev: Any) -> None:
    datasets = session.query(Dataset).order_by(Dataset.name).all()
    observations = (
        session.query(PaperDatasetStatistics)
        .options(joinedload(PaperDatasetStatistics.paper))
        .all()
    )
    obs_by_dataset: dict[int, list[PaperDatasetStatistics]] = {}
    for obs in observations:
        obs_by_dataset.setdefault(obs.dataset_id, []).append(obs)

    lines = [
        "## Statistics Sources & Discrepancies",
        "",
        "Canonical dataset statistics from the database (seeded from `config/seed_data.yaml`) "
        "compared with structural statistics reported in papers.",
        "",
    ]

    mismatch_total = sum(1 for obs in observations if obs.match_status == "mismatch")
    lines.append(f"**Datasets with observations:** {len(obs_by_dataset)}")
    lines.append(f"**Total paper observations:** {len(observations)}")
    lines.append(f"**Mismatched observations:** {mismatch_total}")
    lines.append("")

    for ds in datasets:
        ds_obs = obs_by_dataset.get(ds.id, [])
        if not ds_obs:
            continue

        extra_canonical: dict = {}
        if ds.extra_stats:
            try:
                extra_canonical = json.loads(ds.extra_stats)
            except (json.JSONDecodeError, TypeError):
                extra_canonical = {}

        lines.extend(
            [
                f"### {ds.name}",
                "",
                "**Canonical (DB / seed_data.yaml):** "
                + _format_stats_cell(
                    ds.num_graphs,
                    ds.avg_nodes,
                    ds.avg_edges,
                    ds.num_classes,
                    extra_canonical if isinstance(extra_canonical, dict) else None,
                    None,
                ),
                "",
                "| Paper | Year | Conference | Reported stats | Match |",
                "|-------|------|------------|----------------|-------|",
            ]
        )

        for obs in sorted(ds_obs, key=lambda row: row.paper.title if row.paper else ""):
            paper = obs.paper
            title = sanitize_title(paper.title if paper else "Unknown")
            year = hugo._publication_year(paper.published_date if paper else None) or "—"
            conf = hugo._conference_export_fields(
                paper.venue if paper else None,
                paper.published_date if paper else None,
            )
            conference = conf.get("published_conference") or "—"

            extra_obs: dict = {}
            if obs.extra_stats:
                try:
                    extra_obs = json.loads(obs.extra_stats)
                except (json.JSONDecodeError, TypeError):
                    extra_obs = {}
            raw_values: dict = {}
            if obs.raw_values:
                try:
                    raw_values = json.loads(obs.raw_values)
                except (json.JSONDecodeError, TypeError):
                    raw_values = {}

            reported = _format_stats_cell(
                obs.num_graphs,
                obs.avg_nodes,
                obs.avg_edges,
                obs.num_classes,
                extra_obs if isinstance(extra_obs, dict) else None,
                raw_values if isinstance(raw_values, dict) else None,
            )
            match_label = obs.match_status or "pending"
            if obs.match_status == "mismatch" and obs.mismatch_fields:
                try:
                    fields = json.loads(obs.mismatch_fields)
                    if isinstance(fields, list) and fields:
                        match_label = f"mismatch ({', '.join(fields)})"
                except (json.JSONDecodeError, TypeError):
                    pass

            arxiv_id = paper.arxiv_id if paper else ""
            paper_link = hugo._paper_site_link(arxiv_id) if arxiv_id else title
            lines.append(f"| {paper_link} | {year} | {conference} | {reported} | {match_label} |")
        lines.append("")

    hugo._write_md(
        content_dev / "statistics-sources.md",
        {
            "title": "Statistics Sources & Discrepancies",
            "type": "dev",
            "description": "Canonical dataset stats vs paper-reported statistics",
        },
        "\n".join(lines),
    )


def _format_restrictions(raw: str | None) -> str:
    if not raw:
        return "—"
    try:
        items = json.loads(raw)
    except (json.JSONDecodeError, TypeError):
        return "—"
    if not isinstance(items, list) or not items:
        return "—"
    parts: list[str] = []
    for item in items:
        if isinstance(item, dict):
            desc = str(item.get("description") or "").strip()
            kind = str(item.get("type") or "").strip()
            if desc and kind:
                parts.append(f"{kind}: {desc}")
            elif desc:
                parts.append(desc)
        elif item:
            parts.append(str(item))
    return "; ".join(parts) if parts else "—"


def _format_json_name_list(raw: str | None) -> str:
    if not raw:
        return "—"
    try:
        items = json.loads(raw)
    except (json.JSONDecodeError, TypeError):
        return "—"
    if not isinstance(items, list) or not items:
        return "—"
    return ", ".join(str(item) for item in items)


def _export_sota_claims_page(session: Session, hugo: Any, content_dev: Any) -> None:
    claims = (
        session.query(PaperSotaClaim)
        .options(joinedload(PaperSotaClaim.paper))
        .order_by(PaperSotaClaim.paper_id, PaperSotaClaim.id)
        .all()
    )
    verifications = verify_unrestricted_claims(session)

    unrestricted_total = sum(1 for claim in claims if is_unrestricted_claim(claim))
    restricted_total = sum(1 for claim in claims if (claim.scope or "") == "restricted")

    lines = [
        "## SOTA Claims",
        "",
        "State-of-the-art performance claims extracted from pre-appendix paper prose "
        "(not tables or appendix). Section B audits unrestricted claims against "
        "at-publication leaderboard data.",
        "",
        f"**Total claims:** {len(claims)}",
        f"**Unrestricted:** {unrestricted_total}",
        f"**Restricted:** {restricted_total}",
        "",
        "### All extracted claims",
        "",
        "| Paper | Year | Raw quote | Summary | Datasets | Scope | Restrictions | Source | Confidence |",
        "|-------|------|-----------|---------|----------|-------|--------------|--------|------------|",
    ]

    for claim in claims:
        paper = claim.paper
        title = hugo._truncate_words(paper.title if paper else "Unknown", 8)
        arxiv_id = paper.arxiv_id if paper else ""
        paper_link = hugo._paper_site_link(arxiv_id, title) if arxiv_id else title
        year = hugo._publication_year(paper.published_date if paper else None) or "—"
        quote = hugo._truncate_words(claim.raw_sentence, 20)
        summary = hugo._truncate_words(claim.claim_summary or "—", 12)
        datasets = _format_json_name_list(claim.datasets)
        scope = claim.scope or "unclear"
        restrictions = _format_restrictions(claim.restrictions)
        source_ref = claim.source_ref or "—"
        confidence = claim.confidence or "—"
        lines.append(
            f"| {paper_link} | {year} | {quote} | {summary} | {datasets} | {scope} | "
            f"{restrictions} | {source_ref} | {confidence} |"
        )

    lines.extend(
        [
            "",
            "### Unrestricted claim audit",
            "",
            "Claims with `scope=unrestricted` and no listed restrictions, compared to the "
            "best known result on each dataset at the paper's publication date.",
            "",
            "| Paper | Claim | Dataset | Paper result | Best at pub | Prior best paper | Gap | Verdict |",
            "|-------|-------|---------|--------------|-------------|------------------|-----|---------|",
        ]
    )

    for row in verifications:
        title = hugo._truncate_words(row.paper_title, 8)
        paper_link = hugo._paper_site_link(row.arxiv_id, title)
        claim_text = hugo._truncate_words(row.raw_sentence, 16)
        paper_result = f"{row.paper_value:.4f}" if row.paper_value is not None else "—"
        if row.paper_std is not None and row.paper_value is not None:
            paper_result = f"{row.paper_value:.4f} ± {row.paper_std:.4f}"
        prior_result = f"{row.prior_best_value:.4f}" if row.prior_best_value is not None else "—"
        if row.prior_best_std is not None and row.prior_best_value is not None:
            prior_result = f"{row.prior_best_value:.4f} ± {row.prior_best_std:.4f}"
        prior_paper = "—"
        if row.prior_best_arxiv:
            prior_paper = hugo._paper_site_link(
                row.prior_best_arxiv,
                hugo._truncate_words(row.prior_best_title or row.prior_best_arxiv, 8),
            )
        gap = f"{row.gap:.4f}" if row.gap is not None else "—"
        verdict = row.verdict
        if row.details:
            verdict = f"{verdict} ({row.details})"
        lines.append(
            f"| {paper_link} | {claim_text} | {row.dataset_name} | {paper_result} | "
            f"{prior_result} | {prior_paper} | {gap} | {verdict} |"
        )

    hugo._write_md(
        content_dev / "sota-claims.md",
        {
            "title": "SOTA Claims",
            "type": "dev",
            "description": "Extracted SOTA claims and unrestricted claim audit",
        },
        "\n".join(lines),
    )
