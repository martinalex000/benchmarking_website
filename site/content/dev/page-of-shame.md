---
title: Page of Shame
type: dev
description: Papers whose reported model values materially disagree with the stored
  benchmark values
---

## Page of Shame: Papers Using Wrong Model Values

This page lists papers whose reported primary-metric value for a model disagrees with the stored global benchmark value by more than the reported std, or differs at all when no std is given.

**Flagged papers:** 125
**Flagged rows:** 2186
**Rows where a better value was already known at publication time:** 912
**Rows whose current best source is from a later paper:** 1220
**Rows whose current best source is the same paper:** 54
**Rows with unknown timing:** 0

### Most affected datasets

| Dataset | Wrong Rows | Papers | Models | Worst Rank Shift | Earlier-known Rows |
|---|---:|---:|---:|---:|---:|
| ZINC | 225 | 41 | 36 | 216 | 116 |
| Peptides-func | 193 | 60 | 25 | 287 | 55 |
| Peptides-struct | 178 | 57 | 23 | 312 | 36 |
| Cora | 130 | 28 | 38 | 292 | 52 |
| CiteSeer | 88 | 18 | 24 | 177 | 38 |
| PubMed | 73 | 14 | 22 | 148 | 16 |
| Chameleon | 72 | 12 | 24 | 109 | 43 |
| CIFAR10 | 65 | 21 | 11 | 89 | 18 |
| ogbn-arxiv | 64 | 20 | 15 | 90 | 40 |
| Texas | 62 | 15 | 24 | 136 | 44 |
| MNIST | 62 | 21 | 8 | 86 | 13 |
| Roman-empire | 58 | 18 | 13 | 82 | 35 |
| PascalVOC-SP | 57 | 19 | 10 | 63 | 13 |
| PCQM-Contact | 57 | 16 | 9 | 61 | 30 |
| Squirrel | 55 | 10 | 21 | 87 | 23 |
| PATTERN | 53 | 16 | 6 | 63 | 18 |
| COCO-SP | 47 | 16 | 10 | 33 | 14 |
| Wisconsin | 45 | 16 | 16 | 134 | 23 |
| Minesweeper | 44 | 13 | 8 | 76 | 26 |
| Cornell | 42 | 14 | 18 | 131 | 35 |
| CLUSTER | 38 | 13 | 4 | 44 | 16 |
| ogbg-molhiv | 36 | 16 | 10 | 180 | 2 |
| PROTEINS | 35 | 13 | 13 | 170 | 17 |
| LRIM | 30 | 1 | 6 | 5 | 0 |
| Amazon-ratings | 29 | 13 | 6 | 83 | 18 |

### Most affected models

| Model | Wrong Rows | Papers | Datasets | Worst Rank Shift | Earlier-known Rows |
|---|---:|---:|---:|---:|---:|
| GCN | 503 | 108 | 54 | 312 | 237 |
| GatedGCN | 241 | 63 | 18 | 269 | 58 |
| GAT | 198 | 61 | 34 | 244 | 103 |
| GIN | 190 | 61 | 34 | 297 | 56 |
| GINE | 72 | 31 | 6 | 245 | 30 |
| GPS | 68 | 36 | 10 | 216 | 36 |
| NodeFormer | 47 | 15 | 15 | 132 | 18 |
| Nagphormer | 44 | 17 | 15 | 196 | 14 |
| GPRGNN | 42 | 11 | 14 | 231 | 18 |
| MLP | 39 | 13 | 13 | 225 | 12 |
| APPNP | 36 | 12 | 12 | 250 | 21 |
| SGFormer | 35 | 10 | 13 | 202 | 15 |
| GraphSAGE | 35 | 17 | 17 | 133 | 24 |
| Graphormer | 33 | 27 | 6 | 175 | 13 |
| Exphormer | 33 | 15 | 15 | 156 | 5 |
| GatedGCN+RWSE | 31 | 17 | 2 | 119 | 6 |
| H2GCN | 27 | 10 | 9 | 114 | 9 |
| GraphGPS | 18 | 7 | 8 | 173 | 7 |
| Polynormer | 18 | 5 | 8 | 115 | 7 |
| GAT-sep | 18 | 8 | 4 | 16 | 11 |
| FOSR | 15 | 5 | 10 | 127 | 6 |
| GRIT | 14 | 14 | 1 | 195 | 13 |
| GT | 14 | 2 | 8 | 47 | 1 |
| PNA | 12 | 12 | 1 | 183 | 8 |
| ChebNet | 12 | 4 | 8 | 92 | 1 |

