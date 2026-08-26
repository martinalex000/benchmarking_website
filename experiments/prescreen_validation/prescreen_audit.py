#!/usr/bin/env python3
"""Audit abstract pre-screening decisions against lexical and downstream evidence.

This experiment is read-only. It combines the Kaggle screening decision stream,
its SQLite abstract queue, local paper artifacts, and the benchmark database. The
generated review cohort is evidence for manual inspection, not an automatic
classification of screening errors.
"""

from __future__ import annotations

import argparse
import csv
import json
import random
import re
import sqlite3
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import yaml

_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))


@dataclass(frozen=True)
class ScreeningDecision:
    """One completed pre-screening decision."""

    arxiv_id: str
    decision: str
    matched_tier: str
    datasets_mentioned: tuple[str, ...]
    confidence: float | None
    reason: str


@dataclass(frozen=True)
class QueuePaper:
    """Title and abstract presented to the pre-screener."""

    arxiv_id: str
    title: str
    abstract: str


@dataclass(frozen=True)
class DownstreamEvidence:
    """Evidence produced after a paper passed or bypassed screening."""

    extraction_status: str | None = None
    stored_result_count: int | None = None
    artifact_result_count: int | None = None
    artifact_error: str | None = None


@dataclass
class AuditPaper:
    """All evidence used for aggregate analysis and cohort selection."""

    arxiv_id: str
    title: str
    abstract: str
    decision: str
    matched_tier: str
    confidence: float | None
    reason: str
    screener_datasets: list[str]
    abstract_dataset_mentions: list[str]
    abstract_exact_case_mentions: list[str]
    full_text_available: bool
    full_text_dataset_mentions: list[str]
    downstream: DownstreamEvidence = field(default_factory=DownstreamEvidence)
    cohort: str = ""

    @property
    def suspicious_rejection(self) -> bool:
        """Return whether cheap evidence makes a rejection worth prioritizing."""
        return self.decision == "rejected" and bool(
            self.screener_datasets
            or self.abstract_exact_case_mentions
            or len(self.abstract_dataset_mentions) >= 2
            or self.full_text_dataset_mentions
            or (self.downstream.artifact_result_count or 0) > 0
        )


class DatasetMatcher:
    """Exact-name lexical matcher for canonical benchmark dataset names."""

    def __init__(self, names: list[str]) -> None:
        spellings: dict[str, str] = {}
        for name in names:
            cleaned = str(name).strip()
            if cleaned:
                spellings.setdefault(cleaned.casefold(), cleaned)
        if not spellings:
            raise ValueError("dataset vocabulary is empty")
        self._spellings = spellings
        alternatives = sorted(
            (re.escape(name) for name in spellings.values()), key=len, reverse=True
        )
        self._pattern = re.compile(
            r"(?<![A-Za-z0-9])(?:" + "|".join(alternatives) + r")(?![A-Za-z0-9])",
            re.IGNORECASE,
        )

    def find(self, text: str) -> tuple[list[str], list[str]]:
        """Return all canonical matches and the subset with canonical casing."""
        found: dict[str, str] = {}
        exact: dict[str, str] = {}
        for match in self._pattern.finditer(text or ""):
            raw = match.group(0)
            canonical = self._spellings[raw.casefold()]
            found[canonical.casefold()] = canonical
            if raw == canonical:
                exact[canonical.casefold()] = canonical
        key = str.casefold
        return sorted(found.values(), key=key), sorted(exact.values(), key=key)


def load_dataset_names(seed_path: Path) -> list[str]:
    """Load the canonical dataset vocabulary used by extraction prompts."""
    payload = yaml.safe_load(seed_path.read_text(encoding="utf-8")) or {}
    names = {
        str(dataset.get("name") or "").strip()
        for benchmark in payload.get("benchmarks", [])
        for dataset in benchmark.get("datasets", [])
        if isinstance(dataset, dict)
    }
    return sorted((name for name in names if name), key=str.casefold)


