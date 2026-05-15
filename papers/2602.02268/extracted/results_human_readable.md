# Extraction: HopFormer: Sparse Graph Transformers \ Explicit Receptive Field Control
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-11  **Confidence**: HIGH

## Proposed Model: HopFormer
- Type: GNN

## Results

### Chameleon — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.4415 | 0.0169 | Yes | this paper | Table 2 |
| GAT | 0.4613 | 0.0021 | Yes | this paper | Table 2 |
| APPNP | 0.4956 | 0.0100 | Yes | this paper | Table 2 |
| Graphtransformer | 0.4006 | 0.0055 | Yes | this paper | Table 2 |
| Graphormer | 0.5453 | 0.0136 | Yes | this paper | Table 2 |
| SAN | 0.4189 | 0.0267 | Yes | this paper | Table 2 |
| GPS | 0.4905 | 0.0092 | Yes | this paper | Table 2 |
| DIFFormer | 0.4854 | 0.0058 | Yes | this paper | Table 2 |
| SpecFormer | 0.5623 | 0.0089 | Yes | this paper | Table 2 |
| Exphormer | 0.5161 | 0.0068 | Yes | this paper | Table 2 |
| GRIT | 0.4722 | 0.0260 | Yes | this paper | Table 2 |
| NodeFormer | 0.4788 | 0.0058 | Yes | this paper | Table 2 |
| CoBFormer | 0.5124 | 0.0057 | Yes | this paper | Table 2 |
| SGFormer | 0.5080 | 0.0010 | Yes | this paper | Table 2 |
| DeGTA | 0.4920 | 0.0045 | Yes | this paper | Table 2 |
| HopFormer | 0.5738 | 0.0278 | No | this paper | Table 2 |

### Cornell — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3243 | 0.0441 | Yes | this paper | Table 2 |
| GAT | 0.3513 | 0.0441 | Yes | this paper | Table 2 |
| APPNP | 0.4414 | 0.0127 | Yes | this paper | Table 2 |
| Graphtransformer | 0.3874 | 0.0127 | Yes | this paper | Table 2 |
| Graphormer | 0.7117 | 0.0127 | Yes | this paper | Table 2 |
| SAN | 0.6667 | 0.0337 | Yes | this paper | Table 2 |
| GPS | 0.7297 | 0.0221 | Yes | this paper | Table 2 |
| DIFFormer | 0.6486 | 0.0441 | Yes | this paper | Table 2 |
| SpecFormer | 0.7478 | 0.0255 | Yes | this paper | Table 2 |
| Exphormer | 0.5405 | 0.0441 | Yes | this paper | Table 2 |
| GRIT | 0.6486 | 0.0584 | Yes | this paper | Table 2 |
| NodeFormer | 0.6577 | 0.0459 | Yes | this paper | Table 2 |
| CoBFormer | 0.7117 | 0.0337 | Yes | this paper | Table 2 |
| SGFormer | 0.7207 | 0.0127 | Yes | this paper | Table 2 |
| DeGTA | 0.5315 | 0.0459 | Yes | this paper | Table 2 |
| HopFormer | 0.7657 | 0.0412 | No | this paper | Table 2 |

### Texas — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.4505 | 0.0709 | Yes | this paper | Table 2 |
| GAT | 0.3604 | 0.1469 | Yes | this paper | Table 2 |
| APPNP | 0.5405 | 0.0000 | Yes | this paper | Table 2 |
| Graphtransformer | 0.6036 | 0.0255 | Yes | this paper | Table 2 |
| Graphormer | 0.7748 | 0.0127 | Yes | this paper | Table 2 |
| SAN | 0.6667 | 0.0337 | Yes | this paper | Table 2 |
| GPS | 0.7478 | 0.0127 | Yes | this paper | Table 2 |
| DIFFormer | 0.7207 | 0.0337 | Yes | this paper | Table 2 |
| SpecFormer | 0.7838 | 0.0221 | Yes | this paper | Table 2 |
| Exphormer | 0.3784 | 0.0221 | Yes | this paper | Table 2 |
| GRIT | 0.7027 | 0.0382 | Yes | this paper | Table 2 |
| NodeFormer | 0.6937 | 0.0255 | Yes | this paper | Table 2 |
| CoBFormer | 0.7387 | 0.0637 | Yes | this paper | Table 2 |
| SGFormer | 0.7568 | 0.0221 | Yes | this paper | Table 2 |
| DeGTA | 0.6126 | 0.0127 | Yes | this paper | Table 2 |
| HopFormer | 0.7937 | 0.0270 | No | this paper | Table 2 |

### Wisconsin — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.4379 | 0.0515 | Yes | this paper | Table 2 |
| GAT | 0.3791 | 0.0606 | Yes | this paper | Table 2 |
| APPNP | 0.4641 | 0.0092 | Yes | this paper | Table 2 |
| Graphtransformer | 0.5229 | 0.0462 | Yes | this paper | Table 2 |
| Graphormer | 0.7582 | 0.0244 | Yes | this paper | Table 2 |
| SAN | 0.7843 | 0.0160 | Yes | this paper | Table 2 |
| GPS | 0.7974 | 0.0092 | Yes | this paper | Table 2 |
| DIFFormer | 0.7451 | 0.0320 | Yes | this paper | Table 2 |
| SpecFormer | 0.7778 | 0.0092 | Yes | this paper | Table 2 |
| Exphormer | 0.6994 | 0.0333 | Yes | this paper | Table 2 |
| GRIT | 0.8039 | 0.0160 | Yes | this paper | Table 2 |
| NodeFormer | 0.7386 | 0.0403 | Yes | this paper | Table 2 |
| CoBFormer | 0.7647 | 0.0320 | Yes | this paper | Table 2 |
| SGFormer | 0.7843 | 0.0000 | Yes | this paper | Table 2 |
| DeGTA | 0.5229 | 0.0092 | Yes | this paper | Table 2 |
| HopFormer | 0.8169 | 0.0113 | No | this paper | Table 2 |

