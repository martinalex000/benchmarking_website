# Pre-screening validation experiment

This read-only experiment checks the first pipeline decision: whether a title and abstract justify
sending a paper to full benchmark-result extraction.

It combines four kinds of evidence:

1. the actual accepted/rejected decisions in `papers/screening/results.yaml`;
2. titles and abstracts from `papers/screening/queue.sqlite3`;
3. exact canonical dataset-name matches from `config/seed_data.yaml`;
4. downstream raw extraction artifacts and stored database results, when available.

Run it from the repository root:

```bash
UV_CACHE_DIR=/tmp/benchmarking-uv-cache uv run python \
  experiments/prescreen_validation/prescreen_audit.py
```

Generated files are written to `experiments/prescreen_validation/output/` and ignored by Git:

- `summary.md` and `summary.json` contain aggregate counts with explicit denominators;
- `manual_review.md` contains the abstracts and evidence for a deterministic 10-paper sample;
- `review_cohort.csv` has blank manual-label columns;
- `rejected_rerun_candidates.txt` lists rejected sample papers that could optionally be forced
  through the rest of the pipeline.

The default manual cohort contains three high-priority suspicious rejections, two ordinary rejected controls,
three accepted papers with zero raw extracted rows, and two accepted positive controls. Increase it
with `--sample-size`; the proportions remain approximately 30/20/30/20.

Suspicious rejections are prioritized by evidence strength. A rejected paper that already has
positive downstream extraction rows ranks ahead of a local full-text dataset match, which ranks
ahead of an abstract-only catalog-name match. This deliberately prevents common-word dataset names
from dominating the small manual cohort.

## Interpretation

A dataset-name match is only a review lead. It may be incidental, refer to a different task or
protocol, or occur in a paper that reports no result. Likewise, a database paper with zero stored
rows is not automatically a screening false positive: parsing, protocol filtering, unresolved
datasets, or quarantine can remove otherwise extracted rows. Zero rows in the raw
`llm_output.yaml` artifact are therefore reported separately.

For manual labels, answer the question the screener actually receives: does the abstract indicate
benchmark results or a new benchmark strongly enough to justify full extraction? Inspect the full
paper only after recording that abstract-only judgment. Rejected papers can then optionally be run
downstream with the command printed in `manual_review.md`; the experiment does not do this
automatically because it uses model calls and changes local paper/database state.
