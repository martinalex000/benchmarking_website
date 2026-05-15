# Extraction: arXiv:2306.05955
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: PathNN-SP+
- Type: Other

## Results

### CSL — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.1000 | 0.0000 | Yes | Xu et al. 2019 | Table 1 |
| 3WLGNN | 0.9780 | 0.1090 | Yes | Maron et al. 2019 | Table 1 |
| PathNN-SP | 0.9000 | 0.0000 | Yes | this paper | Table 1 |
| PathNN-SP+ | 1.0000 | 0.0000 | No | this paper | Table 1 |
| PathNN-AP | 1.0000 | 0.0000 | Yes | this paper | Table 1 |

### ENZYMES — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DGCNN | 0.3890 | 0.0570 | Yes | Zhang et al. 2018 | Table 1 |
| DiffPool | 0.5950 | 0.0560 | Yes | Ying et al. 2018 | Table 1 |
| ECC | 0.2950 | 0.0820 | Yes | Simonovsky et al. 2017 | Table 1 |
| GIN | 0.5960 | 0.0450 | Yes | Xu et al. 2019 | Table 1 |
| GraphSAGE | 0.5820 | 0.0600 | Yes | Hamilton et al. 2017 | Table 1 |
| GAT | 0.4950 | 0.0890 | Yes | Velickovic et al. 2018 | Table 1 |
| SPN (K=1) | 0.6750 | 0.0550 | Yes | Abboud et al. 2022 | Table 1 |
| SPN (K=5) | 0.6940 | 0.0620 | Yes | Abboud et al. 2022 | Table 1 |
| PathNet (N=10, K=2) | 0.6930 | 0.0540 | Yes | Sun et al. 2022 | Table 1 |
| Nested GNN | 0.3120 | 0.0670 | Yes | Zhang et al. 2021 | Table 1 |
| PathNN-P (K=1) | 0.7300 | 0.0520 | No | this paper | Table 1 |
| PathNN-SP (K=2) | 0.7160 | 0.0640 | No | this paper | Table 1 |
| PathNN-SP (K=3) | 0.6920 | 0.0470 | No | this paper | Table 1 |
| PathNN-SP+ (K=2) | 0.7250 | 0.0530 | No | this paper | Table 1 |
| PathNN-SP+ (K=3) | 0.7040 | 0.0310 | No | this paper | Table 1 |
| PathNN-AP (K=2) | 0.7180 | 0.0480 | No | this paper | Table 1 |
| PathNN-AP (K=3) | 0.6900 | 0.0530 | No | this paper | Table 1 |

### EXP-Class — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.5000 | 0.0000 | Yes | Xu et al. 2019 | Table 1 |
| 3WLGNN | 1.0000 | 0.0000 | Yes | Maron et al. 2019 | Table 1 |
| PathNN-SP | 1.0000 | 0.0000 | Yes | this paper | Table 1 |
| PathNN-SP+ | 1.0000 | 0.0000 | Yes | this paper | Table 1 |
| PathNN-AP | 1.0000 | 0.0000 | No | this paper | Table 1 |

### IMDB-B — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DGCNN | 0.6920 | 0.0300 | Yes | Zhang et al. 2018 | Table 1 |
| DiffPool | 0.6840 | 0.0330 | Yes | Ying et al. 2018 | Table 1 |
| ECC | 0.6770 | 0.0280 | Yes | Simonovsky et al. 2017 | Table 1 |
| GIN | 0.7120 | 0.0390 | Yes | Xu et al. 2019 | Table 1 |
| GraphSAGE | 0.6880 | 0.0450 | Yes | Hamilton et al. 2017 | Table 1 |
| GAT | 0.6920 | 0.0480 | Yes | Veličković et al. 2018 | Table 1 |
| PathNet (N=10, K=2) | 0.7040 | 0.0380 | Yes | Sun et al. 2022 | Table 1 |
| PathNN-P (K=1) | 0.7260 | 0.0330 | No | this paper | Table 1 |
| PathNN-SP (K=2) | 0.7080 | 0.0350 | No | this paper | Table 1 |
| PathNN-SP+ (K=2) | 0.7050 | 0.0340 | No | this paper | Table 1 |
| PathNN-AP (K=2) | 0.7170 | 0.0360 | No | this paper | Table 1 |

