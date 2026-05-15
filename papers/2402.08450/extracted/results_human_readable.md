# Extraction: arXiv:2402.08450
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: Subgraphormer + PE (0.3M params)
- Type: GraphTransformer

## Results

### Alchemy-12k — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.1800 | 0.0060 | Yes | Xu et al. 2018 | Table 1 |
| SignNet | 0.1130 | 0.0020 | Yes | Lim et al. 2022 | Table 1 |
| delta-2-GNN | 0.1180 | 0.0010 | Yes | Morris et al. 2020 | Table 1 |
| delta-2-LGNN | 0.1220 | 0.0030 | Yes | Morris et al. 2020 | Table 1 |
| SpeqNet | 0.1150 | 0.0010 | Yes | Morris et al. 2022 | Table 1 |
| GNN-IR | 0.1190 | 0.0020 | Yes | Dupty et al. 2022 | Table 1 |
| PF-GNN | 0.1110 | 0.0100 | Yes | Dupty et al. 2021 | Table 1 |
| PPGN++(6) | 0.1090 | 0.0010 | Yes | Puny et al. 2023 | Table 1 |
| Recon. GNN | 0.1250 | 0.0010 | Yes | Cotta et al. 2021 | Table 1 |
| DS-GNN (NM) | 0.1160 | 0.0010 | Yes | Bevilacqua et al. 2023 | Table 1 |
| GNN-SSWL+ | 0.1160 | 0.0020 | Yes | Zhang et al. 2023 | Table 1 |
| Subgraphormer | 0.1140 | 0.0010 | Yes | this paper | Table 1 |
| Subgraphormer + PE | 0.1130 | 0.0020 | No | this paper | Table 1 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5930 | 0.0023 | Yes | Kipf 2016 | Table 1 |
| GIN | 0.5498 | 0.0079 | Yes | Xu 2018 | Table 1 |
| GatedGCN | 0.5864 | 0.0077 | Yes | Bresson 2017 | Table 1 |
| GatedGCN+RWSE | 0.6069 | 0.0035 | Yes | Dwivedi 2022 | Table 1 |
| Transf.+LapPE | 0.6326 | 0.0126 | Yes | Dwivedi 2022 | Table 1 |
| SAN+LapPE | 0.6384 | 0.0121 | Yes | Kreuzer 2021 | Table 1 |
| SAN+RWSE | 0.6439 | 0.0075 | Yes | Kreuzer 2021 | Table 1 |
| GPS | 0.6535 | 0.0041 | Yes | Rampásek 2022 | Table 1 |
| GNN-SSWL+ | 0.5847 | 0.0050 | Yes | Zhang 2023 | Table 1 |
| Subgraphormer | 0.6415 | 0.0052 | No | this paper | Table 1 |
| Subgraphormer + PE | 0.6373 | 0.0110 | No | this paper | Table 1 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3496 | 0.0013 | Yes | Kipf 2016 | Table 1 |
| GIN | 0.3547 | 0.0045 | Yes | Xu 2018 | Table 1 |
| GatedGCN | 0.3420 | 0.0013 | Yes | Bresson 2017 | Table 1 |
| GatedGCN+RWSE | 0.3357 | 0.0006 | Yes | Dwivedi 2022 | Table 1 |
| Transf.+LapPE | 0.2529 | 0.0016 | Yes | Dwivedi 2022 | Table 1 |
| SAN+LapPE | 0.2683 | 0.0043 | Yes | Kreuzer 2021 | Table 1 |
| SAN+RWSE | 0.2545 | 0.0012 | Yes | Kreuzer 2021 | Table 1 |
| GPS | 0.2500 | 0.0005 | Yes | Rampavsek 2022 | Table 1 |
| GNN-SSWL+ | 0.2570 | 0.0006 | Yes | Zhang 2023 | Table 1 |
| Subgraphormer | 0.2494 | 0.0020 | Yes | this paper | Table 1 |
| Subgraphormer + PE | 0.2475 | 0.0007 | No | this paper | Table 1 |

