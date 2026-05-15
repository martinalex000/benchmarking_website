# Extraction: Quantum Graph Attention Network: A Novel Quantum Multi-Head Attention Mechanism for Graph Learning
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: QGAT
- Type: GAT_variant

## Results

### PPI — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GAT | 0.9730 | 0.0020 | Yes | Hamilton et al. 2017 | Table 1 |
| GATv2 | 0.9820 | 0.0025 | Yes | Brody et al. 2021 | Table 1 |
| QGAT | 0.9890 | 0.0012 | No | this paper | Table 1 |

### PubMed — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GAT | 0.7810 | 0.0059 | Yes | Brody et al. 2021 | Table 1 |
| GATv2 | 0.7850 | 0.0038 | Yes | Brody et al. 2021 | Table 1 |
| QGAT | 0.7920 | 0.0062 | No | this paper | Table 1 |

### ogbl-citation2 — MRR ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GAT | 0.7595 | 0.0131 | Yes | Brody et al. 2021 | Table 1 |
| GATv2 | 0.8014 | 0.0071 | Yes | Brody et al. 2021 | Table 1 |
| QGAT | 0.8220 | 0.0127 | No | this paper | Table 1 |

### ogbl-collab — Hits@50 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GAT | 0.4663 | 0.0280 | Yes | Brody et al. 2021 | Table 1 |
| GATv2 | 0.4970 | 0.0308 | Yes | Brody et al. 2021 | Table 1 |
| QGAT | 0.5120 | 0.0192 | No | this paper | Table 1 |

### ogbn-arxiv — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GAT | 0.7154 | 0.0030 | Yes | Brody et al. 2021 | Table 1 |
| GATv2 | 0.7187 | 0.0025 | Yes | Brody et al. 2021 | Table 1 |
| QGAT | 0.7362 | 0.0042 | No | this paper | Table 1 |

### ogbn-products — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GAT | 0.7904 | 0.0154 | Yes | Brody et al. 2021 | Table 1 |
| GATv2 | 0.8063 | 0.0070 | Yes | Brody et al. 2021 | Table 1 |
| QGAT | 0.8210 | 0.0231 | No | this paper | Table 1 |

### ogbn-proteins — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GAT | 0.7863 | 0.0162 | Yes | Hamilton 2017 | Table 1 |
| GATv2 | 0.7952 | 0.0055 | Yes | Brody 2021 | Table 1 |
| QGAT | 0.7941 | 0.0021 | No | this paper | Table 1 |

## Baseline Models Identified

- **GAT** (from: Brody et al. 2021)
- **GATv2** (from: Brody et al. 2021)

## Extraction Notes

[PubMed] Extracted only PubMed results as requested. Values were percentages in the table (e.g.,
78.1), normalized to [0,1] range (0.781). Standard deviations were also divided by 100. The table
caption indicates results are averaged over 5 runs. [ogbn-arxiv] Extracted only ogbn-arxiv results
from Table 1. Values were percentages in the table (e.g., 71.54), normalized to [0,1] range as per
rules. Standard deviations were parsed from '±' notation. Note: The std values in the table are
likely scaled by 100 relative to the percentage format (e.g., 0.3 for 71.54% implies 0.3% std, which
is 0.003 in normalized form). I have adjusted the std to match the normalized value scale (dividing
by 100). [ogbn-products] Extracted only ogbn-products results as requested. Values were percentages
in the table (e.g., 79.04), so they were divided by 100 to fit the [0,1] range for Accuracy.
Standard deviations were parsed from the ± notation. [PPI] Extracted only PPI results as requested.
The table reports Micro-F1 for PPI. Values were converted from percentages (e.g., 97.3) to decimals
(0.973) per instructions. Standard deviations were parsed from the 'mean ± std' format. [ogbn-
proteins] Extracted only the ogbn-proteins column as requested. Values were converted from
percentages (e.g., 78.63) to decimals (0.7863) as per standard ROC-AUC reporting conventions in this
context, although the table caption says 'ROC-AUC' and values look like percentages. Standard
practice for OGB benchmarks is 0-100 scale often reported as such, but the schema rule says
'Accuracy, F1, AP, AUC, ROC-AUC... are always in the range [0, 1]'. Therefore, 78.63 becomes 0.7863.
Standard deviations were similarly scaled. [ogbl-collab] Extracted only ogbl-collab results as
requested. The table reports Hits@50 in percentage (%), so values were divided by 100 to normalize
to [0, 1]. Standard deviations were parsed from the 'mean ± std' format. Baseline citations point to
Brody et al. 2021. [ogbl-citation2] Extracted MRR results for ogbl-citation2 from Table 1. Values
were reported as percentages in the table caption context (implied by standard OGB reporting and
comparison with known baselines, though the table itself doesn't explicitly show '%' symbol in the
cells, the caption says 'MRR for ogbl-citation2' and typically OGB MRR is reported as percentage or
raw. However, looking at the values: 75.95, 80.14, 82.2. Standard OGB MRR is usually between 0 and
1. If these are percentages, they should be divided by 100. The caption says 'Metric: ... Mean
Reciprocal Rank (MRR)'. In OGB, MRR is often reported as a percentage in tables for readability, but
the metric definition is [0,1]. Given the values are > 1, they are clearly percentages. I have
normalized them to [0,1] range as per instructions for MRR.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*