### ZINC — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.6090 | 0.0155 | Yes | this paper | Table 3 |
| GAT | 0.6225 | 0.0096 | Yes | this paper | Table 3 |
| APPNP | 0.6619 | 0.0067 | Yes | this paper | Table 3 |
| Graphtransformer | 0.6038 | 0.0151 | Yes | this paper | Table 3 |
| Graphormer | 0.1305 | 0.0072 | Yes | this paper | Table 3 |
| SAN | 0.1341 | 0.0063 | Yes | this paper | Table 3 |
| GPS | 0.1968 | 0.0120 | Yes | this paper | Table 3 |
| GPS+RWSE | 0.0681 | 0.0004 | Yes | this paper | Table 3 |
| GPS+GE | 0.1789 | 0.0071 | Yes | this paper | Table 3 |
| DIFFormer | 0.6602 | 0.0294 | Yes | this paper | Table 3 |
| Exphormer | 0.1905 | 0.0276 | Yes | this paper | Table 3 |
| GRIT | 0.0607 | 0.0000 | Yes | this paper | Table 3 |
| GraphMLPMixer | 0.3617 | 0.0222 | Yes | this paper | Table 3 |
| SGFormer | 0.6703 | 0.0033 | Yes | this paper | Table 3 |
| HopFormer | 0.1306 | 0.0194 | No | this paper | Table 3 |

## Baseline Models Identified

- **GCN** (from: Kipf & Welling 2017)
- **GAT** (from: Veličković et al. 2018)
- **APPNP** (from: Klicpera et al. 2019)
- **Graphtransformer** (from: Veličković 2021)
- **Graphormer** (from: Ying et al. 2021)
- **SAN** (from: Ying et al. 2021)
- **GPS** (from: Shchur et al. 2021)
- **DIFFormer** (from: Bresson & Laurent 2021)
- **SpecFormer** (from: De Brouwer et al. 2021)
- **Exphormer** (from: Fey et al. 2020)
- **GRIT** (from: Chen et al. 2022)
- **NodeFormer** (from: Chen et al. 2022)
- **CoBFormer** (from: Chen et al. 2022)
- **SGFormer** (from: Wu et al. 2022)
- **DeGTA** (from: Zhang et al. 2022)
- **GPS+RWSE** (from: Dwivedi et al. 2022)
- **GPS+GE** (from: Dwivedi et al. 2022)
- **GraphMLPMixer** (from: Tay et al. 2022)

## Extraction Notes

[Cora] failed: 1 validation error for ExtractionOutput results.10.value   Input should be a valid
number [type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [CiteSeer] failed: 2 validation errors for
ExtractionOutput results.5.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.10.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [PubMed] failed: 4 validation errors for
ExtractionOutput results.4.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.5.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.10.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.14.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [Chameleon] Extracted only the Chameleon column from
Table 2. All values are test accuracy. Standard deviations are parsed from the LaTeX format
mean_{std}. OOM entries were skipped as they contain no numerical result. [Squirrel] failed: 2
validation errors for ExtractionOutput results.5.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.10.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [Actor] failed: 2 validation errors for
ExtractionOutput results.5.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.10.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [Cornell] Extracted all rows for the 'Cornell' dataset
from Table 2. The metric is Accuracy. Standard deviations are parsed from the format mean_std.
[Texas] Extracted all rows from Table 2 corresponding to the 'Texas' dataset column. The metric is
Test Accuracy. Standard deviations are parsed from the format mean_std. All models are treated as
baselines except HopFormer which is marked as proposed. [Wisconsin] Extracted all rows from Table 2
for the 'Wisconsin' dataset column. The metric is Test Accuracy. Standard deviations are parsed from
the format mean_std. All models are treated as baselines except HopFormer which is marked as
proposed. [OGBG-MolHIV] failed: 4 validation errors for ExtractionOutput results.4.value   Input
should be a valid number [type=float_type, input_value=None, input_type=NoneType]     For further
information visit https://errors.pydantic.dev/2.13/v/float_type results.5.value   Input should be a
valid number [type=float_type, input_value=None, input_type=NoneType]     For further information
visit https://errors.pydantic.dev/2.13/v/float_type results.8.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.10.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [OGBG-MolPCBA] failed: 5 validation errors for
ExtractionOutput results.4.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.5.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.6.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.8.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.10.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [Peptides-Func] failed: 4 validation errors for
ExtractionOutput results.4.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.5.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.8.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.11.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [Peptides-Struct] failed: 4 validation errors for
ExtractionOutput results.4.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.5.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.8.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.11.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [ZINC] Extracted all ZINC MAE results from Table 3.
Note that GRIT reports std as 0.0000, which is preserved as 0.0. HopFormer is identified as the
proposed model based on the 'Ours' label and bolding context.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*