| ArXiv | Title | Wrong Rows | Earlier-known Rows | Worst Rank Shift | Datasets | Models |
|---|---|---:|---:|---:|---|---|
| [2401.01233](/papers/2401.01233/) | [GEN: A Practical Alternative to Graph Transformers for Long-Range Graph...](/papers/2401.01233/) | 79 | 8 | 141 | Amazon-Photo, Amazon-ratings, COCO-SP, Chameleon | CPGNN, Exphormer, FSGNN, GAT |
| [2406.08993](/papers/2406.08993/) | [Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification](/papers/2406.08993/) | 64 | 9 | 118 | Amazon-Photo, Chameleon, CiteSeer, Coauthor-Physics | CPGNN, Exphormer, FSGNN, GAT |
| [2308.11129](/papers/2308.11129/) | [Enhancing Graph Transformers with Hierarchical Distance Structural Encoding](/papers/2308.11129/) | 61 | 2 | 284 | Actor, CIFAR10, CLUSTER, Chameleon | APPNP, CIN, GAT, GCN |
| [2512.14619](/papers/2512.14619/) | [ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation Learning](/papers/2512.14619/) | 52 | 50 | 126 | Amazon-Computers, Chameleon, CiteSeer, Cora | APPNP, CoBFormer, GAT, GCN |
| [2406.03386](/papers/2406.03386/) | [Learning Long Range Dependencies on Graphs via Random Walks](/papers/2406.03386/) | 50 | 9 | 197 | Amazon-ratings, CIFAR10, CLUSTER, COCO-SP | CRaWl, Exphormer, GAT, GAT-sep |
| [2310.05174](/papers/2310.05174/) | [GSLB: The Graph Structure Learning Benchmark](/papers/2310.05174/) | 48 | 9 | 297 | Actor, COLLAB, CiteSeer, Cora | GAT, GCN, GIN, GPRGNN |
| [2410.05697](/papers/2410.05697/) | [Diffusing to the Top: Boost Graph Neural Networks with Minimal...](/papers/2410.05697/) | 46 | 17 | 211 | Actor, Amazon-Computers, COCO-SP, CiteSeer | APPNP, ChebNet, GAT, GCN |
| [2507.00647](/papers/2507.00647/) | [Cooperative Sheaf Neural Networks](/papers/2507.00647/) | 44 | 44 | 110 | Amazon-ratings, Cornell, Film, Minesweeper | ACMGCN, FAGCN, FSGNN, GAT |
| [2411.15671](/papers/2411.15671/) | [Best of Both Worlds: Advantages of Hybrid Graph Sequence Models](/papers/2411.15671/) | 40 | 17 | 89 | Amazon-ratings, CIFAR10, D&D, MNIST | Exphormer, GAT, GCN, GIN |
| [2312.16560](/papers/2312.16560/) | [Algorithmic Graph Tasks](/papers/2312.16560/) | 39 | 9 | 284 | Actor, Chameleon, CiteSeer, Cora | GAT, GCN, GCN+JK, GINE |
| [2407.05649](/papers/2407.05649/) | [Greener GRASS: Enhancing GNNs with Encoding, Rewiring, and Attention](/papers/2407.05649/) | 38 | 9 | 197 | CIFAR10, CLUSTER, COCO-SP, MNIST | CIN, DRew(GatedGCN), DRew-GCN+LapPE, Drew-GIN |
| [2402.08678](/papers/2402.08678/) | [Graph Mamba: Towards Learning on Graphs with State Space Models](/papers/2402.08678/) | 37 | 0 | 286 | Amazon-ratings, CIFAR10, COCO-SP, MNIST | CRaWl, Exphormer, GCN, GIN |
| [2508.05070](/papers/2508.05070/) | [Tango: Graph Neural Dynamics via Learned Energy and Tangential Flows](/papers/2508.05070/) | 37 | 29 | 284 | Amazon-ratings, CLUSTER, Minesweeper, PATTERN | GAT, GAT-sep, GCN, GIN |
| [2501.18739](/papers/2501.18739/) | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | 36 | 29 | 236 | Amazon-Computers, COLLAB, Cora, PubMed | APPNP, GAT, GCN, GIN |
| [2410.05593](/papers/2410.05593/) | [When Graph Neural Networks Meet Dynamic Mode Decomposition](/papers/2410.05593/) | 36 | 15 | 223 | COCO-SP, CiteSeer, Cora, Cornell | APPNP, GAT, GCN, GPRGNN |
| [2410.13798](/papers/2410.13798/) | [Learning Graph Quantized Tokenizers](/papers/2410.13798/) | 35 | 19 | 284 | COCO-SP, CiteSeer, Cora, PCQM-Contact | APPNP, Exphormer, GAT, GCN |
| [2504.12588](/papers/2504.12588/) | [Plain Transformers Can be Powerful Graph Learners](/papers/2504.12588/) | 34 | 33 | 197 | CIFAR10, CLUSTER, MNIST, PATTERN | GAT, GCN, GIN, GPS |
| [2603.27529](/papers/2603.27529/) | [Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in GNNs](/papers/2603.27529/) | 33 | 33 | 292 | Amazon-Photo, Chameleon, CiteSeer, Coauthor-CS | BORF, DR, FOSR, GAT |
| [2310.07430](/papers/2310.07430/) | [Non-backtracking Graph Neural Networks](/papers/2310.07430/) | 33 | 5 | 286 | CiteSeer, Cora, Cornell, PascalVOC-SP | ChebNet, DRew-GCN+LapPE, GAT, GCN |
| [2407.18480](/papers/2407.18480/) | [Scalable Graph Compressed Convolutions](/papers/2407.18480/) | 33 | 19 | 135 | Actor, COLLAB, Cornell, IMDB-BINARY | ACMII-GCN, APPNP, ChebNet, DiffPool |
| [2401.17791](/papers/2401.17791/) | [Graph Transformers without Positional Encodings](/papers/2401.17791/) | 32 | 3 | 284 | CIFAR10, CLUSTER, MNIST, PATTERN | CIN, GAT, GCN, GIN |
| [2505.23185](/papers/2505.23185/) | [Improving the Effective Receptive Field of Message-Passing Neural Networks](/papers/2505.23185/) | 30 | 20 | 76 | Amazon-ratings, COCO-SP, D&D, London | GAT, GAT-sep, GCN, GPS |
| [IAZXEX1dVV](/papers/IAZXEX1dVV/) | [LRIM: a Physics-Based Benchmark for Provably Evaluating Long-Range Capabilities in...](/papers/IAZXEX1dVV/) | 30 | 0 | 5 | LRIM | GIN, GPS+LapPE, GPS+RWSE, GPS-Base |
| [2406.18380](/papers/2406.18380/) | [KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning](/papers/2406.18380/) | 28 | 15 | 237 | CiteSeer, Cora, Cornell, ENZYMES | GAT, GCN, GIN |
| [2406.03671](/papers/2406.03671/) | [PANDA: Expanded Width-Aware Message Passing Beyond Rewiring](/papers/2406.03671/) | 28 | 6 | 97 | COLLAB, Cora, Cornell, ENZYMES | + DIGL, BORF, FOSR, GCN |
| [2310.19285](/papers/2310.19285/) | [Facilitating Graph Neural Networks with Random Walk on Simplicial Complexes](/papers/2310.19285/) | 27 | 3 | 284 | CIFAR10, MNIST, PCQM-Contact, Peptides-func | CIN, GAT, GCN, GIN |
| [2406.12059](/papers/2406.12059/) | [A Scalable and Effective Alternative to Graph Transformers](/papers/2406.12059/) | 27 | 12 | 284 | COCO-SP, PCQM-Contact, PCQM4Mv2, PascalVOC-SP | ANS-GT, GAT, GCN, GINE |
| [2506.04765](/papers/2506.04765/) | [OpenGT: A Comprehensive Benchmark For Graph Transformers](/papers/2506.04765/) | 27 | 26 | 216 | Chameleon, Cornell, Texas, Wisconsin | APPNP, Exphormer, GAT, GCN |
| [2602.02268](/papers/2602.02268/) | [HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control](/papers/2602.02268/) | 27 | 26 | 216 | Chameleon, Cornell, Texas, Wisconsin | APPNP, Exphormer, GAT, GCN |
| [2405.13806](/papers/2405.13806/) | [A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition](/papers/2405.13806/) | 26 | 5 | 284 | Amazon-Computers, Amazon-Photo, COCO-SP, Coauthor-CS | APPNP, GAT, GCN, GINE |
| [2502.09365](/papers/2502.09365/) | [Simple Path Structural Encoding for Graph Transformers](/papers/2502.09365/) | 26 | 23 | 221 | CIFAR10, CLUSTER, MNIST, PATTERN | GAT, GCN, GIN, GINE |
| [2605.05689](/papers/2605.05689/) | [GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency Model](/papers/2605.05689/) | 26 | 26 | 197 | CIFAR10, CLUSTER, COCO-SP, MNIST | GAT, GCN, GIN, GPS |
| [2502.00282](/papers/2502.00282/) | [GraphMinNet: Learning Dependencies in Graphs with Light Complexity Minimal Architecture](/papers/2502.00282/) | 25 | 24 | 286 | CIFAR10, CLUSTER, MNIST, MalNet-Tiny | Exphormer, GAT, GCN, GIN |
| [2210.07606](/papers/2210.07606/) | [Revisiting Heterophily For Graph Neural Networks](/papers/2210.07606/) | 25 | 0 | 210 | Chameleon, CiteSeer, Cora, Cornell | APPNP, FAGCN, GAT, GCN |
| [2404.09774](/papers/2404.09774/) | [RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional Networks](/papers/2404.09774/) | 23 | 2 | 243 | CIFAR10, CLUSTER, MNIST, PATTERN | GCN, GIN, GINE, GPS |
| [2407.02758](/papers/2407.02758/) | [Differential Encoding for Improved Representation Learning over Graphs](/papers/2407.02758/) | 23 | 8 | 243 | CIFAR10, COCO-SP, MNIST, PCQM-Contact | GCN, GIN, GINE, GPS |
| [2310.03274](/papers/2310.03274/) | [Fragment-based Pretraining and Finetuning on Molecular Graphs](/papers/2310.03274/) | 22 | 6 | 286 | BACE, BBBP, ClinTox, Peptides-func | GCN, GIN, GatedGCN, GatedGCN+RWSE |
| [2402.00789](/papers/2402.00789/) | [Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective State Spaces](/papers/2402.00789/) | 22 | 1 | 89 | CIFAR10, CLUSTER, MNIST, PATTERN | Exphormer, GCN, GIN, GatedGCN |
| [2306.05955](/papers/2306.05955/) | [Path Neural Networks: Expressive and Accurate Graph Neural Networks](/papers/2306.05955/) | 20 | 0 | 286 | IMDB-BINARY, IMDB-MULTI, NCI1, PROTEINS | AgentNet, CIN, DiffPool, ESAN |
| [2502.09263](/papers/2502.09263/) | [Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple...](/papers/2502.09263/) | 20 | 9 | 169 | CIFAR10, COLLAB, MNIST, PATTERN | Exphormer, GCN, GIN, GMN |
| [2512.04475](/papers/2512.04475/) | [GraphBench](/papers/2512.04475/) | 20 | 0 | 2 | Bridges, Flow, MST, Max Clique | GIN, GT |
| [2206.08164](/papers/2206.08164/) | [LRGB](/papers/2206.08164/) | 19 | 0 | 284 | COCO-SP, PCQM-Contact, PascalVOC-SP, Peptides-func | GCN, GINE, GatedGCN, GatedGCN+LapPE |
| [2404.03380](/papers/2404.03380/) | [On the Theoretical Expressive Power and the Design Space of...](/papers/2404.03380/) | 18 | 6 | 284 | Cornell, Peptides-func, Peptides-struct, Texas | CIN, GAT, GCN, GIN |
| [2501.03113](/papers/2501.03113/) | [Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based Centrality](/papers/2501.03113/) | 18 | 6 | 151 | BACE, Peptides-func, Peptides-struct, Tox21 | CIN, GCN, GIN, GPS |
| [2411.17296](/papers/2411.17296/) | [GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers](/papers/2411.17296/) | 18 | 14 | 87 | Actor, Amazon-Photo, Chameleon, CiteSeer | GAT, GCN, GPRGNN, GraphGPS |
| [2602.18837](/papers/2602.18837/) | [L2G-Net: Local to Global Spectral Graph Neural Networks via Cauchy...](/papers/2602.18837/) | 18 | 18 | 71 | Amazon-ratings, Minesweeper, Roman-empire, Tolokers | GAT, GAT-sep, GCN, GPS |
| [2402.08450](/papers/2402.08450/) | [Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph Products](/papers/2402.08450/) | 17 | 2 | 286 | BACE, Peptides-func, Peptides-struct, ZINC | GCN, GIN, GNN (a), GPS |
| [2409.19117](/papers/2409.19117/) | [Range-aware Positional Encoding via High-order Pretraining: Theory and Practice](/papers/2409.19117/) | 17 | 5 | 284 | CIFAR10, MNIST, NCI1, Peptides-func | DGCNN, GAT, GCN, GIN |
| [2506.14098](/papers/2506.14098/) | [Toward a Graph Foundation Model: Pre-Training Transformers With Random Walks](/papers/2506.14098/) | 17 | 6 | 216 | Cora, PubMed, WikiCS, ogbg-molhiv | BGRL, GAT, GCN, GIN |
| [2312.01538](/papers/2312.01538/) | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | 17 | 1 | 189 | Peptides-func, Peptides-struct, ZINC | DRew, GAT, GCN, GIN |
| [2412.07188](/papers/2412.07188/) | [Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking...](/papers/2412.07188/) | 16 | 8 | 258 | Coauthor-CS, Coauthor-Physics, Cora | APPNP, FA, GAT, GATv2 |
| [2601.07419](/papers/2601.07419/) | [Position: Don't be Afraid of Over-Smoothing And Over-Squashing](/papers/2601.07419/) | 16 | 16 | 192 | Amazon-Computers, Amazon-Photo, CiteSeer, Cora | GATv2, GCN, GCN + SDRF, GCNII |
| [2310.20519](/papers/2310.20519/) | [Enhancing Graph Neural Networks with Quantum Computed Encodings](/papers/2310.20519/) | 16 | 0 | 125 | CIFAR10, MNIST, PATTERN, PCQM4Mv2 | GAT, GCN, GIN, GPS |
| [2506.07624](/papers/2506.07624/) | [Return of ChebNet: Understanding and Improving an Overlooked GNN on...](/papers/2506.07624/) | 16 | 12 | 78 | Minesweeper, Peptides-func, Peptides-struct, Tolokers | Drew-GIN, Exphormer, GAT, GAT-sep |
| [2309.00367](/papers/2309.00367/) | [Where Did the Gap Go? Reassessing the Long-Range Graph Benchmark](/papers/2309.00367/) | 16 | 0 | 76 | COCO-SP, PCQM-Contact, PascalVOC-SP, Peptides-func | Exphormer, GCN, GINE, GPS |
| [2310.02156](/papers/2310.02156/) | [Probabilistically Rewired Message-Passing Neural Networks](/papers/2310.02156/) | 15 | 4 | 284 | Cornell, NCI1, Peptides-func, Peptides-struct | + DIGL, DGCNN, DRew-GCN+LapPE, Drew-GIN |
| [2405.02795](/papers/2405.02795/) | [Graph as Point Set](/papers/2405.02795/) | 15 | 3 | 284 | PascalVOC-SP, Peptides-func, Peptides-struct, ZINC | GCN, GIN, GINE, GNN (a) |
| [2410.23686](/papers/2410.23686/) | [Towards Dynamic Message Passing on Graphs](/papers/2410.23686/) | 15 | 6 | 284 | COLLAB, IMDB-BINARY, IMDB-MULTI, NCI1 | DiffPool, GAT, GCN, GIN |
| [2601.19094](/papers/2601.19094/) | [FloydNet: A Learning Paradigm for Global Relational Reasoning](/papers/2601.19094/) | 15 | 11 | 284 | COCO-SP, PCQM-Contact, PascalVOC-SP, Peptides-func | Exphormer, GCN, GPS, Graphormer |
| [2605.06462](/papers/2605.06462/) | [Invariant-Based Diagnostics for Graph Benchmarks](/papers/2605.06462/) | 15 | 11 | 284 | Flow, Peptides-func, Peptides-struct | GCN, GIN, GINE, GPS |
| [2311.04653](/papers/2311.04653/) | [Hybrid Focal and Full-Range Attention Based Graph Transformers](/papers/2311.04653/) | 15 | 1 | 269 | Chameleon, CiteSeer, Cora, Peptides-func | GCN, GPS, GatedGCN, Graph ViT |
| [2405.03481](/papers/2405.03481/) | [AnchorGT: Efficient and Flexible Attention Architecture for Scalable Graph Transformers](/papers/2405.03481/) | 14 | 3 | 284 | CLUSTER, CiteSeer, Peptides-func, Peptides-struct | GAT, GCN, GatedGCN, GraphSAGE |
| [2510.02565](/papers/2510.02565/) | [On The Expressive Power of GNN Derivatives](/papers/2510.02565/) | 14 | 11 | 284 | Peptides-func, Peptides-struct, Tox21 | GCN, GIN, GIN + RWSE, GINE |
| [2509.06777](/papers/2509.06777/) | [Asynchronous Message Passing for Addressing Oversquashing in Graph Neural Networks](/papers/2509.06777/) | 14 | 2 | 119 | ENZYMES, IMDB-BINARY, MUTAG, PROTEINS | BORF, FOSR, GCN + BORF, GCN + DIGL |
| [2405.15540](/papers/2405.15540/) | [Bundle Neural Networks for message diffusion on graphs](/papers/2405.15540/) | 14 | 3 | 76 | Amazon-ratings, Minesweeper, Peptides-func, Peptides-struct | GAT, GAT-sep, GCN, GatedGCN |
| [2410.09737](/papers/2410.09737/) | [Towards Stable, Globally Expressive Graph Representations with Laplacian Eigenvectors](/papers/2410.09737/) | 13 | 9 | 183 | PCQM-Contact, ZINC | CIN, GCN, GIN, GINE |
| [2410.05499](/papers/2410.05499/) | [Unitary convolutions for learning on graphs and groups](/papers/2410.05499/) | 13 | 8 | 149 | ENZYMES, Minesweeper, PROTEINS, PascalVOC-SP | GAT, GCN, GIN, GatedGCN |
| [2310.01267](/papers/2310.01267/) | [Cooperative Graph Neural Networks](/papers/2310.01267/) | 13 | 1 | 71 | Amazon-ratings, IMDB-BINARY, IMDB-MULTI, Minesweeper | DiffPool, GAT, GAT-sep, GCN |
| [2306.02866](/papers/2306.02866/) | [Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance](/papers/2306.02866/) | 12 | 0 | 284 | PCQM-Contact, Peptides-func, Peptides-struct | GCN, GINE, GatedGCN, GatedGCN+RWSE |
| [2604.06336](/papers/2604.06336/) | [BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular Representation Learning](/papers/2604.06336/) | 12 | 12 | 284 | BACE, Peptides-func, Peptides-struct, SIDER | GCN, GINE, GatedGCN, GatedGCN+RWSE |
| [2307.07107](/papers/2307.07107/) | [Graph Positional and Structural Encoder](/papers/2307.07107/) | 12 | 0 | 215 | CIFAR10, MNIST, PCQM4Mv2, Peptides-func | GCN, GIN, GINE, GPS |
| [2410.03424](/papers/2410.03424/) | [Cayley Graph Propagation](/papers/2410.03424/) | 12 | 5 | 153 | COLLAB, PROTEINS, ogbg-molhiv | GCN, GCN + BORF, GCN + FoSR, GCN + PANDA |
| [2406.05815](/papers/2406.05815/) | [What Can We Learn from State Space Models for Machine...](/papers/2406.05815/) | 12 | 0 | 88 | CIFAR10, MNIST, MalNet-Tiny, PATTERN | GCN, GIN, GatedGCN |
| [2306.03561](/papers/2306.03561/) | [CIN++: Enhancing Topological Message Passing](/papers/2306.03561/) | 11 | 0 | 284 | Peptides-func, Peptides-struct, ogbg-molhiv | GCN, GIN, GINE, GSN |
| [2310.01668](/papers/2310.01668/) | [Locality-Aware Graph Rewiring in GNNs](/papers/2310.01668/) | 11 | 0 | 284 | IMDB-BINARY, MUTAG, PROTEINS, Peptides-func | FOSR, GAT, GCN, GCN + FoSR |
| [2311.01276](/papers/2311.01276/) | [Neural Atoms: Propagating Long-range Interaction in Molecular Graphs through Efficient...](/papers/2311.01276/) | 11 | 2 | 284 | PCQM-Contact, Peptides-func, Peptides-struct | GCN, GINE, GatedGCN, GatedGCN+RWSE |
| [2405.13526](/papers/2405.13526/) | [Understanding Virtual Nodes: Oversquashing and Node Heterogeneity](/papers/2405.13526/) | 11 | 2 | 284 | CIFAR10, Peptides-struct, ogbg-molhiv, ogbg-molpcba | GCN, GIN, GINE, GatedGCN |
| [2412.01519](/papers/2412.01519/) | [ReHub: Linear Complexity Graph Transformers with Adaptive Hub-Spoke Reassignment](/papers/2412.01519/) | 11 | 6 | 284 | PCQM-Contact, Peptides-func, Peptides-struct | GCN, GINE, GatedGCN, GatedGCN+RWSE |
| [2604.03815](/papers/2604.03815/) | [k-Maximum Inner Product Attention for Graph Transformers and the Expressive...](/papers/2604.03815/) | 11 | 11 | 78 | COCO-SP, PascalVOC-SP, Peptides-func, Peptides-struct | GAT, GCN, GatedGCN |
| [2405.17311](/papers/2405.17311/) | [Probabilistic Graph Rewiring via Virtual Nodes](/papers/2405.17311/) | 10 | 2 | 110 | Cornell, PCQM-Contact, Peptides-func, QM9 | + DIGL, GCN, GIN, GPS |
| [2502.10818](/papers/2502.10818/) | [On Vanishing Gradients, Over-Smoothing, and Over-Squashing in GNNs: Bridging Recurrent...](/papers/2502.10818/) | 10 | 9 | 93 | Amazon-ratings, Minesweeper, Peptides-func, Peptides-struct | Exphormer, GAT, GCN, GRED |
| [2511.16767](/papers/2511.16767/) | [When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed Graphs...](/papers/2511.16767/) | 10 | 10 | 83 | Amazon-ratings, BACE, BBBP, CiteSeer | GAT, GCN, GIN, MLP |
| [2309.04941](/papers/2309.04941/) | [Distance-Restricted Folklore Weisfeiler-Leman GNNs with Provable Cycle Counting Power](/papers/2309.04941/) | 9 | 1 | 284 | Peptides-func, Peptides-struct, ogbg-molhiv | GCN, GIN, GINE, GatedGCN |
| [2604.17324](/papers/2604.17324/) | [SigGate-GT: Taming Over-Smoothing in Graph Transformers via Sigmoid-Gated Attention](/papers/2604.17324/) | 9 | 9 | 183 | Peptides-func, Peptides-struct, ZINC, ogbg-molhiv | GCN, GRIT, GatedGCN, Graphormer |
| [2406.09291](/papers/2406.09291/) | [A Flexible, Equivariant Framework for Subgraph GNNs via Graph Products...](/papers/2406.09291/) | 9 | 6 | 151 | ZINC | DSS-GNN, GCN, GIN, GNN (a) |
| [2505.15405](/papers/2505.15405/) | [HOPSE: Scalable Higher-Order Positional and Structural Encoder for Combinatorial Representations](/papers/2505.15405/) | 8 | 8 | 200 | MUTAG, NCI1, ZINC | GAT, GCN, GIN |
| [2309.09384](/papers/2309.09384/) | [Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci Curvature](/papers/2309.09384/) | 8 | 0 | 90 | MUTAG, PROTEINS, Wisconsin | BORF, FOSR, GCN, GCN + BORF |
| [2409.11504](/papers/2409.11504/) | [Preventing Representational Rank Collapse in MPNNs by Splitting the Computational...](/papers/2409.11504/) | 7 | 2 | 118 | Roman-empire, Squirrel, ZINC | GAT, GCN, GIN, GatedGCN |
| [2602.17893](/papers/2602.17893/) | [COMBA: Cross Batch Aggregation for Learning Large Graphs with Context...](/papers/2602.17893/) | 7 | 7 | 76 | Amazon-ratings, Minesweeper, Roman-empire, ogbn-arxiv | GCN, Graph Mamba-1, Nagphormer |
| [2310.01704](/papers/2310.01704/) | [Transformers are efficient hierarchical chemical graph learners](/papers/2310.01704/) | 6 | 0 | 286 | Peptides-struct, ZINC | GAT, GCN, GIN, Graphormer |
| [2309.04082](/papers/2309.04082/) | [Curve Your Attention: Mixed-Curvature Transformers for Graph Representation Learning](/papers/2309.04082/) | 6 | 1 | 225 | Cora | GAT, GCN, H2GCN, MLP |
| [2312.04234](/papers/2312.04234/) | [Graph Convolutions Enrich the Self-Attention in Transformers!](/papers/2312.04234/) | 6 | 0 | 171 | CIFAR10, Peptides-func, Peptides-struct, ZINC | GPS, Graph ViT, Graphormer |
| [2508.11390](/papers/2508.11390/) | [A Remedy for Over-Squashing in Graph Learning via Forman‐Ricci Curvature...](/papers/2508.11390/) | 6 | 4 | 157 | NCI1, PROTEINS, ogbg-molhiv | GAT, GCN |
| [2502.02379](/papers/2502.02379/) | [No Metric to Rule Them All: Toward Principled Evaluations of...](/papers/2502.02379/) | 6 | 5 | 120 | MUTAG, NCI1, ogbg-molhiv | GAT, GCN, GIN |
| [2604.24293](/papers/2604.24293/) | [Latent-Hysteresis Graph ODEs: Modeling Coupled Topology-Feature Evolution via Continuous Phase...](/papers/2604.24293/) | 6 | 6 | 120 | Chameleon, Cora, ZINC | GraphGPS, Polynormer, SGFormer, Subgraphormer |
| [2402.10793](/papers/2402.10793/) | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | 6 | 0 | 100 | Peptides-func, Peptides-struct, ZINC | GCN, GIN, Graphormer |
| [2509.01254](/papers/2509.01254/) | [What Expressivity Theory Misses: Message Passing Complexity for GNNs](/papers/2509.01254/) | 5 | 5 | 197 | ZINC | CIN, GCN, GIN, GSN |
| [2508.19071](/papers/2508.19071/) | [Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks](/papers/2508.19071/) | 5 | 5 | 146 | Cora, Cornell, Texas, Wisconsin | + DIGL, BORF, FA |
| [2410.18676](/papers/2410.18676/) | [Homomorphism Counts as Structural Encodings for Graph Learning](/papers/2410.18676/) | 5 | 4 | 119 | MNIST, ZINC | CIN, GIN, GIN + RWSE, GPS |
| [2306.10759](/papers/2306.10759/) | [SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations](/papers/2306.10759/) | 5 | 0 | 50 | ogbn-arxiv, ogbn-proteins | GCN, MLP, NodeFormer, SIGN |
| [2503.09008](/papers/2503.09008/) | [City-Networks](/papers/2503.09008/) | 5 | 3 | 29 | D&D | ChebNet, GAT, GCN, MLP |
| [2505.23345](/papers/2505.23345/) | [Graph Positional Autoencoders as Self-supervised Learners](/papers/2505.23345/) | 5 | 5 | 25 | BACE, BBBP, ClinTox | GraphMAE, JOAO |
| [2412.03783](/papers/2412.03783/) | [Expressivity of Representation Learning on Continuous-Time Dynamic Graphs: An Information-Flow...](/papers/2412.03783/) | 5 | 5 | 14 | ogbl-wikikg2 | CTAN, DyRep, JODIE, TGAT |
| [2309.16014](/papers/2309.16014/) | [Graph-level Representation Learning with Joint-Embedding Predictive Architectures](/papers/2309.16014/) | 4 | 0 | 286 | Peptides-func, Peptides-struct | GCN, GatedGCN+RWSE |
| [2407.12419](/papers/2407.12419/) | [Dirac--Bianconi Graph Neural Networks -- Enabling Non-Diffusive Long-Range Graph Predictions](/papers/2407.12419/) | 4 | 0 | 284 | Peptides-struct | GCN, GINE, GatedGCN, GatedGCN+RWSE |
| [2407.12136](/papers/2407.12136/) | [Molecular Topological Profile (MOLTOP) - Simple and Strong Baseline for...](/papers/2407.12136/) | 4 | 1 | 243 | Peptides-func | GCN, GINE, GatedGCN, GatedGCN+RWSE |
| [2502.01122](/papers/2502.01122/) | [Learning Efficient Positional Encodings with Graph Neural Networks](/papers/2502.01122/) | 4 | 3 | 165 | Peptides-struct, ZINC | GCN, GIN, GPS, SignNet |
| [2310.01618](/papers/2310.01618/) | [Operator Learning Meets Numerical Analysis: Improving Neural Networks through Iterative...](/papers/2310.01618/) | 4 | 2 | 120 | CiteSeer, Cora | GAT, GCN |
| [2508.17630](/papers/2508.17630/) | [Quantum Graph Attention Network: A Novel Quantum Multi-Head Attention Mechanism...](/papers/2508.17630/) | 4 | 2 | 119 | PubMed, ogbn-arxiv, ogbn-proteins | GAT, GATv2 |
| [2406.06984](/papers/2406.06984/) | [On the Stability of Multiset and Graph Neural Networks](/papers/2406.06984/) | 4 | 0 | 76 | Peptides-func, Peptides-struct | GCN, GatedGCN |
| [2401.14580](/papers/2401.14580/) | [Design Your Own Universe: A Physics-Informed Agnostic Method for Enhancing...](/papers/2401.14580/) | 4 | 1 | 62 | ogbn-arxiv | GAT, GCN, GRAND, MLP |
| [2506.08618](/papers/2506.08618/) | [HSG-12M](/papers/2506.08618/) | 4 | 4 | 38 | D&D | GAT, GCN, GIN, GraphSAGE |
| [2512.15549](/papers/2512.15549/) | [Photonics-Enhanced Graph Convolutional Networks](/papers/2512.15549/) | 3 | 3 | 312 | Peptides-func, Peptides-struct | GCN, GCN+LapPE |
| [2508.10651](/papers/2508.10651/) | [Graph Learning via Logic-Based Weisfeiler--Leman Variants and Tabularization](/papers/2508.10651/) | 3 | 3 | 271 | ClinTox, Peptides-func | GCN, GIN |
| [2509.22259](/papers/2509.22259/) | [Rotary Position Encodings for Graphs](/papers/2509.22259/) | 3 | 2 | 99 | Cora | GAT, GCN, GraphSAGE |
| [2501.09821](/papers/2501.09821/) | [bnpool: Bayesian Nonparametric Pooling for Graphs](/papers/2501.09821/) | 3 | 3 | 70 | COLLAB, ENZYMES | DiffPool, SEP |
| [2407.04236](/papers/2407.04236/) | [Graph Pooling via Ricci Flow](/papers/2407.04236/) | 3 | 0 | 55 | COLLAB, ogbg-molhiv | DMON, MinCut |
| [2401.03350](/papers/2401.03350/) | [Accurate and Scalable Estimation of Epistemic Uncertainty for Graph Neural...](/papers/2401.03350/) | 2 | 0 | 86 | MNIST | GPS+LapPE, GatedGCN |
| [2502.07364](/papers/2502.07364/) | [Effects of Dropout on Performance in Long-range Graph Learning Tasks](/papers/2502.07364/) | 2 | 2 | 65 | Cora | None, SDRF |
| [2405.19121](/papers/2405.19121/) | [Spatio-Spectral Graph Neural Networks](/papers/2405.19121/) | 2 | 0 | 19 | CLUSTER | GCN, GatedGCN |
| [2506.05393](/papers/2506.05393/) | [Are Large Language Models Good Temporal Graph Learners?](/papers/2506.05393/) | 2 | 2 | 19 | ogbl-wikikg2 | GraphMixer, TGN |
| [2508.14097](/papers/2508.14097/) | [Non-Dissipative Graph Propagation for Non-Local Community Detection](/papers/2508.14097/) | 1 | 1 | 95 | Wisconsin | SUBLIME |
| [2603.00599](/papers/2603.00599/) | [Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger](/papers/2603.00599/) | 1 | 1 | 35 | Cora | HGNN |
| [2307.03393](/papers/2307.03393/) | [Exploring the Potential of Large Language Models (LLMs) in Learning...](/papers/2307.03393/) | 1 | 0 | 8 | ogbn-arxiv | GCN |
| [2405.11951](/papers/2405.11951/) | [Distinguished In Uniform: Self-Attention Vs. Virtual Nodes](/papers/2405.11951/) | 1 | 0 | 8 | ogbg-molpcba | GCN |

### Flagged Rows

| ArXiv | Dataset | Model | Actual | Paper | Rank Shift | Actual Source | Timing |
|---|---|---|---:|---:|---:|---|---|
| [2512.15549](/papers/2512.15549/) | Peptides-struct | GCN | 0.2421 | 0.4077 | 312 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2310.05174](/papers/2310.05174/) | Peptides-struct | GIN | 0.2429 | 0.3647 | 297 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.05174](/papers/2310.05174/) | Peptides-struct | GCN | 0.2421 | 0.3566 | 297 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2603.27529](/papers/2603.27529/) | Cora | DR | 0.9139 | 0.4435 | 292 | [Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks](/papers/2508.19071/) | already known (2025-08) |
| [2512.15549](/papers/2512.15549/) | Peptides-func | GCN | 0.7261 | 0.4396 | 287 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2306.05955](/papers/2306.05955/) | Peptides-struct | GIN | 0.2429 | 0.3547 | 286 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.01704](/papers/2310.01704/) | Peptides-struct | GIN | 0.2429 | 0.3547 | 286 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.03274](/papers/2310.03274/) | Peptides-struct | GIN | 0.2429 | 0.3547 | 286 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.07430](/papers/2310.07430/) | Peptides-struct | GIN | 0.2429 | 0.3547 | 286 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2402.08450](/papers/2402.08450/) | Peptides-struct | GIN | 0.2429 | 0.3547 | 286 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2402.08678](/papers/2402.08678/) | Peptides-struct | GIN | 0.2429 | 0.3547 | 286 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2502.00282](/papers/2502.00282/) | Peptides-struct | GIN | 0.2429 | 0.3547 | 286 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2309.16014](/papers/2309.16014/) | Peptides-struct | GCN | 0.2421 | 0.3500 | 286 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2206.08164](/papers/2206.08164/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 284 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2306.02866](/papers/2306.02866/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 284 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2306.03561](/papers/2306.03561/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 284 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2306.05955](/papers/2306.05955/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 284 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2308.11129](/papers/2308.11129/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 284 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2309.04941](/papers/2309.04941/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 284 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.01668](/papers/2310.01668/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 284 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.01704](/papers/2310.01704/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 284 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.02156](/papers/2310.02156/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 284 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.03274](/papers/2310.03274/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 284 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.07430](/papers/2310.07430/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 284 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.19285](/papers/2310.19285/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 284 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2311.01276](/papers/2311.01276/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 284 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2312.16560](/papers/2312.16560/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 284 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2401.17791](/papers/2401.17791/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 284 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2402.08450](/papers/2402.08450/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 284 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2402.08678](/papers/2402.08678/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 284 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2404.03380](/papers/2404.03380/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 284 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2405.02795](/papers/2405.02795/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 284 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2405.03481](/papers/2405.03481/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 284 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2405.13526](/papers/2405.13526/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 284 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2405.13806](/papers/2405.13806/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 284 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2406.12059](/papers/2406.12059/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 284 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2407.12419](/papers/2407.12419/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 284 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2409.19117](/papers/2409.19117/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 284 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2410.13798](/papers/2410.13798/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 284 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2410.23686](/papers/2410.23686/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 284 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2412.01519](/papers/2412.01519/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 284 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2502.00282](/papers/2502.00282/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 284 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2508.05070](/papers/2508.05070/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 284 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2510.02565](/papers/2510.02565/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 284 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2601.19094](/papers/2601.19094/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 284 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2604.06336](/papers/2604.06336/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 284 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2605.06462](/papers/2605.06462/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 284 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2310.01668](/papers/2310.01668/) | Peptides-struct | GIN | 0.2429 | 0.3493 | 279 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2508.10651](/papers/2508.10651/) | Peptides-func | GCN | 0.7261 | 0.5410 | 271 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2206.08164](/papers/2206.08164/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 269 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2306.02866](/papers/2306.02866/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 269 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2306.03561](/papers/2306.03561/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 269 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2306.05955](/papers/2306.05955/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 269 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2308.11129](/papers/2308.11129/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 269 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2309.04941](/papers/2309.04941/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 269 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.02156](/papers/2310.02156/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 269 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.03274](/papers/2310.03274/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 269 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.07430](/papers/2310.07430/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 269 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.19285](/papers/2310.19285/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 269 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2311.01276](/papers/2311.01276/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 269 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2311.04653](/papers/2311.04653/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 269 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2401.17791](/papers/2401.17791/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 269 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2402.08450](/papers/2402.08450/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 269 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2402.08678](/papers/2402.08678/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 269 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2404.03380](/papers/2404.03380/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 269 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2405.03481](/papers/2405.03481/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 269 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2405.13526](/papers/2405.13526/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 269 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2405.13806](/papers/2405.13806/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 269 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2406.12059](/papers/2406.12059/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 269 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2407.12419](/papers/2407.12419/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 269 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2409.19117](/papers/2409.19117/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 269 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2412.01519](/papers/2412.01519/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 269 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2502.00282](/papers/2502.00282/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 269 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2508.05070](/papers/2508.05070/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 269 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2510.02565](/papers/2510.02565/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 269 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2604.06336](/papers/2604.06336/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 269 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2605.06462](/papers/2605.06462/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 269 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2311.04653](/papers/2311.04653/) | Peptides-struct | GCN | 0.2421 | 0.3234 | 267 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2312.16560](/papers/2312.16560/) | Peptides-struct | GatedGCN | 0.2431 | 0.3357 | 261 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2405.02795](/papers/2405.02795/) | Peptides-struct | GatedGCN | 0.2431 | 0.3357 | 261 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2410.23686](/papers/2410.23686/) | Peptides-struct | GatedGCN | 0.2431 | 0.3357 | 261 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2412.07188](/papers/2412.07188/) | Cora | GCNII | 0.8893 | 0.6054 | 258 | [Revisiting Heterophily For Graph Neural Networks](/papers/2210.07606/) | already known (2022-10) |
| [2310.05174](/papers/2310.05174/) | Peptides-func | GCN | 0.7261 | 0.5831 | 255 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2412.07188](/papers/2412.07188/) | Cora | APPNP | 0.8800 | 0.5426 | 250 | [ParaFormer: A Generalized PageRank Graph Transformer for Graph...](/papers/2512.14619/) | published later (2025-12) |
| [2409.19117](/papers/2409.19117/) | Peptides-struct | GINE | 0.2473 | 0.6346 | 245 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2412.07188](/papers/2412.07188/) | Cora | GAT | 0.8825 | 0.6033 | 244 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2206.08164](/papers/2206.08164/) | Peptides-func | GCN | 0.7261 | 0.5930 | 243 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2306.02866](/papers/2306.02866/) | Peptides-func | GCN | 0.7261 | 0.5930 | 243 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2306.03561](/papers/2306.03561/) | Peptides-func | GCN | 0.7261 | 0.5930 | 243 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2308.11129](/papers/2308.11129/) | Peptides-func | GCN | 0.7261 | 0.5930 | 243 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2309.04941](/papers/2309.04941/) | Peptides-func | GCN | 0.7261 | 0.5930 | 243 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2309.16014](/papers/2309.16014/) | Peptides-func | GCN | 0.7261 | 0.5930 | 243 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.01668](/papers/2310.01668/) | Peptides-func | GCN | 0.7261 | 0.5930 | 243 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.02156](/papers/2310.02156/) | Peptides-func | GCN | 0.7261 | 0.5930 | 243 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.03274](/papers/2310.03274/) | Peptides-func | GCN | 0.7261 | 0.5930 | 243 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.07430](/papers/2310.07430/) | Peptides-func | GCN | 0.7261 | 0.5930 | 243 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.19285](/papers/2310.19285/) | Peptides-func | GCN | 0.7261 | 0.5930 | 243 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2311.01276](/papers/2311.01276/) | Peptides-func | GCN | 0.7261 | 0.5930 | 243 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2311.04653](/papers/2311.04653/) | Peptides-func | GCN | 0.7261 | 0.5930 | 243 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2312.16560](/papers/2312.16560/) | Peptides-func | GCN | 0.7261 | 0.5930 | 243 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2401.17791](/papers/2401.17791/) | Peptides-func | GCN | 0.7261 | 0.5930 | 243 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2402.08450](/papers/2402.08450/) | Peptides-func | GCN | 0.7261 | 0.5930 | 243 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2402.08678](/papers/2402.08678/) | Peptides-func | GCN | 0.7261 | 0.5930 | 243 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2404.03380](/papers/2404.03380/) | Peptides-func | GCN | 0.7261 | 0.5930 | 243 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2404.09774](/papers/2404.09774/) | Peptides-func | GCN | 0.7261 | 0.5930 | 243 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2405.02795](/papers/2405.02795/) | Peptides-func | GCN | 0.7261 | 0.5930 | 243 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2405.03481](/papers/2405.03481/) | Peptides-func | GCN | 0.7261 | 0.5930 | 243 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2405.13806](/papers/2405.13806/) | Peptides-func | GCN | 0.7261 | 0.5930 | 243 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2406.12059](/papers/2406.12059/) | Peptides-func | GCN | 0.7261 | 0.5930 | 243 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2407.02758](/papers/2407.02758/) | Peptides-func | GCN | 0.7261 | 0.5930 | 243 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2407.12136](/papers/2407.12136/) | Peptides-func | GCN | 0.7261 | 0.5930 | 243 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2409.19117](/papers/2409.19117/) | Peptides-func | GCN | 0.7261 | 0.5930 | 243 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2410.13798](/papers/2410.13798/) | Peptides-func | GCN | 0.7261 | 0.5930 | 243 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2412.01519](/papers/2412.01519/) | Peptides-func | GCN | 0.7261 | 0.5930 | 243 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2508.05070](/papers/2508.05070/) | Peptides-func | GCN | 0.7261 | 0.5930 | 243 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2510.02565](/papers/2510.02565/) | Peptides-func | GCN | 0.7261 | 0.5930 | 243 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2601.19094](/papers/2601.19094/) | Peptides-func | GCN | 0.7261 | 0.5930 | 243 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2604.06336](/papers/2604.06336/) | Peptides-func | GCN | 0.7261 | 0.5930 | 243 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2605.06462](/papers/2605.06462/) | Peptides-func | GCN | 0.7261 | 0.5930 | 243 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2310.03274](/papers/2310.03274/) | Peptides-func | GIN | 0.7059 | 0.5498 | 238 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.07430](/papers/2310.07430/) | Peptides-func | GIN | 0.7059 | 0.5498 | 238 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2402.08450](/papers/2402.08450/) | Peptides-func | GIN | 0.7059 | 0.5498 | 238 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2402.08678](/papers/2402.08678/) | Peptides-func | GIN | 0.7059 | 0.5498 | 238 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2406.18380](/papers/2406.18380/) | Peptides-func | GIN | 0.7059 | 0.5501 | 237 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2405.13806](/papers/2405.13806/) | Cora | GAT | 0.8825 | 0.6447 | 236 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2410.13798](/papers/2410.13798/) | Cora | GAT | 0.8825 | 0.6447 | 236 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2501.18739](/papers/2501.18739/) | Cora | GAT | 0.8825 | 0.6447 | 236 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2410.13798](/papers/2410.13798/) | Cora | GPRGNN | 0.8857 | 0.6712 | 231 | [GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers](/papers/2411.17296/) | published later (2024-11-26) |
| [2501.18739](/papers/2501.18739/) | Cora | GPRGNN | 0.8857 | 0.6712 | 231 | [GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers](/papers/2411.17296/) | already known (2024-11-26) |
| [2405.13806](/papers/2405.13806/) | Cora | APPNP | 0.8800 | 0.6516 | 227 | [ParaFormer: A Generalized PageRank Graph Transformer for Graph...](/papers/2512.14619/) | published later (2025-12) |
| [2410.13798](/papers/2410.13798/) | Cora | APPNP | 0.8800 | 0.6516 | 227 | [ParaFormer: A Generalized PageRank Graph Transformer for Graph...](/papers/2512.14619/) | published later (2025-12) |
| [2501.18739](/papers/2501.18739/) | Cora | APPNP | 0.8800 | 0.6516 | 227 | [ParaFormer: A Generalized PageRank Graph Transformer for Graph...](/papers/2512.14619/) | published later (2025-12) |
| [2310.01668](/papers/2310.01668/) | Peptides-func | GIN | 0.7059 | 0.5799 | 226 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2309.04082](/papers/2309.04082/) | Cora | MLP | 0.8709 | 0.5244 | 225 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2405.13806](/papers/2405.13806/) | Cora | GCN | 0.8778 | 0.6176 | 224 | [Revisiting Heterophily For Graph Neural Networks](/papers/2210.07606/) | already known (2022-10) |
| [2410.13798](/papers/2410.13798/) | Cora | GCN | 0.8778 | 0.6176 | 224 | [Revisiting Heterophily For Graph Neural Networks](/papers/2210.07606/) | already known (2022-10) |
| [2412.07188](/papers/2412.07188/) | Cora | GCN | 0.8778 | 0.6217 | 224 | [Revisiting Heterophily For Graph Neural Networks](/papers/2210.07606/) | already known (2022-10) |
| [2410.05593](/papers/2410.05593/) | Cora | MLP | 0.8709 | 0.5510 | 223 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2206.08164](/papers/2206.08164/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 221 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2306.02866](/papers/2306.02866/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 221 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2306.03561](/papers/2306.03561/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 221 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2308.11129](/papers/2308.11129/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 221 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2309.04941](/papers/2309.04941/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 221 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2310.02156](/papers/2310.02156/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 221 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2310.19285](/papers/2310.19285/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 221 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2311.01276](/papers/2311.01276/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 221 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2312.16560](/papers/2312.16560/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 221 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2401.17791](/papers/2401.17791/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 221 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2404.03380](/papers/2404.03380/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 221 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2405.02795](/papers/2405.02795/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 221 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2405.13526](/papers/2405.13526/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 221 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2405.13806](/papers/2405.13806/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 221 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2406.12059](/papers/2406.12059/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 221 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2407.12419](/papers/2407.12419/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 221 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2410.23686](/papers/2410.23686/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 221 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2412.01519](/papers/2412.01519/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 221 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2502.09365](/papers/2502.09365/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 221 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2508.05070](/papers/2508.05070/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 221 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2510.02565](/papers/2510.02565/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 221 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2604.06336](/papers/2604.06336/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 221 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | already known (2026-04) |
| [2605.06462](/papers/2605.06462/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 221 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | already known (2026-04) |
| [2310.05174](/papers/2310.05174/) | Peptides-func | GAT | 0.6924 | 0.4559 | 218 | [GEN: A Practical Alternative to Graph Transformers for...](/papers/2401.01233/) | published later (2024-01) |
| [2506.14098](/papers/2506.14098/) | Cora | MLP | 0.8709 | 0.5803 | 216 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2506.04765](/papers/2506.04765/) | ZINC | GPS | 0.0238 | 0.1968 | 216 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2602.02268](/papers/2602.02268/) | ZINC | GPS | 0.0238 | 0.1968 | 216 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2310.05174](/papers/2310.05174/) | Cora | MLP | 0.8709 | 0.5855 | 215 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2206.08164](/papers/2206.08164/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 215 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2306.02866](/papers/2306.02866/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 215 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2306.03561](/papers/2306.03561/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 215 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2307.07107](/papers/2307.07107/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 215 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2308.11129](/papers/2308.11129/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 215 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2309.04941](/papers/2309.04941/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 215 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.02156](/papers/2310.02156/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 215 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.03274](/papers/2310.03274/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 215 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.07430](/papers/2310.07430/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 215 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.19285](/papers/2310.19285/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 215 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2311.01276](/papers/2311.01276/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 215 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2311.04653](/papers/2311.04653/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 215 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2401.17791](/papers/2401.17791/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 215 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2402.08450](/papers/2402.08450/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 215 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2402.08678](/papers/2402.08678/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 215 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2404.03380](/papers/2404.03380/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 215 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2404.09774](/papers/2404.09774/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 215 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2405.03481](/papers/2405.03481/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 215 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2405.13806](/papers/2405.13806/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 215 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2406.12059](/papers/2406.12059/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 215 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2407.02758](/papers/2407.02758/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 215 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2407.12136](/papers/2407.12136/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 215 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2409.19117](/papers/2409.19117/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 215 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2412.01519](/papers/2412.01519/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 215 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2508.05070](/papers/2508.05070/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 215 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2510.02565](/papers/2510.02565/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 215 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2604.06336](/papers/2604.06336/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 215 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2605.06462](/papers/2605.06462/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 215 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2508.10651](/papers/2508.10651/) | Peptides-func | GIN | 0.7059 | 0.5940 | 212 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2410.05697](/papers/2410.05697/) | Cora | MLP | 0.8709 | 0.5941 | 211 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2210.07606](/papers/2210.07606/) | Cora | MixHop | 0.8761 | 0.6565 | 210 | [Algorithmic Graph Tasks](/papers/2312.16560/) | published later (2023-12) |
| [2306.05955](/papers/2306.05955/) | ZINC | AgentNet | 0.0400 | 0.2580 | 209 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2310.02156](/papers/2310.02156/) | Peptides-struct | GatedGCN+LapPE | 0.2466 | 0.3357 | 209 | [Non-backtracking Graph Neural Networks](/papers/2310.07430/) | already known (2023-10) |
| [2310.05174](/papers/2310.05174/) | Peptides-struct | GAT | 0.2488 | 0.4375 | 207 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2501.18739](/papers/2501.18739/) | Cora | SGFormer | 0.8810 | 0.6970 | 202 | [ParaFormer: A Generalized PageRank Graph Transformer for Graph...](/papers/2512.14619/) | published later (2025-12) |
| [2505.15405](/papers/2505.15405/) | ZINC | GIN | 0.0650 | 0.5700 | 200 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2509.01254](/papers/2509.01254/) | ZINC | GIN | 0.0650 | 0.5300 | 197 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2308.11129](/papers/2308.11129/) | ZINC | GIN | 0.0650 | 0.5260 | 197 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.19285](/papers/2310.19285/) | ZINC | GIN | 0.0650 | 0.5260 | 197 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2401.17791](/papers/2401.17791/) | ZINC | GIN | 0.0650 | 0.5260 | 197 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2406.03386](/papers/2406.03386/) | ZINC | GIN | 0.0650 | 0.5260 | 197 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2407.05649](/papers/2407.05649/) | ZINC | GIN | 0.0650 | 0.5260 | 197 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2409.19117](/papers/2409.19117/) | ZINC | GIN | 0.0650 | 0.5260 | 197 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2502.00282](/papers/2502.00282/) | ZINC | GIN | 0.0650 | 0.5260 | 197 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2502.09365](/papers/2502.09365/) | ZINC | GIN | 0.0650 | 0.5260 | 197 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2504.12588](/papers/2504.12588/) | ZINC | GIN | 0.0650 | 0.5260 | 197 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2508.05070](/papers/2508.05070/) | ZINC | GIN | 0.0650 | 0.5260 | 197 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2605.05689](/papers/2605.05689/) | ZINC | GIN | 0.0650 | 0.5260 | 197 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2410.13798](/papers/2410.13798/) | Cora | Nagphormer | 0.8820 | 0.7151 | 196 | [ParaFormer: A Generalized PageRank Graph Transformer for Graph...](/papers/2512.14619/) | published later (2025-12) |
| [2412.07188](/papers/2412.07188/) | Cora | SGC | 0.8660 | 0.6109 | 195 | [ParaFormer: A Generalized PageRank Graph Transformer for Graph...](/papers/2512.14619/) | published later (2025-12) |
| [2310.19285](/papers/2310.19285/) | ZINC | GRIT | 0.0230 | 0.1490 | 195 | [Enhancing Graph Neural Networks with Quantum Computed Encodings](/papers/2310.20519/) | already known (2023-10) |
| [2406.18380](/papers/2406.18380/) | ZINC | GIN | 0.0650 | 0.4131 | 194 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.01704](/papers/2310.01704/) | ZINC | GIN | 0.0650 | 0.4080 | 193 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2601.07419](/papers/2601.07419/) | Peptides-func | GIN | 0.7059 | 0.6070 | 192 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2310.05174](/papers/2310.05174/) | Peptides-func | GIN | 0.7059 | 0.6092 | 191 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2306.05955](/papers/2306.05955/) | ZINC | GIN | 0.0650 | 0.3870 | 189 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2312.01538](/papers/2312.01538/) | ZINC | GIN | 0.0650 | 0.3870 | 189 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.01668](/papers/2310.01668/) | Peptides-func | GAT | 0.6924 | 0.5800 | 189 | [GEN: A Practical Alternative to Graph Transformers for...](/papers/2401.01233/) | published later (2024-01) |
| [2312.16560](/papers/2312.16560/) | Peptides-func | GatedGCN | 0.7006 | 0.6069 | 184 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2405.02795](/papers/2405.02795/) | Peptides-func | GatedGCN | 0.7006 | 0.6069 | 184 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2308.11129](/papers/2308.11129/) | ZINC | PNA | 0.0573 | 0.1880 | 183 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | published later (2024-02) |
| [2310.19285](/papers/2310.19285/) | ZINC | PNA | 0.0573 | 0.1880 | 183 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | published later (2024-02) |
| [2312.01538](/papers/2312.01538/) | ZINC | PNA | 0.0573 | 0.1880 | 183 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | published later (2024-02) |
| [2401.17791](/papers/2401.17791/) | ZINC | PNA | 0.0573 | 0.1880 | 183 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | published later (2024-02) |
| [2404.03380](/papers/2404.03380/) | ZINC | PNA | 0.0573 | 0.1880 | 183 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2407.05649](/papers/2407.05649/) | ZINC | PNA | 0.0573 | 0.1880 | 183 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2410.09737](/papers/2410.09737/) | ZINC | PNA | 0.0573 | 0.1880 | 183 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2504.12588](/papers/2504.12588/) | ZINC | PNA | 0.0573 | 0.1880 | 183 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2508.05070](/papers/2508.05070/) | ZINC | PNA | 0.0573 | 0.1880 | 183 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2604.17324](/papers/2604.17324/) | ZINC | PNA | 0.0573 | 0.1880 | 183 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2605.05689](/papers/2605.05689/) | ZINC | PNA | 0.0573 | 0.1880 | 183 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2506.14098](/papers/2506.14098/) | ogbg-molhiv | GCN | 0.9681 | 0.6484 | 180 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2506.14098](/papers/2506.14098/) | ogbg-molhiv | MLP | 0.9685 | 0.6637 | 180 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2310.01668](/papers/2310.01668/) | Peptides-struct | GAT | 0.2488 | 0.3506 | 180 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2506.14098](/papers/2506.14098/) | ogbg-molhiv | GAT | 0.9682 | 0.6554 | 179 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2406.18380](/papers/2406.18380/) | CiteSeer | GIN | 0.7932 | 0.4798 | 177 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2506.14098](/papers/2506.14098/) | ogbg-molhiv | GIN | 0.9680 | 0.6686 | 177 | [No Metric to Rule Them All: Toward Principled...](/papers/2502.02379/) | already known (2025-02-04) |
| [2310.02156](/papers/2310.02156/) | Peptides-func | GatedGCN+LapPE | 0.6982 | 0.6069 | 177 | [Non-backtracking Graph Neural Networks](/papers/2310.07430/) | already known (2023-10) |
| [2506.04765](/papers/2506.04765/) | ZINC | Graphormer | 0.0250 | 0.1305 | 175 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | already known (2025-01-30) |
| [2602.02268](/papers/2602.02268/) | ZINC | Graphormer | 0.0250 | 0.1305 | 175 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | already known (2025-01-30) |
| [2410.13798](/papers/2410.13798/) | Cora | GraphGPS | 0.8387 | 0.5576 | 173 | [GEN: A Practical Alternative to Graph Transformers for...](/papers/2401.01233/) | already known (2024-01) |
| [2501.18739](/papers/2501.18739/) | Cora | GraphGPS | 0.8387 | 0.5576 | 173 | [GEN: A Practical Alternative to Graph Transformers for...](/papers/2401.01233/) | already known (2024-01) |
| [2601.07419](/papers/2601.07419/) | Cora | GCNII | 0.8893 | 0.7630 | 171 | [Revisiting Heterophily For Graph Neural Networks](/papers/2210.07606/) | already known (2022-10) |
| [2312.04234](/papers/2312.04234/) | ZINC | Graphormer | 0.0250 | 0.1240 | 171 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2410.05697](/papers/2410.05697/) | CiteSeer | MLP | 0.7939 | 0.5826 | 170 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2406.18380](/papers/2406.18380/) | PROTEINS | GAT | 0.7634 | 0.5978 | 170 | [HOPSE: Scalable Higher-Order Positional and Structural Encoder for...](/papers/2505.15405/) | published later (2025-05) |
| [2306.05955](/papers/2306.05955/) | ZINC | Graphormer | 0.0250 | 0.1220 | 169 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2310.01704](/papers/2310.01704/) | ZINC | Graphormer | 0.0250 | 0.1220 | 169 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2310.19285](/papers/2310.19285/) | ZINC | Graphormer | 0.0250 | 0.1220 | 169 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2312.01538](/papers/2312.01538/) | ZINC | Graphormer | 0.0250 | 0.1220 | 169 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2401.17791](/papers/2401.17791/) | ZINC | Graphormer | 0.0250 | 0.1220 | 169 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2404.03380](/papers/2404.03380/) | ZINC | Graphormer | 0.0250 | 0.1220 | 169 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2406.03386](/papers/2406.03386/) | ZINC | Graphormer | 0.0250 | 0.1220 | 169 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2407.05649](/papers/2407.05649/) | ZINC | Graphormer | 0.0250 | 0.1220 | 169 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2410.09737](/papers/2410.09737/) | ZINC | Graphormer | 0.0250 | 0.1220 | 169 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2502.09263](/papers/2502.09263/) | ZINC | Graphormer | 0.0250 | 0.1220 | 169 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | already known (2025-01-30) |
| [2502.09365](/papers/2502.09365/) | ZINC | Graphormer | 0.0250 | 0.1220 | 169 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | already known (2025-01-30) |
| [2504.12588](/papers/2504.12588/) | ZINC | Graphormer | 0.0250 | 0.1220 | 169 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | already known (2025-01-30) |
| [2604.17324](/papers/2604.17324/) | ZINC | Graphormer | 0.0250 | 0.1220 | 169 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | already known (2025-01-30) |
| [2410.05593](/papers/2410.05593/) | CiteSeer | MLP | 0.7939 | 0.5910 | 167 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2310.05174](/papers/2310.05174/) | CiteSeer | MLP | 0.7939 | 0.5952 | 167 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2406.18380](/papers/2406.18380/) | CiteSeer | GAT | 0.8052 | 0.6091 | 166 | [GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers](/papers/2411.17296/) | published later (2024-11-26) |
| [2502.01122](/papers/2502.01122/) | ZINC | GIN | 0.0650 | 0.2090 | 165 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2405.03481](/papers/2405.03481/) | ZINC | Graphormer | 0.0250 | 0.1200 | 165 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2601.07419](/papers/2601.07419/) | PROTEINS | GIN | 0.7620 | 0.6650 | 160 | [Probabilistic Graph Rewiring via Virtual Nodes](/papers/2405.17311/) | already known (2024-05) |
| [2310.19285](/papers/2310.19285/) | ZINC | GPS | 0.0238 | 0.1130 | 160 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | published later (2024-02) |
| [2310.05174](/papers/2310.05174/) | PROTEINS | GAT | 0.7634 | 0.6863 | 159 | [HOPSE: Scalable Higher-Order Positional and Structural Encoder for...](/papers/2505.15405/) | published later (2025-05) |
| [2406.18380](/papers/2406.18380/) | PROTEINS | GCN | 0.7600 | 0.6310 | 158 | [On the Stability of Multiset and Graph Neural...](/papers/2406.06984/) | already known (2024-06) |
| [2508.11390](/papers/2508.11390/) | PROTEINS | GAT | 0.7634 | 0.6900 | 157 | [HOPSE: Scalable Higher-Order Positional and Structural Encoder for...](/papers/2505.15405/) | already known (2025-05) |
| [2310.03274](/papers/2310.03274/) | ogbg-molhiv | GCN | 0.9681 | 0.7460 | 156 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2506.04765](/papers/2506.04765/) | ZINC | Exphormer | 0.0660 | 0.1905 | 156 | [SigGate-GT: Taming Over-Smoothing in Graph Transformers via Sigmoid-Gated...](/papers/2604.17324/) | published later (2026-04) |
| [2602.02268](/papers/2602.02268/) | ZINC | Exphormer | 0.0660 | 0.1905 | 156 | [SigGate-GT: Taming Over-Smoothing in Graph Transformers via Sigmoid-Gated...](/papers/2604.17324/) | published later (2026-04) |
| [2506.14098](/papers/2506.14098/) | Cora | GAT | 0.8825 | 0.7624 | 156 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2505.15405](/papers/2505.15405/) | ZINC | GCN | 0.0760 | 0.6200 | 155 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2506.04765](/papers/2506.04765/) | ZINC | GCN | 0.0760 | 0.6090 | 155 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2602.02268](/papers/2602.02268/) | ZINC | GCN | 0.0760 | 0.6090 | 155 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2406.18380](/papers/2406.18380/) | Cora | GAT | 0.8825 | 0.7651 | 154 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2312.16560](/papers/2312.16560/) | Peptides-struct | GRED | 0.2455 | 0.2584 | 154 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2410.03424](/papers/2410.03424/) | PROTEINS | GCN | 0.7600 | 0.6665 | 153 | [On the Stability of Multiset and Graph Neural...](/papers/2406.06984/) | already known (2024-06) |
| [2310.05174](/papers/2310.05174/) | PROTEINS | GIN | 0.7620 | 0.6907 | 153 | [Probabilistic Graph Rewiring via Virtual Nodes](/papers/2405.17311/) | published later (2024-05) |
| [2412.07188](/papers/2412.07188/) | Cora | GATv2 | 0.8350 | 0.6305 | 151 | [Rotary Position Encodings for Graphs](/papers/2509.22259/) | published later (2025-09) |
| [2412.07188](/papers/2412.07188/) | Cora | SAGE | 0.8360 | 0.6397 | 151 | [Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in...](/papers/2603.27529/) | published later (2026-03) |
| [2402.08450](/papers/2402.08450/) | ZINC | GIN | 0.0650 | 0.1630 | 151 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2406.09291](/papers/2406.09291/) | ZINC | GIN | 0.0650 | 0.1630 | 151 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2410.09737](/papers/2410.09737/) | ZINC | GIN | 0.0650 | 0.1630 | 151 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2501.03113](/papers/2501.03113/) | ZINC | GIN | 0.0650 | 0.1630 | 151 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.05174](/papers/2310.05174/) | PROTEINS | GCN | 0.7600 | 0.6752 | 151 | [On the Stability of Multiset and Graph Neural...](/papers/2406.06984/) | published later (2024-06) |
| [2210.07606](/papers/2210.07606/) | Cora | GAT | 0.8825 | 0.7670 | 150 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2502.01122](/papers/2502.01122/) | ZINC | GCN | 0.0760 | 0.4690 | 149 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2406.09291](/papers/2406.09291/) | ZINC | NGNN | 0.0290 | 0.1110 | 149 | [Graph as Point Set](/papers/2405.02795/) | already known (2024-05-05) |
| [2410.05499](/papers/2410.05499/) | PROTEINS | GIN | 0.7620 | 0.6970 | 149 | [Probabilistic Graph Rewiring via Virtual Nodes](/papers/2405.17311/) | already known (2024-05) |
| [2306.05955](/papers/2306.05955/) | ZINC | GatedGCN | 0.0770 | 0.4350 | 148 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2506.14098](/papers/2506.14098/) | PubMed | MLP | 0.9476 | 0.6866 | 148 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2508.11390](/papers/2508.11390/) | PROTEINS | GCN | 0.7600 | 0.6900 | 147 | [On the Stability of Multiset and Graph Neural...](/papers/2406.06984/) | already known (2024-06) |
| [2506.04765](/papers/2506.04765/) | ZINC | GAT | 0.0776 | 0.6225 | 146 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2602.02268](/papers/2602.02268/) | ZINC | GAT | 0.0776 | 0.6225 | 146 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2505.15405](/papers/2505.15405/) | ZINC | GAT | 0.0776 | 0.6100 | 146 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2508.19071](/papers/2508.19071/) | Cora | FA | 0.8165 | 0.2986 | 146 | [Effects of Dropout on Performance in Long-range Graph...](/papers/2502.07364/) | already known (2025-02) |
| [2410.05593](/papers/2410.05593/) | PubMed | MLP | 0.9476 | 0.7140 | 146 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2210.07606](/papers/2210.07606/) | CiteSeer | MixHop | 0.7626 | 0.4952 | 145 | [Algorithmic Graph Tasks](/papers/2312.16560/) | published later (2023-12) |
| [2412.07188](/papers/2412.07188/) | Cora | GIN | 0.8303 | 0.6098 | 145 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2307.07107](/papers/2307.07107/) | Peptides-func | R-GCN (RWSE) | 0.6860 | 0.6067 | 145 | [Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based...](/papers/2501.03113/) | published later (2025-01) |
| [2510.02565](/papers/2510.02565/) | Peptides-func | R-GCN (RWSE) | 0.6860 | 0.6067 | 145 | [Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based...](/papers/2501.03113/) | already known (2025-01) |
| [2506.14098](/papers/2506.14098/) | PubMed | GIN | 0.9140 | 0.6951 | 144 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2506.14098](/papers/2506.14098/) | Cora | GCN | 0.8778 | 0.7565 | 143 | [Revisiting Heterophily For Graph Neural Networks](/papers/2210.07606/) | already known (2022-10) |
| [2410.03424](/papers/2410.03424/) | PROTEINS | GIN | 0.7620 | 0.7031 | 143 | [Probabilistic Graph Rewiring via Virtual Nodes](/papers/2405.17311/) | already known (2024-05) |
| [2412.07188](/papers/2412.07188/) | Cora | FA | 0.8165 | 0.5488 | 142 | [Effects of Dropout on Performance in Long-range Graph...](/papers/2502.07364/) | published later (2025-02) |
| [2410.03424](/papers/2410.03424/) | ogbg-molhiv | GCN | 0.9681 | 0.7566 | 142 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2410.05697](/papers/2410.05697/) | PubMed | MLP | 0.9476 | 0.7383 | 142 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2509.01254](/papers/2509.01254/) | ZINC | GCN | 0.0760 | 0.3700 | 141 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2308.11129](/papers/2308.11129/) | ZINC | GCN | 0.0760 | 0.3670 | 141 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.01704](/papers/2310.01704/) | ZINC | GCN | 0.0760 | 0.3670 | 141 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2311.04653](/papers/2311.04653/) | ZINC | GCN | 0.0760 | 0.3670 | 141 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2401.01233](/papers/2401.01233/) | ZINC | GCN | 0.0760 | 0.3670 | 141 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2401.17791](/papers/2401.17791/) | ZINC | GCN | 0.0760 | 0.3670 | 141 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2404.03380](/papers/2404.03380/) | ZINC | GCN | 0.0760 | 0.3670 | 141 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2406.03386](/papers/2406.03386/) | ZINC | GCN | 0.0760 | 0.3670 | 141 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2407.05649](/papers/2407.05649/) | ZINC | GCN | 0.0760 | 0.3670 | 141 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2502.00282](/papers/2502.00282/) | ZINC | GCN | 0.0760 | 0.3670 | 141 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2502.09365](/papers/2502.09365/) | ZINC | GCN | 0.0760 | 0.3670 | 141 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2504.12588](/papers/2504.12588/) | ZINC | GCN | 0.0760 | 0.3670 | 141 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2508.05070](/papers/2508.05070/) | ZINC | GCN | 0.0760 | 0.3670 | 141 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2604.17324](/papers/2604.17324/) | ZINC | GCN | 0.0760 | 0.3670 | 141 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2605.05689](/papers/2605.05689/) | ZINC | GCN | 0.0760 | 0.3670 | 141 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2306.05955](/papers/2306.05955/) | ogbg-molhiv | GIN | 0.9680 | 0.7558 | 141 | [No Metric to Rule Them All: Toward Principled...](/papers/2502.02379/) | published later (2025-02-04) |
| [2402.08450](/papers/2402.08450/) | ogbg-molhiv | GIN | 0.9680 | 0.7558 | 141 | [No Metric to Rule Them All: Toward Principled...](/papers/2502.02379/) | published later (2025-02-04) |
| [2405.13526](/papers/2405.13526/) | ogbg-molhiv | GIN | 0.9680 | 0.7558 | 141 | [No Metric to Rule Them All: Toward Principled...](/papers/2502.02379/) | published later (2025-02-04) |
| [2501.03113](/papers/2501.03113/) | ogbg-molhiv | GIN | 0.9680 | 0.7558 | 141 | [No Metric to Rule Them All: Toward Principled...](/papers/2502.02379/) | published later (2025-02-04) |
| [2404.09774](/papers/2404.09774/) | ogbg-molhiv | GCN | 0.9681 | 0.7599 | 139 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2402.08450](/papers/2402.08450/) | ZINC | GNN (a) | 0.0340 | 0.1050 | 139 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2406.18380](/papers/2406.18380/) | PROTEINS | GIN | 0.7620 | 0.7066 | 139 | [Probabilistic Graph Rewiring via Virtual Nodes](/papers/2405.17311/) | already known (2024-05) |
| [2306.05955](/papers/2306.05955/) | PROTEINS | GAT | 0.7634 | 0.7090 | 139 | [HOPSE: Scalable Higher-Order Positional and Structural Encoder for...](/papers/2505.15405/) | published later (2025-05) |
| [2206.08164](/papers/2206.08164/) | Peptides-func | GINE | 0.6621 | 0.5498 | 137 | [Where Did the Gap Go? Reassessing the Long-Range...](/papers/2309.00367/) | published later (2023-09) |
| [2306.02866](/papers/2306.02866/) | Peptides-func | GINE | 0.6621 | 0.5498 | 137 | [Where Did the Gap Go? Reassessing the Long-Range...](/papers/2309.00367/) | published later (2023-09) |
| [2306.03561](/papers/2306.03561/) | Peptides-func | GINE | 0.6621 | 0.5498 | 137 | [Where Did the Gap Go? Reassessing the Long-Range...](/papers/2309.00367/) | published later (2023-09) |
| [2307.07107](/papers/2307.07107/) | Peptides-func | GINE | 0.6621 | 0.5498 | 137 | [Where Did the Gap Go? Reassessing the Long-Range...](/papers/2309.00367/) | published later (2023-09) |
| [2308.11129](/papers/2308.11129/) | Peptides-func | GINE | 0.6621 | 0.5498 | 137 | [Where Did the Gap Go? Reassessing the Long-Range...](/papers/2309.00367/) | published later (2023-09) |
| [2309.04941](/papers/2309.04941/) | Peptides-func | GINE | 0.6621 | 0.5498 | 137 | [Where Did the Gap Go? Reassessing the Long-Range...](/papers/2309.00367/) | already known (2023-09) |
| [2310.02156](/papers/2310.02156/) | Peptides-func | GINE | 0.6621 | 0.5498 | 137 | [Where Did the Gap Go? Reassessing the Long-Range...](/papers/2309.00367/) | already known (2023-09) |
| [2310.19285](/papers/2310.19285/) | Peptides-func | GINE | 0.6621 | 0.5498 | 137 | [Where Did the Gap Go? Reassessing the Long-Range...](/papers/2309.00367/) | already known (2023-09) |
| [2311.01276](/papers/2311.01276/) | Peptides-func | GINE | 0.6621 | 0.5498 | 137 | [Where Did the Gap Go? Reassessing the Long-Range...](/papers/2309.00367/) | already known (2023-09) |
| [2312.16560](/papers/2312.16560/) | Peptides-func | GINE | 0.6621 | 0.5498 | 137 | [Where Did the Gap Go? Reassessing the Long-Range...](/papers/2309.00367/) | already known (2023-09) |
| [2401.17791](/papers/2401.17791/) | Peptides-func | GINE | 0.6621 | 0.5498 | 137 | [Where Did the Gap Go? Reassessing the Long-Range...](/papers/2309.00367/) | already known (2023-09) |
| [2404.03380](/papers/2404.03380/) | Peptides-func | GINE | 0.6621 | 0.5498 | 137 | [Where Did the Gap Go? Reassessing the Long-Range...](/papers/2309.00367/) | already known (2023-09) |
| [2404.09774](/papers/2404.09774/) | Peptides-func | GINE | 0.6621 | 0.5498 | 137 | [Where Did the Gap Go? Reassessing the Long-Range...](/papers/2309.00367/) | already known (2023-09) |
| [2405.02795](/papers/2405.02795/) | Peptides-func | GINE | 0.6621 | 0.5498 | 137 | [Where Did the Gap Go? Reassessing the Long-Range...](/papers/2309.00367/) | already known (2023-09) |
| [2405.13806](/papers/2405.13806/) | Peptides-func | GINE | 0.6621 | 0.5498 | 137 | [Where Did the Gap Go? Reassessing the Long-Range...](/papers/2309.00367/) | already known (2023-09) |
| [2406.12059](/papers/2406.12059/) | Peptides-func | GINE | 0.6621 | 0.5498 | 137 | [Where Did the Gap Go? Reassessing the Long-Range...](/papers/2309.00367/) | already known (2023-09) |
| [2407.02758](/papers/2407.02758/) | Peptides-func | GINE | 0.6621 | 0.5498 | 137 | [Where Did the Gap Go? Reassessing the Long-Range...](/papers/2309.00367/) | already known (2023-09) |
| [2407.12136](/papers/2407.12136/) | Peptides-func | GINE | 0.6621 | 0.5498 | 137 | [Where Did the Gap Go? Reassessing the Long-Range...](/papers/2309.00367/) | already known (2023-09) |
| [2409.19117](/papers/2409.19117/) | Peptides-func | GINE | 0.6621 | 0.5498 | 137 | [Where Did the Gap Go? Reassessing the Long-Range...](/papers/2309.00367/) | already known (2023-09) |
| [2412.01519](/papers/2412.01519/) | Peptides-func | GINE | 0.6621 | 0.5498 | 137 | [Where Did the Gap Go? Reassessing the Long-Range...](/papers/2309.00367/) | already known (2023-09) |
| [2502.09365](/papers/2502.09365/) | Peptides-func | GINE | 0.6621 | 0.5498 | 137 | [Where Did the Gap Go? Reassessing the Long-Range...](/papers/2309.00367/) | already known (2023-09) |
| [2508.05070](/papers/2508.05070/) | Peptides-func | GINE | 0.6621 | 0.5498 | 137 | [Where Did the Gap Go? Reassessing the Long-Range...](/papers/2309.00367/) | already known (2023-09) |
| [2510.02565](/papers/2510.02565/) | Peptides-func | GINE | 0.6621 | 0.5498 | 137 | [Where Did the Gap Go? Reassessing the Long-Range...](/papers/2309.00367/) | already known (2023-09) |
| [2604.06336](/papers/2604.06336/) | Peptides-func | GINE | 0.6621 | 0.5498 | 137 | [Where Did the Gap Go? Reassessing the Long-Range...](/papers/2309.00367/) | already known (2023-09) |
| [2605.06462](/papers/2605.06462/) | Peptides-func | GINE | 0.6621 | 0.5498 | 137 | [Where Did the Gap Go? Reassessing the Long-Range...](/papers/2309.00367/) | already known (2023-09) |
| [2406.09291](/papers/2406.09291/) | ZINC | DSS-GNN | 0.0290 | 0.1020 | 137 | [Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via...](/papers/2402.08450/) | already known (2024-02) |
| [2506.04765](/papers/2506.04765/) | Texas | APPNP | 0.9118 | 0.5405 | 136 | [Revisiting Heterophily For Graph Neural Networks](/papers/2210.07606/) | already known (2022-10) |
| [2602.02268](/papers/2602.02268/) | Texas | APPNP | 0.9118 | 0.5405 | 136 | [Revisiting Heterophily For Graph Neural Networks](/papers/2210.07606/) | already known (2022-10) |
| [2406.18380](/papers/2406.18380/) | MUTAG | GCN | 0.9010 | 0.5995 | 136 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2410.13798](/papers/2410.13798/) | Cora | SAN | 0.8191 | 0.5901 | 136 | [Hybrid Focal and Full-Range Attention Based Graph Transformers](/papers/2311.04653/) | already known (2023-11) |
| [2501.18739](/papers/2501.18739/) | Cora | SAN | 0.8191 | 0.5901 | 136 | [Hybrid Focal and Full-Range Attention Based Graph Transformers](/papers/2311.04653/) | already known (2023-11) |
| [2306.05955](/papers/2306.05955/) | ZINC | ESAN | 0.0290 | 0.1020 | 136 | [Graph as Point Set](/papers/2405.02795/) | published later (2024-05-05) |
| [2407.18480](/papers/2407.18480/) | Texas | APPNP | 0.9118 | 0.5510 | 135 | [Revisiting Heterophily For Graph Neural Networks](/papers/2210.07606/) | already known (2022-10) |
| [2506.04765](/papers/2506.04765/) | Wisconsin | APPNP | 0.9010 | 0.4641 | 134 | [When Graph Neural Networks Meet Dynamic Mode Decomposition](/papers/2410.05593/) | already known (2024-10) |
| [2602.02268](/papers/2602.02268/) | Wisconsin | APPNP | 0.9010 | 0.4641 | 134 | [When Graph Neural Networks Meet Dynamic Mode Decomposition](/papers/2410.05593/) | already known (2024-10) |
| [2306.03561](/papers/2306.03561/) | ogbg-molhiv | GCN | 0.9681 | 0.7606 | 134 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2306.05955](/papers/2306.05955/) | ogbg-molhiv | GCN | 0.9681 | 0.7606 | 134 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2402.08450](/papers/2402.08450/) | ogbg-molhiv | GCN | 0.9681 | 0.7606 | 134 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2405.13526](/papers/2405.13526/) | ogbg-molhiv | GCN | 0.9681 | 0.7606 | 134 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2501.03113](/papers/2501.03113/) | ogbg-molhiv | GCN | 0.9681 | 0.7606 | 134 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2604.17324](/papers/2604.17324/) | ogbg-molhiv | GCN | 0.9681 | 0.7606 | 134 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | already known (2025-11) |
| [2506.14098](/papers/2506.14098/) | PubMed | GAT | 0.9201 | 0.7486 | 134 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2601.07419](/papers/2601.07419/) | Cora | GCN | 0.8778 | 0.7710 | 133 | [Revisiting Heterophily For Graph Neural Networks](/papers/2210.07606/) | already known (2022-10) |
| [2210.07606](/papers/2210.07606/) | Cora | GPRGNN | 0.8857 | 0.7951 | 133 | [GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers](/papers/2411.17296/) | published later (2024-11-26) |
| [2601.07419](/papers/2601.07419/) | PROTEINS | GraphSAGE | 0.7590 | 0.7010 | 133 | [On the Stability of Multiset and Graph Neural...](/papers/2406.06984/) | already known (2024-06) |
| [2410.05499](/papers/2410.05499/) | PROTEINS | GCN | 0.7600 | 0.7060 | 133 | [On the Stability of Multiset and Graph Neural...](/papers/2406.06984/) | already known (2024-06) |
| [2306.05955](/papers/2306.05955/) | ZINC | GAT | 0.0776 | 0.3840 | 132 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | published later (2024-02) |
| [2310.01704](/papers/2310.01704/) | ZINC | GAT | 0.0776 | 0.3840 | 132 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | published later (2024-02) |
| [2310.19285](/papers/2310.19285/) | ZINC | GAT | 0.0776 | 0.3840 | 132 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | published later (2024-02) |
| [2312.01538](/papers/2312.01538/) | ZINC | GAT | 0.0776 | 0.3840 | 132 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | published later (2024-02) |
| [2401.01233](/papers/2401.01233/) | ZINC | GAT | 0.0776 | 0.3840 | 132 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | published later (2024-02) |
| [2401.17791](/papers/2401.17791/) | ZINC | GAT | 0.0776 | 0.3840 | 132 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | published later (2024-02) |
| [2404.03380](/papers/2404.03380/) | ZINC | GAT | 0.0776 | 0.3840 | 132 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2406.03386](/papers/2406.03386/) | ZINC | GAT | 0.0776 | 0.3840 | 132 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2407.05649](/papers/2407.05649/) | ZINC | GAT | 0.0776 | 0.3840 | 132 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2409.19117](/papers/2409.19117/) | ZINC | GAT | 0.0776 | 0.3840 | 132 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2502.00282](/papers/2502.00282/) | ZINC | GAT | 0.0776 | 0.3840 | 132 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2502.09365](/papers/2502.09365/) | ZINC | GAT | 0.0776 | 0.3840 | 132 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2504.12588](/papers/2504.12588/) | ZINC | GAT | 0.0776 | 0.3840 | 132 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2508.05070](/papers/2508.05070/) | ZINC | GAT | 0.0776 | 0.3840 | 132 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2605.05689](/papers/2605.05689/) | ZINC | GAT | 0.0776 | 0.3840 | 132 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2406.09291](/papers/2406.09291/) | ZINC | GCN | 0.0760 | 0.3210 | 132 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2501.03113](/papers/2501.03113/) | ZINC | GCN | 0.0760 | 0.3210 | 132 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.03274](/papers/2310.03274/) | ogbg-molhiv | GIN | 0.9680 | 0.7610 | 132 | [No Metric to Rule Them All: Toward Principled...](/papers/2502.02379/) | published later (2025-02-04) |
| [2310.05174](/papers/2310.05174/) | Cora | NodeFormer | 0.8870 | 0.8028 | 132 | [ParaFormer: A Generalized PageRank Graph Transformer for Graph...](/papers/2512.14619/) | published later (2025-12) |
| [2506.04765](/papers/2506.04765/) | Cornell | APPNP | 0.9180 | 0.4414 | 131 | [Revisiting Heterophily For Graph Neural Networks](/papers/2210.07606/) | already known (2022-10) |
| [2602.02268](/papers/2602.02268/) | Cornell | APPNP | 0.9180 | 0.4414 | 131 | [Revisiting Heterophily For Graph Neural Networks](/papers/2210.07606/) | already known (2022-10) |
| [2312.16560](/papers/2312.16560/) | Cora | MLP | 0.8709 | 0.7475 | 131 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2501.18739](/papers/2501.18739/) | Cora | NodeFormer | 0.8870 | 0.8078 | 131 | [ParaFormer: A Generalized PageRank Graph Transformer for Graph...](/papers/2512.14619/) | published later (2025-12) |
| [2210.07606](/papers/2210.07606/) | CiteSeer | GAT | 0.8052 | 0.6720 | 130 | [GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers](/papers/2411.17296/) | published later (2024-11-26) |
| [2603.27529](/papers/2603.27529/) | CiteSeer | GAT | 0.8052 | 0.6794 | 129 | [GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers](/papers/2411.17296/) | already known (2024-11-26) |
| [2501.03113](/papers/2501.03113/) | Peptides-struct | GCN | 0.2421 | 0.2505 | 129 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2603.27529](/papers/2603.27529/) | CiteSeer | GCN | 0.8139 | 0.6910 | 128 | [Revisiting Heterophily For Graph Neural Networks](/papers/2210.07606/) | already known (2022-10) |
| [2502.01122](/papers/2502.01122/) | ZINC | SignNet | 0.0240 | 0.0853 | 128 | [Graph as Point Set](/papers/2405.02795/) | already known (2024-05-05) |
| [2308.11129](/papers/2308.11129/) | ZINC | SAT | 0.0360 | 0.0940 | 128 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2502.09263](/papers/2502.09263/) | ZINC | SAT | 0.0360 | 0.0940 | 128 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | already known (2025-01-30) |
| [2407.18480](/papers/2407.18480/) | MUTAG | GCN | 0.9010 | 0.6950 | 127 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2505.15405](/papers/2505.15405/) | MUTAG | GCN | 0.9010 | 0.6979 | 127 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2603.27529](/papers/2603.27529/) | PROTEINS | FOSR | 0.7510 | 0.6670 | 127 | [Probabilistic Graph Rewiring via Virtual Nodes](/papers/2405.17311/) | already known (2024-05) |
| [2406.09291](/papers/2406.09291/) | ZINC | GNN (a) | 0.0340 | 0.0910 | 127 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2512.14619](/papers/2512.14619/) | Cora | MLP | 0.8709 | 0.7570 | 126 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | already known (2025-11) |
| [2410.05697](/papers/2410.05697/) | Cora | GPRGNN | 0.8857 | 0.8103 | 126 | [GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers](/papers/2411.17296/) | published later (2024-11-26) |
| [2401.01233](/papers/2401.01233/) | ZINC | Exphormer | 0.0660 | 0.1320 | 126 | [SigGate-GT: Taming Over-Smoothing in Graph Transformers via Sigmoid-Gated...](/papers/2604.17324/) | published later (2026-04) |
| [2308.11129](/papers/2308.11129/) | ZINC | GatedGCN | 0.0770 | 0.2820 | 125 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.20519](/papers/2310.20519/) | ZINC | GatedGCN | 0.0770 | 0.2820 | 125 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2312.01538](/papers/2312.01538/) | ZINC | GatedGCN | 0.0770 | 0.2820 | 125 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2401.17791](/papers/2401.17791/) | ZINC | GatedGCN | 0.0770 | 0.2820 | 125 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2404.03380](/papers/2404.03380/) | ZINC | GatedGCN | 0.0770 | 0.2820 | 125 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2406.03386](/papers/2406.03386/) | ZINC | GatedGCN | 0.0770 | 0.2820 | 125 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2407.05649](/papers/2407.05649/) | ZINC | GatedGCN | 0.0770 | 0.2820 | 125 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2409.19117](/papers/2409.19117/) | ZINC | GatedGCN | 0.0770 | 0.2820 | 125 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2502.09365](/papers/2502.09365/) | ZINC | GatedGCN | 0.0770 | 0.2820 | 125 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2504.12588](/papers/2504.12588/) | ZINC | GatedGCN | 0.0770 | 0.2820 | 125 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2508.05070](/papers/2508.05070/) | ZINC | GatedGCN | 0.0770 | 0.2820 | 125 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2604.17324](/papers/2604.17324/) | ZINC | GatedGCN | 0.0770 | 0.2820 | 125 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2605.05689](/papers/2605.05689/) | ZINC | GatedGCN | 0.0770 | 0.2820 | 125 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2306.05955](/papers/2306.05955/) | ZINC | GCN | 0.0760 | 0.2780 | 125 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2312.01538](/papers/2312.01538/) | ZINC | GCN | 0.0760 | 0.2780 | 125 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2407.18480](/papers/2407.18480/) | PROTEINS | GIN | 0.7620 | 0.7146 | 125 | [Probabilistic Graph Rewiring via Virtual Nodes](/papers/2405.17311/) | already known (2024-05) |
| [2506.14098](/papers/2506.14098/) | PubMed | GCN | 0.9224 | 0.7561 | 124 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2407.18480](/papers/2407.18480/) | Wisconsin | APPNP | 0.9010 | 0.5459 | 123 | [When Graph Neural Networks Meet Dynamic Mode Decomposition](/papers/2410.05593/) | published later (2024-10) |
| [2210.07606](/papers/2210.07606/) | CiteSeer | GPRGNN | 0.8012 | 0.6763 | 123 | [GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers](/papers/2411.17296/) | published later (2024-11-26) |
| [2501.03113](/papers/2501.03113/) | Peptides-func | GIN | 0.7059 | 0.6555 | 122 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2501.18739](/papers/2501.18739/) | Cora | GOAT | 0.8326 | 0.6855 | 121 | [GEN: A Practical Alternative to Graph Transformers for...](/papers/2401.01233/) | already known (2024-01) |
| [2410.13798](/papers/2410.13798/) | Cora | Exphormer | 0.8329 | 0.6909 | 121 | [GEN: A Practical Alternative to Graph Transformers for...](/papers/2401.01233/) | already known (2024-01) |
| [2401.17791](/papers/2401.17791/) | ZINC | Graphormer-URPE | 0.0280 | 0.0860 | 121 | [Enhancing Graph Neural Networks with Quantum Computed Encodings](/papers/2310.20519/) | already known (2023-10) |
| [2407.05649](/papers/2407.05649/) | ZINC | Graphormer-URPE | 0.0280 | 0.0860 | 121 | [Enhancing Graph Neural Networks with Quantum Computed Encodings](/papers/2310.20519/) | already known (2023-10) |
| [2502.09263](/papers/2502.09263/) | ZINC | Graphormer-URPE | 0.0280 | 0.0860 | 121 | [Enhancing Graph Neural Networks with Quantum Computed Encodings](/papers/2310.20519/) | already known (2023-10) |
| [2502.02379](/papers/2502.02379/) | MUTAG | GCN | 0.9010 | 0.7180 | 120 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2210.07606](/papers/2210.07606/) | Cora | APPNP | 0.8800 | 0.7941 | 120 | [ParaFormer: A Generalized PageRank Graph Transformer for Graph...](/papers/2512.14619/) | published later (2025-12) |
| [2310.01618](/papers/2310.01618/) | Cora | GAT | 0.8825 | 0.8040 | 120 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2410.05697](/papers/2410.05697/) | Cora | GAT | 0.8825 | 0.8110 | 120 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2308.11129](/papers/2308.11129/) | Cora | NodeFormer | 0.8870 | 0.8220 | 120 | [ParaFormer: A Generalized PageRank Graph Transformer for Graph...](/papers/2512.14619/) | published later (2025-12) |
| [2311.04653](/papers/2311.04653/) | ZINC | SUN | 0.0240 | 0.0840 | 120 | [Graph as Point Set](/papers/2405.02795/) | published later (2024-05-05) |
| [2604.24293](/papers/2604.24293/) | ZINC | Subgraphormer | 0.0230 | 0.0820 | 120 | [Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via...](/papers/2402.08450/) | already known (2024-02) |
| [2506.04765](/papers/2506.04765/) | Cornell | GCN | 0.8246 | 0.3243 | 119 | [Revisiting Heterophily For Graph Neural Networks](/papers/2210.07606/) | already known (2022-10) |
| [2602.02268](/papers/2602.02268/) | Cornell | GCN | 0.8246 | 0.3243 | 119 | [Revisiting Heterophily For Graph Neural Networks](/papers/2210.07606/) | already known (2022-10) |
| [2509.06777](/papers/2509.06777/) | MUTAG | GCN + SDRF | 0.8950 | 0.7105 | 119 | [Position: Don't be Afraid of Over-Smoothing And Over-Squashing](/papers/2601.07419/) | published later (2026-01) |
| [2508.17630](/papers/2508.17630/) | PubMed | GAT | 0.9201 | 0.7810 | 119 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2310.01618](/papers/2310.01618/) | CiteSeer | GAT | 0.8052 | 0.6990 | 119 | [GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers](/papers/2411.17296/) | published later (2024-11-26) |
| [2206.08164](/papers/2206.08164/) | Peptides-struct | GatedGCN+RWSE | 0.2529 | 0.3357 | 119 | [Range-aware Positional Encoding via High-order Pretraining: Theory and...](/papers/2409.19117/) | published later (2024-09) |
| [2306.02866](/papers/2306.02866/) | Peptides-struct | GatedGCN+RWSE | 0.2529 | 0.3357 | 119 | [Range-aware Positional Encoding via High-order Pretraining: Theory and...](/papers/2409.19117/) | published later (2024-09) |
| [2306.03561](/papers/2306.03561/) | Peptides-struct | GatedGCN+RWSE | 0.2529 | 0.3357 | 119 | [Range-aware Positional Encoding via High-order Pretraining: Theory and...](/papers/2409.19117/) | published later (2024-09) |
| [2308.11129](/papers/2308.11129/) | Peptides-struct | GatedGCN+RWSE | 0.2529 | 0.3357 | 119 | [Range-aware Positional Encoding via High-order Pretraining: Theory and...](/papers/2409.19117/) | published later (2024-09) |
| [2309.04941](/papers/2309.04941/) | Peptides-struct | GatedGCN+RWSE | 0.2529 | 0.3357 | 119 | [Range-aware Positional Encoding via High-order Pretraining: Theory and...](/papers/2409.19117/) | published later (2024-09) |
| [2309.16014](/papers/2309.16014/) | Peptides-struct | GatedGCN+RWSE | 0.2529 | 0.3357 | 119 | [Range-aware Positional Encoding via High-order Pretraining: Theory and...](/papers/2409.19117/) | published later (2024-09) |
| [2310.03274](/papers/2310.03274/) | Peptides-struct | GatedGCN+RWSE | 0.2529 | 0.3357 | 119 | [Range-aware Positional Encoding via High-order Pretraining: Theory and...](/papers/2409.19117/) | published later (2024-09) |
| [2311.01276](/papers/2311.01276/) | Peptides-struct | GatedGCN+RWSE | 0.2529 | 0.3357 | 119 | [Range-aware Positional Encoding via High-order Pretraining: Theory and...](/papers/2409.19117/) | published later (2024-09) |
| [2401.17791](/papers/2401.17791/) | Peptides-struct | GatedGCN+RWSE | 0.2529 | 0.3357 | 119 | [Range-aware Positional Encoding via High-order Pretraining: Theory and...](/papers/2409.19117/) | published later (2024-09) |
| [2402.08450](/papers/2402.08450/) | Peptides-struct | GatedGCN+RWSE | 0.2529 | 0.3357 | 119 | [Range-aware Positional Encoding via High-order Pretraining: Theory and...](/papers/2409.19117/) | published later (2024-09) |
| [2406.12059](/papers/2406.12059/) | Peptides-struct | GatedGCN+RWSE | 0.2529 | 0.3357 | 119 | [Range-aware Positional Encoding via High-order Pretraining: Theory and...](/papers/2409.19117/) | published later (2024-09) |
| [2407.12419](/papers/2407.12419/) | Peptides-struct | GatedGCN+RWSE | 0.2529 | 0.3357 | 119 | [Range-aware Positional Encoding via High-order Pretraining: Theory and...](/papers/2409.19117/) | published later (2024-09) |
| [2412.01519](/papers/2412.01519/) | Peptides-struct | GatedGCN+RWSE | 0.2529 | 0.3357 | 119 | [Range-aware Positional Encoding via High-order Pretraining: Theory and...](/papers/2409.19117/) | already known (2024-09) |
| [2604.06336](/papers/2604.06336/) | Peptides-struct | GatedGCN+RWSE | 0.2529 | 0.3357 | 119 | [Range-aware Positional Encoding via High-order Pretraining: Theory and...](/papers/2409.19117/) | already known (2024-09) |
| [2605.06462](/papers/2605.06462/) | Peptides-struct | GatedGCN+RWSE | 0.2529 | 0.3357 | 119 | [Range-aware Positional Encoding via High-order Pretraining: Theory and...](/papers/2409.19117/) | already known (2024-09) |
| [2306.05955](/papers/2306.05955/) | ZINC | CIN | 0.0220 | 0.0790 | 119 | [Graph as Point Set](/papers/2405.02795/) | published later (2024-05-05) |
| [2308.11129](/papers/2308.11129/) | ZINC | CIN | 0.0220 | 0.0790 | 119 | [Graph as Point Set](/papers/2405.02795/) | published later (2024-05-05) |
| [2310.19285](/papers/2310.19285/) | ZINC | CIN | 0.0220 | 0.0790 | 119 | [Graph as Point Set](/papers/2405.02795/) | published later (2024-05-05) |
| [2401.17791](/papers/2401.17791/) | ZINC | CIN | 0.0220 | 0.0790 | 119 | [Graph as Point Set](/papers/2405.02795/) | published later (2024-05-05) |
| [2404.03380](/papers/2404.03380/) | ZINC | CIN | 0.0220 | 0.0790 | 119 | [Graph as Point Set](/papers/2405.02795/) | published later (2024-05-05) |
| [2407.05649](/papers/2407.05649/) | ZINC | CIN | 0.0220 | 0.0790 | 119 | [Graph as Point Set](/papers/2405.02795/) | already known (2024-05-05) |
| [2410.09737](/papers/2410.09737/) | ZINC | CIN | 0.0220 | 0.0790 | 119 | [Graph as Point Set](/papers/2405.02795/) | already known (2024-05-05) |
| [2410.18676](/papers/2410.18676/) | ZINC | CIN | 0.0220 | 0.0790 | 119 | [Graph as Point Set](/papers/2405.02795/) | already known (2024-05-05) |
| [2501.03113](/papers/2501.03113/) | ZINC | CIN | 0.0220 | 0.0790 | 119 | [Graph as Point Set](/papers/2405.02795/) | already known (2024-05-05) |
| [2406.03386](/papers/2406.03386/) | ZINC | SAT | 0.0360 | 0.0890 | 119 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2311.04653](/papers/2311.04653/) | ZINC | GatedGCN | 0.0770 | 0.2260 | 118 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2410.05697](/papers/2410.05697/) | PubMed | GAT | 0.9201 | 0.7845 | 118 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2410.05593](/papers/2410.05593/) | PubMed | GAT | 0.9201 | 0.7850 | 118 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2410.05593](/papers/2410.05593/) | PubMed | GCN | 0.9224 | 0.7900 | 118 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2401.01233](/papers/2401.01233/) | Cora | Nagphormer | 0.8820 | 0.8092 | 118 | [ParaFormer: A Generalized PageRank Graph Transformer for Graph...](/papers/2512.14619/) | published later (2025-12) |
| [2406.08993](/papers/2406.08993/) | Cora | Nagphormer | 0.8820 | 0.8092 | 118 | [ParaFormer: A Generalized PageRank Graph Transformer for Graph...](/papers/2512.14619/) | published later (2025-12) |
| [2409.11504](/papers/2409.11504/) | ZINC | GIN | 0.0650 | 0.1230 | 118 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2410.03424](/papers/2410.03424/) | ogbg-molhiv | GIN | 0.9680 | 0.7678 | 117 | [No Metric to Rule Them All: Toward Principled...](/papers/2502.02379/) | published later (2025-02-04) |
| [2410.05593](/papers/2410.05593/) | CiteSeer | GCN | 0.8139 | 0.7090 | 117 | [Revisiting Heterophily For Graph Neural Networks](/papers/2210.07606/) | already known (2022-10) |
| [2310.05174](/papers/2310.05174/) | Cora | GAT | 0.8825 | 0.8141 | 117 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2406.09291](/papers/2406.09291/) | ZINC | SUN | 0.0240 | 0.0830 | 117 | [Graph as Point Set](/papers/2405.02795/) | already known (2024-05-05) |
| [2504.12588](/papers/2504.12588/) | ZINC | SUN | 0.0240 | 0.0830 | 117 | [Graph as Point Set](/papers/2405.02795/) | already known (2024-05-05) |
| [2506.04765](/papers/2506.04765/) | Texas | GCN | 0.8311 | 0.4505 | 116 | [Revisiting Heterophily For Graph Neural Networks](/papers/2210.07606/) | already known (2022-10) |
| [2602.02268](/papers/2602.02268/) | Texas | GCN | 0.8311 | 0.4505 | 116 | [Revisiting Heterophily For Graph Neural Networks](/papers/2210.07606/) | already known (2022-10) |
| [2410.05697](/papers/2410.05697/) | PubMed | GCN | 0.9224 | 0.7927 | 116 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2508.11390](/papers/2508.11390/) | ogbg-molhiv | GAT | 0.9682 | 0.7700 | 115 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2401.01233](/papers/2401.01233/) | CiteSeer | Polynormer | 0.8180 | 0.7219 | 115 | [GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers](/papers/2411.17296/) | published later (2024-11-26) |