# Extraction: k-Maximum Inner Product Attention for Graph Transformers and the Expressive Power of GraphGPS
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-11  **Confidence**: HIGH

## Proposed Model: GPS + k-MIP (ours)
- Type: GraphTransformer

## Results

### COCO-SP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 13.3800 | 0.0700 | Yes | Tonshoff 2023 | Table 1 |
| GINE | 21.2500 | 0.0900 | Yes | Tonshoff 2023 | Table 1 |
| GAT | 18.8600 | 0.1100 | Yes | this paper | Table 1 |
| GatedGCN | 29.2200 | 0.1800 | Yes | Tonshoff 2023 | Table 1 |
| GPS + BigBird | 35.2500 | 0.2700 | Yes | this paper | Table 1 |
| GPS + Performer | 27.7000 | 0.2700 | Yes | this paper | Table 1 |
| GPS + Transformer | 38.8400 | 0.5500 | Yes | Tonshoff 2023 | Table 1 |
| Exphormer | 34.5500 | 0.0900 | Yes | Shirzad 2023 | Table 1 |
| GPS + k-MIP | 35.5600 | 0.4500 | No | this paper | Table 1 |

### Cifar10 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GraphGPS with k-MIP attention (k=1) | 74.3700 | 0.5600 | No | this paper | Table 1 |
| GraphGPS with k-MIP attention (k=2) | 74.8400 | 0.4100 | No | this paper | Table 1 |
| GraphGPS with k-MIP attention (k=3) | 74.7500 | 0.3300 | No | this paper | Table 1 |
| GraphGPS with k-MIP attention (k=5) | 75.0800 | 0.2700 | No | this paper | Table 1 |
| GraphGPS with k-MIP attention (k=10) | 75.0500 | 0.3200 | No | this paper | Table 1 |
| GraphGPS with k-MIP attention (k=20) | 75.1200 | 0.3100 | No | this paper | Table 1 |
| GraphGPS with k-MIP attention (k=30) | 75.0800 | 0.4800 | No | this paper | Table 1 |
| GraphGPS with k-MIP attention (k=50) | 75.5000 | 0.4300 | No | this paper | Table 1 |
| GraphGPS with k-MIP attention (k=100) | 75.6500 | 0.4400 | No | this paper | Table 1 |

### MalNet-Tiny — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GraphGPS with k-MIP attention (k=1) | 93.0000 | 0.5800 | No | this paper | Table 1 |
| GraphGPS with k-MIP attention (k=2) | 92.9200 | 0.6900 | No | this paper | Table 1 |
| GraphGPS with k-MIP attention (k=3) | 92.8800 | 0.4100 | No | this paper | Table 1 |
| GraphGPS with k-MIP attention (k=5) | 93.5400 | 0.5200 | No | this paper | Table 1 |
| GraphGPS with k-MIP attention (k=10) | 93.5200 | 0.4900 | No | this paper | Table 1 |
| GraphGPS with k-MIP attention (k=20) | 93.2600 | 0.4500 | No | this paper | Table 1 |
| GraphGPS with k-MIP attention (k=30) | 92.6200 | 0.7000 | No | this paper | Table 1 |
| GraphGPS with k-MIP attention (k=50) | 92.7800 | 0.7500 | No | this paper | Table 1 |
| GraphGPS with k-MIP attention (k=100) | 93.4000 | 0.5700 | No | this paper | Table 1 |

### PascalVOC-SP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 20.7800 | 0.3100 | Yes | Tonshoff 2023 | Table 1 |
| GINE | 27.1800 | 0.5400 | Yes | Tonshoff 2023 | Table 1 |
| GAT | 27.1500 | 0.4900 | Yes | this paper | Table 1 |
| GatedGCN | 38.8000 | 0.4000 | Yes | Tonshoff 2023 | Table 1 |
| GPS + BigBird | 38.7500 | 0.6400 | Yes | this paper | Table 1 |
| GPS + Performer | 37.9200 | 1.1300 | Yes | this paper | Table 1 |
| GPS + Transformer | 44.4000 | 0.6500 | Yes | Tonshoff 2023 | Table 1 |
| Exphormer | 39.7500 | 0.3700 | Yes | Shirzad 2023 | Table 1 |
| GPS + k-MIP (ours) | 39.6900 | 0.9200 | No | this paper | Table 1 |
| GraphGPS + k-MIP (k=1) | 35.5700 | 1.0600 | Yes | this paper | Table 2 |
| GraphGPS + k-MIP (k=2) | 37.6500 | 0.7000 | Yes | this paper | Table 2 |
| GraphGPS + k-MIP (k=3) | 37.4700 | 0.4800 | Yes | this paper | Table 2 |
| GraphGPS + k-MIP (k=5) | 37.3000 | 0.9900 | Yes | this paper | Table 2 |
| GraphGPS + k-MIP (k=10) | 36.5800 | 1.5000 | Yes | this paper | Table 2 |
| GraphGPS + k-MIP (k=20) | 35.8000 | 1.6000 | Yes | this paper | Table 2 |
| GraphGPS + k-MIP (k=30) | 37.1500 | 0.7300 | Yes | this paper | Table 2 |
| GraphGPS + k-MIP (k=50) | 36.8200 | 0.4300 | Yes | this paper | Table 2 |
| GraphGPS + k-MIP (k=100) | 36.9000 | 0.3300 | Yes | this paper | Table 2 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 68.6000 | 0.5000 | Yes | Tonshoff 2023 | Table 1 |
| GINE | 66.2100 | 0.6700 | Yes | Tonshoff 2023 | Table 1 |
| GAT | 67.8700 | 0.5600 | Yes | this paper | Table 1 |
| GatedGCN | 67.6500 | 0.4700 | Yes | Tonshoff 2023 | Table 1 |
| GPS + BigBird | 64.8300 | 0.7300 | Yes | this paper | Table 1 |
| GPS + Performer | 66.0600 | 0.6400 | Yes | this paper | Table 1 |
| GPS + Transformer | 65.3400 | 0.9100 | Yes | Tonshoff 2023 | Table 1 |
| Exphormer | 65.2700 | 0.4300 | Yes | Shirzad 2023 | Table 1 |
| GPS + k-MIP (ours) | 66.2700 | 0.4400 | No | this paper | Table 1 |
| GPS + k-MIP (k=1) | 60.6400 | 1.1300 | No | this paper | Table 2 |
| GPS + k-MIP (k=2) | 62.9700 | 0.2700 | No | this paper | Table 2 |
| GPS + k-MIP (k=3) | 63.1300 | 0.6500 | No | this paper | Table 2 |
| GPS + k-MIP (k=5) | 64.6500 | 0.3700 | No | this paper | Table 2 |
| GPS + k-MIP (k=10) | 65.1000 | 0.4200 | No | this paper | Table 2 |
| GPS + k-MIP (k=20) | 65.3100 | 0.5200 | No | this paper | Table 2 |
| GPS + k-MIP (k=30) | 65.1400 | 0.7600 | No | this paper | Table 2 |
| GPS + k-MIP (k=50) | 64.9000 | 0.8400 | No | this paper | Table 2 |
| GPS + k-MIP (k=100) | 65.2900 | 0.3400 | No | this paper | Table 2 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.2460 | 0.0007 | Yes | Tonshoff 2023 | Table 1 |
| GINE | 0.2473 | 0.0017 | Yes | Tonshoff 2023 | Table 1 |
| GAT | 0.2488 | 0.0018 | Yes | this paper | Table 1 |
| GatedGCN | 0.2477 | 0.0009 | Yes | Tonshoff 2023 | Table 1 |
| GPS + BigBird | 0.2566 | 0.0019 | Yes | this paper | Table 1 |
| GPS + Performer | 0.2643 | 0.0008 | Yes | this paper | Table 1 |
| GPS + Transformer | 0.2509 | 0.0014 | Yes | Tonshoff 2023 | Table 1 |
| Exphormer | 0.2481 | 0.0007 | Yes | Shirzad 2023 | Table 1 |
| GPS + k-MIP | 0.2562 | 0.0037 | No | this paper | Table 1 |

