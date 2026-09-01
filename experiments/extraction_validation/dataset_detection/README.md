# Dataset-detection validation

This experiment prepares a blind 20-paper core manual review for the dataset-discovery stage:

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

After completing the core annotations (and any supplemental v3 annotations appended to the same
CSV), compare them with the current database:

```bash
UV_CACHE_DIR=/tmp/benchmarking-uv-cache uv run python \
  experiments/extraction_validation/dataset_detection/evaluate_review.py
```

This writes the ignored local outputs `evaluation_report.md` and `evaluation_results.json`. The
evaluation keeps partial, uncertain, and protocol-qualified annotations separate from strict
precision and recall rather than coercing them into binary labels. The manual annotations are the
reference standard; precision, recall, false positives, and false negatives describe the
LLM-derived database output. Only datasets present in the database catalog contribute to scores;
untracked manual datasets remain visible in the report as excluded evidence. The Markdown report
contains one editable adjudication checkbox per candidate discrepancy and compares every
manual-only dataset with the corresponding raw `papers/*/extracted/llm_output.yaml` result rows
and `discovered_datasets` manifest. This distinguishes a dataset detected by the LLM but not
promoted from one absent from the raw LLM output.

Dataset precision is `TP / (TP + FP)`, and recall is `TP / (TP + FN)`, where each item is a tracked
paper–dataset pair. These are end-to-end database metrics: a raw YAML detection that is later
rejected by catalog, protocol, or table handling counts as missing from the database output. The
report also gives detection-only metrics on the raw YAML artifact: a tracked name in either a
result row or `discovered_datasets` is a positive detection, with table assignment, protocol
compatibility, and database promotion ignored. A manifest-only diagnostic is reported separately;
it can be lower when the result rows contain a more specific spelling or alias. The report also
splits database-missing pairs into those with raw result rows, manifest-only detections, and no raw
detection. The CSV result count is only a snapshot; if the database changes, the evaluator uses the
current count and records the drift.
