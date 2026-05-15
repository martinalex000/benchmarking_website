# Extraction: arXiv:2412.01519
**Model used**: `MiniMaxAI/MiniMax-M2.5`  **Date**: 2026-05-13  **Confidence**: HIGH

## Proposed Model: ReHub
- Type: GNN

## Results

### PCQM-Contact — MRR ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.2329 | 0.0009 | Yes | this paper | Table lrgb-vs-na |
| + NeuralAtoms | 0.2534 | 0.0200 | Yes | this paper | Table lrgb-vs-na |
| + ReHub-FC | 0.3492 | 0.0012 | No | this paper | Table lrgb-vs-na |
| + ReHub | 0.3469 | 0.0014 | No | this paper | Table lrgb-vs-na |
| GCN2 | 0.3161 | 0.0004 | Yes | this paper | Table lrgb-vs-na |
| GINE | 0.3180 | 0.0027 | Yes | this paper | Table lrgb-vs-na |
| GatedGCN | 0.3218 | 0.0011 | Yes | this paper | Table lrgb-vs-na |
| GatedGCN+RWSE | 0.3242 | 0.0008 | Yes | this paper | Table lrgb-vs-na |
| Transformer+LapPE | 0.3174 | 0.0020 | Yes | this paper | Table tab:lrgb-baseline |
| SAN+LapPE | 0.3350 | 0.0003 | Yes | this paper | Table tab:lrgb-baseline |
| GraphGPS | 0.3337 | 0.0006 | Yes | this paper | Table tab:lrgb-baseline |
| Exphormer | 0.3637 | 0.0020 | Yes | this paper | Table tab:lrgb-baseline |
| NeuralAtoms | 0.3262 | 0.0010 | Yes | this paper | Table tab:lrgb-baseline |
| ReHub-FC (Ours) | 0.3526 | 0.0014 | No | this paper | Table tab:lrgb-baseline |
| ReHub (Ours) | 0.3534 | 0.0014 | No | this paper | Table tab:lrgb-baseline |

