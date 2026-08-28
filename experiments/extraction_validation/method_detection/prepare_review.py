#!/usr/bin/env python3
"""Prepare a manual method-detection review for the dataset-review paper cohort."""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import shutil
import sqlite3
from dataclasses import dataclass, field
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parents[3]
_EXPECTED_PAPER_COUNT = 20
_FIELDNAMES = [
    "review_row_id",
    "paper_index",
    "arxiv_id",
    "cohort",
    "title",
    "pdf_path",
    "row_type",
    "database_method_count",
    "database_method",
    "database_raw_names",
    "database_datasets",
    "database_table_refs",
    "database_dataset_table_pairs",
    "database_result_count",
    "database_role",
    "database_problematic_result_count",
    "manual_decision",
    "manual_corrected_or_canonical_name",
    "manual_missing_methods",
    "manual_missing_method_evidence",
    "manual_notes",
    "review_complete",
]


@dataclass(frozen=True)
class ReviewPaper:
    """One paper retained from the dataset-detection review."""

    index: int
    arxiv_id: str
    cohort: str
    title: str
    source_pdf: Path

    @property
    def pdf_filename(self) -> str:
        return f"{self.arxiv_id.replace('/', '_')}.pdf"

    @property
    def review_pdf_path(self) -> str:
        return f"pdfs/{self.cohort}/{self.pdf_filename}"


@dataclass
class _MethodAccumulator:
    """Mutable database evidence collected for one effective method name."""

    name: str
    raw_names: set[str] = field(default_factory=set)
    datasets: set[str] = field(default_factory=set)
    table_refs: set[str] = field(default_factory=set)
    dataset_table_pairs: set[str] = field(default_factory=set)
    result_count: int = 0
    baseline_count: int = 0
    problematic_count: int = 0


@dataclass(frozen=True)
class MethodEvidence:
    """Review-facing evidence for one database-detected method."""

    name: str
    raw_names: tuple[str, ...]
    datasets: tuple[str, ...]
    table_refs: tuple[str, ...]
    dataset_table_pairs: tuple[str, ...]
    result_count: int
    role: str
    problematic_count: int


def _natural_key(value: str) -> tuple[tuple[int, str | int], ...]:
    return tuple(
        (1, int(part)) if part.isdigit() else (0, part)
        for part in re.split(r"(\d+)", value.casefold())
        if part
    )


