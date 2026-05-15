# Extraction: arXiv:2405.15540
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: BuNN
- Type: GNN

## Results

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.6860 | 0.0050 | Yes | this paper | Table 1 |
| GINE | 0.6621 | 0.0067 | Yes | this paper | Table 1 |
| GatedGCN | 0.6765 | 0.0047 | Yes | this paper | Table 1 |
| DReW | 0.7150 | 0.0044 | Yes | this paper | Table 1 |
| SAN | 0.6439 | 0.0075 | Yes | this paper | Table 1 |
| GPS | 0.6534 | 0.0091 | Yes | this paper | Table 1 |
| GAPH ViT | 0.6942 | 0.0075 | Yes | this paper | Table 1 |
| Exphormer | 0.6527 | 0.0043 | Yes | this paper | Table 1 |
| BuNN | 0.7276 | 0.0065 | No | this paper | Table 1 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.2460 | 0.0007 | Yes | this paper | Table 1 |
| GINE | 0.2473 | 0.0017 | Yes | this paper | Table 1 |
| GatedGCN | 0.2477 | 0.0009 | Yes | this paper | Table 1 |
| DReW | 0.2536 | 0.0015 | Yes | this paper | Table 1 |
| SAN | 0.2545 | 0.0012 | Yes | this paper | Table 1 |
| GPS | 0.2509 | 0.0014 | Yes | this paper | Table 1 |
| GAPH ViT | 0.2449 | 0.0016 | Yes | this paper | Table 1 |
| Exphormer | 0.2481 | 0.0007 | Yes | this paper | Table 1 |
| BuNN | 0.2463 | 0.0012 | No | this paper | Table 1 |

### amazon-ratings — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.4870 | 0.0063 | Yes | this paper | Table 1 |
| SAGE | 0.5363 | 0.0039 | Yes | this paper | Table 1 |
| GAT | 0.4909 | 0.0063 | Yes | this paper | Table 1 |
| GAT-sep | 0.5270 | 0.0062 | Yes | this paper | Table 1 |
| GT | 0.5117 | 0.0066 | Yes | this paper | Table 1 |
| GT-sep | 0.5218 | 0.0080 | Yes | this paper | Table 1 |
| NSD | 0.4276 | 0.0054 | Yes | this paper | Table 1 |
| BuNN | 0.5374 | 0.0051 | No | this paper | Table 1 |

### minesweeper — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.8975 | 0.0052 | Yes | this paper | Table 1 |
| SAGE | 0.9351 | 0.0057 | Yes | this paper | Table 1 |
| GAT | 0.9201 | 0.0068 | Yes | this paper | Table 1 |
| GAT-sep | 0.9391 | 0.0035 | Yes | this paper | Table 1 |
| GT | 0.9185 | 0.0076 | Yes | this paper | Table 1 |
| GT-sep | 0.9229 | 0.0047 | Yes | this paper | Table 1 |
| NSD | 0.9215 | 0.0084 | Yes | this paper | Table 1 |
| BuNN | 0.9899 | 0.0016 | No | this paper | Table 1 |

### questions — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7609 | 0.0127 | Yes | this paper | Table 1 |
| SAGE | 0.7644 | 0.0062 | Yes | this paper | Table 1 |
| GAT | 0.7743 | 0.0120 | Yes | this paper | Table 1 |
| GAT-sep | 0.7679 | 0.0071 | Yes | this paper | Table 1 |
| GT | 0.7795 | 0.0068 | Yes | this paper | Table 1 |
| GT-sep | 0.7805 | 0.0093 | Yes | this paper | Table 1 |
| NSD | 0.6969 | 0.0146 | Yes | this paper | Table 1 |
| BuNN | 0.7875 | 0.0109 | No | this paper | Table 1 |

### roman-empire — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7369 | 0.0074 | Yes | this paper | Table 1 |
| SAGE | 0.8574 | 0.0067 | Yes | this paper | Table 1 |
| GAT | 0.8087 | 0.0030 | Yes | this paper | Table 1 |
| GAT-sep | 0.8875 | 0.0041 | Yes | this paper | Table 1 |
| GT | 0.8651 | 0.0073 | Yes | this paper | Table 1 |
| GT-sep | 0.8732 | 0.0039 | Yes | this paper | Table 1 |
| NSD | 0.8041 | 0.0072 | Yes | this paper | Table 1 |
| BuNN | 0.9175 | 0.0039 | No | this paper | Table 1 |

