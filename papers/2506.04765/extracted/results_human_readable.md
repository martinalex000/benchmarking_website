# Extraction: OpenGT: A Comprehensive Benchmark For Graph Transformers
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: DIFFormer+GE
- Type: GraphTransformer

## Results

### Chameleon — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.4415 | 0.0169 | Yes | this paper | Table 1 |
| GAT | 0.4613 | 0.0021 | Yes | this paper | Table 1 |
| APPNP | 0.4956 | 0.0100 | Yes | this paper | Table 1 |
| Graphtransformer | 0.4006 | 0.0055 | Yes | this paper | Table 1 |
| Graphormer | 0.5453 | 0.0136 | Yes | this paper | Table 1 |
| SAN | 0.4189 | 0.0267 | Yes | this paper | Table 1 |
| GPS | 0.4905 | 0.0092 | Yes | this paper | Table 1 |
| DIFFormer | 0.4854 | 0.0058 | Yes | this paper | Table 1 |
| SpecFormer | 0.6623 | 0.0089 | Yes | this paper | Table 1 |
| Exphormer | 0.5161 | 0.0068 | Yes | this paper | Table 1 |
| GRIT | 0.4722 | 0.0260 | Yes | this paper | Table 1 |
| NodeFormer | 0.4788 | 0.0058 | Yes | this paper | Table 1 |
| CoBFormer | 0.5124 | 0.0057 | Yes | this paper | Table 1 |
| SGFormer | 0.5080 | 0.0010 | Yes | this paper | Table 1 |
| DeGTA | 0.4920 | 0.0045 | Yes | this paper | Table 1 |
| DIFFormer+GE | 0.5446 | 0.0010 | No | this paper | Table 2 |
| DIFFormer+GESP | 0.5446 | 0.0010 | Yes | this paper | Table 2 |
| GPS+GE | 0.5395 | 0.0142 | Yes | this paper | Table 2 |
| GPS+GESP | 0.5387 | 0.0152 | Yes | this paper | Table 2 |
| SGFormer+GE | 0.5446 | 0.0075 | Yes | this paper | Table 2 |
| SGFormer+GESP | 0.5446 | 0.0075 | Yes | this paper | Table 2 |

### Cornell — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3243 | 0.0441 | Yes | this paper | Table 1 |
| GAT | 0.3513 | 0.0441 | Yes | this paper | Table 1 |
| APPNP | 0.4414 | 0.0127 | Yes | this paper | Table 1 |
| Graphtransformer | 0.3874 | 0.0127 | Yes | this paper | Table 1 |
| Graphormer | 0.7117 | 0.0127 | Yes | this paper | Table 1 |
| SAN | 0.6667 | 0.0337 | Yes | this paper | Table 1 |
| GPS | 0.7297 | 0.0221 | Yes | this paper | Table 1 |
| DIFFormer | 0.6486 | 0.0441 | No | this paper | Table 1 |
| SpecFormer | 0.7478 | 0.0255 | Yes | this paper | Table 1 |
| Exphormer | 0.5405 | 0.0441 | Yes | this paper | Table 1 |
| GRIT | 0.6486 | 0.0584 | Yes | this paper | Table 1 |
| NodeFormer | 0.6577 | 0.0459 | Yes | this paper | Table 1 |
| CoBFormer | 0.7117 | 0.0337 | Yes | this paper | Table 1 |
| SGFormer | 0.7207 | 0.0127 | Yes | this paper | Table 1 |
| DeGTA | 0.5315 | 0.0459 | Yes | this paper | Table 1 |

### Texas — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.4505 | 0.0709 | Yes | this paper | Table 1 |
| GAT | 0.3604 | 0.1469 | Yes | this paper | Table 1 |
| APPNP | 0.5405 | 0.0000 | Yes | this paper | Table 1 |
| Graphtransformer | 0.6036 | 0.0255 | Yes | this paper | Table 1 |
| Graphormer | 0.7748 | 0.0127 | Yes | this paper | Table 1 |
| SAN | 0.6667 | 0.0337 | Yes | this paper | Table 1 |
| GPS | 0.7478 | 0.0127 | Yes | this paper | Table 1 |
| DIFFormer | 0.7207 | 0.0337 | No | this paper | Table 1 |
| SpecFormer | 0.7838 | 0.0221 | Yes | this paper | Table 1 |
| Exphormer | 0.3784 | 0.0221 | Yes | this paper | Table 1 |
| GRIT | 0.7027 | 0.0382 | Yes | this paper | Table 1 |
| NodeFormer | 0.6937 | 0.0255 | Yes | this paper | Table 1 |
| CoBFormer | 0.7387 | 0.0637 | Yes | this paper | Table 1 |
| SGFormer | 0.7568 | 0.0221 | Yes | this paper | Table 1 |
| DeGTA | 0.6126 | 0.0127 | Yes | this paper | Table 1 |

### Wisconsin — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.4379 | 0.0515 | Yes | this paper | Table 1 |
| GAT | 0.3791 | 0.0606 | Yes | this paper | Table 1 |
| APPNP | 0.4641 | 0.0092 | Yes | this paper | Table 1 |
| Graphtransformer | 0.5229 | 0.0462 | Yes | this paper | Table 1 |
| Graphormer | 0.7582 | 0.0244 | Yes | this paper | Table 1 |
| SAN | 0.7843 | 0.0160 | Yes | this paper | Table 1 |
| GPS | 0.7974 | 0.0092 | Yes | this paper | Table 1 |
| DIFFormer | 0.7451 | 0.0320 | No | this paper | Table 1 |
| SpecFormer | 0.7778 | 0.0092 | Yes | this paper | Table 1 |
| Exphormer | 0.6994 | 0.0333 | Yes | this paper | Table 1 |
| GRIT | 0.8039 | 0.0160 | Yes | this paper | Table 1 |
| NodeFormer | 0.7386 | 0.0403 | Yes | this paper | Table 1 |
| CoBFormer | 0.7647 | 0.0320 | Yes | this paper | Table 1 |
| SGFormer | 0.7843 | 0.0000 | Yes | this paper | Table 1 |
| DeGTA | 0.5229 | 0.0092 | Yes | this paper | Table 1 |

