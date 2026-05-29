---
title: Baseline Coverage Gaps
type: dev
description: Datasets missing common GNN or MLP baseline families
---

## Baseline Coverage Gaps

Datasets in this report are missing one of the baseline families we usually want on the leaderboard for context.

### No GCN/GIN/GraphSAGE Baseline (42)

| Benchmark | Dataset | Task | Metric | Results | Present Families |
|-----------|---------|------|--------|--------:|------------------|
| Algorithmic Graph Tasks | Eccentricity | graph_regression | MSE | 0 | — |
| City-Networks | London | node_classification | Accuracy | 0 | — |
| City-Networks | Paris | node_classification | Accuracy | 0 | — |
| City-Networks | Shanghai | node_classification | Accuracy | 0 | — |
| CosmoBench | CAMELS-SAM | graph_regression | R^2 | 0 | — |
| CosmoBench | CS-Trees | graph_regression | R2 | 0 | — |
| CosmoBench | CS-Trees-200 | graph_classification | Accuracy | 0 | — |
| CosmoBench | Quijote | graph_regression | R^2 | 0 | — |
| DualEquiNet RNA Benchmarks | COVID | graph_regression | RMSE | 7 | — |
| DualEquiNet RNA Benchmarks | Ribonanza | graph_regression | RMSE | 7 | — |
| DualEquiNet RNA Benchmarks | Tc-Ribo | graph_regression | RMSE | 7 | — |
| DualEquiNet RNA Benchmarks | TorsionAngle | graph_regression | Circular MAE | 25 | — |
| ECHO Benchmark | ECHO-Charge | graph_regression | MAE | 0 | — |
| ECHO Benchmark | ECHO-Energy | graph_regression | MAE | 12 | — |
| ECHO Benchmark | ECHO-Synth | graph_regression | MAE | 5 | — |
| GraphBench | Algorithmic Reasoning | graph_classification | Accuracy | 0 | — |
| GraphBench | BlueSky | node_classification | MAE | 0 | — |
| GraphBench | Bridges | graph_classification | F1 | 5 | — |
| GraphBench | Chip Design | graph_generation | Accuracy | 0 | — |
| GraphBench | Combinatorial Optimization | node_classification | Accuracy | 0 | — |
| GraphBench | Electronic Circuits | graph_classification | MAE | 10 | — |
| GraphBench | MST | graph_classification | F1 | 5 | — |
| GraphBench | Weather Forecasting | node_classification | MAE | 0 | — |
| Heterogeneous Graph Benchmarks | RCDD | link_prediction | MRR | 0 | — |
| Heterophilic Graphs | Deezer | node_classification | ROC-AUC | 1 | — |
| Hypergraph Benchmarks | AMAP | node_classification | F1 | 124 | — |
| Hypergraph Benchmarks | BAT | node_classification | F1 | 52 | — |
| Hypergraph Benchmarks | Congress | node_classification | Accuracy | 0 | — |
| Hypergraph Benchmarks | DBLP-CA | node_classification | Accuracy | 0 | — |
| Hypergraph Benchmarks | EAT | node_classification | F1 | 52 | — |
| Hypergraph Benchmarks | Senate | node_classification | Accuracy | 0 | — |
| Hypergraph Benchmarks | UAT | node_classification | F1 | 0 | — |
| Hypergraph Benchmarks | Walmart | node_classification | Accuracy | 0 | — |
| Knowledge Graphs | FB15k-237 | link_prediction | MRR | 134 | — |
| Knowledge Graphs | WN18 | link_prediction | MRR | 26 | — |
| Knowledge Graphs | WN18RR | link_prediction | MRR | 98 | — |
| LRIM Graph Benchmark | LRIM | node_regression | log-MSE | 6 | — |
| OGB | ogbl-biokg | link_prediction | MRR | 19 | — |
| Other Graph Benchmarks | ShapeNet-Part | node_classification | F1 | 12 | — |
| Power Flow Benchmarks | Case 1 | graph_regression | Accuracy | 81 | — |
| Power Flow Benchmarks | Case 2 | graph_regression | Accuracy | 12 | — |
| Quantum Chemistry | MD17 | graph_regression | MAE | 82 | — |

### No MLP Baseline (95)

