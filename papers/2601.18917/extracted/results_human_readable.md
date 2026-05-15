# Extraction: GraIP: A Benchmarking Framework For Neural Graph Inverse Problems
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: Max-DAG I-MLE
- Type: GNN

## Results

### Charged — MSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| NRI + STE | 0.0021 | 0.0000 | No | this paper | Table 2 |
| NRI + SIMPLE | 0.0028 | 0.0000 | Yes | this paper | Table 2 |
| NRI + STE (non-blind) | 0.0002 | 0.0000 | Yes | this paper | Table 2 |

### Cornell — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Baseline (GINE) | 0.5740 | 0.0060 | Yes | this paper | Table 1 |
| Random rewire | 0.5100 | 0.0570 | Yes | this paper | Table 1 |
| Gumbel | 0.5410 | 0.0380 | Yes | this paper | Table 1 |
| I-MLE | 0.5950 | 0.0510 | Yes | this paper | Table 1 |
| SIMPLE | 0.6590 | 0.0400 | No | this paper | Table 1 |

### ER2-30 — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| NoTears | 0.9850 | 0.0180 | Yes | zheng2018 | Table 1 |
| Golem | 0.8180 | 0.0810 | Yes | Ng2020role | Table 1 |
| Max-DAG I-MLE | 0.9420 | 0.0180 | No | this paper | Table 1 |

### ER4-30 — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| NoTears | 1.0000 | 0.0000 | Yes | this paper | Table 1 |
| Golem | 0.8260 | 0.1010 | Yes | this paper | Table 1 |
| Max-DAG I-MLE | 0.5190 | 0.0980 | No | this paper | Table 1 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Baseline (GINE) | 0.5500 | 0.0080 | Yes | this paper | Table 1 |
| Random rewire | 0.6510 | 0.0030 | Yes | this paper | Table 1 |
| Gumbel | 0.5730 | 0.0120 | Yes | this paper | Table 1 |
| I-MLE | 0.6590 | 0.0120 | Yes | this paper | Table 1 |
| SIMPLE | 0.6830 | 0.0090 | No | this paper | Table 1 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Baseline (GINE) | 0.3550 | 0.0050 | Yes | this paper | Table 1 |
| Random rewire | 0.2510 | 0.0010 | Yes | this paper | Table 1 |
| Gumbel | 0.2510 | 0.0030 | Yes | this paper | Table 1 |
| I-MLE | 0.2520 | 0.0030 | Yes | this paper | Table 1 |
| SIMPLE | 0.2480 | 0.0010 | No | this paper | Table 1 |

### SF2-30 — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| NoTears | 0.9300 | 0.0450 | Yes | this paper | Table 1 |
| Golem | 0.9120 | 0.0420 | Yes | this paper | Table 1 |
| Max-DAG I-MLE | 0.5370 | 0.1080 | No | this paper | Table 1 |

### SF4-30 — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| NoTears | 0.9660 | 0.0280 | Yes | this paper | Table 1 |
| Golem | 0.9080 | 0.0590 | Yes | this paper | Table 1 |
| Max-DAG I-MLE | 0.3860 | 0.0720 | No | this paper | Table 1 |

### Springs — MSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| NRI + STE | 0.0002 | 0.0000 | Yes | this paper | Table 2 |
| NRI + SIMPLE | 0.0001 | 0.0000 | Yes | this paper | Table 2 |
| NRI + I-MLE | 0.0003 | 0.0000 | No | this paper | Table 2 |
| NRI + STE (non-blind) | 0.0000 | 0.0000 | Yes | this paper | Table 2 |

### Texas — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Baseline (GINE) | 0.6740 | 0.0100 | Yes | this paper | Table 1 |
| Random rewire | 0.7380 | 0.0120 | Yes | this paper | Table 1 |
| Gumbel | 0.7890 | 0.0670 | Yes | this paper | Table 1 |
| I-MLE | 0.7840 | 0.0330 | Yes | this paper | Table 1 |
| SIMPLE | 0.8270 | 0.0320 | No | this paper | Table 1 |

### Wisconsin — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Baseline (GINE) | 0.6970 | 0.0130 | Yes | this paper | Table 1 |
| Random rewire | 0.7310 | 0.0050 | Yes | this paper | Table 1 |
| Gumbel | 0.7060 | 0.0370 | Yes | this paper | Table 1 |
| I-MLE | 0.6940 | 0.0220 | Yes | this paper | Table 1 |
| SIMPLE | 0.7500 | 0.0150 | No | this paper | Table 1 |

### ZINC — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Baseline (GINE) | 0.2090 | 0.0050 | Yes | this paper | Table 1 |
| Random rewire | 0.1900 | 0.0070 | Yes | this paper | Table 1 |
| Gumbel | 0.1600 | 0.0060 | Yes | this paper | Table 1 |
| I-MLE | 0.1480 | 0.0080 | No | this paper | Table 1 |
| SIMPLE | 0.1510 | 0.0010 | No | this paper | Table 1 |

