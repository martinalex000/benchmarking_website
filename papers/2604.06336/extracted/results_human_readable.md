# Extraction: BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular Representation Learning
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: BiScale-GTR
- Type: GNN

## Results

### BACE — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GraphMVP | 0.7930 | 0.0150 | Yes | Liu et al. 2021 | Table 1 |
| GraphMAE | 0.7820 | 0.0150 | Yes | Hou et al. 2022 | Table 1 |
| Mole-BERT | 0.8080 | 0.0140 | Yes | Xia et al. 2023 | Table 1 |
| SimSGT | 0.8430 | 0.0060 | Yes | Liu et al. 2023 | Table 1 |
| GraphFP | 0.8050 | 0.0180 | Yes | Luong et al. 2023 | Table 1 |
| MORE | 0.8280 | 0.0130 | Yes | Son et al. 2025 | Table 1 |
| GraphGPS+LAC | 0.8250 | — | Yes | Yang et al. 2025 | Table 1 |
| BiScale-GTR (Fragment) | 0.8380 | 0.0120 | No | this paper | Table 1 |
| BiScale-GTR (Molecule) | 0.8500 | 0.0110 | No | this paper | Table 1 |

### BBBP — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GraphMVP | 0.7080 | 0.0050 | Yes | Liu et al. 2021 | Table 1 |
| GraphMAE | 0.7120 | 0.0100 | Yes | Hou et al. 2022 | Table 1 |
| Mole-BERT | 0.7190 | 0.0080 | Yes | Xia et al. 2023 | Table 1 |
| SimSGT | 0.7220 | 0.0090 | Yes | Liu et al. 2023 | Table 1 |
| GraphFP | 0.7200 | 0.0170 | Yes | Luong et al. 2023 | Table 1 |
| MORE | 0.7190 | 0.0090 | Yes | Son et al. 2025 | Table 1 |
| GraphGPS+LAC | 0.7360 | — | Yes | Yang et al. 2025 | Table 1 |
| BiScale-GTR (Fragment) | 0.7380 | 0.0040 | No | this paper | Table 1 |
| BiScale-GTR (Molecule) | 0.6840 | 0.0080 | No | this paper | Table 1 |

### CYP2C9 — RMSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| RF | 18.4710 | — | Yes | Rigatti 2017 | Table 1 |
| XGBoost | 17.5820 | — | Yes | Chen 2016 | Table 1 |
| CMPNN | 18.3770 | — | Yes | Swanson 2019 | Table 1 |
| FPGNN | 16.9330 | — | Yes | Cai 2022 | Table 1 |
| DHTNN | 17.4490 | — | Yes | Song 2023 | Table 1 |
| KANO | 17.3500 | — | Yes | Li 2023 | Table 1 |
| MPG | 17.4170 | — | Yes | Li 2020 | Table 1 |
| UniMol | 17.7740 | — | Yes | Zhou 2023 | Table 1 |
| Trans-M | 18.0800 | — | Yes | Luo 2022 | Table 1 |
| KP-GPT | 17.0360 | — | Yes | Wu 2018 | Table 1 |
| GraphFP | 17.3670 | — | Yes | Luong 2023 | Table 1 |
| FraGAT | 17.7880 | — | Yes | Zhang 2021 | Table 1 |
| PharmHGT | 17.4900 | — | Yes | Jiang 2023 | Table 1 |
| FragFormer | 16.8550 | — | Yes | Wang 2025 | Table 1 |
| BiScale-GTR (Molecule) | 16.6330 | — | No | this paper | Table 1 |

### CYP2D6 — RMSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| RF | 18.0410 | — | Yes | this paper | Table 1 |
| XGBoost | 17.8190 | — | Yes | this paper | Table 1 |
| CMPNN | 19.1560 | — | Yes | this paper | Table 1 |
| FPGNN | 17.6110 | — | Yes | this paper | Table 1 |
| DHTNN | 17.8900 | — | Yes | this paper | Table 1 |
| KANO | 17.6220 | — | Yes | this paper | Table 1 |
| MPG | 17.5270 | — | Yes | this paper | Table 1 |
| UniMol | 18.0710 | — | Yes | this paper | Table 1 |
| Trans-M | 17.6770 | — | Yes | this paper | Table 1 |
| KP-GPT | 16.8600 | — | Yes | this paper | Table 1 |
| GraphFP | 21.1830 | — | Yes | this paper | Table 1 |
| FraGAT | 22.5030 | — | Yes | this paper | Table 1 |
| PharmHGT | 15.0200 | — | Yes | this paper | Table 1 |
| FragFormer | 14.4250 | — | Yes | this paper | Table 1 |
| BiScale-GTR (Molecule) | 16.9010 | — | No | this paper | Table 1 |

