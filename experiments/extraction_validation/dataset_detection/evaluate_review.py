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
from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from datetime import UTC, datetime
from math import sqrt
from pathlib import Path
from typing import Any

import yaml

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


@dataclass
class YamlDataset:
    """Raw dataset evidence from one paper's LLM output before database promotion."""

    names: set[str] = field(default_factory=set)
    result_rows: int = 0
    discovered_manifest: bool = False
    table_refs: set[str] = field(default_factory=set)
    protocols: set[str] = field(default_factory=set)
    extraction_note: str = ""
    coverage_assessment: str = ""


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
    # Supplemental dataset-only review from extraction-validation v3. The checked items in
    # manual_review_v3.md are treated as confirmed database positives; its explicit missing list
    # supplies the additional manual positives. Table assignments are intentionally unscored here.
    "2311.01038": ManualTruth(
        True,
        (
            "BACE",
            "BBBP",
            "ClinTox",
            "COLLAB",
            "IMDB-BINARY",
            "SIDER",
            "Tox21",
            "ToxCast",
            "Wisconsin",
            "Cornell",
            "Cora",
            "PubMed",
            "ogbn-arxiv",
            "ogbn-proteins",
            "IMDB-MULTI",
        ),
        qualification="Supplemental manual review; dataset detection only.",
    ),
    "2405.16435": ManualTruth(
        True,
        (
            "Chameleon",
            "CiteSeer",
            "Cora",
            "ogbl-collab",
            "ogbn-arxiv",
            "ogbn-products",
            "ogbn-proteins",
            "Pokec",
            "PubMed",
            "Questions",
            "Squirrel",
            "WikiCS",
            "Amazon-Computers",
            "Amazon-Photo",
            "Coauthor-CS",
            "Coauthor-Physics",
            "Amazon-ratings",
            "Peptides-func",
            "Peptides-struct",
        ),
        qualification="Supplemental manual review; dataset detection only.",
    ),
    "2506.04765": ManualTruth(
        True,
        (
            "Actor",
            "Chameleon",
            "CiteSeer",
            "Cora",
            "Cornell",
            "PubMed",
            "Squirrel",
            "Texas",
            "Wisconsin",
            "ogbg-molhiv",
            "ogbg-molpcba",
            "Peptides-func",
            "Peptides-struct",
            "ZINC",
        ),
        qualification="Supplemental manual review; dataset detection only.",
    ),
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
    "2311.01038": ManualAdjudication(
        "Confirmed from the supplemental manual review; the paper uses transfer-learning experiments, "
        "and the listed missing datasets were checked against the source. Untracked datasets are excluded.",
        confirms_dataset_discrepancies=True,
    ),
    "2405.16435": ManualAdjudication(
        "Confirmed from the supplemental manual review; seven manually listed datasets are not currently "
        "promoted to database rows.",
        confirms_dataset_discrepancies=True,
    ),
    "2506.04765": ManualAdjudication(
        "Confirmed from the supplemental manual review; five manually listed datasets are not currently "
        "promoted to database rows.",
        confirms_dataset_discrepancies=True,
    ),
}


