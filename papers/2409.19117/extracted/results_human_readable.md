# Extraction: arXiv:2409.19117
**Model used**: `alias-huge-no-thinking`  **Date**: 2026-05-13  **Confidence**: HIGH

## Proposed Model: MPNN + HOPE-WavePE (ours)
- Type: GNN

## Results

### BACE — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| D-MPNN | 0.8090 | 0.0060 | Yes | yang2019analyzing | Table 1 |
| AttentiveFP | 0.7840 | 0.0000 | Yes | xiong2019pushing | Table 1 |
| N-GramRF | 0.7790 | 0.0150 | Yes | N_gram | Table 1 |
| N-GramXGB | 0.7910 | 0.0130 | Yes | N_gram | Table 1 |
| PretrainGNN | 0.7990 | 0.0090 | Yes | strategies_pretrain | Table 1 |
| GROVERbase | 0.8260 | 0.0070 | Yes | GROVER | Table 1 |
| GROVERlarge | 0.8100 | 0.0140 | Yes | GROVER | Table 1 |
| GraphLOG pretrained | 0.8350 | 0.0120 | Yes | GraphLog | Table 1 |
| GraphCL pretrained | 0.7540 | 0.0140 | Yes | GraphCL | Table 1 |
| InfoGraph pretrained | 0.6480 | 0.0070 | Yes | InfoGraph | Table 1 |
| MPNN + HOPE-WavePE (ours) | 0.8680 | 0.0040 | No | this paper | Table 1 |

### BBBP — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| D-MPNN | 0.7100 | 0.0030 | Yes | yang2019analyzing | Table 1 |
| AttentiveFP | 0.6430 | 0.0180 | Yes | xiong2019pushing | Table 1 |
| N-GramRF | 0.6970 | 0.0060 | Yes | N_gram | Table 1 |
| N-GramXGB | 0.6910 | 0.0080 | Yes | N_gram | Table 1 |
| PretrainGNN | 0.6870 | 0.0130 | Yes | strategies_pretrain | Table 1 |
| GROVERbase | 0.7000 | 0.0010 | Yes | GROVER | Table 1 |
| GROVERlarge | 0.6950 | 0.0010 | Yes | GROVER | Table 1 |
| GraphLOG pretrained | 0.7250 | 0.0080 | Yes | GraphLog | Table 1 |
| GraphCL pretrained | 0.6970 | 0.0070 | Yes | GraphCL | Table 1 |
| InfoGraph pretrained | 0.6630 | 0.0060 | Yes | InfoGraph | Table 1 |
| MPNN + HOPE-WavePE (ours) | 0.7120 | 0.0040 | No | this paper | Table 1 |

### CIFAR10 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.5526 | 0.0153 | Yes | this paper | Table 4 |
| GAT | 0.6422 | 0.0045 | Yes | this paper | Table 4 |
| GatedGCN | 0.6731 | 0.0031 | Yes | this paper | Table 4 |
| Graph MLP-Mixer | 0.7246 | 0.0036 | Yes | this paper | Table 4 |
| GPS + none | 0.7176 | 0.0001 | Yes | this paper | Table 4 |
| GPS + (RWSE/LapPE) | 0.7230 | 0.0036 | Yes | this paper | Table 4 |
| GPS + HOPE-WavePE (ours) | 0.7301 | 0.0081 | No | this paper | Table 4 |

### IMDB-B — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| WL kernel | 0.7380 | 0.0390 | Yes | this paper | Table 3 |
| DCNN | 0.4910 | 0.0140 | Yes | this paper | Table 3 |
| DGCNN | 0.7000 | 0.0090 | Yes | this paper | Table 3 |
| IGN | 0.7200 | 0.0550 | Yes | this paper | Table 3 |
| GIN | 0.7510 | 0.0510 | Yes | this paper | Table 3 |
| PPGNs | 0.7300 | 0.0580 | Yes | this paper | Table 3 |
| Natural GN | 0.7350 | 0.0200 | Yes | this paper | Table 3 |
| GSN | 0.7780 | 0.0330 | Yes | this paper | Table 3 |
| SIN | 0.7560 | 0.0320 | Yes | this paper | Table 3 |
| CIN | 0.7560 | 0.0370 | Yes | this paper | Table 3 |
| GIN + HOPE-WavePE (ours) | 0.7600 | 0.0370 | No | this paper | Table 3 |

