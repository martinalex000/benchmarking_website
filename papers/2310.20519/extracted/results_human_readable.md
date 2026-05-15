# Extraction: arXiv:2310.20519
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: GRIT 1-CQRW (0.5M params)
- Type: GNN

## Results

### CIFAR10 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5571 | 0.0038 | Yes | this paper | Table 1 |
| GIN | 0.5525 | 0.0153 | Yes | this paper | Table 1 |
| GAT | 0.6422 | 0.0046 | Yes | this paper | Table 1 |
| GatedGCN | 0.6731 | 0.0031 | Yes | this paper | Table 1 |
| DGN | 0.7284 | 0.0042 | Yes | this paper | Table 1 |
| GIN-AK+ | 0.7219 | 0.0013 | Yes | this paper | Table 1 |
| EGT | 0.6870 | 0.0041 | Yes | this paper | Table 1 |
| GPS | 0.7230 | 0.0036 | Yes | this paper | Table 1 |
| GRIT | 0.7647 | 0.0088 | Yes | ma2023graph | Table 1 |
| GRIT (our run) | 0.7620 | 0.0074 | Yes | this paper | Table 1 |
| GRIT 1-CQRW | 0.7635 | 0.0070 | No | this paper | Table 1 |
| GRIT 2-QiQRW | 0.7644 | 0.0107 | No | this paper | Table 1 |

### MNIST — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.9071 | 0.0022 | Yes | this paper | Table 1 |
| GIN | 0.9648 | 0.0025 | Yes | this paper | Table 1 |
| GAT | 0.9554 | 0.0021 | Yes | this paper | Table 1 |
| GatedGCN | 0.9734 | 0.0014 | Yes | this paper | Table 1 |
| EGT | 0.9817 | 0.0009 | Yes | this paper | Table 1 |
| GPS | 0.9805 | 0.0013 | Yes | this paper | Table 1 |
| GRIT | 0.9811 | 0.0011 | Yes | this paper | Table 1 |
| GRIT (our run) | 0.9816 | 0.0005 | Yes | this paper | Table 1 |
| GRIT 1-CQRW | 0.9811 | 0.0011 | Yes | this paper | Table 1 |
| GRIT 2-QiQRW | 0.9820 | 0.0005 | No | this paper | Table 1 |

### PATTERN — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7189 | 0.0033 | Yes | this paper | Table 1 |
| GIN | 0.8539 | 0.0014 | Yes | this paper | Table 1 |
| GAT | 0.7827 | 0.0019 | Yes | this paper | Table 1 |
| GatedGCN | 0.8557 | 0.0009 | Yes | this paper | Table 1 |
| DGN | 0.8668 | 0.0003 | Yes | ma2023graph | Table 1 |
| GIN-AK+ | 0.8685 | 0.0006 | Yes | ma2023graph | Table 1 |
| SAN | 0.8658 | 0.0004 | Yes | ma2023graph | Table 1 |
| K-Subgraph SAT | 0.8685 | 0.0004 | Yes | ma2023graph | Table 1 |
| EGT | 0.8682 | 0.0002 | Yes | ma2023graph | Table 1 |
| GPS | 0.8669 | 0.0006 | Yes | ma2023graph | Table 1 |
| GRIT | 0.8720 | 0.0008 | Yes | ma2023graph | Table 1 |
| GRIT (our run) | 0.9041 | 0.0023 | Yes | this paper | Table 1 |
| GRIT 1-CQRW | 0.8720 | 0.0004 | No | this paper | Table 1 |
| GRIT 2-QiQRW | 0.9016 | 0.0045 | Yes | this paper | Table 1 |

### PCQM4Mv2 — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.1195 | — | Yes | this paper | Table 1 |
| GCN | 0.1195 | — | Yes | this paper | Table 1 |
| Graphormer | 0.0864 | — | Yes | this paper | Table 1 |
| GPS-medium | 0.0858 | — | Yes | this paper | Table 1 |
| GRIT | 0.0859 | — | Yes | Ma 2023 | Table 1 |
| GRIT (our run) | 0.0842 | — | Yes | this paper | Table 1 |
| GRIT 1-CQRW (ours) | 0.0947 | — | No | this paper | Table 1 |
| GRIT 2-QiQRW (ours) | 0.0838 | — | No | this paper | Table 1 |

### ZINC — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3670 | 0.0110 | Yes | this paper | Table 1 |
| GIN | 0.5260 | 0.0510 | Yes | this paper | Table 1 |
| GAT | 0.3840 | 0.0070 | Yes | this paper | Table 1 |
| GatedGCN | 0.2820 | 0.0150 | Yes | this paper | Table 1 |
| DGN | 0.1680 | 0.0030 | Yes | ma2023graph | Table 1 |
| GIN-AK+ | 0.0800 | 0.0010 | Yes | ma2023graph | Table 1 |
| SAN | 0.1390 | 0.0060 | Yes | ma2023graph | Table 1 |
| K-Subgraph SAT | 0.0940 | 0.0080 | Yes | ma2023graph | Table 1 |
| EGT | 0.1080 | 0.0090 | Yes | ma2023graph | Table 1 |
| GPS | 0.0700 | 0.0040 | Yes | ma2023graph | Table 1 |
| GRIT | 0.0590 | 0.0020 | Yes | ma2023graph | Table 1 |
| GRIT (our run) | 0.0600 | 0.0020 | Yes | this paper | Table 1 |
| GRIT 1-CQRW | 0.0580 | 0.0020 | No | this paper | Table 1 |
| GRIT 2-QiQRW | 0.0590 | 0.0040 | No | this paper | Table 1 |

