"""Profile Hugo export performance on a random sample of papers and datasets.

Phase 1: wall-clock timings (default).
Phase 2: line_profiler stats on slowest items (--line-profile).
Phase 3: focused line_profiler on hot functions (--deep-profile).

Usage::

    uv run python scripts/profile_export.py --papers 20 --datasets 10 --seed 42
    uv run python scripts/profile_export.py --line-profile --report /tmp/export_profile.json
    uv run python scripts/profile_export.py --deep-profile
    uv run kernprof -l -v scripts/profile_export.py -- --deep-profile
"""

from __future__ import annotations

import argparse
import json
import random
import statistics
import sys
import tempfile
import time
from datetime import UTC, datetime
from io import StringIO
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from backend import baseline_aggregator, export_to_hugo
from backend.db import init_db, session_scope
from backend.models import Dataset, Paper, Result
from backend.paper_storage import PaperStorage

# Fixtures used for deep profiling (seed-42 slowest items).
DEEP_PROFILE_PAPER = "2410.10320"
DEEP_PROFILE_DATASET_ID = 51

LINE_PROFILE_FUNCTIONS = (
    export_to_hugo.export_paper,
    export_to_hugo.export_dataset,
    export_to_hugo.export_benchmarks_data,
    export_to_hugo._dataset_page_export_metadata,
    export_to_hugo._global_ranks_for_dataset,
    export_to_hugo._compute_paper_mrr,
    export_to_hugo._build_multi_metric_rows,
    export_to_hugo._write_md,
    baseline_aggregator.get_best_results_over_time,
    PaperStorage.load_llm_output,
)

DEEP_PROFILE_SCENARIOS: tuple[tuple[str, tuple[Any, ...]], ...] = (
    (
        "load_llm_output_via_global_ranks",
        (export_to_hugo._global_ranks_for_dataset, PaperStorage.load_llm_output),
    ),
    ("export_paper", (export_to_hugo.export_paper,)),
    (
        "dataset_page_export_metadata",
        (
            export_to_hugo._dataset_page_export_metadata,
            export_to_hugo._build_multi_metric_rows,
            PaperStorage.load_llm_output,
        ),
    ),
)


def _configure_export_site(site_dir: Path) -> None:
    site_dir.mkdir(parents=True, exist_ok=True)
    export_to_hugo._SITE_DIR = site_dir
    export_to_hugo._CONTENT = site_dir / "content"
    export_to_hugo._DATA_DIR = site_dir / "data"
    export_to_hugo._STATIC = site_dir / "static"
    export_to_hugo._CONTENT.mkdir(parents=True, exist_ok=True)
    export_to_hugo._DATA_DIR.mkdir(parents=True, exist_ok=True)
    export_to_hugo._STATIC.mkdir(parents=True, exist_ok=True)


def _clear_export_caches() -> None:
    export_to_hugo.clear_export_caches()


def _summary_stats(values: list[float]) -> dict[str, float | int]:
    if not values:
        return {
            "count": 0,
            "total": 0.0,
            "mean": 0.0,
            "median": 0.0,
            "p90": 0.0,
            "p99": 0.0,
            "max": 0.0,
        }
    ordered = sorted(values)
    n = len(ordered)

    def _percentile(p: float) -> float:
        if n == 1:
            return ordered[0]
        idx = min(n - 1, max(0, int(round((n - 1) * p))))
        return ordered[idx]

    return {
        "count": n,
        "total": sum(ordered),
        "mean": statistics.mean(ordered),
        "median": statistics.median(ordered),
        "p90": _percentile(0.9),
        "p99": _percentile(0.99),
        "max": ordered[-1],
    }


def _paper_metrics(arxiv_id: str) -> dict[str, int]:
    with session_scope() as session:
        paper = session.query(Paper).filter_by(arxiv_id=arxiv_id).first()
        if paper is None:
            return {"result_count": 0, "dataset_count": 0}
        results = (
            session.query(Result)
            .filter_by(paper_id=paper.id)
            .filter(Result.is_problematic.is_(None) | (Result.is_problematic == 0))
            .all()
        )
        datasets = {
            r.dataset_variant.dataset.name
            for r in results
            if r.dataset_variant and r.dataset_variant.dataset
        }
        return {"result_count": len(results), "dataset_count": len(datasets)}


