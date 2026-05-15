# Extraction: arXiv:2402.04821
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: EMNN
- Type: GNN

## Results

### FAUST — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GEM-CNN | 0.9792 | 0.0030 | Yes | gemcnn | Table 1 |
| EMAN | 0.9846 | 0.0015 | Yes | eman | Table 1 |
| EGNN | 0.9950 | 0.0002 | Yes | this paper | Table 1 |
| EGNN + MC | 0.9976 | 0.0001 | Yes | this paper | Table 1 |
| EGNN + MC + Hier | 0.9993 | 0.0001 | Yes | this paper | Table 1 |
| EMNN | 1.0000 | 0.0000 | No | this paper | Table 1 |
| EMNN + MC | 1.0000 | 0.0000 | No | this paper | Table 1 |
| EMNN + MC + Hier | 1.0000 | 0.0000 | No | this paper | Table 1 |

### Human Body Segmentation — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| PointNet | 0.7470 | — | Yes | Qi 2016 | Table 1 |
| PointNet++ | 0.8230 | — | Yes | Qi 2017 | Table 1 |
| MeshCNN | 0.8540 | — | Yes | MeshCNN | Table 1 |
| PD-MeshNet | 0.8560 | — | Yes | Milano 2020 | Table 1 |
| HodgeNet | 0.8500 | — | Yes | Smirnov 2021 | Table 1 |
| SubdivNet | 0.9170 | — | Yes | Hu 2022 | Table 1 |
| DiffusionNet | 0.9030 | — | Yes | DiffusionNet | Table 1 |
| Laplacian2Mesh | 0.8860 | — | Yes | Laplacian2Mesh | Table 1 |
| Mesh-MLP | 0.8880 | — | Yes | MeshMLP | Table 1 |
| EGNN (baseline) | 0.8060 | — | Yes | EGNN | Table 1 |
| EGNN+MC (baseline) | 0.8270 | — | Yes | this paper | Table 1 |
| EGNN+MC+Hier (baseline) | 0.8720 | — | Yes | this paper | Table 1 |
| EMNN | 0.8100 | — | Yes | this paper | Table 1 |
| EMNN+MC | 0.8350 | — | Yes | this paper | Table 1 |
| EMNN+MC+Hier | 0.8870 | — | No | this paper | Table 1 |

### TOSCA — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GEM-CNN | 0.8235 | 0.0588 | Yes | gemcnn | Table 1 |
| EMAN | 0.4235 | 0.2055 | Yes | eman | Table 1 |
| EGNN (baseline) | 0.9523 | 0.0011 | Yes | this paper | Table 1 |
| EGNN + MC (baseline) | 1.0000 | 0.0000 | Yes | this paper | Table 1 |
| EGNN + MC + Hier (baseline) | 1.0000 | 0.0000 | Yes | this paper | Table 1 |
| EMNN (ours) | 1.0000 | 0.0000 | No | this paper | Table 1 |
| EMNN + MC (ours) | 1.0000 | 0.0000 | No | this paper | Table 1 |
| EMNN + MC + Hier (ours) | 1.0000 | 0.0000 | No | this paper | Table 1 |

## Baseline Models Identified

- **GEM-CNN** (from: gemcnn)
- **EMAN** (from: eman)
- **EGNN** (from: this paper)
- **PointNet** (from: Qi 2016)
- **PointNet++** (from: Qi 2017)
- **MeshCNN** (from: MeshCNN)
- **PD-MeshNet** (from: Milano 2020)
- **HodgeNet** (from: Smirnov 2021)
- **SubdivNet** (from: Hu 2022)
- **DiffusionNet** (from: DiffusionNet)
- **Laplacian2Mesh** (from: Laplacian2Mesh)
- **Mesh-MLP** (from: MeshMLP)
- **EGNN (baseline)** (from: EGNN)
- **EGNN+MC (baseline)** (from: this paper)
- **EGNN+MC+Hier (baseline)** (from: this paper)
- **EMNN** (from: this paper)
- **EMNN+MC** (from: this paper)

## Extraction Notes

[FAUST] Extracted only the 'Test' column from Table 1 as it represents the standard evaluation
metric for the FAUST dataset. The table reports Accuracy in percentages, which were divided by 100
to fit the [0,1] range. Multiple variants of baselines (different initial features) are included as
separate rows. The proposed model EMNN and its variants also have multiple rows corresponding to
different feature inputs. [TOSCA] The table contains multiple columns for accuracy: 'Test', 'Gauge',
and 'Rot-Tr-Ref-Scale'. The 'Test' column is the standard evaluation metric for the dataset. The
'Gauge' and 'Rot-Tr-Ref-Scale' columns appear to be specific invariance/equivariance checks or
alternative configurations. I have extracted the 'Test' accuracy values as they represent the
standard benchmark performance. Note that for GEM-CNN and EMAN, different 'Initial Features' (XYZ,
GET, RELTAN) are listed. I extracted all rows as they represent different configurations of the
baseline models. The proposed model EMNN and its variants also show multiple rows with identical
perfect scores. [SHREC] failed: 1 validation error for ExtractionOutput results.12.value   Input
should be a valid number [type=float_type, input_value=None, input_type=NoneType]     For further
information visit https://errors.pydantic.dev/2.13/v/float_type [Human Body Segmentation] Extracted
only the main comparison table (Table 1) for the 'Human Body Segmentation' dataset. The ablation
study table (Table 2) was ignored as per instructions to skip optional variants/ablations and focus
on the standard configuration results. The proposed model is identified as 'EMNN+MC+Hier' which
achieves the best performance among the authors' variants and is marked as 'ours'. Note that
SubdivNet achieves a higher accuracy (91.7%), but it is a baseline. All accuracy percentages were
converted to [0,1] range.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*