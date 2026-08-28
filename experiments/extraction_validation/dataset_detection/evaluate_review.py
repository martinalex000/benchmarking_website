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


@dataclass(frozen=True)
class ManualAdjudication:
    """Follow-up decision about discrepancies found in the first comparison."""

    summary: str
    confirms_dataset_discrepancies: bool = False
    confirms_table_discrepancies: bool = False


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
        True,
        ("Cora", "CiteSeer", "PubMed", "BlogCatalog", "POS", "PPI"),
        qualification="Compatibility was confirmed in manual follow-up; table mapping remains incomplete.",
    ),
    "2403.07954": ManualTruth(
        True,
        (
            "Cora",
            "CiteSeer",
            "PubMed",
            "Actor",
            "Chameleon",
            "Squirrel",
            "Penn94",
            "Genius",
            "ogbn-arxiv",
        ),
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
            ),
            ("Penn94", "Table 8"),
            ("Genius", "Table 8"),
            ("ogbn-arxiv", "Table 8"),
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
        True,
        (
            "CSL",
            "IMDB-BINARY",
            "IMDB-MULTI",
            "COLLAB",
            "MUTAG",
            "PTC",
            "PROTEINS",
        ),
        qualification="Compatibility was confirmed in manual follow-up; table mapping remains incomplete.",
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


_ADJUDICATIONS: dict[str, ManualAdjudication] = {
    "2003.13663": ManualAdjudication(
        "Confirmed: Cora results are in Table 2; Table 1 contains statistics only.",
        confirms_table_discrepancies=True,
    ),
    "2206.08005": ManualAdjudication(
        "Confirmed: the extraction discrepancies are real; HIV and MUV are nevertheless excluded "
        "from scoring because they are not tracked in the database catalog.",
        confirms_dataset_discrepancies=True,
        confirms_table_discrepancies=True,
    ),
    "2401.14155": ManualAdjudication(
        "Confirmed: the paper uses a different Amazon dataset version, not Amazon2M.",
        confirms_dataset_discrepancies=True,
    ),
    "1903.02428": ManualAdjudication(
        "Confirmed: despite the older non-standard benchmarking setup, the manually listed datasets "
        "are compatible and the LLM missed the reported subset. ModelNet10 is untracked and excluded "
        "from scoring.",
        confirms_dataset_discrepancies=True,
    ),
    "1710.03059": ManualAdjudication(
        "Confirmed: the manually identified datasets are compatible. BlogCatalog and POS are genuine "
        "extraction misses but are untracked and therefore excluded from scoring.",
        confirms_dataset_discrepancies=True,
    ),
    "2403.07954": ManualAdjudication(
        "Confirmed: Table 1 contains statistics, Table 2 contains the main results, and Table 8 adds "
        "Genius, ogbn-arxiv, and Penn94. Genius is untracked and excluded from scoring.",
        confirms_dataset_discrepancies=True,
        confirms_table_discrepancies=True,
    ),
    "2508.05070": ManualAdjudication(
        "Confirmed: Table 1 contains untracked synthetic graphs; CLUSTER and MNIST results are not in "
        "Table 1, and the manual table assignments are correct.",
        confirms_dataset_discrepancies=True,
        confirms_table_discrepancies=True,
    ),
    "1905.12560": ManualAdjudication(
        "Confirmed: the 10-fold cross-validation setup was conventional for the period, so the listed "
        "datasets are compatible. PTC is untracked and excluded from scoring.",
        confirms_dataset_discrepancies=True,
    ),
}


def _name_key(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.casefold())


_CATALOG_SCOPE_ALIASES = {
    # The catalog stores the logical dataset as ZINC and the 12k subset as a variant.
    "zinc12k": "zinc",
}


