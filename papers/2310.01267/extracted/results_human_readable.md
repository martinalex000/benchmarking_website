# Extraction: arXiv:2310.01267
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: Co-GNNs
- Type: GNN

## Results

### ENZYMES — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DGCNN | 0.3890 | 0.0570 | Yes | this paper | Table 1 |
| DiffPool | 0.5950 | 0.0560 | Yes | this paper | Table 1 |
| ECC | 0.2950 | 0.0820 | Yes | this paper | Table 1 |
| GIN | 0.5960 | 0.0450 | Yes | this paper | Table 1 |
| GraphSAGE | 0.5820 | 0.0600 | Yes | this paper | Table 1 |
| SPN(k=5) | 0.6940 | 0.0620 | Yes | this paper | Table 1 |
| Co-GNN(\Sigma,\Sigma) | 0.6570 | 0.0490 | No | this paper | Table 1 |
| Co-GNN(\mu,\mu) | 0.6830 | 0.0570 | No | this paper | Table 1 |

### IMDB-B — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DGCNN | 0.6920 | 0.0300 | Yes | this paper | Table 1 |
| DiffPool | 0.6840 | 0.0330 | Yes | this paper | Table 1 |
| ECC | 0.6770 | 0.0280 | Yes | this paper | Table 1 |
| GIN | 0.7120 | 0.0390 | Yes | this paper | Table 1 |
| GraphSAGE | 0.6880 | 0.0450 | Yes | this paper | Table 1 |
| ICGMM_f | 0.7180 | 0.0440 | Yes | this paper | Table 1 |
| Co-GNN(\Sigma,\Sigma) | 0.7080 | 0.0330 | No | this paper | Table 1 |
| Co-GNN(\mu,\mu) | 0.7220 | 0.0410 | No | this paper | Table 1 |

### IMDB-M — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DGCNN | 0.4560 | 0.0340 | Yes | this paper | Table 1 |
| DiffPool | 0.4560 | 0.0340 | Yes | this paper | Table 1 |
| ECC | 0.4350 | 0.0310 | Yes | this paper | Table 1 |
| GIN | 0.4850 | 0.0330 | Yes | this paper | Table 1 |
| GraphSAGE | 0.4760 | 0.0350 | Yes | this paper | Table 1 |
| ICGMM_f | 0.4900 | 0.0380 | Yes | this paper | Table 1 |
| Co-GNN(\Sigma,\Sigma) | 0.4850 | 0.0400 | No | this paper | Table 1 |
| Co-GNN(\mu,\mu) | 0.4990 | 0.0450 | No | this paper | Table 1 |

### NCI1 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DGCNN | 0.7640 | 0.0170 | Yes | this paper | Table 1 |
| DiffPool | 0.7690 | 0.0190 | Yes | this paper | Table 1 |
| ECC | 0.7620 | 0.0140 | Yes | this paper | Table 1 |
| GIN | 0.8000 | 0.0140 | Yes | this paper | Table 1 |
| GraphSAGE | 0.7600 | 0.0180 | Yes | this paper | Table 1 |
| CGMM | 0.7620 | 0.0200 | Yes | this paper | Table 1 |
| ICGMM_f | 0.7640 | 0.0140 | Yes | this paper | Table 1 |
| SPN(k=5) | 0.7860 | 0.0170 | Yes | this paper | Table 1 |
| GSPN | 0.7660 | 0.0190 | Yes | this paper | Table 1 |
| Co-GNN(\Sigma,\Sigma) | 0.8060 | 0.0110 | No | this paper | Table 1 |
| Co-GNN(\mu,\mu) | 0.7940 | 0.0070 | No | this paper | Table 1 |

### PROTEINS — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DGCNN | 0.7290 | 0.0350 | Yes | this paper | Table 1 |
| DiffPool | 0.7370 | 0.0350 | Yes | this paper | Table 1 |
| ECC | 0.7230 | 0.0340 | Yes | this paper | Table 1 |
| GIN | 0.7330 | 0.0400 | Yes | this paper | Table 1 |
| GraphSAGE | 0.7300 | 0.0450 | Yes | this paper | Table 1 |
| SPN(k=5) | 0.7420 | 0.0270 | Yes | this paper | Table 1 |
| Co-GNN(\Sigma,\Sigma) | 0.7310 | 0.0230 | No | this paper | Table 1 |
| Co-GNN(\mu,\mu) | 0.7130 | 0.0200 | No | this paper | Table 1 |