_DATASET_FINDINGS: dict[str, tuple[tuple[str, str], ...]] = {
    "2003.13663": (
        (
            "Cora",
            "Tracked and correctly detected as a compatible dataset. The results are in Table 2; "
            "the LLM's Table 1 association is wrong because Table 1 contains statistics only.",
        ),
    ),
    "2206.08005": (
        ("BACE", "Tracked, compatible, and correctly recovered from Table 1."),
        (
            "BBBP",
            "Tracked and correctly recovered from Table 1; the additional LLM Table 2 association "
            "is a confirmed false positive.",
        ),
        ("ClinTox", "Tracked, compatible, and correctly recovered from Table 1."),
        ("HIV", "Compatible but missed by the LLM; untracked and excluded from scores."),
        ("MUV", "Compatible but missed by the LLM; untracked and excluded from scores."),
        ("SIDER", "Tracked, compatible, and correctly recovered from Table 1."),
        ("Tox21", "Tracked, compatible, and correctly recovered from Table 1."),
        ("ToxCast", "Tracked, compatible, and correctly recovered from Table 1."),
    ),
    "2401.14155": (
        (
            "Amazon2M",
            "Tracked in the catalog, but not the dataset version used by this paper. The earlier "
            "database snapshot stored Amazon2M rows; those rows are absent from the current database "
            "after manual removal.",
        ),
    ),
    "1903.02428": (
        ("CiteSeer", "Tracked, compatible, and recovered by the LLM; manually mapped to Table 1."),
        ("COLLAB", "Tracked, compatible, and recovered by the LLM."),
        ("Cora", "Tracked and compatible but missed by the LLM; manually mapped to Table 1."),
        ("IMDB-BINARY", "Tracked and compatible but missed by the LLM."),
        (
            "ModelNet10",
            "Compatible and manually mapped to Table 3, but missed by the LLM; untracked and excluded "
            "from scores.",
        ),
        (
            "MUTAG",
            "Tracked and recovered, but the manual reference places the result in Table 2 while the "
            "LLM/database uses Table 1. The paper's overall table mapping remains incomplete and unscored.",
        ),
        ("PROTEINS", "Tracked, compatible, and recovered by the LLM."),
        ("PubMed", "Tracked, compatible, and recovered by the LLM; manually mapped to Table 1."),
        ("REDDIT-BINARY", "Tracked and compatible but missed by the LLM."),
    ),
    "1710.03059": (
        ("BlogCatalog", "Compatible but missed by the LLM; untracked and excluded from scores."),
        ("CiteSeer", "Tracked, compatible, and recovered by the LLM."),
        ("Cora", "Tracked, compatible, and recovered by the LLM."),
        ("POS", "Compatible but missed by the LLM; untracked and excluded from scores."),
        ("PPI", "Tracked, compatible, and recovered by the LLM."),
        ("PubMed", "Tracked, compatible, and recovered by the LLM."),
    ),
    "2403.07954": (
        (
            "Actor",
            "Tracked and detected, but its results are in Table 2; the LLM Table 1 association is a "
            "confirmed table false positive.",
        ),
        ("Chameleon", "Tracked and compatible in Table 2 but missed by the LLM."),
        ("CiteSeer", "Tracked and compatible in Table 2 but missed by the LLM."),
        ("Cora", "Tracked and compatible in Table 2 but missed by the LLM."),
        (
            "Genius",
            "Compatible in appendix Table 8 but missed by the LLM; untracked and excluded from scores.",
        ),
        ("ogbn-arxiv", "Tracked and compatible in appendix Table 8 but missed by the LLM."),
        (
            "Penn94",
            "Tracked and detected, but its results are in appendix Table 8; the LLM Table 1 "
            "association is a confirmed table false positive.",
        ),
        ("PubMed", "Tracked and compatible in Table 2 but missed by the LLM."),
        (
            "Squirrel",
            "Tracked and detected, but its results are in Table 2; the LLM Table 1 association is a "
            "confirmed table false positive.",
        ),
    ),
    "2508.05070": (
        ("CIFAR10", "Tracked and compatible in Table 2 but missed by the LLM."),
        (
            "CLUSTER",
            "Tracked and detected, but its results are in Table 2 and definitely not Table 1; the LLM "
            "Table 1 association is a confirmed false positive.",
        ),
        (
            "Eccentricity",
            "Tracked in the catalog, but its stored association comes from Table 1's synthetic-graph "
            "experiments, which are outside this review's accepted results; counted as an LLM false positive.",
        ),
        (
            "MNIST",
            "Tracked and detected, but its results are in Table 2 and definitely not Table 1; the LLM "
            "Table 1 association is a confirmed false positive.",
        ),
        ("PATTERN", "Tracked and compatible in Table 2 but missed by the LLM."),
        ("Peptides-func", "Tracked and compatible in Table 3 but missed by the LLM."),
        ("Peptides-struct", "Tracked and compatible in Table 3 but missed by the LLM."),
        (
            "ZINC-12k",
            "Tracked as the ZINC subset variant; compatible in Table 2 but missed by the LLM.",
        ),
    ),
    "1905.12560": (
        ("COLLAB", "Tracked, compatible under the period-typical 10-fold protocol, and recovered."),
        ("CSL", "Tracked, compatible under the period-typical 10-fold protocol, and recovered."),
        (
            "IMDB-BINARY",
            "Tracked and compatible under the period-typical protocol, but missed by the LLM.",
        ),
        (
            "IMDB-MULTI",
            "Tracked and compatible under the period-typical protocol, but missed by the LLM.",
        ),
        ("MUTAG", "Tracked, compatible under the period-typical 10-fold protocol, and recovered."),
        (
            "PROTEINS",
            "Tracked, compatible under the period-typical 10-fold protocol, and recovered.",
        ),
        (
            "PTC",
            "Compatible under the period-typical protocol but missed by the LLM; untracked and "
            "excluded from scores.",
        ),
    ),
}


def _name_key(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.casefold())


_CATALOG_SCOPE_ALIASES = {
    # The catalog stores the logical dataset as ZINC and the 12k subset as a variant.
    "zinc12k": "zinc",
    "imdbb": "imdbbinary",
    "imdbm": "imdbmulti",
    "mnistsuperpixelgraph": "mnist",
    # Spellings used in the 2311.01038 paper and supplemental annotations.
    "imbdb": "imdbbinary",
    "ogbarxiv": "ogbnarxiv",
    "ogbproteins": "ogbnproteins",
}


