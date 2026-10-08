# Dataset usage: extraction ablation

This sibling variant leaves `experiments/datasets_over_time` unchanged. It reads
the original experiment's configuration without executing it and reuses its
aggregation, publication filters, and current leaderboard eligibility predicate.

Run from the repository root:

```sh
MPLCONFIGDIR=/tmp/dataset-usage-matplotlib UV_CACHE_DIR=/tmp/benchmarking-uv-cache \
  uv run python experiments/datasets_over_time_ablation/datasets_over_time_ablation.py
```

Optional paths: `--db`, `--papers-dir`, and `--output-dir`.

## Counting rules

- **Current:** unique paper–dataset/benchmark uses from stored results satisfying
  `result_is_leaderboard_eligible`, as in the original experiment.
- **Ablation:** use the current `papers/<arxiv_id>/extracted/llm_output.yaml`
  (legacy JSON if YAML is absent). Any extracted result row naming a resolvable
  dataset establishes usage, regardless of protocol, split, task, value, result
  origin, or paper quarantine status. Discovery-only mentions do not establish usage.
- **Fallback:** if the extraction file or result payload is unavailable, invalid,
  unreadable, or belongs to another paper, count all stored dataset uses for that
  paper without an eligibility filter. Successful empty extractions remain empty.
  Unresolved names do not trigger fallback; they are exported for inspection.
- Repeated rows, models, metrics, and variants contribute at most one use per
  logical dataset per paper. Benchmark counts further deduplicate across datasets.
- Dataset identities use configured global and paper-specific aliases and the
  production name resolver, without compatibility gates. Ambiguous generic
  variant names are excluded from name matching. Fuzzy matches inherit the
  production resolver's limitations; these are extraction-based statistics,
  not a manual verification of experiments actually executed by the authors.
- Dates and publication evidence come from database paper metadata. Benchmark
  plots cover 2019–2025; dataset plots retain the original's lack of a lower
  date cutoff. Papers dated after 2025 or without a usable date are excluded.
  Papers with extractions but no stored results are included. Files outside the
  database paper cohort and archived historical extraction files are not used.
- Relative curves divide by the union of papers using any selected group,
  separately in each arm and year. Shares may therefore decrease even when
  counts increase. CSVs also include the original sum-of-group-count shares.

## Outputs

- `plots/{all_papers,conference_only,peer_reviewed}/`: side-by-side PNG/PDF
  stacked counts, count curves, and union-relative curves for benchmarks and
  the five LRGB datasets. Each comparison shares axes and colors.
  `*_relative_overlay` overlays the original solid curves with dashed ablation
  curves, using the original experiment's group colors and introduction years.
- `summary.json`: cohort, extraction coverage, fallback counts, and net/gross
  changes for every publication scope.
- `report.md`: readable findings and links to plots.
- `data/*_comparison.csv`: yearly counts, changes, and both share definitions.
- `data/extraction_coverage.csv`, `missing_extractions.csv`: per-paper coverage,
  paths, pipeline status, raw result counts, and fallback details.
- `data/current_usage.csv`, `ablation_usage.csv`, `membership_comparison.csv`:
  audit of logical dataset memberships, additions, removals, and evidence source.
- `data/unresolved_dataset_names.csv`: distinct paper/name pairs outside the
  resolver, including datasets that are not tracked by the database.

The database is read through a temporary consistent SQLite backup that includes
committed WAL contents. The experiment never checkpoints or writes the source
database. Output artifacts stay local under the repository's ignore rules.

Because saved extractions can differ from the extractions that produced existing
database rows, the ablation can lose usages as well as gain them. It also removes
quarantine and other insertion gates, so the difference is broader than the
isolated causal effect of protocol compatibility filtering.

Validation:

```sh
UV_CACHE_DIR=/tmp/benchmarking-uv-cache uv run pytest \
  experiments/datasets_over_time_ablation/test_ablation.py -q
```
