---
title: Baseline Coverage Gaps
type: dev
description: Datasets missing common GNN or MLP baseline families
---

## Baseline Coverage Gaps

Datasets in this report are missing one of the baseline families we usually want on the leaderboard for context.

### No GCN/GIN/GraphSAGE Baseline (67)

| Benchmark | Dataset | Task | Metric | Results | Present Families |
|-----------|---------|------|--------|--------:|------------------|
| Algorithmic Graph Tasks | Eccentricity | graph_regression | MSE | 0 | — |
| Algorithmic Graph Tasks | SSSP | graph_regression | MSE | 0 | — |
| City-Networks | London | node_classification | Accuracy | 0 | — |
| City-Networks | Los Angeles | node_classification | Accuracy | 0 | — |
| City-Networks | Paris | node_classification | Accuracy | 0 | — |
| City-Networks | Shanghai | node_classification | Accuracy | 0 | — |
| CosmoBench | CAMELS-SAM | graph_regression | R^2 | 0 | — |
| CosmoBench | CS-Trees | graph_regression | R2 | 0 | — |
| CosmoBench | CS-Trees-200 | graph_classification | Accuracy | 0 | — |
| CosmoBench | Quijote | graph_regression | R^2 | 0 | — |
| DualEquiNet RNA Benchmarks | COVID | graph_regression | RMSE | 7 | — |
| DualEquiNet RNA Benchmarks | Ribonanza | graph_regression | RMSE | 7 | — |
| DualEquiNet RNA Benchmarks | Tc-Ribo | graph_regression | RMSE | 7 | — |
| DualEquiNet RNA Benchmarks | TorsionAngle | graph_regression | Circular MAE | 7 | — |
| ECHO Benchmark | ECHO-Charge | graph_regression | MAE | 0 | — |
| ECHO Benchmark | ECHO-Energy | graph_regression | MAE | 0 | — |
| ECHO Benchmark | ECHO-Synth | graph_regression | MAE | 0 | — |
| GraphBench | Algorithmic Reasoning | graph_classification | Accuracy | 0 | — |
| GraphBench | BlueSky | node_classification | MAE | 0 | — |
| GraphBench | Bridges | graph_classification | F1 | 5 | — |
| GraphBench | Chip Design | graph_generation | Accuracy | 0 | — |
| GraphBench | Combinatorial Optimization | node_classification | Accuracy | 0 | — |
| GraphBench | Electronic Circuits | graph_classification | MAE | 0 | — |
| GraphBench | MST | graph_classification | F1 | 5 | — |
| GraphBench | Max Clique | graph_classification | F1 | 0 | — |
| GraphBench | Max Matching | graph_classification | F1 | 0 | — |
| GraphBench | SAT Solving | node_classification | Accuracy | 0 | — |
| GraphBench | Steiner Trees | graph_classification | F1 | 0 | — |
| GraphBench | Topological Sorting | node_classification | MAE | 0 | — |
| GraphBench | Weather Forecasting | node_classification | MAE | 0 | — |
| Heterogeneous Graph Benchmarks | ACM | node_classification | Micro-F1 | 0 | — |
| Heterogeneous Graph Benchmarks | DBLP | node_classification | Micro-F1 | 0 | — |
| Heterogeneous Graph Benchmarks | Freebase | node_classification | Macro-F1 | 0 | — |
| Heterogeneous Graph Benchmarks | IMDB | node_classification | Micro-F1 | 0 | — |
| Heterogeneous Graph Benchmarks | RCDD | link_prediction | MRR | 0 | — |
| Heterophilic Graphs | Deezer | node_classification | ROC-AUC | 1 | — |
| Hypergraph Benchmarks | AMAP | node_classification | F1 | 0 | — |
| Hypergraph Benchmarks | BAT | node_classification | F1 | 0 | — |
| Hypergraph Benchmarks | Congress | node_classification | Accuracy | 0 | — |
| Hypergraph Benchmarks | Cora-CA | node_classification | Accuracy | 0 | — |
| Hypergraph Benchmarks | DBLP-CA | node_classification | Accuracy | 0 | — |
| Hypergraph Benchmarks | EAT | node_classification | F1 | 0 | — |
| Hypergraph Benchmarks | House | node_classification | Accuracy | 0 | — |
| Hypergraph Benchmarks | LEN | node_classification | Accuracy | 6 | — |
| Hypergraph Benchmarks | Senate | node_classification | Accuracy | 0 | — |
| Hypergraph Benchmarks | UAT | node_classification | F1 | 0 | — |
| Hypergraph Benchmarks | Walmart | node_classification | Accuracy | 0 | — |
| Knowledge Graphs | FB15k-237 | link_prediction | MRR | 7 | — |
| Knowledge Graphs | WN18 | link_prediction | MRR | 7 | — |
| Knowledge Graphs | WN18RR | link_prediction | MRR | 0 | — |
| LINKX Benchmarks | Pokec | node_classification | Accuracy | 2 | mlp |
| LRIM Graph Benchmark | LRIM | node_regression | log-MSE | 0 | — |
| MoleculeNet | ClinTox | graph_classification | ROC-AUC | 0 | — |
| MoleculeNet | ESOL | graph_regression | RMSE | 5 | — |
| MoleculeNet | FreeSolv | graph_regression | RMSE | 0 | — |
| MoleculeNet | Lipophilicity | graph_regression | RMSE | 0 | — |
| MoleculeNet | SIDER | graph_classification | ROC-AUC | 0 | — |
| MoleculeNet | ToxCast | graph_classification | ROC-AUC | 0 | — |
| OGB | ogbl-biokg | link_prediction | MRR | 12 | — |
| OGB | ogbl-wikikg2 | link_prediction | MRR | 45 | — |
| Other Graph Benchmarks | Amazon2M | node_classification | Accuracy | 2 | — |
| Other Graph Benchmarks | ShapeNet-Part | node_classification | F1 | 0 | — |
| Power Flow Benchmarks | Case 1 | graph_regression | Accuracy | 0 | — |
| Power Flow Benchmarks | Case 2 | graph_regression | Accuracy | 0 | — |
| Quantum Chemistry | MD17 | graph_regression | MAE | 0 | — |
| Quantum Chemistry | QM7b | graph_regression | MAE | 0 | — |
| TU Dortmund | RDT-B | graph_classification | Accuracy | 1 | — |

