#!/usr/bin/env python3
"""run_manual.py — interactive helper for processing a single paper.

Usage::
    python scripts/run_manual.py 2206.08164
    python scripts/run_manual.py 2206.08164 --model fallback
    python scripts/run_manual.py 2206.08164 --skip-download
"""
from __future__ import annotations
import argparse
import sys
from pathlib import Path

# Ensure project root is on the path
sys.path.insert(0, str(Path(__file__).parent.parent))

from backend.pipeline import stage_extract, stage_parse, stage_export


def main():
    parser = argparse.ArgumentParser(description="Process a single paper manually")
    parser.add_argument("arxiv_id")
    parser.add_argument("--model", "-m", default="primary")
    parser.add_argument("--skip-download", action="store_true")
    parser.add_argument("--skip-extract", action="store_true")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    arxiv_id = args.arxiv_id.strip().lstrip("arXiv:").split("v")[0]

    if not args.skip_download:
        from backend.arxiv_downloader import download_paper
        print(f"Downloading arXiv:{arxiv_id}…")
        if not download_paper(arxiv_id, force=args.force):
            sys.exit(f"Download failed for {arxiv_id}")

    if not args.skip_extract:
        from backend.llm_extractor import run_extraction
        print(f"Extracting with model_tier={args.model}…")
        if not run_extraction(arxiv_id, model_tier=args.model):
            sys.exit(f"Extraction failed for {arxiv_id}")

    from backend.results_parser import parse_and_store
    print("Parsing and storing results…")
    n = parse_and_store(arxiv_id)
    print(f"Stored {n} new result rows.")

    from backend.export_to_hugo import export_all
    print("Exporting to Hugo…")
    export_all(arxiv_ids=[arxiv_id])

    print("Done. Run `bin/hugo server` in site/ to preview.")


if __name__ == "__main__":
    main()