def _catalog_key(value: str) -> str:
    key = _name_key(value)
    return _CATALOG_SCOPE_ALIASES.get(key, key)


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
) -> tuple[dict[str, dict[str, DatabaseDataset]], dict[str, int], set[str]]:
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
        tracked_dataset_keys = {
            _catalog_key(str(row["name"]))
            for row in connection.execute("SELECT name FROM datasets").fetchall()
        }
    finally:
        connection.close()

    evidence: dict[str, dict[str, DatabaseDataset]] = defaultdict(dict)
    row_counts: dict[str, int] = dict.fromkeys(paper_ids, 0)
    for row in rows:
        paper_id = str(row["arxiv_id"])
        dataset = str(row["dataset"])
        key = _catalog_key(dataset)
        item = evidence[paper_id].setdefault(key, DatabaseDataset(name=dataset))
        if row["table_ref"]:
            item.table_refs.add(str(row["table_ref"]))
        if row["protocol_decision"]:
            item.protocols.add(str(row["protocol_decision"]))
        count = int(row["result_rows"])
        item.result_rows += count
        row_counts[paper_id] += count
    return dict(evidence), row_counts, tracked_dataset_keys


def _dataset_names(items: dict[str, DatabaseDataset], keys: set[str]) -> list[str]:
    return _sorted_names(items[key].name for key in keys)


