# Extraction: arXiv:2410.03424
**Model used**: `alias-huge-no-thinking`  **Date**: 2026-05-13  **Confidence**: HIGH

## Proposed Model: CGP
- Type: Other

## Results

### COLLAB — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7049 | 0.0163 | Yes | this paper | Table 1 |
| GCN + FA | 0.7204 | 0.0077 | Yes | this paper | Table 1 |
| GCN + DIGL | 0.5647 | 0.0086 | Yes | this paper | Table 1 |
| GCN + SDRF | 0.7133 | 0.0081 | Yes | this paper | Table 1 |
| GCN + FoSR | 0.6722 | 0.0137 | Yes | this paper | Table 1 |
| GCN + GTR | 0.7260 | 0.0103 | Yes | this paper | Table 1 |
| GCN + PANDA | 0.7385 | 0.0069 | Yes | this paper | Table 1 |
| GCN + EGP | 0.6947 | 0.0097 | Yes | this paper | Table 1 |
| GCN + CGP | 0.6963 | 0.0073 | No | this paper | Table 1 |
| GIN | 0.7149 | 0.0075 | Yes | this paper | Table 1 |
| GIN + FA | 0.7274 | 0.0079 | Yes | this paper | Table 1 |
| GIN + DIGL | 0.5762 | 0.0101 | Yes | this paper | Table 1 |
| GIN + SDRF | 0.7296 | 0.0042 | Yes | this paper | Table 1 |
| GIN + FoSR | 0.7172 | 0.0089 | Yes | this paper | Table 1 |
| GIN + GTR | 0.7185 | 0.0071 | Yes | this paper | Table 1 |
| GIN + PANDA | 0.7332 | 0.0081 | Yes | this paper | Table 1 |
| GIN + EGP | 0.7233 | 0.0095 | Yes | this paper | Table 1 |
| GIN + CGP | 0.7335 | 0.0079 | No | this paper | Table 1 |

### PROTEINS — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.6665 | 0.0193 | Yes | this paper | Table 1 |
| GCN + FA | 0.7107 | 0.0151 | Yes | this paper | Table 1 |
| GCN + DIGL | 0.7272 | 0.0142 | Yes | this paper | Table 1 |
| GCN + SDRF | 0.6728 | 0.0217 | Yes | this paper | Table 1 |
| GCN + FoSR | 0.7085 | 0.0162 | Yes | this paper | Table 1 |
| GCN + BORF | 0.6741 | 0.0002 | Yes | this paper | Table 1 |
| GCN + GTR | 0.7299 | 0.0196 | Yes | this paper | Table 1 |
| GCN + PANDA | 0.7013 | 0.0152 | Yes | this paper | Table 1 |
| GCN + EGP | 0.7330 | 0.0252 | Yes | this paper | Table 1 |
| GCN + CGP | 0.7304 | 0.0129 | No | this paper | Table 1 |
| GIN | 0.7031 | 0.0175 | Yes | this paper | Table 1 |
| GIN + FA | 0.7290 | 0.0142 | Yes | this paper | Table 1 |
| GIN + DIGL | 0.7232 | 0.0144 | Yes | this paper | Table 1 |
| GIN + SDRF | 0.6951 | 0.0171 | Yes | this paper | Table 1 |
| GIN + FoSR | 0.7152 | 0.0177 | Yes | this paper | Table 1 |
| GIN + BORF | 0.7063 | 0.0002 | Yes | this paper | Table 1 |
| GIN + GTR | 0.7205 | 0.0151 | Yes | this paper | Table 1 |
| GIN + PANDA | 0.7232 | 0.0179 | Yes | this paper | Table 1 |
| GIN + EGP | 0.7085 | 0.0157 | Yes | this paper | Table 1 |
| GIN + CGP | 0.7308 | 0.0140 | No | this paper | Table 1 |