def load_decisions(path: Path) -> dict[str, ScreeningDecision]:
    """Stream the YAML document sequence and validate its decision keys."""
    decisions: dict[str, ScreeningDecision] = {}
    with path.open(encoding="utf-8") as handle:
        for index, payload in enumerate(yaml.safe_load_all(handle), start=1):
            if not isinstance(payload, dict):
                raise ValueError(f"invalid screening document {index} in {path}")
            arxiv_id = str(payload.get("arxiv_id") or "").strip()
            decision = str(payload.get("decision") or "").strip()
            if not arxiv_id or decision not in {"accepted", "rejected"}:
                raise ValueError(f"invalid screening document {index} in {path}")
            if arxiv_id in decisions:
                raise ValueError(f"duplicate screening decision for arXiv:{arxiv_id}")
            raw_datasets = payload.get("datasets_mentioned") or []
            if not isinstance(raw_datasets, list):
                raw_datasets = []
            raw_confidence = payload.get("confidence")
            try:
                confidence = float(raw_confidence) if raw_confidence is not None else None
            except (TypeError, ValueError):
                confidence = None
            decisions[arxiv_id] = ScreeningDecision(
                arxiv_id=arxiv_id,
                decision=decision,
                matched_tier=str(payload.get("matched_tier") or "unknown"),
                datasets_mentioned=tuple(
                    str(item).strip() for item in raw_datasets if str(item).strip()
                ),
                confidence=confidence,
                reason=str(payload.get("reason") or "").strip(),
            )
    return decisions


def _connect_read_only(path: Path) -> sqlite3.Connection:
    connection = sqlite3.connect(f"file:{path.resolve()}?mode=ro", uri=True)
    connection.row_factory = sqlite3.Row
    return connection


def load_queue_papers(path: Path, decision_ids: set[str]) -> dict[str, QueuePaper]:
    """Load the metadata corresponding to completed decisions from the queue."""
    papers: dict[str, QueuePaper] = {}
    with _connect_read_only(path) as connection:
        for row in connection.execute("SELECT arxiv_id, title, abstract FROM papers"):
            arxiv_id = str(row["arxiv_id"])
            if arxiv_id not in decision_ids:
                continue
            papers[arxiv_id] = QueuePaper(
                arxiv_id=arxiv_id,
                title=str(row["title"] or ""),
                abstract=str(row["abstract"] or ""),
            )
    return papers


def load_database_evidence(path: Path) -> dict[str, DownstreamEvidence]:
    """Count result rows for every paper without modifying the database."""
    evidence: dict[str, DownstreamEvidence] = {}
    query = """
        SELECT p.arxiv_id, p.extraction_status, COUNT(r.id) AS result_count
        FROM papers AS p
        LEFT JOIN results AS r ON r.paper_id = p.id
        WHERE p.arxiv_id IS NOT NULL
        GROUP BY p.id, p.arxiv_id, p.extraction_status
    """
    with _connect_read_only(path) as connection:
        for row in connection.execute(query):
            evidence[str(row["arxiv_id"])] = DownstreamEvidence(
                extraction_status=str(row["extraction_status"] or "") or None,
                stored_result_count=int(row["result_count"]),
            )
    return evidence


def _artifact_result_count(path: Path) -> tuple[int | None, str | None]:
    if not path.is_file():
        return None, None
    try:
        payload = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        result_block = payload.get("results") or {}
        rows = result_block.get("results") if isinstance(result_block, dict) else result_block
        return (len(rows), None) if isinstance(rows, list) else (0, None)
    except (OSError, yaml.YAMLError, UnicodeError) as exc:
        return None, f"{type(exc).__name__}: {exc}"


def add_artifact_evidence(
    evidence: dict[str, DownstreamEvidence], papers_dir: Path, decision_ids: set[str]
) -> None:
    """Add raw extraction row counts for screened papers with local artifacts."""
    for arxiv_id in decision_ids:
        path = papers_dir / arxiv_id / "extracted" / "llm_output.yaml"
        artifact_count, artifact_error = _artifact_result_count(path)
        if artifact_count is None and artifact_error is None:
            continue
        previous = evidence.get(arxiv_id, DownstreamEvidence())
        evidence[arxiv_id] = DownstreamEvidence(
            extraction_status=previous.extraction_status,
            stored_result_count=previous.stored_result_count,
            artifact_result_count=artifact_count,
            artifact_error=artifact_error,
        )


