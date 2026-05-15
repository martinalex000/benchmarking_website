# Extraction: arXiv:2407.04236
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-13  **Confidence**: HIGH

## Proposed Model: ORC-Pool
- Type: Other

## Results

### COLLAB — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Diff | 0.7000 | 0.0200 | Yes | this paper | Table 1 |
| Mincut | 0.6700 | 0.0200 | Yes | this paper | Table 1 |
| DMoN | 0.6800 | 0.0200 | Yes | this paper | Table 1 |
| TV | 0.7000 | 0.0200 | Yes | this paper | Table 1 |
| ORC | 0.7100 | 0.0200 | No | this paper | Table 1 |

### CiteSeer — NMI ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| ORC (us) | 0.3500 | 0.0400 | No | this paper | Table 1 |
| Diff | 0.2400 | 0.1200 | Yes | this paper | Table 1 |
| Mincut | 0.3100 | 0.0400 | Yes | this paper | Table 1 |
| DMoN | 0.2900 | 0.0300 | Yes | this paper | Table 1 |
| TV | 0.3000 | 0.0500 | Yes | this paper | Table 1 |
| EMD | 0.3500 | 0.0400 | Yes | this paper | Table 2 |
| Sinkhorn | 0.3500 | 0.0300 | Yes | this paper | Table 2 |
| ORC-approx | 0.3500 | 0.0300 | Yes | this paper | Table 2 |
| ORC (us) (4 iterations) | 0.3500 | 0.0400 | No | this paper | Table 3 |
| ORC (us) (2 iterations) | 0.3400 | 0.0300 | No | this paper | Table 3 |
| ORC (us) (6 iterations) | 0.3300 | 0.0200 | No | this paper | Table 3 |
| ORC (us) with GAT | 0.3400 | 0.0400 | No | this paper | Table 4 |
| ORC (us) with GIN | 0.3500 | 0.0400 | No | this paper | Table 4 |
| Curv | 0.3200 | — | Yes | this paper | Table 5 |

### Cora — NMI ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Diff | 0.2000 | 0.0400 | Yes | this paper | Table 1 |
| Mincut | 0.4300 | 0.0300 | Yes | this paper | Table 1 |
| DMoN | 0.3700 | 0.0500 | Yes | this paper | Table 1 |
| TV | 0.3300 | 0.0500 | Yes | this paper | Table 1 |
| ORC (us) | 0.4700 | 0.0400 | No | this paper | Table 1 |
| EMD | 0.4700 | 0.0400 | Yes | this paper | Table 2 |
| Sinkhorn | 0.4500 | 0.0300 | Yes | this paper | Table 2 |
| ORC-approx | 0.4500 | 0.0300 | Yes | this paper | Table 2 |
| ORC (us) [2 iters] | 0.4500 | 0.0400 | No | this paper | Table 3 |
| ORC (us) [4 iters] | 0.4700 | 0.0400 | No | this paper | Table 3 |
| ORC (us) [6 iters] | 0.4400 | 0.0500 | No | this paper | Table 3 |
| CurvPool | 0.3500 | — | Yes | this paper | Table 5 |

### ENZYMES — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Diff | 0.3100 | 0.0300 | Yes | this paper | Table 1 |
| Mincut | 0.3700 | 0.0500 | Yes | this paper | Table 1 |
| DMoN | 0.4000 | 0.0400 | Yes | this paper | Table 1 |
| TV | 0.3700 | 0.0500 | Yes | this paper | Table 1 |
| ORC | 0.3800 | 0.0600 | No | this paper | Table 1 |

### IMDB-BINARY — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Diff | 0.6400 | 0.0600 | Yes | this paper | Table 1 |
| Mincut | 0.6500 | 0.0500 | Yes | this paper | Table 1 |
| DMoN | 0.6500 | 0.0400 | Yes | this paper | Table 1 |
| TV | 0.5400 | 0.0300 | Yes | this paper | Table 1 |
| ORC-Pool | 0.7100 | 0.0400 | No | this paper | Table 1 |
| HighCurvPool | 0.7100 | 0.0510 | Yes | Sanders et al. | Table 3 |