def evaluate(
    annotations: list[dict[str, str]],
    database_evidence: dict[str, dict[str, DatabaseDataset]],
    database_row_counts: dict[str, int],
    tracked_dataset_keys: set[str] | None = None,
) -> dict[str, Any]:
    paper_tp = paper_fp = paper_tn = paper_fn = 0
    dataset_tp = dataset_fp = dataset_fn = 0
    table_tp = table_fp = table_fn = 0
    details: list[dict[str, Any]] = []

    for annotation in annotations:
        paper_id = annotation["arxiv_id"]
        truth = _MANUAL_TRUTH[paper_id]
        adjudication = _ADJUDICATIONS.get(paper_id)
        stored = database_evidence.get(paper_id, {})
        if tracked_dataset_keys is None:
            paper_tracked_keys = {
                *stored,
                *(_catalog_key(name) for name in truth.expected_datasets),
                *(_catalog_key(name) for name in truth.annotated_datasets),
            }
        else:
            paper_tracked_keys = tracked_dataset_keys
        scored_stored = {key: item for key, item in stored.items() if key in paper_tracked_keys}
        stored_keys = set(scored_stored)
        expected_by_key = {
            _catalog_key(name): name
            for name in truth.expected_datasets
            if _catalog_key(name) in paper_tracked_keys
        }
        excluded_expected_datasets = _sorted_names(
            name for name in truth.expected_datasets if _catalog_key(name) not in paper_tracked_keys
        )
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
            if _catalog_key(dataset) in paper_tracked_keys:
                expected_table_pairs.update(
                    (_catalog_key(dataset), _table_key(ref)) for ref in refs
                )
        stored_table_pairs = {
            (dataset_key, _table_key(table_ref))
            for dataset_key, item in scored_stored.items()
            for table_ref in item.table_refs
        }
        if truth.table_refs_complete:
            table_tp += len(expected_table_pairs & stored_table_pairs)
            table_fn += len(expected_table_pairs - stored_table_pairs)
            table_fp += len(stored_table_pairs - expected_table_pairs)

        annotated_by_key = {
            _catalog_key(name): name
            for name in truth.annotated_datasets
            if _catalog_key(name) in paper_tracked_keys
        }
        annotated_keys = set(annotated_by_key)
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
                "manual_adjudication": adjudication.summary if adjudication else "",
                "database_result_rows": actual_count,
                "expected_compatible_datasets": _sorted_names(expected_by_key.values()),
                "excluded_untracked_manual_datasets": excluded_expected_datasets,
                "annotated_datasets_for_qualified_case": _sorted_names(annotated_by_key.values()),
                "excluded_untracked_qualified_datasets": _sorted_names(
                    name
                    for name in truth.annotated_datasets
                    if _catalog_key(name) not in paper_tracked_keys
                ),
                "stored_datasets": _dataset_names(scored_stored, stored_keys),
                "excluded_untracked_stored_datasets": _dataset_names(
                    stored, set(stored) - stored_keys
                ),
                "matched_datasets": _dataset_names(scored_stored, matched_keys),
                "missing_datasets": _sorted_names(expected_by_key[key] for key in missing_keys),
                "unexpected_datasets": _dataset_names(scored_stored, extra_keys)
                if truth.strict_paper_label is not None
                else [],
                "qualified_annotation_overlap": _dataset_names(
                    scored_stored, stored_keys & annotated_keys
                ),
                "qualified_annotation_missing": _sorted_names(
                    name for key, name in annotated_by_key.items() if key not in stored_keys
                ),
                "manual_table_pairs": _sorted_names(
                    f"{dataset} — {ref}"
                    for dataset, refs in truth.table_refs
                    if _catalog_key(dataset) in paper_tracked_keys
                    for ref in refs
                ),
                "excluded_untracked_manual_table_pairs": _sorted_names(
                    f"{dataset} — {ref}"
                    for dataset, refs in truth.table_refs
                    if _catalog_key(dataset) not in paper_tracked_keys
                    for ref in refs
                ),
                "database_table_pairs": _sorted_names(
                    f"{item.name} — {table_ref}"
                    for item in scored_stored.values()
                    for table_ref in item.table_refs
                ),
                "missing_table_pairs": _sorted_names(
                    f"{dataset} — {ref}"
                    for dataset, refs in truth.table_refs
                    for ref in refs
                    if _catalog_key(dataset) in paper_tracked_keys
                    and (_catalog_key(dataset), _table_key(ref)) not in stored_table_pairs
                ),
                "unexpected_table_pairs": _sorted_names(
                    f"{scored_stored[dataset_key].name} — {table_ref}"
                    for dataset_key, table_key in (stored_table_pairs - expected_table_pairs)
                    for table_ref in scored_stored[dataset_key].table_refs
                    if _table_key(table_ref) == table_key
                )
                if truth.table_refs_complete
                else [],
                "table_refs_scored": truth.table_refs_complete,
                "database_protocols": sorted(
                    {protocol for item in scored_stored.values() for protocol in item.protocols}
                ),
            }
        )

    reviewed_truth = [_MANUAL_TRUTH[row["arxiv_id"]] for row in annotations]
    strict_count = sum(item.strict_paper_label is not None for item in reviewed_truth)
    qualified_count = len(reviewed_truth) - strict_count
    confirmed_dataset_fn = sum(
        len(item["missing_datasets"])
        for item in details
        if (adjudication := _ADJUDICATIONS.get(item["arxiv_id"]))
        and adjudication.confirms_dataset_discrepancies
    )
    confirmed_dataset_fp = sum(
        len(item["unexpected_datasets"])
        for item in details
        if (adjudication := _ADJUDICATIONS.get(item["arxiv_id"]))
        and adjudication.confirms_dataset_discrepancies
    )
    confirmed_table_fn = sum(
        len(item["missing_table_pairs"])
        for item in details
        if (adjudication := _ADJUDICATIONS.get(item["arxiv_id"]))
        and adjudication.confirms_table_discrepancies
    )
    confirmed_table_fp = sum(
        len(item["unexpected_table_pairs"])
        for item in details
        if (adjudication := _ADJUDICATIONS.get(item["arxiv_id"]))
        and adjudication.confirms_table_discrepancies
    )
    strict_excluded_dataset_pairs = sum(
        len(item["excluded_untracked_manual_datasets"])
        for item in details
        if item["strict_paper_label"] is not None
    )
    qualified_excluded_dataset_pairs = sum(
        len(item["excluded_untracked_qualified_datasets"])
        for item in details
        if item["strict_paper_label"] is None
    )
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
            "manual_adjudication": {
                "confirmed_dataset_false_negatives": confirmed_dataset_fn,
                "confirmed_dataset_false_positives": confirmed_dataset_fp,
                "confirmed_table_false_negatives": confirmed_table_fn,
                "confirmed_table_false_positives": confirmed_table_fp,
                "unresolved_dataset_discrepancies": (
                    dataset_fn + dataset_fp - confirmed_dataset_fn - confirmed_dataset_fp
                ),
                "unresolved_table_discrepancies": (
                    table_fn + table_fp - confirmed_table_fn - confirmed_table_fp
                ),
            },
            "tracking_scope": {
                "catalog_dataset_count": (
                    len(tracked_dataset_keys) if tracked_dataset_keys is not None else None
                ),
                "strict_manual_dataset_pairs_excluded": strict_excluded_dataset_pairs,
                "qualified_manual_dataset_pairs_excluded": qualified_excluded_dataset_pairs,
                "manual_table_pairs_excluded": sum(
                    len(item["excluded_untracked_manual_table_pairs"]) for item in details
                ),
                "stored_dataset_pairs_excluded": sum(
                    len(item["excluded_untracked_stored_datasets"]) for item in details
                ),
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


def _discrepancy_state(item: dict[str, Any], level: str) -> tuple[str, str]:
    adjudication = _ADJUDICATIONS.get(item["arxiv_id"])
    confirmed = bool(
        adjudication
        and (
            adjudication.confirms_dataset_discrepancies
            if level == "dataset"
            else adjudication.confirms_table_discrepancies
        )
    )
    return ("x", "Confirmed") if confirmed else (" ", "Candidate")


def _discrepancy_checkboxes(item: dict[str, Any]) -> list[str]:
    """Render editable checks with the evaluated system named explicitly."""
    lines = ["", "#### Discrepancy checks", ""]
    checkbox_count = 0
    if item["strict_paper_label"] is not None:
        dataset_check, dataset_status = _discrepancy_state(item, "dataset")
        table_check, table_status = _discrepancy_state(item, "table")
        dataset_suffix = (
            "Confirmed in manual follow-up." if dataset_status == "Confirmed" else "Adjudication:"
        )
        table_suffix = (
            "Confirmed in manual follow-up." if table_status == "Confirmed" else "Adjudication:"
        )
        for value in item["missing_datasets"]:
            lines.append(
                f"- [{dataset_check}] **{dataset_status} LLM false negative — paper-dataset pair:** "
                f"`{value}`. "
                "Manual reference: compatible and present. LLM/database output: absent. "
                f"{dataset_suffix}"
            )
            checkbox_count += 1
        for value in item["unexpected_datasets"]:
            lines.append(
                f"- [{dataset_check}] **{dataset_status} LLM false positive — paper-dataset pair:** "
                f"`{value}`. "
                "Manual reference: absent or incompatible. LLM/database output: present. "
                f"{dataset_suffix}"
            )
            checkbox_count += 1
        if item["table_refs_scored"]:
            for value in item["missing_table_pairs"]:
                lines.append(
                    f"- [{table_check}] **{table_status} LLM false negative — dataset-table pair:** "
                    f"`{value}`. "
                    "Manual reference: present. LLM/database output: absent. "
                    f"{table_suffix}"
                )
                checkbox_count += 1
            for value in item["unexpected_table_pairs"]:
                lines.append(
                    f"- [{table_check}] **{table_status} LLM false positive — dataset-table pair:** "
                    f"`{value}`. "
                    "Manual reference: absent. LLM/database output: present. "
                    f"{table_suffix}"
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
    adjudication = summary["manual_adjudication"]
    scope = summary["tracking_scope"]
    details = result["papers"]

    lines = [
        "# Evaluation of LLM dataset extraction against manual annotations",
        "",
        "> **Reference standard:** the manual annotations.  ",
        "> **System being evaluated:** the LLM-derived extraction represented by the current database.  ",
        "> **Important:** precision and recall below measure the LLM/database output, not the human reviewer.",
        "> **Scoring scope:** only datasets present in the database catalog; manually identified "
        "untracked datasets remain documented but do not affect any score.",
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
        "- **LLM false negative (missing)** = present in the manual reference but absent "
        "from the LLM/database output.",
        "- **LLM false positive (unexpected)** = present in the LLM/database output but "
        "absent or incompatible in the manual reference.",
        "- **Confirmed** means the discrepancy was resolved in manual follow-up; **candidate** means it "
        "still needs adjudication.",
        "",
        "## Executive summary",
        "",
        f"- **LLM/database output:** {summary['stored_result_rows']} stored result rows across "
        f"{summary['stored_paper_dataset_pairs']} paper-dataset pairs for the 20 reviewed papers. "
        "The manual annotations do not contain result-row counts.",
        f"- **Manual reference:** {summary['strict_paper_count']} papers have strict compatible/incompatible "
        f"labels; {summary['qualified_paper_count']} ambiguous or protocol-qualified manual judgments are "
        "reported but excluded from strict LLM metrics.",
        f"- **Tracked-dataset scope:** {scope['catalog_dataset_count']} catalog datasets. "
        f"{scope['strict_manual_dataset_pairs_excluded']} strict manual paper-dataset pairs and "
        f"{scope['manual_table_pairs_excluded']} manual dataset-table pairs were excluded as untracked; "
        f"the database contributed {scope['stored_dataset_pairs_excluded']} untracked stored pairs.",
        f"- **LLM paper-inclusion performance:** precision {_percent(paper['precision'])}, "
        f"recall {_percent(paper['recall'])}, "
        f"specificity {_percent(paper['specificity'])}, accuracy {_percent(paper['accuracy'])}.",
        f"- **LLM tracked-dataset performance:** precision {_percent(dataset['precision'])}, "
        f"recall {_percent(dataset['recall'])}, F1 {_percent(dataset['f1'])} "
        f"({dataset['true_positive']} manual–LLM matches; {dataset['false_negative']} manual-only "
        f"LLM false negatives; {dataset['false_positive']} LLM-only false positives). "
        f"The manual reference contains {dataset['true_positive'] + dataset['false_negative']} positive "
        f"paper-dataset pairs; the LLM/database returned "
        f"{dataset['true_positive'] + dataset['false_positive']} positive pairs.",
        f"- **LLM exact tracked-dataset-table performance** on {table['scored_paper_count']} fully interpretable "
        f"papers: "
        f"precision {_percent(table['precision'])}, recall {_percent(table['recall'])}, "
        f"F1 {_percent(table['f1'])} ({table['true_positive']} manual–LLM matches; "
        f"{table['false_negative']} manual-only LLM false negatives; "
        f"{table['false_positive']} LLM-only false positives). "
        f"The manual reference contains {table['true_positive'] + table['false_negative']} positive "
        f"dataset-table pairs; the LLM/database returned "
        f"{table['true_positive'] + table['false_positive']} positive pairs.",
        f"- Descriptive 95% Wilson intervals: paper accuracy "
        f"{_interval(paper['accuracy_wilson_95'])}; dataset precision "
        f"{_interval(dataset['precision_wilson_95'])} and recall "
        f"{_interval(dataset['recall_wilson_95'])}; table precision "
        f"{_interval(table['precision_wilson_95'])} and recall "
        f"{_interval(table['recall_wilson_95'])}.",
        f"- **Manual follow-up status:** all {dataset['false_negative'] + dataset['false_positive']} "
        f"strict tracked-dataset discrepancies are confirmed "
        f"({adjudication['confirmed_dataset_false_negatives']} "
        f"LLM false negatives and {adjudication['confirmed_dataset_false_positives']} LLM false positives); "
        f"unresolved: {adjudication['unresolved_dataset_discrepancies']}. All "
        f"{table['false_negative'] + table['false_positive']} scored tracked-dataset-table discrepancies are "
        f"confirmed ({adjudication['confirmed_table_false_negatives']} LLM false negatives and "
        f"{adjudication['confirmed_table_false_positives']} LLM false positives); unresolved: "
        f"{adjudication['unresolved_table_discrepancies']}.",
        "",
        "The LLM's main weakness in this testbed is recall and table association, not coarse paper "
        "detection. Relative to the manual reference, the LLM/database usually identifies that a paper "
        "contributes results, but frequently returns only a subset of the compatible datasets or attaches "
        "results to a different table.",
        "",
        "## Highest-priority findings",
        "",
    ]

    priority_ids = [
        "2401.14155",
        "2010.05788",
        "1905.12560",
        "1710.03059",
        "2403.07954",
        "2508.05070",
        "1903.02428",
        "2206.08005",
        "2003.13663",
    ]
    by_id = {item["arxiv_id"]: item for item in details}
    priority_explanations = {
        "2401.14155": (
            "Confirmed LLM false positive: the LLM/database labels four rows as Amazon2M, but the paper "
            "uses a different Amazon dataset version; its Table 2 contains statistics rather than "
            "compatible benchmark results."
        ),
        "2010.05788": (
            "Potential LLM false negative requiring adjudication: the LLM/database has zero rows, while "
            "the qualified manual note says one MNIST value from Table 1 could be compatible."
        ),
        "1905.12560": (
            "The manual follow-up accepts the period-typical 10-fold cross-validation protocol. COLLAB, "
            "CSL, MUTAG, and PROTEINS are therefore LLM true positives; IMDB-BINARY, IMDB-MULTI, and PTC "
            "were missed, but untracked PTC is excluded, leaving two scored LLM false negatives."
        ),
        "1710.03059": (
            "The manual follow-up confirms all six named datasets as compatible. The LLM recovered "
            "all four tracked datasets: CiteSeer, Cora, PPI, and PubMed. BlogCatalog and POS were missed "
            "but are untracked and excluded from the score."
        ),
        "2403.07954": (
            "Confirmed tracked-dataset LLM false negatives: Chameleon, CiteSeer, Cora, ogbn-arxiv, and "
            "PubMed. Untracked Genius is excluded. "
            "Penn94 is a true dataset match, but belongs to appendix Table 8 with Genius and ogbn-arxiv. "
            "The LLM's Table 1 associations are false positives because Table 1 contains statistics; "
            "Actor and Squirrel results are in Table 2."
        ),
        "2508.05070": (
            "Confirmed LLM false negatives: CIFAR10, PATTERN, Peptides-func, Peptides-struct, and "
            "ZINC-12k. Eccentricity is a confirmed LLM false positive because Table 1 contains untracked "
            "synthetic graphs; CLUSTER and MNIST are true dataset matches but their Table 1 associations "
            "are false positives."
        ),
        "1903.02428": (
            "Confirmed tracked-dataset LLM false negatives: Cora, IMDB-BINARY, and REDDIT-BINARY. "
            "ModelNet10 was also missed but is untracked and excluded. The explicit table reference differs: "
            "manual MUTAG Table 2 versus LLM/database Table 1."
        ),
        "2206.08005": (
            "HIV and MUV are genuine extraction misses but are untracked and excluded from scoring. "
            "The remaining confirmed tracked discrepancy is BBBP's additional LLM/database Table 2 "
            "association, which is absent from the manual reference."
        ),
        "2003.13663": (
            "The manual and LLM agree on Cora, but the confirmed result location is Table 2; Table 1 "
            "contains statistics only, so the LLM/database Table 1 association is false."
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
            "The sole strict LLM paper-level false positive is the manually confirmed arXiv:2401.14155. "
            "There are no "
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
                *(
                    [f"- **Manual follow-up adjudication:** {item['manual_adjudication']}"]
                    if item["manual_adjudication"]
                    else []
                ),
                f"- **LLM/database output:** {item['database_result_rows']} stored result rows; "
                f"tracked datasets: "
                f"{_list(item['stored_datasets'])}.",
                *(
                    [
                        f"- **Untracked LLM/database datasets (excluded):** "
                        f"{_list(item['excluded_untracked_stored_datasets'])}."
                    ]
                    if item["excluded_untracked_stored_datasets"]
                    else []
                ),
            ]
        )
        if item["strict_paper_label"] is not None:
            lines.extend(
                [
                    f"- **Manual tracked compatible datasets:** "
                    f"{_list(item['expected_compatible_datasets'])}.",
                    *(
                        [
                            f"- **Manual untracked datasets (excluded from scores):** "
                            f"{_list(item['excluded_untracked_manual_datasets'])}."
                        ]
                        if item["excluded_untracked_manual_datasets"]
                        else []
                    ),
                    f"- **Manual–LLM dataset matches:** {_list(item['matched_datasets'])}.",
                    f"- **Manual-only datasets (LLM false negatives):** "
                    f"{_list(item['missing_datasets'])}.",
                    f"- **LLM-only datasets (LLM false positives):** "
                    f"{_list(item['unexpected_datasets'])}.",
                ]
            )
            if item["table_refs_scored"]:
                lines.extend(
                    [
                        f"- **Manual tracked dataset-table pairs:** "
                        f"{_list(item['manual_table_pairs'])}.",
                        *(
                            [
                                f"- **Manual untracked dataset-table pairs (excluded from scores):** "
                                f"{_list(item['excluded_untracked_manual_table_pairs'])}."
                            ]
                            if item["excluded_untracked_manual_table_pairs"]
                            else []
                        ),
                        f"- **LLM/database dataset-table pairs:** "
                        f"{_list(item['database_table_pairs'])}.",
                        f"- **Manual-only table pairs (LLM false negatives):** "
                        f"{_list(item['missing_table_pairs'])}.",
                        f"- **LLM-only table pairs (LLM false positives):** "
                        f"{_list(item['unexpected_table_pairs'])}.",
                    ]
                )
        else:
            lines.extend(
                [
                    f"- **Why this manual judgment is unscored:** {item['qualification']}",
                    f"- **LLM/database overlap with manually named tracked datasets:** "
                    f"{_list(item['qualified_annotation_overlap'])}.",
                    f"- **Manual-only tracked datasets (unscored):** "
                    f"{_list(item['qualified_annotation_missing'])}.",
                    *(
                        [
                            f"- **Manually named untracked datasets (excluded):** "
                            f"{_list(item['excluded_untracked_qualified_datasets'])}."
                        ]
                        if item["excluded_untracked_qualified_datasets"]
                        else []
                    ),
                ]
            )
        if item["excluded_untracked_manual_table_pairs"] and not item["table_refs_scored"]:
            lines.append(
                f"- **Manual untracked dataset-table pairs (excluded from scores):** "
                f"{_list(item['excluded_untracked_manual_table_pairs'])}."
            )
        if item["manual_reason"] or item["manual_notes"]:
            rationale_label = (
                "Original manual rationale (before follow-up)"
                if item["manual_adjudication"]
                else "Manual rationale"
            )
            lines.append(
                f"- **{rationale_label}:** "
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
            "- Scores include only datasets present in the current `datasets` catalog table. Untracked "
            "manual datasets are retained in each paper section but excluded from TP, FP, FN, precision, "
            "recall, and table-pair counts. ZINC-12k resolves to the tracked ZINC subset variant.",
            "- Dataset names and dataset-table pairs are displayed in case-insensitive natural "
            "alphabetical order throughout the report.",
            "- An LLM true positive requires the same positive paper-dataset or dataset-table pair in the "
            "manual reference and LLM/database output. Result values, models, and metrics were not manually "
            "annotated and are outside this evaluation.",
            "- Table scoring uses exact dataset-table pairs and only the six papers whose free-text table "
            "annotations could be assigned to every compatible dataset without guessing.",
            "- Two qualified papers are excluded from strict rates: 2010.05788 and 2006.05535. "
            "Manual follow-up moved 1710.03059 and 1905.12560 into the strict compatible set.",
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
    database_evidence, database_row_counts, tracked_dataset_keys = load_database_evidence(
        args.database, paper_ids
    )
    result = evaluate(
        annotations,
        database_evidence,
        database_row_counts,
        tracked_dataset_keys,
    )
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