### MNIST — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.9649 | 0.0025 | Yes | this paper | Table 4 |
| GAT | 0.9553 | 0.0020 | Yes | this paper | Table 4 |
| GatedGCN | 0.9734 | 0.0014 | Yes | this paper | Table 4 |
| Graph MLP-Mixer | 0.9835 | 0.0010 | Yes | this paper | Table 4 |
| GPS + none | 0.9805 | 0.0000 | Yes | this paper | Table 4 |
| GPS + (RWSE/LapPE) | 0.9805 | 0.0013 | Yes | this paper | Table 4 |
| GPS + HOPE-WavePE (ours) | 0.9815 | 0.0011 | No | this paper | Table 4 |

### MUTAG — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| RWK | 0.7920 | 0.0210 | Yes | this paper | Table: TU datasets |
| GK (k=3) | 0.8140 | 0.0170 | Yes | this paper | Table: TU datasets |
| PK | 0.7600 | 0.0270 | Yes | this paper | Table: TU datasets |
| WL kernel | 0.9040 | 0.0570 | Yes | this paper | Table: TU datasets |
| DGCNN | 0.8580 | 0.0180 | Yes | this paper | Table: TU datasets |
| IGN | 0.8390 | 0.1300 | Yes | this paper | Table: TU datasets |
| GIN | 0.8940 | 0.0560 | Yes | this paper | Table: TU datasets |
| PPGNs | 0.9060 | 0.0870 | Yes | this paper | Table: TU datasets |
| Natural GN | 0.8940 | 0.0160 | Yes | this paper | Table: TU datasets |
| GSN | 0.9220 | 0.0750 | Yes | this paper | Table: TU datasets |
| CIN | 0.9270 | 0.0610 | Yes | this paper | Table: TU datasets |
| GIN + HOPE-WavePE (ours) | 0.9360 | 0.0580 | No | this paper | Table: TU datasets |

### NCI1 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GK (k=3) | 0.6250 | 0.0030 | Yes | this paper | Table 3 |
| PK | 0.8250 | 0.0050 | Yes | this paper | Table 3 |
| WL kernel | 0.8600 | 0.0180 | Yes | this paper | Table 3 |
| DCNN | 0.5660 | 0.0100 | Yes | this paper | Table 3 |
| DGCNN | 0.7440 | 0.0050 | Yes | this paper | Table 3 |
| IGN | 0.7430 | 0.0270 | Yes | this paper | Table 3 |
| GIN | 0.8270 | 0.0170 | Yes | this paper | Table 3 |
| PPGNs | 0.8320 | 0.0110 | Yes | this paper | Table 3 |
| Natural GN | 0.8240 | 0.0130 | Yes | this paper | Table 3 |
| GSN | 0.8350 | 0.0200 | Yes | this paper | Table 3 |
| SIN | 0.8270 | 0.0210 | Yes | this paper | Table 3 |
| CIN | 0.8360 | 0.0140 | Yes | this paper | Table 3 |
| GIN + HOPE-WavePE (ours) | 0.8450 | 0.0200 | No | this paper | Table 3 |