### PascalVOC-SP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Transformer+LapPE | 0.2694 | 0.0098 | Yes | this paper | Table 1 |
| SAN+LapPE | 0.3230 | 0.0039 | Yes | this paper | Table 1 |
| GraphGPS | 0.3748 | 0.0109 | Yes | rampavsek2022recipe | Table 1 |
| Exphormer | 0.3975 | 0.0037 | Yes | shirzad2023exphormer | Table 1 |
| ReHub-FC (Ours) | 0.3526 | 0.0045 | No | this paper | Table 1 |
| ReHub (Ours) | 0.3860 | 0.0172 | No | this paper | Table 1 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5930 | 0.0023 | Yes | this paper | Table lrgb-vs-na |
| + NeuralAtoms | 0.6220 | 0.0046 | Yes | li2024neural | Table lrgb-vs-na |
| + ReHub-FC | 0.6663 | 0.0053 | No | this paper | Table lrgb-vs-na |
| + ReHub | 0.6656 | 0.0043 | No | this paper | Table lrgb-vs-na |
| GCN2 | 0.5543 | 0.0078 | Yes | this paper | Table lrgb-vs-na |
| GINE | 0.5498 | 0.0079 | Yes | this paper | Table lrgb-vs-na |
| GatedGCN | 0.5864 | 0.0077 | Yes | this paper | Table lrgb-vs-na |
| GatedGCN+RWSE | 0.6069 | 0.0035 | Yes | this paper | Table lrgb-vs-na |
| Transformer+LapPE | 0.6326 | 0.0126 | Yes | this paper | Table tab:lrgb-baseline |
| SAN+LapPE | 0.6384 | 0.0121 | Yes | this paper | Table tab:lrgb-baseline |
| GraphGPS | 0.6535 | 0.0041 | Yes | rampavsek2022recipe | Table tab:lrgb-baseline |
| Exphormer | 0.6527 | 0.0043 | Yes | shirzad2023exphormer | Table tab:lrgb-baseline |
| NeuralAtoms | 0.6591 | 0.0050 | Yes | li2024neural | Table tab:lrgb-baseline |
| ReHub-FC (Ours) | 0.6732 | 0.0107 | No | this paper | Table tab:lrgb-baseline |
| ReHub (Ours) | 0.6685 | 0.0074 | No | this paper | Table tab:lrgb-baseline |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3496 | 0.0013 | Yes | this paper | Table lrgb-vs-na |
| + NeuralAtoms | 0.2606 | 0.0027 | Yes | this paper | Table lrgb-vs-na |
| + ReHub-FC | 0.2489 | 0.0011 | No | this paper | Table lrgb-vs-na |
| + ReHub | 0.2497 | 0.0021 | No | this paper | Table lrgb-vs-na |
| GCN2 | 0.3471 | 0.0010 | Yes | this paper | Table lrgb-vs-na |
| GINE | 0.3547 | 0.0045 | Yes | this paper | Table lrgb-vs-na |
| GatedGCN | 0.3420 | 0.0013 | Yes | this paper | Table lrgb-vs-na |
| GatedGCN+RWSE | 0.3357 | 0.0006 | Yes | this paper | Table lrgb-vs-na |
| Transformer+LapPE | 0.2529 | 0.0016 | Yes | this paper | Table tab:lrgb-baseline |
| SAN+LapPE | 0.2683 | 0.0043 | Yes | this paper | Table tab:lrgb-baseline |
| GraphGPS | 0.2500 | 0.0005 | Yes | this paper | Table tab:lrgb-baseline |
| Exphormer | 0.2481 | 0.0007 | Yes | this paper | Table tab:lrgb-baseline |
| NeuralAtoms | 0.2553 | 0.0005 | Yes | this paper | Table tab:lrgb-baseline |
| ReHub-FC (Ours) | 0.2489 | 0.0011 | No | this paper | Table tab:lrgb-baseline |
| ReHub (Ours) | 0.2488 | 0.0017 | No | this paper | Table tab:lrgb-baseline |

## Baseline Models Identified

- **GCN**
- **NeuralAtoms** (from: li2024neural)
- **GCN2**
- **GINE**
- **GatedGCN**
- **GatedGCN+RWSE**
- **Transformer+LapPE**
- **SAN+LapPE**
- **GraphGPS** (from: rampavsek2022recipe)
- **Exphormer** (from: shirzad2023exphormer)

## Extraction Notes

[Peptides-func] Extracted all AP results for Peptides-func from the modularity table, baseline
table, and ablation table. Ablation results were omitted as they represent specific configuration
variants rather than the standard model performance. [Peptides-struct] Extracted all MAE results for
Peptides-struct from both the modularity table (lrgb-vs-na) and the baseline table (tab:lrgb-
baseline). The modularity table contains multiple GNN backbones paired with NeuralAtoms and ReHub
variants. [PCQM-Contact] Extracted all MRR results for PCQM-Contact from both provided tables. The
first table shows ReHub and NeuralAtoms as modular additions to various GNN backbones, while the
second table compares them as standalone models against other baselines. [PascalVOC-SP] Extracted
only the main benchmark results from Table 1 as requested. Ablation tables (Table 2 and 3) were
skipped as they represent non-standard configurations/variants of the proposed model rather than the
default benchmark performance. [Coauthor Physics] failed: 1 validation error for ExtractionOutput
results.0.value   Input should be a valid number [type=float_type, input_value=None,
input_type=NoneType]     For further information visit https://errors.pydantic.dev/2.13/v/float_type
[OGBN-Arxiv] failed: 1 validation error for ExtractionOutput results.0.value   Input should be a
valid number [type=float_type, input_value=None, input_type=NoneType]     For further information
visit https://errors.pydantic.dev/2.13/v/float_type

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*