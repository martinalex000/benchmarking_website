#!/usr/bin/env python3
"""Pre-screen keyword-matched papers from the Kaggle arXiv metadata snapshot.

The source is streamed into a small SQLite work queue so screening can follow a
deterministic tier/category order without loading the multi-gigabyte JSONL file
into memory. Final decisions are appended to a YAML document stream.

Usage::

    UV_CACHE_DIR=/tmp/benchmarking-uv-cache uv run python \
        scripts/prescreen_kaggle_arxiv.py --workers 8
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sqlite3
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import yaml
from rich.console import Console
from rich.table import Table
from tqdm import tqdm

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from backend.config import cfg
from backend.llm_extractor import LLMExtractor, ScreenResult

console = Console()

_DEFAULT_SOURCE = cfg.papers_dir / "arxiv-metadata-oai-snapshot.json"
_DEFAULT_SCREENING_DIR = cfg.papers_dir / "screening"
_DEFAULT_OUTPUT = _DEFAULT_SCREENING_DIR / "results.yaml"
_DEFAULT_QUEUE = _DEFAULT_SCREENING_DIR / "queue.sqlite3"
_DEFAULT_KEYWORDS = cfg.config_dir / "arxiv_prescreen_keywords.yaml"
_GENERAL_GRAPH_PATTERN = re.compile(r"(?<!\w)graph(?!\w)", re.IGNORECASE)
_INDEX_PROGRESS_INTERVAL = 10_000
_SCHEMA_VERSION = 1
_FAST_HASH_CHUNK_SIZE = 1 << 20
_thread_state = threading.local()


@dataclass(frozen=True)
class KeywordMatcher:
    """Compiled matchers for the specific and general screening tiers."""

    specific: re.Pattern[str]
    graph: re.Pattern[str]
    canonical_keywords: dict[str, str]


@dataclass(frozen=True)
class WorkItem:
    arxiv_id: str
    title: str
    abstract: str
    tier: str
    matched_keywords: list[str]


@dataclass
class ResultSummary:
    arxiv_ids: set[str]
    accepted: int = 0
    rejected: int = 0

    @property
    def processed(self) -> int:
        return self.accepted + self.rejected


@dataclass(frozen=True)
class RequestUsage:
    """Usage reported by one completed screening request."""

    worker: str
    duration_s: float
    prompt_tokens: int | None
    completion_tokens: int | None


@dataclass
class WorkerUsage:
    requests: int = 0
    duration_s: float = 0.0
    prompt_tokens: int = 0
    completion_tokens: int = 0
    prompt_requests: int = 0
    completion_requests: int = 0

    def add(self, usage: RequestUsage) -> None:
        self.requests += 1
        self.duration_s += usage.duration_s
        if usage.prompt_tokens is not None:
            self.prompt_tokens += usage.prompt_tokens
            self.prompt_requests += 1
        if usage.completion_tokens is not None:
            self.completion_tokens += usage.completion_tokens
            self.completion_requests += 1


@dataclass
class LLMUsage:
    workers: dict[str, WorkerUsage]

    def __init__(self) -> None:
        self.workers = {}

    def add(self, usage: RequestUsage) -> None:
        self.workers.setdefault(usage.worker, WorkerUsage()).add(usage)

    @property
    def requests(self) -> int:
        return sum(worker.requests for worker in self.workers.values())

    @property
    def duration_s(self) -> float:
        return sum(worker.duration_s for worker in self.workers.values())

    @property
    def prompt_tokens(self) -> int:
        return sum(worker.prompt_tokens for worker in self.workers.values())

    @property
    def completion_tokens(self) -> int:
        return sum(worker.completion_tokens for worker in self.workers.values())

    @property
    def prompt_requests(self) -> int:
        return sum(worker.prompt_requests for worker in self.workers.values())

    @property
    def completion_requests(self) -> int:
        return sum(worker.completion_requests for worker in self.workers.values())


def load_specific_keywords(path: Path) -> list[str]:
    """Load a de-duplicated, ordered list of specific keywords."""
    payload = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    raw_keywords = payload.get("specific_keywords")
    if not isinstance(raw_keywords, list) or not raw_keywords:
        raise ValueError(f"{path} must contain a non-empty 'specific_keywords' list")

    keywords: list[str] = []
    seen: set[str] = set()
    for raw_keyword in raw_keywords:
        keyword = str(raw_keyword).strip()
        normalized = keyword.casefold()
        if not keyword or normalized in seen:
            continue
        seen.add(normalized)
        keywords.append(keyword)
    if not keywords:
        raise ValueError(f"{path} does not contain any usable keywords")
    return keywords


def compile_keyword_patterns(keywords: list[str]) -> KeywordMatcher:
    """Compile one case-insensitive alternation for all specific keywords."""
    unique_keywords = list(dict.fromkeys(keywords))
    alternatives = []
    canonical_keywords: dict[str, str] = {}
    for keyword in unique_keywords:
        escaped = re.escape(keyword).replace(r"\ ", r"\s+")
        alternatives.append(escaped)
        canonical_keywords[" ".join(keyword.casefold().split())] = keyword

    # Longer alternatives first prevents a short phrase from winning when both match.
    alternatives.sort(key=len, reverse=True)
    specific = re.compile(
        rf"(?<!\w)(?:{'|'.join(alternatives)})(?!\w)",
        re.IGNORECASE,
    )
    return KeywordMatcher(
        specific=specific,
        graph=_GENERAL_GRAPH_PATTERN,
        canonical_keywords=canonical_keywords,
    )


def match_tier(
    title: str,
    abstract: str,
    matcher: KeywordMatcher,
) -> tuple[str, list[str]] | None:
    """Return the highest-priority matching tier and its keywords."""
    text = f"{title}\n{abstract}"
    matched: list[str] = []
    seen: set[str] = set()
    for found in matcher.specific.finditer(text):
        normalized = " ".join(found.group(0).casefold().split())
        keyword = matcher.canonical_keywords.get(normalized, found.group(0))
        if keyword.casefold() not in seen:
            seen.add(keyword.casefold())
            matched.append(keyword)
    if matched:
        return "specific", matched
    if matcher.graph.search(text):
        return "graph", ["graph"]
    return None


def processing_bucket(categories: str) -> str:
    """Put all cs.LG cross-lists first, otherwise use the primary category."""
    category_list = categories.split()
    if "cs.LG" in category_list:
        return "cs.LG"
    return category_list[0] if category_list else "uncategorized"


def _source_fingerprint(source: Path, keywords: list[str]) -> str:
    stat = source.stat()
    fast_hash = _fast_file_hash(source, stat.st_size)
    payload = json.dumps(
        {
            "source": str(source.resolve()),
            "size": stat.st_size,
            "fast_hash": fast_hash,
            "keywords": keywords,
            "index_version": 1,
        },
        sort_keys=True,
    )
    return hashlib.sha256(payload.encode()).hexdigest()


def _fast_file_hash(source: Path, size: int) -> str:
    """Hash bounded samples from the file so mtime-only changes do not invalidate it."""
    if size <= 0:
        return hashlib.blake2b(b"", digest_size=16).hexdigest()

    offsets = {
        0,
        max(0, size // 2 - _FAST_HASH_CHUNK_SIZE // 2),
        max(0, size - _FAST_HASH_CHUNK_SIZE),
    }
    digest = hashlib.blake2b(digest_size=16)
    with source.open("rb") as source_file:
        for offset in sorted(offsets):
            source_file.seek(offset)
            digest.update(source_file.read(_FAST_HASH_CHUNK_SIZE))
    return digest.hexdigest()


class WorkQueue:
    """SQLite-backed candidate index and resumable work state."""

    def __init__(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        self.connection = sqlite3.connect(path)
        self.connection.row_factory = sqlite3.Row
        self.connection.execute(
            "CREATE TABLE IF NOT EXISTS metadata (key TEXT PRIMARY KEY, value TEXT NOT NULL)"
        )
        self._create_papers_table()

    def close(self) -> None:
        self.connection.close()

    def _create_papers_table(self) -> None:
        self.connection.executescript(
            """
            CREATE TABLE IF NOT EXISTS papers (
                arxiv_id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                abstract TEXT NOT NULL,
                tier TEXT NOT NULL,
                matched_keywords TEXT NOT NULL,
                bucket TEXT NOT NULL,
                bucket_priority INTEGER NOT NULL,
                status TEXT NOT NULL DEFAULT 'pending',
                attempts INTEGER NOT NULL DEFAULT 0,
                last_error TEXT
            );
            CREATE INDEX IF NOT EXISTS idx_screening_work
                ON papers(tier, bucket_priority, bucket, status, arxiv_id);
            """
        )
        self.connection.commit()

    def _metadata(self, key: str) -> str | None:
        row = self.connection.execute("SELECT value FROM metadata WHERE key = ?", (key,)).fetchone()
        return str(row["value"]) if row else None

    def is_current(self, fingerprint: str) -> bool:
        return (
            self._metadata("fingerprint") == fingerprint and self._metadata("index_complete") == "1"
        )

    def rebuild(
        self,
        source: Path,
        matcher: KeywordMatcher,
        fingerprint: str,
    ) -> tuple[int, int]:
        """Stream the source and replace the derived candidate index."""
        self.connection.execute("DELETE FROM papers")
        self.connection.execute("DELETE FROM metadata")
        self.connection.commit()

        matched_count = 0
        malformed_count = 0
        with (
            source.open("r", encoding="utf-8") as source_file,
            tqdm(source_file, desc="Indexing arXiv snapshot", unit="paper") as progress,
        ):
            for line_number, line in enumerate(progress, 1):
                try:
                    paper = json.loads(line)
                    if not isinstance(paper, dict):
                        raise TypeError("paper row must be an object")
                    arxiv_id = str(paper["id"] or "").strip()
                    if not arxiv_id:
                        raise ValueError("paper row has no arXiv ID")
                    title = str(paper.get("title") or "").strip()
                    abstract = str(paper.get("abstract") or "").strip()
                except (json.JSONDecodeError, KeyError, TypeError, ValueError):
                    malformed_count += 1
                    continue

                match = match_tier(title, abstract, matcher)
                if match is not None:
                    tier, matched_keywords = match
                    bucket = processing_bucket(str(paper.get("categories") or ""))
                    self.connection.execute(
                        """
                        INSERT OR REPLACE INTO papers (
                            arxiv_id, title, abstract, tier, matched_keywords,
                            bucket, bucket_priority, status
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, 'pending')
                        """,
                        (
                            arxiv_id,
                            title,
                            abstract,
                            tier,
                            json.dumps(matched_keywords),
                            bucket,
                            0 if bucket == "cs.LG" else 1,
                        ),
                    )
                    matched_count += 1

                if line_number % _INDEX_PROGRESS_INTERVAL == 0:
                    self.connection.commit()
                    progress.set_postfix(matches=f"{matched_count:,}", refresh=False)

        self.connection.execute(
            "INSERT INTO metadata(key, value) VALUES ('fingerprint', ?)", (fingerprint,)
        )
        self.connection.execute("INSERT INTO metadata(key, value) VALUES ('index_complete', '1')")
        self.connection.commit()
        return matched_count, malformed_count

    def reconcile(self, completed_ids: set[str]) -> None:
        """Apply the YAML stream as the source of truth after an interrupted run."""
        self.connection.execute("UPDATE papers SET status = 'pending' WHERE status = 'error'")
        self.connection.executemany(
            "UPDATE papers SET status = 'done', last_error = NULL WHERE arxiv_id = ?",
            ((arxiv_id,) for arxiv_id in completed_ids),
        )
        self.connection.commit()

    def buckets(self) -> list[tuple[str, str]]:
        rows = self.connection.execute(
            """
            SELECT tier, bucket, MIN(bucket_priority) AS priority
            FROM papers
            WHERE status = 'pending'
            GROUP BY tier, bucket
            ORDER BY CASE tier WHEN 'specific' THEN 0 ELSE 1 END, priority, bucket
            """
        ).fetchall()
        return [(str(row["tier"]), str(row["bucket"])) for row in rows]

    def fetch(self, tier: str, bucket: str, limit: int) -> list[WorkItem]:
        rows = self.connection.execute(
            """
            SELECT arxiv_id, title, abstract, tier, matched_keywords
            FROM papers
            WHERE status = 'pending' AND tier = ? AND bucket = ?
            ORDER BY attempts DESC, arxiv_id
            LIMIT ?
            """,
            (tier, bucket, limit),
        ).fetchall()
        return [
            WorkItem(
                arxiv_id=str(row["arxiv_id"]),
                title=str(row["title"]),
                abstract=str(row["abstract"]),
                tier=str(row["tier"]),
                matched_keywords=json.loads(row["matched_keywords"]),
            )
            for row in rows
        ]

    def mark_done(self, arxiv_id: str) -> None:
        self.connection.execute(
            """
            UPDATE papers
            SET status = 'done', attempts = attempts + 1, last_error = NULL
            WHERE arxiv_id = ?
            """,
            (arxiv_id,),
        )
        self.connection.commit()

    def mark_error(self, arxiv_id: str, error: str) -> None:
        self.connection.execute(
            """
            UPDATE papers
            SET status = 'error', attempts = attempts + 1, last_error = ?
            WHERE arxiv_id = ?
            """,
            (error[:2_000], arxiv_id),
        )
        self.connection.commit()

    def pending_count(self) -> int:
        row = self.connection.execute(
            "SELECT COUNT(*) AS count FROM papers WHERE status != 'done'"
        ).fetchone()
        return int(row["count"])

    def remaining_breakdown(self) -> dict[tuple[str, str], int]:
        """Return pending counts by screening stage and cs.LG/other category."""
        rows = self.connection.execute(
            """
            SELECT tier,
                   CASE WHEN bucket = 'cs.LG' THEN 'cs.LG' ELSE 'other' END AS category,
                   COUNT(*) AS count
            FROM papers
            WHERE status = 'pending'
            GROUP BY tier, category
            """
        ).fetchall()
        return {(str(row["tier"]), str(row["category"])): int(row["count"]) for row in rows}

    def bucket_pending_count(self, tier: str, bucket: str) -> int:
        row = self.connection.execute(
            """
            SELECT COUNT(*) AS count FROM papers
            WHERE status = 'pending' AND tier = ? AND bucket = ?
            """,
            (tier, bucket),
        ).fetchone()
        return int(row["count"])


def _parse_yaml_document(raw: bytes, path: Path) -> dict[str, Any]:
    payload = yaml.safe_load(raw.decode("utf-8"))
    if not isinstance(payload, dict) or not payload.get("arxiv_id"):
        raise ValueError(f"Invalid screening result document in {path}")
    return payload


def load_results(path: Path) -> ResultSummary:
    """Load completed IDs and truncate only an incomplete trailing document."""
    summary = ResultSummary(arxiv_ids=set())
    if not path.exists():
        return summary

    def add_document(raw: bytes) -> None:
        payload = _parse_yaml_document(raw, path)
        arxiv_id = str(payload["arxiv_id"])
        if arxiv_id in summary.arxiv_ids:
            raise ValueError(f"Duplicate result for arXiv:{arxiv_id} in {path}")
        summary.arxiv_ids.add(arxiv_id)
        decision = payload.get("decision")
        if decision == "accepted":
            summary.accepted += 1
        elif decision == "rejected":
            summary.rejected += 1
        else:
            raise ValueError(f"Invalid decision for arXiv:{arxiv_id} in {path}")

    with path.open("r+b") as result_file:
        document_start: int | None = None
        document = bytearray()
        while True:
            line_start = result_file.tell()
            line = result_file.readline()
            if not line:
                if document_start is not None and document:
                    complete = document.rstrip().endswith(b"...")
                    try:
                        if not complete:
                            raise ValueError("incomplete YAML document")
                        add_document(bytes(document))
                    except (UnicodeDecodeError, yaml.YAMLError, ValueError):
                        result_file.seek(document_start)
                        result_file.truncate()
                        console.print(
                            f"[yellow]Removed an incomplete trailing YAML document from {path}[/yellow]"
                        )
                break

            if line.strip() == b"---":
                if document_start is not None:
                    if not document.rstrip().endswith(b"..."):
                        raise ValueError(f"Incomplete non-final YAML document in {path}")
                    add_document(bytes(document))
                document_start = line_start
                document = bytearray(line)
            elif document_start is None:
                if line.strip():
                    raise ValueError(f"Unexpected content before first YAML document in {path}")
            else:
                document.extend(line)

    return summary


def append_result(
    path: Path,
    item: WorkItem,
    result: ScreenResult,
    model_name: str,
) -> str:
    """Append one minimal, self-contained result document."""
    accepted = result.has_benchmark_results or result.has_new_benchmark
    decision = "accepted" if accepted else "rejected"
    payload = {
        "schema_version": _SCHEMA_VERSION,
        "arxiv_id": item.arxiv_id,
        "matched_tier": item.tier,
        "matched_keywords": item.matched_keywords,
        "decision": decision,
        "has_benchmark_results": result.has_benchmark_results,
        "has_new_benchmark": result.has_new_benchmark,
        "datasets_mentioned": result.datasets_mentioned,
        "confidence": result.confidence,
        "reason": result.notes,
        "model": model_name,
        "screened_at": datetime.now(UTC).isoformat(),
    }
    rendered = yaml.safe_dump(
        payload,
        allow_unicode=True,
        sort_keys=False,
        explicit_start=True,
        explicit_end=True,
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as result_file:
        result_file.write(rendered)
        result_file.flush()
        os.fsync(result_file.fileno())
    return decision


def _screen(item: WorkItem) -> tuple[ScreenResult, str, RequestUsage]:
    extractor = getattr(_thread_state, "extractor", None)
    if extractor is None:
        extractor = LLMExtractor(model_tier="small")
        _thread_state.extractor = extractor
    try:
        result = extractor.screen_paper(item.title, item.abstract, fail_open=False)
        record = extractor._call_log[-1]
        usage = RequestUsage(
            worker=threading.current_thread().name,
            duration_s=record.duration_s,
            prompt_tokens=record.prompt_tokens,
            completion_tokens=record.completion_tokens,
        )
        return result, extractor.model_name, usage
    finally:
        # Call records contain the full prompt and would otherwise grow for the entire scan.
        extractor._call_log.clear()
        extractor._last_progress_idx = -1


def _print_progress(
    summary: ResultSummary,
    *,
    errors: int,
    remaining: int,
    run_attempts: int,
    started_at: float,
    llm_usage: LLMUsage,
) -> None:
    elapsed = max(time.monotonic() - started_at, 0.001)
    rate = run_attempts / elapsed
    console.print(
        f"  Processed [cyan]{summary.processed:,}[/cyan] total — "
        f"[green]{summary.accepted:,} accepted[/green], "
        f"[yellow]{summary.rejected:,} rejected[/yellow], "
        f"[red]{errors:,} errors this run[/red], {remaining:,} remaining "
        f"([cyan]{rate:.2f} papers/s[/cyan])"
    )
    _print_llm_usage(llm_usage, wall_elapsed=elapsed)


def _rate(tokens: int, duration_s: float) -> str:
    return f"{tokens / duration_s:.1f}" if duration_s > 0 else "0.0"


def _average(tokens: int, requests: int) -> str:
    return f"{tokens / requests:.1f}" if requests else "?"


def _print_llm_usage(llm_usage: LLMUsage, *, wall_elapsed: float) -> None:
    """Print aggregate and per-worker token usage for completed requests."""
    if not llm_usage.requests:
        console.print("  LLM usage: no completed requests with usage recorded yet")
        return

    wall_elapsed = max(wall_elapsed, 0.001)
    console.print(
        "  LLM usage: "
        f"{llm_usage.requests:,} requests; "
        f"input {llm_usage.prompt_tokens:,} tokens ({_rate(llm_usage.prompt_tokens, wall_elapsed)} tok/s wall), "
        f"output {llm_usage.completion_tokens:,} tokens "
        f"({_rate(llm_usage.completion_tokens, wall_elapsed)} tok/s wall); "
        f"average {_average(llm_usage.prompt_tokens, llm_usage.prompt_requests)} input + "
        f"{_average(llm_usage.completion_tokens, llm_usage.completion_requests)} output/request"
    )

    table = Table(title="LLM usage by worker")
    table.add_column("Worker")
    table.add_column("Requests", justify="right")
    table.add_column("Input tok/s", justify="right")
    table.add_column("Output tok/s", justify="right")
    table.add_column("Avg in/out", justify="right")
    for worker_name, worker in sorted(llm_usage.workers.items()):
        table.add_row(
            worker_name,
            f"{worker.requests:,}",
            _rate(worker.prompt_tokens, worker.duration_s),
            _rate(worker.completion_tokens, worker.duration_s),
            f"{_average(worker.prompt_tokens, worker.prompt_requests)} / "
            f"{_average(worker.completion_tokens, worker.completion_requests)}",
        )
    console.print(table)


def _print_remaining_breakdown(queue: WorkQueue) -> None:
    """Print the candidate counts before dispatching any screening requests."""
    counts = queue.remaining_breakdown()
    table = Table(title="Remaining papers before screening")
    table.add_column("Stage")
    table.add_column("cs.LG", justify="right")
    table.add_column("other", justify="right")
    table.add_column("total", justify="right")

    stage_labels = [("specific", "specialized"), ("graph", "graph")]
    column_totals = {"cs.LG": 0, "other": 0}
    for tier, label in stage_labels:
        stage_counts = {category: counts.get((tier, category), 0) for category in column_totals}
        column_totals["cs.LG"] += stage_counts["cs.LG"]
        column_totals["other"] += stage_counts["other"]
        row_total = sum(stage_counts.values())
        table.add_row(
            label,
            f"{stage_counts['cs.LG']:,}",
            f"{stage_counts['other']:,}",
            f"{row_total:,}",
        )

    grand_total = sum(column_totals.values())
    table.add_row(
        "total",
        f"{column_totals['cs.LG']:,}",
        f"{column_totals['other']:,}",
        f"{grand_total:,}",
    )
    console.print(table)


def run_screening(
    *,
    source: Path,
    output: Path,
    queue_path: Path,
    keywords_path: Path,
    workers: int,
    progress_every: int,
    max_papers: int,
    force_reindex: bool = False,
) -> ResultSummary:
    """Index the snapshot as needed, then screen candidates in priority order."""
    if not source.is_file():
        raise FileNotFoundError(f"Kaggle arXiv snapshot not found: {source}")

    keywords = load_specific_keywords(keywords_path)
    matcher = compile_keyword_patterns(keywords)
    fingerprint = _source_fingerprint(source, keywords)
    queue = WorkQueue(queue_path)
    try:
        if force_reindex or not queue.is_current(fingerprint):
            console.print(f"[bold]Indexing keyword matches from {source}[/bold]")
            matched, malformed = queue.rebuild(source, matcher, fingerprint)
            console.print(
                f"  Index complete: [cyan]{matched:,} matches[/cyan], "
                f"[yellow]{malformed:,} malformed rows skipped[/yellow]"
            )
        else:
            console.print(f"[dim]Reusing screening index at {queue_path}[/dim]")

        summary = load_results(output)
        queue.reconcile(summary.arxiv_ids)
        _print_remaining_breakdown(queue)
        console.print(
            f"[bold]Screening with {cfg.model_for_tier('small')}[/bold] using "
            f"{workers} worker(s); {queue.pending_count():,} papers remaining"
        )

        started_at = time.monotonic()
        run_attempts = 0
        errors = 0
        llm_usage = LLMUsage()
        batch_size = max(1, workers * 2)

        with ThreadPoolExecutor(max_workers=workers) as executor:
            for tier, bucket in queue.buckets():
                if max_papers and run_attempts >= max_papers:
                    break
                bucket_count = queue.bucket_pending_count(tier, bucket)
                console.print(
                    f"\n[bold]{tier}[/bold] / [cyan]{bucket}[/cyan]: {bucket_count:,} pending"
                )

                while True:
                    remaining_limit = max_papers - run_attempts if max_papers else batch_size
                    if max_papers and remaining_limit <= 0:
                        break
                    items = queue.fetch(tier, bucket, min(batch_size, remaining_limit))
                    if not items:
                        break

                    future_items = {executor.submit(_screen, item): item for item in items}
                    for future in as_completed(future_items):
                        item = future_items[future]
                        run_attempts += 1
                        try:
                            result, model_name, usage = future.result()
                            llm_usage.add(usage)
                            decision = append_result(output, item, result, model_name)
                            queue.mark_done(item.arxiv_id)
                            summary.arxiv_ids.add(item.arxiv_id)
                            if decision == "accepted":
                                summary.accepted += 1
                            else:
                                summary.rejected += 1
                        except Exception as exc:
                            errors += 1
                            queue.mark_error(item.arxiv_id, f"{type(exc).__name__}: {exc}")
                            console.print(
                                f"  [red]Error[/red] arXiv:{item.arxiv_id}: "
                                f"{type(exc).__name__}: {exc}"
                            )

                        if run_attempts % progress_every == 0:
                            _print_progress(
                                summary,
                                errors=errors,
                                remaining=queue.pending_count(),
                                run_attempts=run_attempts,
                                started_at=started_at,
                                llm_usage=llm_usage,
                            )

                if max_papers and run_attempts >= max_papers:
                    break

        _print_progress(
            summary,
            errors=errors,
            remaining=queue.pending_count(),
            run_attempts=run_attempts,
            started_at=started_at,
            llm_usage=llm_usage,
        )
        if errors:
            console.print(
                "[yellow]Failed papers remain retryable and will be attempted first on restart.[/yellow]"
            )
        return summary
    finally:
        queue.close()


def _positive_int(value: str) -> int:
    parsed = int(value)
    if parsed < 1:
        raise argparse.ArgumentTypeError("must be at least 1")
    return parsed


def _non_negative_int(value: str) -> int:
    parsed = int(value)
    if parsed < 0:
        raise argparse.ArgumentTypeError("must be at least 0")
    return parsed


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Pre-screen keyword-matched Kaggle arXiv papers with the fast model"
    )
    parser.add_argument("--source", type=Path, default=_DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path, default=_DEFAULT_OUTPUT)
    parser.add_argument("--queue", type=Path, default=_DEFAULT_QUEUE)
    parser.add_argument("--keywords", type=Path, default=_DEFAULT_KEYWORDS)
    parser.add_argument("--workers", type=_positive_int, default=1)
    parser.add_argument("--progress-every", type=_positive_int, default=25, metavar="N")
    parser.add_argument(
        "--max-papers",
        type=_non_negative_int,
        default=0,
        metavar="N",
        help="Stop after N requests in this run; 0 means unlimited",
    )
    parser.add_argument(
        "--reindex",
        action="store_true",
        help="Rebuild the derived keyword index even when the source is unchanged",
    )
    return parser


def main(argv: list[str] | None = None) -> None:
    args = build_parser().parse_args(argv)
    run_screening(
        source=args.source,
        output=args.output,
        queue_path=args.queue,
        keywords_path=args.keywords,
        workers=args.workers,
        progress_every=args.progress_every,
        max_papers=args.max_papers,
        force_reindex=args.reindex,
    )


if __name__ == "__main__":
    main()
