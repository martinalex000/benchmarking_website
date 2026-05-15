# Extraction: arXiv:2311.04653
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: FFGT
- Type: GraphTransformer

## Results

### Chameleon — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| SAN | 0.5562 | 0.0043 | Yes | this paper | Table 1 |
| Graphormer | 0.3681 | 0.0169 | Yes | this paper | Table 1 |
| GRPE | 0.5465 | 0.0150 | Yes | this paper | Table 1 |
| GRPE-FFGT | 0.6252 | 0.0097 | No | this paper | Table 1 |

### CiteSeer — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| SAN | 0.6963 | 0.0376 | Yes | this paper | Table 1 |
| Graphormer | 0.7330 | 0.0148 | Yes | this paper | Table 1 |
| UniMP | 0.7500 | 0.0159 | Yes | this paper | Table 1 |
| NAGphormer | 0.7369 | 0.0148 | Yes | this paper | Table 1 |
| GRPE | 0.7259 | 0.0140 | Yes | this paper | Table 1 |
| GRPE-FFGT | 0.7531 | 0.0132 | No | this paper | Table 1 |

### Cora — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| SAN | 0.8191 | 0.0342 | Yes | this paper | Table 1 |
| Graphormer | 0.6771 | 0.0078 | Yes | this paper | Table 1 |
| UniMP | 0.8418 | 0.0139 | Yes | this paper | Table 1 |
| NAGphormer | 0.8577 | 0.0135 | Yes | this paper | Table 1 |
| GRPE | 0.8252 | 0.0130 | Yes | this paper | Table 1 |
| GRPE-FFGT | 0.8659 | 0.0083 | No | this paper | Table 1 |

### Peptide-Func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| VANILLA | 0.6648 | 0.0087 | Yes | this paper | Table 1 |
| VANILLA-FFGT | 0.6914 | 0.0040 | Yes | this paper | Table 1 |
| GRPE | 0.6836 | 0.0060 | Yes | this paper | Table 1 |
| GRPE-FFGT | 0.6956 | 0.0080 | No | this paper | Table 1 |
| GCN | 0.5930 | 0.0023 | Yes | this paper | Table 2 |
| GatedGCN | 0.5864 | 0.0077 | Yes | this paper | Table 2 |
| SUN | 0.6730 | 0.0078 | Yes | this paper | Table 2 |
| SAN + LapPE | 0.6384 | 0.0121 | Yes | this paper | Table 2 |
| GPS | 0.6535 | 0.0041 | Yes | this paper | Table 2 |
| Exphormer | 0.6527 | 0.0043 | Yes | this paper | Table 2 |
| MGT | 0.6817 | 0.0064 | Yes | this paper | Table 2 |
| Graph ViT | 0.6942 | 0.0075 | Yes | this paper | Table 2 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| VANILLA | 0.2500 | 0.0027 | Yes | this paper | Table 1 |
| VANILLA-FFGT | 0.2456 | 0.0017 | Yes | this paper | Table 1 |
| GRPE | 0.2436 | 0.0018 | Yes | this paper | Table 1 |
| GRPE-FFGT | 0.2416 | 0.0026 | No | this paper | Table 1 |
| GCN | 0.3234 | 0.0006 | Yes | this paper | Table 2 |
| GatedGCN | 0.3420 | 0.0013 | Yes | this paper | Table 2 |
| SUN | 0.2498 | 0.0008 | Yes | this paper | Table 2 |
| SAN + LapPE | 0.2683 | 0.0042 | Yes | this paper | Table 2 |
| GPS | 0.2500 | 0.0012 | Yes | this paper | Table 2 |
| Exphormer | 0.2481 | 0.0007 | Yes | this paper | Table 2 |
| MGT | 0.2453 | 0.0025 | Yes | this paper | Table 2 |
| Graph ViT | 0.2449 | 0.0016 | Yes | this paper | Table 2 |

### SBM-PATTERN — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Vanilla | 0.8736 | 0.0007 | Yes | this paper | Table 1 |
| FFGT (FL=1) | 0.8761 | 0.0010 | No | this paper | Table 1 |
| FFGT (FL=2) | 0.8747 | 0.0008 | No | this paper | Table 1 |
| FFGT (FL=3) | 0.8744 | 0.0007 | No | this paper | Table 1 |

### ZINC — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3670 | 0.0110 | Yes | this paper | Table 2 |
| GatedGCN | 0.2260 | 0.0140 | Yes | this paper | Table 2 |
| SUN | 0.0840 | 0.0020 | Yes | this paper | Table 2 |
| SAN + LapPE | 0.1390 | 0.0060 | Yes | this paper | Table 2 |
| GraphGPS | 0.0700 | 0.0040 | Yes | this paper | Table 2 |
| MGT | 0.1310 | 0.0030 | Yes | this paper | Table 2 |
| Graph ViT | 0.0850 | 0.0050 | Yes | this paper | Table 2 |
| VANILLA-FFGT | 0.1400 | 0.0050 | No | this paper | Table 2 |
| GRPE-FFGT | 0.0930 | 0.0040 | No | this paper | Table 2 |