### IMDB-M — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DGCNN | 0.4560 | 0.0340 | Yes | Zhang et al. 2018 | Table 1 |
| DiffPool | 0.4560 | 0.0340 | Yes | Ying et al. 2018 | Table 1 |
| ECC | 0.4350 | 0.0310 | Yes | Simonovsky et al. 2017 | Table 1 |
| GIN | 0.4850 | 0.0330 | Yes | Xu et al. 2019 | Table 1 |
| GraphSAGE | 0.4760 | 0.0350 | Yes | Hamilton et al. 2017 | Table 1 |
| GAT | 0.4820 | 0.0490 | Yes | Velickovic et al. 2018 | Table 1 |
| PathNet | 0.4910 | 0.0360 | Yes | Sun et al. 2022 | Table 1 |
| PathNN-P (K=1) | 0.5080 | 0.0450 | No | this paper | Table 1 |
| PathNN-SP (K=2) | 0.5000 | 0.0410 | No | this paper | Table 1 |
| PathNN-SP+ (K=2) | 0.5070 | 0.0450 | No | this paper | Table 1 |
| PathNN-AP (K=2) | 0.4980 | 0.0420 | No | this paper | Table 1 |

### NCI1 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DGCNN | 0.7640 | 0.0170 | Yes | Zhang et al. 2018 | Table 1 |
| DiffPool | 0.7690 | 0.0190 | Yes | Ying et al. 2018 | Table 1 |
| ECC | 0.7620 | 0.0140 | Yes | Simonovsky et al. 2017 | Table 1 |
| GIN | 0.8000 | 0.0140 | Yes | Xu et al. 2019 | Table 1 |
| GraphSAGE | 0.7600 | 0.0180 | Yes | Hamilton et al. 2017 | Table 1 |
| GAT | 0.7730 | 0.0250 | Yes | Veličković et al. 2018 | Table 1 |
| SPN (K=1) | 0.8000 | 0.0150 | Yes | Abboud et al. 2022 | Table 1 |
| SPN (K=5) | 0.7860 | 0.0380 | Yes | Abboud et al. 2022 | Table 1 |
| PathNet (N=10, K=2) | 0.6410 | 0.0230 | Yes | Sun et al. 2022 | Table 1 |
| PathNN-P (K=1) | 0.7750 | 0.0160 | No | this paper | Table 1 |
| PathNN-SP (K=2) | 0.8200 | 0.0160 | No | this paper | Table 1 |
| PathNN-SP (K=3) | 0.8220 | 0.0170 | No | this paper | Table 1 |
| PathNN-SP+ (K=2) | 0.8100 | 0.0140 | No | this paper | Table 1 |
| PathNN-SP+ (K=3) | 0.8230 | 0.0190 | No | this paper | Table 1 |
| PathNN-AP (K=2) | 0.8130 | 0.0180 | No | this paper | Table 1 |
| PathNN-AP (K=3) | 0.8230 | 0.0170 | No | this paper | Table 1 |

