# Extraction: arXiv:2405.13806
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: M (ours)
- Type: GNN

## Results

### Amazon-Computers — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.8965 | 0.0052 | Yes | this paper | Table 1 |
| GAT | 0.9078 | 0.0013 | Yes | this paper | Table 1 |
| APPNP | 0.9018 | 0.0017 | Yes | this paper | Table 1 |
| Scattering | 0.8568 | 0.0071 | Yes | this paper | Table 1 |
| Scattering GCN | 0.8883 | 0.0044 | Yes | this paper | Table 1 |
| SGWT | 0.8519 | 0.0059 | Yes | this paper | Table 1 |
| GWNN | 0.9075 | 0.0059 | Yes | this paper | Table 1 |
| UFGConvS | 0.8868 | 0.0039 | Yes | this paper | Table 1 |
| UFGConvR | 0.8929 | 0.0046 | Yes | this paper | Table 1 |
| WaveShrink-ChebNet | 0.8820 | 0.0065 | Yes | this paper | Table 1 |
| DEFT | 0.9163 | 0.0052 | Yes | this paper | Table 1 |
| WaveNet | 0.9206 | 0.0033 | Yes | this paper | Table 1 |
| SEA-GWNN | 0.8988 | 0.0064 | Yes | this paper | Table 1 |
| M (ours) | 0.9226 | 0.0018 | No | this paper | Table 1 |

### Amazon-Photo — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.9270 | 0.0020 | Yes | this paper | Table 1 |
| GAT | 0.9387 | 0.0011 | Yes | this paper | Table 1 |
| APPNP | 0.9432 | 0.0014 | Yes | this paper | Table 1 |
| Scattering | 0.9210 | 0.0061 | Yes | this paper | Table 1 |
| Scattering GCN | 0.9307 | 0.0042 | Yes | this paper | Table 1 |
| SGWT | 0.9245 | 0.0062 | Yes | this paper | Table 1 |
| GWNN | 0.9445 | 0.0045 | Yes | this paper | Table 1 |
| UFGConvS | 0.9398 | 0.0059 | Yes | this paper | Table 1 |
| UFGConvR | 0.9434 | 0.0034 | Yes | this paper | Table 1 |
| WaveShrink-ChebNet | 0.9354 | 0.0090 | Yes | this paper | Table 1 |
| DEFT | 0.9435 | 0.0044 | Yes | this paper | Table 1 |
| WaveNet | 0.9409 | 0.0063 | Yes | this paper | Table 1 |
| SEA-GWNN | 0.9435 | 0.0050 | Yes | this paper | Table 1 |
| M (ours) | 0.9537 | 0.0044 | No | this paper | Table 1 |

### COCO-SP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.0841 | 0.0010 | Yes | this paper | Table 1 |
| GINE | 0.1339 | 0.0044 | Yes | this paper | Table 1 |
| GatedGCN | 0.2641 | 0.0045 | Yes | this paper | Table 1 |
| Scattering | 0.1644 | 0.0079 | Yes | this paper | Table 1 |
| Scattering GCN | 0.3027 | 0.0060 | Yes | this paper | Table 1 |
| SGWT | 0.3297 | 0.0053 | Yes | this paper | Table 1 |
| GWNN | 0.1339 | 0.0044 | Yes | this paper | Table 1 |
| UFGConvS | 0.2315 | 0.0055 | Yes | this paper | Table 1 |
| UFGConvR | 0.2602 | 0.0048 | Yes | this paper | Table 1 |
| WaveShrink-ChebNet | 0.1112 | 0.0046 | Yes | this paper | Table 1 |
| DEFT | 0.3014 | 0.0049 | Yes | this paper | Table 1 |
| WaveNet | 0.2306 | 0.0018 | Yes | this paper | Table 1 |
| SEA-GWNN | 0.2433 | 0.0023 | Yes | this paper | Table 1 |
| M | 0.3596 | 0.0022 | No | this paper | Table 1 |