### MUTAG — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Diff | 0.8300 | 0.0900 | Yes | this paper | Table 1 |
| Mincut | 0.8300 | 0.0700 | Yes | this paper | Table 1 |
| DMoN | 0.8400 | 0.0800 | Yes | this paper | Table 1 |
| TV | 0.8300 | 0.0800 | Yes | this paper | Table 1 |
| ORC | 0.9000 | 0.0600 | No | this paper | Table 1 |

### OGBN-ARXIV — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Diff | 0.6500 | 0.0310 | Yes | this paper | Table 1 |
| Mincut | 0.7000 | 0.0270 | Yes | this paper | Table 1 |
| DMoN | 0.6800 | 0.0280 | Yes | this paper | Table 1 |
| TV | 0.6800 | 0.0400 | Yes | this paper | Table 1 |
| ORC (us) | 0.7200 | 0.0360 | No | this paper | Table 1 |

### PROTEINS — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Diff | 0.7500 | 0.0400 | Yes | this paper | Table 1 |
| Mincut | 0.7600 | 0.0500 | Yes | this paper | Table 1 |
| DMoN | 0.7600 | 0.0500 | Yes | this paper | Table 1 |
| TV | 0.7500 | 0.0400 | Yes | this paper | Table 1 |
| ORC-Pool | 0.7800 | 0.0400 | No | this paper | Table 1 |
| HighCurvPool | 0.7700 | 0.0610 | Yes | Sanders et al. | Table 4 |

### PubMed — NMI ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Diff | 0.0300 | 0.0200 | Yes | this paper | Table 1 |
| Mincut | 0.2300 | 0.0400 | Yes | this paper | Table 1 |
| DMoN | 0.1800 | 0.0400 | Yes | this paper | Table 1 |
| TV | 0.2100 | 0.0300 | Yes | this paper | Table 1 |
| ORC-Pool | 0.2400 | 0.0400 | No | this paper | Table 1 |
| EMD | 0.2400 | 0.0400 | Yes | this paper | Table 2 |
| Sinkhorn | 0.2200 | 0.0500 | Yes | this paper | Table 2 |
| ORC-approx | 0.2100 | 0.0300 | Yes | this paper | Table 2 |
| CurvPool | 0.1500 | — | Yes | this paper | Table 3 |

### REDDIT-BINARY — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Diff | 0.8600 | 0.0200 | Yes | this paper | Table 1 |
| Mincut | 0.8500 | 0.0200 | Yes | this paper | Table 1 |
| DMoN | 0.8500 | 0.0200 | Yes | this paper | Table 1 |
| TV | 0.8500 | 0.0300 | Yes | this paper | Table 1 |
| ORC | 0.8800 | 0.0200 | No | this paper | Table 1 |

### ogbg-molhiv — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Diff | 0.6800 | 0.0520 | Yes | this paper | Table 1 |
| Mincut | 0.7000 | 0.0400 | Yes | this paper | Table 1 |
| DMoN | 0.7300 | 0.0370 | Yes | this paper | Table 1 |
| TV | 0.6900 | 0.0340 | Yes | this paper | Table 1 |
| ORC (us) | 0.7300 | 0.0480 | No | this paper | Table 1 |

## Baseline Models Identified

- **Diff**
- **Mincut**
- **DMoN**
- **TV**
- **CurvPool**
- **EMD**
- **Sinkhorn**
- **ORC-approx**
- **Curv**
- **HighCurvPool** (from: Sanders et al.)

## Extraction Notes

