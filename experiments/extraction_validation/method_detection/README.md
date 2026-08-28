# Method-detection validation

This experiment reuses the exact 20 papers and cohort order from the dataset-detection review.
It verifies every distinct method attached to stored result rows and provides one paper-level row
for recording methods that the extraction missed.

Run from the repository root:

```bash
UV_CACHE_DIR=/tmp/benchmarking-uv-cache uv run python \
  experiments/extraction_validation/method_detection/prepare_review.py
```

The command creates these ignored local review artifacts:

- `review_cohort.csv` — a paper-summary row plus one row per database-detected method;
- `manual_review.md` — linked PDFs, database evidence, and a paper-by-paper checklist;
- `pdfs/with_database_results/` and `pdfs/zero_database_results/` — the same papers as before.

For each `database_method` row, use `manual_decision`:

- `correct` — a distinct method with quantitative results in scope;
- `alias` — the method exists but should be grouped under another name; record that name;
- `not_a_method` — the extracted name is not a method;
- `not_in_results` — the method is mentioned but does not have an in-scope quantitative result;
- `unclear` — requires later adjudication.

On each `paper_summary` row, list omitted methods and their dataset/table evidence, enter `NONE`
when nothing is missing, and set `review_complete` to `yes`. Existing CSV annotations and Markdown
notes are never overwritten by rerunning the preparation script.