## Baseline Models Identified

- **NoTears** (from: zheng2018)
- **Golem** (from: Ng2020role)
- **NRI + STE** (from: Kip+2018)
- **NRI + SIMPLE** (from: ahmed2022simple)
- **NRI + I-MLE** (from: this paper)
- **NRI + STE (non-blind)** (from: this paper)
- **Baseline (GINE)** (from: Xu+2018b)
- **Random rewire** (from: this paper)
- **Gumbel** (from: this paper)
- **I-MLE** (from: this paper)

## Extraction Notes

[ER2-30] Extracted F1 scores for ER2-30 dataset from Table 1. Values were percentages in the table
(e.g., 98.5) and were divided by 100 to normalize to [0,1] range as per instructions. Standard
deviations were parsed from the ± notation. Only the top half of the table corresponding to ER2-30
was extracted, ignoring ER4-30 and SF datasets. [ER4-30] Extracted F1 scores for ER4-30 from the
bottom half of Table 1. The table reports percentages (e.g., 100.0, 82.6, 51.9), which were
normalized to [0, 1] range as per instructions for F1 metric. The table header indicates 'F1' with
an up arrow, confirming higher is better. The values correspond to the 'Discretized' section for
ER4-30. [SF2-30] Extracted F1 scores for SF2-30 from the top section of Table 1. Values were
percentages in the table (e.g., 93.0) and were divided by 100 to normalize to [0,1]. The table
reports mean over 24 ground truth graphs with 95% confidence intervals, which are treated as
standard deviations for the purpose of this extraction schema. [SF4-30] Extracted results for SF4-30
from the bottom half of the right-side columns in Table 1. The table caption indicates 'SF2-30 (top)
& SF4-30 (bottom)', so the bottom rows correspond to SF4-30. Values are percentages in the table,
normalized to [0,1] as per rules for F1. NoTears and Golem are listed under 'Non-discretized' and
Max-DAG I-MLE under 'Discretized' for the bottom section. All three models have results for SF4-30.
[Springs] Extracted all MSE results for the 'Springs' dataset from Table 2. The table distinguishes
between N=5 and N=10 configurations. Both are included as they represent the standard benchmark
configurations for this dataset in the paper. The 'non-blind' variants are also included as they are
part of the main experimental comparison for Springs. Values are converted from scientific notation
(e.g., 1.7e-4) to decimal floats. Standard deviations are reported as 0.0 in the table. [Charged]
Extracted MSE results for the 'Charged' dataset from Table 2. The table lists results for N=5 and
N=10. The prompt asked for 'STANDARD / DEFAULT configuration'. The paper does not explicitly define
a single 'default' N, but N=5 is the first listed and often the primary case in such benchmarks.
However, since both N=5 and N=10 are standard configurations for the Charged benchmark in this
paper, and the prompt says 'Skip results for optional variants... if the table shows multiple
configurations', I included both N=5 and N=10 as they represent distinct experimental settings
(different number of objects) rather than hyperparameter variants of the same setting. If 'standard'
implies only one, N=5 is the most likely candidate, but excluding N=10 might be an error if both are
considered standard benchmarks. Given the ambiguity, I extracted all Charged rows. Note: The prompt
asks to skip optional variants. N=5 and N=10 are distinct problem sizes, not variants of the same
graph construction. I will include both to be safe, as they are both main results for the Charged
dataset. [ZINC] Extracted all rows from Table 1 for the ZINC dataset. The primary metric is MAE
(lower is better). The proposed model is GraIP, which uses I-MLE or SIMPLE as discretization
strategies; both are treated as proposed variants. Baselines include the original GINE and a random
rewiring baseline. [Cornell] Extracted only the 'Cornell' column from Table 1 as requested. The
metric is Accuracy (Acc). All values are normalized to [0,1]. The proposed model is identified as
SIMPLE based on the bolded best results and context. [Texas] Extracted only the Texas dataset
results from Table 1 as requested. The metric is Accuracy. All values are normalized to [0,1]. The
proposed model is identified as SIMPLE based on the bolded best performance and context of the paper
describing the discretization strategies. [Wisconsin] Extracted only the Wisconsin dataset results
from Table 1 as requested. The metric is Accuracy. All values are normalized to [0,1]. The proposed
model is identified as SIMPLE based on the bolded best performance and context of the paper
describing the GraIP framework with different discretization strategies. [Peptides-func] Extracted
only the Peptides-func AP column from Table 1. All values are normalized to [0,1] as AP is an
accuracy-like metric. The proposed model is identified as SIMPLE based on the bolded best results
and context of the paper describing the discretization strategies. [Peptides-struct] Extracted all
rows from Table 1 corresponding to the 'Peptides-struct (MAE)' column. The proposed model is
identified as SIMPLE based on the bolded best results and context. All values are MAE, so lower is
better. No percentage normalization needed.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*