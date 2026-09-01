"""Audit random train/validation/test split usage for the result-paper cohort.

The audit is deliberately conservative: a paper is marked ``yes`` only when its
local LaTeX source contains explicit split/protocol wording.  Bare mentions of
random seeds or random initialization are not evidence.
"""

from __future__ import annotations

import argparse
import importlib
import json
import re
import sqlite3
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
is_conference_publication_venue = importlib.import_module(
    "backend.venue"
).is_conference_publication_venue


POSITIVE_PATTERNS = (
    re.compile(r"\brandom(?:ly)?\s+(?:split|partition|divid(?:e|ed)|assign)", re.I),
    re.compile(r"\b(?:random|randomly)\s+(?:data\s+)?splits?\b", re.I),
    re.compile(r"\bstratified\s+(?:random\s+)?split(?:s|ting)?\b", re.I),
    re.compile(r"\brandom\s+(?:train(?:ing)?|test|validation)\s+split", re.I),
)
NEGATIVE_PATTERNS = (
    re.compile(r"\b(?:official|predefined|fixed|standard|canonical)\s+(?:data\s+)?split", re.I),
    re.compile(r"\b(?:scaffold|temporal|time[- ]based|chronological|group)\s+split", re.I),
    re.compile(r"\bsplit(?:s|ting)?\s+(?:by|according to|based on)\b", re.I),
)
KEYWORD_RE = re.compile(r"\b(?:random|stratified|split|partition|cross[- ]?validation)\b", re.I)
TU_DATASETS = {
    "MUTAG",
    "PROTEINS",
    "D&D",
    "NCI1",
    "COLLAB",
    "IMDB-BINARY",
    "IMDB-MULTI",
    "REDDIT-BINARY",
    "REDDIT-MULTI-5K",
    "RDT-B",
    "ENZYMES",
}
MANUAL_REVIEW_OVERRIDES = {
    "2112.03499": {
        "database_action": "retain",
        "review_note": "Retain: the heterophilic results use the established Geom-GCN-style fixed split referenced by the paper.",
    },
    "2305.18965": {
        "database_action": "retain",
        "review_note": "Retain: the heterophilic results use the established Geom-GCN-style fixed split referenced by the paper.",
    },
    "2407.11596": {
        "database_action": "retain",
        "review_note": "Retain: the Actor results use the established Geom-GCN 48/32/20 split.",
    },
    "2510.10116": {
        "database_action": "retain",
        "review_note": "Retain: the heterophilic results use the established Geom-GCN-style split referenced by the paper.",
    },
    "2201.12994": {
        "database_action": "exclude_all_results",
        "review_note": "The stored results use a 60/20/20 train/validation/test split rather than the tracked canonical benchmark protocol.",
    },
    "2205.11172": {
        "database_action": "exclude_all_results",
        "review_note": "The stored results use a 60/20/20 train/validation/test split rather than the tracked canonical benchmark protocol.",
    },
    "2306.07608": {
        "database_action": "exclude_all_results",
        "review_note": "The stored results use a 60/20/20 train/validation/test split rather than the tracked canonical benchmark protocol.",
    },
    "2310.05296": {
        "database_action": "exclude_all_results",
        "review_note": "The stored results use a 60/20/20 train/validation/test split rather than the tracked canonical benchmark protocol.",
    },
    "2310.10064": {
        "database_action": "exclude_all_results",
        "review_note": "The stored results use a 60/20/20 train/validation/test split rather than the tracked canonical benchmark protocol.",
    },
    "2405.12474": {
        "database_action": "exclude_all_results",
        "review_note": "The stored results use a 60/20/20 train/validation/test split rather than the tracked canonical benchmark protocol.",
    },
    "2408.07191": {
        "database_action": "exclude_all_results",
        "review_note": "The stored results use a 60/20/20 train/validation/test split rather than the tracked canonical benchmark protocol.",
    },
    "2408.16288": {
        "database_action": "exclude_all_results",
        "review_note": "The stored results use a 60/20/20 train/validation/test split rather than the tracked canonical benchmark protocol.",
    },
    "2412.19106": {
        "database_action": "exclude_all_results",
        "review_note": "The stored results use a 60/20/20 train/validation/test split rather than the tracked canonical benchmark protocol.",
    },
    "2504.20430": {
        "database_action": "exclude_all_results",
        "review_note": "The stored results use a 60/20/20 train/validation/test split rather than the tracked canonical benchmark protocol.",
    },
    "2505.23014": {
        "database_action": "exclude_all_results",
        "review_note": "The stored results use a 60/20/20 train/validation/test split rather than the tracked canonical benchmark protocol.",
    },
    "2602.07256": {
        "database_action": "exclude_all_results",
        "review_note": "The stored results use a 60/20/20 train/validation/test split rather than the tracked canonical benchmark protocol.",
    },
    "2010.12408": {
        "database_action": "exclude_all_results",
        "review_note": "The reported comparison uses repeated random data splits rather than the fixed default protocol for the stored CiteSeer and PubMed results.",
    },
    "2010.13993": {
        "database_action": "retain_only_eligible_results",
        "review_note": "Mixed batch: retain the OGB Arxiv and Products rows using benchmark-provided splits; exclude the smaller citation-network rows using incompatible random splits.",
    },
    "2102.11391": {
        "database_action": "exclude_all_results",
        "review_note": "The evaluation setting is broken for database use: the reported random/noncanonical split setup does not provide comparable stored benchmark results.",
    },
    "2112.14531": {
        "database_action": "exclude_non_default_results",
        "review_note": "The paper uses random 60/20/20 or repeated random splits; these are incompatible with the fixed database protocol where applicable.",
    },
    "2312.04737": {
        "database_action": "exclude_non_default_results",
        "review_note": "The Cora results use repeated random splits, incompatible with the database's fixed Planetoid protocol.",
    },
    "2006.05057": {
        "database_action": "exclude_all_results",
        "review_note": "Attack paper: clean rows are controls inside an adversarial-attack evaluation, not standalone canonical benchmark results.",
    },
    "2007.02133": {
        "database_action": "exclude_all_results",
        "review_note": "The current audit policy excludes this paper's stored results because the source includes the 20-nodes-per-class setting under review.",
    },
    "2007.09296": {
        "database_action": "exclude_non_default_results",
        "review_note": "The paper evaluates citation datasets with random splits in addition to fixed settings; retain no random-split rows because the database defaults are fixed or otherwise dataset-specific.",
    },
    "2009.03509": {
        "database_action": "retain",
        "review_note": "Stored rows use the official OGB standard splits. The paper's Random Partition is computational subgraph partitioning, not a replacement train/validation/test split.",
    },
    "2107.04086": {
        "database_action": "exclude_all_results",
        "review_note": "Counterfactual-explanation paper: the stored NCI1 rows are base-model controls for an explanation/robustness study, not standalone benchmark results.",
    },
    "2308.15614": {
        "database_action": "exclude_all_results",
        "review_note": "Adversarial graph-attack paper: the stored citation-graph rows are attack-evaluation controls, not standalone canonical benchmark results.",
    },
    "2404.17947": {
        "database_action": "exclude_all_results",
        "review_note": "Robustness/defense paper: stored rows compare defenses under node-feature attacks and are not ordinary benchmark results.",
    },
}


