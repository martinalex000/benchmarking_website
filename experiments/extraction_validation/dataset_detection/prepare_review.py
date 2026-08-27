#!/usr/bin/env python3
"""Prepare a blind manual-review cohort for dataset detection."""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import shutil
import sqlite3
from dataclasses import dataclass
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parents[3]
_COHORTS = ("with_database_results", "zero_database_results")
_FIELDNAMES = [
    "paper_index",
    "arxiv_id",
    "cohort",
    "title",
    "database_result_count",
    "pdf_path",
    "manual_dataset_name",
    "manual_relevant_table_refs",
    "manual_experiment_compatible",
    "manual_compatibility_reason",
    "manual_notes",
]


@dataclass(frozen=True)
class PaperCandidate:
    """A processed paper eligible for the manual review."""

    arxiv_id: str
    title: str
    database_result_count: int
    source_pdf: Path

    @property
    def cohort(self) -> str:
        return (
            "with_database_results" if self.database_result_count > 0 else "zero_database_results"
        )

    @property
    def pdf_filename(self) -> str:
        return f"{self.arxiv_id.replace('/', '_')}.pdf"


def load_excluded_ids(path: Path) -> set[str]:
    """Load paper IDs already used for the pre-screening review."""
    if not path.is_file():
        return set()
    with path.open(encoding="utf-8", newline="") as handle:
        return {
            arxiv_id
            for row in csv.DictReader(handle)
            if (arxiv_id := str(row.get("arxiv_id") or "").strip())
        }


def load_candidates(database: Path, papers_dir: Path) -> list[PaperCandidate]:
    """Load completed papers with the local artifacts needed for review."""
    connection = sqlite3.connect(f"file:{database}?mode=ro", uri=True)
    connection.row_factory = sqlite3.Row
    try:
        rows = connection.execute(
            """
            SELECT p.arxiv_id, p.title, COUNT(r.id) AS result_count
            FROM papers AS p
            LEFT JOIN results AS r ON r.paper_id = p.id
            WHERE p.arxiv_id IS NOT NULL
              AND p.extraction_status = 'extracted'
            GROUP BY p.id
            """
        ).fetchall()
    finally:
        connection.close()

    candidates: list[PaperCandidate] = []
    for row in rows:
        arxiv_id = str(row["arxiv_id"])
        paper_dir = papers_dir / arxiv_id
        source_pdf = paper_dir / "paper.pdf"
        extraction_artifact = paper_dir / "extracted" / "llm_output.yaml"
        if not source_pdf.is_file() or source_pdf.stat().st_size == 0:
            continue
        if not extraction_artifact.is_file():
            continue
        candidates.append(
            PaperCandidate(
                arxiv_id=arxiv_id,
                title=" ".join(str(row["title"]).split()),
                database_result_count=int(row["result_count"]),
                source_pdf=source_pdf,
            )
        )
    return candidates


def _stable_rank(candidate: PaperCandidate, seed: int) -> str:
    payload = f"dataset-detection:{seed}:{candidate.arxiv_id}".encode()
    return hashlib.sha256(payload).hexdigest()


def select_additions(
    candidates: list[PaperCandidate],
    existing_rows: list[dict[str, str]],
    *,
    target_per_cohort: int,
    seed: int,
    excluded_ids: set[str],
) -> list[PaperCandidate]:
    """Select only the papers needed to extend each cohort to its target."""
    existing_ids = {
        arxiv_id for row in existing_rows if (arxiv_id := str(row.get("arxiv_id") or "").strip())
    }
    existing_by_cohort = {
        cohort: {
            str(row.get("arxiv_id") or "").strip()
            for row in existing_rows
            if row.get("cohort") == cohort and str(row.get("arxiv_id") or "").strip()
        }
        for cohort in _COHORTS
    }

    additions: list[PaperCandidate] = []
    for cohort in _COHORTS:
        missing = max(0, target_per_cohort - len(existing_by_cohort[cohort]))
        eligible = [
            candidate
            for candidate in candidates
            if candidate.cohort == cohort
            and candidate.arxiv_id not in existing_ids
            and candidate.arxiv_id not in excluded_ids
        ]
        eligible.sort(key=lambda candidate: _stable_rank(candidate, seed))
        if len(eligible) < missing:
            raise RuntimeError(
                f"Need {missing} additional {cohort} papers, but only {len(eligible)} are eligible"
            )
        additions.extend(eligible[:missing])
    return additions