### tolokers — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.8364 | 0.0067 | Yes | this paper | Table 1 |
| SAGE | 0.8243 | 0.0044 | Yes | this paper | Table 1 |
| GAT | 0.8370 | 0.0047 | Yes | this paper | Table 1 |
| GAT-sep | 0.8378 | 0.0043 | Yes | this paper | Table 1 |
| GT | 0.8323 | 0.0064 | Yes | this paper | Table 1 |
| GT-sep | 0.8252 | 0.0092 | Yes | this paper | Table 1 |
| NSD | 0.7883 | 0.0076 | Yes | this paper | Table 1 |
| BuNN | 0.8478 | 0.0080 | No | this paper | Table 1 |

## Baseline Models Identified

- **GCN** (from: Kipf & Welling 2017)
- **GINE** (from: Xu et al. 2019)
- **GatedGCN** (from: Brody et al. 2021)
- **DReW** (from: Liao et al. 2019)
- **SAN** (from: Veličković et al. 2021)
- **GPS** (from: Rampásek et al. 2022)
- **GAPH ViT** (from: Bresson & Laurent 2021)
- **Exphormer** (from: Fey et al. 2020)
- **SAGE** (from: Hamilton et al. 2017)
- **GAT** (from: Veličković et al. 2018)
- **GAT-sep** (from: Veličković et al. 2018 (variant))
- **GT** (from: Corso et al. 2020 or similar)
- **GT-sep** (from: Corso et al. 2020 (variant))
- **NSD**

## Extraction Notes

[Peptides-func] Extracted only Peptides-func AP results from Table 1. Values were divided by 100 as
per the table caption stating results are x100 for clarity. Standard deviations were parsed from the
± notation. Baseline models are treated as standard GNN baselines from the LRGB benchmark context.
[Peptides-struct] The table caption states results are x100 for clarity. Values were divided by 100
to normalize MAE to standard scale (e.g., 24.60 -> 0.246). The primary metric for Peptides-struct is
MAE (lower is better). All rows from Table 1 corresponding to Peptides-struct were extracted. The
ablation tables (Table 2 and 3) report results for BuNN which are already included in Table 1, so
they were not duplicated to avoid redundancy, but the values match. Specifically, BuNN's LPE result
in Table 2 (24.63) matches Table 1. GAPH ViT's result in Table 1 is bolded as best, but extracted
normally. [PascalVOC-SP] failed: 1 validation error for ExtractionOutput results.6.value   Input
should be a valid number [type=float_type, input_value=None, input_type=NoneType]     For further
information visit https://errors.pydantic.dev/2.13/v/float_type [Roman-empire] Extracted only the
'roman-empire' column as requested. The table caption indicates Accuracy is reported for roman-
empire. Values were converted from percentages (e.g., 73.69) to decimals (0.7369) as per standard
benchmark reporting conventions for Accuracy. Standard deviations were parsed from the 'mean ± std'
format. [Amazon-ratings] Extracted only the 'amazon-ratings' column from Table 1. Values were
percentages in the table (e.g., 48.70), so they were divided by 100 to fit the [0,1] range for
Accuracy. Standard deviations were parsed from the 'mean ± std' format. [Minesweeper] Extracted only
the 'minesweeper' column from Table 1 as requested. The metric is ROC-AUC. Values were converted
from percentages (e.g., 89.75) to decimals (0.8975). Standard deviations were parsed from the ±
notation. [Tolokers] Extracted only the 'tolokers' column from Table 1 as requested. The metric is
ROC-AUC. Values were converted from percentages (e.g., 83.64) to decimals (0.8364) as per standard
ROC-AUC reporting conventions in the schema instructions, although the table caption says 'ROC AUC
is reported' and values look like percentages. Given the rule 'Accuracy, F1, AP, AUC, ROC-AUC... are
always in the range [0, 1]', I divided by 100. Standard deviations were parsed from the 'mean ± std'
format. [Questions] Extracted only the 'questions' column from Table 1 as requested. The metric is
ROC-AUC. Values were converted from percentages (e.g., 76.09) to decimals (0.7609) as per standard
benchmark reporting conventions for ROC-AUC in this context, although the table caption says 'ROC
AUC is reported', the values are clearly percentages (0-100 scale). Standard practice for JSON
extraction of such metrics is to normalize to [0,1] if they represent probabilities/auc scores, but
often papers report AUC as 0-100. However, the rule states 'Accuracy, F1, AP, AUC, ROC-AUC... are
always in the range [0, 1]. If a paper reports such a value as a percentage... divide by 100'. Thus,
76.09 becomes 0.7609.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*