### PROTEINS — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DGCNN | 0.7290 | 0.0350 | Yes | Zhang et al. 2018 | Table 1 |
| DiffPool | 0.7370 | 0.0350 | Yes | Ying et al. 2018 | Table 1 |
| ECC | 0.7230 | 0.0340 | Yes | Simonovsky et al. 2017 | Table 1 |
| GIN | 0.7330 | 0.0400 | Yes | Xu et al. 2019 | Table 1 |
| GraphSAGE | 0.7300 | 0.0450 | Yes | Hamilton et al. 2017 | Table 1 |
| GAT | 0.7090 | 0.0270 | Yes | Veličković et al. 2018 | Table 1 |
| SPN (K=1) | 0.7100 | 0.0370 | Yes | Abboud et al. 2022 | Table 1 |
| SPN (K=5) | 0.7420 | 0.0270 | Yes | Abboud et al. 2022 | Table 1 |
| PathNet (N=10, K=2) | 0.7050 | 0.0390 | Yes | Sun et al. 2022 | Table 1 |
| Nested GNN | 0.7420 | 0.0370 | Yes | Zhang et al. 2021 | Table 1 |
| PathNN-P (K=1) | 0.7520 | 0.0390 | No | this paper | Table 1 |
| PathNN-SP (K=2) | 0.7310 | 0.0310 | No | this paper | Table 1 |
| PathNN-SP (K=3) | 0.7220 | 0.0270 | No | this paper | Table 1 |
| PathNN-SP+ (K=2) | 0.7310 | 0.0370 | No | this paper | Table 1 |
| PathNN-SP+ (K=3) | 0.7320 | 0.0330 | No | this paper | Table 1 |
| PathNN-AP (K=2) | 0.7310 | 0.0490 | No | this paper | Table 1 |
| PathNN-AP (K=3) | 0.7310 | 0.0400 | No | this paper | Table 1 |

### Peptides-Functional — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5930 | 0.0023 | Yes | Kipf 2017 | Table 1 |
| GIN | 0.5498 | 0.0079 | Yes | Xu 2019 | Table 1 |
| GatedGCN | 0.5864 | 0.0077 | Yes | Bresson 2017 | Table 1 |
| PathNN-SP | 0.6816 | 0.0026 | No | this paper | Table 1 |
| PathNN-SP+ | 0.6784 | 0.0052 | No | this paper | Table 1 |
| PathNN-AP | 0.6807 | 0.0072 | No | this paper | Table 1 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3496 | 0.0013 | Yes | Kipf 2017 | Table 1 |
| GIN | 0.3547 | 0.0045 | Yes | Xu 2019 | Table 1 |
| GatedGCN | 0.3420 | 0.0013 | Yes | Bresson 2017 | Table 1 |
| PathNN-SP | 0.2545 | 0.0032 | Yes | this paper | Table 1 |
| PathNN-SP+ | 0.2540 | 0.0046 | No | this paper | Table 1 |
| PathNN-AP | 0.2569 | 0.0030 | Yes | this paper | Table 1 |

### ZINC12K — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.2780 | 0.0030 | Yes | Kipf 2017 | Table 1 |
| GraphSAGE | 0.3980 | 0.0020 | Yes | Hamilton 2017 | Table 1 |
| MoNet | 0.2920 | 0.0060 | Yes | Monti 2017 | Table 1 |
| GAT | 0.3840 | 0.0070 | Yes | Veličković 2018 | Table 1 |
| GIN | 0.3870 | 0.0150 | Yes | Xu 2019 | Table 1 |
| GatedGCN | 0.4350 | 0.0110 | Yes | Bresson 2017 | Table 1 |
| GatedGCN-E | 0.2820 | 0.0150 | Yes | Bresson 2017 | Table 1 |
| RingGNN-E | 0.3530 | 0.0190 | Yes | Chen 2019 | Table 1 |
| 3WLGNN | 0.4070 | 0.0280 | Yes | Maron 2019 | Table 1 |
| 3WLGNN-E | 0.2560 | 0.0540 | Yes | Maron 2019 | Table 1 |
| GNNML3 | 0.1610 | 0.0060 | Yes | Balcilar 2021 | Table 1 |
| Graphormer | 0.1220 | 0.0060 | Yes | Ying 2021 | Table 1 |
| CIN | 0.0790 | 0.0060 | Yes | Bodnar 2021 | Table 1 |
| ESAN | 0.1020 | 0.0030 | Yes | Bevilacqua 2022 | Table 1 |
| KP-GIN | 0.0930 | 0.0070 | Yes | Feng 2022 | Table 1 |
| AgentNet | 0.2580 | 0.0330 | Yes | Martinkus 2023 | Table 1 |
| PathNN-SP | 0.1040 | 0.0020 | Yes | this paper | Table 1 |
| PathNN-SP+ | 0.1310 | 0.0080 | Yes | this paper | Table 1 |
| PathNN-AP | 0.0900 | 0.0040 | No | this paper | Table 1 |