def _dataset_metrics(dataset_id: int) -> dict[str, Any]:
    with session_scope() as session:
        ds = session.get(Dataset, dataset_id)
        if ds is None:
            return {"name": "", "row_count": 0, "output_bytes": 0}
        meta = export_to_hugo._dataset_page_export_metadata(session, dataset_id)
        slug = export_to_hugo._slug(ds.name)
        out_path = export_to_hugo._CONTENT / "datasets" / slug / "index.md"
        output_bytes = out_path.stat().st_size if out_path.exists() else 0
        return {
            "name": ds.name,
            "row_count": int(meta.get("result_count", 0)),
            "output_bytes": output_bytes,
        }


def _sample_ids(
    paper_count: int,
    dataset_count: int,
    seed: int,
) -> tuple[list[str], list[int], dict[str, int]]:
    init_db()
    with session_scope() as session:
        all_papers = [p.arxiv_id for p in session.query(Paper).all()]
        all_datasets = [d.id for d in session.query(Dataset).all()]
        db_counts = {
            "papers": len(all_papers),
            "datasets": len(all_datasets),
        }
    rng = random.Random(seed)
    papers = rng.sample(all_papers, min(paper_count, len(all_papers)))
    datasets = rng.sample(all_datasets, min(dataset_count, len(all_datasets)))
    return papers, datasets, db_counts


def _run_wall_clock_sample(
    paper_ids: list[str],
    dataset_ids: list[int],
    *,
    all_dataset_ids: list[int],
    skip_benchmarks: bool,
    skip_dev: bool,
    production_order: bool = True,
) -> dict[str, Any]:
    """Wall-clock timings; default order matches ``export_all`` (cache warm for benchmarks)."""
    phases: dict[str, Any] = {}
    paper_rows: list[dict[str, Any]] = []
    dataset_rows: list[dict[str, Any]] = []

    _clear_export_caches()
    dataset_export_ids = all_dataset_ids if production_order else dataset_ids

    def _time_datasets(export_ids: list[int]) -> None:
        for dataset_id in export_ids:
            t0 = time.perf_counter()
            ok = export_to_hugo.export_dataset(dataset_id)
            dataset_rows.append(
                {
                    "dataset_id": dataset_id,
                    "seconds": time.perf_counter() - t0,
                    "ok": ok,
                    **_dataset_metrics(dataset_id),
                }
            )

    def _time_papers() -> None:
        for arxiv_id in paper_ids:
            metrics = _paper_metrics(arxiv_id)
            t0 = time.perf_counter()
            ok = export_to_hugo.export_paper(arxiv_id)
            paper_rows.append(
                {
                    "arxiv_id": arxiv_id,
                    "seconds": time.perf_counter() - t0,
                    "ok": ok,
                    **metrics,
                }
            )

    if production_order:
        t0 = time.perf_counter()
        _time_datasets(dataset_export_ids)
        phases["datasets"] = {
            "seconds": time.perf_counter() - t0,
            "count": len(dataset_export_ids),
        }

        if not skip_benchmarks:
            t0 = time.perf_counter()
            export_to_hugo.export_benchmarks_data()
            phases["benchmarks"] = {"seconds": time.perf_counter() - t0}

        t0 = time.perf_counter()
        _time_papers()
        phases["papers"] = {"seconds": time.perf_counter() - t0}

        if not skip_dev:
            t0 = time.perf_counter()
            export_to_hugo.export_development_data()
            phases["development"] = {"seconds": time.perf_counter() - t0}
    else:
        if not skip_benchmarks:
            t0 = time.perf_counter()
            export_to_hugo.export_benchmarks_data()
            phases["benchmarks"] = {"seconds": time.perf_counter() - t0}

        if not skip_dev:
            t0 = time.perf_counter()
            export_to_hugo.export_development_data()
            phases["development"] = {"seconds": time.perf_counter() - t0}

        t0 = time.perf_counter()
        _time_papers()
        phases["papers"] = {"seconds": time.perf_counter() - t0}

        t0 = time.perf_counter()
        _time_datasets(dataset_ids)
        phases["datasets"] = {"seconds": time.perf_counter() - t0, "count": len(dataset_ids)}

    paper_times = [r["seconds"] for r in paper_rows]
    dataset_times = [r["seconds"] for r in dataset_rows]
    paper_rows_sorted = sorted(paper_rows, key=lambda r: r["seconds"], reverse=True)
    dataset_rows_sorted = sorted(dataset_rows, key=lambda r: r["seconds"], reverse=True)

    return {
        "phases": phases,
        "papers": paper_rows,
        "datasets": dataset_rows,
        "summary": {
            "papers": _summary_stats(paper_times),
            "datasets": _summary_stats(dataset_times),
        },
        "slowest": {
            "paper": paper_rows_sorted[0] if paper_rows_sorted else None,
            "dataset": dataset_rows_sorted[0] if dataset_rows_sorted else None,
        },
        "top5_papers": paper_rows_sorted[:5],
        "top5_datasets": dataset_rows_sorted[:5],
    }


