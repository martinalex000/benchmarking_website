# Pairwise significance in plot experiments

`backend.significance.is_significantly_different(mean1, std1, num_runs1, mean2, std2,
num_runs2)` accepts six nullable summary statistics and returns a boolean.

- Both stds: independent, two-sided Welch's t-test, significant when `p < 0.05`.
- One std: the other value must lie outside the two-sided 95% Student-t confidence
  interval for the mean. It is treated as a fixed reference, including when it has
  an extracted repetition count. This deliberately ignores its unreported uncertainty.
- Neither std: any unequal means are considered significantly different, regardless
  of counts. Equal means always return false.
- Missing counts for std-bearing results default to four. Explicit counts, including
  counts of two or three, are preserved; counts below two or non-integer counts raise
  `ValueError` because they cannot support the test.
- Missing/non-finite means return false. Negative or non-finite stds are treated as
  unavailable. Zero std is valid; unequal means with zero variance on both sides
  are different.

Comparisons are pairwise without multiple-comparison correction. Runs are assumed
independent and approximately normal; summary statistics cannot support a paired test.

The helper controls shared SOTA ownership (against the best mean), stale baseline
classification, and MLP better/tied/worse classification. Source repetition counts
are retained in analysis records. The optional single-mean SOTA winner figures keep
their directional rule. Website rendering/deduplication rules are outside this change.

References: [Welch's test](https://www.itl.nist.gov/div898/handbook/eda/section3/eda353.htm)
and [mean confidence intervals](https://www.itl.nist.gov/div898/handbook/eda/section3/eda352.htm).

## Regenerate

Run these from the repository root (all database loaders are read-only):

```sh
UV_CACHE_DIR=/tmp/benchmarking-uv-cache uv run python experiments/analysis/analyze_sota_architecture.py
UV_CACHE_DIR=/tmp/benchmarking-uv-cache uv run python experiments/analysis/analyze_stale_baselines.py
UV_CACHE_DIR=/tmp/benchmarking-uv-cache uv run python experiments/mlp_baseline_comparison/compare_mlp_baseline.py
```

Each script accepts `--db PATH` for a consistent SQLite snapshot and `--output-dir PATH`.
Outputs stay in their existing experiment directories and remain untracked. Each run
includes the existing publication-filtered variants: nine SOTA figures, 33 stale-baseline
figures, and six MLP figures, each as PNG and PDF. Historical `_old` files are not regenerated.

The 2026-10-15 regeneration found three negative stored stds (result IDs 246346,
246356, 246858, paper 2212.10822); the local LaTeX source also prints negative
parenthetical values. These stds are treated as unavailable without editing source
data. The regeneration manifest records the database hash and output checksums.