_YAML_ARTIFACT_OVERRIDES = {
    # The database rows were rebuilt from this uncapped re-evaluation, rather than the older
    # top-level artifact left by the original extraction run.
    "2311.01038": Path("extracted/experiments/reeval-uncapped-2026-09-01/llm_output.yaml"),
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
    if len(ids) < 20 or len(set(ids)) != len(ids):
        raise ValueError("Expected at least 20 unique annotated papers")
    missing = sorted(set(ids) - _MANUAL_TRUTH.keys())
    stale = sorted(_MANUAL_TRUTH.keys() - set(ids))
    if missing or stale:
        raise ValueError(f"Manual adjudication is stale: missing={missing}, stale={stale}")
    return rows


def load_markdown_dataset_truth(path: Path, paper_id: str) -> ManualTruth | None:
    """Read checked and explicitly missing datasets for one paper from the review Markdown."""
    if not path.is_file():
        return None
    text = path.read_text(encoding="utf-8")
    paper_match = re.search(
        rf"^##\s+{re.escape(paper_id)}\b.*?(?=^##\s+|\Z)", text, flags=re.MULTILINE | re.DOTALL
    )
    if not paper_match:
        return None
    paper_section = paper_match.group(0)
    dataset_match = re.search(
        r"^###\s+Datasets currently in the database\s*(.*?)(?=^###\s+|\Z)",
        paper_section,
        flags=re.MULTILINE | re.DOTALL,
    )
    if not dataset_match:
        return None

    checked: list[str] = []
    for line in dataset_match.group(1).splitlines():
        match = re.match(r"\s*-\s*\[[xX]\]\s+(.+?)\s*(?:—|\(|$)", line)
        if match:
            checked.append(match.group(1).strip())

    missing: list[str] = []
    missing_match = re.search(
        r"^\*\*Missing datasets \(add names\):\*\*\s*(.*?)(?=^###\s+|\Z)",
        paper_section,
        flags=re.MULTILINE | re.DOTALL,
    )
    if missing_match:
        for line in missing_match.group(1).splitlines():
            value = line.strip()
            if not value.startswith("-"):
                continue
            value = value[1:].strip().strip("`")
            if not value:
                continue
            for item in re.split(r"[,;]", value):
                item = item.strip().strip("`")
                if item.casefold() == "peptides-func/struct":
                    missing.extend(("Peptides-func", "Peptides-struct"))
                elif item:
                    missing.append(item)

    names = list(dict.fromkeys((*checked, *missing)))
    if not names:
        raise ValueError(f"No dataset annotations found for {paper_id} in {path}")
    return ManualTruth(
        strict_paper_label=True,
        expected_datasets=tuple(names),
        qualification="Dataset detection reference read from manual_review_v3.md.",
    )


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


def load_yaml_dataset_evidence(
    papers_dir: Path, paper_ids: list[str]
) -> dict[str, dict[str, YamlDataset]]:
    """Read dataset names from raw YAML results before protocol/catalog promotion."""
    evidence: dict[str, dict[str, YamlDataset]] = defaultdict(dict)
    for paper_id in paper_ids:
        path = papers_dir / paper_id / "extracted" / "llm_output.yaml"
        if override := _YAML_ARTIFACT_OVERRIDES.get(paper_id):
            path = papers_dir / paper_id / override
        if not path.is_file():
            continue
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        if not isinstance(data, dict):
            continue
        results_section = data.get("results") or {}
        rows = results_section.get("results", []) if isinstance(results_section, dict) else []
        if not isinstance(rows, list):
            rows = []
        notes = str(results_section.get("extraction_notes") or "")
        coverage_assessment = str(results_section.get("coverage_assessment") or "").strip()
        note_by_key: dict[str, str] = {}
        for line in notes.splitlines():
            match = re.match(r"\s*\[([^\]]+)\]\s*(.*)", line)
            if match:
                note_by_key.setdefault(_catalog_key(match.group(1)), line.strip())
        for row in rows:
            if not isinstance(row, dict) or not row.get("dataset"):
                continue
            name = str(row["dataset"]).strip()
            key = _catalog_key(name)
            item = evidence[paper_id].setdefault(key, YamlDataset())
            item.names.add(name)
            item.result_rows += 1
            if row.get("table_ref"):
                item.table_refs.add(str(row["table_ref"]).strip())
            if row.get("protocol_decision"):
                item.protocols.add(str(row["protocol_decision"]).strip())
            item.extraction_note = note_by_key.get(key, item.extraction_note)
            item.coverage_assessment = coverage_assessment or item.coverage_assessment
        discovered_datasets = (
            results_section.get("discovered_datasets", [])
            if isinstance(results_section, dict)
            else []
        )
        if not isinstance(discovered_datasets, list):
            discovered_datasets = []
        for discovered in discovered_datasets:
            if not isinstance(discovered, dict) or not discovered.get("name"):
                continue
            name = str(discovered["name"]).strip()
            key = _catalog_key(name)
            item = evidence[paper_id].setdefault(key, YamlDataset())
            item.names.add(name)
            item.discovered_manifest = True
            item.coverage_assessment = coverage_assessment or item.coverage_assessment
            for table_ref in discovered.get("table_refs") or []:
                if str(table_ref).strip():
                    item.table_refs.add(str(table_ref).strip())
        for key, note in note_by_key.items():
            item = evidence[paper_id].setdefault(key, YamlDataset())
            item.extraction_note = item.extraction_note or note
            item.coverage_assessment = coverage_assessment or item.coverage_assessment
    return dict(evidence)


def _dataset_names(items: dict[str, DatabaseDataset], keys: set[str]) -> list[str]:
    return _sorted_names(items[key].name for key in keys)


def _yaml_dataset_names(items: dict[str, YamlDataset], keys: Iterable[str]) -> list[str]:
    return _sorted_names(name for key in keys for name in items[key].names)


def evaluate(
    annotations: list[dict[str, str]],
    database_evidence: dict[str, dict[str, DatabaseDataset]],
    database_row_counts: dict[str, int],
    tracked_dataset_keys: set[str] | None = None,
    yaml_dataset_evidence: dict[str, dict[str, YamlDataset]] | None = None,
    manual_truth: Mapping[str, ManualTruth] | None = None,
) -> dict[str, Any]:
    paper_tp = paper_fp = paper_tn = paper_fn = 0
    dataset_tp = dataset_fp = dataset_fn = 0
    raw_detection_tp = raw_detection_fp = raw_detection_fn = 0
    manifest_detection_tp = manifest_detection_fp = manifest_detection_fn = 0
    raw_detection_fp_on_positive_papers = 0
    raw_detection_fp_on_negative_papers = 0
    table_tp = table_fp = table_fn = 0
    details: list[dict[str, Any]] = []
    database_snapshot_drifts: list[dict[str, Any]] = []

    for annotation in annotations:
        paper_id = annotation["arxiv_id"]
        truth = (manual_truth or _MANUAL_TRUTH)[paper_id]
        markdown_reference = manual_truth is not None and paper_id == "2508.05070"
        adjudication = None if markdown_reference else _ADJUDICATIONS.get(paper_id)
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

        # Dataset detection is evaluated before database promotion. A raw detection is any
        # tracked catalog name present either in a YAML result row or in the discovery manifest;
        # table assignment, protocol compatibility, and result-row counts are deliberately ignored.
        yaml_for_paper = (yaml_dataset_evidence or {}).get(paper_id, {})
        raw_detected_keys = {
            key
            for key, item in yaml_for_paper.items()
            if item.result_rows or item.discovered_manifest
        }
        manifest_detected_keys = {
            key for key, item in yaml_for_paper.items() if item.discovered_manifest
        }
        raw_detected_keys &= paper_tracked_keys
        manifest_detected_keys &= paper_tracked_keys
        if truth.strict_paper_label is not None:
            raw_detection_tp += len(expected_keys & raw_detected_keys)
            raw_detection_fn += len(expected_keys - raw_detected_keys)
            raw_detection_fp += len(raw_detected_keys - expected_keys)
            if truth.strict_paper_label:
                raw_detection_fp_on_positive_papers += len(raw_detected_keys - expected_keys)
            else:
                raw_detection_fp_on_negative_papers += len(raw_detected_keys - expected_keys)
            manifest_detection_tp += len(expected_keys & manifest_detected_keys)
            manifest_detection_fn += len(expected_keys - manifest_detected_keys)
            manifest_detection_fp += len(manifest_detected_keys - expected_keys)

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
        try:
            manual_count = int(annotation.get("database_result_count") or 0)
        except (TypeError, ValueError):
            manual_count = None
        actual_count = database_row_counts.get(paper_id, 0)
        count_drift = manual_count != actual_count
        if count_drift:
            database_snapshot_drifts.append(
                {
                    "arxiv_id": paper_id,
                    "annotation_count": manual_count,
                    "current_database_count": actual_count,
                }
            )

        manual_dataset_names = (
            truth.expected_datasets
            if truth.strict_paper_label is not None
            else truth.annotated_datasets
        )
        missing_manual_names: list[str] = []
        seen_missing_keys: set[str] = set()
        for name in manual_dataset_names:
            key = _catalog_key(name)
            if key not in stored_keys and key not in seen_missing_keys:
                missing_manual_names.append(name)
                seen_missing_keys.add(key)
        yaml_audit: list[dict[str, Any]] = []
        if yaml_dataset_evidence is not None:
            for name in missing_manual_names:
                key = _catalog_key(name)
                yaml_item = yaml_for_paper.get(key)
                yaml_audit.append(
                    {
                        "dataset": name,
                        "tracked": key in paper_tracked_keys,
                        "database_promoted": key in stored_keys,
                        "yaml_detected": bool(
                            yaml_item and (yaml_item.result_rows or yaml_item.discovered_manifest)
                        ),
                        "yaml_discovery_manifest": bool(
                            yaml_item and yaml_item.discovered_manifest
                        ),
                        "yaml_names": _sorted_names(yaml_item.names) if yaml_item else [],
                        "yaml_result_rows": yaml_item.result_rows if yaml_item else 0,
                        "yaml_table_refs": _sorted_names(yaml_item.table_refs) if yaml_item else [],
                        "yaml_protocols": sorted(yaml_item.protocols) if yaml_item else [],
                        "yaml_extraction_note": yaml_item.extraction_note if yaml_item else "",
                        "yaml_coverage_assessment": (
                            yaml_item.coverage_assessment if yaml_item else ""
                        ),
                    }
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
                "dataset_findings": [
                    {"dataset": dataset, "finding": finding}
                    for dataset, finding in sorted(
                        () if markdown_reference else _DATASET_FINDINGS.get(paper_id, ()),
                        key=lambda entry: _natural_sort_key(entry[0]),
                    )
                ],
                "yaml_dataset_audit": yaml_audit,
                "yaml_detected_datasets": _yaml_dataset_names(yaml_for_paper, raw_detected_keys),
                "yaml_manifest_datasets": _yaml_dataset_names(
                    yaml_for_paper, manifest_detected_keys
                ),
                "yaml_result_datasets": _yaml_dataset_names(
                    yaml_for_paper,
                    (key for key in raw_detected_keys if yaml_for_paper[key].result_rows),
                ),
                "database_result_rows": actual_count,
                "annotation_database_result_rows": manual_count,
                "database_result_count_drift": count_drift,
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

    truth_map = manual_truth or _MANUAL_TRUTH
    reviewed_truth = [truth_map[row["arxiv_id"]] for row in annotations]
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
    yaml_missing_audits = [
        audit
        for item in details
        for audit in item["yaml_dataset_audit"]
        if item["strict_paper_label"] is not None and audit["tracked"]
    ]
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
            "yaml_discovery": {
                "tracked_manual_positive_pairs": (dataset_tp + len(yaml_missing_audits)),
                "tracked_manual_missing_pairs": len(yaml_missing_audits),
                "tracked_manual_missing_detected_in_yaml": sum(
                    audit["yaml_detected"] for audit in yaml_missing_audits
                ),
                "tracked_manual_missing_with_yaml_rows": sum(
                    audit["yaml_detected"] and audit["yaml_result_rows"] > 0
                    for audit in yaml_missing_audits
                ),
                "tracked_manual_missing_manifest_only": sum(
                    audit["yaml_detected"] and audit["yaml_result_rows"] == 0
                    for audit in yaml_missing_audits
                ),
                "tracked_manual_missing_absent_from_yaml": sum(
                    not audit["yaml_detected"] for audit in yaml_missing_audits
                ),
                "tracked_manual_positive_detected_in_yaml": (
                    dataset_tp
                    + sum(
                        audit["yaml_detected"] for audit in yaml_missing_audits if audit["tracked"]
                    )
                ),
                "tracked_manual_positive_absent_from_yaml": sum(
                    not audit["yaml_detected"] for audit in yaml_missing_audits if audit["tracked"]
                ),
            },
            "raw_detection": {
                "definition": (
                    "Tracked dataset name present in a raw YAML result row or discovered_datasets "
                    "manifest; strict papers only; table/protocol/database promotion ignored."
                ),
                "true_positive": raw_detection_tp,
                "false_positive": raw_detection_fp,
                "false_negative": raw_detection_fn,
                "false_positive_on_manual_positive_papers": raw_detection_fp_on_positive_papers,
                "false_positive_on_manual_negative_papers": raw_detection_fp_on_negative_papers,
                "precision": _ratio(raw_detection_tp, raw_detection_tp + raw_detection_fp),
                "recall": _ratio(raw_detection_tp, raw_detection_tp + raw_detection_fn),
                "f1": _ratio(
                    2 * raw_detection_tp,
                    2 * raw_detection_tp + raw_detection_fp + raw_detection_fn,
                ),
                "manifest_only": {
                    "true_positive": manifest_detection_tp,
                    "false_positive": manifest_detection_fp,
                    "false_negative": manifest_detection_fn,
                    "precision": _ratio(
                        manifest_detection_tp,
                        manifest_detection_tp + manifest_detection_fp,
                    ),
                    "recall": _ratio(
                        manifest_detection_tp,
                        manifest_detection_tp + manifest_detection_fn,
                    ),
                    "f1": _ratio(
                        2 * manifest_detection_tp,
                        2 * manifest_detection_tp
                        + manifest_detection_fp
                        + manifest_detection_fn,
                    ),
                },
            },
            "database_snapshot": {
                "drift_count": len(database_snapshot_drifts),
                "drifts": database_snapshot_drifts,
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


def _render_dataset_finding(item: dict[str, Any], finding: dict[str, str]) -> str:
    """Make static adjudication text distinguish raw LLM detection from DB promotion."""
    text = finding["finding"]
    if "missed by the LLM" not in text:
        return text
    key = _catalog_key(finding["dataset"])
    audit = next(
        (
            candidate
            for candidate in item["yaml_dataset_audit"]
            if _catalog_key(candidate["dataset"]) == key
        ),
        None,
    )
    stored_keys = {_catalog_key(name) for name in item["stored_datasets"]}
    if key in stored_keys:
        replacement = "stored in the database"
    elif audit and audit["yaml_detected"]:
        replacement = "detected in raw YAML but not promoted"
    else:
        replacement = "absent from raw YAML"
    return text.replace("missed by the LLM", replacement)


def render_report(result: dict[str, Any], annotation_hash: str) -> str:
    summary = result["summary"]
    paper = summary["paper_level"]
    dataset = summary["dataset_level"]
    table = summary["table_reference_level"]
    adjudication = summary["manual_adjudication"]
    scope = summary["tracking_scope"]
    yaml_discovery = summary["yaml_discovery"]
    raw_detection = summary["raw_detection"]
    manifest_detection = raw_detection["manifest_only"]
    database_snapshot = summary["database_snapshot"]
    details = result["papers"]
    supplemental_count = sum(item["cohort"] == "supplemental_v3" for item in details)
    core_count = summary["paper_count"] - supplemental_count

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
        "- **Raw LLM dataset detection** = a tracked dataset name present in either a raw YAML "
        "result row or the `discovered_datasets` manifest, before table/protocol filtering or "
        "database promotion. This is the detection-only metric; it is distinct from the "
        "end-to-end LLM/database metric.",
        "- **Confirmed** means the discrepancy was resolved in manual follow-up; **candidate** means it "
        "still needs adjudication.",
        "",
        "## Executive summary",
        "",
        f"- **LLM/database output:** {summary['stored_result_rows']} stored result rows across "
        f"{summary['stored_paper_dataset_pairs']} paper-dataset pairs for {summary['paper_count']} reviewed papers "
        f"({core_count} core + {supplemental_count} supplemental v3). "
        "The manual annotations do not contain result-row counts.",
        f"- **Database snapshot:** {database_snapshot['drift_count']} paper(s) changed since the cohort CSV "
        "was prepared; current database counts are used for all metrics, while the original CSV counts "
        "are retained as a provenance check.",
        f"- **Manual reference:** {summary['strict_paper_count']} papers have strict compatible/incompatible "
        f"labels; {summary['qualified_paper_count']} ambiguous or protocol-qualified manual judgments are "
        "reported but excluded from strict LLM metrics.",
        f"- **Tracked-dataset scope:** {scope['catalog_dataset_count']} catalog datasets. "
        f"{scope['strict_manual_dataset_pairs_excluded']} strict manual paper-dataset pairs and "
        f"{scope['manual_table_pairs_excluded']} manual dataset-table pairs were excluded as untracked; "
        f"the database contributed {scope['stored_dataset_pairs_excluded']} untracked stored pairs.",
        f"- **LLM paper-inclusion performance:** precision {_percent(paper['precision'])}, "
        f"recall {_percent(paper['recall'])}, "
        f"specificity {_percent(paper['specificity'])}, accuracy {_percent(paper['accuracy'])}. "
        f"Absolute counts: TP {paper['true_positive']}, FP {paper['false_positive']}, "
        f"TN {paper['true_negative']}, FN {paper['false_negative']}; precision fraction "
        f"{paper['true_positive']}/{paper['true_positive'] + paper['false_positive']}, recall fraction "
        f"{paper['true_positive']}/{paper['true_positive'] + paper['false_negative']}.",
        f"- **LLM tracked-dataset performance:** precision {_percent(dataset['precision'])}, "
        f"recall {_percent(dataset['recall'])}, F1 {_percent(dataset['f1'])} "
        f"(TP {dataset['true_positive']}, FP {dataset['false_positive']}, "
        f"FN {dataset['false_negative']}; precision fraction "
        f"{dataset['true_positive']}/{dataset['true_positive'] + dataset['false_positive']}, "
        f"recall fraction {dataset['true_positive']}/"
        f"{dataset['true_positive'] + dataset['false_negative']}). "
        f"The manual reference contains {dataset['true_positive'] + dataset['false_negative']} positive "
        f"paper-dataset pairs; the LLM/database returned "
        f"{dataset['true_positive'] + dataset['false_positive']} positive pairs.",
        f"- **LLM raw dataset-detection performance (rows or manifest):** precision "
        f"{_percent(raw_detection['precision'])}, recall {_percent(raw_detection['recall'])}, "
        f"F1 {_percent(raw_detection['f1'])} (TP {raw_detection['true_positive']}, "
        f"FP {raw_detection['false_positive']}, FN {raw_detection['false_negative']}; "
        f"precision fraction {raw_detection['true_positive']}/"
        f"{raw_detection['true_positive'] + raw_detection['false_positive']}, recall fraction "
        f"{raw_detection['true_positive']}/"
        f"{raw_detection['true_positive'] + raw_detection['false_negative']}). "
        f"This ignores table assignment, protocol compatibility, and database promotion. Of the "
        f"{raw_detection['false_positive']} raw false positives, "
        f"{raw_detection['false_positive_on_manual_positive_papers']} are extra names on manually "
        f"positive papers and {raw_detection['false_positive_on_manual_negative_papers']} are names "
        "detected on manually incompatible papers.",
        f"- **Manifest-only diagnostic:** precision {_percent(manifest_detection['precision'])}, "
        f"recall {_percent(manifest_detection['recall'])}, F1 {_percent(manifest_detection['f1'])} "
        f"(TP {manifest_detection['true_positive']}, FP {manifest_detection['false_positive']}, "
        f"FN {manifest_detection['false_negative']}). The broader raw-detection score also accepts "
        "dataset-bearing result rows, which is why it can recover aliases or names absent from the "
        "manifest.",
        f"- **Raw-YAML discovery audit:** of {yaml_discovery['tracked_manual_missing_pairs']} strict "
        f"tracked manual-only pairs, the YAML result rows or discovery manifest contain "
        f"{yaml_discovery['tracked_manual_missing_detected_in_yaml']} (not promoted to the database) and "
        f"{yaml_discovery['tracked_manual_missing_absent_from_yaml']} are absent from YAML result rows. "
        f"Raw-YAML discovery recall is "
        f"{_percent(_ratio(yaml_discovery['tracked_manual_positive_detected_in_yaml'], yaml_discovery['tracked_manual_positive_pairs']))} "
        f"({yaml_discovery['tracked_manual_positive_detected_in_yaml']}/{yaml_discovery['tracked_manual_positive_pairs']}); "
        f"of the {yaml_discovery['tracked_manual_missing_detected_in_yaml']} database-missing pairs, "
        f"{yaml_discovery['tracked_manual_missing_with_yaml_rows']} have raw result rows and "
        f"{yaml_discovery['tracked_manual_missing_manifest_only']} appear only in the discovery manifest. "
        "The database recall is lower when detected datasets are filtered or not promoted. "
        "This is a discovery-versus-promotion diagnostic, not a replacement for the database score.",
        f"- **LLM exact tracked-dataset-table performance** on {table['scored_paper_count']} fully interpretable "
        f"papers: "
        f"precision {_percent(table['precision'])}, recall {_percent(table['recall'])}, "
        f"F1 {_percent(table['f1'])} (TP {table['true_positive']}, FP {table['false_positive']}, "
        f"FN {table['false_negative']}; precision fraction "
        f"{table['true_positive']}/{table['true_positive'] + table['false_positive']}, "
        f"recall fraction {table['true_positive']}/"
        f"{table['true_positive'] + table['false_negative']}). "
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
        f"The end-to-end database recall is lower than raw dataset-detection recall because datasets can "
        f"be detected but filtered during catalog, protocol, or table handling. In this cohort, raw YAML "
        f"evidence recovers {yaml_discovery['tracked_manual_positive_detected_in_yaml']} of "
        f"{yaml_discovery['tracked_manual_positive_pairs']} strict tracked manual-positive datasets; "
        "the remaining database misses are therefore not necessarily pure LLM discovery misses. "
        "Table association remains the clearest extraction weakness.",
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
            "The earlier database snapshot labeled four rows as Amazon2M, but the paper uses a different "
            "Amazon dataset version and its Table 2 contains statistics. Those rows are no longer in the "
            "current database, so this is retained as historical adjudication rather than a current false "
            "positive."
        ),
        "2010.05788": (
            "Qualified case: the database has zero rows, while the manual note says one MNIST value "
            "could be compatible. The raw YAML contains MNIST evidence, so this is not an unambiguous "
            "raw dataset-discovery miss and remains outside strict scoring."
        ),
        "1905.12560": (
            "The manual follow-up accepts the period-typical 10-fold cross-validation protocol. COLLAB, "
            "CSL, MUTAG, and PROTEINS are therefore database true positives; IMDB-BINARY and IMDB-MULTI "
            "are absent from the database, although both are present in the raw YAML artifact. PTC is "
            "untracked and excluded."
        ),
        "1710.03059": (
            "The manual follow-up confirms all six named datasets as compatible. The LLM recovered "
            "all four tracked datasets: CiteSeer, Cora, PPI, and PubMed. BlogCatalog and POS are present "
            "in the raw YAML but untracked and excluded from the score."
        ),
        "2403.07954": (
            "The database is missing Chameleon, CiteSeer, Cora, ogbn-arxiv, and PubMed, but the raw YAML "
            "contains all five; these are not pure LLM discovery misses. Untracked Genius is excluded. "
            "Penn94 is a true dataset match, but belongs to appendix Table 8 with Genius and ogbn-arxiv. "
            "The LLM's Table 1 associations are false positives because Table 1 contains statistics; "
            "Actor and Squirrel results are in Table 2."
        ),
        "2508.05070": (
            "For TANGO, the manual dataset reference is read from manual_review_v3.md. The current "
            "file marks all 13 database datasets as checked and has no additional missing-dataset entry, "
            "so the database dataset list is a perfect match under that reference. The raw YAML also "
            "lists ZINC-12k and Diameter; these are not counted as manual positives unless added to the "
            "Markdown review."
        ),
        "1903.02428": (
            "The database is missing Cora, IMDB-BINARY, and REDDIT-BINARY, while the raw YAML contains "
            "evidence for each; these are promotion/table-handling misses. ModelNet10 is untracked and "
            "excluded. The explicit table reference differs: "
            "manual MUTAG Table 2 versus LLM/database Table 1."
        ),
        "2206.08005": (
            "HIV and MUV are present in the raw YAML but untracked, so they are excluded from scoring. "
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
            f"At paper level, the current database has {paper['false_positive']} strict false positives "
            f"and {paper['false_negative']} strict false negatives in this cohort. The two qualified "
            "papers remain outside the strict paper-level metrics.",
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
                        f"- **Database snapshot note:** cohort CSV recorded "
                        f"{item['annotation_database_result_rows']} rows; current database has "
                        f"{item['database_result_rows']} rows. Current rows are used for scoring."
                    ]
                    if item["database_result_count_drift"]
                    else []
                ),
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
        if item["dataset_findings"]:
            lines.append("- **Dataset-specific manual findings:**")
            lines.extend(
                f"  - **{finding['dataset']}:** {_render_dataset_finding(item, finding)}"
                for finding in item["dataset_findings"]
            )
        if item["yaml_dataset_audit"]:
            lines.append("- **Missing-dataset YAML/promotion audit:**")
            for audit in item["yaml_dataset_audit"]:
                scope_label = "tracked" if audit["tracked"] else "untracked; excluded from scores"
                if audit["yaml_detected"]:
                    yaml_names = _list(audit["yaml_names"])
                    if audit["yaml_result_rows"]:
                        evidence = (
                            f"detected in YAML result rows as {yaml_names} "
                            f"({audit['yaml_result_rows']} result rows; tables: "
                            f"{_list(audit['yaml_table_refs'])}; protocols: "
                            f"{_list(audit['yaml_protocols'])})"
                        )
                    else:
                        evidence = (
                            f"listed in YAML discovered_datasets as {yaml_names} "
                            f"(no result rows; tables: {_list(audit['yaml_table_refs'])})"
                        )
                    if audit["yaml_coverage_assessment"]:
                        evidence += f"; YAML coverage={audit['yaml_coverage_assessment']}"
                else:
                    evidence = "not detected in YAML result rows"
                    if audit["yaml_extraction_note"]:
                        evidence += f"; YAML note: {audit['yaml_extraction_note']}"
                promotion = (
                    "promoted to the database"
                    if audit["database_promoted"]
                    else "not promoted to the database"
                )
                lines.append(
                    f"  - **{audit['dataset']}** ({scope_label}): {evidence}; {promotion}."
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
            "- The raw-YAML audit reads dataset-bearing result rows and the "
            "`discovered_datasets` manifest from each paper's `extracted/llm_output.yaml` before "
            "database promotion. A YAML detection can still be untracked, protocol-incompatible, "
            "incomplete, or otherwise omitted downstream; it is reported as diagnostic evidence "
            "and does not alter the LLM/database scores.",
            "- An LLM true positive requires the same positive paper-dataset or dataset-table pair in the "
            "manual reference and LLM/database output. Result values, models, and metrics were not manually "
            "annotated and are outside this evaluation.",
            "- Table scoring uses exact dataset-table pairs and only the six papers whose free-text table "
            "annotations could be assigned to every compatible dataset without guessing.",
            "- Two qualified papers are excluded from strict rates: 2010.05788 and 2006.05535. "
            "Manual follow-up moved 1710.03059 and 1905.12560 into the strict compatible set.",
            f"- The core cohort was deliberately stratified as 10 papers with and 10 without stored results; "
            f"the report adds {supplemental_count} supplemental v3 paper(s). LLM paper-level precision and "
            "accuracy therefore describe this testbed, not corpus prevalence.",
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
    manual_truth = dict(_MANUAL_TRUTH)
    markdown_truth = load_markdown_dataset_truth(args.manual_review_markdown, "2508.05070")
    if markdown_truth is not None:
        manual_truth["2508.05070"] = markdown_truth
    database_evidence, database_row_counts, tracked_dataset_keys = load_database_evidence(
        args.database, paper_ids
    )
    yaml_dataset_evidence = load_yaml_dataset_evidence(args.papers_dir, paper_ids)
    result = evaluate(
        annotations,
        database_evidence,
        database_row_counts,
        tracked_dataset_keys,
        yaml_dataset_evidence,
        manual_truth,
    )
    annotation_hash = hashlib.sha256(args.annotations.read_bytes()).hexdigest()
    markdown_hash = (
        hashlib.sha256(args.manual_review_markdown.read_bytes()).hexdigest()
        if args.manual_review_markdown.is_file()
        else None
    )
    result["metadata"] = {
        "generated_at": datetime.now(UTC).isoformat(),
        "annotation_path": str(args.annotations),
        "annotation_sha256": annotation_hash,
        "manual_review_markdown": str(args.manual_review_markdown),
        "manual_review_markdown_sha256": markdown_hash,
        "database_path": str(args.database),
        "papers_dir": str(args.papers_dir),
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
    parser.add_argument(
        "--manual-review-markdown",
        type=Path,
        default=_PROJECT_ROOT / "experiments/extraction_validation/manual_review_v3.md",
    )
    parser.add_argument("--database", type=Path, default=_PROJECT_ROOT / "data/benchmarks.db")
    parser.add_argument("--papers-dir", type=Path, default=_PROJECT_ROOT / "papers")
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