### NCI109 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GK (k=3) | 0.6240 | 0.0030 | Yes | this paper | Table 3 |
| IGN | 0.7280 | 0.0150 | Yes | this paper | Table 3 |
| PPGNs | 0.8220 | 0.0140 | Yes | this paper | Table 3 |
| CIN | 0.8400 | 0.0160 | Yes | this paper | Table 3 |
| GIN + HOPE-WavePE (ours) | 0.8310 | 0.0190 | No | this paper | Table 3 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5930 | 0.0023 | Yes | this paper | Table 2 |
| GINE | 0.5498 | 0.0079 | Yes | this paper | Table 2 |
| GatedGCN | 0.5864 | 0.0077 | Yes | this paper | Table 2 |
| GatedGCN + RWSE | 0.6069 | 0.0035 | Yes | this paper | Table 2 |
| Drew-GCN + LapPE | 0.7150 | 0.0044 | Yes | this paper | Table 2 |
| GraphGPS + LapPE | 0.6535 | 0.0041 | Yes | this paper | Table 2 |
| GRIT | 0.6988 | 0.0082 | Yes | this paper | Table 2 |
| Graph VIT | 0.6942 | 0.0075 | Yes | this paper | Table 2 |
| GraphMLP Mixer | 0.6921 | 0.0054 | Yes | this paper | Table 2 |
| GatedGCN + VN + RWSE | 0.6685 | 0.0062 | Yes | this paper | Table 2 |
| GatedGCN + VN + HOPE-WavePE (ours) | 0.7171 | 0.0023 | No | this paper | Table 2 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3496 | 0.0013 | Yes | this paper | tab:LRGB |
| GINE | 0.6346 | 0.0071 | Yes | this paper | tab:LRGB |
| GatedGCN | 0.3420 | 0.0013 | Yes | this paper | tab:LRGB |
| GatedGCN + RWSE | 0.3357 | 0.0006 | Yes | this paper | tab:LRGB |
| Drew-GCN + LapPE | 0.2536 | 0.0015 | Yes | this paper | tab:LRGB |
| GraphGPS + LapPE | 0.2500 | 0.0005 | Yes | this paper | tab:LRGB |
| GRIT | 0.2460 | 0.0012 | Yes | this paper | tab:LRGB |
| Graph VIT | 0.2449 | 0.0016 | Yes | this paper | tab:LRGB |
| GraphMLP Mixer | 0.2475 | 0.0015 | Yes | this paper | tab:LRGB |
| GatedGCN + VN + RWSE | 0.2529 | 0.0009 | Yes | this paper | tab:LRGB |
| GatedGCN + VN + HOPE-WavePE (ours) | 0.2433 | 0.0011 | No | this paper | tab:LRGB |

### SIDER — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| D-MPNN | 0.5700 | 0.0030 | Yes | this paper | Table 1 |
| AttentiveFP | 0.6060 | 0.0320 | Yes | this paper | Table 1 |
| N-GramRF | 0.6680 | 0.0070 | Yes | this paper | Table 1 |
| N-GramXGB | 0.6550 | 0.0070 | Yes | this paper | Table 1 |
| PretrainGNN | 0.6270 | 0.0080 | Yes | this paper | Table 1 |
| GROVERbase | 0.6480 | 0.0060 | Yes | this paper | Table 1 |
| GROVERlarge | 0.6540 | 0.0010 | Yes | this paper | Table 1 |
| GraphLOG pretrained | 0.6120 | 0.0110 | Yes | this paper | Table 1 |
| GraphCL pretrained | 0.6050 | 0.0090 | Yes | this paper | Table 1 |
| InfoGraph pretrained | 0.5710 | 0.0080 | Yes | this paper | Table 1 |
| MPNN + HOPE-WavePE (ours) | 0.6470 | 0.0030 | No | this paper | Table 1 |

### Tox21 — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| D-MPNN | 0.7590 | 0.0070 | Yes | this paper | Table 1 |
| AttentiveFP | 0.7610 | 0.0050 | Yes | this paper | Table 1 |
| N-GramRF | 0.7430 | 0.0040 | Yes | this paper | Table 1 |
| N-GramXGB | 0.7580 | 0.0090 | Yes | this paper | Table 1 |
| PretrainGNN | 0.7670 | 0.0040 | Yes | this paper | Table 1 |
| GROVERbase | 0.7430 | 0.0010 | Yes | this paper | Table 1 |
| GROVERlarge | 0.7350 | 0.0010 | Yes | this paper | Table 1 |
| GraphLOG pretrained | 0.7570 | 0.0050 | Yes | this paper | Table 1 |
| GraphCL pretrained | 0.7390 | 0.0070 | Yes | this paper | Table 1 |
| InfoGraph pretrained | 0.6810 | 0.0060 | Yes | this paper | Table 1 |
| MPNN + HOPE-WavePE (ours) | 0.7800 | 0.0010 | No | this paper | Table 1 |