### No MLP Baseline (112)

| Benchmark | Dataset | Task | Metric | Results | Present Families |
|-----------|---------|------|--------|--------:|------------------|
<<<<<<< Updated upstream
| Algorithmic Graph Tasks | Eccentricity | graph_regression | MSE | 11 | gcn, gin, sage |
| Algorithmic Graph Tasks | SSSP | graph_regression | MSE | 11 | gcn, gin, sage |
| Classic | AQSOL | graph_regression | MAE | 0 | — |
| Classic | Coauthor-CS | node_classification | Accuracy | 49 | gcn, gin, sage |
| Classic | Coauthor-Physics | node_classification | Accuracy | 40 | gcn, gin, sage |
| Classic | Reddit | node_classification | F1 | 116 | gcn, gin, sage |
| Classic | ZINC | graph_regression | MAE | 1093 | gcn, gin, sage |
| CosmoBench | CAMELS-SAM | graph_regression | R^2 | 7 | — |
| CosmoBench | CS-Trees | graph_regression | R2 | 14 | — |
| CosmoBench | CS-Trees-200 | graph_classification | Accuracy | 10 | — |
| CosmoBench | Quijote | graph_regression | R^2 | 6 | — |
| DualEquiNet RNA Benchmarks | Ribonanza | graph_regression | RMSE | 11 | — |
| DualEquiNet RNA Benchmarks | Tc-Ribo | graph_regression | RMSE | 11 | — |
| DualEquiNet RNA Benchmarks | TorsionAngle | graph_regression | Circular MAE | 8 | — |
| ECHO Benchmark | ECHO-Charge | graph_regression | MAE | 11 | gcn, gin |
| ECHO Benchmark | ECHO-Energy | graph_regression | MAE | 11 | gcn, gin |
| ECHO Benchmark | ECHO-Synth | graph_regression | MAE | 10 | gcn, gin |
| GNNBenchmark | CIFAR10 | graph_classification | Accuracy | 322 | gcn, gin, sage |
| GNNBenchmark | CLUSTER | node_classification | Accuracy | 236 | gcn, gin, sage |
| GNNBenchmark | CSL | graph_classification | Accuracy | 46 | gcn, gin |
| GNNBenchmark | MNIST | graph_classification | Accuracy | 309 | gcn, gin, sage |
| GNNBenchmark | PATTERN | node_classification | Accuracy | 256 | gcn, gin, sage |
| GNNBenchmark | TSP | link_prediction | F1 | 8 | — |
=======
| Algorithmic Graph Tasks | Eccentricity | graph_regression | MSE | 0 | — |
| Algorithmic Graph Tasks | SSSP | graph_regression | MSE | 0 | — |
| City-Networks | London | node_classification | Accuracy | 0 | — |
| City-Networks | Los Angeles | node_classification | Accuracy | 0 | — |
| City-Networks | Paris | node_classification | Accuracy | 0 | — |
| City-Networks | Shanghai | node_classification | Accuracy | 0 | — |
| Classic | AQSOL | graph_regression | MAE | 17 | gcn, gin, sage |
| Classic | PPI | node_classification | F1 | 22 | gcn, gin, sage |
| Classic | Reddit | node_classification | F1 | 34 | gcn, gin, sage |
| Classic | WikiCS | node_classification | Accuracy | 23 | gcn, gin, sage |
| CosmoBench | CAMELS-SAM | graph_regression | R^2 | 0 | — |
| CosmoBench | CS-Trees | graph_regression | R2 | 0 | — |
| CosmoBench | CS-Trees-200 | graph_classification | Accuracy | 0 | — |
| CosmoBench | Quijote | graph_regression | R^2 | 0 | — |
| DualEquiNet RNA Benchmarks | COVID | graph_regression | RMSE | 7 | — |
| DualEquiNet RNA Benchmarks | Ribonanza | graph_regression | RMSE | 7 | — |
| DualEquiNet RNA Benchmarks | Tc-Ribo | graph_regression | RMSE | 7 | — |
| DualEquiNet RNA Benchmarks | TorsionAngle | graph_regression | Circular MAE | 7 | — |
| ECHO Benchmark | ECHO-Charge | graph_regression | MAE | 0 | — |
| ECHO Benchmark | ECHO-Energy | graph_regression | MAE | 0 | — |
| ECHO Benchmark | ECHO-Synth | graph_regression | MAE | 0 | — |
| GNNBenchmark | CIFAR10 | graph_classification | Accuracy | 85 | gcn, gin, sage |
| GNNBenchmark | CLUSTER | node_classification | Accuracy | 68 | gcn, gin, sage |
| GNNBenchmark | CSL | graph_classification | Accuracy | 9 | gcn |
| GNNBenchmark | MNIST | graph_classification | Accuracy | 96 | gcn, gin, sage |
| GNNBenchmark | PATTERN | node_classification | Accuracy | 103 | gcn, gin, sage |
| GNNBenchmark | TSP | link_prediction | F1 | 7 | gcn, gin, sage |
>>>>>>> Stashed changes
| GraphBench | Algorithmic Reasoning | graph_classification | Accuracy | 0 | — |
| GraphBench | BA graph | graph_classification | Accuracy | 26 | gcn, gin, sage |
| GraphBench | BlueSky | node_classification | MAE | 0 | — |
| GraphBench | Bridges | graph_classification | F1 | 5 | — |
| GraphBench | Chip Design | graph_generation | Accuracy | 0 | — |
| GraphBench | Combinatorial Optimization | node_classification | Accuracy | 0 | — |
| GraphBench | ER graph | graph_classification | Accuracy | 20 | gcn, gin, sage |
| GraphBench | Electronic Circuits | graph_classification | MAE | 0 | — |
| GraphBench | Flow | graph_regression | MAE | 14 | gin |
| GraphBench | MST | graph_classification | F1 | 5 | — |
| GraphBench | Max Clique | graph_classification | F1 | 0 | — |
| GraphBench | Max Matching | graph_classification | F1 | 0 | — |
| GraphBench | RB graph | graph_classification | Accuracy | 7 | gcn, gin, sage |
| GraphBench | SAT Solving | node_classification | Accuracy | 0 | — |
| GraphBench | Steiner Trees | graph_classification | F1 | 0 | — |
| GraphBench | Topological Sorting | node_classification | MAE | 0 | — |
| GraphBench | Weather Forecasting | node_classification | MAE | 0 | — |
| HSG-12M | HSG-12M | graph_classification | Accuracy | 8 | gcn, gin, sage |
| HSG-12M | HSG-topology | graph_classification | Accuracy | 8 | gcn, gin, sage |
| Heterogeneous Graph Benchmarks | ACM | node_classification | Micro-F1 | 0 | — |
| Heterogeneous Graph Benchmarks | DBLP | node_classification | Micro-F1 | 0 | — |
| Heterogeneous Graph Benchmarks | Freebase | node_classification | Macro-F1 | 0 | — |
| Heterogeneous Graph Benchmarks | IMDB | node_classification | Micro-F1 | 0 | — |
| Heterogeneous Graph Benchmarks | RCDD | link_prediction | MRR | 0 | — |
| Heterophilic Graphs | Amazon-ratings | node_classification | Accuracy | 87 | gcn, sage |
| Heterophilic Graphs | Deezer | node_classification | ROC-AUC | 1 | — |
| Heterophilic Graphs | Minesweeper | node_classification | ROC-AUC | 35 | gcn, sage |
| Heterophilic Graphs | Questions | node_classification | ROC-AUC | 45 | gcn, sage |
| Heterophilic Graphs | Tolokers | node_classification | ROC-AUC | 87 | gcn, sage |
| Hypergraph Benchmarks | AMAP | node_classification | F1 | 0 | — |
| Hypergraph Benchmarks | BAT | node_classification | F1 | 0 | — |
| Hypergraph Benchmarks | Congress | node_classification | Accuracy | 0 | — |
| Hypergraph Benchmarks | Cora-CA | node_classification | Accuracy | 0 | — |
| Hypergraph Benchmarks | DBLP-CA | node_classification | Accuracy | 0 | — |
| Hypergraph Benchmarks | EAT | node_classification | F1 | 0 | — |
| Hypergraph Benchmarks | House | node_classification | Accuracy | 0 | — |
| Hypergraph Benchmarks | LEN | node_classification | Accuracy | 6 | — |
| Hypergraph Benchmarks | Senate | node_classification | Accuracy | 0 | — |
| Hypergraph Benchmarks | UAT | node_classification | F1 | 0 | — |
| Hypergraph Benchmarks | Walmart | node_classification | Accuracy | 0 | — |
| Knowledge Graphs | FB15k-237 | link_prediction | MRR | 7 | — |
| Knowledge Graphs | WN18 | link_prediction | MRR | 7 | — |
| Knowledge Graphs | WN18RR | link_prediction | MRR | 0 | — |
| LRGB | COCO-SP | node_classification | F1 | 54 | gcn, gin |
| LRGB | PCQM-Contact | link_prediction | MRR | 57 | gcn, gin |
| LRGB | PascalVOC-SP | node_classification | F1 | 69 | gcn, gin |
| LRGB | Peptides-func | graph_classification | AP | 183 | gcn, gin |
| LRGB | Peptides-struct | graph_regression | MAE | 208 | gcn, gin |
| LRIM Graph Benchmark | LRIM | node_regression | log-MSE | 0 | — |
| MoleculeNet | BACE | graph_classification | ROC-AUC | 18 | gcn, gin |
| MoleculeNet | BBBP | graph_classification | ROC-AUC | 19 | gcn, gin, sage |
| MoleculeNet | ClinTox | graph_classification | ROC-AUC | 0 | — |
| MoleculeNet | ESOL | graph_regression | RMSE | 5 | — |
| MoleculeNet | FreeSolv | graph_regression | RMSE | 0 | — |
| MoleculeNet | Lipophilicity | graph_regression | RMSE | 0 | — |
| MoleculeNet | SIDER | graph_classification | ROC-AUC | 0 | — |
| MoleculeNet | Tox21 | graph_classification | ROC-AUC | 39 | gcn, gin, sage |
| MoleculeNet | ToxCast | graph_classification | ROC-AUC | 0 | — |
| OGB | Code | graph_classification | F1 | 18 | gcn, gin |
| OGB | PCQM4Mv2 | graph_regression | MAE | 39 | gcn, gin, sage |
| OGB | ogbg-molhiv | graph_classification | ROC-AUC | 87 | gcn, gin, sage |
| OGB | ogbg-molpcba | graph_classification | AP | 101 | gcn, gin, sage |
| OGB | ogbl-biokg | link_prediction | MRR | 12 | — |
| OGB | ogbl-collab | link_prediction | Hits@50 | 13 | gcn, gin, sage |
| OGB | ogbl-ddi | link_prediction | Hits@20 | 11 | gcn, gin, sage |
| OGB | ogbl-wikikg2 | link_prediction | MRR | 45 | — |
| Other Graph Benchmarks | 20News | graph_classification | Accuracy | 12 | gcn |
| Other Graph Benchmarks | Amazon2M | node_classification | Accuracy | 2 | — |
| Other Graph Benchmarks | MalNet-Tiny | graph_classification | Accuracy | 17 | gcn, gin |
| Other Graph Benchmarks | ShapeNet-Part | node_classification | F1 | 0 | — |
| Power Flow Benchmarks | Case 1 | graph_regression | Accuracy | 0 | — |
| Power Flow Benchmarks | Case 2 | graph_regression | Accuracy | 0 | — |
| Quantum Chemistry | MD17 | graph_regression | MAE | 0 | — |
| Quantum Chemistry | QM7b | graph_regression | MAE | 0 | — |
<<<<<<< Updated upstream
| Quantum Chemistry | QM9 | graph_regression | MAE | 81 | gcn, gin |
| TU Dortmund | AIDS | graph_classification | AUROC | 0 | — |
| TU Dortmund | COLLAB | graph_classification | Accuracy | 134 | gcn, gin, sage |
| TU Dortmund | ENZYMES | graph_classification | Accuracy | 174 | gcn, gin, sage |
| TU Dortmund | IMDB-BINARY | graph_classification | Accuracy | 231 | gcn, gin, sage |
| TU Dortmund | IMDB-MULTI | graph_classification | Accuracy | 127 | gcn, gin, sage |
| TU Dortmund | MUTAG | graph_classification | Accuracy | 257 | gcn, gin, sage |
| TU Dortmund | NCI1 | graph_classification | Accuracy | 165 | gcn, gin, sage |
| TU Dortmund | PROTEINS | graph_classification | Accuracy | 339 | gcn, gin, sage |
| TU Dortmund | PTC | graph_classification | Accuracy | 0 | — |
| TU Dortmund | PTC_MR | graph_classification | Accuracy | 32 | gin |
| TU Dortmund | RDT-B | graph_classification | Accuracy | 6 | gin |
| TU Dortmund | REDDIT-BINARY | graph_classification | Accuracy | 43 | gcn, gin |
| TU Dortmund | REDDIT-MULTI-5K | graph_classification | Accuracy | 34 | gcn, gin |
=======
| Quantum Chemistry | QM9 | graph_regression | MAE | 39 | gcn, gin |
| TU Dortmund | COLLAB | graph_classification | Accuracy | 77 | gcn, gin, sage |
| TU Dortmund | ENZYMES | graph_classification | Accuracy | 54 | gcn, gin, sage |
| TU Dortmund | IMDB-BINARY | graph_classification | Accuracy | 86 | gcn, gin, sage |
| TU Dortmund | IMDB-MULTI | graph_classification | Accuracy | 34 | gcn, gin, sage |
| TU Dortmund | MUTAG | graph_classification | Accuracy | 83 | gcn, gin, sage |
| TU Dortmund | NCI1 | graph_classification | Accuracy | 93 | gcn, gin, sage |
| TU Dortmund | PROTEINS | graph_classification | Accuracy | 129 | gcn, gin, sage |
| TU Dortmund | RDT-B | graph_classification | Accuracy | 1 | — |
| TU Dortmund | REDDIT-BINARY | graph_classification | Accuracy | 27 | gcn, gin, sage |
| TU Dortmund | REDDIT-MULTI-5K | graph_classification | Accuracy | 53 | gcn, gin, sage |
>>>>>>> Stashed changes
