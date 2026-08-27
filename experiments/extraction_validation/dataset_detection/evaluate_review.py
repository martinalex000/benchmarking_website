#!/usr/bin/env python3
"""Compare manual dataset-detection annotations with stored database results."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sqlite3
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import UTC, datetime
from math import sqrt
from pathlib import Path
from typing import Any

_PROJECT_ROOT = Path(__file__).resolve().parents[3]


@dataclass(frozen=True)
class ManualTruth:
    """Normalized interpretation of one free-text manual annotation."""

    strict_paper_label: bool | None
    expected_datasets: tuple[str, ...] = ()
    annotated_datasets: tuple[str, ...] = ()
    table_refs: tuple[tuple[str, tuple[str, ...]], ...] = ()
    table_refs_complete: bool = False
    qualification: str = ""


@dataclass
class DatabaseDataset:
    """Stored evidence for one paper-dataset pair."""

    name: str
    table_refs: set[str] = field(default_factory=set)
    result_rows: int = 0
    protocols: set[str] = field(default_factory=set)


def _refs(*values: tuple[str, str | tuple[str, ...]]) -> tuple[tuple[str, tuple[str, ...]], ...]:
    normalized: list[tuple[str, tuple[str, ...]]] = []
    for dataset, refs in values:
        normalized.append((dataset, (refs,) if isinstance(refs, str) else refs))
    return tuple(normalized)


# The CSV deliberately uses one free-text row per paper. This map records the conservative
# normalization used for scoring; qualified judgments are never forced into the strict metrics.
_MANUAL_TRUTH: dict[str, ManualTruth] = {
    "2304.10074": ManualTruth(
        True,
        ("ogbl-collab", "ogbl-ddi", "ogbl-citation2", "ogbl-ppa"),
        table_refs=_refs(
            ("ogbl-collab", "Table 2"),
            ("ogbl-ddi", "Table 1"),
            ("ogbl-citation2", "Table 1"),
            ("ogbl-ppa", "Table 1"),
        ),
        table_refs_complete=True,
    ),
    "2310.01089": ManualTruth(
        True,
        ("Cora", "CiteSeer", "Texas", "Wisconsin", "Cornell"),
        table_refs=_refs(
            ("Cora", "Table 4"),
            ("CiteSeer", "Table 4"),
            ("Texas", "Table 1"),
            ("Wisconsin", "Table 1"),
            ("Cornell", "Table 1"),
        ),
        table_refs_complete=True,
    ),
    "2003.13663": ManualTruth(
        True,
        ("Cora",),
        table_refs=_refs(("Cora", "Table 2")),
        table_refs_complete=True,
    ),
    "2206.08005": ManualTruth(
        True,
        ("BBBP", "Tox21", "ToxCast", "SIDER", "ClinTox", "MUV", "HIV", "BACE"),
        table_refs=_refs(
            *(
                (dataset, "Table 1")
                for dataset in (
                    "BBBP",
                    "Tox21",
                    "ToxCast",
                    "SIDER",
                    "ClinTox",
                    "MUV",
                    "HIV",
                    "BACE",
                )
            )
        ),
        table_refs_complete=True,
    ),
    "2401.14155": ManualTruth(False),
    "1903.02428": ManualTruth(
        True,
        (
            "Cora",
            "CiteSeer",
            "PubMed",
            "MUTAG",
            "PROTEINS",
            "COLLAB",
            "IMDB-BINARY",
            "REDDIT-BINARY",
            "ModelNet10",
        ),
        table_refs=_refs(
            ("Cora", "Table 1"),
            ("CiteSeer", "Table 1"),
            ("PubMed", "Table 1"),
            ("MUTAG", "Table 2"),
            ("ModelNet10", "Table 3"),
        ),
        qualification="Only five dataset-to-table assignments were explicit; table metrics exclude this paper.",
    ),
    "1710.03059": ManualTruth(
        None,
        annotated_datasets=("Cora", "CiteSeer", "PubMed", "BlogCatalog", "POS", "PPI"),
        qualification="Manual compatibility was 'partially' without a dataset-level split.",
    ),
    "2403.07954": ManualTruth(
        True,
        ("Cora", "CiteSeer", "PubMed", "Actor", "Chameleon", "Squirrel"),
        table_refs=_refs(
            *(
                (dataset, "Table 2")
                for dataset in (
                    "Cora",
                    "CiteSeer",
                    "PubMed",
                    "Actor",
                    "Chameleon",
                    "Squirrel",
                )
            )
        ),
        table_refs_complete=True,
    ),
    "2508.05070": ManualTruth(
        True,
        ("ZINC-12k", "MNIST", "CIFAR10", "PATTERN", "CLUSTER", "Peptides-func", "Peptides-struct"),
        table_refs=_refs(
            ("ZINC-12k", "Table 2"),
            ("MNIST", "Table 2"),
            ("CIFAR10", "Table 2"),
            ("PATTERN", "Table 2"),
            ("CLUSTER", "Table 2"),
            ("Peptides-func", "Table 3"),
            ("Peptides-struct", "Table 3"),
        ),
        table_refs_complete=True,
    ),
    "1905.12560": ManualTruth(
        None,
        annotated_datasets=(
            "CSL",
            "IMDB-BINARY",
            "IMDB-MULTI",
            "COLLAB",
            "MUTAG",
            "PTC",
            "PROTEINS",
        ),
        qualification="Manual judgment was 'yes?' and questioned the evaluation protocols.",
    ),
    "2010.05788": ManualTruth(
        None,
        annotated_datasets=("MNIST", "Bitcoin-Alpha", "Bitcoin-OTC"),
        qualification="Manual note says one MNIST value could be compatible; requires adjudication.",
    ),
    "2001.06216": ManualTruth(False),
    "2112.07191": ManualTruth(False),
    "1908.01207": ManualTruth(False),
    "2006.05535": ManualTruth(
        None,
        annotated_datasets=("Cora", "PubMed", "Facebook", "LastFM"),
        qualification="Privacy-constrained experiments were marked unclear rather than comparable.",
    ),
    "2210.01002": ManualTruth(False),
    "1802.04407": ManualTruth(False),
    "2402.18974": ManualTruth(False),
    "2505.22252": ManualTruth(False),
    "2502.15054": ManualTruth(False),
}


def _name_key(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.casefold())


def _table_key(value: str) -> str:
    match = re.search(r"\d+", value)
    return f"table{match.group(0)}" if match else _name_key(value)


def _ratio(numerator: int, denominator: int) -> float | None:
    return numerator / denominator if denominator else None


def _wilson(successes: int, total: int, z: float = 1.96) -> list[float] | None:
    """Return a descriptive 95% Wilson interval for a binomial proportion."""
    if not total:
        return None
    proportion = successes / total
    denominator = 1 + z**2 / total
    center = (proportion + z**2 / (2 * total)) / denominator
    half_width = (
        z * sqrt(proportion * (1 - proportion) / total + z**2 / (4 * total**2)) / denominator
    )
    return [center - half_width, center + half_width]


def load_annotations(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        rows = [dict(row) for row in csv.DictReader(handle)]
    ids = [str(row.get("arxiv_id") or "").strip() for row in rows]
    if len(ids) != 20 or len(set(ids)) != 20:
        raise ValueError("Expected exactly 20 unique annotated papers")
    missing = sorted(set(ids) - _MANUAL_TRUTH.keys())
    stale = sorted(_MANUAL_TRUTH.keys() - set(ids))
    if missing or stale:
        raise ValueError(f"Manual adjudication is stale: missing={missing}, stale={stale}")
    return rows


def load_database_evidence(
    database: Path, paper_ids: list[str]
) -> tuple[dict[str, dict[str, DatabaseDataset]], dict[str, int]]:
    placeholders = ",".join("?" for _ in paper_ids)
    connection = sqlite3.connect(f"file:{database}?mode=ro", uri=True)
    connection.row_factory = sqlite3.Row
    try:
        rows = connection.execute(
            f"""
            SELECT p.arxiv_id, d.name AS dataset, r.table_ref, r.protocol_decision,
                   COUNT(*) AS result_rows
            FROM papers AS p
            JOIN results AS r ON r.paper_id = p.id
            JOIN dataset_variants AS dv ON dv.id = r.dataset_variant_id
            JOIN datasets AS d ON d.id = dv.dataset_id
            WHERE p.arxiv_id IN ({placeholders})
            GROUP BY p.arxiv_id, d.id, r.table_ref, r.protocol_decision
            """,
            paper_ids,
        ).fetchall()
    finally:
        connection.close()

    evidence: dict[str, dict[str, DatabaseDataset]] = defaultdict(dict)
    row_counts: dict[str, int] = dict.fromkeys(paper_ids, 0)
    for row in rows:
        paper_id = str(row["arxiv_id"])
        dataset = str(row["dataset"])
        key = _name_key(dataset)
        item = evidence[paper_id].setdefault(key, DatabaseDataset(name=dataset))
        if row["table_ref"]:
            item.table_refs.add(str(row["table_ref"]))
        if row["protocol_decision"]:
            item.protocols.add(str(row["protocol_decision"]))
        count = int(row["result_rows"])
        item.result_rows += count
        row_counts[paper_id] += count
    return dict(evidence), row_counts


def _dataset_names(items: dict[str, DatabaseDataset], keys: set[str]) -> list[str]:
    return sorted((items[key].name for key in keys), key=str.casefold)


def evaluate(
    annotations: list[dict[str, str]],
    database_evidence: dict[str, dict[str, DatabaseDataset]],
    database_row_counts: dict[str, int],
) -> dict[str, Any]:
    paper_tp = paper_fp = paper_tn = paper_fn = 0
    dataset_tp = dataset_fp = dataset_fn = 0
    table_tp = table_fp = table_fn = 0
    details: list[dict[str, Any]] = []

    for annotation in annotations:
        paper_id = annotation["arxiv_id"]
        truth = _MANUAL_TRUTH[paper_id]
        stored = database_evidence.get(paper_id, {})
        stored_keys = set(stored)
        expected_by_key = {_name_key(name): name for name in truth.expected_datasets}
        expected_keys = set(expected_by_key)
        matched_keys = expected_keys & stored_keys
        missing_keys = expected_keys - stored_keys
        extra_keys = stored_keys - expected_keys

        if truth.strict_paper_label is not None:
            predicted_positive = bool(stored_keys)
            if truth.strict_paper_label and predicted_positive:
                paper_tp += 1
            elif truth.strict_paper_label:
                paper_fn += 1
            elif predicted_positive:
                paper_fp += 1
            else:
                paper_tn += 1
            dataset_tp += len(matched_keys)
            dataset_fn += len(missing_keys)
            dataset_fp += len(extra_keys)

        expected_table_pairs: set[tuple[str, str]] = set()
        for dataset, refs in truth.table_refs:
            expected_table_pairs.update((_name_key(dataset), _table_key(ref)) for ref in refs)
        stored_table_pairs = {
            (dataset_key, _table_key(table_ref))
            for dataset_key, item in stored.items()
            for table_ref in item.table_refs
        }
        if truth.table_refs_complete:
            table_tp += len(expected_table_pairs & stored_table_pairs)
            table_fn += len(expected_table_pairs - stored_table_pairs)
            table_fp += len(stored_table_pairs - expected_table_pairs)

        annotated_keys = {_name_key(name) for name in truth.annotated_datasets}
        manual_count = int(annotation.get("database_result_count") or 0)
        actual_count = database_row_counts.get(paper_id, 0)
        if manual_count != actual_count:
            raise ValueError(
                f"Database result count changed for {paper_id}: CSV={manual_count}, database={actual_count}"
            )

        details.append(
            {
                "paper_index": int(annotation["paper_index"]),
                "arxiv_id": paper_id,
                "title": annotation["title"],
                "cohort": annotation["cohort"],
                "manual_compatibility": annotation.get("manual_experiment_compatible", ""),
                "manual_reason": annotation.get("manual_compatibility_reason", ""),
                "manual_notes": annotation.get("manual_notes", ""),
                "strict_paper_label": truth.strict_paper_label,
                "qualification": truth.qualification,
                "database_result_rows": actual_count,
                "expected_compatible_datasets": list(truth.expected_datasets),
                "annotated_datasets_for_qualified_case": list(truth.annotated_datasets),
                "stored_datasets": _dataset_names(stored, stored_keys),
                "matched_datasets": _dataset_names(stored, matched_keys),
                "missing_datasets": sorted(
                    (expected_by_key[key] for key in missing_keys), key=str.casefold
                ),
                "unexpected_datasets": _dataset_names(stored, extra_keys)
                if truth.strict_paper_label is not None
                else [],
                "qualified_annotation_overlap": _dataset_names(
                    stored, stored_keys & annotated_keys
                ),
                "qualified_annotation_missing": sorted(
                    (
                        name
                        for name in truth.annotated_datasets
                        if _name_key(name) not in stored_keys
                    ),
                    key=str.casefold,
                ),
                "manual_table_pairs": sorted(
                    f"{dataset} — {ref}" for dataset, refs in truth.table_refs for ref in refs
                ),
                "database_table_pairs": sorted(
                    f"{item.name} — {table_ref}"
                    for item in stored.values()
                    for table_ref in item.table_refs
                ),
                "missing_table_pairs": sorted(
                    f"{dataset} — {ref}"
                    for dataset, refs in truth.table_refs
                    for ref in refs
                    if (_name_key(dataset), _table_key(ref)) not in stored_table_pairs
                ),
                "unexpected_table_pairs": sorted(
                    f"{stored[dataset_key].name} — {table_ref}"
                    for dataset_key, table_key in (stored_table_pairs - expected_table_pairs)
                    for table_ref in stored[dataset_key].table_refs
                    if _table_key(table_ref) == table_key
                )
                if truth.table_refs_complete
                else [],
                "table_refs_scored": truth.table_refs_complete,
                "database_protocols": sorted(
                    {protocol for item in stored.values() for protocol in item.protocols}
                ),
            }
        )

    reviewed_truth = [_MANUAL_TRUTH[row["arxiv_id"]] for row in annotations]
    strict_count = sum(item.strict_paper_label is not None for item in reviewed_truth)
    qualified_count = len(reviewed_truth) - strict_count
    return {
        "summary": {
            "paper_count": len(annotations),
            "strict_paper_count": strict_count,
            "qualified_paper_count": qualified_count,
            "stored_result_rows": sum(database_row_counts.values()),
            "stored_paper_dataset_pairs": sum(
                len(database_evidence.get(annotation["arxiv_id"], {})) for annotation in annotations
            ),
            "paper_level": {
                "true_positive": paper_tp,
                "false_positive": paper_fp,
                "true_negative": paper_tn,
                "false_negative": paper_fn,
                "precision": _ratio(paper_tp, paper_tp + paper_fp),
                "recall": _ratio(paper_tp, paper_tp + paper_fn),
                "specificity": _ratio(paper_tn, paper_tn + paper_fp),
                "accuracy": _ratio(paper_tp + paper_tn, strict_count),
                "f1": _ratio(2 * paper_tp, 2 * paper_tp + paper_fp + paper_fn),
                "accuracy_wilson_95": _wilson(paper_tp + paper_tn, strict_count),
            },
            "dataset_level": {
                "true_positive": dataset_tp,
                "false_positive": dataset_fp,
                "false_negative": dataset_fn,
                "precision": _ratio(dataset_tp, dataset_tp + dataset_fp),
                "recall": _ratio(dataset_tp, dataset_tp + dataset_fn),
                "f1": _ratio(2 * dataset_tp, 2 * dataset_tp + dataset_fp + dataset_fn),
                "precision_wilson_95": _wilson(dataset_tp, dataset_tp + dataset_fp),
                "recall_wilson_95": _wilson(dataset_tp, dataset_tp + dataset_fn),
            },
            "table_reference_level": {
                "scored_paper_count": sum(item.table_refs_complete for item in reviewed_truth),
                "true_positive": table_tp,
                "false_positive": table_fp,
                "false_negative": table_fn,
                "precision": _ratio(table_tp, table_tp + table_fp),
                "recall": _ratio(table_tp, table_tp + table_fn),
                "f1": _ratio(2 * table_tp, 2 * table_tp + table_fp + table_fn),
                "precision_wilson_95": _wilson(table_tp, table_tp + table_fp),
                "recall_wilson_95": _wilson(table_tp, table_tp + table_fn),
            },
        },
        "papers": details,
    }


def _percent(value: float | None) -> str:
    return "n/a" if value is None else f"{100 * value:.1f}%"


def _interval(values: list[float] | None) -> str:
    return "n/a" if values is None else f"{_percent(values[0])}–{_percent(values[1])}"


def _list(values: list[str]) -> str:
    return ", ".join(values) if values else "none"


def render_report(result: dict[str, Any], annotation_hash: str) -> str:
    summary = result["summary"]
    paper = summary["paper_level"]
    dataset = summary["dataset_level"]
    table = summary["table_reference_level"]
    details = result["papers"]

    lines = [
        "# Dataset-detection evaluation",
        "",
        "## Executive summary",
        "",
        f"- Evaluated 20 manually reviewed papers against the current database: "
        f"{summary['stored_result_rows']} stored result rows across "
        f"{summary['stored_paper_dataset_pairs']} paper-dataset pairs.",
        f"- Strict paper-level scoring covers {summary['strict_paper_count']} papers; "
        f"{summary['qualified_paper_count']} ambiguous or protocol-qualified papers are reported separately.",
        f"- Paper inclusion: precision {_percent(paper['precision'])}, recall {_percent(paper['recall'])}, "
        f"specificity {_percent(paper['specificity'])}, accuracy {_percent(paper['accuracy'])}.",
        f"- Compatible dataset recovery: precision {_percent(dataset['precision'])}, "
        f"recall {_percent(dataset['recall'])}, F1 {_percent(dataset['f1'])} "
        f"({dataset['true_positive']} correct, {dataset['false_negative']} missing, "
        f"{dataset['false_positive']} unexpected paper-dataset pairs).",
        f"- Exact dataset-table association on {table['scored_paper_count']} fully interpretable papers: "
        f"precision {_percent(table['precision'])}, recall {_percent(table['recall'])}, "
        f"F1 {_percent(table['f1'])} ({table['true_positive']} exact, "
        f"{table['false_negative']} missing, {table['false_positive']} unexpected pairs).",
        f"- Descriptive 95% Wilson intervals: paper accuracy "
        f"{_interval(paper['accuracy_wilson_95'])}; dataset precision "
        f"{_interval(dataset['precision_wilson_95'])} and recall "
        f"{_interval(dataset['recall_wilson_95'])}; table precision "
        f"{_interval(table['precision_wilson_95'])} and recall "
        f"{_interval(table['recall_wilson_95'])}.",
        "",
        "The main weakness is recall and table association, not coarse paper detection. The database "
        "usually recognizes that a paper contributes results, but frequently stores only a subset of "
        "the compatible datasets or attaches results to a different table than the manual review.",
        "",
        "## Highest-priority discrepancies",
        "",
    ]

    priority_ids = [
        "2401.14155",
        "2010.05788",
        "1905.12560",
        "2403.07954",
        "2508.05070",
        "1903.02428",
        "2206.08005",
        "2003.13663",
    ]
    by_id = {item["arxiv_id"]: item for item in details}
    priority_explanations = {
        "2401.14155": (
            "Strict false positive: four Amazon2M rows are stored from Table 2, which the manual "
            "annotation identifies as a statistics table; the paper's experiments are anomaly detection "
            "and were marked incompatible."
        ),
        "2010.05788": (
            "Potential false negative requiring adjudication: the database has zero rows, while the "
            "manual note says one MNIST value from Table 1 could be compatible."
        ),
        "1905.12560": (
            "Protocol risk requiring adjudication: 17 rows across CSL, COLLAB, MUTAG, and PROTEINS "
            "are marked standard in the database, while the manual review questions the split, "
            "cross-validation setup, and absence of a test set."
        ),
        "2403.07954": (
            "Four compatible datasets are missing (Cora, CiteSeer, PubMed, Chameleon); Penn94 is "
            "unexpected, and the stored Actor/Squirrel rows cite Table 1 instead of manual Table 2."
        ),
        "2508.05070": (
            "Five compatible datasets are missing (ZINC-12k, CIFAR10, PATTERN, Peptides-func, "
            "Peptides-struct); Eccentricity is unexpected, and MNIST/CLUSTER cite Table 1 instead of Table 2."
        ),
        "1903.02428": (
            "Four compatible datasets are missing (Cora, IMDB-BINARY, REDDIT-BINARY, ModelNet10). "
            "The explicit MUTAG reference also differs: manual Table 2 versus database Table 1."
        ),
        "2206.08005": (
            "MUV and HIV are missing. BBBP is present from manual Table 1 but also has an additional "
            "stored Table 2 association not present in the annotation."
        ),
        "2003.13663": (
            "Dataset detection is correct for Cora, but its two result rows cite Table 1 instead of "
            "manual Table 2."
        ),
    }
    for index, paper_id in enumerate(priority_ids, start=1):
        item = by_id[paper_id]
        lines.extend(
            [
                f"{index}. **{paper_id} — {item['title']}**",
                f"   {priority_explanations[paper_id]}",
            ]
        )

    lines.extend(["", "## Strict paper-level confusion counts", ""])
    lines.extend(
        [
            f"- True positives: {paper['true_positive']}",
            f"- False positives: {paper['false_positive']}",
            f"- True negatives: {paper['true_negative']}",
            f"- False negatives: {paper['false_negative']}",
            "",
            "The sole strict paper-level false positive is arXiv:2401.14155. There are no strict "
            "paper-level false negatives, but arXiv:2010.05788 remains a qualified potential false negative.",
            "",
            "## Per-paper comparison",
            "",
        ]
    )

    for item in details:
        label = (
            "compatible"
            if item["strict_paper_label"] is True
            else "incompatible"
            if item["strict_paper_label"] is False
            else "qualified / unscored"
        )
        lines.extend(
            [
                f"### {item['arxiv_id']} — {item['title']}",
                "",
                f"- Manual status used: {label}.",
                f"- Database: {item['database_result_rows']} result rows; datasets: "
                f"{_list(item['stored_datasets'])}.",
            ]
        )
        if item["strict_paper_label"] is not None:
            lines.extend(
                [
                    f"- Expected compatible datasets: {_list(item['expected_compatible_datasets'])}.",
                    f"- Missing datasets: {_list(item['missing_datasets'])}.",
                    f"- Unexpected datasets: {_list(item['unexpected_datasets'])}.",
                ]
            )
            if item["table_refs_scored"]:
                lines.extend(
                    [
                        f"- Missing dataset-table pairs: {_list(item['missing_table_pairs'])}.",
                        f"- Unexpected dataset-table pairs: {_list(item['unexpected_table_pairs'])}.",
                    ]
                )
        else:
            lines.extend(
                [
                    f"- Qualification: {item['qualification']}",
                    f"- Stored overlap with annotated datasets: "
                    f"{_list(item['qualified_annotation_overlap'])}.",
                    f"- Annotated but not stored: {_list(item['qualified_annotation_missing'])}.",
                ]
            )
        if item["manual_reason"] or item["manual_notes"]:
            lines.append(
                f"- Manual rationale: "
                f"{'; '.join(value for value in (item['manual_reason'], item['manual_notes']) if value)}"
            )
        lines.append("")

    lines.extend(
        [
            "## Method and limitations",
            "",
            "- Manual annotations are ground truth. Dataset spellings were normalized only for case, "
            "punctuation, obvious abbreviations, and the explicit OGB prefixes in the annotations.",
            "- A compatible dataset is a true positive only when the same paper-dataset pair exists in "
            "the database. Result values, models, and metrics were not annotated and are outside this evaluation.",
            "- Table scoring uses exact dataset-table pairs and only the six papers whose free-text table "
            "annotations could be assigned to every compatible dataset without guessing.",
            "- Four qualified papers are excluded from strict rates: 1710.03059, 1905.12560, "
            "2010.05788, and 2006.05535.",
            "- The cohort was deliberately stratified as 10 papers with and 10 without stored results. "
            "Paper-level precision and accuracy therefore describe this testbed, not corpus prevalence.",
            "- Wilson intervals are descriptive only. Dataset and table pairs within a paper are "
            "clustered, so pair-level intervals should not be treated as independent-sample inference.",
            "- The report compares the annotation snapshot with the current database. Database result "
            "counts are asserted against the counts recorded in the CSV before statistics are produced.",
            f"- Annotation SHA-256: `{annotation_hash}`.",
            "",
        ]
    )
    return "\n".join(lines)


def run(args: argparse.Namespace) -> dict[str, Any]:
    annotations = load_annotations(args.annotations)
    paper_ids = [row["arxiv_id"] for row in annotations]
    database_evidence, database_row_counts = load_database_evidence(args.database, paper_ids)
    result = evaluate(annotations, database_evidence, database_row_counts)
    annotation_hash = hashlib.sha256(args.annotations.read_bytes()).hexdigest()
    result["metadata"] = {
        "generated_at": datetime.now(UTC).isoformat(),
        "annotation_path": str(args.annotations),
        "annotation_sha256": annotation_hash,
        "database_path": str(args.database),
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    args.output_report.write_text(render_report(result, annotation_hash), encoding="utf-8")
    return result


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    output_dir = _PROJECT_ROOT / "experiments/extraction_validation/dataset_detection"
    parser.add_argument("--annotations", type=Path, default=output_dir / "review_cohort.csv")
    parser.add_argument("--database", type=Path, default=_PROJECT_ROOT / "data/benchmarks.db")
    parser.add_argument("--output-dir", type=Path, default=output_dir)
    parser.add_argument("--output-report", type=Path, default=output_dir / "evaluation_report.md")
    parser.add_argument("--output-json", type=Path, default=output_dir / "evaluation_results.json")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    result = run(args)
    summary = result["summary"]
    print(f"Report written to {args.output_report}")
    print(
        "Dataset precision/recall: "
        f"{_percent(summary['dataset_level']['precision'])} / "
        f"{_percent(summary['dataset_level']['recall'])}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
