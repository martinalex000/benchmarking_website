# Extraction: Where Did the Gap Go? Reassessing the Long-Range Graph Benchmark
**Model used**: `glm-4.7`  **Date**: 2026-05-08  **Confidence**: HIGH

## Proposed Model: GCN (0.5M params)
- Type: GCN_variant

## Main Figure: Figure 1
> On both Peptides datasets, all three MPGNNs surpass GPS. On Peptides-Struct a basic
- Figure 1 is the main figure because it visually summarizes the core empirical finding of the paper: that with proper hyperparameter tuning, Message Passing GNNs (MPGNNs) can match or outperform Graph Transformers (GPS) on the Long-Range Graph Benchmark, directly challenging the premise of the original benchmark.

## Results

### COCO-SP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.1338 | 0.0007 | No | this paper | Table 2a |
| GINE | 0.2125 | 0.0009 | Yes | this paper | Table 2a |
| GatedGCN | 0.2922 | 0.0018 | Yes | this paper | Table 2a |
| GPS | 0.3884 | 0.0055 | Yes | this paper | Table 2a |
| Exphormer | 0.3430 | 0.0008 | Yes | Shirzad et al. 2023 | Table 2a |

### PCQM-Contact — MRR ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3424 | 0.0007 | No | this paper | Figure 3 |
| GCN | 0.3631 | 0.0006 | No | this paper | Figure 3 |
| GCN | 0.4526 | 0.0006 | No | this paper | Figure 3 |
| GINE | 0.3509 | 0.0006 | Yes | this paper | Figure 3 |
| GINE | 0.3725 | 0.0006 | Yes | this paper | Figure 3 |
| GINE | 0.4617 | 0.0005 | Yes | this paper | Figure 3 |
| GatedGCN | 0.3495 | 0.0010 | Yes | this paper | Figure 3 |
| GatedGCN | 0.3714 | 0.0010 | Yes | this paper | Figure 3 |
| GatedGCN | 0.4670 | 0.0004 | Yes | this paper | Figure 3 |
| GPS | 0.3498 | 0.0005 | Yes | this paper | Figure 3 |
| GPS | 0.3722 | 0.0005 | Yes | this paper | Figure 3 |
| GPS | 0.4703 | 0.0014 | Yes | this paper | Figure 3 |

### PascalVOC-SP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.2078 | 0.0031 | No | this paper | Table 2a |
| GINE | 0.2718 | 0.0054 | Yes | this paper | Table 2a |
| GatedGCN | 0.3880 | 0.0040 | Yes | this paper | Table 2a |
| GPS | 0.4440 | 0.0065 | Yes | this paper | Table 2a |
| CRAWL | 0.4588 | 0.0079 | Yes | Tönshoff et al. 2021 | Table 2a |
| DREW | 0.3314 | 0.0024 | Yes | Gutteridge et al. 2023 | Table 2a |
| Exphormer | 0.3960 | 0.0027 | Yes | Shirzad et al. 2023 | Table 2a |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.6860 | 0.0050 | No | this paper | Table 1a |
| GINE | 0.6621 | 0.0067 | Yes | this paper | Table 1a |
| GatedGCN | 0.6765 | 0.0047 | Yes | this paper | Table 1a |
| GPS | 0.6534 | 0.0091 | Yes | this paper | Table 1a |
| CRAWL | 0.7074 | 0.0032 | Yes | Tönshoff et al. 2021 | Table 1a |
| DREW | 0.7150 | 0.0044 | Yes | Gutteridge et al. 2023 | Table 1a |
| Exphormer | 0.6527 | 0.0043 | Yes | Shirzad et al. 2023 | Table 1a |
| GRIT | 0.6988 | 0.0082 | Yes | Ma et al. 2023 | Table 1a |
| Graph ViT | 0.6942 | 0.0075 | Yes | He et al. 2023 | Table 1a |
| G-MLPMixer | 0.6921 | 0.0054 | Yes | He et al. 2023 | Table 1a |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.2460 | 0.0007 | No | this paper | Table 1a |
| GINE | 0.2473 | 0.0017 | Yes | this paper | Table 1a |
| GatedGCN | 0.2477 | 0.0009 | Yes | this paper | Table 1a |
| GPS | 0.2509 | 0.0014 | Yes | this paper | Table 1a |
| CRAWL | 0.2506 | 0.0022 | Yes | Tönshoff et al. 2021 | Table 1a |
| DREW | 0.2536 | 0.0015 | Yes | Gutteridge et al. 2023 | Table 1a |
| Exphormer | 0.2481 | 0.0007 | Yes | Shirzad et al. 2023 | Table 1a |
| GRIT | 0.2460 | 0.0012 | Yes | Ma et al. 2023 | Table 1a |
| Graph ViT | 0.2449 | 0.0016 | Yes | He et al. 2023 | Table 1a |
| G-MLPMixer | 0.2475 | 0.0015 | Yes | He et al. 2023 | Table 1a |

## Baseline Models Identified

- **GINE**, 0.5M params (from: Hu et al. 2020)
- **GatedGCN**, 0.5M params (from: Bresson and Laurent 2017)
- **GPS**, 0.5M params (from: Rampášek et al. 2022)
- **Transformer** (from: Dwivedi et al. 2022)
- **SAN** (from: Dwivedi et al. 2022)
- **CRAWL** (from: Tönshoff et al. 2021)
- **DREW** (from: Gutteridge et al. 2023)
- **Exphormer** (from: Shirzad et al. 2023)
- **GRIT** (from: Ma et al. 2023)
- **Graph ViT** (from: He et al. 2023)
- **G-MLPMixer** (from: He et al. 2023)

## Extraction Notes

The paper presents results for multiple models across LRGB datasets. The 'proposed_model' is set to
GCN as the paper highlights its strong performance after tuning, though the paper is primarily a
reassessment of baselines rather than proposing a single new architecture. Results for PCQM-Contact
are extracted from Figure 3, which presents MRR under three filtering conditions (Raw, Filter, Ext.
Filter). The values were estimated from the bar chart in Figure 3 and verified against the summary
in Table 6 where available. Table 6 provides the exact numbers for the 'OURS' section, which were
used to populate the results.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*