### Coauthor-CS — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.9292 | 0.0012 | Yes | this paper | Table 1 |
| GAT | 0.9361 | 0.0014 | Yes | this paper | Table 1 |
| APPNP | 0.9449 | 0.0007 | Yes | this paper | Table 1 |
| Scattering | 0.9477 | 0.0033 | Yes | this paper | Table 1 |
| Scattering GCN | 0.9518 | 0.0030 | Yes | this paper | Table 1 |
| SGWT | 0.9481 | 0.0023 | Yes | this paper | Table 1 |
| GWNN | 0.9075 | 0.0059 | Yes | this paper | Table 1 |
| UFGConvS | 0.9533 | 0.0027 | Yes | this paper | Table 1 |
| UFGConvR | 0.9546 | 0.0033 | Yes | this paper | Table 1 |
| WaveShrink-ChebNet | 0.9490 | 0.0030 | Yes | this paper | Table 1 |
| DEFT | 0.9504 | 0.0032 | Yes | this paper | Table 1 |
| WaveNet | 0.9491 | 0.0029 | Yes | this paper | Table 1 |
| SEA-GWNN | 0.9511 | 0.0037 | Yes | this paper | Table 1 |
| M (ours) | 0.9589 | 0.0034 | No | this paper | Table 1 |

### CoraFull — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.6176 | 0.0014 | Yes | this paper | Table 1 |
| GAT | 0.6447 | 0.0018 | Yes | this paper | Table 1 |
| APPNP | 0.6516 | 0.0028 | Yes | this paper | Table 1 |
| Scattering | 0.5765 | 0.0084 | Yes | this paper | Table 1 |
| Scattering GCN | 0.6114 | 0.0113 | Yes | this paper | Table 1 |
| SGWT | 0.5504 | 0.0112 | Yes | this paper | Table 1 |
| GWNN | 0.6419 | 0.0079 | Yes | this paper | Table 1 |
| UFGConvS | 0.6125 | 0.0093 | Yes | this paper | Table 1 |
| UFGConvR | 0.6243 | 0.0080 | Yes | this paper | Table 1 |
| WaveShrink-ChebNet | 0.5898 | 0.0069 | Yes | this paper | Table 1 |
| DEFT | 0.6801 | 0.0086 | Yes | this paper | Table 1 |
| WaveNet | 0.5765 | 0.0105 | Yes | this paper | Table 1 |
| SEA-GWNN | 0.6674 | 0.0079 | Yes | this paper | Table 1 |
| M (ours) | 0.6914 | 0.0078 | No | this paper | Table 1 |

### PCQM-Contact — MRR ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3234 | 0.0006 | Yes | this paper | Table 1 |
| GINE | 0.3180 | 0.0027 | Yes | this paper | Table 1 |
| GatedGCN | 0.3218 | 0.0011 | Yes | this paper | Table 1 |
| Scattering | 0.3390 | 0.0027 | Yes | this paper | Table 1 |
| Scattering GCN | 0.3373 | 0.0045 | Yes | this paper | Table 1 |
| SGWT | 0.3404 | 0.0005 | Yes | this paper | Table 1 |
| GWNN | 0.3272 | 0.0008 | Yes | this paper | Table 1 |
| UFGConvS | 0.3394 | 0.0024 | Yes | this paper | Table 1 |
| UFGConvR | 0.3408 | 0.0020 | Yes | this paper | Table 1 |
| WaveShrink-ChebNet | 0.3256 | 0.0011 | Yes | this paper | Table 1 |
| DEFT | 0.3425 | 0.0006 | Yes | this paper | Table 1 |
| WaveNet | 0.3319 | 0.0020 | Yes | this paper | Table 1 |
| SEA-GWNN | 0.2989 | 0.0026 | Yes | this paper | Table 1 |
| M | 0.3450 | 0.0002 | No | this paper | Table 1 |