def _source(papers_dir: Path, arxiv_id: str) -> tuple[str, Path]:
    paths = sorted((papers_dir / arxiv_id / "latex").glob("*.tex"))
    if not paths:
        return "", papers_dir / arxiv_id
    return "\n".join(path.read_text(encoding="utf-8", errors="ignore") for path in paths), paths[0]


def _evidence(text: str) -> list[dict[str, object]]:
    lines = text.splitlines()
    found: list[dict[str, object]] = []
    seen: set[tuple[int, str]] = set()
    for number, line in enumerate(lines, 1):
        if not KEYWORD_RE.search(line):
            continue
        window = " ".join(lines[max(0, number - 2) : min(len(lines), number + 1)]).strip()
        positives = [p.pattern for p in POSITIVE_PATTERNS if p.search(window)]
        negatives = [p.pattern for p in NEGATIVE_PATTERNS if p.search(window)]
        if not positives and not negatives:
            continue
        kind = (
            "positive"
            if positives and not negatives
            else "negative"
            if negatives and not positives
            else "mixed"
        )
        key = (number, kind)
        if key in seen:
            continue
        seen.add(key)
        lowered = window.casefold()
        scope = "protocol"
        if any(
            marker in lowered
            for marker in (
                "many studies",
                "conventional random split",
                "random split is",
                "random splits can",
                "follow the convention",
                "caused by experiments using",
                "sensitive to both data splits",
            )
        ):
            scope = "discussion_or_citation"
        found.append(
            {
                "line": number,
                "kind": kind,
                "scope": scope,
                "text": re.sub(r"\s+", " ", window)[:500],
            }
        )
    return found