### ZINC-12k — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Subgraphormer + PE | 0.0630 | 0.0010 | No | this paper | Table 1 |
| Subgraphormer | 0.0670 | 0.0070 | No | this paper | Table 1 |
| GNN-SSWL+ | 0.0700 | 0.0050 | Yes | Zhang 2023 | Table 1 |
| GPS | 0.0700 | 0.0040 | Yes | Rampásek 2022 | Table 1 |
| PPGN++(6) | 0.0710 | 0.0010 | Yes | Puny 2023 | Table 1 |
| SUN | 0.0830 | 0.0030 | Yes | Frasca 2022 | Table 1 |
| GNN-SSWL | 0.0820 | 0.0030 | Yes | Zhang 2023 | Table 1 |
| URPE | 0.0860 | 0.0070 | Yes | Luo 2022 | Table 1 |
| DS-GNN (efficient) | 0.0870 | 0.0030 | Yes | Bevilacqua 2023 | Table 1 |
| GNN-AK+ | 0.0910 | 0.0020 | Yes | Zhao 2022 | Table 1 |
| CIN (small) | 0.0940 | 0.0040 | Yes | Bodnar 2021 | Table 1 |
| K-Subgraph SAT | 0.0940 | 0.0080 | Yes | Chen 2022 | Table 1 |
| DSS-GNN | 0.1020 | 0.0030 | Yes | Bevilacqua 2021 | Table 1 |
| GSN | 0.1010 | 0.0100 | Yes | Bouritsas 2022 | Table 1 |
| GNN-AK | 0.1050 | 0.0100 | Yes | Zhao 2022 | Table 1 |
| NGNN | 0.1110 | 0.0030 | Yes | Zhang 2021 | Table 1 |
| DS-GNN | 0.1160 | 0.0090 | Yes | Bevilacqua 2021 | Table 1 |
| Graphormer | 0.1220 | 0.0060 | Yes | Ying 2021 | Table 1 |
| SAN | 0.1390 | 0.0060 | Yes | Kreuzer 2021 | Table 1 |
| OSAN | 0.1540 | 0.0080 | Yes | Qian 2022 | Table 1 |
| GIN | 0.1630 | 0.0040 | Yes | Xu 2018 | Table 1 |
| Graphormer-GD | 0.0810 | 0.0090 | Yes | Zhang 2023 | Table 1 |
| DSS-GNN (EGO+) | 0.1020 | 0.0030 | Yes | Bevilacqua 2021 | Table 2 |
| Subgraphormer + product graph PE | 0.0630 | 0.0003 | No | this paper | Table 3 |
| Subgraphormer + concatenation PE | 0.0710 | 0.0030 | No | this paper | Table 3 |

### ZINC-Full — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| CIN (small) | 0.0440 | 0.0030 | Yes | Bodnar et al. 2021 | Table 1 |
| PPGN++(6) | 0.0200 | 0.0010 | Yes | Puny et al. 2023 | Table 1 |
| URPE | 0.0280 | 0.0020 | Yes | Luo et al. 2022 | Table 1 |
| Graphormer | 0.0520 | 0.0050 | Yes | Ying et al. 2021 | Table 1 |
| Graphormer-GD | 0.0250 | 0.0040 | Yes | Zhang et al. 2023 | Table 1 |
| NGNN | 0.0290 | 0.0010 | Yes | Zhang et al. 2021 | Table 1 |
| DSS-GNN | 0.0290 | 0.0030 | Yes | Bevilacqua et al. 2021 | Table 1 |
| SUN | 0.0240 | 0.0030 | Yes | Frasca et al. 2022 | Table 1 |
| GNN-SSWL | 0.0260 | 0.0010 | Yes | Zhang et al. 2023 | Table 1 |
| GNN-SSWL+ | 0.0220 | 0.0010 | Yes | Zhang et al. 2023 | Table 1 |
| Subgraphormer | 0.0200 | 0.0020 | No | this paper | Table 1 |
| Subgraphormer + PE | 0.0230 | 0.0010 | No | this paper | Table 1 |

### ogbg-molbace — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7915 | 0.0144 | Yes | Kipf 2016 | Table 1 |
| GIN | 0.7297 | 0.0400 | Yes | Xu 2018 | Table 1 |
| Recon. GNN | 0.7632 | 0.0140 | Yes | Cotta 2021 | Table 1 |
| OSAN | 0.7230 | 0.0660 | Yes | Qian 2022 | Table 1 |
| DS-GNN | 0.7841 | 0.0194 | Yes | Bevilacqua 2023 | Table 1 |
| GNN-SSWL+ | 0.8270 | 0.0180 | Yes | Zhang 2023 | Table 1 |
| Subgraphormer | 0.8162 | 0.0355 | Yes | this paper | Table 1 |
| Subgraphormer + PE | 0.8435 | 0.0065 | No | this paper | Table 1 |