def _method_key(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip().casefold()


def _method_row_id(arxiv_id: str, method: str) -> str:
    digest = hashlib.sha256(_method_key(method).encode()).hexdigest()[:12]
    return f"{arxiv_id}:method:{digest}"


def _method_role(result_count: int, baseline_count: int) -> str:
    if baseline_count == result_count:
        return "baseline"
    if baseline_count == 0:
        return "non-baseline"
    return "mixed"


def load_papers(cohort_csv: Path, papers_dir: Path) -> list[ReviewPaper]:
    """Load the exact ordered paper set from the completed dataset review."""
    with cohort_csv.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    papers: list[ReviewPaper] = []
    seen: set[str] = set()
    for row in rows:
        arxiv_id = str(row.get("arxiv_id") or "").strip()
        if not arxiv_id or arxiv_id in seen:
            continue
        seen.add(arxiv_id)
        source_pdf = cohort_csv.parent / str(row.get("pdf_path") or "")
        if not source_pdf.is_file():
            source_pdf = papers_dir / arxiv_id / "paper.pdf"
        if not source_pdf.is_file() or source_pdf.stat().st_size == 0:
            raise FileNotFoundError(f"Missing PDF for {arxiv_id}: {source_pdf}")
        papers.append(
            ReviewPaper(
                index=int(row["paper_index"]),
                arxiv_id=arxiv_id,
                cohort=str(row["cohort"]),
                title=" ".join(str(row["title"]).split()),
                source_pdf=source_pdf,
            )
        )

    if len(papers) != _EXPECTED_PAPER_COUNT:
        raise ValueError(
            f"Expected {_EXPECTED_PAPER_COUNT} unique source papers, found {len(papers)}"
        )
    return sorted(papers, key=lambda paper: paper.index)


def load_method_evidence(
    database: Path, paper_ids: list[str]
) -> tuple[dict[str, list[MethodEvidence]], dict[str, int]]:
    """Load distinct effective methods and their result evidence from the database."""
    placeholders = ",".join("?" for _ in paper_ids)
    connection = sqlite3.connect(f"file:{database}?mode=ro", uri=True)
    connection.row_factory = sqlite3.Row
    try:
        rows = connection.execute(
            f"""
            SELECT p.arxiv_id,
                   COALESCE(NULLIF(TRIM(r.model_name_override), ''), m.canonical_name) AS method,
                   m.name AS raw_method,
                   d.name AS dataset,
                   r.table_ref,
                   r.is_baseline,
                   r.is_problematic
            FROM papers AS p
            JOIN results AS r ON r.paper_id = p.id
            JOIN models AS m ON m.id = r.model_id
            JOIN dataset_variants AS dv ON dv.id = r.dataset_variant_id
            JOIN datasets AS d ON d.id = dv.dataset_id
            WHERE p.arxiv_id IN ({placeholders})
            ORDER BY p.arxiv_id, method, d.name, r.table_ref
            """,
            paper_ids,
        ).fetchall()
    finally:
        connection.close()

    accumulators: dict[str, dict[str, _MethodAccumulator]] = {
        paper_id: {} for paper_id in paper_ids
    }
    result_counts: dict[str, int] = dict.fromkeys(paper_ids, 0)
    for row in rows:
        paper_id = str(row["arxiv_id"])
        method = str(row["method"] or "").strip() or str(row["raw_method"] or "").strip()
        key = _method_key(method)
        item = accumulators[paper_id].setdefault(key, _MethodAccumulator(name=method))
        raw_name = str(row["raw_method"] or "").strip()
        dataset = str(row["dataset"] or "").strip()
        table_ref = str(row["table_ref"] or "").strip()
        if raw_name:
            item.raw_names.add(raw_name)
        if dataset:
            item.datasets.add(dataset)
        if table_ref:
            item.table_refs.add(table_ref)
        if dataset:
            item.dataset_table_pairs.add(
                f"{dataset} @ {table_ref}" if table_ref else f"{dataset} @ table unspecified"
            )
        item.result_count += 1
        item.baseline_count += int(bool(row["is_baseline"]))
        item.problematic_count += int(bool(row["is_problematic"]))
        result_counts[paper_id] += 1

    evidence: dict[str, list[MethodEvidence]] = {}
    for paper_id, methods in accumulators.items():
        evidence[paper_id] = sorted(
            (
                MethodEvidence(
                    name=item.name,
                    raw_names=tuple(sorted(item.raw_names, key=_natural_key)),
                    datasets=tuple(sorted(item.datasets, key=_natural_key)),
                    table_refs=tuple(sorted(item.table_refs, key=_natural_key)),
                    dataset_table_pairs=tuple(sorted(item.dataset_table_pairs, key=_natural_key)),
                    result_count=item.result_count,
                    role=_method_role(item.result_count, item.baseline_count),
                    problematic_count=item.problematic_count,
                )
                for item in methods.values()
            ),
            key=lambda item: _natural_key(item.name),
        )
    return evidence, result_counts


def build_review_rows(
    papers: list[ReviewPaper],
    evidence: dict[str, list[MethodEvidence]],
    result_counts: dict[str, int],
) -> list[dict[str, str]]:
    """Build one summary row per paper and one decision row per detected method."""
    rows: list[dict[str, str]] = []
    for paper in papers:
        methods = sorted(evidence.get(paper.arxiv_id, []), key=lambda item: _natural_key(item.name))
        common = {
            "paper_index": str(paper.index),
            "arxiv_id": paper.arxiv_id,
            "cohort": paper.cohort,
            "title": paper.title,
            "pdf_path": paper.review_pdf_path,
            "database_method_count": str(len(methods)),
        }
        rows.append(
            {
                **common,
                "review_row_id": f"{paper.arxiv_id}:summary",
                "row_type": "paper_summary",
                "database_result_count": str(result_counts.get(paper.arxiv_id, 0)),
                "manual_missing_methods": "",
                "manual_missing_method_evidence": "",
                "manual_notes": "",
                "review_complete": "",
            }
        )
        for method in methods:
            rows.append(
                {
                    **common,
                    "review_row_id": _method_row_id(paper.arxiv_id, method.name),
                    "row_type": "database_method",
                    "database_method": method.name,
                    "database_raw_names": "; ".join(method.raw_names),
                    "database_datasets": "; ".join(method.datasets),
                    "database_table_refs": "; ".join(method.table_refs),
                    "database_dataset_table_pairs": "; ".join(method.dataset_table_pairs),
                    "database_result_count": str(method.result_count),
                    "database_role": method.role,
                    "database_problematic_result_count": str(method.problematic_count),
                    "manual_decision": "",
                    "manual_corrected_or_canonical_name": "",
                    "manual_notes": "",
                }
            )
    return [{field: row.get(field, "") for field in _FIELDNAMES} for row in rows]


def write_review_csv(path: Path, rows: list[dict[str, str]]) -> None:
    """Create the annotation sheet once so reruns cannot erase manual decisions."""
    if path.exists():
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=_FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)