### ZINC — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.5260 | 0.0510 | Yes | this paper | Table 4 |
| GAT | 0.3840 | 0.0070 | Yes | this paper | Table 4 |
| GatedGCN | 0.2820 | 0.0150 | Yes | this paper | Table 4 |
| Graph MLP-Mixer | 0.0770 | 0.0030 | Yes | this paper | Table 4 |
| GPS + (RWSE/LapPE) | 0.0700 | 0.0040 | Yes | this paper | Table 4 |
| GPS + HOPE-WavePE (ours) | 0.0670 | 0.0020 | No | this paper | Table 4 |

### ogbl-ppa — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| HOPE-WavePE | 0.9912 | — | No | this paper | Table 5 |

## Baseline Models Identified

- **D-MPNN** (from: yang2019analyzing)
- **AttentiveFP** (from: xiong2019pushing)
- **N-GramRF** (from: N_gram)
- **N-GramXGB** (from: N_gram)
- **PretrainGNN** (from: strategies_pretrain)
- **GROVERbase** (from: GROVER)
- **GROVERlarge** (from: GROVER)
- **GraphLOG pretrained** (from: GraphLog)
- **GraphCL pretrained** (from: GraphCL)
- **InfoGraph pretrained** (from: InfoGraph)
- **GCN**
- **GINE**
- **GatedGCN**
- **GatedGCN + RWSE**
- **Drew-GCN + LapPE**
- **GraphGPS + LapPE**
- **GRIT**
- **Graph VIT**
- **GraphMLP Mixer**
- **GatedGCN + VN + RWSE**
- **RWK**
- **GK (k=3)**
- **PK**
- **WL kernel**
- **DGCNN**
- **IGN** (from: Maron 2018)
- **GIN**
- **PPGNs**
- **Natural GN**
- **GSN**
- **CIN**
- **DCNN**
- **SIN**
- **GAT**
- **Graph MLP-Mixer**
- **GPS + none**
- **GPS + (RWSE/LapPE)**

## Extraction Notes

