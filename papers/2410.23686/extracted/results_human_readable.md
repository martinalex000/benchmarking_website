# Extraction: arXiv:2410.23686
**Model used**: `MiniMaxAI/MiniMax-M2.5`  **Date**: 2026-05-13  **Confidence**: HIGH

## Proposed Model: nsqure
- Type: GNN

## Results

### COLLAB — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| PATCHY-SAN | 0.7260 | 0.0215 | Yes | niepert 2016 | Table 1 |
| GCN | 0.8059 | 0.0027 | Yes | kipf 2017 | Table 1 |
| PG | 0.8090 | 0.0080 | Yes | huang 2022 | Table 1 |
| CoCN | 0.8615 | 0.0010 | Yes | sun 2023 | Table 1 |
| GIN | 0.7819 | 0.0063 | Yes | xu* 2019 | Table 1 |
| GraphSAGE | 0.7390 | 0.0170 | Yes | hamilton 2017 | Table 1 |
| DiffPool | 0.8213 | 0.0043 | Yes | ying 2018 | Table 1 |
| TopKPool | 0.7758 | 0.0085 | Yes | gao 2019 | Table 1 |
| SAGPool | 0.7803 | 0.0031 | Yes | lee 2019 | Table 1 |
| StructPool | 0.7727 | 0.0051 | Yes | yuan 2020 | Table 1 |
| SEP | 0.8128 | 0.0015 | Yes | wu 2022 | Table 1 |
| GMT | 0.8074 | 0.0054 | Yes | baek 2022 | Table 1 |
| nsqure | 0.8672 | 0.0162 | No | this paper | Table 1 |

### Genius — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| SGC | 0.8236 | 0.0037 | Yes | wu_SimplifyingGraphConvolutional_2019 | Table 1 |
| GCN | 0.8742 | 0.0037 | Yes | kipf_SemiSupervisedClassificationGraph_2017 | Table 1 |
| GAT | 0.5580 | 0.0087 | Yes | velickovic_GraphAttentionNetworks_2018 | Table 1 |
| APPNP | 0.8536 | 0.0062 | Yes | gasteiger_PredictThenPropagate_2018 | Table 1 |
| LINKX | 0.9077 | 0.0027 | Yes | lim_LargeScaleLearning_2021 | Table 1 |
| Nodeformer | 0.8862 | 0.0027 | Yes | this paper | Table 1 |
| SGFormer | 0.8391 | 0.0260 | Yes | this paper | Table 1 |
| nsqure | 0.8932 | 0.0026 | No | this paper | Table 1 |

### IMDB-B — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| PATCHY-SAN | 0.7100 | 0.0229 | Yes | niepert_LearningConvolutionalNeural_2016 | Table 1 |
| GCN | 0.7326 | 0.0046 | Yes | kipf_SemiSupervisedClassificationGraph_2017 | Table 1 |
| PG | 0.7680 | 0.0260 | Yes | huang_GoingDeeperPermutationSensitive_2022 | Table 1 |
| CoCN | 0.7726 | 0.0027 | Yes | sun_AllinARow_2023 | Table 1 |
| GIN | 0.7278 | 0.0086 | Yes | xu*_HowPowerfulAre_2019 | Table 1 |
| GraphSAGE | 0.6880 | 0.0450 | Yes | hamilton_InductiveRepresentationLearning_2017 | Table 1 |
| DiffPool | 0.7314 | 0.0070 | Yes | ying_HierarchicalGraphRepresentation_2018 | Table 1 |
| TopKPool | 0.7158 | 0.0095 | Yes | gao_GraphUNets_2019 | Table 1 |
| SAGPool | 0.7255 | 0.0128 | Yes | lee_SelfAttentionGraphPooling_2019 | Table 1 |
| StructPool | 0.7206 | 0.0064 | Yes | yuan_StructPoolStructuredGraph_2020 | Table 1 |
| SEP | 0.7412 | 0.0056 | Yes | wu_StructuralEntropyGuided_2022 | Table 1 |
| GMT | 0.7348 | 0.0076 | Yes | baek_AccurateLearningGraph_2022 | Table 1 |
| nsquare | 0.7995 | 0.0246 | No | this paper | Table 1 |