def render_review_markdown(
    papers: list[ReviewPaper],
    evidence: dict[str, list[MethodEvidence]],
    result_counts: dict[str, int],
) -> str:
    """Render the paper-by-paper review checklist."""
    lines = [
        "# Method-detection manual review",
        "",
        "This review reuses the exact 20-paper dataset-detection cohort. Verify methods that have "
        "quantitative results on tracked, compatible datasets; include both proposed methods and baselines.",
        "",
        "## Fast annotation protocol",
        "",
        "1. Open the linked PDF and the matching rows in `review_cohort.csv`.",
        "2. For every `database_method` row, set `manual_decision` to `correct`, `alias`, "
        "`not_a_method`, `not_in_results`, or `unclear`.",
        "3. For `alias`, fill `manual_corrected_or_canonical_name`; use `manual_notes` for brief evidence.",
        "4. On the paper's `paper_summary` row, list every omitted method in "
        "`manual_missing_methods`, separated by semicolons. Enter `NONE` when no method is missing.",
        "5. Put dataset/table evidence for omissions in `manual_missing_method_evidence`, then set "
        "`review_complete` to `yes`.",
        "",
        "Database evidence below is provided only to make row checking fast; the PDF remains the "
        "manual reference. Method aliases should count as the same method after recording the canonical name.",
        "",
        "## Papers",
        "",
    ]
    for paper in papers:
        methods = evidence.get(paper.arxiv_id, [])
        lines.extend(
            [
                f"### {paper.index}. {paper.title}",
                "",
                f"- arXiv: `{paper.arxiv_id}`",
                f"- Cohort: `{paper.cohort}`",
                f"- PDF: [{paper.pdf_filename}]({paper.review_pdf_path})",
                f"- Database: {result_counts.get(paper.arxiv_id, 0)} result rows; "
                f"{len(methods)} distinct detected methods.",
                f"- Summary CSV row: `{paper.arxiv_id}:summary`",
                "- [ ] Every detected method row adjudicated",
                "- [ ] Missing-method sweep completed on the summary row",
                "- [ ] `review_complete` set to `yes`",
                "",
                "Detected methods:",
                "",
            ]
        )
        if not methods:
            lines.append("- None in the database. Verify this explicitly in the paper.")
        for method in methods:
            pair_text = "; ".join(method.dataset_table_pairs) or "no dataset/table evidence"
            problematic = (
                f"; {method.problematic_count} problematic rows" if method.problematic_count else ""
            )
            lines.append(
                f"- [ ] **{method.name}** — {method.result_count} rows; {method.role}; "
                f"{pair_text}{problematic}."
            )
        lines.extend(["", "Manual notes:", "", ""])
    return "\n".join(lines)


def write_review_markdown(path: Path, content: str) -> None:
    """Create the checklist once so manual checkboxes and notes survive reruns."""
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def copy_pdfs(output_dir: Path, papers: list[ReviewPaper]) -> None:
    """Copy only missing PDFs into the same two-cohort layout as the source review."""
    for paper in papers:
        destination = output_dir / paper.review_pdf_path
        destination.parent.mkdir(parents=True, exist_ok=True)
        if not destination.exists():
            shutil.copy2(paper.source_pdf, destination)


def run(args: argparse.Namespace) -> tuple[int, int]:
    args.output_dir.mkdir(parents=True, exist_ok=True)
    papers = load_papers(args.source_cohort, args.papers_dir)
    evidence, result_counts = load_method_evidence(
        args.database, [paper.arxiv_id for paper in papers]
    )
    rows = build_review_rows(papers, evidence, result_counts)
    write_review_csv(args.output_dir / "review_cohort.csv", rows)
    write_review_markdown(
        args.output_dir / "manual_review.md",
        render_review_markdown(papers, evidence, result_counts),
    )
    copy_pdfs(args.output_dir, papers)
    return len(papers), sum(len(methods) for methods in evidence.values())


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database", type=Path, default=_PROJECT_ROOT / "data/benchmarks.db")
    parser.add_argument("--papers-dir", type=Path, default=_PROJECT_ROOT / "papers")
    parser.add_argument(
        "--source-cohort",
        type=Path,
        default=(
            _PROJECT_ROOT / "experiments/extraction_validation/dataset_detection/review_cohort.csv"
        ),
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=_PROJECT_ROOT / "experiments/extraction_validation/method_detection",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    paper_count, method_count = run(build_parser().parse_args(argv))
    print(f"Prepared {paper_count} papers with {method_count} detected method rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