### ShapeNet-Part — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 60.1800 | 0.0400 | Yes | this paper | Table 1 |
| GINE | 64.5700 | 0.3500 | Yes | this paper | Table 1 |
| GAT | 63.0100 | 0.1700 | Yes | this paper | Table 1 |
| GatedGCN | 76.2000 | 0.3200 | Yes | this paper | Table 1 |
| GPS + BigBird | 79.6500 | 0.9800 | Yes | this paper | Table 1 |
| GPS + Performer | 77.3600 | 1.2300 | Yes | this paper | Table 1 |
| Exphormer | 82.6200 | 0.3100 | Yes | this paper | Table 1 |
| GPS + k-MIP | 82.6800 | 0.6400 | No | this paper | Table 1 |

## Baseline Models Identified

- **GCN** (from: Tonshoff 2023)
- **GINE** (from: Tonshoff 2023)
- **GAT** (from: this paper)
- **GatedGCN** (from: Tonshoff 2023)
- **GPS + BigBird** (from: this paper)
- **GPS + Performer** (from: this paper)
- **GPS + Transformer** (from: Tonshoff 2023)
- **Exphormer** (from: Shirzad 2023)

## Extraction Notes

[PascalVOC-SP] Extracted all rows for PascalVOC-SP from Table 1 and Table 2. Table 1 contains the
main comparison with baselines. Table 2 contains ablation results for varying k values of the
proposed k-MIP attention mechanism. The primary metric F1 was used. All values are test set results
as indicated by table captions. [COCO-SP] Extracted only COCO-SP F1 results from Table 1. All values
are mean ± std over four runs. The proposed model is 'GPS + k-MIP (ours)'. [Peptides-func] Extracted
results for Peptides-func (labeled as Pept-Func in Table 1 and Peptides-Func in Table 2). Table 1
provides the main comparison with baselines for the default configuration (k-MIP without specified
k, likely default or best k). Table 2 provides ablation results for varying k values. All values are
test set performance. Metric is AP (Average Precision), higher is better. Standard deviations are
included where available. [Peptides-struct] Extracted only Peptides-struct (MAE) results from Table
1. The dataset name in the table is 'Pept-Struct', mapped to 'Peptides-struct' as per standard LRGB
naming conventions and the FOCUS instruction. All values are mean ± std over four runs. Baselines
marked with † are taken from Tonshoff 2023, ‡ from Shirzad 2023. [ShapeNet-Part] Extracted only
ShapeNet-Part F1 results as requested. GPS + Transformer row was skipped due to missing values
('--'). All other rows from the ShapeNet-Part column were extracted. [S3DIS] failed: 1 validation
error for ExtractionOutput results.6.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [City-Networks] failed: 7 validation errors for
ExtractionOutput results.18.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.19.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.24.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.25.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.26.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.27.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.31.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [Cifar10] Extracted all rows for the Cifar10 dataset
from Table 1. The table presents results for varying values of hyperparameter k for the proposed
model (GraphGPS with k-MIP attention). No separate baseline models are listed in this specific
table, only variations of the proposed method. The metric is Accuracy, and higher is better.
[MalNet-Tiny] Extracted all rows for MalNet-Tiny from Table 1. The table compares different values
of k for the proposed GraphGPS model with k-MIP attention. No external baselines are listed in this
specific table for MalNet-Tiny, only variations of the proposed method. The metric is Accuracy, and
higher is better.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*