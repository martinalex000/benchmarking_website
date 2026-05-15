# Extraction: arXiv:2405.19121
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: S2GNN
- Type: GNN

## Results

### CLUSTER — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| ARGNP | 0.7735 | 0.0005 | Yes | cai_automatic_2022 | Table 1 |
| GPS | 0.7802 | 0.0018 | Yes | rampasek_recipe_2022 | Table 1 |
| TIGT | 0.7803 | 0.0022 | Yes | choi_topology-informed_2024 | Table 1 |
| GPTrans-Nano | 0.7807 | 0.0015 | Yes | chen_graph_2023 | Table 1 |
| Exphormer | 0.7807 | 0.0004 | Yes | shirzad_exphormer_2023 | Table 1 |
| EGT | 0.7923 | 0.0035 | Yes | hussain_global_2022 | Table 1 |
| GRIT | 0.8003 | 0.0028 | Yes | ma_graph_2023 | Table 1 |
| GatedGCN | 0.7608 | 0.0020 | Yes | this paper | Table 1 |
| S² GatedGCN | 0.7808 | 0.0005 | No | this paper | Table 1 |

### Distance Regression (DAGs) — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DirGCN (DAGs, undir, no PE, no Spec) | 1.9248 | 0.0116 | Yes | this paper | Table 1 (app:source_dist) |
| DirGCN (DAGs, undir, no PE, Spec) | 1.7384 | 0.0039 | Yes | this paper | Table 1 (app:source_dist) |
| DirGCN (DAGs, direc, no PE, no Spec) | 1.2401 | 0.0173 | Yes | this paper | Table 1 (app:source_dist) |
| S²GNN s (DAGs, direc, PE, Spec) | 1.1676 | 0.0032 | No | this paper | Table 1 (app:source_dist) |

### Distance Regression (Trees) — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DirGCN (Trees, undir, no PE, no Spec) | 1.0236 | 0.0408 | Yes | this paper | Table 1 (app:source_dist) |
| DirGCN (Trees, undir, no PE, Spec) | 1.2887 | 0.1195 | Yes | this paper | Table 1 (app:source_dist) |
| DirGCN (Trees, direc, no PE, no Spec) | 0.8166 | 0.5012 | Yes | this paper | Table 1 (app:source_dist) |
| S²GNN s (Trees, direc, PE, Spec) | 0.7767 | 0.3306 | No | this paper | Table 1 (app:source_dist) |

### GMM Clustering — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| S² GCN | 0.4546 | 0.0002 | No | this paper | Table 1 |
| S² GCN (+PE) | 0.4546 | 0.0002 | No | this paper | Table 1 |
| GCN | 0.2700 | 0.0002 | Yes | this paper | Table 2 |
| GCN (+PE) | 0.2684 | 0.0005 | Yes | this paper | Table 2 |

### OGB Products — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GAT | 0.7980 | 0.0030 | Yes | this paper | Table 1 |
| S$^2$GAT | 0.8110 | 0.0070 | No | this paper | Table 1 |

### TPUGraphs — Kendall tau ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.6009 | — | Yes | this paper | Table 2 (in main text, labeled tab:tpu_graphs) |
| S² GCN | 0.6574 | — | No | this paper | Table 2 (in main text, labeled tab:tpu_graphs) |

### arXiv-year — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DirGCN | 0.6408 | 0.0026 | Yes | Rossi et al. 2023 | Table 1 |
| FaberNet | 0.6462 | 0.0101 | Yes | Koke et al. 2024 | Table 1 |
| DirGCN (tuned) | 0.6444 | 0.0027 | Yes | this paper | Table 1 |
| S² DirGCN | 0.6495 | 0.0033 | No | this paper | Table 1 |

## Baseline Models Identified

- **GCN** (from: Kipf & Welling 2017)
- **GAT** (from: Veličković et al. 2018)
- **GraphTransformer** (from: Rong et al. 2020 / Dwivedi et al. 2020)
- **GIN** (from: Xu et al. 2019)
- **PNA** (from: Corso et al. 2020)
- **DimeNet++** (from: Gasteiger et al. 2021)
- **SphereNet** (from: Liu et al. 2022)
- **EGNN** (from: Satorras et al. 2021)
- **SE(3)-Transformer** (from: Fuchs et al. 2020)
- **E(3)-Equivariant** (from: Beaini et al. 2022)
- **ViSNet** (from: Deng et al. 2022)
- **NequIP** (from: Batatia et al. 2022)
- **MACE** (from: Batatia et al. 2022)
- **SchNet** (from: Schütt et al. 2017)
- **DimeNet** (from: Gasteiger et al. 2020)
- **CGCNN** (from: Xie & Grossman 2018)
- **M3GNet** (from: Chen et al. 2021)
- **ALIGNN** (from: Thakkar et al. 2021)
- **DirGCN** (from: Rossi et al. 2023)
- **FaberNet** (from: Koke et al. 2024)
- **ARGNP** (from: cai_automatic_2022)
- **GPS** (from: rampasek_recipe_2022)
- **TIGT** (from: choi_topology-informed_2024)
- **GPTrans-Nano** (from: chen_graph_2023)
- **Exphormer** (from: shirzad_exphormer_2023)
- **EGT** (from: hussain_global_2022)
- **GRIT** (from: ma_graph_2023)
- **GatedGCN** (from: this paper)
- **S² GCN (+PE)**
- **GCN (+PE)**

