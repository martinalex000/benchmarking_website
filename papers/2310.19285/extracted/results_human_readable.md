# Extraction: arXiv:2310.19285
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: GRIT + RRWP + Hodge1Lap_project
- Type: GraphTransformer

## Results

### CIFAR10 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5571 | 0.0038 | Yes | this paper | Table 1 |
| GIN | 0.5525 | 0.0153 | Yes | this paper | Table 1 |
| GAT | 0.6422 | 0.0046 | Yes | this paper | Table 1 |
| GatedGCN | 0.6731 | 0.0031 | Yes | this paper | Table 1 |
| PNA | 0.7035 | 0.0063 | Yes | this paper | Table 1 |
| DGN | 0.7284 | 0.0042 | Yes | this paper | Table 1 |
| CRaWl | 0.6901 | 0.0026 | Yes | this paper | Table 1 |
| GIN-AK+ | 0.7219 | 0.0013 | Yes | this paper | Table 1 |
| EGT | 0.6870 | 0.0041 | Yes | this paper | Table 1 |
| GPS | 0.7230 | 0.0036 | Yes | this paper | Table 1 |
| GatedGCN+EdgeRWSE | 0.7026 | 0.0034 | No | this paper | Table 1 |
| GPS+EdgeRWSE | 0.7242 | 0.0022 | No | this paper | Table 1 |

### MNIST — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.9071 | 0.0022 | Yes | GCN | Table 1 |
| GIN | 0.9648 | 0.0025 | Yes | HowPowerfulGNN | Table 1 |
| GAT | 0.9554 | 0.0021 | Yes | GAT | Table 1 |
| GatedGCN | 0.9734 | 0.0014 | Yes | ResidualGatedGCN | Table 1 |
| PNA | 0.9794 | 0.0012 | Yes | PNA | Table 1 |
| CRaWl | 0.9794 | 0.0005 | Yes | 1DConvRandomWalk | Table 1 |
| EGT | 0.9817 | 0.0009 | Yes | EGT | Table 1 |
| GPS | 0.9805 | 0.0013 | Yes | GPS | Table 1 |
| GatedGCN+EdgeRWSE | 0.9807 | 0.0011 | No | this paper | Table 1 |
| GPS+EdgeRWSE | 0.9825 | 0.0007 | No | this paper | Table 1 |

### PCQM-Contact — MRR ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3234 | 0.0006 | Yes | this paper | Table 1 |
| GINE | 0.3180 | 0.0027 | Yes | this paper | Table 1 |
| GatedGCN | 0.3218 | 0.0011 | Yes | this paper | Table 1 |
| Transformer+LapPE | 0.3174 | 0.0020 | Yes | this paper | Table 1 |
| SAN+LapPE | 0.3350 | 0.0003 | Yes | RethinkingGTLap | Table 1 |
| SAN+RWSE | 0.3350 | 0.0003 | Yes | RethinkingGTLap | Table 1 |
| GPS | 0.3337 | 0.0006 | Yes | GPS | Table 1 |
| GatedGCN+EdgeRWSE | 0.3342 | 0.0008 | Yes | this paper | Table 1 |
| GatedGCN+Hodge1Lap | 0.3336 | 0.0004 | Yes | this paper | Table 1 |
| GPS+EdgeRWSE | 0.3408 | 0.0003 | No | this paper | Table 1 |
| GPS+Hodge1Lap | 0.3407 | 0.0004 | Yes | this paper | Table 1 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5930 | 0.0023 | Yes | this paper | Table 1 |
| GINE | 0.5498 | 0.0079 | Yes | this paper | Table 1 |
| GatedGCN | 0.5864 | 0.0077 | Yes | this paper | Table 1 |
| Transformer+LapPE | 0.6326 | 0.0126 | Yes | this paper | Table 1 |
| SAN+LapPE | 0.6384 | 0.0121 | Yes | this paper | Table 1 |
| SAN+RWSE | 0.6439 | 0.0075 | Yes | this paper | Table 1 |
| GPS | 0.6535 | 0.0041 | Yes | this paper | Table 1 |
| GatedGCN+EdgeRWSE | 0.6002 | 0.0048 | Yes | this paper | Table 1 |
| GatedGCN+Hodge1Lap | 0.5926 | 0.0059 | Yes | this paper | Table 1 |
| GPS+EdgeRWSE | 0.6625 | 0.0042 | No | this paper | Table 1 |
| GPS+Hodge1Lap | 0.6584 | 0.0033 | Yes | this paper | Table 1 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3496 | 0.0013 | Yes | this paper | Table 1 |
| GINE | 0.3547 | 0.0045 | Yes | this paper | Table 1 |
| GatedGCN | 0.3420 | 0.0013 | Yes | this paper | Table 1 |
| Transformer+LapPE | 0.2529 | 0.0016 | Yes | this paper | Table 1 |
| SAN+LapPE | 0.2683 | 0.0043 | Yes | this paper | Table 1 |
| SAN+RWSE | 0.2545 | 0.0012 | Yes | this paper | Table 1 |
| GPS | 0.2500 | 0.0005 | Yes | this paper | Table 1 |
| GatedGCN+EdgeRWSE | 0.2679 | 0.0015 | Yes | this paper | Table 1 |
| GatedGCN+Hodge1Lap | 0.2632 | 0.0008 | Yes | this paper | Table 1 |
| GPS+EdgeRWSE | 0.2501 | 0.0012 | No | this paper | Table 1 |
| GPS+Hodge1Lap | 0.2505 | 0.0014 | Yes | this paper | Table 1 |