def build_audit_rows(
    decisions: dict[str, ScreeningDecision],
    queue_papers: dict[str, QueuePaper],
    downstream: dict[str, DownstreamEvidence],
    matcher: DatasetMatcher,
    papers_dir: Path,
) -> list[AuditPaper]:
    """Join screening, lexical, full-text, and downstream evidence."""
    missing = sorted(set(decisions) - set(queue_papers))
    if missing:
        preview = ", ".join(missing[:5])
        raise ValueError(f"{len(missing)} decisions are missing from the queue: {preview}")

    rows: list[AuditPaper] = []
    for arxiv_id, decision in decisions.items():
        paper = queue_papers[arxiv_id]
        mentions, exact_mentions = matcher.find(f"{paper.title}\n{paper.abstract}")
        full_text_mentions: list[str] = []
        full_text_available = False
        if decision.decision == "rejected":
            full_text_path = papers_dir / arxiv_id / "latex" / "expanded.tex"
            if full_text_path.is_file():
                full_text_available = True
                text = full_text_path.read_text(encoding="utf-8", errors="ignore")
                full_text_mentions, _ = matcher.find(text)
        rows.append(
            AuditPaper(
                arxiv_id=arxiv_id,
                title=paper.title,
                abstract=paper.abstract,
                decision=decision.decision,
                matched_tier=decision.matched_tier,
                confidence=decision.confidence,
                reason=decision.reason,
                screener_datasets=list(decision.datasets_mentioned),
                abstract_dataset_mentions=mentions,
                abstract_exact_case_mentions=exact_mentions,
                full_text_available=full_text_available,
                full_text_dataset_mentions=full_text_mentions,
                downstream=downstream.get(arxiv_id, DownstreamEvidence()),
            )
        )
    return rows


def classify_cohorts(rows: list[AuditPaper]) -> dict[str, list[AuditPaper]]:
    """Create validation strata with distinct interpretations."""
    cohorts: dict[str, list[AuditPaper]] = defaultdict(list)
    for row in rows:
        if row.suspicious_rejection:
            cohorts["rejected_suspicious"].append(row)
        elif row.decision == "rejected":
            cohorts["rejected_control"].append(row)
        elif row.downstream.artifact_result_count == 0:
            cohorts["accepted_zero_artifact_results"].append(row)
        elif (row.downstream.artifact_result_count or 0) > 0:
            cohorts["accepted_positive_control"].append(row)
    return dict(cohorts)


def _allocate_sample_size(sample_size: int) -> dict[str, int]:
    """Allocate a roughly 30/20/30/20 percent review cohort."""
    if sample_size < 4:
        raise ValueError("sample size must be at least 4")
    names = (
        "rejected_suspicious",
        "rejected_control",
        "accepted_zero_artifact_results",
        "accepted_positive_control",
    )
    weights = (0.3, 0.2, 0.3, 0.2)
    allocation = {
        name: int(sample_size * weight) for name, weight in zip(names, weights, strict=True)
    }
    for name in names:
        if allocation[name] == 0:
            allocation[name] = 1
    while sum(allocation.values()) < sample_size:
        name = max(
            names, key=lambda item: weights[names.index(item)] * sample_size - allocation[item]
        )
        allocation[name] += 1
    while sum(allocation.values()) > sample_size:
        name = max(names, key=lambda item: allocation[item] - 1)
        allocation[name] -= 1
    return allocation


def select_review_cohort(
    cohorts: dict[str, list[AuditPaper]], sample_size: int, seed: int
) -> list[AuditPaper]:
    """Select a deterministic stratified sample for manual review."""
    allocation = _allocate_sample_size(sample_size)
    selected: list[AuditPaper] = []
    for offset, (cohort, count) in enumerate(allocation.items()):
        candidates = sorted(cohorts.get(cohort, []), key=lambda row: row.arxiv_id)
        if len(candidates) < count:
            raise ValueError(f"cohort {cohort!r} has {len(candidates)} papers; need {count}")
        rng = random.Random(seed + offset)
        if cohort == "rejected_suspicious":
            # Direct downstream contradictions are substantially stronger leads than
            # catalog-name grep hits. Randomize only within equal evidence scores.
            def evidence_score(row: AuditPaper, *, _rng: random.Random = rng) -> tuple[int, float]:
                score = 0
                score += 1_000 * int((row.downstream.artifact_result_count or 0) > 0)
                score += 500 * int((row.downstream.stored_result_count or 0) > 0)
                score += 100 * int(row.downstream.artifact_result_count == 0)
                score += 50 * int(row.full_text_available)
                score += 10 * len(row.abstract_exact_case_mentions)
                score += 5 * len(row.abstract_dataset_mentions)
                score += 2 * len(row.screener_datasets)
                return score, _rng.random()

            chosen = sorted(candidates, key=evidence_score, reverse=True)[:count]
        else:
            chosen = rng.sample(candidates, count)
        for row in chosen:
            row.cohort = cohort
        selected.extend(chosen)
    return selected


