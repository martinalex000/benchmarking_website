# Extraction: Position: Don't be Afraid of Over-Smoothing And Over-Squashing
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-11  **Confidence**: HIGH

## Proposed Model: None
- Type: Other

## Results

### CiteSeer — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 75.5000 | 0.8000 | Yes | this paper | Table 2 |
| GCN + Pairnorm | 68.3000 | 1.6000 | Yes | this paper | Table 2 |
| GCNII | 77.6000 | 0.2000 | Yes | this paper | Table 2 |
| G² | 76.5000 | 0.4000 | No | this paper | Table 2 |
| GATv2 | 75.0000 | 0.6000 | Yes | this paper | Table 2 |
| GATv2 + Pairnorm | 68.4000 | 0.8000 | Yes | this paper | Table 2 |
| G² (GATv2) | 76.3000 | 0.7000 | No | this paper | Table 2 |
| GraphSAGE | 75.5000 | 0.4000 | Yes | this paper | Table 2 |
| GraphSAGE + Pairnorm | 70.2000 | 1.0000 | Yes | this paper | Table 2 |
| G² (GraphSAGE) | 76.8000 | 0.3000 | No | this paper | Table 2 |

### Computers — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 77.7000 | 3.7000 | Yes | this paper | Table 1 |
| EGP (GCN) | 81.3000 | 1.6000 | No | this paper | Table 1 |
| GCN + SDRF | 76.1000 | 2.6000 | Yes | this paper | Table 1 |

### Cora — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 77.1000 | 3.3000 | Yes | this paper | Table 1 |
| GCN + Pairnorm | 69.6000 | 5.5000 | Yes | this paper | Table 1 |
| GCNII | 76.3000 | 2.3000 | Yes | this paper | Table 1 |
| G2-GCN | 75.6000 | 1.1000 | Yes | this paper | Table 1 |
| GATv2 | 75.5000 | 2.8000 | Yes | this paper | Table 2 |
| GATv2 + Pairnorm | 69.7000 | 1.5000 | Yes | this paper | Table 2 |
| G2-GCN (GATv2) | 78.5000 | 6.0000 | Yes | this paper | Table 2 |
| GraphSAGE | 82.1000 | 5.1000 | Yes | this paper | Table 2 |
| GraphSAGE + Pairnorm | 73.5000 | 4.9000 | Yes | this paper | Table 2 |
| G2-GCN (GraphSAGE) | 78.6000 | 5.0000 | Yes | this paper | Table 2 |

### Enzymes — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 60.6000 | 3.4000 | No | this paper | Table 2 |
| EGP (GIN) | 50.2000 | 2.7000 | Yes | this paper | Table 2 |
| GIN + BORF | 58.4000 | 2.1000 | Yes | this paper | Table 2 |
| GIN + SDRF | 50.3000 | 2.6000 | Yes | this paper | Table 2 |
| GATv2 | 37.7000 | 2.8000 | Yes | this paper | Table 2 |
| EGP (GATv2) | 38.5000 | 2.2000 | Yes | this paper | Table 2 |
| GATv2 + BORF | 37.4000 | 4.1000 | Yes | this paper | Table 2 |
| GATv2 + SDRF | 35.3000 | 3.1000 | Yes | this paper | Table 2 |
| EGP (GraphSAGE) | 42.7000 | 3.3000 | Yes | this paper | Table 2 |
| GraphSAGE + BORF | 31.0000 | 2.5000 | Yes | this paper | Table 2 |
| GraphSAGE + SDRF | 38.7000 | 2.2000 | Yes | this paper | Table 2 |

### Mutag — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 88.2000 | 3.7000 | Yes | this paper | Table 2 |
| EGP (GIN) | 91.1000 | 1.4000 | No | this paper | Table 2 |
| GIN + BORF | 88.1000 | 2.7000 | Yes | this paper | Table 2 |
| GIN + SDRF | 89.5000 | 2.6000 | Yes | this paper | Table 2 |
| GATv2 | 90.4000 | 4.3000 | Yes | this paper | Table 3 |
| EGP (GATv2) | 86.8000 | 3.9000 | No | this paper | Table 3 |
| GATv2 + BORF | 82.8000 | 3.3000 | Yes | this paper | Table 3 |
| GATv2 + SDRF | 87.2000 | 2.7000 | Yes | this paper | Table 3 |
| GraphSAGE | 88.9000 | 1.5000 | Yes | this paper | Table 3 |
| EGP (GraphSAGE) | 88.6000 | 1.2000 | No | this paper | Table 3 |
| GraphSAGE + BORF | 85.6000 | 2.4000 | Yes | this paper | Table 3 |
| GraphSAGE + SDRF | 88.1000 | 3.0000 | Yes | this paper | Table 3 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 60.7000 | 1.0000 | Yes | this paper | Table 1 |
| EGP (GIN) | 42.9000 | 0.6000 | No | this paper | Table 1 |
| GIN + BORF | 59.7000 | 0.6000 | Yes | this paper | Table 1 |
| GIN + SDRF | 56.7000 | 0.6000 | Yes | this paper | Table 1 |