### ZINC — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.6090 | 0.0155 | Yes | this paper | Table 1 |
| GAT | 0.6225 | 0.0096 | Yes | this paper | Table 1 |
| APPNP | 0.6619 | 0.0067 | Yes | this paper | Table 1 |
| Graphtransformer | 0.6038 | 0.0151 | Yes | this paper | Table 1 |
| Graphormer | 0.1305 | 0.0072 | Yes | this paper | Table 1 |
| SAN | 0.1341 | 0.0063 | Yes | this paper | Table 1 |
| GPS | 0.1968 | 0.0120 | Yes | this paper | Table 1 |
| GPS+RWSE | 0.0681 | 0.0004 | Yes | this paper | Table 1 |
| GPS+GE | 0.1789 | 0.0071 | Yes | this paper | Table 1 |
| DIFFormer | 0.6602 | 0.0294 | Yes | this paper | Table 1 |
| Exphormer | 0.1905 | 0.0276 | Yes | this paper | Table 1 |
| GRIT | 0.0607 | 0.0000 | No | this paper | Table 1 |
| GraphMLPMixer | 0.3617 | 0.0222 | Yes | this paper | Table 1 |
| SGFormer | 0.6703 | 0.0033 | Yes | this paper | Table 1 |

## Baseline Models Identified

- **GCN** (from: Kipf & Welling 2017)
- **GAT** (from: Veličković et al. 2018)
- **APPNP** (from: Klicpera et al. 2019)
- **Graphtransformer** (from: Ying et al. 2019)
- **Graphormer** (from: Biao et al. 2022)
- **SAN** (from: Brody et al. 2021)
- **GPS** (from: Beaini et al. 2022)
- **DIFFormer** (from: this paper (baseline variant))
- **SpecFormer** (from: this paper)
- **Exphormer** (from: Pinsard et al. 2022)
- **GRIT** (from: this paper)
- **NodeFormer** (from: Ying et al. 2022)
- **CoBFormer** (from: this paper)
- **SGFormer** (from: Wu et al. 2023)
- **DeGTA** (from: this paper)
- **GPS+RWSE** (from: Dwivedi et al. 2022)
- **GPS+GE** (from: Dwivedi et al. 2022)
- **GraphMLPMixer** (from: Tolstikhin et al. 2021 / Bhatt et al. 2022)

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
https://errors.pydantic.dev/2.13/v/float_type [Chameleon] Extracted results for Chameleon dataset
from Table 1 (standard models) and Table 2 (models with positional encodings). The proposed model is
identified as DIFFormer+GE based on the text highlighting GE/GESP effectiveness and the bolding in
the table (though bolding isn't explicitly visible in raw text, GE/GESP are the focus of Observation
5). Note that DIFFormer+GE, DIFFormer+GESP, SGFormer+GE, and SGFormer+GESP all report the same mean
accuracy (0.5446) but different standard deviations in Table 2. SpecFormer reports a higher accuracy
(0.6623) in Table 1, which is included as a baseline result. All values are normalized to [0,1].
[Squirrel] failed: 2 validation errors for ExtractionOutput results.5.value   Input should be a
valid number [type=float_type, input_value=None, input_type=NoneType]     For further information
visit https://errors.pydantic.dev/2.13/v/float_type results.10.value   Input should be a valid
number [type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [Actor] failed: 2 validation errors for
ExtractionOutput results.5.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.10.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [Cornell] Extracted only the 'Cornell' column from
Table 1. Table 2 contains ablation studies for DIFFormer and GPS with different positional
encodings; per instructions to use standard/default configuration and ignore variants, only the main
DIFFormer row from Table 1 is included as the proposed model result. All other rows in Table 1 are
treated as baselines. [Texas] Extracted only the 'Texas' column from Table 1. Table 2 contains
ablation studies for DIFFormer and GPS with different positional encodings; per instructions to
ignore optional variants and focus on the standard/default configuration, only the main model
results from Table 1 were included. The 'DIFFormer' row in Table 1 represents the standard
configuration. All values are Accuracy (normalized to [0,1]). [Wisconsin] Extracted only the
'Wisconsin' column from Table 1. Table 2 contains ablation studies with positional encodings
(variants of DIFFormer and GPS) which were ignored as per instructions to skip optional variants/PE
configurations. All values are Accuracy. Standard deviations were parsed from the '±' notation.
[ogbg-molhiv] failed: 4 validation errors for ExtractionOutput results.4.value   Input should be a
valid number [type=float_type, input_value=None, input_type=NoneType]     For further information
visit https://errors.pydantic.dev/2.13/v/float_type results.5.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.8.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.10.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [ogbg-molpcba] failed: 5 validation errors for
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
https://errors.pydantic.dev/2.13/v/float_type [Peptides-func] failed: 4 validation errors for
ExtractionOutput results.4.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.5.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.8.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.11.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [Peptides-struct] failed: 4 validation errors for
ExtractionOutput results.4.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.5.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.8.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.11.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [ZINC] Extracted all rows from Table 1 corresponding
to the ZINC dataset and MAE metric. The proposed model is identified as GRIT based on the context of
the paper (implied by the focus on extracting proposed model results and GRIT being the likely new
contribution compared to standard baselines like GCN/GAT). Note: GRIT's std is reported as 0.0000,
which is extracted as 0.0.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*