## Extraction Notes

[Peptides-func] The provided text contains tables for dataset statistics, hyperparameters, and
ablation studies on synthetic clustering tasks (GMM, SBM). It does NOT contain the main experimental
results table for the Peptides-func dataset. Therefore, no quantitative results for Peptides-func
could be extracted from the provided snippet. [OGB Products] Extracted only the Test Accuracy
results for OGB Products as requested. The table also contains F1 scores and Train/Val results,
which were ignored per instructions to focus on the primary metric (Accuracy) and test set only. The
proposed model is S$^2$GAT, a variant of GAT with spectral filters. [TPUGraphs] Extracted results
for TPUGraphs from the table labeled 'tab:tpu_graphs' in the main text. The metric 'Kendall tau' is
reported as raw values (e.g., 60.09, 65.74). Since Kendall tau is a correlation coefficient
typically in [-1, 1], but here reported as percentages or scaled scores (likely * 100 or similar
scaling given the magnitude), I have normalized them to [0, 1] range by dividing by 100, assuming
the paper reports them as percentages or scaled integers. However, looking at the values 60.09 and
65.74, these are likely already scaled or represent a specific metric variant. Standard Kendall tau
is -1 to 1. If these are percentages, 60.09% = 0.6009. If they are raw scores, they might be >1.
Given the instruction to normalize Accuracy/F1/AP/AUC/Hits@K/MRR to [0,1], and Kendall tau is a rank
correlation similar to these, I will treat it as a score that should be in [0,1] if it's a
normalized correlation. However, 60.09 is clearly not in [0,1]. It is highly probable the paper
reports Kendall tau * 100 or it is a different metric. Let's look at the context. 'Kendall tau (↑)'.
Usually Kendall tau is -1 to 1. If the paper reports 60.09, it might be 0.6009 * 100. I will output
the value as 0.6009 and 0.6574 to adhere to the [0,1] rule for correlation-like metrics, assuming
the paper's '60.09' means 60.09% or scaled by 100. If the paper meant raw 60.09, it would be >1.
Given the '↑' and typical reporting, normalization to 0.6009 is the safest interpretation of
'standard benchmark score' in [0,1] range if it's a percentage. Wait, if it's Kendall tau, it can be
negative. But here it's positive and high. I will assume the values 60.09 and 65.74 are percentages
(i.e., 0.6009 and 0.6574). If they are not percentages, they are likely scaled. I will output 0.6009
and 0.6574. [arXiv-year] Extracted all rows from Table 1 (tab:arxiv_year). The table caption
explicitly states 'Results on arXiv-year'. The proposed model is S² DirGCN. Baselines include
DirGCN, FaberNet, and a tuned version of DirGCN. All values are normalized to [0,1] as they are
Accuracy scores. [CLUSTER] Extracted all rows from Table 1 (tab:cluster_sbm) for the CLUSTER
dataset. The proposed model is S² GatedGCN. Baselines are taken from the table, with source
references inferred from citations in the table and text. All values are Accuracy (higher is
better). Standard deviations are parsed from the ± notation. [GMM Clustering] Extracted all rows
from Table 1 and Table 2 which report Accuracy on the GMM Clustering dataset. Table 1 varies the
number of eigenvectors k (0-10). Table 2 varies the number of MP layers (2-10). The 'S² GCN' model
is treated as the proposed model based on the context of comparing it against standard GCN. All
values are normalized to [0,1]. Standard deviations are extracted from the ± notation. [Distance
Regression] The paper presents results for 'Distance Regression' on two graph structures: DAGs and
Trees. The table includes both in-distribution and out-of-distribution results. The FOCUS
instruction requested the 'STANDARD / DEFAULT' configuration. In this context, the 'in-distribution'
split is the standard benchmark setting for evaluating model performance on the training
distribution. The 'out-of-distribution' results are excluded as they represent a specific
variant/evaluation setting. The proposed model S²GNN s is identified by the bold values in the
'direc' + 'PE' + 'Spec' rows, which represent the full proposed architecture. Baselines are DirGCN
variants. MAE is the primary metric. R² and RMSE are secondary and excluded per instructions.
External data usage is false as these are synthetic graph generation tasks.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*