### IMDB-M — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| PATCHY-SAN | 0.4523 | 0.0284 | Yes | niepert_LearningConvolutionalNeural_2016 | Table 1 |
| GCN | 0.5039 | 0.0041 | Yes | kipf_SemiSupervisedClassificationGraph_2017 | Table 1 |
| PG | 0.5320 | 0.0360 | Yes | huang_GoingDeeperPermutationSensitive_2022 | Table 1 |
| CoCN | 0.5632 | 0.0018 | Yes | sun_AllinARow_2023 | Table 1 |
| GIN | 0.4813 | 0.0136 | Yes | xu*_HowPowerfulAre_2019 | Table 1 |
| GraphSAGE | 0.4760 | 0.0350 | Yes | hamilton_InductiveRepresentationLearning_2017 | Table 1 |
| DiffPool | 0.5131 | 0.0072 | Yes | ying_HierarchicalGraphRepresentation_2018 | Table 1 |
| TopKPool | 0.4859 | 0.0072 | Yes | gao_GraphUNets_2019 | Table 1 |
| SAGPool | 0.5023 | 0.0044 | Yes | lee_SelfAttentionGraphPooling_2019 | Table 1 |
| StructPool | 0.5023 | 0.0053 | Yes | yuan_StructPoolStructuredGraph_2020 | Table 1 |
| SEP | 0.5153 | 0.0065 | Yes | wu_StructuralEntropyGuided_2022 | Table 1 |
| GMT | 0.5066 | 0.0082 | Yes | baek_AccurateLearningGraph_2022 | Table 1 |
| nsquare | 0.5731 | 0.0219 | No | this paper | Table 1 |

### NCI1 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| PATCHY-SAN | 0.7860 | 0.0190 | Yes | niepert 2016 | Table 1 |
| GCN | 0.7629 | 0.0179 | Yes | kipf 2017 | Table 1 |
| PG | 0.8280 | 0.0130 | Yes | huang 2022 | Table 1 |
| CoCN | 0.8289 | 0.0019 | Yes | sun 2023 | Table 1 |
| GIN | 0.7662 | 0.0180 | Yes | xu* 2019 | Table 1 |
| +pseudo node | 0.7708 | 0.0149 | Yes | liu 2022 | Table 1 |
| GraphSAGE | 0.7382 | 0.0217 | Yes | hamilton 2017 | Table 1 |
| DiffPool | 0.7662 | 0.0193 | Yes | ying 2018 | Table 1 |
| TopKPool | 0.6702 | 0.0225 | Yes | gao 2019 | Table 1 |
| SAGPool | 0.6745 | 0.0111 | Yes | lee 2019 | Table 1 |
| StructPool | 0.7864 | 0.0153 | Yes | yuan 2020 | Table 1 |
| SEP | 0.7935 | 0.0033 | Yes | wu 2022 | Table 1 |
| GMT | 0.7635 | 0.0262 | Yes | baek 2022 | Table 1 |
| nsqure | 0.8352 | 0.0375 | No | this paper | Table 1 |

### OGB-arXiv — accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| SGC | 0.6779 | 0.0027 | Yes | wu_SimplifyingGraphConvolutional_2019 | Table 1 |
| GCN | 0.7174 | 0.0029 | Yes | kipf_SemiSupervisedClassificationGraph_2017 | Table 1 |
| GAT | 0.6763 | 0.0023 | Yes | velickovic_GraphAttentionNetworks_2018 | Table 1 |
| Exphormer | 0.7244 | 0.0028 | Yes | shirzad_ExphormerSparseTransformers_2023 | Table 1 |
| Nodeformer | 0.5990 | 0.0042 | Yes | wu_NodeFormerScalableGraph_2022 | Table 1 |
| SGFormer | 0.7263 | 0.0013 | Yes | wu_SGFormerSimplifyingEmpowering_2023 | Table 1 |
| nsqure | 0.7001 | 0.0065 | No | this paper | Table 1 |