### CYP3A4 — RMSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| RF | 16.5400 | — | Yes | this paper | Table 1 |
| XGBoost | 16.1230 | — | Yes | this paper | Table 1 |
| CMPNN | 16.7010 | — | Yes | this paper | Table 1 |
| FPGNN | 15.6060 | — | Yes | this paper | Table 1 |
| DHTNN | 16.1560 | — | Yes | this paper | Table 1 |
| KANO | 15.3070 | — | Yes | this paper | Table 1 |
| MPG | 14.3760 | — | Yes | this paper | Table 1 |
| UniMol | 15.8950 | — | Yes | this paper | Table 1 |
| Trans-M | 15.8670 | — | Yes | this paper | Table 1 |
| KP-GPT | 16.3790 | — | Yes | this paper | Table 1 |
| GraphFP | 17.2190 | — | Yes | this paper | Table 1 |
| FraGAT | 20.3130 | — | Yes | this paper | Table 1 |
| PharmHGT | 16.0770 | — | Yes | this paper | Table 1 |
| FragFormer | 15.8940 | — | Yes | this paper | Table 1 |
| BiScale-GTR (Molecule) | 16.0110 | — | No | this paper | Table 1 |

### HIV — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GraphMVP | 0.7600 | 0.0010 | Yes | Liu 2021 | Table 1 |
| GraphMAE | 0.7680 | 0.0060 | Yes | Hou 2022 | Table 1 |
| Mole-BERT | 0.7820 | 0.0080 | Yes | Xia 2023 | Table 1 |
| SimSGT | 0.7800 | 0.0190 | Yes | Liu 2023 | Table 1 |
| GraphFP | 0.7800 | 0.0150 | Yes | Luong 2023 | Table 1 |
| MORE | 0.7700 | 0.0070 | Yes | Son 2025 | Table 1 |
| GraphGPS+LAC | 0.7760 | — | Yes | Yang 2025 | Table 1 |
| BiScale-GTR (Fragment) | 0.7790 | 0.0110 | No | this paper | Table 1 |
| BiScale-GTR (Molecule) | 0.7920 | 0.0060 | No | this paper | Table 1 |

### HLMC — RMSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| RF | 0.8130 | — | Yes | this paper | Table 1 |
| XGBoost | 0.6470 | — | Yes | this paper | Table 1 |
| CMPNN | 0.9210 | — | Yes | this paper | Table 1 |
| FPGNN | 0.6040 | — | Yes | this paper | Table 1 |
| DHTNN | 0.7290 | — | Yes | this paper | Table 1 |
| KANO | 0.5540 | — | Yes | this paper | Table 1 |
| MPG | 0.5410 | — | Yes | this paper | Table 1 |
| UniMol | 0.6130 | — | Yes | this paper | Table 1 |
| Trans-M | 0.5670 | — | Yes | this paper | Table 1 |
| KP-GPT | 0.5640 | — | Yes | this paper | Table 1 |
| GraphFP | 0.7640 | — | Yes | this paper | Table 1 |
| FraGAT | 0.7750 | — | Yes | this paper | Table 1 |
| PharmHGT | 0.5440 | — | Yes | this paper | Table 1 |
| FragFormer | 0.5140 | — | Yes | this paper | Table 1 |
| BiScale-GTR (Molecule) | 0.5010 | — | No | this paper | Table 1 |

### LogD — RMSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| RF | 1.2490 | — | Yes | this paper | Table 1 |
| XGBoost | 1.0710 | — | Yes | this paper | Table 1 |
| CMPNN | 0.8070 | — | Yes | this paper | Table 1 |
| FPGNN | 0.8380 | — | Yes | this paper | Table 1 |
| DHTNN | 0.9120 | — | Yes | this paper | Table 1 |
| KANO | 0.7660 | — | Yes | this paper | Table 1 |
| MPG | 0.7580 | — | Yes | this paper | Table 1 |
| UniMol | 0.7450 | — | Yes | this paper | Table 1 |
| Trans-M | 0.7370 | — | Yes | this paper | Table 1 |
| KP-GPT | 0.7280 | — | Yes | this paper | Table 1 |
| GraphFP | 0.8350 | — | Yes | this paper | Table 1 |
| FraGAT | 0.9450 | — | Yes | this paper | Table 1 |
| PharmHGT | 0.6760 | — | Yes | this paper | Table 1 |
| FragFormer | 0.6670 | — | Yes | this paper | Table 1 |
| BiScale-GTR (Molecule) | 0.8010 | — | No | this paper | Table 1 |

