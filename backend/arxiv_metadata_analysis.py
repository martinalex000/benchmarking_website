"""Streaming analysis and recall auditing for the Cornell arXiv snapshot."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import sqlite3
from collections.abc import Iterable
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml

DEFAULT_SNAPSHOT_PATH = Path("papers/arxiv-metadata/arxiv-metadata-oai-snapshot.json")
DEFAULT_DB_PATH = Path("data/benchmarks.db")
DEFAULT_CONFIG_PATH = Path("config/arxiv_screening.yaml")
_GENERAL_GRAPH_PATTERN = re.compile("graph", re.IGNORECASE)


def normalize_arxiv_id(value: Any) -> str:
    """Normalize common arXiv identifier spellings, retaining legacy IDs."""
    identifier = str(value or "").strip()
    identifier = re.sub(r"^https?://arxiv\.org/(?:abs|pdf)/", "", identifier)
    identifier = re.sub(r"^arXiv:", "", identifier, flags=re.IGNORECASE)
    return re.sub(r"v\d+$", "", identifier, flags=re.IGNORECASE)


def _date_from_record(record: dict[str, Any]) -> str:
    versions = record.get("versions") or []
    if isinstance(versions, list) and versions:
        first = versions[0]
        if isinstance(first, dict):
            created = str(first.get("created") or "")
            match = re.search(r"(\d{4}-\d{2}-\d{2})", created)
            if match:
                return match.group(1)
            try:
                return (
                    datetime.strptime(created.split(" GMT", maxsplit=1)[0], "%a, %d %b %Y %H:%M:%S")
                    .date()
                    .isoformat()
                )
            except ValueError:
                pass
    for key in ("update_date", "published"):
        match = re.search(r"(\d{4}-\d{2}-\d{2})", str(record.get(key) or ""))
        if match:
            return match.group(1)
    return ""


@dataclass(frozen=True)
class KeywordFamily:
    name: str
    patterns: tuple[re.Pattern[str], ...]

    def matches(self, text: str) -> bool:
        return any(pattern.search(text) for pattern in self.patterns)


@dataclass(frozen=True)
class KeywordMatcher:
    """Shared fast matcher used by both the audit and screening workflows."""

    specific: re.Pattern[str]
    graph: re.Pattern[str]
    canonical_keywords: dict[str, str]
    keyword_families: tuple[KeywordFamily, ...]

    def matching_families(self, text: str) -> set[str]:
        return {family.name for family in self.keyword_families if family.matches(text)}

    def match_specific(self, text: str) -> list[str]:
        matched: list[str] = []
        seen: set[str] = set()
        for found in self.specific.finditer(text):
            normalized = " ".join(found.group(0).casefold().split())
            keyword = self.canonical_keywords.get(normalized, found.group(0))
            if keyword.casefold() not in seen:
                seen.add(keyword.casefold())
                matched.append(keyword)
        return matched

    def match_tier(self, title: str, abstract: str) -> tuple[str, list[str]] | None:
        text = f"{title}\n{abstract}"
        matched = self.match_specific(text)
        if matched:
            return "specific", matched
        if self.graph.search(text):
            return "graph", ["graph"]
        return None


def compile_keyword_matcher(
    specific_keywords: Iterable[str],
    keyword_families: tuple[KeywordFamily, ...] = (),
) -> KeywordMatcher:
    """Compile the common fast and family-level matchers."""
    unique_keywords = list(dict.fromkeys(specific_keywords))
    alternatives: list[str] = []
    canonical_keywords: dict[str, str] = {}
    for keyword in unique_keywords:
        escaped = re.escape(keyword).replace(r"\ ", r"\s+")
        alternatives.append(escaped)
        canonical_keywords[" ".join(keyword.casefold().split())] = keyword
    alternatives.sort(key=len, reverse=True)
    specific = re.compile(
        rf"(?<!\w)(?:{'|'.join(alternatives)})(?!\w)" if alternatives else r"(?!x)x",
        re.IGNORECASE,
    )
    return KeywordMatcher(
        specific=specific,
        graph=_GENERAL_GRAPH_PATTERN,
        canonical_keywords=canonical_keywords,
        keyword_families=keyword_families,
    )


@dataclass(frozen=True)
class ScreeningConfig:
    machine_learning_categories: tuple[str, ...]
    keyword_families: tuple[KeywordFamily, ...]
    specific_keywords: tuple[str, ...] = ()

    def matching_families(self, text: str) -> set[str]:
        return {family.name for family in self.keyword_families if family.matches(text)}

    def matcher(self) -> KeywordMatcher:
        """Compile the matcher once per operation rather than per metadata row."""
        return compile_keyword_matcher(
            self.specific_keywords,
            self.keyword_families,
        )

    @classmethod
    def load(cls, path: Path) -> ScreeningConfig:
        raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        categories = tuple(str(item) for item in raw.get("machine_learning_categories", []))
        families: list[KeywordFamily] = []
        for name, patterns in (raw.get("keyword_families") or {}).items():
            if isinstance(patterns, str):
                patterns = [patterns]
            combined = "|".join(f"(?:{pattern})" for pattern in patterns)
            compiled = (re.compile(combined, re.IGNORECASE),)
            families.append(KeywordFamily(str(name), compiled))
        if not categories or not families:
            raise ValueError(f"Screening configuration is empty: {path}")
        specific_keywords = tuple(
            str(keyword).strip()
            for keyword in raw.get("specific_keywords", [])
            if str(keyword).strip()
        )
        return cls(categories, tuple(families), tuple(dict.fromkeys(specific_keywords)))


@dataclass
class KeywordCounts:
    title: int = 0
    abstract: int = 0
    either: int = 0

    def add(self, title_match: bool, abstract_match: bool) -> None:
        self.title += int(title_match)
        self.abstract += int(abstract_match)
        self.either += int(title_match or abstract_match)

    def as_dict(self) -> dict[str, int]:
        return {"title": self.title, "abstract": self.abstract, "either": self.either}


@dataclass
class CategoryStats:
    papers: int = 0
    keywords: dict[str, KeywordCounts] = field(default_factory=dict)

    def add(self, family_matches: dict[str, tuple[bool, bool]]) -> None:
        self.papers += 1
        for family, (title_match, abstract_match) in family_matches.items():
            if not title_match and not abstract_match:
                continue
            self.keywords.setdefault(family, KeywordCounts()).add(title_match, abstract_match)


@dataclass(frozen=True)
class ClassifiedRecord:
    arxiv_id: str
    title: str
    abstract: str
    categories: tuple[str, ...]
    date: str
    family_matches: dict[str, tuple[bool, bool]]

    @property
    def keyword_union(self) -> bool:
        return any(title or abstract for title, abstract in self.family_matches.values())


def classify_record(
    record: dict[str, Any], config: ScreeningConfig, matcher: KeywordMatcher | None = None
) -> ClassifiedRecord:
    title = str(record.get("title") or "").strip()
    abstract = str(record.get("abstract") or "").strip()
    categories = tuple(dict.fromkeys(str(record.get("categories") or "").split()))
    matcher = matcher or config.matcher()
    title_matches = matcher.matching_families(title)
    abstract_matches = matcher.matching_families(abstract)
    family_matches = {
        family.name: (family.name in title_matches, family.name in abstract_matches)
        for family in config.keyword_families
    }
    return ClassifiedRecord(
        arxiv_id=normalize_arxiv_id(record.get("id")),
        title=title,
        abstract=abstract,
        categories=categories,
        date=_date_from_record(record),
        family_matches=family_matches,
    )


def load_known_result_papers(db_path: Path) -> dict[str, dict[str, str]]:
    """Load the recall reference set without allowing SQLite writes."""
    resolved = db_path.resolve()
    uri = f"file:{resolved}?mode=ro"
    with sqlite3.connect(uri, uri=True) as connection:
        rows = connection.execute("""
            SELECT DISTINCT p.arxiv_id, p.title, p.abstract
            FROM papers AS p
            JOIN results AS r ON r.paper_id = p.id
            WHERE p.arxiv_id IS NOT NULL AND trim(p.arxiv_id) != ''
            """).fetchall()
    return {
        normalize_arxiv_id(arxiv_id): {
            "title": str(title or ""),
            "abstract": str(abstract or ""),
        }
        for arxiv_id, title, abstract in rows
    }


def iter_classified_records(
    snapshot_path: Path, config: ScreeningConfig, matcher: KeywordMatcher | None = None
) -> Iterable[ClassifiedRecord]:
    with snapshot_path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON at {snapshot_path}:{line_number}: {exc}") from exc
            if not isinstance(record, dict):
                raise ValueError(f"Expected an object at {snapshot_path}:{line_number}")
            yield classify_record(record, config, matcher)


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(chunk_size), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _empty_family_counts(config: ScreeningConfig) -> dict[str, KeywordCounts]:
    return {family.name: KeywordCounts() for family in config.keyword_families}


def _record_matches_for_category(
    stats: dict[str, dict[str, CategoryStats]],
    categories: tuple[str, ...],
    family_matches: dict[str, tuple[bool, bool]],
) -> None:
    for index, category in enumerate(categories):
        position = "primary" if index == 0 else "secondary"
        stats.setdefault(category, {}).setdefault(position, CategoryStats()).add(family_matches)
        stats[category].setdefault("any", CategoryStats()).add(family_matches)


def analyze_snapshot(
    snapshot_path: Path,
    db_path: Path,
    config: ScreeningConfig,
) -> dict[str, Any]:
    known = load_known_result_papers(db_path)
    known_seen: set[str] = set()
    known_audit: dict[str, dict[str, Any]] = {}
    category_stats: dict[str, dict[str, CategoryStats]] = {}
    global_keywords = _empty_family_counts(config)
    ml_union_counts = {"any": 0, "primary": 0, "secondary": 0, "both": 0}
    total_records = 0
    duplicate_known_rows = 0
    min_date = ""
    max_date = ""
    matcher = config.matcher()

    for classified in iter_classified_records(snapshot_path, config, matcher):
        total_records += 1
        if classified.date and (not min_date or classified.date < min_date):
            min_date = classified.date
        if classified.date and classified.date > max_date:
            max_date = classified.date

        if classified.keyword_union:
            _record_matches_for_category(
                category_stats, classified.categories, classified.family_matches
            )
        ml_categories = set(classified.categories) & set(config.machine_learning_categories)
        ml_union_counts["any"] += bool(ml_categories)
        ml_union_counts["primary"] += bool(
            classified.categories and classified.categories[0] in config.machine_learning_categories
        )
        ml_union_counts["secondary"] += bool(
            set(classified.categories[1:]) & set(config.machine_learning_categories)
        )
        ml_union_counts["both"] += len(ml_categories) == 2
        for family, (title_match, abstract_match) in classified.family_matches.items():
            global_keywords[family].add(title_match, abstract_match)

        if classified.arxiv_id not in known:
            continue
        if classified.arxiv_id in known_seen:
            duplicate_known_rows += 1
            continue
        known_seen.add(classified.arxiv_id)
        ml_any = any(
            category in config.machine_learning_categories for category in classified.categories
        )
        primary_ml = bool(
            classified.categories and classified.categories[0] in config.machine_learning_categories
        )
        secondary_ml = any(
            category in config.machine_learning_categories for category in classified.categories[1:]
        )
        known_audit[classified.arxiv_id] = {
            "arxiv_id": classified.arxiv_id,
            "title": classified.title,
            "categories": " ".join(classified.categories),
            "snapshot_date": classified.date,
            "ml_primary": primary_ml,
            "ml_secondary": secondary_ml,
            "ml_any": ml_any,
            "keyword_union": classified.keyword_union,
            "combined_prefilter": ml_any and classified.keyword_union,
            "keyword_hits": [
                family
                for family, (title_match, abstract_match) in classified.family_matches.items()
                if title_match or abstract_match
            ],
            "keyword_title_hits": [
                family
                for family, (title_match, _abstract_match) in classified.family_matches.items()
                if title_match
            ],
            "keyword_abstract_hits": [
                family
                for family, (_title_match, abstract_match) in classified.family_matches.items()
                if abstract_match
            ],
        }

    missing_ids = sorted(set(known) - known_seen)
    denominator = len(known)
    present_denominator = len(known_seen)

    def count_audit(field: str, rows: Iterable[dict[str, Any]]) -> int:
        return sum(bool(row[field]) for row in rows)

    audit_rows = list(known_audit.values())
    category_counts = {
        category: {position: stats.papers for position, stats in sorted(positions.items())}
        for category, positions in sorted(category_stats.items())
    }
    category_keyword_counts = {
        category: {
            position: {
                "papers": stats.papers,
                "keywords": {
                    family: counts.as_dict() for family, counts in sorted(stats.keywords.items())
                },
            }
            for position, stats in sorted(positions.items())
        }
        for category, positions in sorted(category_stats.items())
    }
    ml_summary = {
        category: category_counts.get(category, {"primary": 0, "secondary": 0, "any": 0})
        for category in config.machine_learning_categories
    }
    recall = {
        "database_papers": denominator,
        "snapshot_present": present_denominator,
        "snapshot_missing": len(missing_ids),
        "category_gate": count_audit("ml_any", audit_rows),
        "keyword_union": count_audit("keyword_union", audit_rows),
        "combined_prefilter": count_audit("combined_prefilter", audit_rows),
        "category_gate_recall_all": (
            count_audit("ml_any", audit_rows) / denominator if denominator else 1.0
        ),
        "combined_recall_all": (
            count_audit("combined_prefilter", audit_rows) / denominator if denominator else 1.0
        ),
        "combined_recall_snapshot_present": (
            count_audit("combined_prefilter", audit_rows) / present_denominator
            if present_denominator
            else 1.0
        ),
    }
    return {
        "corpus": {
            "records": total_records,
            "date_min": min_date,
            "date_max": max_date,
            "duplicate_known_rows": duplicate_known_rows,
        },
        "machine_learning_categories": list(config.machine_learning_categories),
        "machine_learning_category_counts": ml_summary,
        "machine_learning_union_counts": ml_union_counts,
        "category_counts": category_counts,
        "category_keyword_counts": category_keyword_counts,
        "global_keyword_counts": {
            family: counts.as_dict() for family, counts in sorted(global_keywords.items())
        },
        "known_results_recall": recall,
        "snapshot_missing_known_ids": missing_ids,
        "known_results_audit": audit_rows,
    }


def write_reports(report: dict[str, Any], output_dir: Path, config: ScreeningConfig) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8"
    )

    fieldnames = [
        "category",
        "position",
        "papers",
        "keyword_family",
        "title_matches",
        "abstract_matches",
        "either_matches",
    ]
    with (output_dir / "category_keyword_counts.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        category_stats = report["category_keyword_counts"]
        for category, positions in category_stats.items():
            for position, position_stats in positions.items():
                for family, counts in position_stats["keywords"].items():
                    writer.writerow(
                        {
                            "category": category,
                            "position": position,
                            "papers": position_stats["papers"],
                            "keyword_family": family,
                            "title_matches": counts["title"],
                            "abstract_matches": counts["abstract"],
                            "either_matches": counts["either"],
                        }
                    )
        for family, counts in report["global_keyword_counts"].items():
            writer.writerow(
                {
                    "category": "__all__",
                    "position": "all",
                    "papers": report["corpus"]["records"],
                    "keyword_family": family,
                    "title_matches": counts["title"],
                    "abstract_matches": counts["abstract"],
                    "either_matches": counts["either"],
                }
            )

    audit_fields = [
        "arxiv_id",
        "title",
        "categories",
        "snapshot_date",
        "ml_primary",
        "ml_secondary",
        "ml_any",
        "keyword_union",
        "combined_prefilter",
        "keyword_hits",
        "keyword_title_hits",
        "keyword_abstract_hits",
    ]
    audit_rows = report["known_results_audit"]
    with (output_dir / "known_results_audit.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=audit_fields)
        writer.writeheader()
        for row in sorted(audit_rows, key=lambda item: item["arxiv_id"]):
            writer.writerow(
                {
                    **row,
                    "keyword_hits": ",".join(row["keyword_hits"]),
                    "keyword_title_hits": ",".join(row["keyword_title_hits"]),
                    "keyword_abstract_hits": ",".join(row["keyword_abstract_hits"]),
                }
            )

    missing = set(report["snapshot_missing_known_ids"])
    misses = [row for row in audit_rows if not row["combined_prefilter"]]
    with (output_dir / "known_results_misses.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=audit_fields + ["miss_reason"])
        writer.writeheader()
        for row in sorted(misses, key=lambda item: item["arxiv_id"]):
            reason = "not_in_ml_category" if not row["ml_any"] else "no_keyword_match"
            writer.writerow(
                {
                    **row,
                    "keyword_hits": ",".join(row["keyword_hits"]),
                    "keyword_title_hits": ",".join(row["keyword_title_hits"]),
                    "keyword_abstract_hits": ",".join(row["keyword_abstract_hits"]),
                    "miss_reason": reason,
                }
            )
        for arxiv_id in sorted(missing):
            writer.writerow(
                {
                    "arxiv_id": arxiv_id,
                    "miss_reason": "missing_from_snapshot",
                }
            )

    recall = report["known_results_recall"]
    lines = [
        "# arXiv metadata analysis",
        "",
        f"Snapshot records: **{report['corpus']['records']:,}**",
        f"Date range: **{report['corpus']['date_min']}** to **{report['corpus']['date_max']}**",
        "",
        "## Categories with keyword matches",
        "",
        "| Category | Primary | Secondary | Any position |",
        "|---|---:|---:|---:|",
    ]
    for category, positions in report["category_counts"].items():
        lines.append(
            f"| {category} | {positions.get('primary', 0):,} | "
            f"{positions.get('secondary', 0):,} | {positions.get('any', 0):,} |"
        )
    lines += ["", "## Keyword families by category", ""]
    for category, positions in report["category_keyword_counts"].items():
        lines += [
            f"### {category}",
            "",
            "| Position | Family | Title | Abstract | Either |",
            "|---|---|---:|---:|---:|",
        ]
        for position, position_stats in positions.items():
            for family, counts in position_stats["keywords"].items():
                lines.append(
                    f"| {position} | {family} | {counts['title']:,} | "
                    f"{counts['abstract']:,} | {counts['either']:,} |"
                )
        lines.append("")
    ml_union = report.get("machine_learning_union_counts", {})
    lines += [
        "",
        f"Union of ML categories: **{ml_union.get('any', 0):,}** papers "
        f"({ml_union.get('primary', 0):,} primary, {ml_union.get('secondary', 0):,} secondary; "
        f"{ml_union.get('both', 0):,} in both categories).",
    ]
    lines += [
        "",
        "## Database recall audit",
        "",
        f"Reference papers with stored results: **{recall['database_papers']:,}**",
        f"Present in snapshot: **{recall['snapshot_present']:,}**; missing: **{recall['snapshot_missing']:,}**",
        f"ML category gate: **{recall['category_gate']:,}**",
        f"Keyword union: **{recall['keyword_union']:,}**",
        f"Combined pre-filter: **{recall['combined_prefilter']:,}** "
        f"({recall['combined_recall_all']:.2%} of all known papers; "
        f"{recall['combined_recall_snapshot_present']:.2%} of snapshot-present papers)",
        "",
        "The CSV files contain the complete category and paper-level breakdowns, including every miss.",
        "",
    ]
    (output_dir / "summary.md").write_text("\n".join(lines), encoding="utf-8")


def merge_reports(
    report_paths: Iterable[Path], output_dir: Path, config: ScreeningConfig
) -> dict[str, Any]:
    """Merge independent line-chunk reports into one corpus report."""
    reports = [json.loads(path.read_text(encoding="utf-8")) for path in sorted(report_paths)]
    if not reports:
        raise ValueError("No chunk reports supplied")

    category_counts: dict[str, dict[str, int]] = {}
    category_keyword_counts: dict[str, dict[str, dict[str, Any]]] = {}
    global_keyword_counts = _empty_family_counts(config)
    ml_union_counts = {"any": 0, "primary": 0, "secondary": 0, "both": 0}
    audit_by_id: dict[str, dict[str, Any]] = {}
    missing_ids: set[str] | None = None
    corpus = {"records": 0, "date_min": "", "date_max": "", "duplicate_known_rows": 0}
    for report in reports:
        chunk_corpus = report["corpus"]
        corpus["records"] += chunk_corpus["records"]
        corpus["duplicate_known_rows"] += chunk_corpus.get("duplicate_known_rows", 0)
        if chunk_corpus.get("date_min") and (
            not corpus["date_min"] or chunk_corpus["date_min"] < corpus["date_min"]
        ):
            corpus["date_min"] = chunk_corpus["date_min"]
        if chunk_corpus.get("date_max") and chunk_corpus["date_max"] > corpus["date_max"]:
            corpus["date_max"] = chunk_corpus["date_max"]
        chunk_missing = set(report.get("snapshot_missing_known_ids", []))
        missing_ids = chunk_missing if missing_ids is None else missing_ids & chunk_missing
        for field_name in ml_union_counts:
            ml_union_counts[field_name] += report.get("machine_learning_union_counts", {}).get(
                field_name, 0
            )
        for row in report.get("known_results_audit", []):
            audit_by_id.setdefault(row["arxiv_id"], row)

        for category, positions in report["category_keyword_counts"].items():
            for position, position_stats in positions.items():
                target = category_keyword_counts.setdefault(category, {}).setdefault(
                    position,
                    {"papers": 0, "keywords": {}},
                )
                target["papers"] += position_stats["papers"]
                for family, counts in position_stats["keywords"].items():
                    family_target = target["keywords"].setdefault(
                        family, {"title": 0, "abstract": 0, "either": 0}
                    )
                    for field_name in ("title", "abstract", "either"):
                        family_target[field_name] += counts[field_name]
        for family, counts in report["global_keyword_counts"].items():
            global_keyword_counts[family].title += counts["title"]
            global_keyword_counts[family].abstract += counts["abstract"]
            global_keyword_counts[family].either += counts["either"]

    category_keyword_counts = {
        category: {
            position: {
                **position_stats,
                "keywords": {
                    family: counts
                    for family, counts in position_stats["keywords"].items()
                    if counts["title"] or counts["abstract"] or counts["either"]
                },
            }
            for position, position_stats in positions.items()
            if any(
                counts["title"] or counts["abstract"] or counts["either"]
                for counts in position_stats["keywords"].values()
            )
        }
        for category, positions in category_keyword_counts.items()
        if any(
            counts["title"] or counts["abstract"] or counts["either"]
            for position_stats in positions.values()
            for counts in position_stats["keywords"].values()
        )
    }
    category_counts = {
        category: {
            position: position_stats["papers"] for position, position_stats in positions.items()
        }
        for category, positions in category_keyword_counts.items()
    }
    audit_rows = list(audit_by_id.values())
    denominator = reports[0]["known_results_recall"]["database_papers"]
    snapshot_present = len(audit_rows)

    def audit_count(field_name: str) -> int:
        return sum(bool(row[field_name]) for row in audit_rows)

    recall = {
        "database_papers": denominator,
        "snapshot_present": snapshot_present,
        "snapshot_missing": denominator - snapshot_present,
        "category_gate": audit_count("ml_any"),
        "keyword_union": audit_count("keyword_union"),
        "combined_prefilter": audit_count("combined_prefilter"),
        "category_gate_recall_all": audit_count("ml_any") / denominator if denominator else 1.0,
        "combined_recall_all": (
            audit_count("combined_prefilter") / denominator if denominator else 1.0
        ),
        "combined_recall_snapshot_present": (
            audit_count("combined_prefilter") / snapshot_present if snapshot_present else 1.0
        ),
    }
    merged = {
        "corpus": corpus,
        "machine_learning_categories": list(config.machine_learning_categories),
        "machine_learning_category_counts": {
            category: category_counts.get(category, {"primary": 0, "secondary": 0, "any": 0})
            for category in config.machine_learning_categories
        },
        "machine_learning_union_counts": ml_union_counts,
        "category_counts": category_counts,
        "category_keyword_counts": category_keyword_counts,
        "global_keyword_counts": {
            family: counts.as_dict() for family, counts in sorted(global_keyword_counts.items())
        },
        "known_results_recall": recall,
        "snapshot_missing_known_ids": sorted(missing_ids or set()),
        "known_results_audit": audit_rows,
        "source": {"chunk_reports": [str(path) for path in sorted(report_paths)]},
    }
    write_reports(merged, output_dir, config)
    return merged


def download_manifest(
    path: Path,
    *,
    source: str,
    version: str | None,
    resolved_version: str | None = None,
) -> dict[str, Any]:
    return {
        "source": source,
        "requested_version": version or "latest",
        "resolved_version": resolved_version,
        "downloaded_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "path": str(path),
        "bytes": path.stat().st_size,
        "sha256": sha256_file(path),
    }