### ogbg-molhiv — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7606 | 0.0097 | Yes | Kipf 2017 | Table 1 |
| GIN | 0.7558 | 0.0140 | Yes | Xu 2019 | Table 1 |
| GCN+FLAG | 0.7683 | 0.0102 | Yes | Kong 2020 | Table 1 |
| GIN+FLAG | 0.7654 | 0.0114 | Yes | Kong 2020 | Table 1 |
| GSN | 0.7799 | 0.0100 | Yes | Bouritsas 2022 | Table 1 |
| HIMP | 0.7880 | 0.0082 | Yes | Fey 2020 | Table 1 |
| PNA | 0.7905 | 0.0132 | Yes | Corso 2020 | Table 1 |
| DGN | 0.7970 | 0.0097 | Yes | Beaini 2021 | Table 1 |
| Graphormer | 0.8051 | 0.0053 | Yes | Ying 2021 | Table 1 |
| CIN | 0.8094 | 0.0057 | Yes | Bodnar 2021 | Table 1 |
| ESAN | 0.7800 | 0.0142 | Yes | Bevilacqua 2022 | Table 1 |
| E-SPN | 0.7710 | 0.0120 | Yes | Abboud 2022 | Table 1 |
| GRWNN | 0.7838 | 0.0099 | Yes | Nikolentzos 2023 | Table 1 |
| AgentNet | 0.7833 | 0.0069 | Yes | Martinkus 2023 | Table 1 |
| PathNN-SP (K=2) | 0.7862 | 0.0130 | Yes | this paper | Table 1 |
| PathNN-SP+ (K=2) | 0.7917 | 0.0109 | No | this paper | Table 1 |
| PathNN-AP (K=2) | 0.7884 | 0.0146 | Yes | this paper | Table 1 |

## Baseline Models Identified

- **GIN** (from: Xu et al. 2019)
- **3WLGNN** (from: Maron et al. 2019)
- **PathNN-SP** (from: this paper)
- **PathNN-AP** (from: this paper)
- **PathNN-SP+** (from: this paper)
- **DGCNN** (from: Zhang et al. 2018)
- **DiffPool** (from: Ying et al. 2018)
- **ECC** (from: Simonovsky et al. 2017)
- **GraphSAGE** (from: Hamilton et al. 2017)
- **GAT** (from: Veličković et al. 2018)
- **SPN** (from: Abboud et al. 2022)
- **PathNet** (from: Sun et al. 2022)
- **Nested GNN** (from: Zhang et al. 2021)
- **GCN** (from: Kipf 2017)
- **GatedGCN** (from: Bresson 2017)
- **GCN+FLAG** (from: Kong 2020)
- **GIN+FLAG** (from: Kong 2020)
- **GSN** (from: Bouritsas 2022)
- **HIMP** (from: Fey 2020)
- **PNA** (from: Corso 2020)
- **DGN** (from: Beaini 2021)
- **Graphormer** (from: Ying 2021)
- **CIN** (from: Bodnar 2021)
- **ESAN** (from: Bevilacqua 2022)
- **E-SPN** (from: Abboud 2022)
- **GRWNN** (from: Nikolentzos 2023)
- **AgentNet** (from: Martinkus 2023)
- **PathNN-SP (K=2)** (from: this paper)
- **PathNN-AP (K=2)** (from: this paper)
- **MoNet** (from: Monti 2017)
- **GatedGCN-E** (from: Bresson 2017)
- **RingGNN-E** (from: Chen 2019)
- **3WLGNN-E** (from: Maron 2019)
- **GNNML3** (from: Balcilar 2021)
- **KP-GIN** (from: Feng 2022)