### Photo — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 86.0000 | 4.5000 | Yes | this paper | Table 1 |
| EGP (GCN) | 77.9000 | 13.1000 | No | this paper | Table 1 |
| GCN + BORF | 82.0000 | 5.7000 | Yes | this paper | Table 1 |
| GCN + SDRF | 85.8000 | 4.1000 | Yes | this paper | Table 1 |

### Proteins — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 66.5000 | 2.2000 | Yes | this paper | Table 2 |
| EGP (GIN) | 68.1000 | 8.6000 | Yes | this paper | Table 2 |
| GIN + BORF | 72.6000 | 1.9000 | Yes | this paper | Table 2 |
| GIN + SDRF | 72.9000 | 1.8000 | No | this paper | Table 2 |
| GATv2 | 69.9000 | 0.7000 | Yes | this paper | Table 2 |
| EGP (GATv2) | 70.1000 | 1.9000 | Yes | this paper | Table 2 |
| GATv2 + BORF | 69.4000 | 1.5000 | Yes | this paper | Table 2 |
| GATv2 + SDRF | 69.8000 | 0.7000 | Yes | this paper | Table 2 |
| GraphSAGE | 70.1000 | 0.5000 | Yes | this paper | Table 2 |
| EGP (GraphSAGE) | 67.6000 | 0.2000 | Yes | this paper | Table 2 |
| GraphSAGE + BORF | 70.3000 | 0.9000 | Yes | this paper | Table 2 |
| GraphSAGE + SDRF | 69.7000 | 0.6000 | Yes | this paper | Table 2 |

### PubMed — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 87.7000 | 0.4000 | No | this paper | Table 1 |
| GCN + Pairnorm | 87.9000 | 0.4000 | Yes | this paper | Table 1 |
| GCNII | 88.6000 | 0.2000 | Yes | this paper | Table 1 |
| G^2-GCN | 87.6000 | 1.1000 | Yes | this paper | Table 1 |
| GATv2 | 86.7000 | 0.8000 | Yes | this paper | Table 2 |
| GATv2 + Pairnorm | 87.2000 | 0.5000 | Yes | this paper | Table 2 |
| G^2-GCN (GATv2) | 88.2000 | 0.3000 | Yes | this paper | Table 2 |
| GraphSAGE | 88.3000 | 0.4000 | Yes | this paper | Table 2 |

### Roman-Empire — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 41.5000 | 0.7000 | Yes | this paper | Table 1 |
| EGP (GCN) | 41.9000 | 0.2000 | Yes | this paper | Table 1 |
| GCN + BORF | 40.9000 | 0.7000 | Yes | this paper | Table 1 |
| GCN + SDRF | 41.6000 | 0.7000 | Yes | this paper | Table 1 |

## Baseline Models Identified

- **GCN** (from: Kipf & Welling 2017)
- **GCN + Pairnorm** (from: Zhao et al. 2020)
- **GCNII** (from: Chen et al. 2020)
- **G2-GCN** (from: Rusch et al. 2023)
- **GATv2** (from: Brody et al. 2022)
- **GraphSAGE** (from: Hamilton et al. 2017)
- **GATv2 + Pairnorm** (from: Brody et al. 2021; Zaheer et al. 2018)
- **GraphSAGE + Pairnorm** (from: Hamilton et al. 2017; Zaheer et al. 2018)
- **G^2-GCN** (from: Rusch et al. 2023)
- **G^2-GCN (GATv2)** (from: Rusch et al. 2023)
- **G^2-GCN (GraphSAGE)** (from: Rusch et al. 2023)
- **GCN + BORF** (from: Nguyen et al. 2023)
- **GCN + SDRF** (from: Topping et al. 2022)
- **EGP (GCN)** (from: this paper)
- **GIN** (from: Xu et al.)
- **GIN + BORF** (from: Nguyen et al.)
- **GIN + SDRF** (from: Topping et al.)
- **EGP (GIN)** (from: nguyen2023revisitingoversmoothingoversquashingusing)
- **EGP (GATv2)** (from: nguyen2023revisitingoversmoothingoversquashingusing)
- **GATv2 + BORF** (from: nguyen2023revisitingoversmoothingoversquashingusing)
- **GATv2 + SDRF** (from: topping2022understandingoversquashingbottlenecksgraphs)
- **EGP (GraphSAGE)** (from: nguyen2023revisitingoversmoothingoversquashingusing)
- **GraphSAGE + BORF** (from: nguyen2023revisitingoversmoothingoversquashingusing)
- **GraphSAGE + SDRF** (from: topping2022understandingoversquashingbottlenecksgraphs)