### Zinc-12k — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.5260 | 0.0510 | Yes | this paper | Table 1 |
| GSN | 0.1010 | 0.0100 | Yes | this paper | Table 1 |
| Graphormer | 0.1220 | 0.0060 | Yes | this paper | Table 1 |
| SAN | 0.1390 | 0.0060 | Yes | this paper | Table 1 |
| GIN-AK+ | 0.0800 | 0.0010 | Yes | this paper | Table 1 |
| CIN | 0.0790 | 0.0060 | Yes | this paper | Table 1 |
| Specformer | 0.0660 | 0.0030 | Yes | this paper | Table 1 |
| GINE | 0.1330 | 0.0020 | Yes | this paper | Table 1 |
| GINE + EdgeRWSE(directed) | 0.1100 | 0.0030 | Yes | this paper | Table 1 |
| GINE + EdgeRWSE(undirected) | 0.1040 | 0.0080 | Yes | this paper | Table 1 |
| GINE + Hodge1Lap(abs) | 0.1020 | 0.0040 | Yes | this paper | Table 1 |
| GINE + Hodge1Lap(project) | 0.0910 | 0.0040 | Yes | this paper | Table 1 |
| GINE + LapPE | 0.1200 | 0.0050 | Yes | this paper | Table 1 |
| GINE + RWSE | 0.0740 | 0.0030 | Yes | this paper | Table 1 |
| GINE + RWSE + EdgeRWSE(directed) | 0.0700 | 0.0030 | Yes | this paper | Table 1 |
| GINE + RWSE + EdgeRWSE(undirected) | 0.0690 | 0.0020 | Yes | this paper | Table 1 |
| GINE + RWSE + Hodge1Lap(abs) | 0.0680 | 0.0030 | Yes | this paper | Table 1 |
| GINE + RWSE + Hodge1Lap(project) | 0.0680 | 0.0040 | Yes | this paper | Table 1 |
| GINE + RWSE + RWMP | 0.0680 | 0.0030 | Yes | this paper | Table 1 |
| GINE + RWSE + Hodge1Lap(project) + RWMP | 0.0660 | 0.0030 | Yes | this paper | Table 1 |
| GINE + RWSE + Full-EdgeRWSE | 0.0690 | 0.0030 | Yes | this paper | Table 1 |
| GINE + Inter-RWSE | 0.0830 | 0.0060 | Yes | this paper | Table 1 |
| GINE + RWSE + CellularRWSE | 0.0680 | 0.0030 | Yes | this paper | Table 1 |
| GAT | 0.3840 | 0.0070 | Yes | this paper | Table 1 |
| GAT + EdgeRWSE(undirected) | 0.1630 | 0.0080 | Yes | this paper | Table 1 |
| GAT + Hodge1Lap(project) | 0.1300 | 0.0050 | Yes | this paper | Table 1 |
| PNA | 0.1880 | 0.0040 | Yes | this paper | Table 1 |
| PNA + EdgeRWSE(undirected) | 0.1040 | 0.0040 | Yes | this paper | Table 1 |
| PNA + Hodge1Lap(project) | 0.0740 | 0.0050 | Yes | this paper | Table 1 |
| SSWL+ | 0.0700 | 0.0050 | Yes | this paper | Table 1 |
| SSWL+ + EdgeRWSE(undirected) | 0.0670 | 0.0050 | Yes | this paper | Table 1 |
| SSWL+ + Hodge1Lap(project) | 0.0660 | 0.0030 | Yes | this paper | Table 1 |
| GPS | 0.1130 | 0.0050 | Yes | this paper | Table 1 |
| GPS + RWSE | 0.0700 | 0.0040 | Yes | this paper | Table 1 |
| GPS + RWSE + EdgeRWSE(undirected) | 0.0680 | 0.0040 | Yes | this paper | Table 1 |
| GPS + RWSE + Hodge1Lap(project) | 0.0640 | 0.0030 | Yes | this paper | Table 1 |
| GRIT | 0.1490 | 0.0080 | Yes | this paper | Table 1 |
| GRIT + RWSE | 0.0810 | 0.0100 | Yes | this paper | Table 1 |
| GRIT + SPDPE | 0.0670 | 0.0020 | Yes | this paper | Table 1 |
| GRIT + RDPE | 0.0590 | 0.0030 | Yes | this paper | Table 1 |
| GRIT + RRWP | 0.0590 | 0.0020 | Yes | this paper | Table 1 |
| GRIT + EdgeRWSE(undirected) | 0.1030 | 0.0060 | Yes | this paper | Table 1 |
| GRIT + Hodge1Lap(project) | 0.0860 | 0.0050 | Yes | this paper | Table 1 |
| GRIT + RRWP + EdgeRWSE(undirected) | 0.0580 | 0.0020 | Yes | this paper | Table 1 |
| GRIT + RRWP + Hodge1Lap(project) | 0.0570 | 0.0030 | No | this paper | Table 1 |