def _build_line_profiler(*functions: Any) -> Any:
    from line_profiler import LineProfiler

    lp = LineProfiler()
    fns = functions if functions else LINE_PROFILE_FUNCTIONS
    for fn in fns:
        lp.add_function(fn)
    return lp


def _profile_capture(
    label: str, run_fn: Any, *, functions: tuple[Any, ...] = ()
) -> tuple[float, str]:
    """Run *run_fn* under line_profiler; return wall seconds and stats text."""
    _clear_export_caches()
    lp = _build_line_profiler(*functions) if functions else _build_line_profiler()
    buf = StringIO()
    buf.write(f"\n{'=' * 72}\n{label}\n{'=' * 72}\n")
    t0 = time.perf_counter()
    lp.enable()
    try:
        run_fn()
    finally:
        lp.disable()
    elapsed = time.perf_counter() - t0
    lp.print_stats(stream=buf, stripzeros=True)
    return elapsed, buf.getvalue()


def _paper_dataset_names(arxiv_id: str) -> list[tuple[str, str, bool]]:
    """Return (dataset_name, primary_metric, higher_is_better) for a paper's results."""
    with session_scope() as session:
        paper = session.query(Paper).filter_by(arxiv_id=arxiv_id).first()
        if paper is None:
            return []
        results = (
            session.query(Result)
            .filter_by(paper_id=paper.id)
            .filter(Result.is_problematic.is_(None) | (Result.is_problematic == 0))
            .all()
        )
        meta: dict[str, tuple[str, bool]] = {}
        for r in results:
            dv = r.dataset_variant
            if not dv or not dv.dataset:
                continue
            ds_name = dv.dataset.name
            if ds_name not in meta:
                primary = dv.dataset.primary_metric or r.metric_name
                meta[ds_name] = (primary, bool(r.higher_is_better))
        return [(name, m[0], m[1]) for name, m in sorted(meta.items())]