def load_review_rows(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    """Read existing annotations and retain reviewer-created columns."""
    if not path.is_file():
        return [], list(_FIELDNAMES)
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = [dict(row) for row in reader]
        fieldnames = list(reader.fieldnames or _FIELDNAMES)
    for fieldname in _FIELDNAMES:
        if fieldname not in fieldnames:
            fieldnames.append(fieldname)
    return rows, fieldnames


def _paper_order(existing_rows: list[dict[str, str]]) -> dict[str, int]:
    order: dict[str, int] = {}
    for row in existing_rows:
        arxiv_id = str(row.get("arxiv_id") or "").strip()
        if arxiv_id and arxiv_id not in order:
            order[arxiv_id] = len(order) + 1
    return order


def extend_review_csv(path: Path, additions: list[PaperCandidate]) -> list[dict[str, str]]:
    """Append one blank annotation row per new paper without changing existing rows."""
    existing_rows, fieldnames = load_review_rows(path)
    order = _paper_order(existing_rows)
    new_rows: list[dict[str, str]] = []
    for candidate in additions:
        order.setdefault(candidate.arxiv_id, len(order) + 1)
        new_rows.append(
            {
                "paper_index": str(order[candidate.arxiv_id]),
                "arxiv_id": candidate.arxiv_id,
                "cohort": candidate.cohort,
                "title": candidate.title,
                "database_result_count": str(candidate.database_result_count),
                "pdf_path": f"pdfs/{candidate.cohort}/{candidate.pdf_filename}",
                "manual_dataset_name": "",
                "manual_relevant_table_refs": "",
                "manual_experiment_compatible": "",
                "manual_compatibility_reason": "",
                "manual_notes": "",
            }
        )

    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(existing_rows)
        writer.writerows(new_rows)
    return [*existing_rows, *new_rows]


def _review_header(seed: int) -> str:
    return "\n".join(
        [
            "# Dataset-detection manual review",
            "",
            "This is a blind review of dataset discovery, relevant-table selection, and experiment compatibility.",
            "The pipeline's extracted dataset names and table references are intentionally not shown.",
            "",
            "## Annotation protocol",
            "",
            "1. Read the paper and identify every dataset with quantitative model-comparison results.",
            "2. Duplicate that paper's CSV row once per dataset. If none exists, enter `NONE`.",
            "3. Record the main and appendix result tables for that dataset, such as `Table 2; Table 7`.",
            "4. Set compatibility to `yes`, `no`, or `unclear` for the current leaderboard protocol.",
            "5. Explain incompatibility or uncertainty (task, split, metric, features, external data, or another protocol difference).",
            "",
            f"Selection seed: `{seed}`. Papers from the pre-screening cohort are excluded.",
            "",
            "## Papers",
            "",
            "",
        ]
    )


def _review_section(candidate: PaperCandidate, index: int) -> str:
    pdf_path = f"pdfs/{candidate.cohort}/{candidate.pdf_filename}"
    return "\n".join(
        [
            f"### {index}. {candidate.title}",
            "",
            f"- arXiv: `{candidate.arxiv_id}`",
            f"- Cohort: `{candidate.cohort}`",
            f"- PDF: [{candidate.pdf_filename}]({pdf_path})",
            "- [ ] All quantitative datasets recorded in `review_cohort.csv`",
            "- [ ] Relevant result tables recorded for every dataset",
            "- [ ] Compatibility decision and reason recorded for every dataset",
            "",
            "Manual notes:",
            "",
            "",
        ]
    )


def extend_review_markdown(path: Path, additions: list[PaperCandidate], seed: int) -> None:
    """Append missing paper sections while retaining manually entered notes."""
    if not path.is_file():
        content = _review_header(seed)
        sections = [
            _review_section(candidate, index) for index, candidate in enumerate(additions, start=1)
        ]
        path.write_text(content + "\n".join(sections), encoding="utf-8")
        return
    if not additions:
        return

    existing = path.read_text(encoding="utf-8").rstrip()
    start = len(re.findall(r"(?m)^- arXiv: `", existing)) + 1
    sections = [
        _review_section(candidate, index) for index, candidate in enumerate(additions, start=start)
    ]
    path.write_text(existing + "\n\n" + "\n".join(sections), encoding="utf-8")


def copy_pdfs(output_dir: Path, candidates: list[PaperCandidate]) -> None:
    """Copy source PDFs into the two cohort folders without deleting existing files."""
    for cohort in _COHORTS:
        (output_dir / "pdfs" / cohort).mkdir(parents=True, exist_ok=True)
    for candidate in candidates:
        destination = output_dir / "pdfs" / candidate.cohort / candidate.pdf_filename
        if not destination.exists():
            shutil.copy2(candidate.source_pdf, destination)


def run(args: argparse.Namespace) -> list[dict[str, str]]:
    args.output_dir.mkdir(parents=True, exist_ok=True)
    review_csv = args.output_dir / "review_cohort.csv"
    existing_rows, _ = load_review_rows(review_csv)
    candidates = load_candidates(args.database, args.papers_dir)
    additions = select_additions(
        candidates,
        existing_rows,
        target_per_cohort=args.target_per_cohort,
        seed=args.seed,
        excluded_ids=load_excluded_ids(args.exclude_cohort),
    )
    final_rows = extend_review_csv(review_csv, additions)
    extend_review_markdown(args.output_dir / "manual_review.md", additions, args.seed)

    candidates_by_id = {candidate.arxiv_id: candidate for candidate in candidates}
    selected_ids = {
        str(row.get("arxiv_id") or "").strip()
        for row in final_rows
        if str(row.get("arxiv_id") or "").strip()
    }
    missing = sorted(selected_ids - candidates_by_id.keys())
    if missing:
        raise RuntimeError(f"Selected papers are no longer eligible: {', '.join(missing)}")
    copy_pdfs(args.output_dir, [candidates_by_id[arxiv_id] for arxiv_id in selected_ids])
    return final_rows


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database", type=Path, default=_PROJECT_ROOT / "data/benchmarks.db")
    parser.add_argument("--papers-dir", type=Path, default=_PROJECT_ROOT / "papers")
    parser.add_argument(
        "--exclude-cohort",
        type=Path,
        default=_PROJECT_ROOT / "experiments/prescreen_validation/output/review_cohort.csv",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=_PROJECT_ROOT / "experiments/extraction_validation/dataset_detection",
    )
    parser.add_argument("--target-per-cohort", type=int, default=10)
    parser.add_argument("--seed", type=int, default=20260827)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    rows = run(args)
    paper_counts = {
        cohort: len(
            {row["arxiv_id"] for row in rows if row.get("cohort") == cohort and row.get("arxiv_id")}
        )
        for cohort in _COHORTS
    }
    print(f"Review files written to {args.output_dir}")
    for cohort, count in paper_counts.items():
        print(f"{cohort}: {count} papers")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