[Cora] The paper reports Node Clustering results using Normalized Mutual Information (NMI) as the
metric, not standard Accuracy. However, the table captions explicitly label the metric as 'accuracy
(nmi)'. Following the instruction to focus on the primary benchmark metric for the dataset as
reported in the tables, NMI is extracted. The FOCUS instruction asked for 'Accuracy', but since the
paper uses NMI for Cora in these tables, NMI is the correct value to extract. All values are
normalized to [0,1]. Standard deviations are extracted where present. Table 3 shows ablation on
iterations; all are included as they represent the proposed model's performance under different
configurations, though the standard configuration (4 iterations) is the best reported. Table 4 does
not contain Cora results (only CiteSeer). Table 5 repeats the main result for comparison with
CurvPool. [CiteSeer] The paper reports NMI (Normalized Mutual Information) as the metric for node
clustering on CiteSeer. The FOCUS instruction asked for 'Accuracy', but the paper explicitly states
'Average accuracy (NMI)' in the table captions, indicating NMI is the accuracy metric used for this
clustering task. All values are extracted from tables where CiteSeer results are present. Standard
configuration (4 iterations for ORC) is used for the main proposed model result in Table 1 and Table
5. Variants (iterations, base layers) are included as they represent different configurations of the
proposed method or baselines on the same dataset. [PubMed] The paper reports Node Clustering results
using Normalized Mutual Information (NMI) as the accuracy metric for the PubMed dataset. The FOCUS
instruction requested 'Accuracy', but the paper explicitly states 'Average accuracy (NMI)' in the
table captions. NMI is the standard metric for clustering in this context. All rows for PubMed from
Tables 1, 2, and 3 were extracted. Table 1 compares pooling layers, Table 2 compares curvature
computation methods, and Table 3 compares ORC-Pool with CurvPool. The proposed model is ORC-Pool
(referred to as 'ORC (us)' in tables). Baselines include Diff, Mincut, DMoN, TV, CurvPool, EMD,
Sinkhorn, and ORC-approx. Values are already in [0,1] range. [MUTAG] Extracted only MUTAG results
from Table 1 as requested. The table reports average classification accuracy. Values are already in
[0,1] range. Standard deviations are included. [ENZYMES] Extracted only ENZYMES dataset results from
Table 1. The table reports average classification accuracy. All values are already in [0,1] range.
Standard deviations are parsed from the ± notation. [PROTEINS] Extracted results for PROTEINS from
Table 1 (standard GCN-based pooling comparison) and Table 4 (comparison with CurvPool using 10-fold
CV). Table 3 contains results for PROTEINS with GAT/GIN backbones but these are ablation/variations;
the primary benchmark results are in Tables 1 and 4. The 'ORC (us)' label in Tables 3 and 4 refers
to the proposed ORC-Pool model. Values are normalized to [0,1]. [IMDB-BINARY] Extracted results for
IMDB-BINARY from Table 1 (comparison with state-of-the-art pooling layers) and Table 3 (comparison
with CurvPool). Table 1 reports results averaged over 10 trials with 80/10/10 split. Table 3 reports
results using 10-fold cross-validation. The proposed model ORC-Pool achieves 0.71 in both tables.
HighCurvPool is the baseline from the Sanders paper. [REDDIT-BINARY] Extracted results for REDDIT-
BINARY from Table 1. Table 3 reports results for varying Ricci flow iterations, but Table 1 presents
the standard comparison with state-of-the-art pooling layers, which is the primary benchmark result.
The value 0.88 for ORC is bolded in the source, indicating it is the best result. [COLLAB] Extracted
results for COLLAB dataset from Table 1. All values are normalized to [0,1] range as they represent
Accuracy. Standard deviations are parsed from the ± notation. [Peptides-func] The paper reports
results for 'PEPTIDES' (likely Peptides-func or Peptides-struct) in Table 1, but the metric is
'Average classification accuracy', not 'AP' (Average Precision). The FOCUS instruction explicitly
requests results for 'Peptides-func' with PRIMARY METRIC 'AP'. Table 1 does not report AP. Table 2
reports time/epoch, not accuracy/AP. Table 3 reports results for OGBG-MOLHIV. Therefore, no results
matching the specific criteria (Dataset: Peptides-func, Metric: AP) are present in the provided
text. [OGBN-ARXIV] Extracted all rows from Table 1 for the OGBN-ARXIV dataset. The table reports
Accuracy and Seconds/epoch. Per instructions, only Accuracy results were extracted. The proposed
model is identified as 'ORC (us)' based on the bold formatting and context ('us' implies the
authors' method). Baselines are Diff, Mincut, DMoN, and TV. No parameter counts were provided in the
text or table. [ogbg-molhiv] Extracted all rows from the provided table for the dataset ogbg-molhiv.
The table caption explicitly states it reports ROC-AUC on OGBG-MOLHIV. The proposed model is
identified as 'ORC (us)' based on the '(us)' label commonly used in papers to denote the authors'
method. Baselines are Diff, Mincut, DMoN, and TV. All values are normalized to [0,1] as they are
ROC-AUC scores.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*