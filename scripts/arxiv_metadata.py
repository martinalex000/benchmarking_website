#!/usr/bin/env python3
"""Download and analyze the Cornell arXiv metadata snapshot."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from backend.arxiv_metadata_analysis import (
    DEFAULT_CONFIG_PATH,
    DEFAULT_DB_PATH,
    DEFAULT_SNAPSHOT_PATH,
    ScreeningConfig,
    analyze_snapshot,
    download_manifest,
    merge_reports,
    write_reports,
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATASET_HANDLE = "Cornell-University/arxiv"
SNAPSHOT_NAME = "arxiv-metadata-oai-snapshot.json"


def _rooted(path: str | None, default: Path) -> Path:
    candidate = Path(path) if path else default
    return candidate if candidate.is_absolute() else PROJECT_ROOT / candidate


def _download(args: argparse.Namespace) -> Path:
    target = _rooted(args.snapshot, DEFAULT_SNAPSHOT_PATH)
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() and target.stat().st_size > 0 and not args.force_download:
        print(f"Using existing snapshot: {target}")
        return target

    print(f"Downloading {DATASET_HANDLE}/{SNAPSHOT_NAME} …")
    url = "https://www.kaggle.com/api/v1/datasets/download/Cornell-University/arxiv"
    params = {"filename": SNAPSHOT_NAME}
    if args.version:
        params["datasetVersionNumber"] = args.version
    headers = {}
    token = os.environ.get("KAGGLE_API_TOKEN", "").strip()
    if token:
        headers["Authorization"] = f"Bearer {token}"
    resolved_version = None
    with tempfile.TemporaryDirectory(prefix="arxiv-kaggle-", dir=str(target.parent)) as temp_dir:
        payload_path = Path(temp_dir) / "arxiv.payload"
        with requests.get(
            url, params=params, headers=headers, stream=True, timeout=(30, 600)
        ) as response:
            response.raise_for_status()
            version_match = re.search(r"/datasets/\d+/(\d+)/", response.url)
            resolved_version = version_match.group(1) if version_match else args.version
            with payload_path.open("wb") as payload:
                for chunk in response.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        payload.write(chunk)
        staged_path = Path(temp_dir) / SNAPSHOT_NAME
        with payload_path.open("rb") as payload:
            signature = payload.read(4)
        if signature.startswith(b"PK"):
            with zipfile.ZipFile(payload_path) as archive:
                members = [
                    member for member in archive.namelist() if member.endswith(SNAPSHOT_NAME)
                ]
                if len(members) != 1:
                    raise RuntimeError(
                        f"Expected one {SNAPSHOT_NAME} in Kaggle archive, found {members}"
                    )
                with archive.open(members[0]) as source, staged_path.open("wb") as destination:
                    shutil.copyfileobj(source, destination, length=1024 * 1024)
        elif signature.startswith(b"{"):
            os.replace(payload_path, staged_path)
        else:
            raise RuntimeError(f"Kaggle response is neither JSON nor ZIP (signature={signature!r})")
        os.replace(staged_path, target)

    manifest = download_manifest(
        target,
        source=DATASET_HANDLE,
        version=args.version,
        resolved_version=resolved_version,
    )
    manifest_path = target.parent / "download-manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Saved snapshot: {target} ({target.stat().st_size:,} bytes)")
    return target


def _analyze(args: argparse.Namespace, snapshot: Path | None = None) -> int:
    snapshot = snapshot or _rooted(args.snapshot, DEFAULT_SNAPSHOT_PATH)
    db_path = _rooted(args.db, DEFAULT_DB_PATH)
    output_dir = _rooted(args.output_dir, snapshot.parent / "reports")
    config_path = _rooted(args.config, DEFAULT_CONFIG_PATH)
    if not snapshot.exists():
        raise FileNotFoundError(f"Snapshot not found: {snapshot}; run the download command first")
    config = ScreeningConfig.load(config_path)
    print(f"Analyzing {snapshot} …")
    report = analyze_snapshot(snapshot, db_path, config)
    report["source"] = {
        "snapshot": str(snapshot),
        "database": str(db_path),
        "config": str(config_path),
    }
    write_reports(report, output_dir, config)
    recall = report["known_results_recall"]
    print(
        f"Records: {report['corpus']['records']:,}; "
        f"known result papers: {recall['database_papers']:,}; "
        f"combined pre-filter: {recall['combined_prefilter']:,} "
        f"({recall['combined_recall_all']:.2%})"
    )
    print(f"Reports written to {output_dir}")
    return 0


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--snapshot", help=f"Snapshot path (default: {DEFAULT_SNAPSHOT_PATH})")
    common.add_argument("--db", help=f"SQLite database path (default: {DEFAULT_DB_PATH})")
    common.add_argument(
        "--output-dir", help="Report directory (default: papers/arxiv-metadata/reports)"
    )
    common.add_argument("--config", help=f"Keyword config (default: {DEFAULT_CONFIG_PATH})")

    download = subparsers.add_parser(
        "download", parents=[common], help="Download the Kaggle snapshot"
    )
    download.add_argument("--version", help="Pin a Kaggle dataset version")
    download.add_argument("--force-download", action="store_true")

    subparsers.add_parser("analyze", parents=[common], help="Analyze an existing snapshot")

    merge = subparsers.add_parser("merge", parents=[common], help="Merge line-chunk reports")
    merge.add_argument(
        "--input-dir",
        required=True,
        help="Directory containing part-*/report.json chunk reports",
    )

    run_all = subparsers.add_parser(
        "all", parents=[common], help="Download if needed, then analyze"
    )
    run_all.add_argument("--version", help="Pin a Kaggle dataset version")
    run_all.add_argument("--force-download", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    try:
        if args.command == "download":
            _download(args)
            return 0
        if args.command == "analyze":
            return _analyze(args)
        if args.command == "merge":
            config_path = _rooted(args.config, DEFAULT_CONFIG_PATH)
            input_dir = _rooted(args.input_dir, Path("."))
            output_dir = _rooted(args.output_dir, DEFAULT_SNAPSHOT_PATH.parent / "reports")
            config = ScreeningConfig.load(config_path)
            paths = sorted(input_dir.glob("part-*/report.json"))
            report = merge_reports(paths, output_dir, config)
            report["source"].update(
                {
                    "snapshot": str(_rooted(args.snapshot, DEFAULT_SNAPSHOT_PATH)),
                    "database": str(_rooted(args.db, DEFAULT_DB_PATH)),
                    "config": str(config_path),
                }
            )
            write_reports(report, output_dir, config)
            recall = report["known_results_recall"]
            print(
                f"Records: {report['corpus']['records']:,}; "
                f"known result papers: {recall['database_papers']:,}; "
                f"combined pre-filter: {recall['combined_prefilter']:,} "
                f"({recall['combined_recall_all']:.2%})"
            )
            print(f"Reports written to {output_dir}")
            return 0
        snapshot = _download(args)
        return _analyze(args, snapshot=snapshot)
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