def _dataset_checks(
    text: str,
    datasets: list[tuple[str, str]],
    defaults: dict[str, dict[str, str]],
) -> list[dict[str, object]]:
    """Associate split evidence with datasets only when the source names both."""
    lines = text.splitlines()
    global_evidence = []
    for number, _line in enumerate(lines, 1):
        window = "\n".join(lines[max(0, number - 3) : min(len(lines), number + 2)])
        if not re.search(
            r"(?:\b(?:all|each|every)\s+(?:the\s+)?(?:graph\s+)?datasets?\b|"
            r"\bwe\s+(?:randomly\s+)?split\s+the\s+datasets?\b|"
            r"\bfor\s+each\s+(?:data|graph)\s+set\b|"
            r"\bfor\s+the\s+graph\s+kernel(?:s)?\s+datasets?\b|"
            r"\b(?:datasets?|data sets?)\b[^.]{0,100}\b(?:10[- ]fold|cross[- ]validation)\b)",
            window,
            re.I,
        ):
            continue
        positive = any(pattern.search(window) for pattern in POSITIVE_PATTERNS)
        negative = any(pattern.search(window) for pattern in NEGATIVE_PATTERNS)
        if positive or negative:
            global_evidence.append(
                {
                    "line": number,
                    "text": re.sub(r"\s+", " ", window).strip()[:500],
                    "positive": positive,
                    "negative": negative,
                }
            )
    group_match = re.search(
        r"\bgraph\s+kernel(?:s)?\s+datasets?\b.{0,5000}"
        r"\b(?:stratified\s+)?(?:random\s+)?splits?\b",
        text,
        re.I | re.S,
    )
    if group_match:
        global_evidence.append(
            {
                "line": text[: group_match.start()].count("\n") + 1,
                "text": re.sub(r"\s+", " ", group_match.group(0)).strip()[-500:],
                "positive": True,
                "negative": False,
                "association": "named_dataset_group_context",
            }
        )
    checks = []
    for dataset, variant in datasets:
        default = defaults.get(
            dataset,
            {
                "protocol": "unknown",
                "source": "not in seed_data.yaml",
                "evidence": "",
            },
        )
        aliases = [re.sub(r"[^a-z0-9]+", "", dataset.casefold())]
        aliases.extend(
            token.casefold() for token in re.findall(r"[A-Za-z0-9]+", dataset) if len(token) >= 5
        )
        mentions = []
        for number, line in enumerate(lines, 1):
            normalized = re.sub(r"[^a-z0-9]+", "", line.casefold())
            if any(alias and alias in normalized for alias in aliases):
                mentions.append(number)
        evidence = []
        for number in mentions:
            window = "\n".join(lines[max(0, number - 3) : min(len(lines), number + 2)])
            if any(
                pattern.search(window) for pattern in POSITIVE_PATTERNS + NEGATIVE_PATTERNS
            ) or re.search(r"\b(?:10[- ]fold|k[- ]fold|cross[- ]validation)\b", window, re.I):
                evidence.append(
                    {
                        "line": number,
                        "text": re.sub(r"\s+", " ", window).strip()[:500],
                        "positive": any(pattern.search(window) for pattern in POSITIVE_PATTERNS),
                        "negative": any(pattern.search(window) for pattern in NEGATIVE_PATTERNS),
                    }
                )
        if not evidence:
            evidence = [
                dict(
                    item,
                    association=item.get("association", "global_dataset_statement"),
                )
                for item in global_evidence
                if dataset in TU_DATASETS
                or item.get("association") != "named_dataset_group_context"
            ]
        else:
            evidence = [dict(item, association="named_dataset_context") for item in evidence]
        has_positive = any(item["positive"] and not item["negative"] for item in evidence)
        has_negative = any(item["negative"] and not item["positive"] for item in evidence)
        if has_positive and has_negative:
            assessment = "mixed"
            basis = (
                "source_global"
                if evidence and evidence[0].get("association") == "global_dataset_statement"
                else "source"
            )
        elif has_positive:
            assessment = "compatible"
            basis = (
                "source_global"
                if evidence and evidence[0].get("association") == "global_dataset_statement"
                else "source"
            )
        elif has_negative:
            assessment = "incompatible"
            basis = (
                "source_global"
                if evidence and evidence[0].get("association") == "global_dataset_statement"
                else "source"
            )
        else:
            variant_text = f"{dataset} {variant}".casefold()
            if "10-fold" in variant_text or "random" in variant_text:
                assessment = "compatible"
                basis = "database_variant"
            elif any(
                marker in variant_text
                for marker in ("scaffold", "planetoid", "fixed", "project", "species", "time")
            ):
                assessment = "incompatible"
                basis = "database_variant"
            else:
                assessment = "unclear"
                basis = "unresolved"
        protocol_kinds = set()
        for item in evidence:
            lowered = item["text"].casefold()
            if re.search(r"\b(?:10[- ]fold|k[- ]fold|cross[- ]validation)\b", lowered):
                protocol_kinds.add("cross_validation")
            if item["positive"]:
                protocol_kinds.add("random")
            if item["negative"]:
                protocol_kinds.add("non_random")
        default_protocol = default["protocol"]
        if (
            default_protocol == "random"
            and "random" in protocol_kinds
            and "non_random" not in protocol_kinds
        ) or (
            default_protocol in {"cross_validation", "cross_validation_or_random"}
            and protocol_kinds & {"cross_validation", "random"}
        ):
            eligibility = "eligible_default_protocol"
        elif default_protocol in {
            "fixed",
            "scaffold",
            "distribution_shift",
            "cross_validation",
            "cross_validation_or_random",
        } and protocol_kinds & {"random", "cross_validation"}:
            eligibility = "exclude_non_default_random_protocol"
        elif default_protocol == "unknown":
            eligibility = "unresolved_default_protocol"
        else:
            eligibility = "unresolved_paper_protocol"
        checks.append(
            {
                "dataset": dataset,
                "database_variant": variant,
                "default_protocol": default_protocol,
                "default_protocol_source": default["source"],
                "default_protocol_evidence": default["evidence"],
                "paper_protocol_kinds": sorted(protocol_kinds),
                "database_eligibility": eligibility,
                "assessment": assessment,
                "assessment_basis": basis,
                "evidence": evidence,
            }
        )
    return checks


