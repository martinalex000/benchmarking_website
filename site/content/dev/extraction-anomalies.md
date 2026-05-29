---
title: Extraction Anomalies
type: dev
description: Post-extraction anomaly checks over stored results
---

## Post-Extraction Anomalies

This page flags suspicious stored results after overrides are applied.

Checks currently included:

- bounded metrics such as Accuracy/AP/AUC/F1/MRR/Hits@K must not exceed 1
- values roughly 20x away from the dataset-metric median are flagged as likely scale issues

**Flagged papers:** 11
**Flagged rows:** 27

| ArXiv | Title | Dataset | Metric | Model | Value | Dataset Median | Reason |
|-------|-------|---------|--------|-------|------:|---------------:|--------|
| 2309.16014 | Graph-level Representation Learning with Joint-E | IMDB-BINARY | Accuracy | BGRL | 0.005 | 0.708 | 141.6x below dataset median |
| 2309.16014 | Graph-level Representation Learning with Joint-E | IMDB-MULTI | Accuracy | BGRL | 0.0033 | 0.49935 | 151.3x below dataset median |
| 2312.16560 | Algorithmic Graph Tasks | D&D | MSE | A-DGN | -0.453 | 0.0444 | -0.1x below dataset median |
| 2312.16560 | Algorithmic Graph Tasks | D&D | MSE | AMP_ADGN | -0.5891 | 0.0444 | -0.1x below dataset median |
| 2312.16560 | Algorithmic Graph Tasks | D&D | MSE | AMP_GCN | -0.1072 | 0.0444 | -0.4x below dataset median |
| 2312.16560 | Algorithmic Graph Tasks | D&D | MSE | AMP_GIN | -0.4874 | 0.0444 | -0.1x below dataset median |
| 2312.16560 | Algorithmic Graph Tasks | D&D | MSE | GAT | 1.4367 | 0.0444 | 32.4x above dataset median |
| 2312.16560 | Algorithmic Graph Tasks | D&D | MSE | GRAND | 0.9477 | 0.0444 | 21.3x above dataset median |
| 2405.03481 | AnchorGT: Efficient and Flexible Attention Archi | QM8 | MAE | GraphGPS | 0.705 | 0.0279 | 25.3x above dataset median |
| 2405.03481 | AnchorGT: Efficient and Flexible Attention Archi | QM8 | MAE | GraphGPS-AnchorGT | 0.665 | 0.0279 | 23.8x above dataset median |
| 2505.23875 | A Benchmark Dataset for Graph Regression with Ho | D&D | MAE | Cheb | 0.15 | 3.7605 | 25.1x below dataset median |
| 2505.23875 | A Benchmark Dataset for Graph Regression with Ho | D&D | MAE | Code2Vec | 0.15 | 3.7605 | 25.1x below dataset median |
| 2505.23875 | A Benchmark Dataset for Graph Regression with Ho | D&D | MAE | CodeBERT | 0.15 | 3.7605 | 25.1x below dataset median |
| 2505.23875 | A Benchmark Dataset for Graph Regression with Ho | D&D | MAE | GCN | 0.14 | 3.7605 | 26.9x below dataset median |
| 2505.23875 | A Benchmark Dataset for Graph Regression with Ho | D&D | MAE | GIN | 0.14 | 3.7605 | 26.9x below dataset median |
| 2505.23875 | A Benchmark Dataset for Graph Regression with Ho | D&D | MAE | GraphSAGE | 0.14 | 3.7605 | 26.9x below dataset median |
| 2505.23875 | A Benchmark Dataset for Graph Regression with Ho | D&D | MAE | HeteroGAT | 0.18 | 3.7605 | 20.9x below dataset median |
| 2505.23875 | A Benchmark Dataset for Graph Regression with Ho | D&D | MAE | PNA | 0.11 | 3.7605 | 34.2x below dataset median |
| 2506.05393 | Are Large Language Models Good Temporal Graph Le | ogbl-wikikg2 | MRR | TGTalker (with no components) | 0.008 | 0.6 | 75.0x below dataset median |
| 2507.19382 | Learning Long-Range Representations with Equivar | CLUSTER | RMSE F | SpookyNet | 1.052 | 21.282 | 20.2x below dataset median |
| 2509.22259 | Rotary Position Encodings for Graphs | QM9 | MAE | Mace | 0.02 | 0.428 | 21.4x below dataset median |
| 2511.08028 | Generalizable Insights for Graph Transformers in | PCQM-Contact | MAE | SOTA (Range) | 0.0809 | 92.8 | 1147.1x below dataset median |
| 2512.04475 | GraphBench | SAT Solving | Gap Closed | Multi-class Classification | -0.32 | 0.28 | -0.9x below dataset median |
| 2512.04475 | GraphBench | SAT Solving | Gap Closed | Multi-class Classification | -0.13 | 0.28 | -2.2x below dataset median |
| 2601.18917 | GraIP: A Benchmarking Framework For Neural Graph | D&D | MSE | NRI + STE | 0.0021 | 0.0444 | 21.1x below dataset median |
| 2601.18917 | GraIP: A Benchmarking Framework For Neural Graph | D&D | MSE | NRI + STE (non-blind) | 0.00018 | 0.0444 | 246.7x below dataset median |
| 2601.19094 | FloydNet: A Learning Paradigm for Global Relatio | TSP | Gap | Proposed Method (Single Solution, Metric) | 0 | 0.0025 | zero value against positive dataset median |