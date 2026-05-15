# Extraction: arXiv:2505.23345
**Model used**: `MiniMaxAI/MiniMax-M2.5`  **Date**: 2026-05-12  **Confidence**: HIGH

## Proposed Model: GraphPAE
- Type: GNN

## Results

### Actor — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Supervised | 0.3393 | 0.0247 | Yes | this paper | Table 1 |
| DGI | 0.2798 | 0.0009 | Yes | this paper | Table 1 |
| BGRL | 0.2661 | 0.0057 | Yes | this paper | Table 1 |
| MVGRL | 0.3464 | 0.0020 | Yes | this paper | Table 1 |
| CCA-SSG | 0.2779 | 0.0058 | Yes | this paper | Table 1 |
| Sp$^2$GCL | 0.3470 | 0.0092 | Yes | this paper | Table 1 |
| VGAE | 0.3157 | 0.0075 | Yes | this paper | Table 1 |
| GraphMAE | 0.3215 | 0.0133 | Yes | this paper | Table 1 |
| GraphMAE2 | 0.3448 | 0.0026 | Yes | this paper | Table 1 |
| MaskGAE | 0.3344 | 0.0034 | Yes | this paper | Table 1 |
| S2GAE | 0.2617 | 0.0038 | Yes | this paper | Table 1 |
| AUG-MAE | 0.3342 | 0.0038 | Yes | this paper | Table 1 |
| GraphPAE | 0.3855 | 0.0135 | No | this paper | Table 1 |

### BlogCatalog — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Supervised | 0.8052 | 0.0210 | Yes | this paper | Table 1 |
| DGI | 0.7207 | 0.0016 | Yes | this paper | Table 1 |
| BGRL | 0.7974 | 0.0046 | Yes | this paper | Table 1 |
| MVGRL | 0.6324 | 0.0094 | Yes | this paper | Table 1 |
| CCA-SSG | 0.7400 | 0.0028 | Yes | this paper | Table 1 |
| Sp$^2$GCL | 0.7273 | 0.0046 | Yes | this paper | Table 1 |
| VGAE | 0.6047 | 0.0184 | Yes | this paper | Table 1 |
| GraphMAE | 0.7990 | 0.0113 | Yes | this paper | Table 1 |
| GraphMAE2 | 0.7734 | 0.0012 | Yes | this paper | Table 1 |
| MaskGAE | 0.7310 | 0.0008 | Yes | this paper | Table 1 |
| S2GAE | 0.7576 | 0.0043 | Yes | this paper | Table 1 |
| AUG-MAE | 0.8203 | 0.0069 | Yes | this paper | Table 1 |
| GraphPAE | 0.8576 | 0.0122 | No | this paper | Table 1 |

### Chameleon — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Supervised | 0.8002 | 0.0087 | Yes | this paper | Table 1 |
| DGI | 0.4383 | 0.0014 | Yes | this paper | Table 1 |
| BGRL | 0.6124 | 0.0107 | Yes | this paper | Table 1 |
| MVGRL | 0.7319 | 0.0042 | Yes | this paper | Table 1 |
| CCA-SSG | 0.7500 | 0.0075 | Yes | this paper | Table 1 |
| Sp$^2$GCL | 0.7888 | 0.0104 | Yes | this paper | Table 1 |
| VGAE | 0.6232 | 0.0190 | Yes | this paper | Table 1 |
| GraphMAE | 0.7950 | 0.0057 | Yes | this paper | Table 1 |
| GraphMAE2 | 0.7913 | 0.0019 | Yes | this paper | Table 1 |
| MaskGAE | 0.7450 | 0.0087 | Yes | this paper | Table 1 |
| S2GAE | 0.6024 | 0.0037 | Yes | this paper | Table 1 |
| AUG-MAE | 0.7010 | 0.0188 | Yes | this paper | Table 1 |
| GraphPAE | 0.8051 | 0.0125 | No | this paper | Table 1 |

