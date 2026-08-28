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
from collections.abc import Iterable
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


def _natural_sort_key(value: str) -> tuple[tuple[int, str | int], ...]:
    """Sort names case-insensitively while treating embedded numbers numerically."""
    return tuple(
        (1, int(part)) if part.isdigit() else (0, part)
        for part in re.split(r"(\d+)", value.casefold())
        if part
    )


def _sorted_names(values: Iterable[str]) -> list[str]:
    return sorted(values, key=_natural_sort_key)


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
    return _sorted_names(items[key].name for key in keys)


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
                "expected_compatible_datasets": _sorted_names(truth.expected_datasets),
                "annotated_datasets_for_qualified_case": _sorted_names(truth.annotated_datasets),
                "stored_datasets": _dataset_names(stored, stored_keys),
                "matched_datasets": _dataset_names(stored, matched_keys),
                "missing_datasets": _sorted_names(expected_by_key[key] for key in missing_keys),
                "unexpected_datasets": _dataset_names(stored, extra_keys)
                if truth.strict_paper_label is not None
                else [],
                "qualified_annotation_overlap": _dataset_names(
                    stored, stored_keys & annotated_keys
                ),
                "qualified_annotation_missing": _sorted_names(
                    name for name in truth.annotated_datasets if _name_key(name) not in stored_keys
                ),
                "manual_table_pairs": _sorted_names(
                    f"{dataset} — {ref}" for dataset, refs in truth.table_refs for ref in refs
                ),
                "database_table_pairs": _sorted_names(
                    f"{item.name} — {table_ref}"
                    for item in stored.values()
                    for table_ref in item.table_refs
                ),
                "missing_table_pairs": _sorted_names(
                    f"{dataset} — {ref}"
                    for dataset, refs in truth.table_refs
                    for ref in refs
                    if (_name_key(dataset), _table_key(ref)) not in stored_table_pairs
                ),
                "unexpected_table_pairs": _sorted_names(
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


def _discrepancy_checkboxes(item: dict[str, Any]) -> list[str]:
    """Render editable checks with the evaluated system named explicitly."""
    lines = ["", "#### Discrepancy checks", ""]
    checkbox_count = 0
    if item["strict_paper_label"] is not None:
        for value in item["missing_datasets"]:
            lines.append(
                f"- [ ] **Candidate LLM false negative — paper-dataset pair:** `{value}`. "
                "Manual reference: compatible and present. LLM/database output: absent. "
                "Adjudication:"
            )
            checkbox_count += 1
        for value in item["unexpected_datasets"]:
            lines.append(
                f"- [ ] **Candidate LLM false positive — paper-dataset pair:** `{value}`. "
                "Manual reference: absent or incompatible. LLM/database output: present. "
                "Adjudication:"
            )
            checkbox_count += 1
        if item["table_refs_scored"]:
            for value in item["missing_table_pairs"]:
                lines.append(
                    f"- [ ] **Candidate LLM false negative — dataset-table pair:** `{value}`. "
                    "Manual reference: present. LLM/database output: absent. Adjudication:"
                )
                checkbox_count += 1
            for value in item["unexpected_table_pairs"]:
                lines.append(
                    f"- [ ] **Candidate LLM false positive — dataset-table pair:** `{value}`. "
                    "Manual reference: absent. LLM/database output: present. Adjudication:"
                )
                checkbox_count += 1
        elif item["missing_table_pairs"]:
            for value in item["missing_table_pairs"]:
                lines.append(
                    f"- [ ] **Unscored manual-only dataset-table pair:** `{value}`. "
                    "The free-text manual mapping was incomplete, so this does not affect the reported "
                    "LLM table precision or recall. Adjudication:"
                )
                checkbox_count += 1
    else:
        for value in item["qualified_annotation_missing"]:
            lines.append(
                f"- [ ] **Unscored manual-only paper-dataset pair:** `{value}`. "
                "The manual compatibility judgment was qualified, so this is not counted as an LLM "
                "false negative. Adjudication:"
            )
            checkbox_count += 1
    if not checkbox_count:
        lines.append("- No manual–LLM dataset or table discrepancy to adjudicate.")
    return lines


def _perfect_match_message(item: dict[str, Any]) -> str | None:
    """Return a prominent description only for fully comparable exact matches."""
    if item["strict_paper_label"] is None:
        return None
    if item["missing_datasets"] or item["unexpected_datasets"]:
        return None
    if item["table_refs_scored"]:
        if item["missing_table_pairs"] or item["unexpected_table_pairs"]:
            return None
        return (
            "**Perfect manual–LLM match:** The LLM/database output agrees with the manual "
            "reference on paper inclusion, compatible datasets, and every scored dataset-table pair."
        )
    if item["manual_table_pairs"] or item["database_table_pairs"]:
        return None
    return (
        "**Perfect manual–LLM match:** The manual reference contains no compatible dataset result, "
        "and the LLM/database output correctly stores none."
    )


def render_report(result: dict[str, Any], annotation_hash: str) -> str:
    summary = result["summary"]
    paper = summary["paper_level"]
    dataset = summary["dataset_level"]
    table = summary["table_reference_level"]
    details = result["papers"]

    lines = [
        "# Evaluation of LLM dataset extraction against manual annotations",
        "",
        "> **Reference standard:** the manual annotations.  ",
        "> **System being evaluated:** the LLM-derived extraction represented by the current database.  ",
        "> **Important:** precision and recall below measure the LLM/database output, not the human reviewer.",
        "",
        "Operationally, “LLM/database output” means an LLM-extracted result that survived downstream "
        "normalization and protocol filtering and is currently stored. A discrepancy can therefore be "
        "caused by the LLM itself or by later pipeline handling, but it is always counted against the "
        "end-to-end LLM extraction outcome—not against the manual annotation.",
        "",
        "## Metric definitions",
        "",
        "- **LLM precision** = manually confirmed LLM-positive items / all LLM-positive items.",
        "- **LLM recall** = manually annotated positive items recovered by the LLM/database / all "
        "manual positive items.",
        "- **Candidate LLM false negative (missing)** = present in the manual reference but absent "
        "from the LLM/database output.",
        "- **Candidate LLM false positive (unexpected)** = present in the LLM/database output but "
        "absent or incompatible in the manual reference.",
        "- “Candidate” means the item still needs the requested manual double-check. Each candidate "
        "has an editable checkbox below.",
        "",
        "## Executive summary",
        "",
        f"- **LLM/database output:** {summary['stored_result_rows']} stored result rows across "
        f"{summary['stored_paper_dataset_pairs']} paper-dataset pairs for the 20 reviewed papers. "
        "The manual annotations do not contain result-row counts.",
        f"- **Manual reference:** {summary['strict_paper_count']} papers have strict compatible/incompatible "
        f"labels; {summary['qualified_paper_count']} ambiguous or protocol-qualified manual judgments are "
        "reported but excluded from strict LLM metrics.",
        f"- **LLM paper-inclusion performance:** precision {_percent(paper['precision'])}, "
        f"recall {_percent(paper['recall'])}, "
        f"specificity {_percent(paper['specificity'])}, accuracy {_percent(paper['accuracy'])}.",
        f"- **LLM compatible-dataset performance:** precision {_percent(dataset['precision'])}, "
        f"recall {_percent(dataset['recall'])}, F1 {_percent(dataset['f1'])} "
        f"({dataset['true_positive']} manual–LLM matches; {dataset['false_negative']} manual-only candidate "
        f"LLM false negatives; {dataset['false_positive']} LLM-only candidate false positives). "
        f"The manual reference contains {dataset['true_positive'] + dataset['false_negative']} positive "
        f"paper-dataset pairs; the LLM/database returned "
        f"{dataset['true_positive'] + dataset['false_positive']} positive pairs.",
        f"- **LLM exact dataset-table performance** on {table['scored_paper_count']} fully interpretable "
        f"papers: "
        f"precision {_percent(table['precision'])}, recall {_percent(table['recall'])}, "
        f"F1 {_percent(table['f1'])} ({table['true_positive']} manual–LLM matches; "
        f"{table['false_negative']} manual-only candidate LLM false negatives; "
        f"{table['false_positive']} LLM-only candidate false positives). "
        f"The manual reference contains {table['true_positive'] + table['false_negative']} positive "
        f"dataset-table pairs; the LLM/database returned "
        f"{table['true_positive'] + table['false_positive']} positive pairs.",
        f"- Descriptive 95% Wilson intervals: paper accuracy "
        f"{_interval(paper['accuracy_wilson_95'])}; dataset precision "
        f"{_interval(dataset['precision_wilson_95'])} and recall "
        f"{_interval(dataset['recall_wilson_95'])}; table precision "
        f"{_interval(table['precision_wilson_95'])} and recall "
        f"{_interval(table['recall_wilson_95'])}.",
        "",
        "The LLM's main weakness in this testbed is recall and table association, not coarse paper "
        "detection. Relative to the manual reference, the LLM/database usually identifies that a paper "
        "contributes results, but frequently returns only a subset of the compatible datasets or attaches "
        "results to a different table.",
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
            "Candidate LLM false positive: the LLM/database contains four Amazon2M rows from Table 2. "
            "The manual reference identifies Table 2 as a statistics table and marks the anomaly-detection "
            "experiments incompatible."
        ),
        "2010.05788": (
            "Potential LLM false negative requiring adjudication: the LLM/database has zero rows, while "
            "the qualified manual note says one MNIST value from Table 1 could be compatible."
        ),
        "1905.12560": (
            "Potential LLM/downstream protocol false positives: the LLM/database marks 17 rows across "
            "COLLAB, CSL, MUTAG, and PROTEINS as standard, while the manual reference questions the split, "
            "cross-validation setup, and absence of a test set."
        ),
        "2403.07954": (
            "Candidate LLM false negatives: four manual-compatible datasets are absent (Chameleon, "
            "CiteSeer, Cora, PubMed). Candidate LLM false positives: Penn94 and the LLM Table 1 associations "
            "for Actor/Squirrel, where the manual reference says Table 2."
        ),
        "2508.05070": (
            "Candidate LLM false negatives: five manual-compatible datasets are absent (CIFAR10, "
            "PATTERN, Peptides-func, Peptides-struct, ZINC-12k). Candidate LLM false positives: "
            "Eccentricity and LLM Table 1 associations for CLUSTER/MNIST, where the manual reference says Table 2."
        ),
        "1903.02428": (
            "Candidate LLM false negatives: four manual-compatible datasets are absent (Cora, "
            "IMDB-BINARY, ModelNet10, REDDIT-BINARY). The explicit table reference also differs: "
            "manual MUTAG Table 2 versus LLM/database Table 1."
        ),
        "2206.08005": (
            "Candidate LLM false negatives: manual-compatible MUV and HIV are absent. Candidate LLM "
            "false positive: BBBP has an additional LLM/database Table 2 association absent from the "
            "manual reference."
        ),
        "2003.13663": (
            "The manual and LLM agree on Cora, but the manual reference says Table 2 while the "
            "LLM/database stores the two result rows as Table 1."
        ),
    }
    available_priority_ids = [paper_id for paper_id in priority_ids if paper_id in by_id]
    for index, paper_id in enumerate(available_priority_ids, start=1):
        item = by_id[paper_id]
        lines.extend(
            [
                f"{index}. **{paper_id} — {item['title']}**",
                f"   {priority_explanations[paper_id]}",
            ]
        )

    lines.extend(["", "## Strict LLM paper-level confusion counts", ""])
    lines.extend(
        [
            f"- LLM true positives relative to the manual reference: {paper['true_positive']}",
            f"- LLM false positives relative to the manual reference: {paper['false_positive']}",
            f"- LLM true negatives relative to the manual reference: {paper['true_negative']}",
            f"- LLM false negatives relative to the manual reference: {paper['false_negative']}",
            "",
            "The sole strict LLM paper-level false positive candidate is arXiv:2401.14155. There are no "
            "strict LLM paper-level false negatives, but arXiv:2010.05788 remains a qualified potential "
            "LLM false negative.",
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
        lines.extend([f"### {item['arxiv_id']} — {item['title']}", ""])
        if perfect_match := _perfect_match_message(item):
            lines.extend([perfect_match, ""])
        lines.extend(
            [
                f"- **Manual reference status:** {label}.",
                f"- **LLM/database output:** {item['database_result_rows']} stored result rows; datasets: "
                f"{_list(item['stored_datasets'])}.",
            ]
        )
        if item["strict_paper_label"] is not None:
            lines.extend(
                [
                    f"- **Manual compatible datasets:** "
                    f"{_list(item['expected_compatible_datasets'])}.",
                    f"- **Manual–LLM dataset matches:** {_list(item['matched_datasets'])}.",
                    f"- **Manual-only datasets (candidate LLM false negatives):** "
                    f"{_list(item['missing_datasets'])}.",
                    f"- **LLM-only datasets (candidate LLM false positives):** "
                    f"{_list(item['unexpected_datasets'])}.",
                ]
            )
            if item["table_refs_scored"]:
                lines.extend(
                    [
                        f"- **Manual dataset-table pairs:** {_list(item['manual_table_pairs'])}.",
                        f"- **LLM/database dataset-table pairs:** "
                        f"{_list(item['database_table_pairs'])}.",
                        f"- **Manual-only table pairs (candidate LLM false negatives):** "
                        f"{_list(item['missing_table_pairs'])}.",
                        f"- **LLM-only table pairs (candidate LLM false positives):** "
                        f"{_list(item['unexpected_table_pairs'])}.",
                    ]
                )
        else:
            lines.extend(
                [
                    f"- **Why this manual judgment is unscored:** {item['qualification']}",
                    f"- **LLM/database overlap with manually named datasets:** "
                    f"{_list(item['qualified_annotation_overlap'])}.",
                    f"- **Manual-only named datasets (not counted as LLM false negatives):** "
                    f"{_list(item['qualified_annotation_missing'])}.",
                ]
            )
        if item["manual_reason"] or item["manual_notes"]:
            lines.append(
                f"- **Manual rationale:** "
                f"{'; '.join(value for value in (item['manual_reason'], item['manual_notes']) if value)}"
            )
        lines.extend(_discrepancy_checkboxes(item))
        lines.append("")

    lines.extend(
        [
            "## Method and limitations",
            "",
            "- The human manual annotations are the reference standard; the evaluated predictions are "
            "the LLM-derived database contents. Dataset spellings were normalized only for case, "
            "punctuation, obvious abbreviations, and the explicit OGB prefixes in the annotations.",
            "- Dataset names and dataset-table pairs are displayed in case-insensitive natural "
            "alphabetical order throughout the report.",
            "- An LLM true positive requires the same positive paper-dataset or dataset-table pair in the "
            "manual reference and LLM/database output. Result values, models, and metrics were not manually "
            "annotated and are outside this evaluation.",
            "- Table scoring uses exact dataset-table pairs and only the six papers whose free-text table "
            "annotations could be assigned to every compatible dataset without guessing.",
            "- Four qualified papers are excluded from strict rates: 1710.03059, 1905.12560, "
            "2010.05788, and 2006.05535.",
            "- The cohort was deliberately stratified as 10 papers with and 10 without stored results. "
            "LLM paper-level precision and accuracy therefore describe this testbed, not corpus prevalence.",
            "- Wilson intervals are descriptive only. Dataset and table pairs within a paper are "
            "clustered, so pair-level intervals should not be treated as independent-sample inference.",
            "- The report compares the annotation snapshot with the current database. Database result "
            "counts are asserted against the counts recorded in the CSV before statistics are produced.",
            "- This Markdown file is the adjudication surface. Editing its checkboxes or text does not "
            "change the CSV, database, or generated JSON. Rerunning `evaluate_review.py` overwrites this "
            "report, so incorporate completed adjudications into the evaluator before rerunning.",
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
        "LLM dataset precision/recall against manual reference: "
        f"{_percent(summary['dataset_level']['precision'])} / "
        f"{_percent(summary['dataset_level']['recall'])}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