### OGB-proteins — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| SGC | 0.7031 | 0.0023 | Yes | wu_SimplifyingGraphConvolutional_2019 | Table 1 |
| GCN | 0.7251 | 0.0035 | Yes | kipf_SemiSupervisedClassificationGraph_2017 | Table 1 |
| GAT | 0.7463 | 0.0124 | Yes | velickovic_GraphAttentionNetworks_2018 | Table 1 |
| Nodeformer | 0.7745 | 0.0115 | Yes | wu_NodeFormerScalableGraph_2022 | Table 1 |
| SGFormer | 0.7953 | 0.0038 | Yes | wu_SGFormerSimplifyingEmpowering_2023 | Table 1 |
| nsqure | 0.7955 | 0.0079 | No | this paper | Table 1 |

### PROTEIN — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| PATCHY-SAN | 0.7500 | 0.0251 | Yes | niepert_LearningConvolutionalNeural_2016 | Table 1 |
| GCN | 0.7324 | 0.0073 | Yes | kipf_SemiSupervisedClassificationGraph_2017 | Table 1 |
| PG | 0.7680 | 0.0380 | Yes | huang_GoingDeeperPermutationSensitive_2022 | Table 1 |
| CoCN | 0.7686 | 0.0013 | Yes | sun_AllinARow_2023 | Table 1 |
| GIN | 0.7384 | 0.0446 | Yes | xu*_HowPowerfulAre_2019 | Table 1 |
| +pseudo node | 0.7411 | 0.0412 | Yes | liu_BoostingGraphStructure_2022 | Table 1 |
| GraphSAGE | 0.7348 | 0.0566 | Yes | hamilton_InductiveRepresentationLearning_2017 | Table 1 |
| DiffPool | 0.7562 | 0.0517 | Yes | ying_HierarchicalGraphRepresentation_2018 | Table 1 |
| TopKPool | 0.7048 | 0.0101 | Yes | gao_GraphUNets_2019 | Table 1 |
| SAGPool | 0.7156 | 0.0149 | Yes | lee_SelfAttentionGraphPooling_2019 | Table 1 |
| StructPool | 0.7516 | 0.0086 | Yes | yuan_StructPoolStructuredGraph_2020 | Table 1 |
| SEP | 0.7642 | 0.0039 | Yes | wu_StructuralEntropyGuided_2022 | Table 1 |
| GMT | 0.7509 | 0.0059 | Yes | baek_AccurateLearningGraph_2022 | Table 1 |
| nsqure~(Ours) | 0.7753 | 0.0178 | No | this paper | Table 1 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCNII | 34.7100 | — | Yes | this paper | Table ef{tab:app-squashing} |
| GCN | 34.9600 | — | Yes | this paper | Table ef{tab:app-squashing} |
| GINE | 35.4700 | — | Yes | this paper | Table ef{tab:app-squashing} |
| GatedGCN | 33.5700 | — | Yes | this paper | Table ef{tab:app-squashing} |
| SAN | 25.4500 | — | Yes | this paper | Table ef{tab:app-squashing} |
| PathNN | 25.4500 | — | Yes | this paper | Table ef{tab:app-squashing} |
| Drew-GCN | 25.3600 | — | Yes | this paper | Table ef{tab:app-squashing} |
| Exphormer | 24.8100 | — | Yes | this paper | Table ef{tab:app-squashing} |
| squre | 25.1200 | — | No | this paper | Table ef{tab:app-squashing} |

### arXiv-year — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| SGC | 0.3283 | 0.0013 | Yes | wu_SimplifyingGraphConvolutional_2019 | Table 1 |
| GCN | 0.4602 | 0.0026 | Yes | kipf_SemiSupervisedClassificationGraph_2017 | Table 1 |
| GAT | 0.4605 | 0.0051 | Yes | velickovic_GraphAttentionNetworks_2018 | Table 1 |
| APPNP | 0.3815 | 0.0026 | Yes | gasteiger_PredictThenPropagate_2018 | Table 1 |
| H2GCN | 0.4909 | 0.0010 | Yes | zhu_HomophilyGraphNeural_2020 | Table 1 |
| LINKX | 0.5600 | 0.0134 | Yes | lim_LargeScaleLearning_2021 | Table 1 |
| Nodeformer | 0.3768 | 0.0030 | Yes | this paper | Table 1 |
| SGFormer | 0.4434 | 0.0007 | Yes | this paper | Table 1 |
| nsqure | 0.5869 | 0.0042 | No | this paper | Table 1 |