### ogbg-molesol — RMSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 1.1140 | 0.0360 | Yes | Kipf 2016 | Table 1 |
| GIN | 1.1730 | 0.0570 | Yes | Xu 2018 | Table 1 |
| Recon. GNN | 1.0260 | 0.0330 | Yes | Cotta 2021 | Table 1 |
| OSAN | 0.9800 | 0.0860 | Yes | Qian 2022 | Table 1 |
| DS-GNN | 0.8470 | 0.0150 | Yes | Bevilacqua 2023 | Table 1 |
| GNN-SSWL+ | 0.8370 | 0.0190 | Yes | Zhang 2023 | Table 1 |
| Subgraphormer | 0.8320 | 0.0430 | Yes | this paper | Table 1 |
| Subgraphormer + PE | 0.8260 | 0.0100 | No | this paper | Table 1 |

### ogbg-molhiv — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7606 | 0.0097 | Yes | Kipf 2016 | Table 1 |
| GIN | 0.7558 | 0.0140 | Yes | Xu 2018 | Table 1 |
| PNA | 0.7905 | 0.0132 | Yes | Corso 2020 | Table 1 |
| GSN | 0.8039 | 0.0090 | Yes | Bouritsas 2022 | Table 1 |
| CIN | 0.8094 | 0.0057 | Yes | Bodnar 2021 | Table 1 |
| SAN | 0.7785 | 0.0024 | Yes | Kreuzer 2021 | Table 1 |
| GPS | 0.7880 | 0.0101 | Yes | Rampásek 2022 | Table 1 |
| NGNN | 0.7834 | 0.0186 | Yes | Zhang 2021 | Table 1 |
| Recon. GNN | 0.7632 | 0.0140 | Yes | Cotta 2021 | Table 1 |
| DS-GNN | 0.7740 | 0.0219 | Yes | Bevilacqua 2021 | Table 1 |
| DSS-GNN | 0.7678 | 0.0166 | Yes | Bevilacqua 2021 | Table 1 |
| GNN-AK+ | 0.7961 | 0.0119 | Yes | Zhao 2022 | Table 1 |
| SUN | 0.8003 | 0.0055 | Yes | Frasca 2022 | Table 1 |
| GNN-SSWL+ | 0.7958 | 0.0035 | Yes | Zhang 2023 | Table 1 |
| Subgraphormer | 0.8038 | 0.0192 | No | this paper | Table 1 |
| Subgraphormer + PE | 0.7948 | 0.0128 | No | this paper | Table 1 |

## Baseline Models Identified

- **GSN**, 0.5M params (from: Bouritsas et al. 2022)
- **CIN (small)**, 0.1M params (from: Bodnar et al. 2021)
- **GIN**, 0.5M params (from: Xu et al. 2018)
- **PPGN++(6)**, 0.5M params (from: Puny et al. 2023)
- **SAN**, 0.5M params (from: Kreuzer et al. 2021)
- **URPE**, 0.5M params (from: Luo et al. 2022)
- **GPS**, 0.4M params (from: Rampásek et al. 2022)
- **Graphormer**, 0.5M params (from: Ying et al. 2021)
- **Graphormer-GD**, 0.5M params (from: Zhang et al. 2023)
- **K-Subgraph SAT**, 0.5M params (from: Chen et al. 2022)
- **NGNN**, 0.5M params (from: Zhang et al. 2021)
- **DS-GNN**, 0.1M params (from: Bevilacqua et al. 2021)
- **DSS-GNN**, 0.1M params (from: Bevilacqua et al. 2021)
- **GNN-AK**, 0.5M params (from: Zhao et al. 2022)
- **GNN-AK+**, 0.5M params (from: Zhao et al. 2022)
- **SUN**, 0.5M params (from: Frasca et al. 2022)
- **OSAN**, 0.5M params (from: Qian et al. 2022)
- **DS-GNN (efficient)**, 0.5M params (from: Bevilacqua et al. 2023)
- **GNN-SSWL**, 0.3M params (from: Zhang et al. 2023)
- **GNN-SSWL+**, 0.4M params (from: Zhang et al. 2023)
- **Subgraphormer**, 0.3M params (from: this paper)
- **DSS-GNN (EGO+)** (from: Bevilacqua et al. 2021)
- **Subgraphormer + PE**, 0.3M params (from: this paper)
- **GCN** (from: Kipf 2016)
- **PNA** (from: Corso 2020)
- **CIN** (from: Bodnar 2021)
- **Recon. GNN** (from: Cotta 2021)
- **GatedGCN** (from: Bresson 2017)
- **GatedGCN+RWSE** (from: Dwivedi 2022)
- **Transf.+LapPE** (from: Dwivedi 2022)
- **SAN+LapPE** (from: Kreuzer 2021)
- **SAN+RWSE** (from: Kreuzer 2021)
- **SignNet** (from: Lim et al. 2022)
- **delta-2-GNN** (from: Morris et al. 2020)
- **delta-2-LGNN** (from: Morris et al. 2020)
- **SpeqNet** (from: Morris et al. 2022)
- **GNN-IR** (from: Dupty et al. 2022)
- **PF-GNN** (from: Dupty et al. 2021)
- **DS-GNN (NM)** (from: Bevilacqua et al. 2023)

