---
title: Baseline Coverage Gaps
type: dev
description: Datasets missing common GNN or MLP baseline families
---

## Baseline Coverage Gaps

Datasets in this report are missing one of the baseline families we usually want on the leaderboard for context.

### No GCN/GIN/GraphSAGE Baseline (49)

| Benchmark | Dataset | Task | Metric | Results | Present Families |
|-----------|---------|------|--------|--------:|------------------|
| Classic | AQSOL | graph_regression | MAE | 0 | — |
| CosmoBench | CAMELS-SAM | graph_regression | R^2 | 7 | — |
| CosmoBench | CS-Trees | graph_regression | R2 | 14 | — |
| CosmoBench | CS-Trees-200 | graph_classification | Accuracy | 10 | — |
| CosmoBench | Quijote | graph_regression | R^2 | 6 | — |
| DualEquiNet RNA Benchmarks | Ribonanza | graph_regression | RMSE | 11 | — |
| DualEquiNet RNA Benchmarks | Tc-Ribo | graph_regression | RMSE | 11 | — |
| DualEquiNet RNA Benchmarks | TorsionAngle | graph_regression | Circular MAE | 8 | — |
| GNNBenchmark | TSP | link_prediction | F1 | 8 | — |
| GraphBench | Algorithmic Reasoning | graph_classification | Accuracy | 0 | — |
| GraphBench | BlueSky | node_classification | MAE | 3 | mlp |
| GraphBench | Chip Design | graph_generation | Accuracy | 0 | — |
| GraphBench | Combinatorial Optimization | node_classification | Accuracy | 0 | — |
| GraphBench | SAT Solving | node_classification | Accuracy | 42 | — |
| GraphBench | Social Networks | node_classification | MAE | 0 | — |
| GraphBench | Weather Forecasting | node_classification | MAE | 9 | — |
| Heterogeneous Graph Benchmarks | Freebase | node_classification | Macro-F1 | 0 | — |
| Heterogeneous Graph Benchmarks | RCDD | link_prediction | MRR | 0 | — |
| Hypergraph Benchmarks | BAT | node_classification | F1 | 9 | — |
| Hypergraph Benchmarks | Congress | node_classification | Accuracy | 12 | — |
| Hypergraph Benchmarks | Cora-CA | node_classification | Accuracy | 23 | — |
| Hypergraph Benchmarks | DBLP-CA | node_classification | Accuracy | 12 | — |
| Hypergraph Benchmarks | EAT | node_classification | F1 | 9 | — |
| Hypergraph Benchmarks | House | node_classification | Accuracy | 2 | — |
| Hypergraph Benchmarks | Senate | node_classification | Accuracy | 2 | — |
| Hypergraph Benchmarks | UAT | node_classification | F1 | 9 | — |
| Hypergraph Benchmarks | Walmart | node_classification | Accuracy | 11 | — |
| Knowledge Graphs | WN18 | link_prediction | MRR | 0 | — |
| Knowledge Graphs | WN18RR | link_prediction | MRR | 0 | — |
| MoleculeNet | FreeSolv | graph_regression | RMSE | 0 | — |
| MoleculeNet | Lipophilicity | graph_regression | RMSE | 0 | — |
| OGB | Yelp | node_classification | Micro-F1 Score | 0 | — |
| OGB | ogbl-biokg | link_prediction | MRR | 0 | — |
| OGB | ogbl-citation2 | link_prediction | MRR | 4 | — |
| OGB | ogbl-ddi | link_prediction | Hits@20 | 0 | — |
| OGB | ogbn-mag | node_classification | Accuracy | 0 | — |
| Other Graph Benchmarks | 20News | graph_classification | Accuracy | 9 | — |
| Power Flow Benchmarks | Case 1 | graph_regression | Accuracy | 4 | — |
| Power Flow Benchmarks | Case 2 | graph_regression | Accuracy | 7 | — |
| PyG Imported Datasets | Alchemy | graph_regression | MAE | 0 | — |
| PyG Imported Datasets | BlogCatalog | node_classification | Accuracy | 0 | — |
| PyG Imported Datasets | Community | node_classification | Accuracy | 0 | — |
| PyG Imported Datasets | FAUST | graph_classification | Accuracy | 0 | — |
| PyG Imported Datasets | Facebook | node_classification | Accuracy | 0 | — |
| PyG Imported Datasets | Yelp | node_classification | Macro-F1 | 0 | — |
| Quantum Chemistry | MD17 | graph_regression | MAE | 0 | — |
| Quantum Chemistry | QM7b | graph_regression | MAE | 0 | — |
| TU Dortmund | AIDS | graph_classification | AUROC | 0 | — |
| TU Dortmund | PTC | graph_classification | Accuracy | 0 | — |

### No MLP Baseline (114)