## Extraction Notes

[Cora] Extracted best-performing layer configurations for Cora from Table 1 and Table 2. Table 1
contains GCN-based variants. Table 2 contains GATv2 and GraphSAGE variants. Values in parentheses
are standard deviations. Bolded values indicate the best performance for that model across layers,
which were selected as the primary result for each model. [CiteSeer] Extracted results for CiteSeer
from Table 2. The table reports Accuracy (%) with standard deviation in brackets. The best
performing model depth is highlighted in bold. The proposed model is G² (and its variants with
GATv2/GraphSAGE). All other models are baselines. The values correspond to the best performing layer
depth for each model as indicated by the bold formatting in the table. [PubMed] Extracted best-
performing layer configurations for PubMed from Table 1 and Table 2. Table 1 contains GCN,
GCN+Pairnorm, GCNII, and G^2-GCN. Table 2 contains the same plus GATv2 variants and GraphSAGE
variants. For each model, the layer count with the highest accuracy is selected (e.g., GCNII at 64
layers, GCN at 2 layers). The values in parentheses are standard deviations. Note: The text in Table
2 for GraphSAGE is cut off, but the value '88.3 (0.4)' is visible for 2 layers, which is the best
for that model in the visible portion. GATv2 at 2 layers is OOM, so best is at 4 layers. [Roman-
Empire] Extracted results for Roman-Empire from Table 1 (tab:results_squashing_node). The table
reports Accuracy (%) with standard deviation in brackets for different layer depths. The optimal
depth per model is underlined. For Roman-Empire, the optimal depth for all models was 2 layers. The
values extracted correspond to the underlined (best) values for each model on this dataset. The
paper does not propose a single new model but evaluates GCN against mitigation techniques (EGP,
BORF, SDRF). GCN is treated as the baseline/standard model here. [Photo] Extracted results for the
'Photo' dataset from Table 1. The table reports Accuracy (%) with standard deviation in brackets for
different layer depths. The best performing model (GCN at 2 layers) is highlighted in bold. The
optimal depth per model is underlined. Only the 2-layer results are extracted as they represent the
optimal performance for all models on this dataset according to the table's underlining and the
paper's conclusion that shallow models often perform best. Other layer depths show significant
performance degradation (over-smoothing/squashing effects) and are not the primary benchmark results
for comparison. [Computers] Extracted results for the 'Computers' dataset from Table 1. The table
reports Accuracy (%) with standard deviation in brackets. Only the best performing depth
(underlined) is reported for each model, which corresponds to the primary benchmark result for that
configuration. The proposed model is identified as EGP (GCN) based on the caption and context of
mitigating over-squashing. [Mutag] Extracted best-performing results (underlined) for the Mutag
dataset from Table 2 and Table 3. The paper reports results for multiple layer depths; the
underlined value represents the optimal depth for that specific model configuration. EGP is the
proposed method, applied on top of GIN, GATv2, and GraphSAGE. Standard deviations are provided in
parentheses in the table. [Enzymes] Extracted results for the 'Enzymes' dataset from Table 2 (Full
table of experiments on graph-level tasks). The table reports Accuracy (%) with standard deviation
in brackets. The 'best performing model' is highlighted in bold and the 'optimal depth per model and
dataset' is underlined. For each model, the value corresponding to the underlined layer count is the
optimal result reported for that model on this dataset. All other layer configurations are secondary
and thus excluded to focus on the primary benchmark result per model. The proposed model is
identified as GIN based on the context of the paper comparing GIN against mitigation techniques.
[Proteins] Extracted only the 'Proteins' dataset rows from Table 2. The table reports Accuracy (%)
with standard deviation in brackets. The best performing model per dataset is bolded and underlined.
For Proteins, GIN + SDRF achieved the best result (72.9%). All values correspond to the optimal
depth configuration for each model as indicated by the underline in the source table. [Peptides-
func] Extracted results for Peptides-func from Table 1. The table reports Average Precision (AP) in
percent. The best performing model per dataset is highlighted in bold and optimal depth underlined.
For Peptides-func, GIN at 4 layers achieved the best result (60.7%). The proposed model EGP (GIN)
achieved 42.9% at 4 layers. Other configurations for EGP (GIN) at different depths are significantly
lower and not reported in the second table for Peptides-func, but Table 1 covers the primary
comparison. Note: The second table (Table 2) cuts off before showing Peptides-func results for
GATv2/GraphSAGE variants, so only GIN-based variants are extracted from Table 1 which contains the
full set for this dataset.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*