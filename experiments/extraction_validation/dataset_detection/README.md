# Dataset-detection validation

This experiment prepares a blind 20-paper manual review for the dataset-discovery stage:

- 10 processed papers with at least one stored database result;
- 10 processed papers with zero stored database results.

Every selected paper must have `extraction_status = extracted`, a local `paper.pdf`, and a local
`extracted/llm_output.yaml`. Papers already used in the pre-screening review are excluded. Selection
is deterministic for a fixed seed.

Run from the repository root:

```bash
UV_CACHE_DIR=/tmp/benchmarking-uv-cache uv run python \
  experiments/extraction_validation/dataset_detection/prepare_review.py
```

The command creates these ignored, local review artifacts beside this file:

- `review_cohort.csv` — one blank annotation row per paper;
- `manual_review.md` — the ordered paper checklist and annotation protocol;
- `pdfs/with_database_results/` — 10 PDFs;
- `pdfs/zero_database_results/` — 10 PDFs.

For papers with multiple experimental datasets, duplicate the CSV row once per dataset. Enter
`NONE` when the paper has no quantitative dataset result. Use `yes`, `no`, or `unclear` for
compatibility and record the protocol reason rather than inferring compatibility from dataset name
alone.

Rerunning the command preserves every existing CSV row and Markdown note. It only appends papers
when a cohort is below its target and only copies missing PDFs.

After completing the manual annotations, compare them with the current database:

```bash
UV_CACHE_DIR=/tmp/benchmarking-uv-cache uv run python \
  experiments/extraction_validation/dataset_detection/evaluate_review.py
```

This writes the ignored local outputs `evaluation_report.md` and `evaluation_results.json`. The
evaluation keeps partial, uncertain, and protocol-qualified annotations separate from strict
precision and recall rather than coercing them into binary labels. The manual annotations are the
reference standard; precision, recall, false positives, and false negatives describe the
LLM-derived database output. The Markdown report contains one editable adjudication checkbox per
candidate discrepancy.