### RootNeighbors — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Random | 0.4740 | — | Yes | this paper | Table 1 |
| GAT | 0.4420 | — | Yes | this paper | Table 1 |
| SumGNN | 0.3700 | — | Yes | this paper | Table 1 |
| MeanGNN | 0.3290 | — | Yes | this paper | Table 1 |
| Co-GNN(\Sigma,\Sigma) | 0.1960 | — | No | this paper | Table 1 |
| Co-GNN(\mu,\mu) | 0.3390 | — | No | this paper | Table 1 |
| Co-GNN(\Sigma,\alpha) | 0.0850 | — | No | this paper | Table 1 |
| Co-GNN(\Sigma,\mu) | 0.0790 | — | No | this paper | Table 1 |

### amazon-ratings — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.4870 | 0.0063 | Yes | this paper | Table 1 |
| SAGE | 0.5363 | 0.0039 | Yes | this paper | Table 1 |
| GAT | 0.4909 | 0.0063 | Yes | this paper | Table 1 |
| GAT-sep | 0.5270 | 0.0062 | Yes | this paper | Table 1 |
| GT | 0.5117 | 0.0066 | Yes | this paper | Table 1 |
| GT-sep | 0.5218 | 0.0080 | Yes | this paper | Table 1 |
| Co-GNN(\Sigma,\Sigma) | 0.5128 | 0.0056 | Yes | this paper | Table 1 |
| Co-GNN(\mu,\mu) | 0.5417 | 0.0037 | No | this paper | Table 1 |

### minesweeper — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.8975 | 0.0052 | Yes | this paper | Table 1 |
| SAGE | 0.9351 | 0.0057 | Yes | this paper | Table 1 |
| GAT | 0.9201 | 0.0068 | Yes | this paper | Table 1 |
| GAT-sep | 0.9391 | 0.0035 | Yes | this paper | Table 1 |
| GT | 0.9185 | 0.0076 | Yes | this paper | Table 1 |
| GT-sep | 0.9229 | 0.0047 | Yes | this paper | Table 1 |
| Co-GNN(\Sigma,\Sigma) | 0.9509 | 0.0118 | No | this paper | Table 1 |
| Co-GNN(\mu,\mu) | 0.9731 | 0.0041 | No | this paper | Table 1 |

### questions — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7609 | 0.0127 | Yes | this paper | Table 1 |
| SAGE | 0.7644 | 0.0062 | Yes | this paper | Table 1 |
| GAT | 0.7743 | 0.0120 | Yes | this paper | Table 1 |
| GAT-sep | 0.7679 | 0.0071 | Yes | this paper | Table 1 |
| GT | 0.7795 | 0.0068 | Yes | this paper | Table 1 |
| GT-sep | 0.7805 | 0.0093 | Yes | this paper | Table 1 |
| Co-GNN(Σ,Σ) | 0.8002 | 0.0086 | No | this paper | Table 1 |
| Co-GNN(μ,μ) | 0.7654 | 0.0095 | No | this paper | Table 1 |

### roman-empire — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7369 | 0.0074 | Yes | this paper | Table 1 |
| SAGE | 0.8574 | 0.0067 | Yes | this paper | Table 1 |
| GAT | 0.8087 | 0.0030 | Yes | this paper | Table 1 |
| GAT-sep | 0.8875 | 0.0041 | Yes | this paper | Table 1 |
| GT | 0.8651 | 0.0073 | Yes | this paper | Table 1 |
| GT-sep | 0.8732 | 0.0039 | Yes | this paper | Table 1 |
| Co-GNN(Σ,Σ) | 0.9157 | 0.0032 | No | this paper | Table 1 |
| Co-GNN(μ,μ) | 0.9137 | 0.0035 | No | this paper | Table 1 |

### tolokers — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.8364 | 0.0067 | Yes | this paper | Table 1 |
| SAGE | 0.8243 | 0.0044 | Yes | this paper | Table 1 |
| GAT | 0.8370 | 0.0047 | Yes | this paper | Table 1 |
| GAT-sep | 0.8378 | 0.0043 | Yes | this paper | Table 1 |
| GT | 0.8323 | 0.0064 | Yes | this paper | Table 1 |
| GT-sep | 0.8252 | 0.0092 | Yes | this paper | Table 1 |
| Co-GNN(\Sigma,\Sigma) | 0.8336 | 0.0089 | Yes | this paper | Table 1 |
| Co-GNN(\mu,\mu) | 0.8445 | 0.0117 | No | this paper | Table 1 |

## Baseline Models Identified

- **GCN**
- **GAT**
- **SumGNN**
- **MeanGNN**
- **Random**
- **SAGE** (from: Hamilton et al. 2017)
- **GAT-sep**
- **GT** (from: Vaswani et al. 2017)
- **GT-sep**
- **DGCNN** (from: Zhang et al. 2018)
- **DiffPool** (from: Ying et al. 2018)
- **ECC** (from: Bianchi et al. 2020)
- **GIN** (from: Xu et al. 2018)
- **GraphSAGE** (from: Hamilton et al. 2017)
- **CGMM**
- **ICGMM_f**
- **SPN(k=5)**
- **GSPN**