### Facebook — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| BGRL | 0.8971 | 0.0035 | Yes | this paper | Table ef{tab:additional_exp} |
| CCA-SSG | 0.8945 | 0.0060 | Yes | this paper | Table ef{tab:additional_exp} |
| GraphMAE | 0.8954 | 0.0036 | Yes | this paper | Table ef{tab:additional_exp} |
| GraphMAE2 | 0.8849 | 0.0043 | Yes | this paper | Table ef{tab:additional_exp} |
| GraphPAE | 0.9146 | 0.0023 | No | this paper | Table ef{tab:additional_exp} |

### Penn94 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Supervised | 0.8153 | 0.0055 | Yes | this paper | Table 1 |
| BGRL | 0.6331 | 0.0049 | Yes | this paper | Table 1 |
| CCA-SSG | 0.6263 | 0.0020 | Yes | this paper | Table 1 |
| Sp$^2$GCL | 0.6880 | 0.0045 | Yes | this paper | Table 1 |
| VGAE | 0.5531 | 0.0028 | Yes | this paper | Table 1 |
| GraphMAE | 0.6797 | 0.0021 | Yes | this paper | Table 1 |
| GraphMAE2 | 0.6786 | 0.0042 | Yes | this paper | Table 1 |
| MaskGAE | 0.6384 | 0.0003 | Yes | this paper | Table 1 |
| S2GAE | 0.7024 | 0.0009 | Yes | this paper | Table 1 |
| AUG-MAE | 0.6990 | 0.0043 | Yes | this paper | Table 1 |
| GraphPAE | 0.7179 | 0.0037 | No | this paper | Table 1 |

### QM9 — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GraphCL | 1.0350 | — | Yes | this paper | Table 1 |
| GraphMAE | 1.0300 | — | Yes | this paper | Table 1 |
| Mole-BERT | 1.0310 | — | Yes | this paper | Table 1 |
| SimSGT | 1.0640 | — | Yes | this paper | Table 1 |
| GraphPAE | 0.7030 | — | No | this paper | Table 1 |

### Squirrel — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Supervised | 0.7191 | 0.0103 | Yes | this paper | Table 1 |
| DGI | 0.3456 | 0.0010 | Yes | this paper | Table 1 |
| BGRL | 0.4324 | 0.0052 | Yes | this paper | Table 1 |
| MVGRL | 0.6009 | 0.0044 | Yes | this paper | Table 1 |
| CCA-SSG | 0.6158 | 0.0198 | Yes | this paper | Table 1 |
| Sp$^2$GCL | 0.6261 | 0.0087 | Yes | this paper | Table 1 |
| VGAE | 0.4250 | 0.0135 | Yes | this paper | Table 1 |
| GraphMAE | 0.6113 | 0.0060 | Yes | this paper | Table 1 |
| GraphMAE2 | 0.7027 | 0.0088 | Yes | this paper | Table 1 |
| MaskGAE | 0.6853 | 0.0044 | Yes | this paper | Table 1 |
| S2GAE | 0.6860 | 0.0056 | Yes | this paper | Table 1 |
| AUG-MAE | 0.6257 | 0.0067 | Yes | this paper | Table 1 |
| GraphPAE | 0.7205 | 0.0140 | No | this paper | Table 1 |

### Wiki — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| BGRL | 0.7902 | 0.0013 | Yes | this paper | Table ef{tab:additional_exp} |
| CCA-SSG | 0.7885 | 0.0032 | Yes | this paper | Table ef{tab:additional_exp} |
| GraphMAE | 0.7894 | 0.0048 | Yes | this paper | Table ef{tab:additional_exp} |
| GraphMAE2 | 0.7884 | 0.0044 | Yes | this paper | Table ef{tab:additional_exp} |
| GraphPAE | 0.7932 | 0.0029 | No | this paper | Table ef{tab:additional_exp} |

