# Extraction: arXiv:2406.04377
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: GAT-Mamba (0.1M params)
- Type: GNN

## Results

### NLST — C-index ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 0.6590 | 0.0189 | Yes | this paper | Table 2 |
| AttentionMIL | 0.6530 | 0.0211 | Yes | this paper | Table 2 |
| TransMIL | 0.6730 | 0.0291 | Yes | this paper | Table 2 |
| PatchGCN | 0.6160 | 0.0502 | Yes | this paper | Table 2 |
| GTP | 0.6750 | 0.0242 | Yes | this paper | Table 2 |
| Clinical | 0.6080 | 0.0331 | Yes | this paper | Table 2 |
| GAT-Mamba | 0.7000 | 0.0228 | No | this paper | Table 2 |
| GAT | 0.6750 | 0.0304 | Yes | this paper | Table 3 |
| Mamba | 0.6800 | 0.0267 | Yes | this paper | Table 3 |
| GAT-Transformer | 0.6760 | 0.0430 | Yes | this paper | Table 3 |
| GAT-MambaNoE | 0.6910 | 0.0311 | Yes | this paper | Table 3 |
| GAT-MambaNoX_PE | 0.6870 | 0.0447 | Yes | this paper | Table 3 |
| HandCrafted | 0.6290 | 0.0427 | Yes | this paper | Table 4 |
| LUADDeep | 0.6350 | 0.0357 | Yes | this paper | Table 4 |
| ResNet50IN | 0.6690 | 0.0297 | Yes | this paper | Table 4 |
| CONCH | 0.6830 | 0.0377 | Yes | this paper | Table 4 |
| PLIP | 0.6840 | 0.0353 | Yes | this paper | Table 4 |
| UNI | 0.7000 | 0.0228 | Yes | this paper | Table 4 |

### TCGA — C-index ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 0.6590 | 0.0189 | Yes | this paper | Table 2 |
| AttentionMIL | 0.6530 | 0.0211 | Yes | this paper | Table 2 |
| TransMIL | 0.6730 | 0.0291 | Yes | this paper | Table 2 |
| PatchGCN | 0.6160 | 0.0502 | Yes | this paper | Table 2 |
| GTP | 0.6750 | 0.0242 | Yes | this paper | Table 2 |
| Clinical | 0.6080 | 0.0331 | Yes | this paper | Table 2 |
| GAT-Mamba | 0.7000 | 0.0228 | No | this paper | Table 2 |
| GAT | 0.6750 | 0.0304 | Yes | this paper | Table 3 |
| Mamba | 0.6800 | 0.0267 | Yes | this paper | Table 3 |
| GAT-Transformer | 0.6760 | 0.0430 | Yes | this paper | Table 3 |
| GAT-MambaNoE | 0.6910 | 0.0311 | Yes | this paper | Table 3 |
| GAT-MambaNoX_PE | 0.6870 | 0.0447 | Yes | this paper | Table 3 |
| HandCrafted | 0.6290 | 0.0427 | Yes | this paper | Table 4 |
| LUADDeep | 0.6350 | 0.0357 | Yes | this paper | Table 4 |
| ResNet50IN | 0.6690 | 0.0297 | Yes | this paper | Table 4 |
| CONCH | 0.6830 | 0.0377 | Yes | this paper | Table 4 |
| PLIP | 0.6840 | 0.0353 | Yes | this paper | Table 4 |
| UNI | 0.7000 | 0.0228 | Yes | this paper | Table 4 |

## Baseline Models Identified

- **MLP**, 0.1M params
- **AttentionMIL**, 0.1M params
- **TransMIL**, 0.1M params
- **PatchGCN**, 0.1M params
- **GTP**, 0.1M params
- **Clinical**, 0.0M params
- **GAT**, 0.1M params
- **Mamba**, 0.1M params
- **GAT-Transformer**, 0.1M params
- **GAT-MambaNoE**, 0.1M params
- **GAT-MambaNoX_PE**, 0.1M params
- **HandCrafted**
- **LUADDeep**
- **ResNet50IN**
- **CONCH**
- **PLIP**
- **UNI**

## Extraction Notes

[NLST] Extracted C-index results for the NLST dataset from Tables 2, 3, and 4. Table 2 compares GAT-
Mamba against other MIL/GNN baselines. Table 3 shows ablation studies on model architecture. Table 4
shows ablation studies on node features. Note that UNI in Table 4 appears to have identical metrics
to GAT-Mamba in Tables 2 and 3 (0.700 ± 0.0228), suggesting UNI might be the feature extractor used
in the final GAT-Mamba model or there is a reporting overlap. I have extracted them as separate rows
as they are listed as distinct 'Models' or 'Features' in the tables. 'uses_external_data' is set to
true for CONCH, PLIP, and UNI as these are pre-trained vision-language models. [TCGA] Extracted
C-index results for the TCGA dataset from Tables 2, 3, and 4. Table 2 contains main baselines and
the proposed model. Table 3 contains ablation variants of the proposed model. Table 4 contains node
feature ablation studies. Note that UNI in Table 4 appears to have identical stats to GAT-Mamba in
Table 2/3, likely indicating UNI is the feature extractor used for GAT-Mamba, but it is listed as a
separate row in the feature ablation table. All values are normalized to [0,1].

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*