[BBBP] Only Table 1 contains BBBP results. ROC-AUC values were reported as percentages and
normalized to [0,1]. No model parameter counts were provided in the paper. Pretrained baselines are
marked as uses_external_data=true based on their names and known pretraining methodologies. [BACE]
Extracted BACE results from Table 1 only; no other tables contain BACE results. Values were reported
as percentages and normalized to the [0,1] range. Standard deviations were parsed from parentheses
and normalized accordingly. [Tox21] Only Table 1 contains Tox21 results. ROC-AUC values were
reported as percentages and have been normalized to the [0,1] range. All models shown were evaluated
on the scaffold-split Tox21 benchmark. [ToxCast] failed: 1 validation error for ExtractionOutput
Input should be a valid dictionary or instance of ExtractionOutput [type=model_type,
input_value=[{'name': 'D-MPNN', 'para...per_hint': 'InfoGraph'}], input_type=list]     For further
information visit https://errors.pydantic.dev/2.13/v/model_type [SIDER] Extracted SIDER results from
the moleculeNet scaffold-split classification table (Table 1). ROC-AUC values were reported as
percentages and normalized to [0,1]. Only a single standard SIDER column was present, so no optional
variants were skipped. All other provided tables do not contain SIDER results. [Peptides-struct]
Extracted all rows for Peptides-struct MAE from the LRGB table (tab:LRGB). Values and standard
deviations are clearly reported. Parameter counts are not mentioned in the provided text. Peptides-
func AP column and all other tables were omitted per the focus instructions. [Peptides-func] All
Peptides-func AP values were cleanly extracted from the single LRGB results table. No parameter
counts are reported in the paper. The proposed model leverages an autoencoder pretrained on MolPCA
and Peptides-func; marked uses_external_data=true because pretraining incorporates MolPCA, which is
external to the LRGB benchmark. [MUTAG] Extracted only the MUTAG column from the TU datasets table.
Accuracy percentages were normalized to [0,1]. DCNN and SIN had no MUTAG result (-) and were
skipped. No parameter counts were reported for any model. The proposed model uses a pretrained
autoencoder as part of HOPE-WavePE, but no external benchmark data was indicated for the standard
MUTAG evaluation. [PROTEINS] failed: 1 validation error for ExtractionOutput   Input should be a
valid dictionary or instance of ExtractionOutput [type=model_type, input_value=[{'name': 'RWK',
'params_...nal_paper_hint': 'CIN'}], input_type=list]     For further information visit
https://errors.pydantic.dev/2.13/v/model_type [NCI1] RWK on NCI1 is reported as '>3 days' and was
skipped because it is not a numerical value. All other NCI1 accuracy values were extracted from the
TU datasets table (label tab:tu_dataset_result). Values were reported as percentages and normalized
to the [0,1] range. No parameter counts or external data usage indicators were provided in the paper
text. [NCI109] Extracted NCI109 results from the TU datasets table (Table 3). Accuracy percentages
were normalized to [0,1]. Parameter counts were not reported. The proposed method employs a
pretrained autoencoder, but the pretraining data source was not specified, so uses_external_data is
marked null. Rows with '-' for NCI109 were skipped. [IMDB-B] Only Table 3 (TU datasets) contained
IMDB-B results. Accuracy percentages were normalized to [0,1]. Baselines RWK, GK (k=3), and PK had
no IMDB-B entry ('-') and were omitted. Parameter counts were not reported for any model. The
proposed method uses a pretrained autoencoder; it is unclear whether pretraining used only benchmark
data, so uses_external_data is set to null for the proposed model. [IMDB-M] failed: 1 validation
error for ExtractionOutput   Input should be a valid dictionary or instance of ExtractionOutput
[type=model_type, input_value=[{'name': 'RWK', 'params_...nal_paper_hint': 'CIN'}], input_type=list]
For further information visit https://errors.pydantic.dev/2.13/v/model_type [CIFAR10] Only Table 4
contains CIFAR10 results. Accuracy values were reported as percentages and normalized to [0,1]. No
parameter counts or external data usage are mentioned for these CIFAR10 results. All rows from the
CIFAR10 column are extracted. [MNIST] Extracted MNIST results from the image classification table
(Table 4). Cross-domain training table skipped as it represents an optional variant/configuration.
Values were percentage-based and normalized to [0,1]. No parameter counts were reported in the
provided text. [ZINC] Only Table 4 reports ZINC results with the standard MAE metric. Table 5
(cross-domain training) reports accuracy on ZINC but was skipped because it is not the standard
benchmark MAE score. GPS + none has no ZINC result (reported as '-'). Parameter counts are not
provided in the text. [ogbl-collab] The provided tables contain no ogbl-collab results measured by
Hits@50. The only mention of ogbl-collab is in the cross-domain training table, which reports
Accuracy (not Hits@50) under a non-standard transfer setting; those rows were skipped per the focus
instructions. All other tables cover unrelated datasets (MolecularNet, Peptides-func/struct, TU
datasets, CIFAR10, MNIST, ZINC). [ogbl-ppa] Only Table 5 (cross-domain training) contains results
for ogbl-ppa. The table reports accuracy for HOPE-WavePE under four different training-domain
variants. Following the instruction to use only the standard/default configuration, only the in-
domain diagonal entry (row 'Interaction Network' / 'ogbl-ppa', column 'ogbl-ppa') was extracted; the
off-diagonal cross-domain entries were treated as optional variants and skipped. No baseline results
are reported for ogbl-ppa in the provided tables.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*