### arXiv-year — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Supervised | 0.4602 | 0.0026 | Yes | this paper | Table 1 |
| BGRL | 0.4143 | 0.0004 | Yes | this paper | Table 1 |
| CCA-SSG | 0.4078 | 0.0001 | Yes | this paper | Table 1 |
| Sp$^2$GCL | 0.3909 | 0.0002 | Yes | this paper | Table 1 |
| VGAE | 0.3639 | 0.0021 | Yes | this paper | Table 1 |
| GraphMAE | 0.4030 | 0.0004 | Yes | this paper | Table 1 |
| GraphMAE2 | 0.3897 | 0.0003 | Yes | this paper | Table 1 |
| MaskGAE | 0.4059 | 0.0004 | Yes | this paper | Table 1 |
| S2GAE | 0.4032 | 0.0012 | Yes | this paper | Table 1 |
| AUG-MAE | 0.3710 | 0.0013 | Yes | this paper | Table 1 |
| GraphPAE | 0.4185 | 0.0004 | No | this paper | Table 1 |

### molbace — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Supervised | 0.8042 | 0.0096 | Yes | this paper | Table 1 |
| InfoGraph | 0.7364 | 0.0364 | Yes | this paper | Table 1 |
| GraphCL | 0.7332 | 0.0270 | Yes | this paper | Table 1 |
| MVGRL | 0.7488 | 0.0143 | Yes | this paper | Table 1 |
| JOAO | 0.7443 | 0.0194 | Yes | this paper | Table 1 |
| Sp$^2$GCL | 0.7876 | 0.0143 | Yes | this paper | Table 1 |
| GraphMAE | 0.7914 | 0.0131 | Yes | this paper | Table 1 |
| GraphMAE2 | 0.8074 | 0.0153 | Yes | this paper | Table 1 |
| StructMAE | 0.7775 | 0.0042 | Yes | this paper | Table 1 |
| AUG-MAE | 0.7854 | 0.0249 | Yes | this paper | Table 1 |
| GraphPAE | 0.8111 | 0.0124 | No | this paper | Table 1 |

### molbbbp — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Supervised | 0.6817 | 0.0148 | Yes | this paper | Table 1 |
| InfoGraph | 0.6633 | 0.0279 | Yes | this paper | Table 1 |
| GraphCL | 0.6822 | 0.0219 | Yes | this paper | Table 1 |
| MVGRL | 0.6724 | 0.0319 | Yes | this paper | Table 1 |
| JOAO | 0.6762 | 0.0129 | Yes | this paper | Table 1 |
| Sp$^2$GCL | 0.6872 | 0.0153 | Yes | this paper | Table 1 |
| GraphMAE | 0.6655 | 0.0178 | Yes | this paper | Table 1 |
| GraphMAE2 | 0.6767 | 0.0144 | Yes | this paper | Table 1 |
| StructMAE | 0.6566 | 0.0116 | Yes | this paper | Table 1 |
| AUG-MAE | 0.6705 | 0.0063 | Yes | this paper | Table 1 |
| GraphPAE | 0.6856 | 0.0071 | No | this paper | Table 1 |

### molclintox — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Supervised | 0.8814 | 0.0251 | Yes | this paper | Table 1 |
| InfoGraph | 0.6450 | 0.0532 | Yes | this paper | Table 1 |
| GraphCL | 0.7492 | 0.0442 | Yes | this paper | Table 1 |
| MVGRL | 0.7384 | 0.0275 | Yes | this paper | Table 1 |
| JOAO | 0.7128 | 0.0412 | Yes | this paper | Table 1 |
| Sp$^2$GCL | 0.8088 | 0.0386 | Yes | this paper | Table 1 |
| GraphMAE | 0.8056 | 0.0555 | Yes | this paper | Table 1 |
| GraphMAE2 | 0.7575 | 0.0365 | Yes | this paper | Table 1 |
| StructMAE | 0.7942 | 0.0456 | Yes | this paper | Table 1 |
| AUG-MAE | 0.8266 | 0.0198 | Yes | this paper | Table 1 |
| GraphPAE | 0.8269 | 0.0339 | No | this paper | Table 1 |