### PascalVOC-SP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.1268 | 0.0060 | Yes | this paper | Table 1 |
| GINE | 0.1265 | 0.0076 | Yes | this paper | Table 1 |
| GatedGCN | 0.2873 | 0.0219 | Yes | this paper | Table 1 |
| Scattering | 0.1658 | 0.0049 | Yes | this paper | Table 1 |
| Scattering GCN | 0.3045 | 0.0036 | Yes | this paper | Table 1 |
| SGWT | 0.3122 | 0.0056 | Yes | this paper | Table 1 |
| GWNN | 0.2560 | 0.0056 | Yes | this paper | Table 1 |
| UFGConvS | 0.3127 | 0.0039 | Yes | this paper | Table 1 |
| UFGConvR | 0.3108 | 0.0033 | Yes | this paper | Table 1 |
| WaveShrink-ChebNet | 0.1880 | 0.0085 | Yes | this paper | Table 1 |
| DEFT | 0.3598 | 0.0020 | Yes | this paper | Table 1 |
| WaveNet | 0.2860 | 0.0015 | Yes | this paper | Table 1 |
| SEA-GWNN | 0.3197 | 0.0055 | Yes | this paper | Table 1 |
| M | 0.4163 | 0.0019 | No | this paper | Table 1 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5930 | 0.0023 | Yes | this paper | Table 1 |
| GINE | 0.5498 | 0.0079 | Yes | this paper | Table 1 |
| GatedGCN | 0.5864 | 0.0077 | Yes | this paper | Table 1 |
| Scattering | 0.5680 | 0.0038 | Yes | this paper | Table 1 |
| Scattering GCN | 0.6287 | 0.0064 | Yes | this paper | Table 1 |
| SGWT | 0.6023 | 0.0027 | Yes | this paper | Table 1 |
| GWNN | 0.6547 | 0.0048 | Yes | this paper | Table 1 |
| UFGConvS | 0.6583 | 0.0075 | Yes | this paper | Table 1 |
| UFGConvR | 0.6529 | 0.0082 | Yes | this paper | Table 1 |
| WaveShrink-ChebNet | 0.6112 | 0.0053 | Yes | this paper | Table 1 |
| DEFT | 0.6695 | 0.0063 | Yes | this paper | Table 1 |
| WaveNet | 0.6463 | 0.0027 | Yes | this paper | Table 1 |
| SEA-GWNN | 0.6875 | 0.0020 | Yes | this paper | Table 1 |
| M | 0.6973 | 0.0043 | No | this paper | Table 1 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 34.9600 | 0.1300 | Yes | this paper | Table 1 |
| GINE | 35.4700 | 0.4500 | Yes | this paper | Table 1 |
| GatedGCN | 34.2000 | 0.1300 | Yes | this paper | Table 1 |
| Scattering | 26.7700 | 0.1100 | Yes | this paper | Table 1 |
| Scattering GCN | 26.4300 | 0.2000 | Yes | this paper | Table 1 |
| SGWT | 25.3900 | 0.2100 | Yes | this paper | Table 1 |
| GWNN | 27.3400 | 0.0400 | Yes | this paper | Table 1 |
| UFGConvS | 27.0800 | 0.5800 | Yes | this paper | Table 1 |
| UFGConvR | 27.5000 | 0.2100 | Yes | this paper | Table 1 |
| WaveShrink-ChebNet | 27.4500 | 0.0600 | Yes | this paper | Table 1 |
| DEFT | 25.0600 | 0.1300 | Yes | this paper | Table 1 |
| WaveNet | 25.8800 | 0.0100 | Yes | this paper | Table 1 |
| SEA-GWNN | 25.6400 | 0.3100 | Yes | this paper | Table 1 |
| M (ours) | 24.8300 | 0.1100 | No | this paper | Table 1 |

### ogbn-arxiv — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7174 | 0.0029 | Yes | this paper | Table 1 |
| GAT | 0.7182 | 0.0023 | Yes | this paper | Table 1 |
| APPNP | 0.7190 | 0.0025 | Yes | this paper | Table 1 |
| Scattering | 0.6623 | 0.0019 | Yes | this paper | Table 1 |
| Scattering GCN | 0.7118 | 0.0076 | Yes | this paper | Table 1 |
| SGWT | 0.6908 | 0.0030 | Yes | this paper | Table 1 |
| GWNN | 0.7113 | 0.0047 | Yes | this paper | Table 1 |
| UFGConvS | 0.7004 | 0.0022 | Yes | this paper | Table 1 |
| UFGConvR | 0.7197 | 0.0012 | Yes | this paper | Table 1 |
| DEFT | 0.7201 | 0.0020 | Yes | this paper | Table 1 |
| WaveNet | 0.7137 | 0.0014 | Yes | this paper | Table 1 |
| SEA-GWNN | 0.7264 | 0.0021 | Yes | this paper | Table 1 |
| WaveGC | 0.7301 | 0.0018 | No | this paper | Table 1 |