## Extraction Notes

[ZINC-12k] Extracted all ZINC-12k MAE results from Table 1, Table 2, and Table 3. Table 1 contains
the main benchmark comparison. Table 2 contains stochastic sampling variants (100% sampling is the
standard configuration comparable to Table 1). Table 3 contains PE ablation variants. The proposed
model is identified as 'Subgraphormer + PE' which achieves the best MAE. All values are normalized
to [0,1] range (MAE values are small decimals). Standard deviations were parsed from the text (e.g.,
'0.063 ± 0.001'). Note: Table 2 and 3 report results for specific sampling ratios or PE variants;
the 100% sampling row in Table 2 and the 'product graph PE' row in Table 3 correspond to the main
proposed configuration reported in Table 1. [ZINC-Full] Extracted only ZINC-Full MAE results as
requested. Note that PPGN++(6) and Subgraphormer both report 0.020 MAE, with Subgraphormer having a
slightly higher std (0.002 vs 0.001). The table indicates PPGN++ is first (blue bold) and
Subgraphormer is also first (blue bold) for ZINC-Full, likely due to identical mean values or tie-
breaking rules not fully specified in the snippet, but both are extracted. [ogbg-molhiv] Extracted
all rows from Table 1 corresponding to the 'molhiv' column. The metric is ROC-AUC. Values were
converted from percentages (e.g., 76.06) to decimals (0.7606) as per standard OGB benchmark
reporting conventions and instructions. Standard deviations were parsed from the '±' notation.
'Subgraphormer + PE' is treated as a variant of the proposed model. [ogbg-molbace] Extracted results
for ogbg-molbace from Table 1 and Table 2. Table 1 contains the main comparison with baselines.
Table 2 contains a sensitivity analysis on sampling ratios (100%, 50%, 20%, 5%). The FOCUS
instruction requested the STANDARD/DEFAULT configuration, which corresponds to the 100% sampling
ratio results found in both tables. The values are identical in both tables for the 100% case. All
other sampling ratios were ignored as they represent optional variants. Values were converted from
percentages to [0,1] range. [ogbg-molesol] Extracted results for ogbg-molesol from Table 1 and Table
2. Table 1 contains the main comparison with baselines. Table 2 contains a sensitivity analysis on
sampling ratios for the proposed models and GNN-SSWL+. The standard configuration (100% sampling)
results from Table 2 are identical to those in Table 1. Only the 100% sampling ratio rows from Table
2 were included to avoid duplication, as they represent the standard/default configuration.
Secondary metrics (ROC-AUC for other datasets) were ignored as per instructions. [Peptides-func]
Extracted only Peptides-func AP results as requested. The table caption indicates these are test
results (standard for such tables unless specified otherwise). All values normalized to [0,1].
Standard deviations parsed correctly. 'Subgraphormer + PE' is treated as a variant of the proposed
model. [Peptides-struct] Extracted only Peptides-struct MAE results as requested. The table reports
test-set results (standard for LRGB benchmarks). All values are normalized correctly (MAE is not a
percentage). The proposed model is identified as 'Subgraphormer + PE' which achieves the best MAE.
[Alchemy-12k] Extracted all rows from Table 1 for the Alchemy-12k dataset. The metric is MAE (lower
is better). The proposed model is 'Subgraphormer + PE'. Note that 'SignNet' and 'Subgraphormer + PE'
share the same MAE value (0.113), with SignNet ranked 3rd and Subgraphormer + PE ranked 3rd in the
table's visual highlighting (orange bold), likely due to tie-breaking or specific reporting
conventions in the paper. All values are normalized to [0,1] range as they are MAE values < 1.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*