| Benchmark | Dataset | Task | Metric | Results | Present Families |
|-----------|---------|------|--------|--------:|------------------|
| Algorithmic Graph Tasks | Eccentricity | graph_regression | MSE | 11 | gcn, gin, sage |
| Algorithmic Graph Tasks | SSSP | graph_regression | MSE | 11 | gcn, gin, sage |
| Classic | AQSOL | graph_regression | MAE | 0 | — |
| Classic | Coauthor-CS | node_classification | Accuracy | 49 | gcn, gin, sage |
| Classic | Coauthor-Physics | node_classification | Accuracy | 40 | gcn, gin, sage |
| Classic | Reddit | node_classification | F1 | 116 | gcn, gin, sage |
| Classic | ZINC | graph_regression | MAE | 1078 | gcn, gin, sage |
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
| GNNBenchmark | CIFAR10 | graph_classification | Accuracy | 312 | gcn, gin, sage |
| GNNBenchmark | CLUSTER | node_classification | Accuracy | 236 | gcn, gin, sage |
| GNNBenchmark | CSL | graph_classification | Accuracy | 46 | gcn, gin |
| GNNBenchmark | MNIST | graph_classification | Accuracy | 301 | gcn, gin, sage |
| GNNBenchmark | PATTERN | node_classification | Accuracy | 256 | gcn, gin, sage |
| GNNBenchmark | TSP | link_prediction | F1 | 8 | — |
| GraphBench | Algorithmic Reasoning | graph_classification | Accuracy | 0 | — |
| GraphBench | Bridges | graph_classification | F1 | 16 | gin |
| GraphBench | Chip Design | graph_generation | Accuracy | 0 | — |
| GraphBench | Combinatorial Optimization | node_classification | Accuracy | 0 | — |
| GraphBench | Electronic Circuits | graph_classification | MAE | 4 | gcn, gin |
| GraphBench | Flow | graph_regression | MAE | 32 | gin |
| GraphBench | MST | graph_classification | F1 | 16 | gin |
| GraphBench | Max Clique | graph_classification | F1 | 6 | gin |
| GraphBench | Max Matching | graph_classification | F1 | 6 | gin |
| GraphBench | SAT Solving | node_classification | Accuracy | 42 | — |
| GraphBench | Social Networks | node_classification | MAE | 0 | — |
| GraphBench | Steiner Trees | graph_classification | F1 | 6 | gin |
| GraphBench | Topological Sorting | node_classification | MAE | 6 | gin |
| GraphBench | Weather Forecasting | node_classification | MAE | 9 | — |
| HSG-12M | HSG-12M | graph_classification | Accuracy | 8 | gcn, gin, sage |
| HSG-12M | HSG-topology | graph_classification | Accuracy | 8 | gcn, gin, sage |
| Heterogeneous Graph Benchmarks | ACM | node_classification | Micro-F1 | 14 | gcn |
| Heterogeneous Graph Benchmarks | DBLP | node_classification | Micro-F1 | 59 | gcn, gin, sage |
| Heterogeneous Graph Benchmarks | Freebase | node_classification | Macro-F1 | 0 | — |
| Heterogeneous Graph Benchmarks | IMDB | node_classification | Micro-F1 | 25 | gcn, gin |
| Heterogeneous Graph Benchmarks | RCDD | link_prediction | MRR | 0 | — |
| Heterophilic Graphs | Minesweeper | node_classification | ROC-AUC | 222 | gcn, gin, sage |
| Heterophilic Graphs | Questions | node_classification | ROC-AUC | 127 | gcn, gin, sage |
| Heterophilic Graphs | Tolokers | node_classification | ROC-AUC | 186 | gcn, gin, sage |
| Hypergraph Benchmarks | BAT | node_classification | F1 | 9 | — |
| Hypergraph Benchmarks | Congress | node_classification | Accuracy | 12 | — |
| Hypergraph Benchmarks | Cora-CA | node_classification | Accuracy | 23 | — |
| Hypergraph Benchmarks | DBLP-CA | node_classification | Accuracy | 12 | — |
| Hypergraph Benchmarks | EAT | node_classification | F1 | 9 | — |
| Hypergraph Benchmarks | House | node_classification | Accuracy | 2 | — |
| Hypergraph Benchmarks | LEN | node_classification | Accuracy | 30 | gcn, gin, sage |
| Hypergraph Benchmarks | Senate | node_classification | Accuracy | 2 | — |
| Hypergraph Benchmarks | UAT | node_classification | F1 | 9 | — |
| Hypergraph Benchmarks | Walmart | node_classification | Accuracy | 11 | — |
| Knowledge Graphs | WN18 | link_prediction | MRR | 0 | — |
| Knowledge Graphs | WN18RR | link_prediction | MRR | 0 | — |
| LINKX Benchmarks | Pokec | node_classification | Accuracy | 13 | gcn |
| LINKX Benchmarks | twitch-gamers | node_classification | Accuracy | 13 | gcn |
| LRGB | PCQM-Contact | link_prediction | MRR | 172 | gcn, gin |
| LRIM Graph Benchmark | LRIM | node_regression | log-MSE | 39 | gin |
| MoleculeNet | ClinTox | graph_classification | ROC-AUC | 60 | gcn, gin, sage |
| MoleculeNet | ESOL | graph_regression | RMSE | 16 | gcn, gin |
| MoleculeNet | FreeSolv | graph_regression | RMSE | 0 | — |
| MoleculeNet | Lipophilicity | graph_regression | RMSE | 0 | — |
| MoleculeNet | MUV | graph_classification | AUROC | 33 | gcn, gin, sage |
| MoleculeNet | SIDER | graph_classification | ROC-AUC | 52 | gcn, gin, sage |
| MoleculeNet | Tox21 | graph_classification | ROC-AUC | 91 | gcn, gin, sage |
| MoleculeNet | ToxCast | graph_classification | ROC-AUC | 62 | gcn, gin, sage |
| OGB | Alchemy | graph_regression | MAE | 10 | gin |
| OGB | Code | graph_classification | F1 | 31 | gcn, gin |
| OGB | PCQM4Mv2 | graph_regression | MAE | 69 | gcn, gin |
| OGB | Yelp | node_classification | Micro-F1 Score | 0 | — |
| OGB | ogbl-biokg | link_prediction | MRR | 0 | — |
| OGB | ogbl-citation2 | link_prediction | MRR | 4 | — |
| OGB | ogbl-collab | link_prediction | Hits@50 | 15 | gcn |
| OGB | ogbl-ddi | link_prediction | Hits@20 | 0 | — |
| OGB | ogbl-wikikg2 | link_prediction | MRR | 35 | gcn |
| OGB | ogbn-mag | node_classification | Accuracy | 0 | — |
| OGB | ogbn-papers100M | node_classification | Accuracy | 10 | gcn |
| OGB | ogbn-products | node_classification | Accuracy | 61 | gcn, sage |
| Other Graph Benchmarks | 20News | graph_classification | Accuracy | 9 | — |
| Other Graph Benchmarks | Amazon2M | node_classification | Accuracy | 13 | gcn |
| Other Graph Benchmarks | MalNet-Tiny | graph_classification | Accuracy | 49 | gcn, gin, sage |
| Other Graph Benchmarks | ShapeNet-Part | node_classification | F1 | 8 | gcn |
| Power Flow Benchmarks | Case 1 | graph_regression | Accuracy | 4 | — |
| Power Flow Benchmarks | Case 2 | graph_regression | Accuracy | 7 | — |
| PyG Imported Datasets | Alchemy | graph_regression | MAE | 0 | — |
| PyG Imported Datasets | Blog | node_classification | Accuracy | 15 | gcn |
| PyG Imported Datasets | BlogCatalog | node_classification | Accuracy | 0 | — |
| PyG Imported Datasets | Community | node_classification | Accuracy | 0 | — |
| PyG Imported Datasets | FAUST | graph_classification | Accuracy | 0 | — |
| PyG Imported Datasets | Facebook | node_classification | Accuracy | 0 | — |
| PyG Imported Datasets | Flickr | node_classification | Accuracy | 14 | gcn |
| PyG Imported Datasets | QM8 | graph_regression | MAE | 9 | gcn, gin |
| PyG Imported Datasets | Yelp | node_classification | Macro-F1 | 0 | — |
| Quantum Chemistry | MD17 | graph_regression | MAE | 0 | — |
| Quantum Chemistry | QM7b | graph_regression | MAE | 0 | — |
| Quantum Chemistry | QM9 | graph_regression | MAE | 81 | gcn, gin |
| TU Dortmund | AIDS | graph_classification | AUROC | 0 | — |
| TU Dortmund | COLLAB | graph_classification | Accuracy | 126 | gcn, gin, sage |
| TU Dortmund | ENZYMES | graph_classification | Accuracy | 174 | gcn, gin, sage |
| TU Dortmund | IMDB-BINARY | graph_classification | Accuracy | 231 | gcn, gin, sage |
| TU Dortmund | IMDB-MULTI | graph_classification | Accuracy | 119 | gcn, gin, sage |
| TU Dortmund | MUTAG | graph_classification | Accuracy | 257 | gcn, gin, sage |
| TU Dortmund | NCI1 | graph_classification | Accuracy | 165 | gcn, gin, sage |
| TU Dortmund | PROTEINS | graph_classification | Accuracy | 339 | gcn, gin, sage |
| TU Dortmund | PTC | graph_classification | Accuracy | 0 | — |
| TU Dortmund | PTC_MR | graph_classification | Accuracy | 32 | gin |
| TU Dortmund | RDT-B | graph_classification | Accuracy | 6 | gin |
| TU Dortmund | REDDIT-BINARY | graph_classification | Accuracy | 39 | gcn, gin |
| TU Dortmund | REDDIT-MULTI-5K | graph_classification | Accuracy | 34 | gcn, gin |