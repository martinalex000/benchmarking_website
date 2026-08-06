# Suspicious Benchmarking Results Report

**Date:** 2026-08-05  
**Database:** `data/benchmarks.db`  
**Command:** `UV_CACHE_DIR=/tmp/benchmarking-uv-cache uv run python scripts/detect_suspicious_task_papers.py --output experiments/suspicious_task_papers.json --csv experiments/suspicious_task_papers.csv --limit 0`

The interpretation and rankings below describe the initial run, before the scope cleanup. The machine-readable artifacts were refreshed afterward against the cleaned database.

## Executive interpretation

The detector found **563 suspicious paper/dataset/metric observations across 300 papers** out of **6,323 scored observations**. This is a useful triage run, but the output should not be read as 300 papers making implausible frontier claims.

The dominant signal is inconsistent comparability: the detector groups results by dataset and metric name, but not by target unit, benchmark setting, or whether a row is the proposed method or a baseline. The largest scores are therefore mostly valid source values expressed on different scales, or unusually poor baselines, rather than over-optimistic proposed results.

The most important actionable finding is a **unit-normalization problem in molecular benchmarks**, especially QM9 and PCQM4Mv2. The detector is successfully exposing this data-quality issue, but its current ranking is not yet a reliable “too-good-to-be-true” leaderboard detector.

## Initial run summary

| Quantity | Result |
|---|---:|
| Paper/dataset/metric observations scored | 6,323 |
| Suspicious observations | 563 |
| Suspicious papers | 300 |
| Observations with a clustering signal | 2,574 |
| Flagged groups containing at least one proposed-method row | 421 |
| Flagged groups containing baselines only | 142 |
| Problematic rows included | No |
| Robust outlier threshold | 4.5 |

Every flagged observation had the `robust_statistical_outlier` reason. HDBSCAN added `hdbscan_noise` to 394 of them and `hdbscan_minority_cluster` to 85. The clustering signal is intentionally not sufficient for inclusion under the default settings.

The distribution is highly skewed: the median paper score is 1.77, the 90th percentile is 7.18, and the 99th percentile is 342.92. QM9 accounts for 132 of the 563 flagged observations; Accuracy accounts for 305.

## Scope exclusions applied

The current benchmark scope intentionally excludes OOD/domain-shift and adversarial/attack evaluations. Based on the detector output and local LaTeX source review, 18 paper-level exclusions were added to `config/protocol_exclusions.yaml` under `exclude_all_results`. They cover black-box attacks, injection/backdoor/poisoning, adversarial robustness, OOD detection/generalization, domain adaptation, and distribution-shift evaluation.

This configuration change governs future parsing and curation. The 762 legacy result rows for these 18 papers have now been removed from `data/benchmarks.db`; a temporary pre-delete backup was written to `/tmp/benchmarking-before-ood-attack-delete.db`.

The refreshed detector run now scores 6,260 observations and flags 286 papers; none of the 18 excluded papers remain in its output.

### Follow-up cleanup

The remaining review identified **21 additional non-canonical papers** using
labels-as-features, few-shot learning, prompting, graph-language/LLM methods,
cross-domain transfer, domain adaptation, or self-supervised/pretrained
evaluation. They were added to `exclude_all_results` and their **1,222 legacy
result rows were removed**. A rollback copy is available at
`/tmp/benchmarking-before-noncanonical-and-unit-fixes.db`.

The molecular records were corrected as follows:

- `2206.00133`: moved three QM9 HOMO rows out of PCQM4Mv2, renamed the metric
  from bare `MAE` to `HOMO`, and converted meV to eV.
- `2308.00887`: converted 32 explicitly meV-reported QM9 energy rows to eV.
- `2402.04538`: converted 11 explicitly meV-reported PCQM4Mv2 rows to eV,
  matching the rest of the stored PCQM4Mv2 cohort.

The current detector artifacts score **6,160 observations**, flag **272
papers**, and contain **2,358 observations with a clustering signal**. The
remaining top entries are predominantly source-reported baseline scale
differences; `2510.04522` is also expected to remain visible to this detector
because its QM9 conditional-generation rows are a dataset-specific exclusion,
which the detector does not currently apply.

A final sweep found **1,260 legacy rows** belonging to older
`exclude_all_results` entries that had not previously been removed. Those rows
were deleted too; the final backup is
`/tmp/benchmarking-before-all-exclude-all-delete.db`. The final detector run
scores **6,051 observations**, flags **267 papers**, and has **2,314
clustering candidates** at that stage. A subsequent cleanup removed **470
additional rows** matched by configured dataset- and row-level exclusions,
including the QM9 conditional-generation rows from `2510.04522`. Its backup is
`/tmp/benchmarking-before-dataset-exclusion-delete.db`.