### molesol — RMSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Supervised | 1.1730 | 0.0570 | Yes | this paper | Table 1 |
| InfoGraph | 1.3440 | 0.1780 | Yes | this paper | Table 1 |
| GraphCL | 1.2720 | 0.0890 | Yes | this paper | Table 1 |
| MVGRL | 1.4330 | 0.1450 | Yes | this paper | Table 1 |
| JOAO | 1.2850 | 0.1210 | Yes | this paper | Table 1 |
| Sp$^2$GCL | 1.2350 | 0.1190 | Yes | this paper | Table 1 |
| GraphMAE | 1.0500 | 0.0340 | Yes | this paper | Table 1 |
| GraphMAE2 | 1.2250 | 0.0810 | Yes | this paper | Table 1 |
| StructMAE | 1.4990 | 0.0430 | Yes | this paper | Table 1 |
| AUG-MAE | 1.2480 | 0.0260 | Yes | this paper | Table 1 |
| GraphPAE | 1.0150 | 0.0450 | No | this paper | Table 1 |

### molfreesolv — RMSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Supervised | 2.7550 | 0.3490 | Yes | this paper | Table 1 |
| InfoGraph | 10.0050 | 8.1470 | Yes | this paper | Table 1 |
| GraphCL | 7.6790 | 2.7480 | Yes | this paper | Table 1 |
| MVGRL | 9.0240 | 1.9820 | Yes | this paper | Table 1 |
| JOAO | 5.1310 | 0.7820 | Yes | this paper | Table 1 |
| Sp$^2$GCL | 4.1440 | 0.5730 | Yes | this paper | Table 1 |
| GraphMAE | 2.7400 | 0.2330 | Yes | this paper | Table 1 |
| GraphMAE2 | 2.9130 | 0.2930 | Yes | this paper | Table 1 |
| StructMAE | 2.5680 | 0.2620 | Yes | this paper | Table 1 |
| AUG-MAE | 2.3950 | 0.1580 | Yes | this paper | Table 1 |
| GraphPAE | 2.0580 | 0.1880 | No | this paper | Table 1 |

### molipo — RMSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Supervised | 0.7570 | 0.0180 | Yes | this paper | Table 1 |
| InfoGraph | 1.0050 | 0.0230 | Yes | this paper | Table 1 |
| GraphCL | 0.9100 | 0.0160 | Yes | this paper | Table 1 |
| MVGRL | 0.9620 | 0.0360 | Yes | this paper | Table 1 |
| JOAO | 0.8650 | 0.0320 | Yes | this paper | Table 1 |
| Sp$^2$GCL | 0.8350 | 0.0260 | Yes | this paper | Table 1 |
| GraphMAE | 0.8500 | 0.0220 | Yes | this paper | Table 1 |
| GraphMAE2 | 0.8850 | 0.0190 | Yes | this paper | Table 1 |
| StructMAE | 1.0890 | 0.0020 | Yes | this paper | Table 1 |
| AUG-MAE | 0.9170 | 0.0130 | Yes | this paper | Table 1 |
| GraphPAE | 0.8100 | 0.0180 | No | this paper | Table 1 |

### moltocx21 — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Supervised | 0.7491 | 0.0051 | Yes | this paper | Table 1 |
| InfoGraph | 0.6974 | 0.0057 | Yes | this paper | Table 1 |
| GraphCL | 0.7240 | 0.0107 | Yes | this paper | Table 1 |
| MVGRL | 0.7048 | 0.0083 | Yes | this paper | Table 1 |
| JOAO | 0.7138 | 0.0092 | Yes | this paper | Table 1 |
| Sp$^2$GCL | 0.7306 | 0.0075 | Yes | this paper | Table 1 |
| GraphMAE | 0.7384 | 0.0058 | Yes | this paper | Table 1 |
| GraphMAE2 | 0.7293 | 0.0069 | Yes | this paper | Table 1 |
| StructMAE | 0.7113 | 0.0061 | Yes | this paper | Table 1 |
| AUG-MAE | 0.7433 | 0.0007 | Yes | this paper | Table 1 |
| GraphPAE | 0.7446 | 0.0054 | No | this paper | Table 1 |

### ogbg-products — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| BGRL | 0.7859 | 0.0002 | Yes | this paper | Table 1 |
| CCA-SSG | 0.7527 | 0.0005 | Yes | this paper | Table 1 |
| GraphMAE | 0.7889 | 0.0001 | Yes | this paper | Table 1 |
| GraphMAE2 | 0.8159 | 0.0002 | Yes | this paper | Table 1 |
| GraphPAE | 0.7910 | 0.0002 | No | this paper | Table 1 |