## Baseline Models Identified

- **GCN** (from: Kipf & Welling 2017)
- **GAT** (from: Veličković et al. 2018)
- **APPNP** (from: Klicpera et al. 2019)
- **Scattering** (from: Cohen et al. 2019)
- **Scattering GCN** (from: Cohen et al. 2019)
- **SGWT** (from: De Brouwer et al. 2019)
- **GWNN** (from: De Brouwer et al. 2019)
- **UFGConvS** (from: De Brouwer et al. 2019)
- **UFGConvR** (from: De Brouwer et al. 2019)
- **WaveShrink-ChebNet** (from: De Brouwer et al. 2019)
- **DEFT** (from: De Brouwer et al. 2019)
- **WaveNet** (from: De Brouwer et al. 2019)
- **SEA-GWNN** (from: De Brouwer et al. 2019)
- **GINE** (from: Xu et al.)
- **GatedGCN** (from: Bresson & Laurent)

## Extraction Notes

[Coauthor-CS] Extracted only Coauthor-CS (labeled as 'CS' in the table) results. All values are
Accuracy. Standard deviations were parsed from the ± notation. Values were normalized to [0,1]
range. [Amazon-Photo] Extracted results for 'Photo' column from Table 1, which corresponds to the
Amazon-Photo dataset in the LRGB benchmark. All values are normalized to [0,1] range. Standard
deviations were parsed from the ± notation. [Amazon-Computers] Extracted only the 'Computer' column
from Table 1, which corresponds to the Amazon-Computers dataset in the LRGB benchmark. The table
header uses 'Computer' but the context of other datasets (CS, Photo, CoraFull, ogbn-arxiv) confirms
this is Amazon-Computers. All values are normalized to [0,1]. Standard deviations are parsed from
the ± notation. The proposed model is identified as 'M (ours)' based on the bold formatting and
caption. [CoraFull] Extracted only CoraFull results from Table 1. All values are Accuracy. Standard
deviations were parsed from the ± notation. Values were divided by 100 to fit [0,1] range as per
instructions for Accuracy metrics. [ogbn-arxiv] Extracted only the 'ogbn-arxiv' column from Table 1
as requested. All values are Accuracy scores normalized to [0,1]. Standard deviations were parsed
from the 'mean ± std' format. The proposed model name 'WaveGC' was inferred from the text
description ('The main complexity of WaveGC...') and the placeholder '\M' in the table. [PascalVOC-
SP] Extracted only PascalVOC-SP (VOC) F1 scores from Table 1. All values were percentages in the
table (e.g., 12.68) and were divided by 100 to fit the [0,1] range as per instructions. Standard
deviations were parsed from the ± notation. [PCQM-Contact] Extracted MRR results for PCQM-Contact
from Table 1. All values were converted from percentages (e.g., 32.34) to decimals (0.3234) as per
standard MRR reporting in LRGB benchmarks. Standard deviations were parsed from the '±' notation.
The proposed model is referred to as 'M' in the table. [COCO-SP] Extracted F1 scores for COCO-SP
from Table 1. Values were converted from percentages (e.g., 08.41) to decimals (0.0841) as per
standard benchmark reporting conventions for F1/Accuracy metrics. All results are test-set results
as implied by the table caption 'Qualified results... compared to baselines' and standard LRGB
reporting practices. [Peptides-func] Extracted only Peptides-func (Pf) results from Table 1. Values
were converted from percentages (e.g., 59.30) to decimals (0.5930) as per standard AP metric
reporting in this context. Standard deviations were parsed from the ± notation. [Peptides-struct]
Extracted only the 'Ps' (Peptides-struct) column from Table 1. The primary metric is MAE (lower is
better). Values are reported as mean ± std. The proposed model 'M' achieves the best result. Other
tables (Table 2, 3, 4) contain ablation or sensitivity analysis results for Ps, but Table 1 contains
the main benchmark comparison against baselines which is the primary focus for 'results'. The values
in Table 1 are consistent with the best values in the ablation tables.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*