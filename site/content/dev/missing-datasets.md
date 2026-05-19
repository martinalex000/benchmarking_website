---
title: Missing Datasets
type: dev
description: Datasets detected in extraction but not yet mapped into DB
---

## Datasets Detected But Not In DB

During result extraction, the LLM sometimes detects dataset names that are not yet in our benchmarking database. This page lists those datasets. Each entry includes the datasets that were detected in the papers, along with suggested benchmark categories and whether a PyG (PyTorch Geometric) dataset definition is available. These pending datasets should be reviewed for integration into the main benchmark suite.

Source file: `/home/martin/git/benchmarking_website/data/pending_datasets.yaml`

**Total pending entries:** 146

| Status | Dataset | Paper | Metrics Seen | Suggested Benchmark | PyG |
|--------|---------|-------|--------------|---------------------|-----|
| pending | Enzymes | 2601.07419 | Accuracy |  |  |
| pending | Case 1 | 2601.01387 | Accuracy |  |  |
| pending | Case 2 | 2601.01387 | Accuracy |  |  |
| pending | ECHO-Synth | 2512.17762 | MAE |  |  |
| pending | ECHO-Charge | 2512.17762 | MAE |  |  |
| pending | ECHO-Energy | 2512.17762 | MAE |  |  |
| pending | 20News | 2512.14619 | Accuracy |  |  |
| pending | Code | 2511.08028 | F1 |  |  |
| pending | Flow | 2511.08028 | MAE |  |  |
| pending | ENZYMES | 2509.06777 | Accuracy |  |  |
| pending | Cumulene | 2507.19382 | RMSE E, RMSE F |  |  |
| pending | Quijote | 2507.03707 | R^2 |  |  |
| pending | CAMELS-SAM | 2507.03707 | R^2 |  |  |
| pending | CS-Trees | 2507.03707 | R2 |  |  |
| pending | CS-Trees-200 | 2507.03707 | Accuracy |  |  |
| pending | BAT | 2508.14097 | F1 |  |  |
| pending | UAT | 2508.14097 | F1 |  |  |
| pending | LEN | 2506.13912 | Accuracy |  |  |
| pending | Ribonanza | 2506.19862 | RMSE |  |  |
| pending | Tc-Ribo | 2506.19862 | RMSE |  |  |
| pending | TorsionAngle | 2506.19862 | Circular MAE |  |  |
| pending | HSG-12M | 2506.08618 | Accuracy |  |  |
| pending | HSG-topology | 2506.08618 | Accuracy |  |  |
| pending | PTC_MR | 2405.17311 | Accuracy |  |  |
| pending | Paris | 2505.23185 | Accuracy |  |  |
| pending | Shanghai | 2505.23185 | Accuracy |  |  |
| pending | Los Angeles | 2505.23185 | Accuracy |  |  |
| pending | H2 | 2505.23875 | MAE |  |  |
| approved | BlogCatalog | 2505.23345 | Accuracy |  | yes |
| pending | molipo | 2505.23345 | RMSE |  |  |
| pending | moltocx21 | 2505.23345 | ROC-AUC |  |  |
| approved | Facebook | 2505.23345 | Accuracy |  | yes |
| pending | NAME | 2505.15405 | F1 |  |  |
| pending | ORIENT | 2505.15405 | F1 |  |  |
| pending | β1 | 2505.15405 | F1 |  |  |
| pending | β2 | 2505.15405 | F1 |  |  |
| pending | BREC | 2504.12588 | Accuracy |  |  |
| pending | Paris | 2503.09008 | Accuracy |  |  |
| pending | Shanghai | 2503.09008 | Accuracy |  |  |
| pending | Los Angeles | 2503.09008 | Accuracy |  |  |
| approved | AIDS | 2502.02379 | AUROC | TU Dortmund | yes |
| pending | User-post-comment | 2502.01122 | MAP |  |  |
| approved | Blog | 2501.18739 | Accuracy |  | yes |
| approved | Flickr | 2501.18739 | Accuracy |  | yes |
| pending | Flickr-S | 2501.18739 | Accuracy |  |  |
| pending | EXP | 2501.18739 | Accuracy |  |  |
| pending | SR25 | 2501.18739 | Accuracy |  |  |
| pending | APD | 2501.17901 | F1 |  |  |
| pending | CAMP | 2501.17901 | F1 |  |  |
| pending | Average F1 | 2501.17901 | F1 |  |  |
| pending | XUAMP | 2501.17901 | AUROC |  |  |
| approved | Community | 2501.09821 | Accuracy |  | yes |
| pending | Colors3 | 2501.09821 | Accuracy |  |  |
| pending | TGBL-Coin | 2412.03783 | MRR | TGB |  |
| pending | Cycle Check | 2411.15671 | Accuracy |  |  |
| pending | Triangle Counting | 2411.15671 | RMSE |  |  |
| pending | Genius | 2410.23686 | ROC-AUC |  |  |
| approved | Alchemy | 2410.09737 | MAE |  | yes |
| pending | HLS | 2410.06460 | Ranking |  |  |
| pending | SR | 2410.06460 | Ranking |  |  |
| pending | TIME | 2410.06460 | Ranking |  |  |
| pending | Chickenpox | 2410.05593 | MSE |  |  |
| pending | WikiMath | 2410.05593 | MSE |  |  |
| pending | Ele-fashion | 2406.16321 | Accuracy |  |  |
| pending | ImageNet-1K | 2406.16722 | Accuracy |  |  |
| approved | Flickr | 2406.12059 | Accuracy |  | yes |
| approved | Yelp | 2406.12059 | Micro-F1 Score | OGB | yes |
| pending | tkgl-polecat | 2406.09639 | MRR | TKGL |  |
| pending | tkgl-icews | 2406.09639 | MRR | TKGL |  |
| pending | thgl-software | 2406.09639 | MRR |  |  |
| pending | thgl-forum | 2406.09639 | MRR |  |  |
| approved | PTC | 2406.06984 | Accuracy | TU Dortmund | yes |
| pending | NLST | 2406.04377 | C-index |  |  |
| pending | TCGA | 2406.04377 | C-index |  |  |
| pending | LastFM | 2406.02740 | AUC |  |  |
| pending | MOOC | 2406.02740 | AUC |  |  |
| pending | tgbl-review-v2 | 2406.02740 | MRR | TGBL |  |
| pending | TPUGraphs | 2405.19121 | Kendall tau |  |  |
| pending | Distance Regression (DAGs) | 2405.19121 | MAE |  |  |
| approved | Flickr | 2405.17404 | Accuracy |  | yes |
| approved | QM8 | 2405.03481 | MAE |  | yes |
| approved | Alchemy | 2404.03380 | MAE | OGB | yes |
| pending | Superblue | 2404.00477 | RMSE | Superblue |  |
| pending | BREC | 2403.13749 | Num. of distinguished pairs | BREC |  |
| pending | Synthetic Subgraph Counting | 2403.13749 | MAE |  |  |
| pending | Shortest Path (Erdős–Rényi) (15k) | 2402.10793 | MCC | Graph Generation Benchmark |  |
| pending | Shortest Path (Erdős–Rényi) (30k) | 2402.10793 | MCC | GraphGen |  |
| pending | Alchemy-12k | 2402.08450 | MAE | Alchemy |  |
| approved | FAUST | 2402.04821 | Accuracy |  | yes |
| pending | TOSCA | 2402.04821 | Accuracy | TOSCA |  |
| pending | N-UCLA-CIL | 2401.18054 | AOPD, MOPD | G-CLOOB |  |
| pending | NTU-CIL | 2401.18054 | AOPD, MOPD | NTU-CIL |  |
| pending | CYP2C9 | 2604.06336 | RMSE |  |  |
| pending | CYP3A4 | 2604.06336 | RMSE |  |  |
| pending | HLMC | 2604.06336 | RMSE |  |  |
| pending | MLMC | 2604.06336 | RMSE |  |  |
| pending | RLMC | 2604.06336 | RMSE |  |  |
| pending | LogD | 2604.06336 | RMSE |  |  |
| pending | PPB | 2604.06336 | RMSE |  |  |
| pending | CLRS-30 | 2601.19094 | Accuracy | CLRS Benchmark |  |
| pending | BREC | 2601.19094 | Accuracy | BREC |  |
| pending | ER2-30 | 2601.18917 | F1 |  |  |
| pending | ER4-30 | 2601.18917 | F1 | GraphBench |  |
| pending | SF2-30 | 2601.18917 | F1 |  |  |
| pending | SF4-30 | 2601.18917 | F1 |  |  |
| pending | Springs | 2601.18917 | MSE | GNN-Generalization-Benchmark |  |
| pending | School | 2511.16767 | Accuracy |  |  |
| pending | Facebook | 2506.22727 | Accuracy |  |  |
| pending | LastFM | 2506.05393 | MRR |  |  |
| pending | UCI | 2506.05393 | MRR |  |  |
| pending | Enron | 2506.05393 | MRR |  |  |
| approved | Flickr | 2410.05697 | Accuracy |  | yes |
| pending | HCP-Task | 2407.18480 | Accuracy |  |  |
| pending | HCP-Age | 2407.18480 | Accuracy |  |  |
| pending | sr25 | 2407.18480 | Undistinguished Pairs | Graph Isomorphism Benchmark |  |
| pending | EXP | 2407.18480 | Undistinguished Pairs | EXP Benchmark |  |
| pending | GLUE | 2312.04234 | Accuracy | GLUE |  |
| pending | ImageNet-1k | 2312.04234 | Accuracy |  |  |
| pending | LibriSpeech 100h | 2312.04234 | WER |  |  |
| pending | LibriSpeech 960h | 2312.04234 | WER |  |  |
| pending | PTB | 2312.04234 | Perplexity |  |  |
| pending | WikiText-103 | 2312.04234 | Perplexity |  |  |
| pending | ListOps (2K) | 2312.04234 | Accuracy | ListOps |  |
| pending | Image (4K) | 2312.04234 | Accuracy |  |  |
| pending | Motor | 2311.05964 | RMSE |  |  |
| pending | Magnetostatics Shape | 2311.05964 | MSE |  |  |
| pending | Magnetostatics Superpositions | 2311.05964 | MSE |  |  |
| pending | OE62 | 2311.01276 | MAE |  |  |
| approved | Yelp | 2310.05174 | Macro-F1 |  | yes |
| approved | MUV | 2310.03274 | ROC-AUC | MoleculeNet | yes |
| pending | sCIFAR | 2310.02980 | Accuracy |  |  |
| approved | Alchemy | 2310.02156 | MAE | OGB | yes |
| approved | PTC_MR | 2310.02156 | Accuracy | TU Dortmund | yes |
| pending | RootNeighbors | 2310.01267 | MAE | OOD-GNN |  |
| pending | EXP | 2309.16014 | Accuracy |  |  |
| pending | Synthetic | 2309.04941 | Normalized MAE |  |  |
| pending | KIBA | 2309.16685 | MSE | KIBA |  |
| pending | LBA | 2309.16685 | RMSE | OGB-LSC |  |
| approved | MUV | 2307.07107 | AUROC | MoleculeNet | yes |
| pending | EXP | 2307.07107 | ACC | Synthetic Benchmark |  |
| pending | EXP-Class | 2306.05955 | Accuracy | EXP-Bench |  |
| pending | SCOPe | 2306.04667 | F1-Score |  |  |
| approved | PTC_MR | 2306.03561 | Accuracy | TU Dortmund | yes |
| pending | GRAPH8c | 2306.02866 | GRAPH8c | GraphBench |  |
| pending | EXP | 2306.02866 | EXP | OGB-LSC |  |
| pending | EXP-classify | 2306.02866 | Accuracy |  |  |