### ogbg-molhiv — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7566 | 0.0104 | Yes | this paper | Table 1 |
| GCN + Master Node | 0.7531 | 0.0128 | Yes | this paper | Table 1 |
| GCN + FA | 0.7628 | 0.0191 | Yes | this paper | Table 1 |
| GCN + EGP | 0.7731 | 0.0081 | Yes | this paper | Table 1 |
| GCN + CGP | 0.7794 | 0.0122 | No | this paper | Table 1 |
| GIN | 0.7678 | 0.0183 | Yes | this paper | Table 1 |
| GIN + Master Node | 0.7608 | 0.0134 | Yes | this paper | Table 1 |
| GIN + FA | 0.7718 | 0.0147 | Yes | this paper | Table 1 |
| GIN + EGP | 0.7537 | 0.0076 | Yes | this paper | Table 1 |
| GIN + CGP | 0.7899 | 0.0090 | No | this paper | Table 1 |

### ogbg-ppa — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5483 | 0.0209 | Yes | this paper | Table OGB |
| GCN + Master Node | 0.5824 | 0.0219 | Yes | this paper | Table OGB |
| GCN + EGP | 0.6821 | 0.0045 | Yes | this paper | Table OGB |
| GCN + CGP | 0.6782 | 0.0066 | No | this paper | Table OGB |
| GIN | 0.5888 | 0.0441 | Yes | this paper | Table OGB |
| GIN + Master Node | 0.6069 | 0.0062 | Yes | this paper | Table OGB |
| GIN + EGP | 0.6533 | 0.1190 | Yes | this paper | Table OGB |
| GIN + CGP | 0.6562 | 0.0147 | No | this paper | Table OGB |

## Baseline Models Identified

- **GCN**
- **GIN**
- **Master Node** (from: gilmer2017neural)
- **FA** (from: alon2020bottleneck)
- **EGP** (from: deac2022expander)
- **DIGL**
- **SDRF**
- **FoSR**
- **BORF**
- **GTR**
- **PANDA**

## Extraction Notes

[ogbg-molhiv] Only the OGB wraptable (Table 1 / tab:ogb) contained ogbg-molhiv results. All values
were clearly reported as Test ROC-AUC with mean and standard deviation. No parameter counts were
provided in the excerpt. TUDataset and ablation tables were ignored as they do not contain ogbg-
molhiv. [ogbg-ppa] Only the wraptable labeled 'tab:ogb' contains ogbg-ppa results. OOM entries (GCN
+ FA and GIN + FA) were skipped as they are not quantitative values. No model parameter counts are
reported in the provided text. All values are already in [0,1] decimal form. [REDDIT-BINARY] failed:
Model 'alias-huge-no-thinking' returned empty content (input_chars=15866, duration=213.51s) — likely
rate limit or quota exceeded — treating as transient error [IMDB-BINARY] failed: JSON parse error
from 'alias-huge-no-thinking': could not extract valid JSON [MUTAG] failed: JSON parse error from
'alias-huge-no-thinking': could not extract valid JSON [ENZYMES] failed: 1 validation error for
ExtractionOutput   Input should be a valid dictionary or instance of ExtractionOutput
[type=model_type, input_value=[{'name': 'GCN', 'params_...inal_paper_hint': None}], input_type=list]
For further information visit https://errors.pydantic.dev/2.13/v/model_type [PROTEINS] Extracted
PROTEINS Accuracy results only from the main benchmark table (Table 1 / tab:graph_rewiring). Skipped
the complexity table (no Accuracy metric) and the ablation tables showing optional layer-application
variants (Table 3 / tab:tu_ablations) and virtual-node initialisation variants (Table 4) per the
instruction to use only standard/default configurations. All Accuracy values were reported as
percentages and were normalised to [0,1] by dividing by 100. No parameter counts or external data
usage were mentioned in the provided tables. [COLLAB] Extracted standard-configuration COLLAB
Accuracy results from Table 1 (tab:graph_rewiring). Skipped ablation tables showing optional layer
variants (every-layer/last-only) and virtual-node initialisation variants, as well as the
time/memory table, per the focus instructions. OOT (out-of-time) entries were omitted as non-
numerical. Percentage Accuracy values were normalised to [0,1].

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*