### MLMC — RMSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| RF | 0.9870 | — | Yes | this paper | Table 1 |
| XGBoost | 0.8440 | — | Yes | this paper | Table 1 |
| CMPNN | 1.1300 | — | Yes | this paper | Table 1 |
| FPGNN | 0.7740 | — | Yes | this paper | Table 1 |
| DHTNN | 0.9260 | — | Yes | this paper | Table 1 |
| KANO | 0.7670 | — | Yes | this paper | Table 1 |
| MPG | 0.7230 | — | Yes | this paper | Table 1 |
| UniMol | 0.8240 | — | Yes | this paper | Table 1 |
| Trans-M | 0.7440 | — | Yes | this paper | Table 1 |
| KP-GPT | 0.7260 | — | Yes | this paper | Table 1 |
| GraphFP | 0.8780 | — | Yes | this paper | Table 1 |
| FraGAT | 0.8490 | — | Yes | this paper | Table 1 |
| PharmHGT | 0.8200 | — | Yes | this paper | Table 1 |
| FragFormer | 0.7020 | — | Yes | this paper | Table 1 |
| BiScale-GTR (Molecule) | 0.6960 | — | No | this paper | Table 1 |

### PPB — RMSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| RF | 0.2040 | — | Yes | this paper | Table 1 |
| XGBoost | 0.1860 | — | Yes | this paper | Table 1 |
| CMPNN | 0.2360 | — | Yes | this paper | Table 1 |
| FPGNN | 0.1790 | — | Yes | this paper | Table 1 |
| DHTNN | 0.2350 | — | Yes | this paper | Table 1 |
| KANO | 0.1850 | — | Yes | this paper | Table 1 |
| MPG | 0.1700 | — | Yes | this paper | Table 1 |
| UniMol | 0.1790 | — | Yes | this paper | Table 1 |
| Trans-M | 0.1720 | — | Yes | this paper | Table 1 |
| KP-GPT | 0.1720 | — | Yes | this paper | Table 1 |
| GraphFP | 0.2080 | — | Yes | this paper | Table 1 |
| FraGAT | 0.2200 | — | Yes | this paper | Table 1 |
| PharmHGT | 0.1720 | — | Yes | this paper | Table 1 |
| FragFormer | 0.1570 | — | Yes | this paper | Table 1 |
| BiScale-GTR (Molecule) | 0.1530 | — | No | this paper | Table 1 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5930 | 0.0023 | Yes | this paper | Table 1 |
| GCNII | 0.5543 | 0.0078 | Yes | this paper | Table 1 |
| GINE | 0.5498 | 0.0079 | Yes | this paper | Table 1 |
| GatedGCN | 0.5864 | 0.0077 | Yes | this paper | Table 1 |
| GatedGCN+RWSE | 0.6069 | 0.0035 | Yes | this paper | Table 1 |
| Transformer + LapPE | 0.6326 | 0.0126 | Yes | this paper | Table 1 |
| SAN + LapPE | 0.6384 | 0.0121 | Yes | this paper | Table 1 |
| SAN + RWSE | 0.6439 | 0.0075 | Yes | this paper | Table 1 |
| GraphFP | 0.6267 | 0.0073 | Yes | this paper | Table 1 |
| FragFormer | 0.6693 | 0.0154 | Yes | this paper | Table 1 |
| BiScale-GTR | 0.6717 | 0.0107 | No | this paper | Table 1 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3496 | 0.0013 | Yes | this paper | Table 1 |
| GCNII | 0.3471 | 0.0010 | Yes | this paper | Table 1 |
| GINE | 0.3547 | 0.0045 | Yes | this paper | Table 1 |
| GatedGCN | 0.3420 | 0.0013 | Yes | this paper | Table 1 |
| GatedGCN+RWSE | 0.3357 | 0.0006 | Yes | this paper | Table 1 |
| Transformer + LapPE | 0.2529 | 0.0016 | Yes | this paper | Table 1 |
| SAN + LapPE | 0.2683 | 0.0043 | Yes | this paper | Table 1 |
| SAN + RWSE | 0.2545 | 0.0012 | Yes | this paper | Table 1 |
| GraphFP | 0.3137 | 0.0019 | Yes | this paper | Table 1 |
| BiScale-GTR (Molecule) | 0.2621 | 0.0022 | No | this paper | Table 1 |
| Graph BPE (with validity/OOV handling) | 0.2621 | — | Yes | this paper | Table 2 |