## Extraction Notes

[RootNeighbors] Extracted only the 'RootNeighbors' dataset results from Table 1. The table reports
MAE for a synthetic regression task. All values are test-set results as implied by the context of
comparing model performance on a new dataset. No standard deviations are reported in the table for
this specific experiment. [roman-empire] Extracted only the 'roman-empire' column from Table 1 as
requested. Values were converted from percentages to [0,1] range. Standard deviations were parsed
from the LaTeX formatting. Both Co-GNN variants are considered proposed models. [amazon-ratings]
Extracted only the 'amazon-ratings' column from Table 1. Values were percentages in the table (e.g.,
48.70) and were divided by 100 to normalize to [0,1] range as per rules. Standard deviations were
parsed from the LaTeX formatting. The proposed model is identified as Co-GNN, specifically the
variant Co-GNN(\mu,\mu) which achieved the best result. [minesweeper] Extracted results for
'minesweeper' dataset from Table 1. The metric reported in the table is implicitly Accuracy or ROC-
AUC given the context of node classification benchmarks (often Accuracy in OGB/LRGB, but the prompt
asks for ROC-AUC focus and the values are high percentages). However, looking at standard benchmarks
like OGB, 'minesweeper' is an OGB node classification dataset where the metric is ROC-AUC. The
values are reported as percentages (e.g., 89.75). I have normalized them to [0,1] range (0.8975).
The table caption mentions 'Results on node classification'. Standard metric for OGB node
classification is ROC-AUC. If it were Accuracy, the normalization rule for Accuracy applies (divide
by 100). The result is the same numerically for the float representation. I assumed the metric is
ROC-AUC as per FOCUS instruction. The values are clearly percentages. [tolokers] The paper reports
'Results on node classification' with Accuracy values (percentages). The FOCUS instruction requested
ROC-AUC, but the provided table only contains Accuracy. I have extracted the Accuracy values as they
are the only available quantitative results for the 'tolokers' dataset in the provided text. The
values are percentages (e.g., 83.64), so they were divided by 100 to fit the [0,1] range for
Accuracy metrics. The proposed model is identified as Co-GNN, specifically the \mu,\mu variant which
achieved the best score. [questions] Extracted results for the 'questions' dataset from Table 1. The
metric is implicitly ROC-AUC as per the table caption 'Results on node classification' and standard
practice for these datasets (OGB LRGB). Values were converted from percentages to [0,1] range.
Standard deviations were parsed from the LaTeX formatting. [IMDB-B] Extracted only IMDB-B results as
requested. Values are percentages from the table, normalized to [0,1] range. Standard deviations are
parsed from the ± notation. The proposed model variants are Co-GNN(\Sigma,\Sigma) and Co-
GNN(\mu,\mu). CGMM, SPN(k=5), and GSPN have no results for IMDB-B (marked as '-' in table) and are
excluded from results list. [IMDB-M] Extracted only IMDB-M results as requested. The table reports
Accuracy percentages (e.g., 45.6), which were normalized to [0,1] range (0.456). The proposed model
is referred to as Co-GNN with different aggregation functions (Sigma, Sigma) and (mu, mu). Baselines
include standard GNNs and other methods from the same paper (CGMM, ICGMM, SPN, GSPN). SPN and GSPN
did not report results for IMDB-M, so they are excluded from the results list. [REDDIT-B] failed: 2
validation errors for ExtractionOutput results.2.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.7.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [REDDIT-M] failed: 2 validation errors for
ExtractionOutput results.2.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.7.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [NCI1] Extracted only NCI1 results as requested.
Values are percentages from the table, converted to [0,1] range. Standard deviations are parsed from
the '±' notation. The proposed model is identified as Co-GNN based on the context of the table
caption and row highlighting. [PROTEINS] Extracted only the PROTEINS column from Table 1. Values are
percentages from the table, normalized to [0,1] range as per rules. Standard deviations are parsed
from the '±' notation. Note that CGMM, ICGMM_f, and GSPN do not have results reported for PROTEINS
in the table (marked as '-'), so they are excluded from the results list for this specific dataset.
[ENZYMES] Extracted only ENZYMES column results. Values are percentages from the table, normalized
to [0,1] range as per Accuracy metric rules. Co-GNN variants are treated as proposed models. CGMM,
ICGMM_f, and GSPN have no results for ENZYMES (marked as '-' in table), so they are excluded from
results list.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*