### ogbg-molhiv — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN+virtual node | 0.7707 | 0.0149 | Yes | this paper | Table 1 |
| GSN (directional) | 0.8039 | 0.0090 | Yes | GSN | Table 1 |
| PNA | 0.7905 | 0.0132 | Yes | this paper | Table 1 |
| SAN | 0.7785 | 0.2470 | Yes | this paper | Table 1 |
| GIN-AK+ | 0.7961 | 0.0110 | Yes | this paper | Table 1 |
| CIN | 0.8094 | 0.0057 | Yes | CWNetworks | Table 1 |
| GPS | 0.7880 | 0.0101 | Yes | this paper | Table 1 |
| Specformer | 0.7889 | 0.0124 | Yes | this paper | Table 1 |
| GPS+EdgeRWSE | 0.7891 | 0.0118 | Yes | this paper | Table 1 |
| GPS+Hodge1Lap | 0.8021 | 0.0154 | No | this paper | Table 1 |

### ogbg-molpcba — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN+virtual node | 0.2703 | 0.0023 | Yes | this paper | Table 1 |
| PNA | 0.2838 | 0.0035 | Yes | this paper | Table 1 |
| SAN | 0.2765 | 0.0042 | Yes | this paper | Table 1 |
| GIN-AK+ | 0.2930 | 0.0044 | Yes | this paper | Table 1 |
| GPS | 0.2907 | 0.0028 | Yes | this paper | Table 1 |
| Specformer | 0.2972 | 0.0023 | Yes | this paper | Table 1 |
| GPS+EdgeRWSE | 0.2934 | 0.0025 | No | this paper | Table 1 |
| GPS+Hodge1Lap | 0.2937 | 0.0023 | No | this paper | Table 1 |

## Baseline Models Identified

- **GIN** (from: HowPowerfulGNN)
- **GSN** (from: GSN)
- **Graphormer** (from: Graphormer)
- **SAN** (from: RethinkingGTLap)
- **GIN-AK+** (from: GNNAK)
- **CIN** (from: CWNetworks)
- **Specformer** (from: Specformer)
- **GINE** (from: PretrainGINE)
- **GAT** (from: GAT)
- **PNA** (from: PNA)
- **SSWL+** (from: CompleteHierarchySubgraphGNN)
- **GPS** (from: GPS)
- **GRIT** (from: GRIT)
- **GIN+virtual node**
- **GSN (directional)** (from: GSN)
- **GPS+EdgeRWSE**
- **GPS+Hodge1Lap**
- **GCN** (from: GCN)
- **GatedGCN** (from: ResidualGatedGCN)
- **DGN** (from: DGN)
- **CRaWl** (from: 1DConvRandomWalk)
- **EGT** (from: EGT)
- **Transformer+LapPE**
- **SAN+LapPE** (from: RethinkingGTLap)
- **SAN+RWSE**
- **GatedGCN+EdgeRWSE**
- **GatedGCN+Hodge1Lap**

## Extraction Notes

