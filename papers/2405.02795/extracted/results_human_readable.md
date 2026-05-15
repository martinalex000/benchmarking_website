# Extraction: arXiv:2405.02795
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: PST (1.0M params)
- Type: GNN

## Results

### PascalVOC-SP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.1268 | 0.0060 | Yes | this paper | Table 1 |
| GINE | 0.1265 | 0.0076 | Yes | this paper | Table 1 |
| GatedGCN | 0.2873 | 0.0219 | Yes | this paper | Table 1 |
| GatedGCN* | 0.2860 | 0.0085 | Yes | this paper | Table 1 |
| Transformer** | 0.2694 | 0.0098 | Yes | this paper | Table 1 |
| SAN* | 0.3216 | 0.0027 | Yes | this paper | Table 1 |
| SAN** | 0.3230 | 0.0039 | Yes | this paper | Table 1 |
| GraphGPS | 0.3748 | 0.0109 | Yes | this paper | Table 1 |
| Exphormer | 0.3975 | 0.0037 | Yes | this paper | Table 1 |
| PSDS | 0.2134 | 0.0050 | Yes | this paper | Table 1 |
| PST | 0.4010 | 0.0072 | No | this paper | Table 1 |

### Peptides-Func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5930 | 0.0023 | Yes | this paper | Table 1 |
| GINE | 0.5498 | 0.0079 | Yes | this paper | Table 1 |
| GatedGCN | 0.5864 | 0.0077 | Yes | this paper | Table 1 |
| GatedGCN* | 0.6069 | 0.0035 | Yes | this paper | Table 1 |
| Transformer** | 0.6326 | 0.0126 | Yes | this paper | Table 1 |
| SAN* | 0.6439 | 0.0075 | Yes | this paper | Table 1 |
| SAN** | 0.6384 | 0.0121 | Yes | this paper | Table 1 |
| GraphGPS | 0.6535 | 0.0041 | Yes | this paper | Table 1 |
| Exphormer | 0.6527 | 0.0043 | Yes | this paper | Table 1 |
| GMLP-Mixer | 0.6970 | 0.0080 | Yes | this paper | Table 1 |
| Graph ViT | 0.6942 | 0.0075 | Yes | this paper | Table 1 |
| Grit | 0.6988 | 0.0082 | Yes | this paper | Table 1 |
| PSDS | 0.5965 | 0.0064 | Yes | this paper | Table 1 |
| PST | 0.6984 | 0.0051 | No | this paper | Table 1 |
| Graph-MLPMixer | 0.6970 | 0.0080 | Yes | this paper | Table 2 |
| PST-onelayer | 0.6517 | 0.0076 | Yes | this paper | Table 3 |
| PST-gc | 0.6439 | 0.0342 | Yes | this paper | Table 3 |

### Peptides-Struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3496 | 0.0013 | Yes | this paper | Table 1 |
| GINE | 0.3547 | 0.0045 | Yes | this paper | Table 1 |
| GatedGCN | 0.3420 | 0.0013 | Yes | this paper | Table 1 |
| GatedGCN* | 0.3357 | 0.0006 | Yes | this paper | Table 1 |
| Transformer** | 0.2529 | 0.0016 | Yes | this paper | Table 1 |
| SAN* | 0.2545 | 0.0012 | Yes | this paper | Table 1 |
| SAN** | 0.2683 | 0.0043 | Yes | this paper | Table 1 |
| GraphGPS | 0.2500 | 0.0005 | Yes | this paper | Table 1 |
| Exphormer | 0.2481 | 0.0007 | Yes | this paper | Table 1 |
| GMLP-Mixer | 0.2475 | 0.0015 | Yes | this paper | Table 1 |
| Graph ViT | 0.2449 | 0.0016 | Yes | this paper | Table 1 |
| Grit | 0.2460 | 0.0012 | Yes | this paper | Table 1 |
| PSDS | 0.2621 | 0.0036 | Yes | this paper | Table 1 |
| PST | 0.2470 | 0.0015 | No | this paper | Table 1 |
| PST-onelayer | 0.2634 | 0.0019 | Yes | this paper | Table 3 |
| PST-gc | 0.2564 | 0.0120 | Yes | this paper | Table 3 |

### QM9 — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| LRP | 3.6400 | — | Yes | this paper | Table 1 |
| NGNN | 4.2800 | — | Yes | this paper | Table 1 |
| I2GNN | 4.2800 | — | Yes | this paper | Table 1 |
| DF | 3.4600 | — | Yes | this paper | Table 1 |
| PSDS | 3.5300 | 0.0500 | Yes | this paper | Table 1 |
| PST | 3.1900 | 0.0400 | No | this paper | Table 1 |
| 1GNN* | 4.9300 | — | Yes | this paper | Table 1 |
| DTNN* | 2.4400 | — | Yes | this paper | Table 1 |
| 123* | 4.7600 | — | Yes | this paper | Table 1 |
| PPGN* | 2.3100 | — | Yes | this paper | Table 1 |
| PST* | 0.2300 | 0.0100 | No | this paper | Table 1 |