def summarize(rows: list[AuditPaper], cohorts: dict[str, list[AuditPaper]]) -> dict[str, Any]:
    """Build compact aggregate statistics and explicit denominators."""
    decisions = Counter(row.decision for row in rows)
    by_tier = Counter(f"{row.matched_tier}/{row.decision}" for row in rows)
    rejected = [row for row in rows if row.decision == "rejected"]
    accepted = [row for row in rows if row.decision == "accepted"]
    accepted_with_artifact = [
        row for row in accepted if row.downstream.artifact_result_count is not None
    ]
    accepted_with_db = [row for row in accepted if row.downstream.stored_result_count is not None]
    stored_zero_statuses = Counter(
        row.downstream.extraction_status or "unknown"
        for row in accepted_with_db
        if row.downstream.stored_result_count == 0
    )
    return {
        "screening": {
            "total": len(rows),
            "decisions": dict(sorted(decisions.items())),
            "by_tier_and_decision": dict(sorted(by_tier.items())),
        },
        "rejected_evidence": {
            "denominator": len(rejected),
            "screener_reported_dataset": sum(bool(row.screener_datasets) for row in rejected),
            "canonical_name_in_title_or_abstract": sum(
                bool(row.abstract_dataset_mentions) for row in rejected
            ),
            "canonical_name_with_exact_case": sum(
                bool(row.abstract_exact_case_mentions) for row in rejected
            ),
            "local_full_text_available": sum(row.full_text_available for row in rejected),
            "with_local_extraction_artifact": sum(
                row.downstream.artifact_result_count is not None for row in rejected
            ),
            "positive_raw_artifact_results": sum(
                (row.downstream.artifact_result_count or 0) > 0 for row in rejected
            ),
            "positive_stored_results": sum(
                (row.downstream.stored_result_count or 0) > 0 for row in rejected
            ),
            "prioritized_as_suspicious": len(cohorts.get("rejected_suspicious", [])),
        },
        "accepted_downstream": {
            "denominator_all_accepted": len(accepted),
            "with_database_paper": len(accepted_with_db),
            "with_local_extraction_artifact": len(accepted_with_artifact),
            "zero_raw_artifact_results": sum(
                row.downstream.artifact_result_count == 0 for row in accepted_with_artifact
            ),
            "positive_raw_artifact_results": sum(
                (row.downstream.artifact_result_count or 0) > 0 for row in accepted_with_artifact
            ),
            "zero_stored_results": sum(
                row.downstream.stored_result_count == 0 for row in accepted_with_db
            ),
            "zero_stored_results_by_extraction_status": dict(sorted(stored_zero_statuses.items())),
            "artifact_parse_errors": sum(bool(row.downstream.artifact_error) for row in accepted),
        },
        "cohort_sizes": {name: len(values) for name, values in sorted(cohorts.items())},
    }


def _percentage(numerator: int, denominator: int) -> str:
    return "n/a" if not denominator else f"{100 * numerator / denominator:.2f}%"