| Benchmark | Dataset | Task | Metric | Results | Present Families |
|-----------|---------|------|--------|--------:|------------------|
| Algorithmic Graph Tasks | Eccentricity | graph_regression | MSE | 0 | — |
| Algorithmic Graph Tasks | SSSP | graph_regression | MSE | 9 | gcn, gin, sage |
| City-Networks | London | node_classification | Accuracy | 0 | — |
| City-Networks | Los Angeles | node_classification | Accuracy | 6 | gcn, sage |
| City-Networks | Paris | node_classification | Accuracy | 0 | — |
| City-Networks | Shanghai | node_classification | Accuracy | 0 | — |
| Classic | AQSOL | graph_regression | MAE | 17 | gcn, gin, sage |
| CosmoBench | CAMELS-SAM | graph_regression | R^2 | 0 | — |
| CosmoBench | CS-Trees | graph_regression | R2 | 0 | — |
| CosmoBench | CS-Trees-200 | graph_classification | Accuracy | 0 | — |
| CosmoBench | Quijote | graph_regression | R^2 | 0 | — |
| DualEquiNet RNA Benchmarks | COVID | graph_regression | RMSE | 7 | — |
| DualEquiNet RNA Benchmarks | Ribonanza | graph_regression | RMSE | 7 | — |
| DualEquiNet RNA Benchmarks | Tc-Ribo | graph_regression | RMSE | 7 | — |
| DualEquiNet RNA Benchmarks | TorsionAngle | graph_regression | Circular MAE | 25 | — |
| ECHO Benchmark | ECHO-Charge | graph_regression | MAE | 0 | — |
| ECHO Benchmark | ECHO-Energy | graph_regression | MAE | 12 | — |
| ECHO Benchmark | ECHO-Synth | graph_regression | MAE | 5 | — |
| GNNBenchmark | CIFAR10 | graph_classification | Accuracy | 115 | gcn, gin, sage |
| GNNBenchmark | CLUSTER | node_classification | Accuracy | 100 | gcn, gin, sage |
| GNNBenchmark | CSL | graph_classification | Accuracy | 9 | gcn |
| GNNBenchmark | MNIST | graph_classification | Accuracy | 198 | gcn, gin, sage |
| GNNBenchmark | PATTERN | node_classification | Accuracy | 139 | gcn, gin, sage |
| GNNBenchmark | TSP | link_prediction | F1 | 25 | gcn, gin, sage |
| GraphBench | Algorithmic Reasoning | graph_classification | Accuracy | 0 | — |
| GraphBench | BA graph | graph_classification | Accuracy | 139 | gcn, gin, sage |
| GraphBench | BlueSky | node_classification | MAE | 0 | — |
| GraphBench | Bridges | graph_classification | F1 | 5 | — |
| GraphBench | Chip Design | graph_generation | Accuracy | 0 | — |
| GraphBench | Combinatorial Optimization | node_classification | Accuracy | 0 | — |
| GraphBench | ER graph | graph_classification | Accuracy | 35 | gcn, gin, sage |
| GraphBench | Electronic Circuits | graph_classification | MAE | 10 | — |
| GraphBench | Flow | graph_regression | MAE | 41 | gcn, gin, sage |
| GraphBench | MST | graph_classification | F1 | 5 | — |
| GraphBench | Max Clique | graph_classification | F1 | 14 | gcn, gin, sage |
| GraphBench | RB graph | graph_classification | Accuracy | 7 | gcn, gin, sage |
| GraphBench | SAT Solving | node_classification | Accuracy | 97 | gcn, gin, sage |
| GraphBench | Steiner Trees | graph_classification | F1 | 13 | gcn, gin, sage |
| GraphBench | Topological Sorting | node_classification | MAE | 6 | gcn, gin, sage |
| GraphBench | Weather Forecasting | node_classification | MAE | 0 | — |
| HSG-12M | HSG-12M | graph_classification | Accuracy | 8 | gcn, gin, sage |
| HSG-12M | HSG-topology | graph_classification | Accuracy | 8 | gcn, gin, sage |
| Heterogeneous Graph Benchmarks | Freebase | node_classification | Macro-F1 | 63 | gcn, sage |
| Heterogeneous Graph Benchmarks | RCDD | link_prediction | MRR | 0 | — |
| Heterophilic Graphs | Amazon-ratings | node_classification | Accuracy | 148 | gcn, sage |
| Heterophilic Graphs | Deezer | node_classification | ROC-AUC | 1 | — |
| Heterophilic Graphs | Minesweeper | node_classification | ROC-AUC | 50 | gcn, sage |
| Hypergraph Benchmarks | AMAP | node_classification | F1 | 124 | — |
| Hypergraph Benchmarks | BAT | node_classification | F1 | 52 | — |
| Hypergraph Benchmarks | Congress | node_classification | Accuracy | 0 | — |
| Hypergraph Benchmarks | DBLP-CA | node_classification | Accuracy | 0 | — |
| Hypergraph Benchmarks | EAT | node_classification | F1 | 52 | — |
| Hypergraph Benchmarks | House | node_classification | Accuracy | 59 | gcn, gin |
| Hypergraph Benchmarks | LEN | node_classification | Accuracy | 139 | gcn, gin, sage |
| Hypergraph Benchmarks | Senate | node_classification | Accuracy | 0 | — |
| Hypergraph Benchmarks | UAT | node_classification | F1 | 0 | — |
| Hypergraph Benchmarks | Walmart | node_classification | Accuracy | 0 | — |
| Knowledge Graphs | FB15k-237 | link_prediction | MRR | 134 | — |
| Knowledge Graphs | WN18 | link_prediction | MRR | 26 | — |
| Knowledge Graphs | WN18RR | link_prediction | MRR | 98 | — |
| LRGB | PCQM-Contact | link_prediction | MRR | 66 | gcn, gin |
| LRGB | Peptides-func | graph_classification | AP | 245 | gcn, gin, sage |
| LRGB | Peptides-struct | graph_regression | MAE | 256 | gcn, gin |
| LRIM Graph Benchmark | LRIM | node_regression | log-MSE | 6 | — |
| MoleculeNet | BACE | graph_classification | ROC-AUC | 251 | gcn, gin, sage |
| MoleculeNet | ClinTox | graph_classification | ROC-AUC | 185 | gcn, gin, sage |
| MoleculeNet | ESOL | graph_regression | RMSE | 114 | gcn, gin, sage |
| MoleculeNet | FreeSolv | graph_regression | RMSE | 90 | gcn, gin, sage |
| MoleculeNet | Lipophilicity | graph_regression | RMSE | 92 | gcn, gin, sage |
| MoleculeNet | SIDER | graph_classification | ROC-AUC | 135 | gcn, gin, sage |
| MoleculeNet | Tox21 | graph_classification | ROC-AUC | 239 | gcn, gin, sage |
| MoleculeNet | ToxCast | graph_classification | ROC-AUC | 202 | gcn, gin, sage |
| OGB | Code | graph_classification | F1 | 45 | gcn, gin |
| OGB | PCQM4Mv2 | graph_regression | MAE | 107 | gcn, gin, sage |
| OGB | ogbg-molhiv | graph_classification | ROC-AUC | 356 | gcn, gin, sage |
| OGB | ogbg-molpcba | graph_classification | AP | 154 | gcn, gin, sage |
| OGB | ogbl-biokg | link_prediction | MRR | 19 | — |
| OGB | ogbl-ddi | link_prediction | Hits@20 | 64 | gcn, gin, sage |
| OGB | ogbl-wikikg2 | link_prediction | MRR | 107 | gcn, sage |
| Other Graph Benchmarks | MalNet-Tiny | graph_classification | Accuracy | 19 | gcn, gin |
| Other Graph Benchmarks | ShapeNet-Part | node_classification | F1 | 12 | — |
| Power Flow Benchmarks | Case 1 | graph_regression | Accuracy | 81 | — |
| Power Flow Benchmarks | Case 2 | graph_regression | Accuracy | 12 | — |
| Quantum Chemistry | MD17 | graph_regression | MAE | 82 | — |
| Quantum Chemistry | QM7b | graph_regression | MAE | 49 | gcn, gin |
| Quantum Chemistry | QM9 | graph_regression | MAE | 502 | gcn, gin, sage |
| TU Dortmund | ENZYMES | graph_classification | Accuracy | 216 | gcn, gin, sage |
| TU Dortmund | IMDB-BINARY | graph_classification | Accuracy | 403 | gcn, gin, sage |
| TU Dortmund | IMDB-MULTI | graph_classification | Accuracy | 215 | gcn, gin, sage |
| TU Dortmund | MUTAG | graph_classification | Accuracy | 613 | gcn, gin, sage |
| TU Dortmund | NCI1 | graph_classification | Accuracy | 393 | gcn, gin, sage |
| TU Dortmund | PROTEINS | graph_classification | Accuracy | 661 | gcn, gin, sage |
| TU Dortmund | RDT-B | graph_classification | Accuracy | 15 | gcn, gin, sage |
| TU Dortmund | REDDIT-BINARY | graph_classification | Accuracy | 91 | gcn, gin, sage |
| TU Dortmund | REDDIT-MULTI-5K | graph_classification | Accuracy | 110 | gcn, gin, sage |