### RLMC — RMSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| RF | 0.9580 | — | Yes | Niu 2024 | Table 1 |
| XGBoost | 0.8190 | — | Yes | Niu 2024 | Table 1 |
| CMPNN | 0.9390 | — | Yes | Niu 2024 | Table 1 |
| FPGNN | 0.7160 | — | Yes | Niu 2024 | Table 1 |
| DHTNN | 0.9150 | — | Yes | Niu 2024 | Table 1 |
| KANO | 0.7620 | — | Yes | Niu 2024 | Table 1 |
| MPG | 0.6850 | — | Yes | Niu 2024 | Table 1 |
| UniMol | 0.6510 | — | Yes | Niu 2024 | Table 1 |
| Trans-M | 0.6770 | — | Yes | Niu 2024 | Table 1 |
| KP-GPT | 0.8810 | — | Yes | Niu 2024 | Table 1 |
| GraphFP | 0.7710 | — | Yes | Niu 2024 | Table 1 |
| FraGAT | 1.0500 | — | Yes | Niu 2024 | Table 1 |
| PharmHGT | 0.6770 | — | Yes | Niu 2024 | Table 1 |
| FragFormer | 0.5960 | — | Yes | Niu 2024 | Table 1 |
| BiScale-GTR (Molecule) | 0.5710 | — | No | this paper | Table 1 |

### SIDER — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GraphMVP | 0.6020 | 0.0110 | Yes | Liu et al. 2021 | Table 1 |
| GraphMAE | 0.6050 | 0.0120 | Yes | Hou et al. 2022 | Table 1 |
| Mole-BERT | 0.6280 | 0.0110 | Yes | Xia et al. 2023 | Table 1 |
| SimSGT | 0.6170 | 0.0080 | Yes | Liu et al. 2023 | Table 1 |
| GraphFP | 0.6360 | 0.0120 | Yes | Luong et al. 2023 | Table 1 |
| MORE | 0.6090 | 0.0060 | Yes | Son et al. 2025 | Table 1 |
| GraphGPS+LAC | 0.6040 | — | Yes | Yang et al. 2025 | Table 1 |
| BiScale-GTR (Fragment) | 0.6010 | 0.0110 | No | this paper | Table 1 |
| BiScale-GTR (Molecule) | 0.6420 | 0.0090 | No | this paper | Table 1 |

### Sol — RMSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| RF | 0.9180 | — | Yes | Rigatti 2017 | Table 1 |
| XGBoost | 0.8320 | — | Yes | Chen 2016 | Table 1 |
| CMPNN | 0.8580 | — | Yes | Swanson 2019 | Table 1 |
| FPGNN | 0.7470 | — | Yes | Cai 2022 | Table 1 |
| DHTNN | 0.8280 | — | Yes | Song 2023 | Table 1 |
| KANO | 0.7720 | — | Yes | Li 2023 | Table 1 |
| MPG | 0.7580 | — | Yes | Li 2020 | Table 1 |
| UniMol | 0.7070 | — | Yes | Zhou 2023 | Table 1 |
| Trans-M | 0.8340 | — | Yes | Luo 2022 | Table 1 |
| KP-GPT | 1.2210 | — | Yes | Wu 2018 | Table 1 |
| GraphFP | 1.9350 | — | Yes | Luong 2023 | Table 1 |
| FraGAT | 1.3520 | — | Yes | Zhang 2021 | Table 1 |
| PharmHGT | 0.9540 | — | Yes | Jiang 2023 | Table 1 |
| FragFormer | 0.8950 | — | Yes | Wang 2025 | Table 1 |
| BiScale-GTR (Molecule) | 0.9770 | — | No | this paper | Table 1 |

### Tox21 — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GraphMVP | 0.7490 | 0.0080 | Yes | Liu et al. 2021 | Table 1 |
| GraphMAE | 0.7520 | 0.0090 | Yes | Hou et al. 2022 | Table 1 |
| Mole-BERT | 0.7680 | 0.0050 | Yes | Xia et al. 2023 | Table 1 |
| SimSGT | 0.7680 | 0.0090 | Yes | Liu et al. 2023 | Table 1 |
| GraphFP | 0.7400 | 0.0070 | Yes | Luong et al. 2023 | Table 1 |
| MORE | 0.7560 | 0.0050 | Yes | Son et al. 2025 | Table 1 |
| GraphGPS+LAC | 0.7400 | — | Yes | Yang et al. 2025 | Table 1 |
| BiScale-GTR (Fragment) | 0.7310 | 0.0090 | No | this paper | Table 1 |
| BiScale-GTR (Molecule) | 0.7610 | 0.0040 | No | this paper | Table 1 |

