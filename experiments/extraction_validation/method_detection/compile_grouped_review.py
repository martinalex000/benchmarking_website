#!/usr/bin/env python3
"""Compile an editable, dataset-grouped method-detection review."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

_PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from experiments.extraction_validation.method_detection import prepare_review  # noqa: E402


@dataclass(frozen=True)
class DatasetGroup:
    """Datasets whose result tables use substantially the same method cohort."""

    name: str
    datasets: tuple[str, ...]
    reason: str
    database_datasets: tuple[str, ...] = ()


# These boundaries are deliberately explicit: similarity alone incorrectly merges tables that
# happen to contain generic GNN baselines but answer different tasks.
_GROUPS: dict[str, tuple[DatasetGroup, ...]] = {
    "2304.10074": (
        DatasetGroup(
            "OGB link prediction",
            ("ogbl-collab", "collab", "ogbl-ddi", "ogbl-citation2", "ogbl-ppa"),
            "Same five link-prediction methods; `collab` duplicates `ogbl-collab` in the raw output.",
            ("ogbl-collab", "ogbl-ddi", "ogbl-citation2", "ogbl-ppa"),
        ),
        DatasetGroup(
            "Heterophilic link prediction",
            ("Cornell", "Texas", "Wisconsin", "CiteSeer"),
            "Same seven methods and task, separate from the OGB protocol.",
        ),
    ),
    "2310.01089": (
        DatasetGroup(
            "Citation networks", ("Cora", "Citeseer"), "Same broad LLM and GNN comparison."
        ),
        DatasetGroup(
            "WebKB networks",
            ("Texas", "Wisconsin", "Cornell"),
            "Same four GNN baselines; GraphText variants differ slightly by dataset.",
        ),
    ),
    "2003.13663": (
        DatasetGroup("Cora depth comparison", ("Cora",), "Only quantitative dataset extracted."),
    ),
    "2206.08005": (
        DatasetGroup(
            "MoleculeNet classification",
            ("BBBP", "Tox21", "ToxCast", "Sider", "ClinTox", "MUV", "HIV", "Bace"),
            "Shared self-supervised-learning baseline panel.",
            ("BBBP", "Tox21", "ToxCast", "SIDER", "ClinTox", "MUV", "HIV", "BACE"),
        ),
        DatasetGroup(
            "Pretraining source data",
            ("ZINC15",),
            "Different role from the downstream MoleculeNet evaluations.",
        ),
    ),
    "2401.14155": (
        DatasetGroup(
            "Graph anomaly detection",
            ("Amazon", "YelpChi"),
            "Same anomaly-detection comparison; YelpChi was identified manually but has no raw rows.",
            ("Amazon2M", "YelpChi"),
        ),
    ),
    "1903.02428": (
        DatasetGroup(
            "Citation-network node classification",
            ("Cora", "CiteSeer", "PubMed"),
            "Identical six-method panel.",
        ),
        DatasetGroup(
            "TU graph classification",
            ("MUTAG", "PROTEINS", "COLLAB"),
            "Identical pooling and graph-classification panel.",
        ),
        DatasetGroup(
            "ModelNet point clouds", ("ModelNet10",), "Separate task and five-method panel."
        ),
    ),
    "1710.03059": (
        DatasetGroup(
            "Inductive networks",
            ("BlogCatalog", "POS", "PPI"),
            "Identical embedding-method panel.",
        ),
        DatasetGroup(
            "Transductive citation networks",
            ("Cora", "Citeseer", "Pubmed"),
            "Identical feature-and-embedding panel.",
            ("Cora", "CiteSeer", "PubMed"),
        ),
    ),
    "2403.07954": (
        DatasetGroup(
            "Classic citation networks",
            ("Cora", "Citeseer", "Pubmed"),
            "Same polynomial-filter panel, apart from one missing OrthKry row.",
        ),
        DatasetGroup(
            "Heterophilic node classification",
            ("Actor", "Chameleon", "Squirrel"),
            "Identical thirteen-method panel.",
        ),
        DatasetGroup(
            "Large node-classification datasets",
            ("Penn94", "ogbn-arxiv"),
            "Identical reduced nine-method panel.",
        ),
    ),
    "2508.05070": (
        DatasetGroup(
            "Synthetic graph tasks",
            ("SSSP", "Eccentricity"),
            "Identical dynamics-model panel.",
        ),
        DatasetGroup(
            "Benchmarking-GNN image and structure tasks",
            ("MNIST", "CIFAR10", "PATTERN", "CLUSTER"),
            "Overlapping core baselines, with task-specific additions.",
        ),
        DatasetGroup(
            "Long-range graph benchmark",
            ("Peptides-func", "Peptides-struct"),
            "Same benchmark family and mostly shared baselines.",
        ),
        DatasetGroup(
            "Heterophilic node classification",
            ("Questions", "Roman-empire", "Amazon-ratings", "Minesweeper", "Tolokers"),
            "Large shared baseline panel with positional-encoding variants.",
        ),
    ),
    "1905.12560": (
        DatasetGroup("CSL", ("CSL",), "Special isomorphism task and method panel."),
        DatasetGroup(
            "IMDB graph classification",
            ("IMDB-B", "IMDB-M"),
            "Identical seven-method panel.",
        ),
        DatasetGroup(
            "TU graph classification",
            ("MUTAG", "PROTEINS", "PTC", "COLLAB"),
            "Identical three-method panel.",
        ),
    ),
    "2010.05788": (
        DatasetGroup(
            "Explanation benchmarks",
            (
                "Syn 1",
                "Syn 2",
                "Syn 3",
                "Syn 4",
                "Syn 5",
                "Syn 6",
                "Bitcoin-alpha",
                "Bitcoin-OTC",
            ),
            "Identical explainer panel.",
        ),
        DatasetGroup(
            "MNIST classifier", ("MNIST SuperPixel-Graph",), "Separate classifier result."
        ),
    ),
    "2001.06216": (
        DatasetGroup("Cora explanation", ("Cora",), "Only GraphLIME was extracted."),
        DatasetGroup("PubMed explanation", ("Pubmed",), "Five-method explanation comparison."),
    ),
    "2112.07191": (
        DatasetGroup(
            "Localized collaborative filtering",
            (
                "Tianchi-174490",
                "Tianchi-61626",
                "Tianchi-3937919",
                "Tianchi-2798696",
                "MovieLens-War",
            ),
            "Identical six-method recommendation panel.",
        ),
    ),
    "1908.01207": (
        DatasetGroup(
            "Temporal interaction networks",
            ("Reddit", "Wikipedia", "LastFM", "MOOC"),
            "Same temporal baseline panel; MOOC lacks CTDNE.",
        ),
    ),
    "2006.05535": (
        DatasetGroup(
            "Private node classification",
            ("Cora", "Pubmed", "Facebook", "LastFM"),
            "Same privacy mechanisms; only the epsilon annotation changes.",
        ),
    ),
    "2210.01002": (
        DatasetGroup(
            "Structure-robust node classification",
            ("Cora", "Citeseer", "Cora-ML", "ACM"),
            "Identical six-method panel and attack protocol.",
        ),
    ),
    "1802.04407": (
        DatasetGroup(
            "Citation-network link prediction",
            ("Cora", "Citeseer", "PubMed"),
            "Same task; PubMed uses a smaller and partly renamed baseline panel.",
        ),
    ),
    "2402.18974": (
        DatasetGroup(
            "Synthetic graph generation",
            ("Community-Small", "Planar", "Stochastic Block Model (SBM)"),
            "Identical seven-model panel.",
        ),
        DatasetGroup("Protein graph generation", ("Proteins",), "Same panel minus DiGress."),
        DatasetGroup(
            "Molecular graph generation", ("QM9",), "Different molecular generator panel."
        ),
    ),
    "2505.22252": (
        DatasetGroup("B-XAIC explanations", ("B-XAIC",), "Only reported benchmark dataset."),
    ),
    "2502.15054": (
        DatasetGroup(
            "Large-scale graph systems",
            (
                "MAG240M",
                "Internal-full",
                "internal-less-feat",
                "internal-less-edge",
                "internal heterogeneous graph",
            ),
            "Systems comparisons rather than a conventional public baseline table.",
        ),
        DatasetGroup(
            "Content recommendation ablations",
            ("content recommendation",),
            "Ablation labels were extracted as method names.",
        ),
        DatasetGroup(
            "Product-ads recommendation",
            ("product ads recommendation",),
            "Separate internal task and two-system comparison.",
        ),
    ),
}


def _clean(value: Any) -> str:
    return re.sub(r"[\x00-\x1f\x7f]", "", str(value or "")).strip()


def _dataset_key(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.casefold())


def _load_raw_rows(path: Path) -> list[dict[str, str]]:
    payload = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    result_block = payload.get("results") or {}
    return [
        {
            "dataset": _clean(row.get("dataset")),
            "method": _clean(row.get("model")),
            "table_ref": _clean(row.get("table_ref")),
        }
        for row in result_block.get("results") or []
        if _clean(row.get("dataset")) and _clean(row.get("model"))
    ]


def _format_methods(methods: set[str]) -> str:
    return ", ".join(f"`{name}`" for name in sorted(methods, key=prepare_review._natural_key))


def _render_group(
    number: int,
    group: DatasetGroup,
    raw_rows: list[dict[str, str]],
    database_methods: list[prepare_review.MethodEvidence],
) -> list[str]:
    raw_dataset_keys = {_dataset_key(dataset) for dataset in group.datasets}
    grouped_rows = [row for row in raw_rows if _dataset_key(row["dataset"]) in raw_dataset_keys]
    detected_datasets = sorted(
        {row["dataset"] for row in grouped_rows}, key=prepare_review._natural_key
    )
    missing_raw_datasets = [
        dataset
        for dataset in group.datasets
        if _dataset_key(dataset) not in {_dataset_key(item) for item in detected_datasets}
    ]
    methods_by_dataset = {
        dataset: {row["method"] for row in grouped_rows if row["dataset"] == dataset}
        for dataset in detected_datasets
    }
    common_methods = set.intersection(*methods_by_dataset.values()) if methods_by_dataset else set()
    all_methods = set().union(*methods_by_dataset.values()) if methods_by_dataset else set()
    partial_methods = all_methods - common_methods
    table_refs = sorted(
        {row["table_ref"] for row in grouped_rows if row["table_ref"]},
        key=prepare_review._natural_key,
    )

    allowed_database = group.database_datasets or group.datasets
    database_keys = {_dataset_key(dataset) for dataset in allowed_database}
    stored_methods = {
        method.name
        for method in database_methods
        if any(_dataset_key(dataset) in database_keys for dataset in method.datasets)
    }

    lines = [
        f"#### Group {number}: {group.name}",
        "",
        f"- **Datasets:** {', '.join(f'`{dataset}`' for dataset in group.datasets)}",
        f"- **Why grouped:** {group.reason}",
        f"- **Raw table references:** {', '.join(f'`{ref}`' for ref in table_refs) or 'none'}",
        f"- **Raw methods on every detected dataset:** {_format_methods(common_methods) or 'none'}",
    ]
    if partial_methods:
        lines.append("- **Raw methods with partial coverage:**")
        for method in sorted(partial_methods, key=prepare_review._natural_key):
            coverage = [
                dataset for dataset, methods in methods_by_dataset.items() if method in methods
            ]
            lines.append(f"  - `{method}` — {', '.join(f'`{item}`' for item in coverage)}")
    else:
        lines.append("- **Raw methods with partial coverage:** none")
    if missing_raw_datasets:
        lines.append(
            "- **Datasets with no raw result rows:** "
            + ", ".join(f"`{dataset}`" for dataset in missing_raw_datasets)
        )
    lines.extend(
        [
            f"- **Stored method names after filtering/normalization:** "
            f"{_format_methods(stored_methods) or 'none'}",
            "",
            "**Missing methods:**  ",
            "",
            "**Detection / normalization comments:**  ",
            "",
            "- [ ] Group reviewed",
            "",
        ]
    )
    return lines


def render_review(
    papers: list[prepare_review.ReviewPaper],
    raw_rows_by_paper: dict[str, list[dict[str, str]]],
    database_evidence: dict[str, list[prepare_review.MethodEvidence]],
    database_result_counts: dict[str, int],
) -> str:
    """Render the editable dataset-grouped review and validate group coverage."""
    if set(_GROUPS) != {paper.arxiv_id for paper in papers}:
        raise ValueError("Dataset groups do not match the 20-paper cohort")

    lines = [
        "# Grouped method-detection and normalization review",
        "",
        "Review the raw extracted method names against the paper, one comparable dataset group at a "
        "time. Methods listed as partial are not automatically errors: a few missing baselines are "
        "allowed when the paper itself reports them unevenly.",
        "",
        "For each group, fill **Missing methods** when the extraction omitted a reported method, or "
        "use **Detection / normalization comments** for aliases, malformed names, non-method rows, "
        "wrong table association, inappropriate filtering, or other issues. Enter `NONE` when a field "
        "has no finding, then tick the group checkbox.",
        "",
        "`Raw methods` come from the paper's saved `llm_output.yaml`. `Stored method names` are the "
        "effective names currently attached to database rows after dataset/protocol filtering and "
        "normalization. The local LaTeX source and PDF remain the reference standard.",
        "",
        "## Papers",
        "",
    ]
    for paper in papers:
        raw_rows = raw_rows_by_paper[paper.arxiv_id]
        groups = _GROUPS[paper.arxiv_id]
        covered = [_dataset_key(dataset) for group in groups for dataset in group.datasets]
        ungrouped = sorted(
            {row["dataset"] for row in raw_rows if _dataset_key(row["dataset"]) not in covered},
            key=prepare_review._natural_key,
        )
        if ungrouped:
            raise ValueError(f"Ungrouped raw datasets for {paper.arxiv_id}: {ungrouped}")
        if len(covered) != len(set(covered)):
            raise ValueError(f"A dataset occurs in multiple groups for {paper.arxiv_id}")

        database_methods = database_evidence.get(paper.arxiv_id, [])
        lines.extend(
            [
                f"### {paper.index}. {paper.title}",
                "",
                f"- **arXiv:** `{paper.arxiv_id}`",
                f"- **Source:** [PDF]({paper.review_pdf_path}) · "
                f"[`expanded.tex`](../../../papers/{paper.arxiv_id}/latex/expanded.tex)",
                f"- **Cohort:** `{paper.cohort}`",
                f"- **Extraction outcome:** {len(raw_rows)} raw rows; "
                f"{database_result_counts.get(paper.arxiv_id, 0)} stored rows; "
                f"{len(database_methods)} stored method names",
                "",
            ]
        )
        for number, group in enumerate(groups, start=1):
            lines.extend(_render_group(number, group, raw_rows, database_methods))
        lines.extend(["**Paper-level comments:**  ", "", "---", ""])
    return "\n".join(lines)


def run(args: argparse.Namespace) -> tuple[int, int]:
    papers = prepare_review.load_papers(args.source_cohort, args.papers_dir)
    evidence, result_counts = prepare_review.load_method_evidence(
        args.database, [paper.arxiv_id for paper in papers]
    )
    raw_rows_by_paper = {
        paper.arxiv_id: _load_raw_rows(
            args.papers_dir / paper.arxiv_id / "extracted" / "llm_output.yaml"
        )
        for paper in papers
    }
    content = render_review(papers, raw_rows_by_paper, evidence, result_counts)
    args.output.write_text(content, encoding="utf-8")
    return len(papers), sum(len(groups) for groups in _GROUPS.values())


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
        "--output",
        type=Path,
        default=(
            _PROJECT_ROOT
            / "experiments/extraction_validation/method_detection/grouped_manual_review.md"
        ),
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    paper_count, group_count = run(build_parser().parse_args(argv))
    print(f"Compiled {paper_count} papers into {group_count} comparable dataset groups")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