def audit(db_path: Path, papers_dir: Path, seed_data_path: Path) -> dict[str, object]:
    con = sqlite3.connect(db_path)
    seed_data = yaml.safe_load(seed_data_path.read_text(encoding="utf-8"))
    defaults: dict[str, dict[str, str]] = {}
    for benchmark in seed_data.get("benchmarks", []):
        for dataset in benchmark.get("datasets", []):
            detail = dataset.get("detailed_description")
            detail = json.loads(detail) if isinstance(detail, str) else detail or {}
            split_text = str(detail.get("splits_and_evaluation") or "").casefold()
            variants = [item for item in dataset.get("variants", []) if item.get("is_standard")]
            variant_text = " ".join(
                f"{item.get('name') or ''} {item.get('split_type') or ''}" for item in variants
            ).casefold()
            if benchmark.get("name") == "TU Dortmund":
                protocol = "cross_validation_or_random"
            elif "planetoid" in split_text or "fixed public" in split_text:
                protocol = "fixed"
            elif (
                "10-fold" in variant_text
                or "10-fold" in split_text
                or "cross-validation" in split_text
            ):
                protocol = "cross_validation"
            elif "scaffold" in variant_text or "scaffold" in split_text:
                protocol = "scaffold"
            elif (
                "stratified random split" in split_text
                or "official stratified random" in split_text
                or (
                    any(marker in split_text for marker in ("random split", "randomly split"))
                    and not any(
                        marker in split_text
                        for marker in ("not comparable", "different", "rather than")
                    )
                )
            ):
                protocol = "random"
            elif any(
                marker in split_text
                for marker in (
                    "fixed split",
                    "planetoid",
                    "species",
                    "project split",
                    "sales rank",
                    "chronological",
                )
            ):
                protocol = (
                    "distribution_shift"
                    if any(
                        marker in split_text
                        for marker in ("species", "project split", "sales rank", "chronological")
                    )
                    else "fixed"
                )
            else:
                protocol = "unknown"
            defaults[dataset["name"]] = {
                "protocol": protocol,
                "source": "config/seed_data.yaml:" + dataset["name"],
                "evidence": " ".join(str(detail.get("splits_and_evaluation") or "").split()),
            }
    rows = con.execute(
        """
        SELECT p.arxiv_id, p.title, p.venue, COUNT(r.id) AS result_count
        FROM papers AS p JOIN results AS r ON r.paper_id = p.id
        WHERE TRIM(COALESCE(p.venue, '')) <> ''
        GROUP BY p.id ORDER BY p.arxiv_id
        """
    ).fetchall()
    cohort = [row for row in rows if is_conference_publication_venue(row[2])]
    entries = []
    for arxiv_id, title, venue, result_count in cohort:
        text, source_path = _source(papers_dir, arxiv_id)
        evidence = _evidence(text)
        positive = [
            item
            for item in evidence
            if item["kind"] in {"positive", "mixed"} and item["scope"] == "protocol"
        ]
        negative = [
            item
            for item in evidence
            if item["kind"] in {"negative", "mixed"} and item["scope"] == "protocol"
        ]
        if positive and negative:
            status = "mixed"
        elif positive:
            status = "yes"
        elif negative:
            status = "no"
        else:
            status = "unclear"
        entry = {
            "arxiv_id": arxiv_id,
            "title": title,
            "venue": venue,
            "result_count": result_count,
            "random_split": status,
            "source": str(source_path),
            "evidence": evidence,
        }
        if status == "yes":
            dataset_rows = con.execute(
                """
                SELECT DISTINCT d.name, dv.name
                FROM results AS r
                JOIN papers AS p ON p.id = r.paper_id
                JOIN dataset_variants AS dv ON dv.id = r.dataset_variant_id
                JOIN datasets AS d ON d.id = dv.dataset_id
                WHERE p.arxiv_id = ? ORDER BY d.name, dv.name
                """,
                (arxiv_id,),
            ).fetchall()
            entry["dataset_checks"] = _dataset_checks(text, dataset_rows, defaults)
            assessments = {check["assessment"] for check in entry["dataset_checks"]}
            if assessments <= {"compatible"}:
                entry["dataset_compatibility"] = "all_compatible"
            elif assessments & {"incompatible", "mixed"}:
                entry["dataset_compatibility"] = "incompatible_or_mixed"
            else:
                entry["dataset_compatibility"] = "partly_checked_unresolved"
            source_compatible = sum(
                check["assessment"] == "compatible" and check["assessment_basis"] == "source"
                for check in entry["dataset_checks"]
            )
            source_incompatible = sum(
                check["assessment"] in {"incompatible", "mixed"}
                and check["assessment_basis"] == "source"
                for check in entry["dataset_checks"]
            )
            database_only = sum(
                check["assessment_basis"] == "database_variant" for check in entry["dataset_checks"]
            )
            if source_compatible:
                conclusion = "confirmed_for_evaluated_dataset"
            elif source_incompatible:
                conclusion = "random_split_not_compatible_with_confirmed_datasets"
            elif database_only:
                conclusion = "database_variant_only_source_association_unresolved"
            else:
                conclusion = "random_split_not_confirmed_for_evaluated_datasets"
            entry["individual_review"] = {
                "source_inspected": True,
                "conclusion": conclusion,
                "source_confirmed_compatible_datasets": source_compatible,
                "source_confirmed_incompatible_or_mixed_datasets": source_incompatible,
                "database_variant_only_datasets": database_only,
                "unresolved_datasets": sum(
                    check["assessment"] == "unclear" for check in entry["dataset_checks"]
                ),
            }
            eligibilities = {check["database_eligibility"] for check in entry["dataset_checks"]}
            if "exclude_non_default_random_protocol" in eligibilities:
                entry["database_action"] = "exclude_non_default_results"
            elif eligibilities and eligibilities <= {"eligible_default_protocol"}:
                entry["database_action"] = "retain"
            elif "eligible_default_protocol" in eligibilities:
                entry["database_action"] = "retain_only_eligible_results"
            else:
                entry["database_action"] = "exclude_unresolved_results"
            override = MANUAL_REVIEW_OVERRIDES.get(arxiv_id)
            if override:
                entry["database_action"] = override["database_action"]
                entry["review_note"] = override["review_note"]
                if arxiv_id == "2010.13993":
                    entry["individual_review"]["conclusion"] = (
                        "mixed_batch_ogb_retained_citation_results_excluded"
                    )
                elif arxiv_id in {"2010.12408", "2102.11391"}:
                    entry["individual_review"]["conclusion"] = "incompatible_evaluation_excluded"
                elif arxiv_id == "2006.05057":
                    entry["individual_review"]["conclusion"] = "attack_paper_excluded"
                elif arxiv_id in {"2107.04086", "2308.15614", "2404.17947"}:
                    entry["individual_review"]["conclusion"] = (
                        "non_benchmark_robustness_paper_excluded"
                    )
                elif arxiv_id == "2007.09296":
                    entry["individual_review"]["conclusion"] = "random_split_excluded_from_database"
                elif arxiv_id == "2007.02133":
                    for check in entry["dataset_checks"]:
                        check["database_eligibility"] = "eligible_default_protocol"
                        check["assessment"] = "compatible"
                        check["assessment_basis"] = "stored_result_row_and_source"
                        if check["dataset"] in {"Cora", "CiteSeer", "PubMed"}:
                            check["stored_result_protocol"] = "fixed Planetoid split"
                            check["stored_result_evidence"] = (
                                "Local source lines 623-625: fixed split with 20 nodes per class "
                                "for training, 500 validation, and 1,000 testing."
                            )
                        elif check["dataset"] == "PPI":
                            check["stored_result_protocol"] = "fixed inductive 20/2/2 graph split"
                            check["stored_result_evidence"] = (
                                "Local source lines 567-573: 20 PPI graphs for training, 2 for "
                                "validation, and the remainder for testing."
                            )
                    entry["dataset_compatibility"] = "all_compatible"
                    entry["individual_review"]["conclusion"] = (
                        "stored_results_compatible_random_experiment_not_stored"
                    )
                elif arxiv_id == "2009.03509":
                    for check in entry["dataset_checks"]:
                        check["database_eligibility"] = "eligible_default_protocol"
                        check["assessment"] = "compatible"
                        check["assessment_basis"] = "stored_result_row_and_source"
                        check["stored_result_protocol"] = "official OGB standard split"
                        check["stored_result_evidence"] = (
                            "Local source lines 714, 773, and 780-782 identify OGB node-property "
                            "prediction tasks, distinguish subgraph partitioning from evaluation "
                            "splits, and state that the OGB requirements are followed for repeated runs."
                        )
                    entry["dataset_compatibility"] = "all_compatible"
                    entry["individual_review"]["conclusion"] = (
                        "stored_ogb_results_compatible_random_partition_is_sampling"
                    )
        entries.append(entry)
    yes_entries = [entry for entry in entries if entry["random_split"] == "yes"]
    review_conclusions = {}
    database_actions = {}
    for entry in yes_entries:
        conclusion = entry["individual_review"]["conclusion"]
        review_conclusions[conclusion] = review_conclusions.get(conclusion, 0) + 1
        action = entry["database_action"]
        database_actions[action] = database_actions.get(action, 0) + 1
    return {
        "schema_version": 1,
        "generated_by": "scripts/audit_random_splits.py",
        "cohort": {
            "definition": "papers with at least one results row and a venue classified by backend.venue.is_conference_publication_venue",
            "paper_count": len(entries),
            "result_count": sum(int(entry["result_count"]) for entry in entries),
        },
        "status_definitions": {
            "yes": "explicit random or stratified-random split protocol found",
            "no": "explicit non-random split protocol found and no positive protocol evidence found",
            "mixed": "both positive and non-random split protocol evidence found",
            "unclear": "local source did not provide explicit split protocol evidence",
            "dataset_checks": "for yes papers, compatible/incompatible requires split evidence near a named evaluated dataset; unclear means the source association was not resolved",
            "individual_review": "every yes paper has source_inspected=true and a conclusion based on its dataset_checks",
            "database_eligibility": "eligible_default_protocol is required for retaining a result; non-default random or cross-validation protocols are excluded, and unresolved cases are quarantined",
        },
        "yes_paper_review": {
            "paper_count": len(yes_entries),
            "conclusion_counts": review_conclusions,
            "database_action_counts": database_actions,
            "note": "The prior yes status is retained as the candidate result; individual_review is the dataset-aware follow-up conclusion.",
        },
        "default_protocol_source": "config/seed_data.yaml, with dataset-specific split_type/name metadata from the database as a secondary source",
        "papers": entries,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", type=Path, default=Path("data/benchmarks.db"))
    parser.add_argument("--papers", type=Path, default=Path("papers"))
    parser.add_argument("--seed-data", type=Path, default=Path("config/seed_data.yaml"))
    parser.add_argument("--output", type=Path, default=Path("config/random_split_audit.yaml"))
    args = parser.parse_args()
    result = audit(args.db, args.papers, args.seed_data)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        yaml.safe_dump(result, sort_keys=False, allow_unicode=True), encoding="utf-8"
    )
    counts = {}
    for paper in result["papers"]:
        counts[paper["random_split"]] = counts.get(paper["random_split"], 0) + 1
    print(f"wrote {args.output}: {result['cohort']['paper_count']} papers; {counts}")


if __name__ == "__main__":
    main()