### ZINC — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.1630 | 0.0040 | Yes | this paper | Table 1 |
| GNN-AK+ | 0.0800 | 0.0010 | Yes | this paper | Table 1 |
| ESAN | 0.1020 | 0.0030 | Yes | this paper | Table 1 |
| SUN | 0.0830 | 0.0030 | Yes | this paper | Table 1 |
| SSWL | 0.0830 | 0.0030 | Yes | this paper | Table 1 |
| DRFWL | 0.0770 | 0.0020 | Yes | this paper | Table 1 |
| CIN | 0.0790 | 0.0060 | Yes | this paper | Table 1 |
| NGNN | 0.1110 | 0.0030 | Yes | this paper | Table 1 |
| Graphormer | 0.1220 | 0.0060 | Yes | this paper | Table 1 |
| GPS | 0.0700 | 0.0040 | Yes | this paper | Table 1 |
| GMLP-Mixer | 0.0770 | 0.0030 | Yes | this paper | Table 1 |
| SAN | 0.1390 | 0.0060 | Yes | this paper | Table 1 |
| Specformer | 0.0660 | 0.0030 | Yes | this paper | Table 1 |
| SignNet | 0.0840 | 0.0060 | Yes | this paper | Table 1 |
| Grit | 0.0590 | 0.0020 | Yes | this paper | Table 1 |
| PSDS | 0.1620 | 0.0070 | Yes | this paper | Table 1 |
| PST | 0.0630 | 0.0030 | No | this paper | Table 1 |

### ZINC-full — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.0880 | 0.0020 | Yes | this paper | Table 1 |
| ESAN | 0.0290 | 0.0030 | Yes | this paper | Table 1 |
| SUN | 0.0240 | 0.0030 | Yes | this paper | Table 1 |
| SSWL | 0.0220 | 0.0020 | Yes | this paper | Table 1 |
| DRFWL | 0.0250 | 0.0030 | Yes | this paper | Table 1 |
| CIN | 0.0220 | 0.0020 | Yes | this paper | Table 1 |
| NGNN | 0.0290 | 0.0010 | Yes | this paper | Table 1 |
| Graphormer | 0.0520 | 0.0050 | Yes | this paper | Table 1 |
| SignNet | 0.0240 | 0.0030 | Yes | this paper | Table 1 |
| Grit | 0.0240 | 0.0030 | Yes | this paper | Table 1 |
| PSDS | 0.0490 | 0.0020 | Yes | this paper | Table 1 |
| PST | 0.0180 | 0.0010 | No | this paper | Table 1 |

### ogbg-molhiv — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.7707 | 0.0149 | Yes | this paper | Table 1 |
| GNN-AK+ | 0.7961 | 0.0119 | Yes | this paper | Table 1 |
| ESAN | 0.7825 | 0.0098 | Yes | this paper | Table 1 |
| SUN | 0.8003 | 0.0055 | Yes | this paper | Table 1 |
| SSWL | 0.7958 | 0.0035 | Yes | this paper | Table 1 |
| DRFWL | 0.7818 | 0.0219 | Yes | this paper | Table 1 |
| CIN | 0.8094 | 0.0057 | Yes | this paper | Table 1 |
| NGNN | 0.7834 | 0.0186 | Yes | this paper | Table 1 |
| Graphormer | 0.8051 | 0.0053 | Yes | this paper | Table 1 |
| GPS | 0.7880 | 0.0101 | Yes | this paper | Table 1 |
| GMLP-Mixer | 0.7997 | 0.0102 | Yes | this paper | Table 1 |
| SAN | 0.7775 | 0.0061 | Yes | this paper | Table 1 |
| Specformer | 0.7889 | 0.0124 | Yes | this paper | Table 1 |
| PSDS | 0.7492 | 0.0118 | Yes | this paper | Table 1 |
| PST | 0.8032 | 0.0071 | No | this paper | Table 1 |

## Baseline Models Identified