### ToxCast — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GraphMVP | 0.6310 | 0.0020 | Yes | Liu et al. 2021 | Table 1 |
| GraphMAE | 0.6360 | 0.0030 | Yes | Hou et al. 2022 | Table 1 |
| Mole-BERT | 0.6430 | 0.0020 | Yes | Xia et al. 2023 | Table 1 |
| SimSGT | 0.6590 | 0.0080 | Yes | Liu et al. 2023 | Table 1 |
| GraphFP | 0.6390 | 0.0090 | Yes | Luong et al. 2023 | Table 1 |
| MORE | 0.6460 | 0.0060 | Yes | Son et al. 2025 | Table 1 |
| GraphGPS+LAC | 0.7370 | — | Yes | Yang et al. 2025 | Table 1 |
| BiScale-GTR (Fragment) | 0.6390 | 0.0020 | No | this paper | Table 1 |
| BiScale-GTR (Molecule) | 0.6220 | 0.0020 | No | this paper | Table 1 |

## Baseline Models Identified

- **GraphMVP** (from: liu2021pre)
- **GraphMAE** (from: hou2022graphmae)
- **Mole-BERT** (from: xia2023mole)
- **SimSGT** (from: liu2023rethinking)
- **GraphFP** (from: luong2023fragment)
- **MORE** (from: son2025more)
- **GraphGPS+LAC** (from: yang2025curriculum)
- **BiScale-GTR (Fragment)** (from: this paper)
- **RF** (from: Rigatti 2017)
- **XGBoost** (from: Chen 2016)
- **CMPNN** (from: Swanson 2019)
- **FPGNN** (from: Cai 2022)
- **DHTNN** (from: Song 2023)
- **KANO** (from: Li 2023)
- **MPG** (from: Li 2020)
- **UniMol** (from: Zhou 2023)
- **Trans-M** (from: Luo 2022)
- **KP-GPT** (from: Wu 2018)
- **FraGAT** (from: Zhang 2021)
- **PharmHGT** (from: Jiang 2023)
- **FragFormer** (from: Wang 2025)
- **GCN** (from: Kipf et al. 2016)
- **GCNII** (from: Chen et al. 2020)
- **GINE** (from: Hu et al. 2019)
- **GatedGCN** (from: Bresson et al. 2017)
- **GatedGCN+RWSE** (from: Dwivedi et al. 2022)
- **Transformer + LapPE** (from: Vaswani et al. 2017; Dwivedi et al. 2023)
- **SAN + LapPE** (from: Kreuzer et al. 2021; Dwivedi et al. 2023)
- **SAN + RWSE** (from: Kreuzer et al. 2021; Dwivedi et al. 2022)

## Extraction Notes