## Baseline Models Identified

- **PATCHY-SAN** (from: niepert_LearningConvolutionalNeural_2016)
- **GCN** (from: kipf_SemiSupervisedClassificationGraph_2017)
- **PG** (from: huang_GoingDeeperPermutationSensitive_2022)
- **CoCN** (from: sun_AllinARow_2023)
- **GIN** (from: xu*_HowPowerfulAre_2019)
- **GIN +pseudo node** (from: liu_BoostingGraphStructure_2022)
- **GraphSAGE** (from: hamilton_InductiveRepresentationLearning_2017)
- **GraphSAGE +pseudo node** (from: liu_BoostingGraphStructure_2022)
- **DiffPool** (from: ying_HierarchicalGraphRepresentation_2018)
- **DiffPool +pseudo node** (from: liu_BoostingGraphStructure_2022)
- **TopKPool** (from: gao_GraphUNets_2019)
- **SAGPool** (from: lee_SelfAttentionGraphPooling_2019)
- **StructPool** (from: yuan_StructPoolStructuredGraph_2020)
- **SEP** (from: wu_StructuralEntropyGuided_2022)
- **GMT** (from: baek_AccurateLearningGraph_2022)
- **SGC** (from: wu_SimplifyingGraphConvolutional_2019)
- **GAT** (from: velickovic_GraphAttentionNetworks_2018)
- **APPNP** (from: gasteiger_PredictThenPropagate_2018)
- **H2GCN** (from: zhu_HomophilyGraphNeural_2020)
- **LINKX** (from: lim_LargeScaleLearning_2021)
- **Graphormer** (from: ying_TransformersReallyPerform_2021)
- **SAN** (from: kreuzer_RethinkingGraphTransformers_2021)
- **GraphGPS** (from: rampasek_RecipeGeneralPowerful_2022)
- **Exphormer** (from: shirzad_ExphormerSparseTransformers_2023)
- **Nodeformer** (from: wu_NodeFormerScalableGraph_2022)
- **SGFormer** (from: wu_SGFormerSimplifyingEmpowering_2023)
- **GCNII**
- **GINE**
- **GatedGCN**
- **PathNN**
- **Drew-GCN**

## Extraction Notes

[PROTEIN] Extracted results for PROTEIN dataset from Table 1. Normalized percentage values to [0, 1]
range. Handled pseudo-node variants as separate baseline rows as they appear in the table. [NCI1]
Extracted only NCI1 results as requested. Normalized percentages to [0, 1] range. Handled pseudo-
node variants as separate baseline entries. [IMDB-B] Extracted only IMDB-B results as requested.
Normalized percentages to [0, 1] range. [IMDB-M] Extracted results for IMDB-M from Table 1. Values
were converted from percentages to decimals. Pseudo-node variants for GIN, GraphSAGE, and DiffPool
were skipped as they had no reported values for IMDB-M. [COLLAB] Extracted only COLLAB dataset
results as requested. Normalized percentages to [0, 1] range. Pseudo-node variants for GIN,
GraphSAGE, and DiffPool were skipped for COLLAB as they contained no values ('-') in the table.
[Genius] Extracted only Genius dataset results. OOM (Out of Memory) values were skipped as they are
not quantitative results. Reproduced results for Nodeformer and SGFormer are marked as 'this paper'
per source_ref logic since they were reproduced by the authors. [arXiv-year] Extracted only arXiv-
year results as requested. Normalised percentages to [0, 1]. Nodeformer and SGFormer are marked as
reproduced in the text, so source_ref is 'this paper'. [OGB-arXiv] Extracted only OGB-arXiv results
as requested. Normalized percentages to [0, 1]. OOM and empty cells were skipped. [OGB-proteins]
Extracted only OGB-proteins results as requested. Values were converted from percentages to
decimals. Models marked as OOM or empty in the OGB-proteins column were excluded from the results
list. [Peptides-struct] Extracted MAE values for Peptides-struct from the provided table. Model
'squre' is identified as the proposed model.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*