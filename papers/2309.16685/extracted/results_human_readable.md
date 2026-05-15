# Extraction: arXiv:2309.16685
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: PMN
- Type: GNN

## Results

### DAVIS — MSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| KronRLS | 0.3790 | — | Yes | nascimento2016multiple | Table 1 |
| SimBoost | 0.2820 | — | Yes | He2017 | Table 1 |
| SimCNN-DTA | 0.3190 | — | Yes | shim2021prediction | Table 1 |
| DeepDTA | 0.2610 | — | Yes | 10.1093/bioinformatics/bty593 | Table 1 |
| WideDTA | 0.8860 | — | Yes | ozturk2019widedta | Table 1 |
| AttentionDTA | 0.2160 | — | Yes | zhao2019attentiondta | Table 1 |
| MATT-DTI | 0.2270 | — | Yes | 10.1093/bib/bbab117 | Table 1 |
| GraphDTA | 0.2580 | — | Yes | D3RA00281K | Table 1 |
| FusionDTA | 0.2200 | — | Yes | 10.1093/bib/bbab506 | Table 1 |
| BiCompDTA | 0.2370 | — | Yes | 10.1371/journal.pcbi.1011036 | Table 1 |
| PMN | 0.2020 | 0.0070 | No | this paper | Table 1 |

### KIBA — MSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| KronRLS | 0.4110 | — | Yes | nascimento2016multiple | Table 1 |
| SimBoost | 0.2220 | — | Yes | He2017 | Table 1 |
| SimCNN-DTA | 0.2740 | — | Yes | shim2021prediction | Table 1 |
| DeepDTA | 0.1940 | — | Yes | 10.1093/bioinformatics/bty593 | Table 1 |
| WideDTA | 0.8750 | — | Yes | ozturk2019widedta | Table 1 |
| AttentionDTA | 0.1550 | — | Yes | zhao2019attentiondta | Table 1 |
| MATT-DTI | 0.1500 | — | Yes | 10.1093/bib/bbab117 | Table 1 |
| GraphDTA | 0.1620 | — | Yes | D3RA00281K | Table 1 |
| FusionDTA | 0.1670 | — | Yes | 10.1093/bib/bbab506 | Table 1 |
| BiCompDTA | 0.1670 | — | Yes | 10.1371/journal.pcbi.1011036 | Table 1 |
| PMN | 0.1530 | 0.0020 | No | this paper | Table 1 |

### LBA — RMSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| 3D-CNN | 1.4160 | 0.0210 | Yes | this paper | Table 1 |
| GNN | 1.5700 | 0.0250 | Yes | this paper | Table 1 |
| ENN | 1.5680 | 0.0120 | Yes | this paper | Table 1 |
| GVP-MPNN | 1.5940 | 0.0730 | Yes | this paper | Table 1 |
| PMN* | 1.3530 | 0.0120 | No | this paper | Table 1 |

## Baseline Models Identified

- **KronRLS** (from: nascimento2016multiple)
- **SimBoost** (from: He2017)
- **SimCNN-DTA** (from: shim2021prediction)
- **DeepDTA** (from: 10.1093/bioinformatics/bty593)
- **WideDTA** (from: ozturk2019widedta)
- **AttentionDTA** (from: zhao2019attentiondta)
- **MATT-DTI** (from: 10.1093/bib/bbab117)
- **GraphDTA** (from: D3RA00281K)
- **FusionDTA** (from: 10.1093/bib/bbab506)
- **BiCompDTA** (from: 10.1371/journal.pcbi.1011036)
- **3D-CNN** (from: Townshend et al. 2020)
- **GNN** (from: Townshend et al. 2020)
- **ENN** (from: Cormorant (Satorras et al. 2021))
- **GVP-MPNN** (from: Jing et al. 2021)

## Extraction Notes

[DAVIS] Extracted only DAVIS MSE results as requested. FusionDTA uses ESM-1b which is external pre-
trained data, so uses_external_data is set to true. Other baselines are taken from cited papers
without explicit mention of external pre-training in the context of the benchmark setup described.
The table provides mean values; standard deviations are only provided for the proposed model PMN.
[KIBA] Extracted only KIBA MSE results as requested. The table provides averaged results over five
runs. Standard deviations are only provided for the proposed model (PMN). Baseline models do not
have standard deviations listed in the table. FusionDTA uses ESM-1b which is external pre-trained
data, so uses_external_data is set to true. All other baselines are treated as using only benchmark
data unless specified otherwise in their original citations, but for consistency with the extraction
rule 'null if unclear', and since the paper doesn't explicitly detail their pre-training for the
purpose of this specific comparison beyond citing them, I set most to false. However, FusionDTA is
explicitly mentioned as using ESM-1b. GraphDTA citation D3RA00281K is the same source for the 3D
structures, but GraphDTA itself is a sequence-based model typically. The paper states 'results are
taken from [citation]', implying we use their reported numbers. I will stick to false for baselines
unless explicitly stated they use external data in the context of the comparison, except FusionDTA
which is explicitly contrasted for using ESM-1b. [LBA] The user requested 'Accuracy' as the primary
metric, but the paper explicitly states that the LBA dataset is evaluated using RMSE (Root-Mean-
Squared Error). The table only contains RMSE results. Following the instruction to extract
quantitative results reported in the paper for the specified dataset, I extracted the RMSE values.
Accuracy is not reported for this dataset in this paper.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*