[BBBP] Extracted only BBBP results from Table 1 (MoleculeNet comparison). The paper reports ROC-AUC
as percentages (e.g., 73.8), which were normalized to [0, 1] range (0.738). Standard deviations were
parsed from 'mean ± std' format. BiScale-GTR (Fragment) is the best performing variant on BBBP
according to the text and table bolding. Baseline source references were inferred from citation keys
provided in the table. [Tox21] Extracted ROC-AUC results for Tox21 from Table 1. Values were
originally reported as percentages (e.g., 76.1%) and have been normalized to [0, 1] range (e.g.,
0.761) as per instructions. Standard deviations were parsed from the 'mean ± std' format. All models
listed in the table for the Tox21 column were included. [MUV] failed: 1 validation error for
ExtractionOutput results.5.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [BACE] Extracted ROC-AUC results for the BACE dataset
from Table 1. All values were percentages in the table (e.g., 85.0) and were divided by 100 to fit
the [0, 1] range as per instructions. Standard deviations were parsed from the 'mean ± std' format.
The proposed model is identified as BiScale-GTR (Molecule) based on the text stating it achieves the
best performance on BACE and is the primary variant discussed for general molecular property
prediction, although BiScale-GTR (Fragment) is also a variant of the proposed method. Both variants
are included as they are part of the proposed framework's evaluation. [ToxCast] Extracted only
ToxCast results from Table 1 (MoleculeNet comparison). Values were percentages in the table (e.g.,
63.1) and were divided by 100 to fit the [0,1] range for ROC-AUC. Standard deviations were parsed
from the 'mean ± std' format. GraphGPS+LAC had no standard deviation reported. The ablation tables
(Tables 2 and 3) were ignored as they represent variants/ablations of the proposed model rather than
the primary benchmark comparison against baselines, and the prompt asks for standard/default
configuration results which are best represented in Table 1. [SIDER] Extracted only SIDER results
from Table 1 (MoleculeNet comparison). The values in the table are percentages (e.g., 64.2), so they
were divided by 100 to normalize to [0, 1] range as per instructions for ROC-AUC. Standard
deviations were parsed from the 'mean ± std' format. All models listed in the table were included.
The 'uses_external_data' field is set to true for baselines as they are pre-trained models
(GraphMVP, GraphMAE, etc. use large pretraining corpora as noted in the text/table). For the
proposed model, it is also pre-trained on 430k molecules, so uses_external_data is true. [HIV]
Extracted only the HIV column from Table 1 (MoleculeNet results). Values were percentages in the
table (e.g., 79.2) and were divided by 100 to normalize to [0, 1] range as per instructions for ROC-
AUC. Standard deviations were parsed from the 'mean ± std' format. All models listed in the table
were included. The 'BiScale-GTR (Molecule)' is identified as the primary proposed model achieving
best performance on HIV. [CYP2C9] Extracted only the CYP2C9 column from Table 1 as requested. All
values are RMSE. No standard deviations were reported in the table. The proposed model is BiScale-
GTR (Molecule). Baselines are taken from the PharmaBench paper as noted in the caption. [CYP2D6]
Extracted only the CYP2D6 column from Table 1 as requested. All values are RMSE. No standard
deviations were reported in the table. The proposed model is BiScale-GTR (Molecule). Baseline
results are taken from the PharmaBench paper as noted in the caption. [CYP3A4] Extracted only the
CYP3A4 column from Table 1 as requested. All values are RMSE. No standard deviations were reported
in the table. The proposed model is BiScale-GTR (Molecule). Baseline results are taken from the
PharmaBench paper as noted in the caption. [HLMC] Extracted all models for the HLMC dataset from
Table 1. The metric is RMSE, where lower is better. No standard deviations were reported in the
table. Baseline results are cited from the PharmaBench paper as per the table caption. [MLMC]
Extracted only the MLMC column from Table 1 as requested. All values are RMSE. No standard
deviations were reported in the table. The proposed model is BiScale-GTR (Molecule). Baselines are
taken from the PharmaBench paper as noted in the table caption. [RLMC] Extracted all rows for the
RLMC dataset from Table 1. The metric is RMSE, where lower is better. No standard deviations were
reported in the table. Baseline results are cited from the PharmaBench paper (Niu 2024). [LogD]
Extracted only the LogD column from Table 1 as requested. All values are RMSE. The proposed model is
BiScale-GTR (Molecule). Baseline results are taken from the PharmaBench paper as noted in the
caption, but reported in this table. [PPB] Extracted only the PPB column from Table 1 as requested.
All values are RMSE. No standard deviations were reported in the table. The proposed model is
BiScale-GTR (Molecule). Baselines are taken from the PharmaBench paper as noted in the table
caption. [Sol] Extracted all rows from Table 1 for the 'Sol' dataset column. The metric is RMSE,
where lower is better. No standard deviations were reported in the table. The proposed model
BiScale-GTR (Molecule) achieved an RMSE of 0.977, which is not the best result (UniMol achieved
0.707). All baseline results were taken directly from the PharmaBench paper as noted in the table
caption. [Peptides-func] Extracted only Peptides-func AP results from Table 1 as requested. The
second table (Table token ablation) reports ROC-AUC for Peptides-func, which is a different metric
and part of an ablation study, so it was excluded based on the focus on the primary benchmark metric
AP from the main comparison table. FragFormer is marked as using external data because the text
explicitly states it relies on a knowledge fusion layer incorporating handcrafted molecular
descriptors. [Peptides-struct] Extracted Peptides-struct MAE results from Table 1 and Table 2. Table
1 contains the main benchmark comparison. Table 2 contains an ablation study for the proposed method
(Graph BPE with validity/OOV handling corresponds to BiScale-GTR). FragFormer has no result for
Peptides-struct in Table 1 (marked as --), so it is excluded. All values are normalized to [0,1]
range where applicable (MAE is not normalized but values are < 1). Standard deviations were parsed
from the 'mean ± std' format.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*