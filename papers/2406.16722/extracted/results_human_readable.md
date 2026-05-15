# Extraction: arXiv:2406.16722
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: SiMBA (40.0M params)
- Type: Other

## Results

### ImageNet-1K — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| ResNet-18 | 0.6980 | — | Yes | this paper | Table 1 |
| ResNet-50 | 0.7620 | — | Yes | this paper | Table 1 |
| ResNet-101 | 0.7740 | — | Yes | this paper | Table 1 |
| ResNet-152 | 0.7830 | — | Yes | this paper | Table 1 |
| ResNetXt50-32x4d | 0.7760 | — | Yes | this paper | Table 1 |
| RegNetY-4G | 0.8000 | — | Yes | this paper | Table 1 |
| RegNetY-8G | 0.8170 | — | Yes | this paper | Table 1 |
| RegNetY-16G | 0.8290 | — | Yes | this paper | Table 1 |
| ViT-B/16 | 0.7790 | — | Yes | this paper | Table 1 |
| ViT-L/16 | 0.7650 | — | Yes | this paper | Table 1 |
| DeiT-S | 0.7980 | — | Yes | this paper | Table 1 |
| DeiT-B | 0.8310 | — | Yes | this paper | Table 1 |
| Swin-T | 0.8130 | — | Yes | this paper | Table 1 |
| Swin-S | 0.8300 | — | Yes | this paper | Table 1 |
| Swin-B | 0.8350 | — | Yes | this paper | Table 1 |
| S4ND-ViT-B | 0.8040 | — | Yes | this paper | Table 1 |
| Vim-Ti | 0.7310 | — | Yes | this paper | Table 1 |
| Vim-S | 0.8030 | — | Yes | this paper | Table 1 |
| VMamba-T | 0.8250 | — | Yes | this paper | Table 1 |
| VMamba-S | 0.8360 | — | Yes | this paper | Table 1 |
| VMamba-B | 0.8390 | — | Yes | this paper | Table 1 |
| SiMBA-S(MLP) | 0.8400 | — | Yes | this paper | Table 1 |
| SiMBA-B(MLP) | 0.8470 | — | No | this paper | Table 1 |
| SiMBA-L(EinFFT) | 0.8390 | — | Yes | this paper | Table 1 |

## Baseline Models Identified

- **ResNet-18**, 12.0M params (from: He et al. (implied by standard naming))
- **ResNet-50**, 25.0M params (from: He et al. (implied by standard naming))
- **ResNet-101**, 45.0M params (from: He et al. (implied by standard naming))
- **ResNet-152**, 60.0M params (from: He et al. (implied by standard naming))
- **ResNetXt50-32x4d**, 25.0M params (from: Xie et al. (implied by standard naming))
- **RegNetY-4G**, 21.0M params (from: Radosavovic et al. (implied by standard naming))
- **RegNetY-8G**, 39.0M params (from: Radosavovic et al. (implied by standard naming))
- **RegNetY-16G**, 84.0M params (from: Radosavovic et al. (implied by standard naming))
- **ViT-B/16**, 86.0M params (from: Dosovitskiy et al. (implied by standard naming))
- **ViT-L/16**, 307.0M params (from: Dosovitskiy et al. (implied by standard naming))
- **DeiT-S**, 22.0M params (from: Touvron et al. (implied by standard naming))
- **DeiT-B**, 86.0M params (from: Touvron et al. (implied by standard naming))
- **Swin-T**, 29.0M params (from: Liu et al. (implied by standard naming))
- **Swin-S**, 50.0M params (from: Liu et al. (implied by standard naming))
- **Swin-B**, 88.0M params (from: Liu et al. (implied by standard naming))
- **S4ND-ViT-B**, 89.0M params (from: Liu et al. (2024))
- **Vim-Ti**, 7.0M params (from: Liu et al. (2024))
- **Vim-S**, 26.0M params (from: Liu et al. (2024))
- **VMamba-T**, 22.0M params (from: Liu et al. (2024))
- **VMamba-S**, 44.0M params (from: Liu et al. (2024))
- **VMamba-B**, 75.0M params (from: Liu et al. (2024))
- **SiMBA-S(MLP)**, 26.5M params (from: Patro et al. (2024))
- **SiMBA-L(EinFFT)**, 36.6M params (from: Patro et al. (2024))

## Extraction Notes

[ImageNet-1K] Extracted all rows from Table 1 for ImageNet-1K. The proposed model is identified as
SiMBA (specifically SiMBA-B(MLP) which achieves the highest accuracy). Other SiMBA variants are
treated as baselines or ablations from the referenced paper. All accuracy values were divided by 100
to fit the [0,1] range. No standard deviations were reported in the table.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*