- **LRP** (from: CountSubg)
- **NGNN**
- **I2GNN**
- **DF** (from: DRFWL)
- **PSDS**
- **1GNN***
- **DTNN***
- **123*** (from: kWL)
- **PPGN***
- **PST***
- **GIN**, 0.5M params (from: Corominas-Murtra et al. / standard GIN)
- **GNN-AK+**, 0.5M params (from: null)
- **ESAN**, 0.5M params (from: null)
- **SUN**, 0.5M params (from: null)
- **SSWL**, 0.5M params (from: null)
- **DRFWL**, 0.5M params (from: null)
- **CIN**, 0.5M params (from: null)
- **Graphormer**, 47.0M params (from: GT-graphormer)
- **GPS**, 0.5M params (from: null)
- **GMLP-Mixer**, 0.5M params (from: null)
- **SAN**, 0.5M params (from: null)
- **Specformer**, 0.5M params (from: null)
- **SignNet**, 0.5M params (from: null)
- **Grit**, 0.5M params (from: null)
- **GCN**, 0.5M params (from: GCN)
- **GINE**, 0.5M params (from: GIN)
- **GatedGCN**, 0.5M params (from: GatedGCN)
- **GatedGCN***, 0.5M params (from: GatedGCN)
- **Transformer****, 0.5M params
- **SAN***, 0.5M params (from: GT-SAN)
- **SAN****, 0.5M params (from: GT-SAN)
- **GraphGPS**, 0.5M params
- **Exphormer**, 0.5M params
- **Graph ViT**, 0.5M params (from: GraphVit)
- **Graph-MLPMixer**
- **PST-onelayer**
- **PST-gc**

## Extraction Notes

[QM9] The table reports MAE for 12 different target properties of QM9. The values in the table are
raw numbers (e.g., 3.64 for mu). The 'Unit' column indicates scaling factors (e.g., 10^-1 D for mu).
The prompt asks for 'MAE' as the primary metric. Since the table caption says 'MAE' and lists these
values, I have extracted the raw values as presented in the table cells. Note that PST* has
significantly lower values (e.g., 0.23 vs 3.19 for PST) which suggests it might be using a different
unit or normalization, or it is a different variant. However, the table lists them side-by-side.
PST* is likely the model using 3D coordinates/features as input (denoted by *), while PST does not.
The prompt asks for standard/default configuration. PST is the main proposed model without the
asterisk. PST* is also proposed but with external features. I included both as they are distinct
rows. The values for PST* are much smaller, possibly indicating a different scale or error metric
interpretation, but I extracted them exactly as written. Wait, looking closely at PST* values: 0.23
for mu. PST is 3.19. The unit for mu is 10^-1 D. 3.19 * 0.1 = 0.319. 0.23 is still different. It's
possible PST* uses a different loss or normalization. I will extract the values exactly as they
appear in the table cells. [ZINC] Extracted only ZINC dataset results as requested. The table also
contains ZINC-full and MolHiv results which were ignored. All values are MAE (lower is better). The
proposed model is PST. Baselines include GIN, GNN-AK+, ESAN, SUN, SSWL, DRFWL, CIN, NGNN,
Graphormer, GPS, GMLP-Mixer, SAN, Specformer, SignNet, Grit, and PSDS. Parameter counts for
baselines are inferred from the text stating 'ZINC... have 500k parameter budgets' and 'Our PST
follows these budgets', except Graphormer which is explicitly stated as 47000k. Since specific param
counts for other baselines aren't explicitly broken out in the table, I used the budget constraint
mentioned in the text for the standard configuration. [ZINC-full] Extracted only ZINC-full results
as requested. GNN-AK+, GPS, GMLP-Mixer, SAN, and Specformer have no reported results for ZINC-full
in the table (marked with '-' or '–'), so they are excluded from the results list. The proposed
model PST achieves the best MAE. All values are normalized correctly (MAE is not a percentage).
Parameter count is inferred from the text stating '500k parameter budgets' for ZINC-full. [ogbg-
molhiv] Extracted all rows from Table 1 for the 'molhiv' column. The metric is labeled 'AUC' in the
table header, which corresponds to ROC-AUC for the ogbg-molhiv benchmark. Values were converted from
percentages (e.g., 77.07) to decimals (0.7707). Standard deviations were parsed from the format
'value_std'. SignNet and Grit do not have results for molhiv in this table, so they are excluded.
[PascalVOC-SP] Extracted only PascalVOC-SP F1 results from Table 1. Excluded GMLP-Mixer, Graph ViT,
and Grit as they have no reported value ('-') for PascalVOC-SP. Excluded Table 2 as it contains
ablation variants of the proposed model, not distinct baselines or the primary proposed model result
(which is already in Table 1). Parameter counts are inferred from the text stating a 500k budget for
PascalVOC-SP for baselines and ~1M for PST. [Peptides-func] Extracted all rows from Table 1, Table
2, and Table 3 for the 'Peptides-Func' dataset. Note that Table 2 and Table 3 contain duplicate
entries for the main PST model and some baselines (GraphGPS, Graph-MLPMixer) compared to Table 1.
These are included as they appear in distinct tables in the source text. The metric AP is normalized
to [0,1]. Standard deviations are parsed from the '±' notation. [Peptides-struct] Extracted all
Peptides-Struct MAE results from Table 1 and Table 3. Table 2 contains duplicate results for PST,
GraphGPS, and Graph-MLPMixer which are already covered in Table 1. The primary metric MAE is used.
All values are normalized correctly (MAE is not percentage). Standard deviations are parsed from the
underscore notation.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*