## Extraction Notes

[CSL] Extracted only CSL Accuracy results as requested. The table also contains EXP-Class and EXP-
Iso metrics which were ignored per instructions. Values were converted from percentages (e.g., 10.0
-> 0.1) to [0,1] range. [EXP-Class] Extracted only EXP-Class Accuracy results as requested. The
table caption indicates 'best results are highlighted in bold', but all PathNN variants and 3WLGNN
achieved 100.0%. GIN achieved 50.0%. Values were converted from percentages to [0,1] range. [DD]
failed: 2 validation errors for ExtractionOutput results.8.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.16.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [PROTEINS] Extracted all rows for the PROTEINS dataset
from Table 1. Values were converted from percentages to [0,1] range. Standard deviations were parsed
correctly. The proposed model variants (PathNN-P, PathNN-SP, etc.) are all included. Baseline models
are identified by their citations. [NCI1] Extracted all rows for the NCI1 dataset from Table 1.
Values were converted from percentages to [0,1] range. Standard deviations were parsed correctly.
Nested GNN and PathNet (N=10, K=2) had valid values for NCI1 (PathNet was OOM on DD but valid on
NCI1). PathNN-AP (K=3) had OOM on other datasets but valid on NCI1. All proposed model variants are
included. [ENZYMES] Extracted all rows from Table 1 for the ENZYMES dataset. Values were converted
from percentages to [0,1] range. Standard deviations were parsed correctly. Model names were
normalized slightly for JSON consistency (e.g., PathNN-P instead of PathNN-$\mathcal{P}$) but remain
identifiable. [IMDB-B] Extracted only IMDB-B results as requested. Note that some PathNN variants
(SP K=3, SP+ K=3) have '-' or 'OOM' for IMDB-B, so they are excluded. The proposed model name is
generalized to 'PathNN' with specific variants listed in the results. Baseline names are taken
directly from the table. Values are normalized from percentages to [0,1] range. [IMDB-M] Extracted
only IMDB-M results as requested. Note that some proposed model variants (PathNN-SP K=3, PathNN-AP
K=3) have '-' or 'OOM' for IMDB-M, so they are excluded. SPN and Nested GNN have NA for IMDB-M, so
they are excluded. All values converted from percentage to [0,1] range. [Peptides-func] Extracted
only Peptides-Functional results as requested. The table caption indicates the parameter budget is
500K for all models. The proposed model name is inferred as 'PathNN-SP' based on the best performing
variant 'PathNN-SP' (bolded). Other variants PathNN-SP+ and PathNN-AP are also included as they are
part of the proposed method family. Values converted from percentages to [0,1] range. [Peptides-
struct] Extracted only Peptides-struct MAE results as requested. The table caption mentions
'Peptides-Structural' and the column header says 'Peptides-Structural'. I have normalized the
dataset name to 'Peptides-struct' as per the FOCUS instruction. The proposed model is identified as
PathNN-SP+ because it achieves the best MAE (bolded) on Peptides-struct. All models share the same
parameter budget of 500K as stated in the caption. [ogbg-molhiv] Extracted all rows from Table 1 for
the ogbg-molhiv dataset. Values were converted from percentages (e.g., 76.06) to decimals (0.7606)
as per ROC-AUC normalization rules. The proposed model is identified as PathNN-SP+ (K=2) based on
the '+' notation often implying the final proposed variant, though the paper title/context would
confirm. All other PathNN variants are treated as baselines/ablations within the same paper.
[ZINC12K] Extracted all rows from Table 1 for the ZINC12K dataset. The proposed model is identified
as PathNN-AP based on the context of the table listing variants (SP, SP+, AP) at the bottom, with AP
being the best performing variant and likely the primary proposed method in this context. All values
are MAE, lower is better. Standard deviations are parsed correctly. No external data usage is
indicated for these standard GNN benchmarks.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*