The final detector run scores **5,989 observations**, flags **263 papers**, and
has **2,195 clustering candidates**. No paper listed under `exclude_all_results`
remains in the detector output, and no configured dataset/row exclusion still
matches a stored result at that stage. A final configured split cleanup removed
the last **82 rows** for `2210.05920`; its backup is
`/tmp/benchmarking-before-final-protocol-exclusion-delete.db`.

The current detector artifacts therefore score **5,985 observations**, flag
**262 papers**, and contain **2,192 clustering candidates**. The configured
exclusion rules now match zero stored result rows.

## Highest-priority findings

| Rank | Paper and observation | Score | Interpretation |
|---:|---|---:|---|
| 1 | 2308.00887, QM9 / G | 8,200.48 | The source table reports values in meV, including FGNN values around 2,468. These are legitimate source values, but they are mixed with papers reporting other QM9 targets on other scales. Normalize units before comparing. |
| 2 | 2308.00887, QM9 / U0 | 7,076.99 | Same unit/cohort issue as above; not evidence that the proposed method pushed the frontier by 8,000 standard-score units. |
| 3 | 2308.00887, QM9 / H | 6,674.13 | Same unit/cohort issue as above. |
| 4 | 2402.04538, PCQM4Mv2 / MAE | 1,622.75 | The local source labels the values as meV (about 68–115 meV), while most cohort values are around 0.1. This is a direct unit-normalization mismatch. |
| 5 | 2206.00133, PCQM4Mv2 / MAE | 345.31 | The database assigns 15.6–22.0 to PCQM4Mv2, but the local source places those values in a QM9 table. This is likely a dataset-assignment error, compounded by a unit mismatch. |
| 6 | 2305.13987, QM9 / U0, H, G | 106.26, 103.81, 52.40 | The source explicitly reports very poor Graphormer-id baselines (for example, 3457.2 for U0 and 1468.9 for G), while the proposed SPIS values are around 2.1. This is a baseline-scale outlier, not an implausible proposed win. |
| 7 | 2510.04522, QM9 / LUMO, HOMO, gap | 93.11, 59.91, 24.83 | The source includes Random/Natom generation baselines in the hundreds or thousands and reports the proposed values on the same scale. The wide distribution is expected for this conditional-generation setup. |
| 8 | 2511.22435, MNIST / Accuracy | 33.36 | The local source calls this benchmark CMNIST-sp, an OOD binary task, while the database cohort is named MNIST and is mostly standard accuracy near 0.95. This looks like a dataset/setting conflation worth correcting. |

## What the output says about frontier claims

The detector aggregates **all extracted means** for one paper, dataset, and metric. It does not isolate the proposed model. Consequently:

- A paper is flagged when an unusual baseline is present, even if the proposed result is ordinary. This accounts for the baseline-only examples above.
- It treats a valid unit change as an outlier. QM9 target names such as `G`, `H`, and `U0` are not comparable without their source units.
- It can combine standard, OOD, ablation, attacked, and random-baseline settings under one dataset name. The CMNIST-sp/MNIST example demonstrates this failure mode.
- It is direction-agnostic. A very high value can be suspicious for a lower-is-better metric but normal or desirable for a higher-is-better metric; the current statistical score does not use `higher_is_better`.
- A paper with a broad, heterogeneous table can be flagged even when every value is faithful to the source. The score is therefore best interpreted as “review this paper’s comparability and extraction,” not “the paper is overstating SOTA.”

There are still potentially useful claim-level leads in the lower part of the queue. For example, the detector flags unusually high proposed values on Coauthor-Physics, Coauthor-CS, Amazon-Photo, Reddit, and ogbg-molhiv. Those should be reviewed after separating ablations and protocols; they are not validated anomalies from this run alone.

## Recommended follow-up

1. **Add unit-aware grouping and normalization.** Store the target unit (or a canonical conversion) with each result and include it in the anomaly cohort key. Do not compare PCQM4Mv2 values in meV with values in eV.
2. **Add benchmark-setting identity.** Include split, task variant, OOD/attack status, and ablation/random-baseline status in the comparison key. Dataset name alone is insufficient.
3. **Rank proposed rows separately.** Use `is_baseline` and the paper’s proposed method to produce a “frontier-push” queue, while retaining a separate “table/extraction heterogeneity” queue.
4. **Use metric direction.** Incorporate `higher_is_better` when scoring directional frontier claims, while retaining two-sided outlier checks for extraction errors.
5. **Review and normalize the molecular entries first.** The PCQM4Mv2 and QM9 examples dominate the score tail and will otherwise drown out more relevant anomalies.

## Artifacts

The full machine-readable outputs are available in the ignored experiment directory:

- `experiments/suspicious_task_papers.json`
- `experiments/suspicious_task_papers.csv`