[Zinc-12k] Extracted all rows from Table 1 for the Zinc-12k dataset. The proposed model is
identified as the one highlighted in red (first place) in the ablation study section, which is GRIT
augmented with RRWP and Hodge1Lap(project). All other rows are treated as baselines or ablation
variants of baselines. Metric is MAE, lower is better. Values are normalized to [0,1] range
implicitly as they are already small floats representing MAE. [ogbg-molhiv] Extracted only ogbg-
molhiv results as requested. The table caption mentions 'AUROC' which is equivalent to ROC-AUC. All
values were normalized to [0,1]. The standard deviation for SAN is unusually high (0.2470), but
extracted as reported. GPS+Hodge1Lap is identified as the proposed model based on the text stating
'We apply our Hodge1Lap...'. GPS+EdgeRWSE is also an ablation/proposed variant but treated as a
baseline row in the context of the proposed model being the main contribution (Hodge1Lap), or simply
extracted as a separate row. The prompt asks for ALL rows. I marked GPS+Hodge1Lap as
is_proposed=true. GPS+EdgeRWSE is also part of the proposed method family, but typically 'proposed
model' refers to the main architecture. I will mark GPS+Hodge1Lap as true. The text says 'show that
our methods can improve both architectures', implying both EdgeRWSE and Hodge1Lap are contributions.
However, usually one model is the primary 'proposed' one. Given the bolding, GPS+Hodge1Lap is the
best on this specific dataset. I will set is_proposed=true for GPS+Hodge1Lap. For GPS+EdgeRWSE, I
set it to false as it's a variant/ablation, though arguably also proposed. To be safe, I'll stick to
the main named contribution. [ogbg-molpcba] Extracted only results for 'ogbg-molpcba' as requested.
Excluded 'ogbg-molhiv' results. Note that GSN and CIN do not report results for ogbg-molpcba in the
provided table (marked with '-'), so they are excluded from the results list. The proposed models
are GPS+EdgeRWSE and GPS+Hodge1Lap. All values are normalized to [0,1] range for AP metric. [MNIST]
Extracted only MNIST results as requested. DGN and GIN-AK+ had no MNIST results reported (marked as
'-'), so they are excluded from the results list. All values were converted from percentages to
[0,1] range. Standard deviations were parsed from the 'mean ± std' format. [CIFAR10] Extracted all
rows from Table 1 for the CIFAR10 dataset. Values were converted from percentages to [0,1] range.
Standard deviations were parsed from the 'mean ± std' format. The proposed models are
GatedGCN+EdgeRWSE and GPS+EdgeRWSE as indicated by the text and table structure. [Peptides-func]
Extracted all rows from Table 1 for the Peptides-func dataset. The proposed model is identified as
GPS+EdgeRWSE based on the text stating it achieves the best performance on Peptides-func. All values
are normalized to [0,1] as AP is an accuracy-like metric. Standard deviations were parsed from the
'mean ± std' format. [Peptides-struct] Extracted all rows from Table 1 for the 'Peptides-struct'
dataset. The primary metric is MAE (lower is better). The proposed model is identified as
GPS+EdgeRWSE based on the text emphasis and table highlighting (blue for second best, but text
highlights it as achieving best on Peptides-func and implies strong performance; however,
GPS+Hodge1Lap is bolded as third best overall, and GPS+EdgeRWSE is blue. The text says 'GPS model
with EdgeRWSE ... achieve the best ... performance' on Peptides-func, but for Peptides-struct it
says improvement is not significant for GPS. Looking at the table, GPS+EdgeRWSE (0.2501) is slightly
better than GPS (0.2500) and GPS+Hodge1Lap (0.2505). The bolded value is GPS+Hodge1Lap (0.2505)
which is marked as 'third' in caption. The red value is GPS (0.2500) marked as 'first'. The blue
value is GPS+EdgeRWSE (0.2501) marked as 'second'. Wait, the caption says 'Highlighted are the
first, second, third test results'. Red=First, Blue=Second, Bold=Third. On Peptides-struct: GPS is
Red (First, 0.2500), GPS+EdgeRWSE is Blue (Second, 0.2501), GPS+Hodge1Lap is Bold (Third, 0.2505).
The paper proposes EdgeRWSE and Hodge1Lap enhancements. The 'proposed model' in the context of the
paper's contribution is likely the combination or the specific enhancements. However, the prompt
asks for 'proposed_model' in the JSON structure. Usually, this refers to the main new method. The
paper seems to propose EdgeRWSE and Hodge1Lap as general enhancements. I will mark GPS+EdgeRWSE as
proposed because it is one of the two main new configurations introduced, but note that GPS is the
baseline from GPS paper. Actually, the text says 'our results are obtained without hyperparameter
searching - our main goal is to verify the enhancement brought by EdgeRWSE and Hodge1Lap'. So both
GPS+EdgeRWSE and GPS+Hodge1Lap are proposed variants. I will set is_proposed=true for GPS+EdgeRWSE
as it is the first one listed in the bottom block and often the primary focus. Alternatively, since
both are enhancements, I could mark both. But the schema asks for a single proposed_model name. I
will stick with GPS+EdgeRWSE as the representative proposed model, or perhaps the paper considers
'GPS+EdgeRWSE' and 'GPS+Hodge1Lap' as the proposed methods. Given the ambiguity, I will mark
GPS+EdgeRWSE as true. The baselines are the top block models. [PCQM-Contact] Extracted all rows from
Table 1 for the PCQM-Contact dataset. The primary metric MRR was used. All values are normalized to
[0,1]. The proposed model is identified as GPS+EdgeRWSE based on the text highlighting it as
achieving the best performance on PCQM-Contact with EdgeRWSE.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*