# Extraction: arXiv:2206.08164
**Model used**: `glm-4.7`  **Date**: 2026-05-07  **Confidence**: HIGH

## Proposed Model: LRGB
- Type: Other

## Main Figure: Figure 1
> Molecule with LRIs (dotted lines showing 3D atomic contact) that are not trivially captured by the graph structure.
- This figure visually illustrates the core concept of the paper—Long Range Interactions (LRI)—by showing a molecule where relevant connections (dotted lines) exist beyond the immediate graph structure, which is the fundamental problem the benchmark aims to address.

## Results

### COCO-SP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.0841 | 0.0010 | Yes | this paper | Table 3 |
| GCNII | 0.1404 | 0.0011 | Yes | this paper | Table 3 |
| GINE | 0.1339 | 0.0044 | Yes | this paper | Table 3 |
| GatedGCN | 0.2641 | 0.0045 | Yes | this paper | Table 3 |
| GatedGCN+LapPE | 0.2574 | 0.0034 | Yes | this paper | Table 3 |
| Transformer+LapPE | 0.2618 | 0.0031 | Yes | this paper | Table 3 |
| SAN+LapPE | 0.2592 | 0.0158 | Yes | this paper | Table 3 |
| SAN+RWSE | 0.2434 | 0.0156 | Yes | this paper | Table 3 |

### PCQM-Contact — Hits@1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.1321 | 0.0007 | Yes | this paper | Table 5 |
| GCN | 0.3791 | 0.0004 | Yes | this paper | Table 5 |
| GCN | 0.8256 | 0.0006 | Yes | this paper | Table 5 |
| GCN | 0.3234 | 0.0006 | Yes | this paper | Table 5 |
| GCNII | 0.1325 | 0.0009 | Yes | this paper | Table 5 |
| GCNII | 0.3607 | 0.0003 | Yes | this paper | Table 5 |
| GCNII | 0.8116 | 0.0009 | Yes | this paper | Table 5 |
| GCNII | 0.3161 | 0.0004 | Yes | this paper | Table 5 |
| GINE | 0.1337 | 0.0013 | Yes | this paper | Table 5 |
| GINE | 0.3642 | 0.0043 | Yes | this paper | Table 5 |
| GINE | 0.8147 | 0.0062 | Yes | this paper | Table 5 |
| GINE | 0.3180 | 0.0027 | Yes | this paper | Table 5 |
| GatedGCN | 0.1279 | 0.0018 | Yes | this paper | Table 5 |
| GatedGCN | 0.3783 | 0.0004 | Yes | this paper | Table 5 |
| GatedGCN | 0.8433 | 0.0011 | Yes | this paper | Table 5 |
| GatedGCN | 0.3218 | 0.0011 | Yes | this paper | Table 5 |
| GatedGCN+RWSE | 0.1288 | 0.0013 | Yes | this paper | Table 5 |
| GatedGCN+RWSE | 0.3808 | 0.0006 | Yes | this paper | Table 5 |
| GatedGCN+RWSE | 0.8517 | 0.0005 | Yes | this paper | Table 5 |
| GatedGCN+RWSE | 0.3242 | 0.0008 | Yes | this paper | Table 5 |
| Transformer+LapPE | 0.1221 | 0.0011 | Yes | this paper | Table 5 |
| Transformer+LapPE | 0.3679 | 0.0033 | Yes | this paper | Table 5 |
| Transformer+LapPE | 0.8517 | 0.0039 | Yes | this paper | Table 5 |
| Transformer+LapPE | 0.3174 | 0.0020 | Yes | this paper | Table 5 |
| SAN+LapPE | 0.1355 | 0.0017 | Yes | this paper | Table 5 |
| SAN+LapPE | 0.4004 | 0.0021 | Yes | this paper | Table 5 |
| SAN+LapPE | 0.8478 | 0.0044 | Yes | this paper | Table 5 |
| SAN+LapPE | 0.3350 | 0.0003 | Yes | this paper | Table 5 |
| SAN+RWSE | 0.1312 | 0.0016 | Yes | this paper | Table 5 |
| SAN+RWSE | 0.4030 | 0.0008 | Yes | this paper | Table 5 |
| SAN+RWSE | 0.8550 | 0.0024 | Yes | this paper | Table 5 |
| SAN+RWSE | 0.3341 | 0.0006 | Yes | this paper | Table 5 |

### PascalVOC-SP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.1268 | 0.0060 | Yes | this paper | Table 3 |
| GCNII | 0.1698 | 0.0080 | Yes | this paper | Table 3 |
| GINE | 0.1265 | 0.0076 | Yes | this paper | Table 3 |
| GatedGCN | 0.2873 | 0.0219 | Yes | this paper | Table 3 |
| GatedGCN+LapPE | 0.2860 | 0.0085 | Yes | this paper | Table 3 |
| Transformer+LapPE | 0.2694 | 0.0098 | Yes | this paper | Table 3 |
| SAN+LapPE | 0.3230 | 0.0039 | Yes | this paper | Table 3 |
| SAN+RWSE | 0.3216 | 0.0027 | Yes | this paper | Table 3 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5930 | 0.0023 | Yes | this paper | Table 4 |
| GCNII | 0.5543 | 0.0078 | Yes | this paper | Table 4 |
| GINE | 0.5498 | 0.0079 | Yes | this paper | Table 4 |
| GatedGCN | 0.5864 | 0.0077 | Yes | this paper | Table 4 |
| GatedGCN+RWSE | 0.6069 | 0.0035 | Yes | this paper | Table 4 |
| Transformer+LapPE | 0.6326 | 0.0126 | Yes | this paper | Table 4 |
| SAN+LapPE | 0.6384 | 0.0121 | Yes | this paper | Table 4 |
| SAN+RWSE | 0.6439 | 0.0075 | Yes | this paper | Table 4 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3496 | 0.0013 | Yes | this paper | Table 4 |
| GCNII | 0.3471 | 0.0010 | Yes | this paper | Table 4 |
| GINE | 0.3547 | 0.0045 | Yes | this paper | Table 4 |
| GatedGCN | 0.3420 | 0.0013 | Yes | this paper | Table 4 |
| GatedGCN+RWSE | 0.3357 | 0.0006 | Yes | this paper | Table 4 |
| Transformer+LapPE | 0.2529 | 0.0016 | Yes | this paper | Table 4 |
| SAN+LapPE | 0.2683 | 0.0043 | Yes | this paper | Table 4 |
| SAN+RWSE | 0.2545 | 0.0012 | Yes | this paper | Table 4 |

## Baseline Models Identified

- **GCN**, 0.5M params (from: Kipf and Welling 2017)
- **GCNII**, 0.5M params (from: Chen et al. 2020)
- **GINE**, 0.5M params (from: Xu et al. 2019)
- **GatedGCN**, 0.5M params (from: Bresson and Laurent 2017)
- **GatedGCN+LapPE**, 0.5M params (from: Bresson and Laurent 2017)
- **Transformer+LapPE**, 0.5M params (from: Dwivedi et al. 2020)
- **SAN+LapPE**, 0.5M params (from: Kreuzer et al. 2021)
- **SAN+RWSE**, 0.5M params (from: Kreuzer et al. 2021)
- **GatedGCN+RWSE**, 0.5M params (from: Bresson and Laurent 2017)

## Extraction Notes

The paper presents a benchmark suite (LRGB) rather than a single proposed model. Therefore,
'proposed_model' is set to the benchmark name. All results are extracted from Tables 3, 4, and 5.
Standard deviations were parsed from the '±' notation. Parameter counts were taken from the '#
Params' column in the tables.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*