def _run_deep_profile(
    *,
    paper_id: str,
    dataset_id: int,
    output_path: Path,
) -> dict[str, Any]:
    """Focused line_profiler runs to verify proposed bottlenecks."""
    sections: list[str] = []
    runs: dict[str, Any] = {}

    # 1) load_llm_output: exercise via _global_ranks_for_dataset (same path as export_paper).
    datasets = _paper_dataset_names(paper_id)
    if datasets:

        def _global_ranks_all_paper_datasets() -> None:
            with session_scope() as session:
                for ds_name, metric, hib in datasets:
                    export_to_hugo._global_ranks_for_dataset(session, ds_name, metric, hib)

        secs, text = _profile_capture(
            f"load_llm_output path: _global_ranks_for_dataset x{len(datasets)} ({paper_id})",
            _global_ranks_all_paper_datasets,
            functions=DEEP_PROFILE_SCENARIOS[0][1],
        )
        sections.append(text)
        runs["load_llm_output_via_global_ranks"] = {
            "seconds": secs,
            "paper": paper_id,
            "dataset_calls": len(datasets),
            "datasets": [{"name": n, "metric": m} for n, m, _ in datasets],
        }

    # 2) export_paper end-to-end for the slow fixture.
    secs, text = _profile_capture(
        f"export_paper({paper_id})",
        lambda: export_to_hugo.export_paper(paper_id),
        functions=DEEP_PROFILE_SCENARIOS[1][1],
    )
    sections.append(text)
    runs["export_paper"] = {"seconds": secs, "arxiv_id": paper_id, **_paper_metrics(paper_id)}

    # 3a) _dataset_page_export_metadata for one large dataset.
    def _metadata_one() -> None:
        with session_scope() as session:
            export_to_hugo._dataset_page_export_metadata(session, dataset_id)

    secs_one, text_one = _profile_capture(
        f"_dataset_page_export_metadata(dataset_id={dataset_id})",
        _metadata_one,
        functions=DEEP_PROFILE_SCENARIOS[2][1],
    )
    sections.append(text_one)

    # 3b) same function × all datasets (what export_benchmarks_data does).
    def _metadata_all() -> None:
        with session_scope() as session:
            for ds in session.query(Dataset).all():
                export_to_hugo._dataset_page_export_metadata(session, ds.id)

    secs_all, text_all = _profile_capture(
        "_dataset_page_export_metadata x all datasets (benchmarks.json path)",
        _metadata_all,
        functions=DEEP_PROFILE_SCENARIOS[2][1],
    )
    sections.append(text_all)

    with session_scope() as session:
        ds = session.get(Dataset, dataset_id)
        ds_name = ds.name if ds else ""

    with session_scope() as session:
        n_ds = session.query(Dataset).count()
    runs["dataset_page_export_metadata"] = {
        "single": {"seconds": secs_one, "dataset_id": dataset_id, "name": ds_name},
        "all_datasets": {"seconds": secs_all, "dataset_count": n_ds},
        "ratio_all_over_single": (secs_all / secs_one if secs_one > 0 else None),
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("".join(sections), encoding="utf-8")
    return {
        "output_path": str(output_path),
        "fixtures": {"paper": paper_id, "dataset_id": dataset_id},
        "runs": runs,
    }


def _run_line_profile(
    *,
    paper_id: str | None,
    dataset_id: int | None,
    skip_benchmarks: bool,
    output_path: Path,
) -> dict[str, Any]:
    sections: list[str] = []

    def _capture(label: str, run_fn: Any) -> float:
        elapsed, text = _profile_capture(label, run_fn)
        sections.append(text)
        return elapsed

    runs: dict[str, Any] = {}

    if not skip_benchmarks:
        runs["export_benchmarks_data"] = {
            "seconds": _capture("export_benchmarks_data", export_to_hugo.export_benchmarks_data),
        }

    if paper_id:

        def _run_paper_export() -> None:
            with session_scope() as session:
                export_to_hugo._export_paper_impl(session, paper_id)

        runs["export_paper"] = {
            "arxiv_id": paper_id,
            "seconds": _capture(
                f"export_paper({paper_id})",
                _run_paper_export,
            ),
            **_paper_metrics(paper_id),
        }

    if dataset_id is not None:
        name = ""
        with session_scope() as session:
            ds = session.get(Dataset, dataset_id)
            if ds:
                name = ds.name

        def _run_dataset_export() -> None:
            with session_scope() as session:
                export_to_hugo._export_dataset_impl(session, dataset_id)

        runs["export_dataset"] = {
            "dataset_id": dataset_id,
            "name": name,
            "seconds": _capture(
                f"export_dataset({dataset_id} {name})",
                _run_dataset_export,
            ),
        }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("".join(sections), encoding="utf-8")
    return {
        "output_path": str(output_path),
        "runs": runs,
    }


def _print_summary(report: dict[str, Any]) -> None:
    print(f"\nExport profile — seed {report['seed']} @ {report['generated_at']}")
    print(f"DB: {report['db_counts']['papers']} papers, {report['db_counts']['datasets']} datasets")
    print(
        f"Sample: {report['sample']['paper_count']} papers, {report['sample']['dataset_count']} datasets"
    )
    print(f"Site dir: {report['site_dir']}")

    phases = report.get("wall_clock", {}).get("phases", {})
    phase_order = ("datasets", "benchmarks", "development", "papers")
    for name in phase_order:
        info = phases.get(name)
        if info:
            count = info.get("count")
            suffix = f" ({count} items)" if count else ""
            print(f"  {name}: {info['seconds']:.3f}s{suffix}")
    for name, info in phases.items():
        if name not in phase_order:
            print(f"  {name}: {info['seconds']:.3f}s")

    for key, label in (("papers", "Papers"), ("datasets", "Datasets")):
        summary = report.get("wall_clock", {}).get("summary", {}).get(key, {})
        if not summary.get("count"):
            continue
        print(
            f"\n{label}: total={summary['total']:.2f}s "
            f"median={summary['median']:.3f}s "
            f"p90={summary['p90']:.3f}s "
            f"max={summary['max']:.3f}s "
            f"mean={summary['mean']:.3f}s"
        )
        top_key = "top5_papers" if key == "papers" else "top5_datasets"
        print("  Slowest:")
        for row in report["wall_clock"].get(top_key, [])[:5]:
            if key == "papers":
                print(
                    f"    {row['arxiv_id']}: {row['seconds']:.3f}s "
                    f"({row['result_count']} results, {row['dataset_count']} datasets)"
                )
            else:
                print(
                    f"    {row['dataset_id']} {row.get('name', '')}: {row['seconds']:.3f}s "
                    f"({row.get('row_count', 0)} rows, {row.get('output_bytes', 0)} bytes)"
                )

    lp = report.get("line_profile")
    if lp:
        print(f"\nLine profile written to: {lp['output_path']}")

    deep = report.get("deep_profile")
    if deep:
        print(f"\nDeep line profile: {deep['output_path']}")
        for name, info in deep.get("runs", {}).items():
            if "seconds" in info:
                print(f"  {name}: {info['seconds']:.3f}s")
            elif "single" in info:
                print(
                    f"  {name}: single={info['single']['seconds']:.3f}s "
                    f"all={info['all_datasets']['seconds']:.3f}s "
                    f"(×{info['all_datasets']['dataset_count']} datasets)"
                )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Profile Hugo export performance")
    parser.add_argument("--papers", type=int, default=100, help="Number of papers to sample")
    parser.add_argument("--datasets", type=int, default=40, help="Number of datasets to sample")
    parser.add_argument("--seed", type=int, default=42, help="Random seed for sampling")
    parser.add_argument(
        "--report",
        type=Path,
        default=None,
        help="JSON report path (default: logs/export_profile_<timestamp>.json)",
    )
    parser.add_argument(
        "--site-dir", type=Path, default=None, help="Hugo output dir (default: temp)"
    )
    parser.add_argument("--skip-benchmarks", action="store_true", help="Skip benchmarks.json phase")
    parser.add_argument("--skip-dev", action="store_true", help="Skip development export phase")
    parser.add_argument(
        "--legacy-order",
        action="store_true",
        help="Benchmarks before papers/datasets; clears caches per item (old harness)",
    )
    parser.add_argument(
        "--line-profile",
        action="store_true",
        help="Run line_profiler on slowest (or specified) items after wall-clock sample",
    )
    parser.add_argument(
        "--line-profile-only",
        action="store_true",
        help="Skip wall-clock sample; only run line_profiler (requires --line-profile-paper or dataset)",
    )
    parser.add_argument("--line-profile-paper", metavar="ARXIV_ID", help="Paper for line_profiler")
    parser.add_argument(
        "--line-profile-dataset", type=int, metavar="ID", help="Dataset ID for line_profiler"
    )
    parser.add_argument(
        "--line-profile-output",
        type=Path,
        default=None,
        help="line_profiler text output (default: next to JSON report)",
    )
    parser.add_argument(
        "--deep-profile",
        action="store_true",
        help=(
            "line_profiler on load_llm_output (via global ranks), export_paper, "
            "and _dataset_page_export_metadata (fixtures: 2410.10320, dataset 51)"
        ),
    )
    parser.add_argument(
        "--deep-profile-paper",
        default=DEEP_PROFILE_PAPER,
        help="Paper arxiv_id for deep profile (default: seed-42 slowest)",
    )
    parser.add_argument(
        "--deep-profile-dataset",
        type=int,
        default=DEEP_PROFILE_DATASET_ID,
        help="Dataset id for deep profile (default: D&D)",
    )
    parser.add_argument(
        "--deep-profile-output",
        type=Path,
        default=None,
        help="Deep profile text output (default: logs/export_profile_deep.lines.txt)",
    )
    args = parser.parse_args(argv)

    paper_ids, dataset_ids, db_counts = _sample_ids(args.papers, args.datasets, args.seed)
    with session_scope() as session:
        all_dataset_ids = [ds.id for ds in session.query(Dataset).all()]

    if args.site_dir:
        site_dir = args.site_dir.resolve()
        site_dir.mkdir(parents=True, exist_ok=True)
        cleanup_site = False
    else:
        site_dir = Path(tempfile.mkdtemp(prefix="export_profile_"))
        cleanup_site = True

    _configure_export_site(site_dir)
    _clear_export_caches()

    timestamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    report_path = args.report or (Path("logs") / f"export_profile_{timestamp}.json")
    report_path.parent.mkdir(parents=True, exist_ok=True)
    line_output = args.line_profile_output or report_path.with_suffix(".lines.txt")

    report: dict[str, Any] = {
        "generated_at": datetime.now(UTC).isoformat(),
        "seed": args.seed,
        "db_counts": db_counts,
        "sample": {
            "paper_ids": paper_ids,
            "dataset_ids": dataset_ids,
            "paper_count": len(paper_ids),
            "dataset_count": len(dataset_ids),
            "all_dataset_count": len(all_dataset_ids),
        },
        "site_dir": str(site_dir),
        "options": {
            "skip_benchmarks": args.skip_benchmarks,
            "skip_dev": args.skip_dev,
            "production_order": not args.legacy_order,
            "line_profile": args.line_profile or args.line_profile_only,
        },
    }

    slow_paper = args.line_profile_paper
    slow_dataset = args.line_profile_dataset

    if not args.line_profile_only:
        report["wall_clock"] = _run_wall_clock_sample(
            paper_ids,
            dataset_ids,
            all_dataset_ids=all_dataset_ids,
            skip_benchmarks=args.skip_benchmarks,
            skip_dev=args.skip_dev,
            production_order=not args.legacy_order,
        )
        if report["wall_clock"]["slowest"]["paper"]:
            slow_paper = slow_paper or report["wall_clock"]["slowest"]["paper"]["arxiv_id"]
        if report["wall_clock"]["slowest"]["dataset"]:
            slow_dataset = slow_dataset or report["wall_clock"]["slowest"]["dataset"]["dataset_id"]

    if args.line_profile or args.line_profile_only:
        if not slow_paper and not slow_dataset and args.skip_benchmarks:
            print(
                "error: --line-profile needs a target (sample, --line-profile-paper, or benchmarks)"
            )
            return 1
        report["line_profile"] = _run_line_profile(
            paper_id=slow_paper,
            dataset_id=slow_dataset,
            skip_benchmarks=args.skip_benchmarks,
            output_path=line_output,
        )

    if args.deep_profile:
        deep_output = args.deep_profile_output or Path("logs/export_profile_deep.lines.txt")
        report["deep_profile"] = _run_deep_profile(
            paper_id=args.deep_profile_paper,
            dataset_id=args.deep_profile_dataset,
            output_path=deep_output,
        )
        report["options"]["deep_profile"] = True

    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    _print_summary(report)
    print(f"\nJSON report: {report_path}")

    if cleanup_site:
        print(f"(temp site dir retained for inspection: {site_dir})")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