## Baseline Models Identified

- **Supervised**
- **DGI**
- **BGRL**
- **MVGRL**
- **CCA-SSG**
- **Sp$^2$GCL**
- **VGAE**
- **GraphMAE**
- **GraphMAE2**
- **MaskGAE**
- **S2GAE**
- **AUG-MAE**
- **InfoGraph**
- **GraphCL**
- **JOAO**
- **StructMAE**
- **Mole-BERT**
- **SimSGT**

## Extraction Notes

[BlogCatalog] Extracted results for BlogCatalog from Table 1. Table 2 contains ablation studies for
'Blog' which is likely BlogCatalog, but per instructions to focus on standard/default configurations
and primary benchmark results, Table 1 is the primary source. Values were normalized from
percentages to [0, 1]. [Chameleon] Extracted all models from Table 1 for the Chameleon dataset.
Values were normalized from percentages to decimals. [Squirrel] Extracted results for Squirrel from
Table 1. Ablation Table 2 was skipped as it contains internal configuration variants rather than the
standard model benchmark results. [Actor] Extracted only the 'Actor' column from Table 1 as
requested. Values were divided by 100 to normalize percentages to [0, 1]. [arXiv-year] Extracted
only results for arXiv-year from Table 1. DGI and MVGRL had no reported values for this dataset.
[Penn94] Extracted only Penn94 results from Table 1 as requested. DGI and MVGRL had no reported
values for Penn94. [molesol] Extracted only the 'molesol' column from Table 1 as requested. Table 2
did not contain 'molesol' results. [molipo] Extracted only the 'molipo' column from Table 1 as
requested. Table 2 did not contain results for 'molipo'. [molfreesolv] Extracted only molfreesolv
results from Table 1. Table 2 contains ablation studies for 'Freesolv' which is likely the same
dataset, but per instructions to focus on standard benchmark results and the primary metric RMSE,
the main results table was prioritized. Ablation results were skipped as they represent internal
model variants rather than the final proposed model vs baselines. [molbace] Extracted results for
'molbace' from Table 1. Table 2 contains ablation studies for 'Bace' which is likely the same
dataset, but per instructions to focus on the standard configuration and primary benchmark results,
Table 1 was prioritized. ROC-AUC values were divided by 100. [molbbbp] Extracted results for molbbbp
from Table 1. Table 2 contains ablation studies for 'Bbbp' which are internal variants of the
proposed model and were excluded per the instruction to use only the standard/default configuration.
ROC-AUC values were divided by 100 to normalize to [0, 1]. [molclintox] Extracted only molclintox
results from Table 1. ROC-AUC values were converted from percentages to decimals. [moltocx21]
Extracted only moltocx21 results from Table 1. Normalized ROC-AUC% by dividing by 100. [QM9] The
table reports MAE for 12 different target properties of QM9. Each column represents a different
property (mu, alpha, etc.). I have extracted each property as a separate result entry for each
model, all under the metric 'MAE' as per the primary metric instruction. [Bace] Extracted results
for 'molbace' from Table 1. Ablation tables (Table 2 and 3) were skipped as they represent internal
variants/configurations of the proposed model rather than the standard benchmark comparison. [Bbbp]
Extracted results for 'molbbbp' from Table 1. Ablation tables (Table 2 and 3) were skipped as they
represent internal model variants/configurations rather than the standard benchmark comparison of
the proposed model vs baselines. Values were normalized from percentages to [0, 1]. [Freesolv]
Extracted results for 'molfreesolv' from Table 1. Ablation tables (Table 2 and 3) were skipped as
they represent non-standard configurations/variants of the proposed model rather than the final
benchmark results. [Facebook] The table does not explicitly name the metric, but based on the
context of the dataset (Facebook) and the values provided (percentages), Accuracy is the standard
benchmark metric for this task. Values were normalized from percentages to [0, 1]. [Wiki] Extracted
only the Wiki dataset as requested. Values were converted from percentages to decimals. [ogbg-
products] Extracted only ogbg-products results as requested. Values were converted from percentages
to decimals. Table reference is based on the provided snippet.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*