def render_summary(summary: dict[str, Any]) -> str:
    """Render aggregate findings with caveats close to each proxy."""
    rejected = summary["rejected_evidence"]
    accepted = summary["accepted_downstream"]
    lines = [
        "# Pre-screening audit summary",
        "",
        "This is a diagnostic experiment, not an accuracy estimate. Dataset-name matches are review "
        "leads rather than proof that a paper reports comparable benchmark results.",
        "",
        "## Screening corpus",
        "",
        f"- Completed decisions: {summary['screening']['total']:,}",
    ]
    for decision, count in summary["screening"]["decisions"].items():
        lines.append(f"- {decision.title()}: {count:,}")
    lines.extend(
        [
            "",
            "## Rejected-paper evidence",
            "",
            f"Denominator: {rejected['denominator']:,} rejected abstracts.",
            "",
            f"- Screener nevertheless named a dataset: {rejected['screener_reported_dataset']:,} "
            f"({_percentage(rejected['screener_reported_dataset'], rejected['denominator'])})",
            f"- Canonical dataset name in title/abstract: "
            f"{rejected['canonical_name_in_title_or_abstract']:,} "
            f"({_percentage(rejected['canonical_name_in_title_or_abstract'], rejected['denominator'])})",
            f"- Canonical name with exact catalog casing: "
            f"{rejected['canonical_name_with_exact_case']:,} "
            f"({_percentage(rejected['canonical_name_with_exact_case'], rejected['denominator'])})",
            f"- Prioritized suspicious rejections: {rejected['prioritized_as_suspicious']:,}",
            f"- Rejected papers with a local extraction artifact: "
            f"{rejected['with_local_extraction_artifact']:,}; with positive raw rows: "
            f"{rejected['positive_raw_artifact_results']:,}",
            "",
            "A name match can be incidental, can refer to a non-standard protocol, or can occur while "
            "the paper reports no result. Manual abstract/full-text review is required.",
            "",
            "## Accepted-paper downstream evidence",
            "",
            f"Denominator: {accepted['denominator_all_accepted']:,} accepted screening decisions.",
            "",
            f"- Joined to a database paper: {accepted['with_database_paper']:,}",
            f"- Has a local extraction artifact: {accepted['with_local_extraction_artifact']:,}",
            f"- Local artifact has zero raw result rows: {accepted['zero_raw_artifact_results']:,} "
            f"({_percentage(accepted['zero_raw_artifact_results'], accepted['with_local_extraction_artifact'])} "
            "of artifacts)",
            f"- Database has zero stored result rows: {accepted['zero_stored_results']:,} "
            f"({_percentage(accepted['zero_stored_results'], accepted['with_database_paper'])} "
            "of joined papers)",
            "",
            "Zero raw rows are the cleaner signal for a possible screening false positive. Zero stored "
            "rows can instead be caused by parsing, protocol rejection, quarantine, or unresolved datasets.",
        ]
    )
    return "\n".join(lines) + "\n"


def _format_list(values: list[str]) -> str:
    return ", ".join(values) if values else "none"


def render_review(selected: list[AuditPaper], seed: int) -> str:
    """Render the paper-level evidence needed for a blind manual decision."""
    lines = [
        "# Manual pre-screening review cohort",
        "",
        f"Deterministic sample seed: `{seed}`. Review the abstract before using the existing decision "
        "and downstream evidence. Record labels in `review_cohort.csv`.",
        "",
        "Manual question: **Does this abstract justify sending the paper to full extraction because "
        "it indicates benchmark results or a new benchmark?** Dataset mention alone is insufficient.",
        "",
    ]
    for index, row in enumerate(selected, start=1):
        downstream = row.downstream
        lines.extend(
            [
                f"## {index}. arXiv:{row.arxiv_id} — {row.cohort}",
                "",
                f"**Title:** {row.title}",
                "",
                f"**Abstract:** {row.abstract}",
                "",
                "### Evidence revealed after manual judgment",
                "",
                f"- Screen decision: {row.decision}; tier: {row.matched_tier}; "
                f"confidence: {row.confidence if row.confidence is not None else 'unknown'}",
                f"- Screen reason: {row.reason or 'none'}",
                f"- Screener datasets: {_format_list(row.screener_datasets)}",
                f"- Canonical names in title/abstract: {_format_list(row.abstract_dataset_mentions)}",
                f"- Canonical names in available local full text: "
                f"{_format_list(row.full_text_dataset_mentions)}",
                f"- Downstream extraction status: {downstream.extraction_status or 'not in database'}",
                f"- Raw artifact rows: "
                f"{downstream.artifact_result_count if downstream.artifact_result_count is not None else 'no artifact'}; "
                f"stored rows: "
                f"{downstream.stored_result_count if downstream.stored_result_count is not None else 'no database paper'}",
                "",
            ]
        )
    lines.extend(
        [
            "## Optional rejected-paper downstream check",
            "",
            "After manual abstract review, a rejected paper can be forced through the remaining pipeline "
            "with the command below. This experiment does not run it automatically because it makes local "
            "paper/database changes and uses model calls.",
            "",
            "```bash",
            "UV_CACHE_DIR=/tmp/benchmarking-uv-cache uv run python scripts/process_papers.py "
            "<ARXIV_ID> --skip-screen --skip-export",
            "```",
        ]
    )
    return "\n".join(lines) + "\n"