### ogbg-molpcba — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.2424 | 0.0034 | Yes | this paper | Table 2 |
| GatedGCN | 0.2670 | 0.0020 | Yes | this paper | Table 2 |
| SAN + LapPE | 0.2765 | 0.0042 | Yes | this paper | Table 2 |
| GraphGPS | 0.2907 | 0.0028 | Yes | this paper | Table 2 |
| VANILLA-FFGT | 0.2779 | 0.0049 | Yes | this paper | Table 2 |
| GRPE-FFGT | 0.2902 | 0.0010 | No | this paper | Table 2 |

## Baseline Models Identified

- **GCN** (from: Kipf 2016)
- **GatedGCN** (from: Bresson 2017)
- **SUN** (from: Frasca 2022)
- **SAN + LapPE** (from: Kreuzer 2021)
- **GraphGPS** (from: Rampásek 2022)
- **Exphormer** (from: Shirzad 2023)
- **MGT** (from: Ngo 2023)
- **Graph ViT** (from: He 2023)
- **SAN** (from: Kreuzer 2021)
- **VANILLA**
- **VANILLA-FFGT**
- **GRPE**
- **GPS** (from: this paper)
- **Graphormer** (from: Graphormer)
- **UniMP** (from: UniMP)
- **NAGphormer** (from: NAGphormer)

## Extraction Notes

[ZINC] Extracted ZINC MAE results from Table 2 (Table comp). Note: Table 1 contains ablation results
for 'VANILLA' and 'VANILLA-FFGT' and 'GRPE' and 'GRPE-FFGT' which are variants of the proposed
method but Table 2 contains the main comparison against SOTA baselines. The values in Table 2 for
VANILLA-FFGT and GRPE-FFGT match Table 1. I have included all models from Table 2 as they represent
the full benchmark comparison. Excluded Exphormer as it has no ZINC result ('-'). [ogbg-molpcba]
Extracted results for 'ogbg-molpcba' from Table 2 (labeled table.comp). Note that Table 1
(table.FFGT) contains ablation results for the proposed method's backbone variants (VANILLA, GRPE)
which are also included as baselines in Table 2. The primary metric AP was used. Values are
normalized to [0,1]. Missing values in Table 2 for some baselines (SUN, Exphormer, MGT, Graph ViT)
were skipped as per instructions to extract reported results. [Peptides-func] Extracted AP results
for Peptide-Func from Table 1 and Table 2. Note that Table 1 and Table 2 report identical values for
the proposed model (GRPE-FFGT) and its variant (VANILLA-FFGT), as well as GRPE. Table 2 includes
additional baselines. All values are normalized to [0,1]. Standard deviations are parsed from the ±
notation. [Peptides-struct] Extracted all rows for Peptides-struct from Table 1 and Table 2. Note
that Table 1 and Table 2 contain overlapping models (VANILLA-FFGT and GRPE-FFGT appear in both). I
have included all occurrences as they are distinct entries in the provided text tables. The metric
is MAE (lower is better). Values were normalized to [0,1] range implicitly as they are already small
floats representing MAE. No percentage conversion needed. [Cora] Extracted only Cora results as
requested. The table reports Accuracy in percentage (%), so values were divided by 100 to fit the
[0, 1] range. The proposed model is identified as GRPE-FFGT based on the caption and bolding.
Baselines are taken from the table rows. The row '$\Delta$ Acc-FFGT' represents improvement delta
and was skipped as it is not a model performance result. [CiteSeer] Extracted only CiteSeer results
from Table 1. Values were percentages in the table (e.g., 75.31), converted to [0,1] range (0.7531)
as per rules for Accuracy. Standard deviations were parsed from '±' notation. All rows present in
the table for CiteSeer were included. [Chameleon] Extracted only Chameleon results as requested.
Values were percentages in the table (e.g., 55.62) and were divided by 100 to fit the [0,1] range
for Accuracy. Standard deviations were parsed from the ± notation. UniMP and NAGphormer had missing
values ('-') and were excluded from the results list. [SBM-PATTERN] The table presents results for
SBM-PATTERN with varying p values (0.16, 0.14, 0.12, 0.10). The FOCUS instruction asks for the
STANDARD/DEFAULT configuration. In SBM-PATTERN benchmarks, p=0.16 is typically the standard/hard
setting, but the table does not explicitly label one as 'default'. However, since the prompt asks to
extract results for the dataset and the table contains multiple configurations, I have extracted the
results for the first column (p=0.16) as it is the most common standard setting and often the
primary focus. If 'standard' implies averaging or a specific other setting, it is not explicitly
defined in the text. I will assume p=0.16 is the intended standard configuration for extraction
purposes as it is the first and often hardest/most standard variant in SBM literature. Note: The
table caption says 'different sbm-pattern datasets', implying each p is a variant. I extracted the
p=0.16 column as the primary representative. If the user meant all columns, the JSON would be much
larger. Given 'STANDARD / DEFAULT', p=0.16 is the safest bet for SBM-PATTERN.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*