### ZINC-full — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.0880 | 0.0020 | Yes | this paper | Table 1 |
| GraphSAGE | 0.1260 | 0.0030 | Yes | this paper | Table 1 |
| GAT | 0.1110 | 0.0020 | Yes | this paper | Table 1 |
| GCN | 0.1130 | 0.0020 | Yes | this paper | Table 1 |
| SignNet | 0.0240 | 0.0030 | Yes | this paper | Table 1 |
| Graphormer | 0.0520 | 0.0050 | Yes | this paper | Table 1 |
| Graphormer-URPE | 0.0280 | 0.0020 | Yes | this paper | Table 1 |
| Graphormer-GD | 0.0250 | 0.0040 | Yes | this paper | Table 1 |
| GRIT | 0.0230 | 0.0010 | Yes | Ma 2023 | Table 1 |
| GRIT (our run) | 0.0250 | 0.0020 | Yes | this paper | Table 1 |
| GRIT 1-CQRW | 0.0250 | 0.0030 | Yes | this paper | Table 1 |
| GRIT 2-QiQRW | 0.0230 | 0.0020 | No | this paper | Table 1 |

## Baseline Models Identified

- **GCN** (from: this paper)
- **GIN** (from: this paper)
- **GAT** (from: this paper)
- **GatedGCN** (from: this paper)
- **DGN** (from: ma2023graph)
- **GIN-AK+** (from: ma2023graph)
- **SAN** (from: ma2023graph)
- **K-Subgraph SAT** (from: ma2023graph)
- **EGT** (from: ma2023graph)
- **GPS** (from: ma2023graph)
- **GRIT** (from: ma2023graph)
- **GRIT (our run)** (from: this paper)
- **GRIT 2-QiQRW**, 0.5M params (from: this paper)
- **GRIT 1-CQRW** (from: this paper)
- **GraphSAGE** (from: W. Hamilton et al., 2017)
- **SignNet** (from: Rampásek et al., 2022)
- **Graphormer** (from: Y. Ying et al., 2021)
- **Graphormer-URPE** (from: Y. Ying et al., 2021)
- **Graphormer-GD** (from: Y. Ying et al., 2021)
- **GPS-medium** (from: V. V. et al., 2022)
- **GRIT 1-CQRW (ours)** (from: this paper)

## Extraction Notes

[ZINC] Extracted results for the standard ZINC dataset from Table 1. Table 2 contains results for
ZINC-full, which was excluded per instructions to ignore variants/non-standard configurations. The
primary metric MAE was used. All values are normalized correctly (MAE is not a percentage). Standard
deviations were parsed from the 'mean ± std' format. [MNIST] Extracted only MNIST Accuracy results
from Table 1. Values were converted from percentages to [0,1] range. Standard deviations were parsed
from 'mean ± std' format. DGN, GIN-AK+, and SAN have no MNIST results reported in the table (marked
with '-'), so they are excluded from the results list. [CIFAR10] Extracted all rows from Table 1 for
the CIFAR10 dataset. Values are normalized from percentages to [0,1] range. Standard deviations are
parsed from the 'mean ± std' format. The proposed models are identified as 'GRIT 1-CQRW' and 'GRIT
2-QiQRW' based on the bold formatting and text description. Baselines like DGN, GIN-AK+, SAN,
K-Subgraph SAT are excluded as they have no CIFAR10 results reported in the table. [PATTERN]
Extracted only PATTERN dataset results from Table 1. Values were converted from percentages to [0,1]
range. Standard deviations were parsed from the 'mean ± std' format. All models listed in the table
for the PATTERN column were included. [CLUSTER] failed: 2 validation errors for ExtractionOutput
results.4.value   Input should be a valid number [type=float_type, input_value=None,
input_type=NoneType]     For further information visit https://errors.pydantic.dev/2.13/v/float_type
results.5.value   Input should be a valid number [type=float_type, input_value=None,
input_type=NoneType]     For further information visit https://errors.pydantic.dev/2.13/v/float_type
[ZINC-full] Extracted only ZINC-full results as requested. The table contains results for PCQM4Mv2
and small ZINC which were ignored. The proposed model is identified as 'GRIT 2-QiQRW' based on the
text 'Our methods performs the best among all others' and the bold/first-place indicator in the
table. The baseline 'GRIT' results are taken from the original paper citation, while 'GRIT (our
run)' is a reproduction by the authors of this paper. All values are MAE, lower is better.
[PCQM4Mv2] Extracted only PCQM4Mv2 results as requested. The table provides MAE values for PCQM4Mv2.
Note that for 'GRIT 1-CQRW (ours)', the value 0.0947 has an asterisk (*), which the caption explains
means 'only 55 epochs were used'. This is still a valid result for the standard configuration test
set performance, albeit with fewer epochs. Other models like GraphSAGE, GAT, SignNet, Graphormer-
URPE, and Graphormer-GD have '-' for PCQM4Mv2, so they are excluded. The proposed model is
identified as 'GRIT 2-QiQRW (ours)' which achieves the best MAE.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*