def write_outputs(
    output_dir: Path,
    summary: dict[str, Any],
    selected: list[AuditPaper],
    seed: int,
    dataset_count: int,
) -> None:
    """Write aggregate and manual-review artifacts."""
    output_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": datetime.now(UTC).isoformat(),
        "sample_seed": seed,
        "canonical_dataset_count": dataset_count,
        **summary,
    }
    (output_dir / "summary.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    (output_dir / "summary.md").write_text(render_summary(summary), encoding="utf-8")
    (output_dir / "manual_review.md").write_text(render_review(selected, seed), encoding="utf-8")

    fieldnames = [
        "arxiv_id",
        "cohort",
        "title",
        "decision",
        "matched_tier",
        "confidence",
        "screener_datasets",
        "abstract_dataset_mentions",
        "full_text_dataset_mentions",
        "extraction_status",
        "artifact_result_count",
        "stored_result_count",
        "manual_should_pass",
        "manual_has_benchmark_results",
        "manual_notes",
    ]
    with (output_dir / "review_cohort.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in selected:
            writer.writerow(
                {
                    "arxiv_id": row.arxiv_id,
                    "cohort": row.cohort,
                    "title": row.title,
                    "decision": row.decision,
                    "matched_tier": row.matched_tier,
                    "confidence": row.confidence,
                    "screener_datasets": "; ".join(row.screener_datasets),
                    "abstract_dataset_mentions": "; ".join(row.abstract_dataset_mentions),
                    "full_text_dataset_mentions": "; ".join(row.full_text_dataset_mentions),
                    "extraction_status": row.downstream.extraction_status,
                    "artifact_result_count": row.downstream.artifact_result_count,
                    "stored_result_count": row.downstream.stored_result_count,
                    "manual_should_pass": "",
                    "manual_has_benchmark_results": "",
                    "manual_notes": "",
                }
            )
    rejected_ids = [row.arxiv_id for row in selected if row.decision == "rejected"]
    (output_dir / "rejected_rerun_candidates.txt").write_text(
        "\n".join(rejected_ids) + ("\n" if rejected_ids else ""), encoding="utf-8"
    )


def run_experiment(args: argparse.Namespace) -> dict[str, Any]:
    """Run the read-only audit and write its outputs."""
    names = load_dataset_names(args.seed_data)
    matcher = DatasetMatcher(names)
    decisions = load_decisions(args.results)
    queue_papers = load_queue_papers(args.queue, set(decisions))
    downstream = load_database_evidence(args.database)
    add_artifact_evidence(downstream, args.papers_dir, set(decisions))
    rows = build_audit_rows(decisions, queue_papers, downstream, matcher, args.papers_dir)
    cohorts = classify_cohorts(rows)
    selected = select_review_cohort(cohorts, args.sample_size, args.random_seed)
    summary = summarize(rows, cohorts)
    write_outputs(args.output_dir, summary, selected, args.random_seed, len(names))
    return summary


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--results", type=Path, default=_PROJECT_ROOT / "papers/screening/results.yaml"
    )
    parser.add_argument(
        "--queue", type=Path, default=_PROJECT_ROOT / "papers/screening/queue.sqlite3"
    )
    parser.add_argument("--database", type=Path, default=_PROJECT_ROOT / "data/benchmarks.db")
    parser.add_argument("--seed-data", type=Path, default=_PROJECT_ROOT / "config/seed_data.yaml")
    parser.add_argument("--papers-dir", type=Path, default=_PROJECT_ROOT / "papers")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=_PROJECT_ROOT / "experiments/prescreen_validation/output",
    )
    parser.add_argument("--sample-size", type=int, default=10)
    parser.add_argument("--random-seed", type=int, default=20260826)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    summary = run_experiment(args)
    print(render_summary(summary), end="")
    print(f"Review files written to {args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
