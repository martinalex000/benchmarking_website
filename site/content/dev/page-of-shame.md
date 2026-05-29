---
title: Page of Shame
type: dev
description: Papers whose reported model values materially disagree with the stored
  benchmark values
---

## Page of Shame: Papers Using Wrong Model Values

This page lists papers whose reported primary-metric value for a model disagrees with the stored global benchmark value by more than the reported std, or differs at all when no std is given.

<<<<<<< Updated upstream
**Flagged papers:** 126
**Flagged rows:** 2666
**Rows where a better value was already known at publication time:** 1146
**Rows whose current best source is from a later paper:** 1437
**Rows whose current best source is the same paper:** 83
=======
**Flagged papers:** 68
**Flagged rows:** 775
**Rows where a better value was already known at publication time:** 349
**Rows whose current best source is from a later paper:** 395
**Rows whose current best source is the same paper:** 31
>>>>>>> Stashed changes
**Rows with unknown timing:** 0

### Most affected datasets

| Dataset | Wrong Rows | Papers | Models | Worst Rank Shift | Earlier-known Rows |
|---|---:|---:|---:|---:|---:|
<<<<<<< Updated upstream
| ZINC | 463 | 42 | 51 | 244 | 215 |
| Peptides-func | 209 | 64 | 27 | 306 | 64 |
| Peptides-struct | 196 | 61 | 26 | 330 | 41 |
| Cora | 152 | 30 | 41 | 297 | 67 |
| CiteSeer | 98 | 19 | 27 | 206 | 48 |
| PubMed | 91 | 16 | 25 | 152 | 30 |
| Chameleon | 82 | 13 | 28 | 116 | 49 |
| Squirrel | 82 | 13 | 29 | 96 | 42 |
| CIFAR10 | 74 | 24 | 11 | 93 | 21 |
| MNIST | 72 | 24 | 8 | 94 | 16 |
| Texas | 67 | 16 | 24 | 143 | 45 |
| ogbn-arxiv | 64 | 20 | 15 | 90 | 41 |
| PascalVOC-SP | 64 | 21 | 11 | 63 | 15 |
| Roman-empire | 58 | 18 | 13 | 84 | 35 |
| PCQM-Contact | 58 | 16 | 9 | 63 | 31 |
| PATTERN | 56 | 17 | 6 | 63 | 18 |
| ogbg-molhiv | 52 | 21 | 12 | 214 | 10 |
| COCO-SP | 47 | 16 | 10 | 33 | 14 |
| Wisconsin | 45 | 16 | 16 | 136 | 23 |
| Minesweeper | 44 | 13 | 8 | 76 | 26 |
| CLUSTER | 44 | 15 | 4 | 45 | 16 |
| Cornell | 42 | 14 | 18 | 133 | 35 |
| PROTEINS | 38 | 14 | 13 | 170 | 19 |
| Actor | 34 | 8 | 12 | 60 | 14 |
| Amazon-ratings | 31 | 14 | 6 | 87 | 22 |
=======
| ZINC | 157 | 21 | 36 | 116 | 44 |
| Cora | 48 | 17 | 17 | 86 | 10 |
| PubMed | 44 | 13 | 14 | 61 | 12 |
| Peptides-struct | 39 | 15 | 8 | 83 | 22 |
| Peptides-func | 39 | 12 | 8 | 62 | 24 |
| CiteSeer | 37 | 12 | 14 | 66 | 3 |
| PATTERN | 34 | 7 | 8 | 41 | 33 |
| ogbn-arxiv | 32 | 10 | 12 | 44 | 19 |
| CIFAR10 | 25 | 6 | 7 | 34 | 24 |
| Chameleon | 24 | 5 | 16 | 57 | 21 |
| Squirrel | 23 | 6 | 12 | 48 | 17 |
| ogbg-molhiv | 23 | 9 | 9 | 46 | 10 |
| NCI1 | 21 | 7 | 7 | 60 | 10 |
| ogbg-molpcba | 21 | 8 | 8 | 35 | 11 |
| PROTEINS | 17 | 10 | 7 | 75 | 10 |
| D&D | 10 | 5 | 8 | 60 | 4 |
| ogbl-wikikg2 | 10 | 2 | 6 | 27 | 6 |
| COLLAB | 9 | 5 | 6 | 47 | 2 |
| Coauthor-CS | 9 | 4 | 3 | 19 | 0 |
| Roman-empire | 9 | 4 | 4 | 9 | 0 |
| Cornell | 8 | 4 | 6 | 33 | 8 |
| Amazon-Computers | 8 | 4 | 4 | 31 | 1 |
| ENZYMES | 8 | 4 | 6 | 25 | 2 |
| Amazon-Photo | 8 | 3 | 5 | 22 | 2 |
| PCQM4Mv2 | 8 | 4 | 3 | 15 | 1 |
>>>>>>> Stashed changes

### Most affected models

| Model | Wrong Rows | Papers | Datasets | Worst Rank Shift | Earlier-known Rows |
|---|---:|---:|---:|---:|---:|
<<<<<<< Updated upstream
| GCN | 576 | 109 | 55 | 330 | 272 |
| GatedGCN | 270 | 64 | 18 | 285 | 67 |
| GIN | 235 | 62 | 36 | 313 | 71 |
| GAT | 234 | 63 | 35 | 251 | 125 |
| GPS | 92 | 38 | 12 | 244 | 53 |
| GINE | 77 | 33 | 7 | 259 | 31 |
| NodeFormer | 56 | 15 | 15 | 218 | 26 |
| Graphormer | 56 | 27 | 7 | 198 | 22 |
| APPNP | 47 | 12 | 13 | 256 | 29 |
| SGFormer | 46 | 10 | 13 | 209 | 24 |
| Nagphormer | 46 | 17 | 15 | 200 | 14 |
| Exphormer | 46 | 15 | 15 | 186 | 11 |
| GPRGNN | 44 | 12 | 14 | 238 | 19 |
| MLP | 40 | 13 | 13 | 231 | 12 |
| GraphSAGE | 40 | 19 | 17 | 133 | 27 |
| GatedGCN+RWSE | 31 | 17 | 2 | 122 | 6 |
| H2GCN | 30 | 11 | 9 | 143 | 9 |
| GRIT | 26 | 15 | 3 | 222 | 25 |
| PNA | 25 | 14 | 1 | 204 | 15 |
| CIN | 22 | 13 | 1 | 137 | 9 |
| GraphGPS | 19 | 7 | 9 | 179 | 7 |
| Polynormer | 18 | 5 | 8 | 115 | 7 |
| GAT-sep | 18 | 8 | 4 | 17 | 11 |
| FOSR | 15 | 5 | 10 | 127 | 6 |
| Graph ViT | 15 | 7 | 5 | 125 | 3 |

| ArXiv | Title | Wrong Rows | Earlier-known Rows | Worst Rank Shift | Datasets | Models |
|---|---|---:|---:|---:|---|---|
| [2602.02268](/papers/2602.02268/) | [HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control](/papers/2602.02268/) | 92 | 84 | 330 | Actor, Chameleon, CiteSeer, Cora | APPNP, CoBFormer, DIFFormer, Exphormer |
| [2506.04765](/papers/2506.04765/) | [OpenGT: A Comprehensive Benchmark For Graph Transformers](/papers/2506.04765/) | 82 | 62 | 330 | Actor, Chameleon, Cora, Cornell | APPNP, CoBFormer, DIFFormer, Exphormer |
| [2401.01233](/papers/2401.01233/) | [GEN: A Practical Alternative to Graph Transformers for Long-Range Graph...](/papers/2401.01233/) | 80 | 8 | 155 | Amazon-Photo, Amazon-ratings, COCO-SP, Chameleon | CPGNN, Exphormer, FSGNN, GAT |
| [2308.11129](/papers/2308.11129/) | [Enhancing Graph Transformers with Hierarchical Distance Structural Encoding](/papers/2308.11129/) | 73 | 2 | 301 | Actor, CIFAR10, CLUSTER, Chameleon | APPNP, CIN, GAT, GCN |
| [2406.08993](/papers/2406.08993/) | [Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification](/papers/2406.08993/) | 64 | 9 | 118 | Amazon-Photo, Chameleon, CiteSeer, Coauthor-Physics | CPGNN, Exphormer, FSGNN, GAT |
| [2406.03386](/papers/2406.03386/) | [Learning Long Range Dependencies on Graphs via Random Walks](/papers/2406.03386/) | 58 | 11 | 218 | Amazon-ratings, CIFAR10, CLUSTER, COCO-SP | CRaWl, Exphormer, GAT, GAT-sep |
| [2407.18480](/papers/2407.18480/) | [Scalable Graph Compressed Convolutions](/papers/2407.18480/) | 55 | 30 | 141 | Actor, Amazon-ratings, COLLAB, Chameleon | ACMII-GCN, APPNP, ChebNet, DiffPool |
| [2512.14619](/papers/2512.14619/) | [ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation Learning](/papers/2512.14619/) | 54 | 52 | 129 | Amazon-Computers, Chameleon, CiteSeer, Cora | APPNP, CoBFormer, GAT, GCN |
| [2508.05070](/papers/2508.05070/) | [Tango: Graph Neural Dynamics via Learned Energy and Tangential Flows](/papers/2508.05070/) | 51 | 43 | 301 | Amazon-ratings, CIFAR10, CLUSTER, MNIST | GAT, GAT-sep, GCN, GIN |
| [2501.18739](/papers/2501.18739/) | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | 50 | 32 | 243 | Amazon-Computers, COLLAB, Cora, PubMed | APPNP, AWE, AgentNet, CRaWl |
| [2407.05649](/papers/2407.05649/) | [Greener GRASS: Enhancing GNNs with Encoding, Rewiring, and Attention](/papers/2407.05649/) | 49 | 16 | 218 | CIFAR10, CLUSTER, COCO-SP, MNIST | CIN, DRew(GatedGCN), DRew-GCN+LapPE, Drew-GIN |
| [2310.05174](/papers/2310.05174/) | [GSLB: The Graph Structure Learning Benchmark](/papers/2310.05174/) | 48 | 9 | 314 | Actor, COLLAB, CiteSeer, Cora | GAT, GCN, GIN, GPRGNN |
| [2410.05697](/papers/2410.05697/) | [Diffusing to the Top: Boost Graph Neural Networks with Minimal...](/papers/2410.05697/) | 46 | 17 | 218 | Actor, Amazon-Computers, COCO-SP, CiteSeer | APPNP, ChebNet, GAT, GCN |
| [2507.00647](/papers/2507.00647/) | [Cooperative Sheaf Neural Networks](/papers/2507.00647/) | 45 | 45 | 114 | Amazon-ratings, Cornell, Film, Minesweeper | ACMGCN, FAGCN, FSGNN, GAT |
| [2401.17791](/papers/2401.17791/) | [Graph Transformers without Positional Encodings](/papers/2401.17791/) | 42 | 4 | 301 | CIFAR10, CLUSTER, MNIST, PATTERN | CIN, GAT, GCN, GIN |
| [2411.15671](/papers/2411.15671/) | [Best of Both Worlds: Advantages of Hybrid Graph Sequence Models](/papers/2411.15671/) | 40 | 17 | 93 | Amazon-ratings, CIFAR10, D&D, MNIST | Exphormer, GAT, GCN, GIN |
| [2502.00282](/papers/2502.00282/) | [GraphMinNet: Learning Dependencies in Graphs with Light Complexity Minimal Architecture](/papers/2502.00282/) | 39 | 33 | 302 | CIFAR10, CLUSTER, MNIST, MalNet-Tiny | Exphormer, GAT, GCN, GIN |
| [2312.16560](/papers/2312.16560/) | [Algorithmic Graph Tasks](/papers/2312.16560/) | 39 | 9 | 301 | Actor, Chameleon, CiteSeer, Cora | GAT, GCN, GCN+JK, GINE |
| [2312.01538](/papers/2312.01538/) | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | 38 | 2 | 211 | CIFAR10, CLUSTER, MNIST, PATTERN | DRew, GAT, GCN, GIN |
| [2402.08678](/papers/2402.08678/) | [Graph Mamba: Towards Learning on Graphs with State Space Models](/papers/2402.08678/) | 37 | 1 | 302 | Amazon-ratings, CIFAR10, COCO-SP, MNIST | CRaWl, Exphormer, GCN, GIN |
| [2310.19285](/papers/2310.19285/) | [Facilitating Graph Neural Networks with Random Walk on Simplicial Complexes](/papers/2310.19285/) | 37 | 4 | 301 | CIFAR10, MNIST, PCQM-Contact, Peptides-func | CIN, GAT, GCN, GIN |
| [2410.05593](/papers/2410.05593/) | [When Graph Neural Networks Meet Dynamic Mode Decomposition](/papers/2410.05593/) | 36 | 15 | 229 | COCO-SP, CiteSeer, Cora, Cornell | APPNP, GAT, GCN, GPRGNN |
| [2504.12588](/papers/2504.12588/) | [Plain Transformers Can be Powerful Graph Learners](/papers/2504.12588/) | 36 | 35 | 218 | CIFAR10, CLUSTER, MNIST, PATTERN | GAT, GCN, GCN-virtual, GIN |
| [2410.13798](/papers/2410.13798/) | [Learning Graph Quantized Tokenizers](/papers/2410.13798/) | 35 | 19 | 301 | COCO-SP, CiteSeer, Cora, PCQM-Contact | APPNP, Exphormer, GAT, GCN |
| [2310.07430](/papers/2310.07430/) | [Non-backtracking Graph Neural Networks](/papers/2310.07430/) | 33 | 5 | 302 | CiteSeer, Cora, Cornell, PascalVOC-SP | ChebNet, DRew-GCN+LapPE, GAT, GCN |
| [2603.27529](/papers/2603.27529/) | [Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in GNNs](/papers/2603.27529/) | 33 | 33 | 297 | Amazon-Photo, Chameleon, CiteSeer, Coauthor-CS | BORF, DR, FOSR, GAT |
| [2502.09365](/papers/2502.09365/) | [Simple Path Structural Encoding for Graph Transformers](/papers/2502.09365/) | 33 | 30 | 232 | CIFAR10, CLUSTER, MNIST, PATTERN | GAT, GCN, GIN, GINE |
| [2605.05689](/papers/2605.05689/) | [GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency Model](/papers/2605.05689/) | 33 | 33 | 218 | CIFAR10, CLUSTER, COCO-SP, MNIST | GAT, GCN, GIN, GPS |
| [2406.03671](/papers/2406.03671/) | [PANDA: Expanded Width-Aware Message Passing Beyond Rewiring](/papers/2406.03671/) | 33 | 6 | 97 | COLLAB, Cora, Cornell, ENZYMES | + DIGL, BORF, FOSR, GCN |
| [2306.05955](/papers/2306.05955/) | [Path Neural Networks: Expressive and Accurate Graph Neural Networks](/papers/2306.05955/) | 31 | 2 | 302 | IMDB-BINARY, IMDB-MULTI, NCI1, PROTEINS | 3WLGNN, AgentNet, CIN, DiffPool |
| [2405.02795](/papers/2405.02795/) | [Graph as Point Set](/papers/2405.02795/) | 31 | 7 | 301 | PascalVOC-SP, Peptides-func, Peptides-struct, QM9 | 1-GNN, CIN, DRFWL, DTNN* |
| [2410.03424](/papers/2410.03424/) | [Cayley Graph Propagation](/papers/2410.03424/) | 31 | 10 | 166 | COLLAB, ENZYMES, IMDB-BINARY, MUTAG | EGP (GIN), GCN, GCN + BORF, GCN + DIGL |
| [2402.08450](/papers/2402.08450/) | [Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph Products](/papers/2402.08450/) | 30 | 3 | 302 | BACE, Peptides-func, Peptides-struct, ZINC | CIN (small), DSS-GNN, GCN, GIN |
| [2406.18380](/papers/2406.18380/) | [KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning](/papers/2406.18380/) | 30 | 15 | 246 | CiteSeer, Cora, Cornell, D&D | GAT, GCN, GIN |
| [2505.23185](/papers/2505.23185/) | [Improving the Effective Receptive Field of Message-Passing Neural Networks](/papers/2505.23185/) | 30 | 20 | 78 | Amazon-ratings, COCO-SP, D&D, London | GAT, GAT-sep, GCN, GPS |
| [IAZXEX1dVV](/papers/IAZXEX1dVV/) | [LRIM: a Physics-Based Benchmark for Provably Evaluating Long-Range Capabilities in...](/papers/IAZXEX1dVV/) | 30 | 0 | 5 | LRIM | GIN, GPS+LapPE, GPS+RWSE, GPS-Base |
| [2406.12059](/papers/2406.12059/) | [A Scalable and Effective Alternative to Graph Transformers](/papers/2406.12059/) | 27 | 12 | 301 | COCO-SP, PCQM-Contact, PCQM4Mv2, PascalVOC-SP | ANS-GT, GAT, GCN, GINE |
| [2102.08786](/papers/2102.08786/) | [Walking Out of the Weisfeiler Leman Hierarchy: Graph Learning Beyond...](/papers/2102.08786/) | 26 | 0 | 301 | CIFAR10, MNIST, PascalVOC-SP, Peptides-func | CIN, CRaWl, GAT, GCN |
| [2405.13806](/papers/2405.13806/) | [A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition](/papers/2405.13806/) | 26 | 5 | 301 | Amazon-Computers, Amazon-Photo, COCO-SP, Coauthor-CS | APPNP, GAT, GCN, GINE |
| [2404.03380](/papers/2404.03380/) | [On the Theoretical Expressive Power and the Design Space of...](/papers/2404.03380/) | 25 | 9 | 301 | Cornell, Peptides-func, Peptides-struct, Texas | CIN, GAT, GCN, GIN |
| [2210.07606](/papers/2210.07606/) | [Revisiting Heterophily For Graph Neural Networks](/papers/2210.07606/) | 25 | 0 | 217 | Chameleon, CiteSeer, Cora, Cornell | APPNP, FAGCN, GAT, GCN |
| [2310.03274](/papers/2310.03274/) | [Fragment-based Pretraining and Finetuning on Molecular Graphs](/papers/2310.03274/) | 24 | 8 | 302 | BACE, BBBP, ClinTox, Peptides-func | GCN, GIN, GatedGCN, GatedGCN+RWSE |
| [2407.02758](/papers/2407.02758/) | [Differential Encoding for Improved Representation Learning over Graphs](/papers/2407.02758/) | 24 | 8 | 252 | CIFAR10, COCO-SP, MNIST, PCQM-Contact | GCN, GIN, GINE, GPS |
| [2502.09263](/papers/2502.09263/) | [Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple...](/papers/2502.09263/) | 24 | 13 | 192 | CIFAR10, COLLAB, MNIST, PATTERN | Exphormer, GCN, GIN, GMN |
| [2404.09774](/papers/2404.09774/) | [RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional Networks](/papers/2404.09774/) | 23 | 2 | 252 | CIFAR10, CLUSTER, MNIST, PATTERN | GCN, GIN, GINE, GPS |
| [2410.09737](/papers/2410.09737/) | [Towards Stable, Globally Expressive Graph Representations with Laplacian Eigenvectors](/papers/2410.09737/) | 23 | 15 | 204 | PCQM-Contact, ZINC | CIN, GCN, GIN, GINE |
| [2501.03113](/papers/2501.03113/) | [Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based Centrality](/papers/2501.03113/) | 23 | 9 | 171 | BACE, Peptides-func, Peptides-struct, Tox21 | CIN, GCN, GIN, GPS |
| [2402.00789](/papers/2402.00789/) | [Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective State Spaces](/papers/2402.00789/) | 22 | 1 | 93 | CIFAR10, CLUSTER, MNIST, PATTERN | Exphormer, GCN, GIN, GatedGCN |
| [2409.19117](/papers/2409.19117/) | [Range-aware Positional Encoding via High-order Pretraining: Theory and Practice](/papers/2409.19117/) | 21 | 7 | 301 | CIFAR10, MNIST, NCI1, Peptides-func | DGCNN, GAT, GCN, GIN |
| [2311.04653](/papers/2311.04653/) | [Hybrid Focal and Full-Range Attention Based Graph Transformers](/papers/2311.04653/) | 21 | 1 | 285 | Chameleon, CiteSeer, Cora, Peptides-func | GCN, GPS, GRPE, GatedGCN |
| [2512.04475](/papers/2512.04475/) | [GraphBench](/papers/2512.04475/) | 20 | 0 | 2 | Bridges, Flow, MST, Max Clique | GIN, GT |
| [2206.08164](/papers/2206.08164/) | [LRGB](/papers/2206.08164/) | 19 | 0 | 301 | COCO-SP, PCQM-Contact, PascalVOC-SP, Peptides-func | GCN, GINE, GatedGCN, GatedGCN+LapPE |
| [2309.04941](/papers/2309.04941/) | [Distance-Restricted Folklore Weisfeiler-Leman GNNs with Provable Cycle Counting Power](/papers/2309.04941/) | 19 | 1 | 301 | Peptides-func, Peptides-struct, ZINC, ogbg-molhiv | CIN, CIN (small), GCN, GIN |
| [2310.20519](/papers/2310.20519/) | [Enhancing Graph Neural Networks with Quantum Computed Encodings](/papers/2310.20519/) | 19 | 0 | 138 | CIFAR10, CLUSTER, MNIST, PATTERN | GAT, GCN, GIN, GPS |
| [2411.17296](/papers/2411.17296/) | [GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers](/papers/2411.17296/) | 19 | 15 | 87 | Actor, Amazon-Photo, Chameleon, CiteSeer | ChebNet, GAT, GCN, GPRGNN |
| [2405.03481](/papers/2405.03481/) | [AnchorGT: Efficient and Flexible Attention Architecture for Scalable Graph Transformers](/papers/2405.03481/) | 18 | 5 | 301 | CLUSTER, CiteSeer, PCQM4Mv2, Peptides-func | GAT, GCN, GatedGCN, GraphSAGE |
| [2406.09291](/papers/2406.09291/) | [A Flexible, Equivariant Framework for Subgraph GNNs via Graph Products...](/papers/2406.09291/) | 18 | 12 | 171 | ZINC | DSS-GNN, GCN, GIN, GNN (a) |
| [2602.18837](/papers/2602.18837/) | [L2G-Net: Local to Global Spectral Graph Neural Networks via Cauchy...](/papers/2602.18837/) | 18 | 18 | 71 | Amazon-ratings, Minesweeper, Roman-empire, Tolokers | GAT, GAT-sep, GCN, GPS |
| [2412.07188](/papers/2412.07188/) | [Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking...](/papers/2412.07188/) | 17 | 8 | 264 | Coauthor-CS, Coauthor-Physics, Cora | APPNP, FA, GAT, GATv2 |
| [2506.14098](/papers/2506.14098/) | [Toward a Graph Foundation Model: Pre-Training Transformers With Random Walks](/papers/2506.14098/) | 17 | 6 | 222 | Cora, PubMed, WikiCS, ogbg-molhiv | BGRL, GAT, GCN, GIN |
| [2310.02156](/papers/2310.02156/) | [Probabilistically Rewired Message-Passing Neural Networks](/papers/2310.02156/) | 16 | 4 | 301 | Cornell, NCI1, Peptides-func, Peptides-struct | + DIGL, DGCNN, DRew-GCN+LapPE, Drew-GIN |
| [2410.23686](/papers/2410.23686/) | [Towards Dynamic Message Passing on Graphs](/papers/2410.23686/) | 16 | 7 | 301 | COLLAB, IMDB-BINARY, IMDB-MULTI, NCI1 | DiffPool, GAT, GCN, GIN |
| [2601.07419](/papers/2601.07419/) | [Position: Don't be Afraid of Over-Smoothing And Over-Squashing](/papers/2601.07419/) | 16 | 16 | 198 | Amazon-Computers, Amazon-Photo, CiteSeer, Cora | GATv2, GCN, GCN + SDRF, GCNII |
| [2506.07624](/papers/2506.07624/) | [Return of ChebNet: Understanding and Improving an Overlooked GNN on...](/papers/2506.07624/) | 16 | 12 | 80 | Minesweeper, Peptides-func, Peptides-struct, Tolokers | Drew-GIN, Exphormer, GAT, GAT-sep |
| [2309.00367](/papers/2309.00367/) | [Where Did the Gap Go? Reassessing the Long-Range Graph Benchmark](/papers/2309.00367/) | 16 | 0 | 78 | COCO-SP, PCQM-Contact, PascalVOC-SP, Peptides-func | Exphormer, GCN, GINE, GPS |
| [2605.06462](/papers/2605.06462/) | [Invariant-Based Diagnostics for Graph Benchmarks](/papers/2605.06462/) | 15 | 11 | 301 | Flow, Peptides-func, Peptides-struct | GCN, GIN, GINE, GPS |
| [2509.06777](/papers/2509.06777/) | [Asynchronous Message Passing for Addressing Oversquashing in Graph Neural Networks](/papers/2509.06777/) | 15 | 3 | 127 | ENZYMES, IMDB-BINARY, MUTAG, PROTEINS | BORF, FOSR, GCN + BORF, GCN + DIGL |
| [2405.17311](/papers/2405.17311/) | [Probabilistic Graph Rewiring via Virtual Nodes](/papers/2405.17311/) | 15 | 5 | 125 | Cornell, NCI1, PCQM-Contact, Peptides-func | + DIGL, DGCNN, GCN, GIN |
| [2310.01704](/papers/2310.01704/) | [Transformers are efficient hierarchical chemical graph learners](/papers/2310.01704/) | 14 | 2 | 302 | Peptides-struct, ZINC, ogbg-molhiv | GAT, GCN, GIN, Graphormer |
| [2510.02565](/papers/2510.02565/) | [On The Expressive Power of GNN Derivatives](/papers/2510.02565/) | 14 | 11 | 301 | Peptides-func, Peptides-struct, Tox21 | GCN, GIN, GIN + RWSE, GINE |
| [2601.19094](/papers/2601.19094/) | [FloydNet: A Learning Paradigm for Global Relational Reasoning](/papers/2601.19094/) | 14 | 10 | 301 | COCO-SP, PCQM-Contact, PascalVOC-SP, Peptides-func | Exphormer, GCN, GPS |
| [2604.17324](/papers/2604.17324/) | [SigGate-GT: Taming Over-Smoothing in Graph Transformers via Sigmoid-Gated Attention](/papers/2604.17324/) | 14 | 14 | 204 | Peptides-func, Peptides-struct, ZINC, ogbg-molhiv | GCN, GRIT, GatedGCN, Graphormer |
| [2405.15540](/papers/2405.15540/) | [Bundle Neural Networks for message diffusion on graphs](/papers/2405.15540/) | 14 | 4 | 78 | Amazon-ratings, Minesweeper, Peptides-func, Peptides-struct | GAT, GAT-sep, GCN, GatedGCN |
| [2410.05499](/papers/2410.05499/) | [Unitary convolutions for learning on graphs and groups](/papers/2410.05499/) | 13 | 8 | 149 | ENZYMES, Minesweeper, PROTEINS, PascalVOC-SP | GAT, GCN, GIN, GatedGCN |
| [2310.01267](/papers/2310.01267/) | [Cooperative Graph Neural Networks](/papers/2310.01267/) | 13 | 1 | 71 | Amazon-ratings, IMDB-BINARY, IMDB-MULTI, Minesweeper | DiffPool, GAT, GAT-sep, GCN |
| [2306.02866](/papers/2306.02866/) | [Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance](/papers/2306.02866/) | 12 | 0 | 301 | PCQM-Contact, Peptides-func, Peptides-struct | GCN, GINE, GatedGCN, GatedGCN+RWSE |
| [2604.06336](/papers/2604.06336/) | [BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular Representation Learning](/papers/2604.06336/) | 12 | 12 | 301 | BACE, Peptides-func, Peptides-struct, SIDER | GCN, GINE, GatedGCN, GatedGCN+RWSE |
| [2307.07107](/papers/2307.07107/) | [Graph Positional and Structural Encoder](/papers/2307.07107/) | 12 | 0 | 224 | CIFAR10, MNIST, PCQM4Mv2, Peptides-func | GCN, GIN, GINE, GPS |
| [2406.05815](/papers/2406.05815/) | [What Can We Learn from State Space Models for Machine...](/papers/2406.05815/) | 12 | 0 | 92 | CIFAR10, MNIST, MalNet-Tiny, PATTERN | GCN, GIN, GatedGCN |
| [2306.03561](/papers/2306.03561/) | [CIN++: Enhancing Topological Message Passing](/papers/2306.03561/) | 11 | 0 | 301 | Peptides-func, Peptides-struct, ogbg-molhiv | GCN, GIN, GINE, GSN |
| [2310.01668](/papers/2310.01668/) | [Locality-Aware Graph Rewiring in GNNs](/papers/2310.01668/) | 11 | 0 | 301 | IMDB-BINARY, MUTAG, PROTEINS, Peptides-func | FOSR, GAT, GCN, GCN + FoSR |
| [2311.01276](/papers/2311.01276/) | [Neural Atoms: Propagating Long-range Interaction in Molecular Graphs through Efficient...](/papers/2311.01276/) | 11 | 2 | 301 | PCQM-Contact, Peptides-func, Peptides-struct | GCN, GINE, GatedGCN, GatedGCN+RWSE |
| [2405.13526](/papers/2405.13526/) | [Understanding Virtual Nodes: Oversquashing and Node Heterogeneity](/papers/2405.13526/) | 11 | 2 | 301 | CIFAR10, Peptides-struct, ogbg-molhiv, ogbg-molpcba | GCN, GIN, GINE, GatedGCN |
| [2412.01519](/papers/2412.01519/) | [ReHub: Linear Complexity Graph Transformers with Adaptive Hub-Spoke Reassignment](/papers/2412.01519/) | 11 | 6 | 301 | PCQM-Contact, Peptides-func, Peptides-struct | GCN, GINE, GatedGCN, GatedGCN+RWSE |
| [2309.04082](/papers/2309.04082/) | [Curve Your Attention: Mixed-Curvature Transformers for Graph Representation Learning](/papers/2309.04082/) | 11 | 2 | 231 | Cora, Texas | GAT, GCN, H2GCN, MLP |
| [2604.03815](/papers/2604.03815/) | [k-Maximum Inner Product Attention for Graph Transformers and the Expressive...](/papers/2604.03815/) | 11 | 11 | 80 | COCO-SP, PascalVOC-SP, Peptides-func, Peptides-struct | GAT, GCN, GatedGCN |
| [2505.15405](/papers/2505.15405/) | [HOPSE: Scalable Higher-Order Positional and Structural Encoder for Combinatorial Representations](/papers/2505.15405/) | 10 | 10 | 221 | MUTAG, NCI1, ZINC | GAT, GCN, GIN |
| [2509.01254](/papers/2509.01254/) | [What Expressivity Theory Misses: Message Passing Complexity for GNNs](/papers/2509.01254/) | 10 | 10 | 218 | ZINC | CIN, GCN, GIN, GSN |
| [2502.10818](/papers/2502.10818/) | [On Vanishing Gradients, Over-Smoothing, and Over-Squashing in GNNs: Bridging Recurrent...](/papers/2502.10818/) | 10 | 10 | 100 | Amazon-ratings, Minesweeper, Peptides-func, Peptides-struct | Exphormer, GAT, GCN, GRED |
| [2511.16767](/papers/2511.16767/) | [When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed Graphs...](/papers/2511.16767/) | 10 | 10 | 87 | Amazon-ratings, BACE, BBBP, CiteSeer | GAT, GCN, GIN, MLP |
| [2502.02379](/papers/2502.02379/) | [No Metric to Rule Them All: Toward Principled Evaluations of...](/papers/2502.02379/) | 8 | 6 | 168 | MUTAG, NCI1, PROTEINS, ogbg-molhiv | GAT, GCN, GIN |
| [2409.11504](/papers/2409.11504/) | [Preventing Representational Rank Collapse in MPNNs by Splitting the Computational...](/papers/2409.11504/) | 8 | 3 | 136 | Roman-empire, Squirrel, ZINC | GAT, GCN, GIN, GLoGNN |
| [2309.09384](/papers/2309.09384/) | [Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci Curvature](/papers/2309.09384/) | 8 | 0 | 93 | MUTAG, PROTEINS, Wisconsin | BORF, FOSR, GCN, GCN + BORF |
| [2312.04234](/papers/2312.04234/) | [Graph Convolutions Enrich the Self-Attention in Transformers!](/papers/2312.04234/) | 7 | 0 | 194 | CIFAR10, Peptides-func, Peptides-struct, ZINC | GPS, Graph ViT, Graphormer |
| [2502.01122](/papers/2502.01122/) | [Learning Efficient Positional Encodings with Graph Neural Networks](/papers/2502.01122/) | 7 | 6 | 186 | Peptides-struct, ZINC | GCN, GIN, GPS, SignNet |
| [2604.24293](/papers/2604.24293/) | [Latent-Hysteresis Graph ODEs: Modeling Coupled Topology-Feature Evolution via Continuous Phase...](/papers/2604.24293/) | 7 | 7 | 139 | Chameleon, Cora, ZINC | GraphGPS, Polynormer, SGFormer, Subgraphormer |
| [2402.10793](/papers/2402.10793/) | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | 7 | 0 | 103 | Peptides-func, Peptides-struct, ZINC | GCN, GIN, Graphormer |
| [2602.17893](/papers/2602.17893/) | [COMBA: Cross Batch Aggregation for Learning Large Graphs with Context...](/papers/2602.17893/) | 7 | 7 | 76 | Amazon-ratings, Minesweeper, Roman-empire, ogbn-arxiv | GCN, Graph Mamba-1, Nagphormer |
| [2508.10651](/papers/2508.10651/) | [Graph Learning via Logic-Based Weisfeiler--Leman Variants and Tabularization](/papers/2508.10651/) | 6 | 5 | 282 | ClinTox, Peptides-func, ogbg-molhiv | GCN, GIN, GPS |
| [2508.11390](/papers/2508.11390/) | [A Remedy for Over-Squashing in Graph Learning via Forman‐Ricci Curvature...](/papers/2508.11390/) | 6 | 4 | 157 | NCI1, PROTEINS, ogbg-molhiv | GAT, GCN |
| [2508.19071](/papers/2508.19071/) | [Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks](/papers/2508.19071/) | 5 | 5 | 152 | Cora, Cornell, Texas, Wisconsin | + DIGL, BORF, FA |
| [2410.18676](/papers/2410.18676/) | [Homomorphism Counts as Structural Encodings for Graph Learning](/papers/2410.18676/) | 5 | 4 | 137 | MNIST, ZINC | CIN, GIN, GIN + RWSE, GPS |
| [2306.10759](/papers/2306.10759/) | [SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations](/papers/2306.10759/) | 5 | 0 | 50 | ogbn-arxiv, ogbn-proteins | GCN, MLP, NodeFormer, SIGN |
| [2503.09008](/papers/2503.09008/) | [City-Networks](/papers/2503.09008/) | 5 | 3 | 32 | D&D | ChebNet, GAT, GCN, MLP |
| [2505.23345](/papers/2505.23345/) | [Graph Positional Autoencoders as Self-supervised Learners](/papers/2505.23345/) | 5 | 5 | 25 | BACE, BBBP, ClinTox | GraphMAE, JOAO |
| [2412.03783](/papers/2412.03783/) | [Expressivity of Representation Learning on Continuous-Time Dynamic Graphs: An Information-Flow...](/papers/2412.03783/) | 5 | 5 | 14 | ogbl-wikikg2 | CTAN, DyRep, JODIE, TGAT |
| [2309.16014](/papers/2309.16014/) | [Graph-level Representation Learning with Joint-Embedding Predictive Architectures](/papers/2309.16014/) | 4 | 0 | 303 | Peptides-func, Peptides-struct | GCN, GatedGCN+RWSE |
| [2407.12419](/papers/2407.12419/) | [Dirac--Bianconi Graph Neural Networks -- Enabling Non-Diffusive Long-Range Graph Predictions](/papers/2407.12419/) | 4 | 0 | 301 | Peptides-struct | GCN, GINE, GatedGCN, GatedGCN+RWSE |
| [2407.12136](/papers/2407.12136/) | [Molecular Topological Profile (MOLTOP) - Simple and Strong Baseline for...](/papers/2407.12136/) | 4 | 1 | 252 | Peptides-func | GCN, GINE, GatedGCN, GatedGCN+RWSE |
| [2310.01618](/papers/2310.01618/) | [Operator Learning Meets Numerical Analysis: Improving Neural Networks through Iterative...](/papers/2310.01618/) | 4 | 2 | 120 | CiteSeer, Cora | GAT, GCN |
| [2508.17630](/papers/2508.17630/) | [Quantum Graph Attention Network: A Novel Quantum Multi-Head Attention Mechanism...](/papers/2508.17630/) | 4 | 2 | 119 | PubMed, ogbn-arxiv, ogbn-proteins | GAT, GATv2 |
| [2406.06984](/papers/2406.06984/) | [On the Stability of Multiset and Graph Neural Networks](/papers/2406.06984/) | 4 | 0 | 78 | Peptides-func, Peptides-struct | GCN, GatedGCN |
| [2401.14580](/papers/2401.14580/) | [Design Your Own Universe: A Physics-Informed Agnostic Method for Enhancing...](/papers/2401.14580/) | 4 | 1 | 62 | ogbn-arxiv | GAT, GCN, GRAND, MLP |
| [2506.08618](/papers/2506.08618/) | [HSG-12M](/papers/2506.08618/) | 4 | 4 | 39 | D&D | GAT, GCN, GIN, GraphSAGE |
| [2512.15549](/papers/2512.15549/) | [Photonics-Enhanced Graph Convolutional Networks](/papers/2512.15549/) | 3 | 3 | 329 | Peptides-func, Peptides-struct | GCN, GCN+LapPE |
| [2509.22259](/papers/2509.22259/) | [Rotary Position Encodings for Graphs](/papers/2509.22259/) | 3 | 2 | 99 | Cora | GAT, GCN, GraphSAGE |
| [2501.09821](/papers/2501.09821/) | [bnpool: Bayesian Nonparametric Pooling for Graphs](/papers/2501.09821/) | 3 | 3 | 75 | COLLAB, ENZYMES | DiffPool, SEP |
| [2407.04236](/papers/2407.04236/) | [Graph Pooling via Ricci Flow](/papers/2407.04236/) | 3 | 0 | 62 | COLLAB, ogbg-molhiv | DMON, MinCut |
| [2401.03350](/papers/2401.03350/) | [Accurate and Scalable Estimation of Epistemic Uncertainty for Graph Neural...](/papers/2401.03350/) | 2 | 0 | 94 | MNIST | GPS+LapPE, GatedGCN |
| [2502.07364](/papers/2502.07364/) | [Effects of Dropout on Performance in Long-range Graph Learning Tasks](/papers/2502.07364/) | 2 | 2 | 65 | Cora | None, SDRF |
| [2405.11951](/papers/2405.11951/) | [Distinguished In Uniform: Self-Attention Vs. Virtual Nodes](/papers/2405.11951/) | 2 | 1 | 22 | ogbg-molpcba | GCN, GINE |
| [2405.19121](/papers/2405.19121/) | [Spatio-Spectral Graph Neural Networks](/papers/2405.19121/) | 2 | 0 | 20 | CLUSTER | GCN, GatedGCN |
| [2506.05393](/papers/2506.05393/) | [Are Large Language Models Good Temporal Graph Learners?](/papers/2506.05393/) | 2 | 2 | 19 | ogbl-wikikg2 | GraphMixer, TGN |
| [2508.14097](/papers/2508.14097/) | [Non-Dissipative Graph Propagation for Non-Local Community Detection](/papers/2508.14097/) | 1 | 1 | 96 | Wisconsin | SUBLIME |
| [2603.00599](/papers/2603.00599/) | [Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger](/papers/2603.00599/) | 1 | 1 | 39 | Cora | HGNN |
| [2307.03393](/papers/2307.03393/) | [Exploring the Potential of Large Language Models (LLMs) in Learning...](/papers/2307.03393/) | 1 | 0 | 8 | ogbn-arxiv | GCN |
=======
| GCN | 171 | 54 | 43 | 111 | 79 |
| GAT | 91 | 36 | 27 | 73 | 39 |
| GIN | 79 | 31 | 23 | 116 | 43 |
| GraphSAGE | 58 | 21 | 26 | 114 | 14 |
| GatedGCN | 51 | 20 | 9 | 112 | 28 |
| PNA | 28 | 17 | 10 | 75 | 8 |
| Graphormer | 20 | 15 | 4 | 63 | 2 |
| APPNP | 19 | 8 | 10 | 57 | 6 |
| GINE | 17 | 9 | 2 | 72 | 8 |
| GPS | 14 | 12 | 3 | 87 | 11 |
| NodeFormer | 9 | 6 | 6 | 74 | 6 |
| DiffPool | 9 | 5 | 4 | 58 | 2 |
| DGN | 9 | 6 | 4 | 24 | 7 |
| GloGNN | 8 | 3 | 6 | 86 | 7 |
| Exphormer | 8 | 3 | 8 | 54 | 5 |
| LP | 8 | 4 | 3 | 33 | 3 |
| FAGCN | 7 | 3 | 5 | 55 | 4 |
| NAGphormer | 6 | 3 | 4 | 12 | 1 |
| SAN+RWSE | 6 | 6 | 1 | 12 | 5 |
| MLP | 5 | 3 | 3 | 57 | 4 |
| DGCNN | 5 | 3 | 4 | 54 | 2 |
| ChebNet | 5 | 4 | 4 | 29 | 3 |
| DIFFormer | 4 | 2 | 4 | 52 | 4 |
| Graphtransformer | 4 | 2 | 3 | 46 | 2 |
| Graphormer-GD | 4 | 4 | 1 | 34 | 1 |

| ArXiv | Title | Wrong Rows | Earlier-known Rows | Worst Rank Shift | Datasets | Models |
|---|---|---:|---:|---:|---|---|
| [2305.17589](/papers/2305.17589/) | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | 59 | 26 | 104 | Amazon-Computers, Amazon-Photo, COLLAB, CiteSeer | APPNP, CompGCN, ComplEx, DistMult |
| [2305.15747](/papers/2305.15747/) | [Union Subgraph Neural Networks](/papers/2305.15747/) | 45 | 0 | 115 | Amazon-Computers, Amazon-Photo, CiteSeer, Cora | GAT, GCN, GIN, GPS |
| [2602.02268](/papers/2602.02268/) | [HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control](/papers/2602.02268/) | 41 | 41 | 111 | Chameleon, Cora, Cornell, Peptides-func | APPNP, DIFFormer, Exphormer, GAT |
| [2508.05070](/papers/2508.05070/) | [Tango: Graph Neural Dynamics via Learned Energy and Tangential Flows](/papers/2508.05070/) | 32 | 24 | 115 | Amazon-ratings, CIFAR10, CLUSTER, Minesweeper | DGN, GAT, GCN, GIN |
| [2401.17791](/papers/2401.17791/) | [Graph Transformers without Positional Encodings](/papers/2401.17791/) | 26 | 23 | 115 | CIFAR10, CLUSTER, PATTERN, Peptides-func | DGN, GAT, GCN, GIN |
| [2108.03348](/papers/2108.03348/) | [Global Self-Attention as a Replacement for Graph Convolution](/papers/2108.03348/) | 26 | 13 | 114 | CIFAR10, MNIST, PATTERN, PCQM4Mv2 | DGN, EGT, GAT, GCN |
| [2501.18739](/papers/2501.18739/) | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | 24 | 14 | 115 | COLLAB, Cora, REDDIT-MULTI-5K, ZINC | APPNP, AWE, AgentNet, CRaWl |
| [2602.07256](/papers/2602.07256/) | [Graph homophily booster: Reimagining the role of discrete features in...](/papers/2602.07256/) | 23 | 23 | 86 | Actor, Chameleon, CiteSeer, Cora | APPNP, DIFFormer, FAGCN, FSGNN |
| [2312.01538](/papers/2312.01538/) | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | 22 | 16 | 110 | CIFAR10, NCI1, PATTERN, PROTEINS | DRew, DiffPool, GAT, GCN |
| [2101.00797](/papers/2101.00797/) | [Beyond Low-frequency Information in Graph Convolutional Networks](/papers/2101.00797/) | 21 | 2 | 56 | CiteSeer, Cora, PubMed | APPNP, ChebNet, FAGCN, GAT |
| [2301.09505](/papers/2301.09505/) | [Rethinking the Expressive Power of GNNs via Graph Biconnectivity](/papers/2301.09505/) | 19 | 1 | 115 | ZINC | CIN (small), DS-GNN, GAT, GCN |
| [2502.00282](/papers/2502.00282/) | [GraphMinNet: Learning Dependencies in Graphs with Light Complexity Minimal Architecture](/papers/2502.00282/) | 19 | 19 | 115 | CIFAR10, CLUSTER, PATTERN, Peptides-func | GAT, GCN, GIN, GatedGCN |
| [2402.08450](/papers/2402.08450/) | [Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph Products](/papers/2402.08450/) | 19 | 7 | 87 | Peptides-func, Peptides-struct, ZINC | CIN (small), DS-GNN, GCN, GIN |
| [2005.00687](/papers/2005.00687/) | [Open Graph Benchmark: Datasets for Machine Learning on Graphs](/papers/2005.00687/) | 19 | 0 | 35 | ogbg-molhiv, ogbg-molpcba, ogbl-ddi, ogbl-wikikg2 | ComplEx, DistMult, GCN, GIN |
| [2305.06102](/papers/2305.06102/) | [Towards Better Graph Representation Learning with Parameterized Decomposition & Filtering](/papers/2305.06102/) | 14 | 4 | 115 | ENZYMES, NCI1, PROTEINS, ZINC | DGCNN, ECC, GAT, GCN |
| [2302.11640](/papers/2302.11640/) | [A critical look at the evaluation of GNNs under heterophily:...](/papers/2302.11640/) | 14 | 6 | 37 | Chameleon, Roman-empire, Squirrel | CPGNN, FAGCN, FSGNN, GAT |
| [2205.12454](/papers/2205.12454/) | [Recipe for a General, Powerful, Scalable Graph Transformer](/papers/2205.12454/) | 13 | 0 | 115 | PCQM4Mv2, Peptides-struct, ZINC, ogbg-molhiv | CRaWl, GAT, GCN, GIN |
| [2303.06147](/papers/2303.06147/) | [Exphormer: Sparse Transformers for Graphs](/papers/2303.06147/) | 13 | 7 | 80 | CLUSTER, PATTERN, Peptides-func, Peptides-struct | DGN, GAT, GCN, GIN |
| [2605.06462](/papers/2605.06462/) | [Invariant-Based Diagnostics for Graph Benchmarks](/papers/2605.06462/) | 13 | 7 | 80 | Flow, Peptides-func, Peptides-struct | GCN, GIN, GINE, GatedGCN |
| [2410.23686](/papers/2410.23686/) | [Towards Dynamic Message Passing on Graphs](/papers/2410.23686/) | 13 | 13 | 56 | COLLAB, IMDB-BINARY, IMDB-MULTI, NCI1 | GCN, GIN, GraphSAGE, SAGPool |
| [2506.07624](/papers/2506.07624/) | [Return of ChebNet: Understanding and Improving an Overlooked GNN on...](/papers/2506.07624/) | 13 | 5 | 23 | Amazon-ratings, Roman-empire, Tolokers, ogbn-arxiv | Exphormer, GAT, GCN, GPS_GCNI+Performer (RWSE) |
| [2302.08647](/papers/2302.08647/) | [Multiresolution Graph Transformers and Wavelet Positional Encoding for Learning Hierarchical...](/papers/2302.08647/) | 12 | 1 | 103 | Peptides-func, Peptides-struct, ZINC | GAT, GCN, GINE, GPS |
| [1312.6203](/papers/1312.6203/) | [Spectral Networks and Locally Connected Networks on Graphs](/papers/1312.6203/) | 12 | 0 | 54 | CiteSeer, Cora, PubMed | APPNP, GAT, GCN, GraphSAGE |
| [2002.04025](/papers/2002.04025/) | [Can Graph Neural Networks Count Substructures?](/papers/2002.04025/) | 10 | 0 | 113 | ZINC, ogbg-molhiv | GAT, GCN, GIN, GatedGCN |
| [1609.02907](/papers/1609.02907/) | [Semi-Supervised Classification with Graph Convolutional Networks](/papers/1609.02907/) | 10 | 4 | 48 | CiteSeer, Cora, Cornell, PubMed | DeepWalk, GCN, LP, ManiReg |
| [1811.05868](/papers/1811.05868/) | [Pitfalls of Graph Neural Network Evaluation](/papers/1811.05868/) | 10 | 0 | 40 | Amazon-Computers, Amazon-Photo, CiteSeer, Coauthor-CS | GAT, GCN, MLP |
| [2402.00789](/papers/2402.00789/) | [Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective State Spaces](/papers/2402.00789/) | 10 | 7 | 38 | CIFAR10, CLUSTER, MNIST, PATTERN | Exphormer, GCN, GIN, GatedGCN |
| [2106.05234](/papers/2106.05234/) | [Do Transformers Really Perform Bad for Graph Representation?](/papers/2106.05234/) | 9 | 0 | 115 | PCQM4Mv2, ZINC | GAT, GCN, GIN, GatedGCN+LapPE |
| [2110.07875](/papers/2110.07875/) | [Graph Neural Networks with Learnable Structural and Positional Representations](/papers/2110.07875/) | 9 | 1 | 105 | ZINC, ogbg-molpcba | GAT, GCN, GIN, GIN-VN |
| [2405.13806](/papers/2405.13806/) | [A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition](/papers/2405.13806/) | 9 | 9 | 80 | Peptides-func, Peptides-struct, ogbn-arxiv | APPNP, GAT, GCN, GINE |
| [1905.05178](/papers/1905.05178/) | [Graph U-Nets](/papers/1905.05178/) | 9 | 1 | 48 | COLLAB, CiteSeer, Cora, PROTEINS | DeepWalk, DiffPool, GAT, GCN |
| [2001.05140](/papers/2001.05140/) | [Graph-Bert: Only Attention is Needed for Learning Graph Representations](/papers/2001.05140/) | 9 | 3 | 48 | CiteSeer, Cora, PubMed | DeepWalk, GAT, GCN, LP |
| [2110.09443](/papers/2110.09443/) | [Beltrami Flow and Neural Diffusion on Graphs](/papers/2110.09443/) | 9 | 0 | 48 | Amazon-Computers, CiteSeer, Coauthor-CS, Cora | CPGNN, GAT, GCN |
| [2205.07308](/papers/2205.07308/) | [Finding Global Homophily in Graph Neural Networks When Meeting Heterophily](/papers/2205.07308/) | 9 | 1 | 25 | Squirrel, ogbn-arxiv | APPNP, ChebNet, GAT, GCN |
| [2305.10498](/papers/2305.10498/) | [Edge Directionality Improves Learning on Heterophilic Graphs](/papers/2305.10498/) | 8 | 7 | 48 | Chameleon, Roman-empire, Squirrel, snap-patents | GCN, GloGNN, MLP |
| [1611.08402](/papers/1611.08402/) | [Geometric deep learning on graphs and manifolds using mixture model...](/papers/1611.08402/) | 8 | 0 | 47 | Cora, MNIST, PubMed | ChebNet, DGCNN, DeepWalk, GCN |
| [2103.09430](/papers/2103.09430/) | [OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs](/papers/2103.09430/) | 8 | 0 | 34 | ogbg-molpcba, ogbn-mag | DGN, GAT, GCN, GIN |
| [2206.08164](/papers/2206.08164/) | [Long Range Graph Benchmark](/papers/2206.08164/) | 7 | 0 | 80 | Peptides-func, Peptides-struct | GCN, GINE, GatedGCN, SAN+RWSE |
| [2306.02866](/papers/2306.02866/) | [Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance](/papers/2306.02866/) | 7 | 1 | 80 | Peptides-func, Peptides-struct | GCN, GINE, GatedGCN, SAN+RWSE |
| [1812.04202](/papers/1812.04202/) | [Deep Learning on Graphs: A Survey](/papers/1812.04202/) | 7 | 1 | 56 | Cora, PubMed | ChebNet, FastGCN, GAT, GCN |
| [2308.07134](/papers/2308.07134/) | [Language is All a Graph Needs](/papers/2308.07134/) | 7 | 5 | 55 | Cora, PubMed, ogbn-arxiv | DeeperGCN, GAT, GCN, GraphSAGE |
| [1806.08804](/papers/1806.08804/) | [Hierarchical Graph Representation Learning with Differentiable Pooling](/papers/1806.08804/) | 7 | 0 | 54 | COLLAB, D&D, ENZYMES, PROTEINS | DiffPool, GraphSAGE |
| [2507.00647](/papers/2507.00647/) | [Cooperative Sheaf Neural Networks](/papers/2507.00647/) | 7 | 6 | 45 | Chameleon, Cornell, Squirrel | GAT, GCN, GT, GT-sep |
| [2502.01122](/papers/2502.01122/) | [Learning Efficient Positional Encodings with Graph Neural Networks](/papers/2502.01122/) | 6 | 6 | 108 | Peptides-struct, REDDIT-BINARY, REDDIT-MULTI-5K, ZINC | GCN, GIN, GPS |
| [2310.18716](/papers/2310.18716/) | [Laplacian Canonization: A Minimalist Approach to Sign and Basis Invariant...](/papers/2310.18716/) | 6 | 3 | 105 | ZINC, ogbg-molpcba | GatedGCN, GatedGCN+LapPE, Graph-ViT, PNA |
| [2502.02379](/papers/2502.02379/) | [No Metric to Rule Them All: Toward Principled Evaluations of...](/papers/2502.02379/) | 6 | 6 | 75 | NCI1, PROTEINS | GAT, GCN, GIN |
| [2406.11714](/papers/2406.11714/) | [Scalable Expressiveness through Preprocessed Graph Perturbations](/papers/2406.11714/) | 6 | 6 | 37 | IMDB-MULTI, Tox21, ogbg-molhiv | GCN, GIN |
| [2602.17893](/papers/2602.17893/) | [COMBA: Cross Batch Aggregation for Learning Large Graphs with Context...](/papers/2602.17893/) | 6 | 6 | 31 | Amazon-ratings, Minesweeper, ogbn-arxiv, ogbn-products | Cluster-GCN, GCN, Graph-Mamba, NAGphormer |
| [2006.15646](/papers/2006.15646/) | [Expressive Power of Invariant and Equivariant Graph Neural Networks](/papers/2006.15646/) | 6 | 0 | 8 | ER graph | DGN, GAT, GCN, GIN |
| [1904.08082](/papers/1904.08082/) | [Self-Attention Graph Pooling](/papers/1904.08082/) | 5 | 3 | 58 | D&D, NCI1 | DiffPool, SAGPool, Set2Set, SortPool |
| [2302.08671](/papers/2302.08671/) | [Search to Capture Long-range Dependency with Stacking GNNs for Graph...](/papers/2302.08671/) | 5 | 2 | 40 | D&D, NCI1, PROTEINS | DiffPool, GCN, SAGPool |
| [1603.08861](/papers/1603.08861/) | [Revisiting Semi-Supervised Learning with Graph Embeddings](/papers/1603.08861/) | 5 | 0 | 16 | CiteSeer, Cora, PubMed | LP, Planetoid* |
| [2004.11198](/papers/2004.11198/) | [SIGN: Scalable Inception Graph Neural Networks](/papers/2004.11198/) | 5 | 3 | 5 | PPI, Reddit | Cluster-GCN, FastGCN, GCN, GraphSAGE |
| [2509.01254](/papers/2509.01254/) | [What Expressivity Theory Misses: Message Passing Complexity for GNNs](/papers/2509.01254/) | 4 | 4 | 116 | ZINC | GCN, GIN, GSN, GraphSAGE |
| [2006.15107](/papers/2006.15107/) | [Building powerful and equivariant graph neural networks with structural message-passing](/papers/2006.15107/) | 4 | 0 | 106 | ZINC | GIN, GatedGCN, MPNN, PNA |
| [2309.09384](/papers/2309.09384/) | [Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci Curvature](/papers/2309.09384/) | 4 | 3 | 52 | Cora, Cornell, MUTAG | GCN, GIN |
| [2106.07476](/papers/2106.07476/) | [Training Graph Neural Networks with 1000 Layers](/papers/2106.07476/) | 4 | 0 | 19 | ogbn-arxiv, ogbn-proteins | GCN, GraphSAGE |
| [2210.13148](/papers/2210.13148/) | [Transformers over Directed Acyclic Graphs](/papers/2210.13148/) | 3 | 0 | 27 | CiteSeer, Cora, MalNet-Tiny | GraphGPS, NodeFormer |
| [2009.03509](/papers/2009.03509/) | [Masked Label Prediction: Unified Message Passing Model for Semi-Supervised Classification](/papers/2009.03509/) | 3 | 0 | 24 | ogbn-arxiv, ogbn-proteins | DeeperGCN, JK-Net |
| [2110.13197](/papers/2110.13197/) | [Nested Graph Neural Networks](/papers/2110.13197/) | 3 | 3 | 12 | QM9 | 123-gnn, DTNN, MPNN |
| [2210.02997](/papers/2210.02997/) | [Expander Graph Propagation](/papers/2210.02997/) | 2 | 0 | 34 | ogbg-molhiv, ogbg-molpcba | GIN |
| [1902.07153](/papers/1902.07153/) | [Simplifying Graph Convolutional Networks](/papers/1902.07153/) | 2 | 0 | 31 | PubMed | GAT, GCN |
| [2511.03824](/papers/2511.03824/) | [Sketch-Augmented Features Improve Learning Long-Range Dependencies in Graph Neural Networks](/papers/2511.03824/) | 2 | 2 | 17 | Peptides-struct, REDDIT-MULTI-5K | GPS, SignNet-8S |
| [2402.07568](/papers/2402.07568/) | [--Leman at the margin: When more expressivity matters](/papers/2402.07568/) | 2 | 2 | 13 | ENZYMES, PROTEINS | 1-WL |
| [2006.06972](/papers/2006.06972/) | [Towards Deeper Graph Neural Networks with Differentiable Group Normalization](/papers/2006.06972/) | 2 | 0 | 6 | Coauthor-CS | GAT, GCN |
| [1703.06103](/papers/1703.06103/) | [Modeling Relational Data with Graph Convolutional Networks](/papers/1703.06103/) | 1 | 0 | 45 | MUTAG | WL |
| [1912.06058](/papers/1912.06058/) | [Coloring graph neural networks for node disambiguation](/papers/1912.06058/) | 1 | 1 | 11 | PROTEINS | DGCNN |
| [1905.07953](/papers/1905.07953/) | [Cluster-GCN: An Efficient Algorithm for Training Deep and Large Graph...](/papers/1905.07953/) | 1 | 1 | 1 | Reddit | GaAN |
>>>>>>> Stashed changes

### Flagged Rows

| ArXiv | Dataset | Model | Actual | Paper | Rank Shift | Actual Source | Timing |
|---|---|---|---:|---:|---:|---|---|
<<<<<<< Updated upstream
| [2506.04765](/papers/2506.04765/) | Peptides-struct | GCN | 0.2421 | 0.4347 | 330 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2602.02268](/papers/2602.02268/) | Peptides-struct | GCN | 0.2421 | 0.4347 | 330 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2512.15549](/papers/2512.15549/) | Peptides-struct | GCN | 0.2421 | 0.4077 | 329 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2310.05174](/papers/2310.05174/) | Peptides-struct | GCN | 0.2421 | 0.3566 | 314 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.05174](/papers/2310.05174/) | Peptides-struct | GIN | 0.2429 | 0.3647 | 313 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2506.04765](/papers/2506.04765/) | Peptides-func | GCN | 0.7261 | 0.3614 | 306 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2602.02268](/papers/2602.02268/) | Peptides-func | GCN | 0.7261 | 0.3614 | 306 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2309.16014](/papers/2309.16014/) | Peptides-struct | GCN | 0.2421 | 0.3500 | 303 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2306.05955](/papers/2306.05955/) | Peptides-struct | GIN | 0.2429 | 0.3547 | 302 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.01704](/papers/2310.01704/) | Peptides-struct | GIN | 0.2429 | 0.3547 | 302 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.03274](/papers/2310.03274/) | Peptides-struct | GIN | 0.2429 | 0.3547 | 302 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.07430](/papers/2310.07430/) | Peptides-struct | GIN | 0.2429 | 0.3547 | 302 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2402.08450](/papers/2402.08450/) | Peptides-struct | GIN | 0.2429 | 0.3547 | 302 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2402.08678](/papers/2402.08678/) | Peptides-struct | GIN | 0.2429 | 0.3547 | 302 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2502.00282](/papers/2502.00282/) | Peptides-struct | GIN | 0.2429 | 0.3547 | 302 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2102.08786](/papers/2102.08786/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 301 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2206.08164](/papers/2206.08164/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 301 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2306.02866](/papers/2306.02866/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 301 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2306.03561](/papers/2306.03561/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 301 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2306.05955](/papers/2306.05955/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 301 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2308.11129](/papers/2308.11129/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 301 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2309.04941](/papers/2309.04941/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 301 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.01668](/papers/2310.01668/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 301 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.01704](/papers/2310.01704/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 301 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.02156](/papers/2310.02156/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 301 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.03274](/papers/2310.03274/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 301 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.07430](/papers/2310.07430/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 301 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.19285](/papers/2310.19285/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 301 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2311.01276](/papers/2311.01276/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 301 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2312.16560](/papers/2312.16560/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 301 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2401.17791](/papers/2401.17791/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 301 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2402.08450](/papers/2402.08450/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 301 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2402.08678](/papers/2402.08678/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 301 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2404.03380](/papers/2404.03380/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 301 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2405.02795](/papers/2405.02795/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 301 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2405.03481](/papers/2405.03481/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 301 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2405.13526](/papers/2405.13526/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 301 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2405.13806](/papers/2405.13806/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 301 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2406.12059](/papers/2406.12059/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 301 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2407.12419](/papers/2407.12419/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 301 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2409.19117](/papers/2409.19117/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 301 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2410.13798](/papers/2410.13798/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 301 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2410.23686](/papers/2410.23686/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 301 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2412.01519](/papers/2412.01519/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 301 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2502.00282](/papers/2502.00282/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 301 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2508.05070](/papers/2508.05070/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 301 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2510.02565](/papers/2510.02565/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 301 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2601.19094](/papers/2601.19094/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 301 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2604.06336](/papers/2604.06336/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 301 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2605.06462](/papers/2605.06462/) | Peptides-struct | GCN | 0.2421 | 0.3496 | 301 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2512.15549](/papers/2512.15549/) | Peptides-func | GCN | 0.7261 | 0.4396 | 298 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2603.27529](/papers/2603.27529/) | Cora | DR | 0.9139 | 0.4435 | 297 | [Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks](/papers/2508.19071/) | already known (2025-08) |
| [2310.01668](/papers/2310.01668/) | Peptides-struct | GIN | 0.2429 | 0.3493 | 295 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2206.08164](/papers/2206.08164/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 285 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2306.02866](/papers/2306.02866/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 285 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2306.03561](/papers/2306.03561/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 285 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2306.05955](/papers/2306.05955/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 285 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2308.11129](/papers/2308.11129/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 285 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2309.04941](/papers/2309.04941/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 285 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.02156](/papers/2310.02156/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 285 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.03274](/papers/2310.03274/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 285 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.07430](/papers/2310.07430/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 285 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.19285](/papers/2310.19285/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 285 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2311.01276](/papers/2311.01276/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 285 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2311.04653](/papers/2311.04653/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 285 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2401.17791](/papers/2401.17791/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 285 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2402.08450](/papers/2402.08450/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 285 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2402.08678](/papers/2402.08678/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 285 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2404.03380](/papers/2404.03380/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 285 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2405.03481](/papers/2405.03481/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 285 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2405.13526](/papers/2405.13526/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 285 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2405.13806](/papers/2405.13806/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 285 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2406.12059](/papers/2406.12059/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 285 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2407.12419](/papers/2407.12419/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 285 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2409.19117](/papers/2409.19117/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 285 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2412.01519](/papers/2412.01519/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 285 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2502.00282](/papers/2502.00282/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 285 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2508.05070](/papers/2508.05070/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 285 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2510.02565](/papers/2510.02565/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 285 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2604.06336](/papers/2604.06336/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 285 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2605.06462](/papers/2605.06462/) | Peptides-struct | GatedGCN | 0.2431 | 0.3420 | 285 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2311.04653](/papers/2311.04653/) | Peptides-struct | GCN | 0.2421 | 0.3234 | 284 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2508.10651](/papers/2508.10651/) | Peptides-func | GCN | 0.7261 | 0.5410 | 282 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2102.08786](/papers/2102.08786/) | Peptides-struct | GatedGCN | 0.2431 | 0.3357 | 277 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2312.16560](/papers/2312.16560/) | Peptides-struct | GatedGCN | 0.2431 | 0.3357 | 277 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2405.02795](/papers/2405.02795/) | Peptides-struct | GatedGCN | 0.2431 | 0.3357 | 277 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2410.23686](/papers/2410.23686/) | Peptides-struct | GatedGCN | 0.2431 | 0.3357 | 277 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2506.04765](/papers/2506.04765/) | Cora | SpecFormer | 0.8857 | 0.4883 | 271 | [GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers](/papers/2411.17296/) | already known (2024-11-26) |
| [2602.02268](/papers/2602.02268/) | Cora | SpecFormer | 0.8857 | 0.4883 | 271 | [GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers](/papers/2411.17296/) | already known (2024-11-26) |
| [2310.05174](/papers/2310.05174/) | Peptides-func | GCN | 0.7261 | 0.5831 | 266 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2412.07188](/papers/2412.07188/) | Cora | GCNII | 0.8893 | 0.6054 | 264 | [Revisiting Heterophily For Graph Neural Networks](/papers/2210.07606/) | already known (2022-10) |
| [2409.19117](/papers/2409.19117/) | Peptides-struct | GINE | 0.2473 | 0.6346 | 259 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2412.07188](/papers/2412.07188/) | Cora | APPNP | 0.8800 | 0.5426 | 256 | [ParaFormer: A Generalized PageRank Graph Transformer for Graph...](/papers/2512.14619/) | published later (2025-12) |
| [2102.08786](/papers/2102.08786/) | Peptides-func | GCN | 0.7261 | 0.5930 | 252 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2206.08164](/papers/2206.08164/) | Peptides-func | GCN | 0.7261 | 0.5930 | 252 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2306.02866](/papers/2306.02866/) | Peptides-func | GCN | 0.7261 | 0.5930 | 252 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2306.03561](/papers/2306.03561/) | Peptides-func | GCN | 0.7261 | 0.5930 | 252 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2308.11129](/papers/2308.11129/) | Peptides-func | GCN | 0.7261 | 0.5930 | 252 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2309.04941](/papers/2309.04941/) | Peptides-func | GCN | 0.7261 | 0.5930 | 252 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2309.16014](/papers/2309.16014/) | Peptides-func | GCN | 0.7261 | 0.5930 | 252 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.01668](/papers/2310.01668/) | Peptides-func | GCN | 0.7261 | 0.5930 | 252 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.02156](/papers/2310.02156/) | Peptides-func | GCN | 0.7261 | 0.5930 | 252 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.03274](/papers/2310.03274/) | Peptides-func | GCN | 0.7261 | 0.5930 | 252 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.07430](/papers/2310.07430/) | Peptides-func | GCN | 0.7261 | 0.5930 | 252 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.19285](/papers/2310.19285/) | Peptides-func | GCN | 0.7261 | 0.5930 | 252 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2311.01276](/papers/2311.01276/) | Peptides-func | GCN | 0.7261 | 0.5930 | 252 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2311.04653](/papers/2311.04653/) | Peptides-func | GCN | 0.7261 | 0.5930 | 252 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2312.16560](/papers/2312.16560/) | Peptides-func | GCN | 0.7261 | 0.5930 | 252 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2401.17791](/papers/2401.17791/) | Peptides-func | GCN | 0.7261 | 0.5930 | 252 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2402.08450](/papers/2402.08450/) | Peptides-func | GCN | 0.7261 | 0.5930 | 252 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2402.08678](/papers/2402.08678/) | Peptides-func | GCN | 0.7261 | 0.5930 | 252 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2404.03380](/papers/2404.03380/) | Peptides-func | GCN | 0.7261 | 0.5930 | 252 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2404.09774](/papers/2404.09774/) | Peptides-func | GCN | 0.7261 | 0.5930 | 252 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2405.02795](/papers/2405.02795/) | Peptides-func | GCN | 0.7261 | 0.5930 | 252 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2405.03481](/papers/2405.03481/) | Peptides-func | GCN | 0.7261 | 0.5930 | 252 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2405.13806](/papers/2405.13806/) | Peptides-func | GCN | 0.7261 | 0.5930 | 252 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2406.12059](/papers/2406.12059/) | Peptides-func | GCN | 0.7261 | 0.5930 | 252 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2407.02758](/papers/2407.02758/) | Peptides-func | GCN | 0.7261 | 0.5930 | 252 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2407.12136](/papers/2407.12136/) | Peptides-func | GCN | 0.7261 | 0.5930 | 252 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2409.19117](/papers/2409.19117/) | Peptides-func | GCN | 0.7261 | 0.5930 | 252 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2410.13798](/papers/2410.13798/) | Peptides-func | GCN | 0.7261 | 0.5930 | 252 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2412.01519](/papers/2412.01519/) | Peptides-func | GCN | 0.7261 | 0.5930 | 252 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2502.00282](/papers/2502.00282/) | Peptides-func | GCN | 0.7261 | 0.5930 | 252 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2508.05070](/papers/2508.05070/) | Peptides-func | GCN | 0.7261 | 0.5930 | 252 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2510.02565](/papers/2510.02565/) | Peptides-func | GCN | 0.7261 | 0.5930 | 252 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2601.19094](/papers/2601.19094/) | Peptides-func | GCN | 0.7261 | 0.5930 | 252 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2604.06336](/papers/2604.06336/) | Peptides-func | GCN | 0.7261 | 0.5930 | 252 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2605.06462](/papers/2605.06462/) | Peptides-func | GCN | 0.7261 | 0.5930 | 252 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2412.07188](/papers/2412.07188/) | Cora | GAT | 0.8825 | 0.6033 | 251 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2310.03274](/papers/2310.03274/) | Peptides-func | GIN | 0.7059 | 0.5498 | 247 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.07430](/papers/2310.07430/) | Peptides-func | GIN | 0.7059 | 0.5498 | 247 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2402.08450](/papers/2402.08450/) | Peptides-func | GIN | 0.7059 | 0.5498 | 247 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2402.08678](/papers/2402.08678/) | Peptides-func | GIN | 0.7059 | 0.5498 | 247 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2502.00282](/papers/2502.00282/) | Peptides-func | GIN | 0.7059 | 0.5498 | 247 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2406.18380](/papers/2406.18380/) | Peptides-func | GIN | 0.7059 | 0.5501 | 246 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2506.04765](/papers/2506.04765/) | Peptides-func | GraphMLPMixer | 0.6970 | 0.4225 | 245 | [Graph as Point Set](/papers/2405.02795/) | already known (2024-05-05) |
| [2602.02268](/papers/2602.02268/) | Peptides-func | GraphMLPMixer | 0.6970 | 0.4225 | 245 | [Graph as Point Set](/papers/2405.02795/) | already known (2024-05-05) |
| [2506.04765](/papers/2506.04765/) | ZINC | GPS | 0.0238 | 0.1968 | 244 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2506.04765](/papers/2506.04765/) | ZINC | GPS | 0.0238 | 0.1968 | 244 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2602.02268](/papers/2602.02268/) | ZINC | GPS | 0.0238 | 0.1968 | 244 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2602.02268](/papers/2602.02268/) | ZINC | GPS | 0.0238 | 0.1968 | 244 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2405.13806](/papers/2405.13806/) | Cora | GAT | 0.8825 | 0.6447 | 243 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2410.13798](/papers/2410.13798/) | Cora | GAT | 0.8825 | 0.6447 | 243 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2501.18739](/papers/2501.18739/) | Cora | GAT | 0.8825 | 0.6447 | 243 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2410.13798](/papers/2410.13798/) | Cora | GPRGNN | 0.8857 | 0.6712 | 238 | [GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers](/papers/2411.17296/) | published later (2024-11-26) |
| [2501.18739](/papers/2501.18739/) | Cora | GPRGNN | 0.8857 | 0.6712 | 238 | [GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers](/papers/2411.17296/) | already known (2024-11-26) |
| [2506.04765](/papers/2506.04765/) | Peptides-func | GAT | 0.6924 | 0.3719 | 236 | [GEN: A Practical Alternative to Graph Transformers for...](/papers/2401.01233/) | already known (2024-01) |
| [2602.02268](/papers/2602.02268/) | Peptides-func | GAT | 0.6924 | 0.3719 | 236 | [GEN: A Practical Alternative to Graph Transformers for...](/papers/2401.01233/) | already known (2024-01) |
| [2310.01668](/papers/2310.01668/) | Peptides-func | GIN | 0.7059 | 0.5799 | 235 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2405.13806](/papers/2405.13806/) | Cora | APPNP | 0.8800 | 0.6516 | 234 | [ParaFormer: A Generalized PageRank Graph Transformer for Graph...](/papers/2512.14619/) | published later (2025-12) |
| [2410.13798](/papers/2410.13798/) | Cora | APPNP | 0.8800 | 0.6516 | 234 | [ParaFormer: A Generalized PageRank Graph Transformer for Graph...](/papers/2512.14619/) | published later (2025-12) |
| [2501.18739](/papers/2501.18739/) | Cora | APPNP | 0.8800 | 0.6516 | 234 | [ParaFormer: A Generalized PageRank Graph Transformer for Graph...](/papers/2512.14619/) | published later (2025-12) |
| [2102.08786](/papers/2102.08786/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 232 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2206.08164](/papers/2206.08164/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 232 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2306.02866](/papers/2306.02866/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 232 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2306.03561](/papers/2306.03561/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 232 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2308.11129](/papers/2308.11129/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 232 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2309.04941](/papers/2309.04941/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 232 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2310.02156](/papers/2310.02156/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 232 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2310.19285](/papers/2310.19285/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 232 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2311.01276](/papers/2311.01276/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 232 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2312.16560](/papers/2312.16560/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 232 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2401.17791](/papers/2401.17791/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 232 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2404.03380](/papers/2404.03380/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 232 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2405.02795](/papers/2405.02795/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 232 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2405.13526](/papers/2405.13526/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 232 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2405.13806](/papers/2405.13806/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 232 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2406.12059](/papers/2406.12059/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 232 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2407.12419](/papers/2407.12419/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 232 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2410.23686](/papers/2410.23686/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 232 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2412.01519](/papers/2412.01519/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 232 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2502.09365](/papers/2502.09365/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 232 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2508.05070](/papers/2508.05070/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 232 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2510.02565](/papers/2510.02565/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 232 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2604.06336](/papers/2604.06336/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 232 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | already known (2026-04) |
| [2605.06462](/papers/2605.06462/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 232 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | already known (2026-04) |
| [2309.04082](/papers/2309.04082/) | Cora | MLP | 0.8709 | 0.5244 | 231 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2405.13806](/papers/2405.13806/) | Cora | GCN | 0.8778 | 0.6176 | 231 | [Revisiting Heterophily For Graph Neural Networks](/papers/2210.07606/) | already known (2022-10) |
| [2410.13798](/papers/2410.13798/) | Cora | GCN | 0.8778 | 0.6176 | 231 | [Revisiting Heterophily For Graph Neural Networks](/papers/2210.07606/) | already known (2022-10) |
| [2501.18739](/papers/2501.18739/) | Cora | GCN | 0.8778 | 0.6176 | 231 | [Revisiting Heterophily For Graph Neural Networks](/papers/2210.07606/) | already known (2022-10) |
| [2412.07188](/papers/2412.07188/) | Cora | GCN | 0.8778 | 0.6217 | 231 | [Revisiting Heterophily For Graph Neural Networks](/papers/2210.07606/) | already known (2022-10) |
| [2306.05955](/papers/2306.05955/) | ZINC | AgentNet | 0.0400 | 0.2580 | 230 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2306.05955](/papers/2306.05955/) | ZINC | AgentNet | 0.0400 | 0.2580 | 230 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2410.05593](/papers/2410.05593/) | Cora | MLP | 0.8709 | 0.5510 | 229 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2310.05174](/papers/2310.05174/) | Peptides-func | GAT | 0.6924 | 0.4559 | 227 | [GEN: A Practical Alternative to Graph Transformers for...](/papers/2401.01233/) | published later (2024-01) |
| [2206.08164](/papers/2206.08164/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 224 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2306.02866](/papers/2306.02866/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 224 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2306.03561](/papers/2306.03561/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 224 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2307.07107](/papers/2307.07107/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 224 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2308.11129](/papers/2308.11129/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 224 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2309.04941](/papers/2309.04941/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 224 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.02156](/papers/2310.02156/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 224 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.03274](/papers/2310.03274/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 224 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.07430](/papers/2310.07430/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 224 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.19285](/papers/2310.19285/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 224 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2311.01276](/papers/2311.01276/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 224 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2311.04653](/papers/2311.04653/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 224 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2401.17791](/papers/2401.17791/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 224 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2402.08450](/papers/2402.08450/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 224 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2402.08678](/papers/2402.08678/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 224 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2404.03380](/papers/2404.03380/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 224 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2404.09774](/papers/2404.09774/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 224 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2405.03481](/papers/2405.03481/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 224 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2405.13806](/papers/2405.13806/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 224 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2406.12059](/papers/2406.12059/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 224 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2407.02758](/papers/2407.02758/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 224 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2407.12136](/papers/2407.12136/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 224 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2409.19117](/papers/2409.19117/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 224 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2412.01519](/papers/2412.01519/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 224 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2502.00282](/papers/2502.00282/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 224 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2508.05070](/papers/2508.05070/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 224 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2510.02565](/papers/2510.02565/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 224 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2604.06336](/papers/2604.06336/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 224 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2605.06462](/papers/2605.06462/) | Peptides-func | GatedGCN | 0.7006 | 0.5864 | 224 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2506.14098](/papers/2506.14098/) | Cora | MLP | 0.8709 | 0.5803 | 222 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2310.05174](/papers/2310.05174/) | Cora | MLP | 0.8709 | 0.5855 | 222 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2310.19285](/papers/2310.19285/) | ZINC | GRIT | 0.0230 | 0.1490 | 222 | [Enhancing Graph Neural Networks with Quantum Computed Encodings](/papers/2310.20519/) | already known (2023-10) |
| [2310.19285](/papers/2310.19285/) | ZINC | GRIT | 0.0230 | 0.1490 | 222 | [Enhancing Graph Neural Networks with Quantum Computed Encodings](/papers/2310.20519/) | already known (2023-10) |
| [2505.15405](/papers/2505.15405/) | ZINC | GIN | 0.0650 | 0.5700 | 221 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2505.15405](/papers/2505.15405/) | ZINC | GIN | 0.0650 | 0.5700 | 221 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2310.02156](/papers/2310.02156/) | Peptides-struct | GatedGCN+LapPE | 0.2466 | 0.3357 | 221 | [Non-backtracking Graph Neural Networks](/papers/2310.07430/) | already known (2023-10) |
| [2508.10651](/papers/2508.10651/) | Peptides-func | GIN | 0.7059 | 0.5940 | 219 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2509.01254](/papers/2509.01254/) | ZINC | GIN | 0.0650 | 0.5300 | 218 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2509.01254](/papers/2509.01254/) | ZINC | GIN | 0.0650 | 0.5300 | 218 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2102.08786](/papers/2102.08786/) | ZINC | GIN | 0.0650 | 0.5260 | 218 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2308.11129](/papers/2308.11129/) | ZINC | GIN | 0.0650 | 0.5260 | 218 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2308.11129](/papers/2308.11129/) | ZINC | GIN | 0.0650 | 0.5260 | 218 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.19285](/papers/2310.19285/) | ZINC | GIN | 0.0650 | 0.5260 | 218 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.19285](/papers/2310.19285/) | ZINC | GIN | 0.0650 | 0.5260 | 218 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2401.17791](/papers/2401.17791/) | ZINC | GIN | 0.0650 | 0.5260 | 218 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2401.17791](/papers/2401.17791/) | ZINC | GIN | 0.0650 | 0.5260 | 218 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2406.03386](/papers/2406.03386/) | ZINC | GIN | 0.0650 | 0.5260 | 218 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2406.03386](/papers/2406.03386/) | ZINC | GIN | 0.0650 | 0.5260 | 218 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2407.05649](/papers/2407.05649/) | ZINC | GIN | 0.0650 | 0.5260 | 218 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2407.05649](/papers/2407.05649/) | ZINC | GIN | 0.0650 | 0.5260 | 218 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2409.19117](/papers/2409.19117/) | ZINC | GIN | 0.0650 | 0.5260 | 218 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2409.19117](/papers/2409.19117/) | ZINC | GIN | 0.0650 | 0.5260 | 218 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2501.18739](/papers/2501.18739/) | ZINC | GIN | 0.0650 | 0.5260 | 218 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2502.00282](/papers/2502.00282/) | ZINC | GIN | 0.0650 | 0.5260 | 218 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2502.00282](/papers/2502.00282/) | ZINC | GIN | 0.0650 | 0.5260 | 218 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2502.09365](/papers/2502.09365/) | ZINC | GIN | 0.0650 | 0.5260 | 218 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2502.09365](/papers/2502.09365/) | ZINC | GIN | 0.0650 | 0.5260 | 218 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2504.12588](/papers/2504.12588/) | ZINC | GIN | 0.0650 | 0.5260 | 218 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2508.05070](/papers/2508.05070/) | ZINC | GIN | 0.0650 | 0.5260 | 218 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2508.05070](/papers/2508.05070/) | ZINC | GIN | 0.0650 | 0.5260 | 218 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2605.05689](/papers/2605.05689/) | ZINC | GIN | 0.0650 | 0.5260 | 218 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2605.05689](/papers/2605.05689/) | ZINC | GIN | 0.0650 | 0.5260 | 218 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2410.05697](/papers/2410.05697/) | Cora | MLP | 0.8709 | 0.5941 | 218 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2501.18739](/papers/2501.18739/) | Cora | NodeFormer | 0.8870 | 0.7101 | 218 | [ParaFormer: A Generalized PageRank Graph Transformer for Graph...](/papers/2512.14619/) | published later (2025-12) |
| [2210.07606](/papers/2210.07606/) | Cora | MixHop | 0.8761 | 0.6565 | 217 | [Algorithmic Graph Tasks](/papers/2312.16560/) | published later (2023-12) |
| [2506.04765](/papers/2506.04765/) | Cora | NodeFormer | 0.8870 | 0.7103 | 217 | [ParaFormer: A Generalized PageRank Graph Transformer for Graph...](/papers/2512.14619/) | published later (2025-12) |
| [2602.02268](/papers/2602.02268/) | Cora | NodeFormer | 0.8870 | 0.7103 | 217 | [ParaFormer: A Generalized PageRank Graph Transformer for Graph...](/papers/2512.14619/) | already known (2025-12) |
| [2406.18380](/papers/2406.18380/) | ZINC | GIN | 0.0650 | 0.4131 | 215 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2406.18380](/papers/2406.18380/) | ZINC | GIN | 0.0650 | 0.4131 | 215 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.05174](/papers/2310.05174/) | Peptides-struct | GAT | 0.2488 | 0.4375 | 215 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2310.01704](/papers/2310.01704/) | ZINC | GIN | 0.0650 | 0.4080 | 214 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.01704](/papers/2310.01704/) | ZINC | GIN | 0.0650 | 0.4080 | 214 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2506.14098](/papers/2506.14098/) | ogbg-molhiv | GCN | 0.9681 | 0.6484 | 214 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2506.14098](/papers/2506.14098/) | ogbg-molhiv | MLP | 0.9685 | 0.6637 | 214 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2506.14098](/papers/2506.14098/) | ogbg-molhiv | GAT | 0.9682 | 0.6554 | 213 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2506.04765](/papers/2506.04765/) | Peptides-struct | GAT | 0.2488 | 0.4231 | 212 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2602.02268](/papers/2602.02268/) | Peptides-struct | GAT | 0.2488 | 0.4231 | 212 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2306.05955](/papers/2306.05955/) | ZINC | GIN | 0.0650 | 0.3870 | 211 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2306.05955](/papers/2306.05955/) | ZINC | GIN | 0.0650 | 0.3870 | 211 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2312.01538](/papers/2312.01538/) | ZINC | GIN | 0.0650 | 0.3870 | 211 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2312.01538](/papers/2312.01538/) | ZINC | GIN | 0.0650 | 0.3870 | 211 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2506.14098](/papers/2506.14098/) | ogbg-molhiv | GIN | 0.9680 | 0.6686 | 211 | [No Metric to Rule Them All: Toward Principled...](/papers/2502.02379/) | already known (2025-02-04) |
| [2506.04765](/papers/2506.04765/) | ogbg-molhiv | GCN | 0.9681 | 0.6888 | 210 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2602.02268](/papers/2602.02268/) | ogbg-molhiv | GCN | 0.9681 | 0.6888 | 210 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | already known (2025-11) |
| [2501.18739](/papers/2501.18739/) | Cora | SGFormer | 0.8810 | 0.6970 | 209 | [ParaFormer: A Generalized PageRank Graph Transformer for Graph...](/papers/2512.14619/) | published later (2025-12) |
| [2602.02268](/papers/2602.02268/) | CiteSeer | SpecFormer | 0.8149 | 0.4540 | 206 | [GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers](/papers/2411.17296/) | already known (2024-11-26) |
| [2308.11129](/papers/2308.11129/) | ZINC | PNA | 0.0573 | 0.1880 | 204 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | published later (2024-02) |
| [2308.11129](/papers/2308.11129/) | ZINC | PNA | 0.0573 | 0.1880 | 204 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | published later (2024-02) |
| [2309.04941](/papers/2309.04941/) | ZINC | PNA | 0.0573 | 0.1880 | 204 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | published later (2024-02) |
| [2310.19285](/papers/2310.19285/) | ZINC | PNA | 0.0573 | 0.1880 | 204 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | published later (2024-02) |
| [2310.19285](/papers/2310.19285/) | ZINC | PNA | 0.0573 | 0.1880 | 204 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | published later (2024-02) |
| [2312.01538](/papers/2312.01538/) | ZINC | PNA | 0.0573 | 0.1880 | 204 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | published later (2024-02) |
| [2312.01538](/papers/2312.01538/) | ZINC | PNA | 0.0573 | 0.1880 | 204 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | published later (2024-02) |
| [2401.17791](/papers/2401.17791/) | ZINC | PNA | 0.0573 | 0.1880 | 204 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | published later (2024-02) |
| [2401.17791](/papers/2401.17791/) | ZINC | PNA | 0.0573 | 0.1880 | 204 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | published later (2024-02) |
| [2404.03380](/papers/2404.03380/) | ZINC | PNA | 0.0573 | 0.1880 | 204 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2404.03380](/papers/2404.03380/) | ZINC | PNA | 0.0573 | 0.1880 | 204 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2407.05649](/papers/2407.05649/) | ZINC | PNA | 0.0573 | 0.1880 | 204 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2407.05649](/papers/2407.05649/) | ZINC | PNA | 0.0573 | 0.1880 | 204 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2410.09737](/papers/2410.09737/) | ZINC | PNA | 0.0573 | 0.1880 | 204 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2410.09737](/papers/2410.09737/) | ZINC | PNA | 0.0573 | 0.1880 | 204 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2504.12588](/papers/2504.12588/) | ZINC | PNA | 0.0573 | 0.1880 | 204 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2508.05070](/papers/2508.05070/) | ZINC | PNA | 0.0573 | 0.1880 | 204 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2508.05070](/papers/2508.05070/) | ZINC | PNA | 0.0573 | 0.1880 | 204 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2604.17324](/papers/2604.17324/) | ZINC | PNA | 0.0573 | 0.1880 | 204 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2604.17324](/papers/2604.17324/) | ZINC | PNA | 0.0573 | 0.1880 | 204 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2605.05689](/papers/2605.05689/) | ZINC | PNA | 0.0573 | 0.1880 | 204 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2605.05689](/papers/2605.05689/) | ZINC | PNA | 0.0573 | 0.1880 | 204 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2405.02795](/papers/2405.02795/) | ZINC | PSDS | 0.0490 | 0.1620 | 203 | [Graph as Point Set](/papers/2405.02795/) | same paper |
| [2412.07188](/papers/2412.07188/) | Cora | SGC | 0.8660 | 0.6109 | 202 | [ParaFormer: A Generalized PageRank Graph Transformer for Graph...](/papers/2512.14619/) | published later (2025-12) |
| [2410.13798](/papers/2410.13798/) | Cora | Nagphormer | 0.8820 | 0.7151 | 200 | [ParaFormer: A Generalized PageRank Graph Transformer for Graph...](/papers/2512.14619/) | published later (2025-12) |
| [2501.18739](/papers/2501.18739/) | Cora | Nagphormer | 0.8820 | 0.7151 | 200 | [ParaFormer: A Generalized PageRank Graph Transformer for Graph...](/papers/2512.14619/) | published later (2025-12) |
| [2310.01668](/papers/2310.01668/) | Peptides-func | GAT | 0.6924 | 0.5800 | 198 | [GEN: A Practical Alternative to Graph Transformers for...](/papers/2401.01233/) | published later (2024-01) |
| [2506.04765](/papers/2506.04765/) | ZINC | Graphormer | 0.0250 | 0.1305 | 198 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | already known (2025-01-30) |
| [2506.04765](/papers/2506.04765/) | ZINC | Graphormer | 0.0250 | 0.1305 | 198 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | already known (2025-01-30) |
| [2602.02268](/papers/2602.02268/) | ZINC | Graphormer | 0.0250 | 0.1305 | 198 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | already known (2025-01-30) |
| [2602.02268](/papers/2602.02268/) | ZINC | Graphormer | 0.0250 | 0.1305 | 198 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | already known (2025-01-30) |
| [2601.07419](/papers/2601.07419/) | Peptides-func | GIN | 0.7059 | 0.6070 | 198 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2310.05174](/papers/2310.05174/) | Peptides-func | GIN | 0.7059 | 0.6092 | 197 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2508.10651](/papers/2508.10651/) | ogbg-molhiv | GCN | 0.9681 | 0.7370 | 195 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2506.04765](/papers/2506.04765/) | ogbg-molhiv | GAT | 0.9682 | 0.7385 | 195 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2602.02268](/papers/2602.02268/) | ogbg-molhiv | GAT | 0.9682 | 0.7385 | 195 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | already known (2025-11) |
| [2310.02156](/papers/2310.02156/) | Peptides-struct | GatedGCN+GPSE | 0.2477 | 0.3357 | 195 | [Understanding Virtual Nodes: Oversquashing and Node Heterogeneity](/papers/2405.13526/) | published later (2024-05) |
| [2508.10651](/papers/2508.10651/) | ogbg-molhiv | GIN | 0.9680 | 0.7370 | 194 | [No Metric to Rule Them All: Toward Principled...](/papers/2502.02379/) | already known (2025-02-04) |
| [2102.08786](/papers/2102.08786/) | ZINC | HIMP | 0.0360 | 0.1510 | 194 | [Distance-Restricted Folklore Weisfeiler-Leman GNNs with Provable Cycle Counting...](/papers/2309.04941/) | published later (2023-09) |
| [2309.04941](/papers/2309.04941/) | ZINC | HIMP | 0.0360 | 0.1510 | 194 | [Distance-Restricted Folklore Weisfeiler-Leman GNNs with Provable Cycle Counting...](/papers/2309.04941/) | same paper |
| [2310.01704](/papers/2310.01704/) | ZINC | HIMP | 0.0360 | 0.1510 | 194 | [Distance-Restricted Folklore Weisfeiler-Leman GNNs with Provable Cycle Counting...](/papers/2309.04941/) | already known (2023-09) |
| [2310.01704](/papers/2310.01704/) | ZINC | HIMP | 0.0360 | 0.1510 | 194 | [Distance-Restricted Folklore Weisfeiler-Leman GNNs with Provable Cycle Counting...](/papers/2309.04941/) | already known (2023-09) |
| [2312.04234](/papers/2312.04234/) | ZINC | Graphormer | 0.0250 | 0.1240 | 194 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2312.04234](/papers/2312.04234/) | ZINC | Graphormer | 0.0250 | 0.1240 | 194 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2501.18739](/papers/2501.18739/) | ZINC | AgentNet | 0.0400 | 0.1440 | 192 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | same paper |
| [2306.05955](/papers/2306.05955/) | ZINC | Graphormer | 0.0250 | 0.1220 | 192 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2306.05955](/papers/2306.05955/) | ZINC | Graphormer | 0.0250 | 0.1220 | 192 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2310.01704](/papers/2310.01704/) | ZINC | Graphormer | 0.0250 | 0.1220 | 192 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2310.01704](/papers/2310.01704/) | ZINC | Graphormer | 0.0250 | 0.1220 | 192 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2310.19285](/papers/2310.19285/) | ZINC | Graphormer | 0.0250 | 0.1220 | 192 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2310.19285](/papers/2310.19285/) | ZINC | Graphormer | 0.0250 | 0.1220 | 192 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2312.01538](/papers/2312.01538/) | ZINC | Graphormer | 0.0250 | 0.1220 | 192 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2312.01538](/papers/2312.01538/) | ZINC | Graphormer | 0.0250 | 0.1220 | 192 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2401.17791](/papers/2401.17791/) | ZINC | Graphormer | 0.0250 | 0.1220 | 192 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2401.17791](/papers/2401.17791/) | ZINC | Graphormer | 0.0250 | 0.1220 | 192 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2402.08450](/papers/2402.08450/) | ZINC | Graphormer | 0.0250 | 0.1220 | 192 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2404.03380](/papers/2404.03380/) | ZINC | Graphormer | 0.0250 | 0.1220 | 192 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2404.03380](/papers/2404.03380/) | ZINC | Graphormer | 0.0250 | 0.1220 | 192 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2405.02795](/papers/2405.02795/) | ZINC | Graphormer | 0.0250 | 0.1220 | 192 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2406.03386](/papers/2406.03386/) | ZINC | Graphormer | 0.0250 | 0.1220 | 192 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2406.03386](/papers/2406.03386/) | ZINC | Graphormer | 0.0250 | 0.1220 | 192 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2407.05649](/papers/2407.05649/) | ZINC | Graphormer | 0.0250 | 0.1220 | 192 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2407.05649](/papers/2407.05649/) | ZINC | Graphormer | 0.0250 | 0.1220 | 192 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2410.09737](/papers/2410.09737/) | ZINC | Graphormer | 0.0250 | 0.1220 | 192 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2410.09737](/papers/2410.09737/) | ZINC | Graphormer | 0.0250 | 0.1220 | 192 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2501.18739](/papers/2501.18739/) | ZINC | Graphormer | 0.0250 | 0.1220 | 192 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | same paper |
| [2502.09263](/papers/2502.09263/) | ZINC | Graphormer | 0.0250 | 0.1220 | 192 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | already known (2025-01-30) |
| [2502.09263](/papers/2502.09263/) | ZINC | Graphormer | 0.0250 | 0.1220 | 192 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | already known (2025-01-30) |
| [2502.09365](/papers/2502.09365/) | ZINC | Graphormer | 0.0250 | 0.1220 | 192 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | already known (2025-01-30) |
| [2502.09365](/papers/2502.09365/) | ZINC | Graphormer | 0.0250 | 0.1220 | 192 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | already known (2025-01-30) |
| [2504.12588](/papers/2504.12588/) | ZINC | Graphormer | 0.0250 | 0.1220 | 192 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | already known (2025-01-30) |
| [2604.17324](/papers/2604.17324/) | ZINC | Graphormer | 0.0250 | 0.1220 | 192 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | already known (2025-01-30) |
| [2604.17324](/papers/2604.17324/) | ZINC | Graphormer | 0.0250 | 0.1220 | 192 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | already known (2025-01-30) |
| [2506.04765](/papers/2506.04765/) | Cora | CoBFormer | 0.8820 | 0.7243 | 190 | [ParaFormer: A Generalized PageRank Graph Transformer for Graph...](/papers/2512.14619/) | published later (2025-12) |
| [2602.02268](/papers/2602.02268/) | Cora | CoBFormer | 0.8820 | 0.7243 | 190 | [ParaFormer: A Generalized PageRank Graph Transformer for Graph...](/papers/2512.14619/) | already known (2025-12) |
| [2102.08786](/papers/2102.08786/) | Peptides-func | GatedGCN | 0.7006 | 0.6069 | 190 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2312.16560](/papers/2312.16560/) | Peptides-func | GatedGCN | 0.7006 | 0.6069 | 190 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2405.02795](/papers/2405.02795/) | Peptides-func | GatedGCN | 0.7006 | 0.6069 | 190 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2405.03481](/papers/2405.03481/) | ZINC | Graphormer | 0.0250 | 0.1200 | 188 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2405.03481](/papers/2405.03481/) | ZINC | Graphormer | 0.0250 | 0.1200 | 188 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2310.01668](/papers/2310.01668/) | Peptides-struct | GAT | 0.2488 | 0.3506 | 187 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2506.04765](/papers/2506.04765/) | Peptides-struct | GraphMLPMixer | 0.2475 | 0.3065 | 187 | [Range-aware Positional Encoding via High-order Pretraining: Theory and...](/papers/2409.19117/) | already known (2024-09) |
| [2602.02268](/papers/2602.02268/) | Peptides-struct | GraphMLPMixer | 0.2475 | 0.3065 | 187 | [Range-aware Positional Encoding via High-order Pretraining: Theory and...](/papers/2409.19117/) | already known (2024-09) |
| [2310.03274](/papers/2310.03274/) | ogbg-molhiv | GCN | 0.9681 | 0.7460 | 186 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2502.01122](/papers/2502.01122/) | ZINC | GIN | 0.0650 | 0.2090 | 186 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2502.01122](/papers/2502.01122/) | ZINC | GIN | 0.0650 | 0.2090 | 186 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2506.04765](/papers/2506.04765/) | Peptides-struct | Exphormer | 0.2481 | 0.3297 | 186 | [Invariant-Based Diagnostics for Graph Benchmarks](/papers/2605.06462/) | published later (2026-05) |
| [2602.02268](/papers/2602.02268/) | Peptides-struct | Exphormer | 0.2481 | 0.3297 | 186 | [Invariant-Based Diagnostics for Graph Benchmarks](/papers/2605.06462/) | published later (2026-05) |
| [2310.19285](/papers/2310.19285/) | ZINC | GPS | 0.0238 | 0.1130 | 185 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | published later (2024-02) |
| [2310.19285](/papers/2310.19285/) | ZINC | GPS | 0.0238 | 0.1130 | 185 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | published later (2024-02) |
| [2506.04765](/papers/2506.04765/) | Cora | GCN | 0.8778 | 0.7180 | 184 | [Revisiting Heterophily For Graph Neural Networks](/papers/2210.07606/) | already known (2022-10) |
| [2602.02268](/papers/2602.02268/) | Cora | GCN | 0.8778 | 0.7180 | 184 | [Revisiting Heterophily For Graph Neural Networks](/papers/2210.07606/) | already known (2022-10) |
| [2506.04765](/papers/2506.04765/) | Peptides-struct | Graph transformer | 0.2509 | 0.4345 | 183 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2602.02268](/papers/2602.02268/) | Peptides-struct | Graph transformer | 0.2509 | 0.4345 | 183 | [k-Maximum Inner Product Attention for Graph Transformers and...](/papers/2604.03815/) | published later (2026-04) |
| [2308.11129](/papers/2308.11129/) | ZINC | GT + HDSE | 0.0590 | 0.1590 | 183 | [Enhancing Graph Transformers with Hierarchical Distance Structural Encoding](/papers/2308.11129/) | same paper |
| [2310.02156](/papers/2310.02156/) | Peptides-func | GatedGCN+LapPE | 0.6982 | 0.6069 | 183 | [Non-backtracking Graph Neural Networks](/papers/2310.07430/) | already known (2023-10) |
| [2406.18380](/papers/2406.18380/) | CiteSeer | GIN | 0.7932 | 0.4798 | 182 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2102.08786](/papers/2102.08786/) | ZINC | PNA | 0.0573 | 0.1420 | 182 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | published later (2024-02) |
| [2501.18739](/papers/2501.18739/) | ZINC | PNA | 0.0573 | 0.1420 | 182 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2410.13798](/papers/2410.13798/) | Cora | GraphGPS | 0.8387 | 0.5576 | 179 | [GEN: A Practical Alternative to Graph Transformers for...](/papers/2401.01233/) | already known (2024-01) |
| [2501.18739](/papers/2501.18739/) | Cora | GraphGPS | 0.8387 | 0.5576 | 179 | [GEN: A Practical Alternative to Graph Transformers for...](/papers/2401.01233/) | already known (2024-01) |
| [2506.04765](/papers/2506.04765/) | ZINC | Exphormer | 0.0660 | 0.1905 | 177 | [SigGate-GT: Taming Over-Smoothing in Graph Transformers via Sigmoid-Gated...](/papers/2604.17324/) | published later (2026-04) |
| [2506.04765](/papers/2506.04765/) | ZINC | Exphormer | 0.0660 | 0.1905 | 177 | [SigGate-GT: Taming Over-Smoothing in Graph Transformers via Sigmoid-Gated...](/papers/2604.17324/) | published later (2026-04) |
| [2602.02268](/papers/2602.02268/) | ZINC | Exphormer | 0.0660 | 0.1905 | 177 | [SigGate-GT: Taming Over-Smoothing in Graph Transformers via Sigmoid-Gated...](/papers/2604.17324/) | published later (2026-04) |
| [2602.02268](/papers/2602.02268/) | ZINC | Exphormer | 0.0660 | 0.1905 | 177 | [SigGate-GT: Taming Over-Smoothing in Graph Transformers via Sigmoid-Gated...](/papers/2604.17324/) | published later (2026-04) |
| [2410.05697](/papers/2410.05697/) | CiteSeer | MLP | 0.7939 | 0.5826 | 175 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2602.02268](/papers/2602.02268/) | CiteSeer | NodeFormer | 0.7956 | 0.5903 | 175 | [GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers](/papers/2411.17296/) | already known (2024-11-26) |
| [2602.02268](/papers/2602.02268/) | CiteSeer | GCN | 0.8139 | 0.6173 | 175 | [Revisiting Heterophily For Graph Neural Networks](/papers/2210.07606/) | already known (2022-10) |
| [2601.07419](/papers/2601.07419/) | Cora | GCNII | 0.8893 | 0.7630 | 173 | [Revisiting Heterophily For Graph Neural Networks](/papers/2210.07606/) | already known (2022-10) |
| [2410.05593](/papers/2410.05593/) | CiteSeer | MLP | 0.7939 | 0.5910 | 172 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2310.05174](/papers/2310.05174/) | CiteSeer | MLP | 0.7939 | 0.5952 | 172 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2406.18380](/papers/2406.18380/) | CiteSeer | GAT | 0.8052 | 0.6091 | 171 | [GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers](/papers/2411.17296/) | published later (2024-11-26) |
| [2506.04765](/papers/2506.04765/) | Cora | GAT | 0.8825 | 0.7460 | 171 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2602.02268](/papers/2602.02268/) | Cora | GAT | 0.8825 | 0.7460 | 171 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | already known (2025-11) |
| [2309.04941](/papers/2309.04941/) | ZINC | GIN | 0.0650 | 0.1630 | 171 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2402.08450](/papers/2402.08450/) | ZINC | GIN | 0.0650 | 0.1630 | 171 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2402.08450](/papers/2402.08450/) | ZINC | GIN | 0.0650 | 0.1630 | 171 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2405.02795](/papers/2405.02795/) | ZINC | GIN | 0.0650 | 0.1630 | 171 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2406.09291](/papers/2406.09291/) | ZINC | GIN | 0.0650 | 0.1630 | 171 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2406.09291](/papers/2406.09291/) | ZINC | GIN | 0.0650 | 0.1630 | 171 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2410.09737](/papers/2410.09737/) | ZINC | GIN | 0.0650 | 0.1630 | 171 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2410.09737](/papers/2410.09737/) | ZINC | GIN | 0.0650 | 0.1630 | 171 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2501.03113](/papers/2501.03113/) | ZINC | GIN | 0.0650 | 0.1630 | 171 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2501.03113](/papers/2501.03113/) | ZINC | GIN | 0.0650 | 0.1630 | 171 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2602.02268](/papers/2602.02268/) | CiteSeer | GAT | 0.8052 | 0.6123 | 170 | [GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers](/papers/2411.17296/) | already known (2024-11-26) |
| [2406.18380](/papers/2406.18380/) | PROTEINS | GAT | 0.7634 | 0.5978 | 170 | [HOPSE: Scalable Higher-Order Positional and Structural Encoder for...](/papers/2505.15405/) | published later (2025-05) |
| [2402.08450](/papers/2402.08450/) | ZINC | NGNN | 0.0290 | 0.1110 | 170 | [Graph as Point Set](/papers/2405.02795/) | published later (2024-05-05) |
| [2405.02795](/papers/2405.02795/) | ZINC | NGNN | 0.0290 | 0.1110 | 170 | [Graph as Point Set](/papers/2405.02795/) | same paper |
| [2406.09291](/papers/2406.09291/) | ZINC | NGNN | 0.0290 | 0.1110 | 170 | [Graph as Point Set](/papers/2405.02795/) | already known (2024-05-05) |
| [2406.09291](/papers/2406.09291/) | ZINC | NGNN | 0.0290 | 0.1110 | 170 | [Graph as Point Set](/papers/2405.02795/) | already known (2024-05-05) |
| [2505.15405](/papers/2505.15405/) | ZINC | GCN | 0.0760 | 0.6200 | 168 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2505.15405](/papers/2505.15405/) | ZINC | GCN | 0.0760 | 0.6200 | 168 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2506.04765](/papers/2506.04765/) | ZINC | GCN | 0.0760 | 0.6090 | 168 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2506.04765](/papers/2506.04765/) | ZINC | GCN | 0.0760 | 0.6090 | 168 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2602.02268](/papers/2602.02268/) | ZINC | GCN | 0.0760 | 0.6090 | 168 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2602.02268](/papers/2602.02268/) | ZINC | GCN | 0.0760 | 0.6090 | 168 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2306.05955](/papers/2306.05955/) | ogbg-molhiv | GIN | 0.9680 | 0.7558 | 168 | [No Metric to Rule Them All: Toward Principled...](/papers/2502.02379/) | published later (2025-02-04) |
| [2402.08450](/papers/2402.08450/) | ogbg-molhiv | GIN | 0.9680 | 0.7558 | 168 | [No Metric to Rule Them All: Toward Principled...](/papers/2502.02379/) | published later (2025-02-04) |
| [2405.13526](/papers/2405.13526/) | ogbg-molhiv | GIN | 0.9680 | 0.7558 | 168 | [No Metric to Rule Them All: Toward Principled...](/papers/2502.02379/) | published later (2025-02-04) |
| [2501.03113](/papers/2501.03113/) | ogbg-molhiv | GIN | 0.9680 | 0.7558 | 168 | [No Metric to Rule Them All: Toward Principled...](/papers/2502.02379/) | published later (2025-02-04) |
| [2502.02379](/papers/2502.02379/) | PROTEINS | GAT | 0.7634 | 0.6120 | 168 | [HOPSE: Scalable Higher-Order Positional and Structural Encoder for...](/papers/2505.15405/) | published later (2025-05) |
| [2309.04941](/papers/2309.04941/) | ZINC | Nested-GNN | 0.0290 | 0.1110 | 167 | [Distance-Restricted Folklore Weisfeiler-Leman GNNs with Provable Cycle Counting...](/papers/2309.04941/) | same paper |
| [2410.03424](/papers/2410.03424/) | ogbg-molhiv | GCN | 0.9681 | 0.7566 | 166 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2502.02379](/papers/2502.02379/) | PROTEINS | GIN | 0.7620 | 0.6090 | 166 | [Probabilistic Graph Rewiring via Virtual Nodes](/papers/2405.17311/) | already known (2024-05) |
| [2312.16560](/papers/2312.16560/) | Peptides-struct | GRED | 0.2455 | 0.2584 | 166 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.01704](/papers/2310.01704/) | ogbg-molhiv | GIN | 0.9680 | 0.7560 | 165 | [No Metric to Rule Them All: Toward Principled...](/papers/2502.02379/) | published later (2025-02-04) |
| [2404.09774](/papers/2404.09774/) | ogbg-molhiv | GCN | 0.9681 | 0.7599 | 163 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2502.00282](/papers/2502.00282/) | ogbg-molhiv | GCN | 0.9681 | 0.7599 | 163 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2502.01122](/papers/2502.01122/) | ZINC | GCN | 0.0760 | 0.4690 | 162 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2502.01122](/papers/2502.01122/) | ZINC | GCN | 0.0760 | 0.4690 | 162 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2502.02379](/papers/2502.02379/) | PROTEINS | GCN | 0.7600 | 0.5930 | 162 | [On the Stability of Multiset and Graph Neural...](/papers/2406.06984/) | already known (2024-06) |
| [2306.05955](/papers/2306.05955/) | ZINC | GatedGCN | 0.0770 | 0.4350 | 161 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2306.05955](/papers/2306.05955/) | ZINC | GatedGCN | 0.0770 | 0.4350 | 161 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2601.07419](/papers/2601.07419/) | PROTEINS | GIN | 0.7620 | 0.6650 | 160 | [Probabilistic Graph Rewiring via Virtual Nodes](/papers/2405.17311/) | already known (2024-05) |
| [2602.02268](/papers/2602.02268/) | CiteSeer | Exphormer | 0.7683 | 0.5117 | 159 | [Learning Graph Quantized Tokenizers](/papers/2410.13798/) | already known (2024-10-17) |
| [2506.14098](/papers/2506.14098/) | Cora | GAT | 0.8825 | 0.7624 | 159 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2310.05174](/papers/2310.05174/) | PROTEINS | GAT | 0.7634 | 0.6863 | 159 | [HOPSE: Scalable Higher-Order Positional and Structural Encoder for...](/papers/2505.15405/) | published later (2025-05) |
| [2402.08450](/papers/2402.08450/) | ZINC | DSS-GNN | 0.0290 | 0.1020 | 159 | [Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via...](/papers/2402.08450/) | same paper |
| [2406.09291](/papers/2406.09291/) | ZINC | DSS-GNN | 0.0290 | 0.1020 | 159 | [Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via...](/papers/2402.08450/) | already known (2024-02) |
| [2406.09291](/papers/2406.09291/) | ZINC | DSS-GNN | 0.0290 | 0.1020 | 159 | [Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via...](/papers/2402.08450/) | already known (2024-02) |
| [2402.08450](/papers/2402.08450/) | ZINC | GNN (a) | 0.0340 | 0.1050 | 159 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2306.03561](/papers/2306.03561/) | ogbg-molhiv | GCN | 0.9681 | 0.7606 | 158 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2306.05955](/papers/2306.05955/) | ogbg-molhiv | GCN | 0.9681 | 0.7606 | 158 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2402.08450](/papers/2402.08450/) | ogbg-molhiv | GCN | 0.9681 | 0.7606 | 158 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2405.13526](/papers/2405.13526/) | ogbg-molhiv | GCN | 0.9681 | 0.7606 | 158 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2501.03113](/papers/2501.03113/) | ogbg-molhiv | GCN | 0.9681 | 0.7606 | 158 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2604.17324](/papers/2604.17324/) | ogbg-molhiv | GCN | 0.9681 | 0.7606 | 158 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | already known (2025-11) |
| [2412.07188](/papers/2412.07188/) | Cora | GATv2 | 0.8350 | 0.6305 | 158 | [Rotary Position Encodings for Graphs](/papers/2509.22259/) | published later (2025-09) |
| [2412.07188](/papers/2412.07188/) | Cora | SAGE | 0.8360 | 0.6397 | 158 | [Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in...](/papers/2603.27529/) | published later (2026-03) |
| [2406.18380](/papers/2406.18380/) | PROTEINS | GCN | 0.7600 | 0.6310 | 158 | [On the Stability of Multiset and Graph Neural...](/papers/2406.06984/) | already known (2024-06) |
| [2306.05955](/papers/2306.05955/) | ZINC | ESAN | 0.0290 | 0.1020 | 158 | [Graph as Point Set](/papers/2405.02795/) | published later (2024-05-05) |
| [2306.05955](/papers/2306.05955/) | ZINC | ESAN | 0.0290 | 0.1020 | 158 | [Graph as Point Set](/papers/2405.02795/) | published later (2024-05-05) |
| [2405.02795](/papers/2405.02795/) | ZINC | ESAN | 0.0290 | 0.1020 | 158 | [Graph as Point Set](/papers/2405.02795/) | same paper |
| [2506.04765](/papers/2506.04765/) | ZINC | GAT | 0.0776 | 0.6225 | 157 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2506.04765](/papers/2506.04765/) | ZINC | GAT | 0.0776 | 0.6225 | 157 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2602.02268](/papers/2602.02268/) | ZINC | GAT | 0.0776 | 0.6225 | 157 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2602.02268](/papers/2602.02268/) | ZINC | GAT | 0.0776 | 0.6225 | 157 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2505.15405](/papers/2505.15405/) | ZINC | GAT | 0.0776 | 0.6100 | 157 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2505.15405](/papers/2505.15405/) | ZINC | GAT | 0.0776 | 0.6100 | 157 | [An end-to-end attention-based approach for learning on graphs](/papers/2402.10793/) | already known (2024-02) |
| [2310.01704](/papers/2310.01704/) | ogbg-molhiv | GCN | 0.9681 | 0.7610 | 157 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2406.18380](/papers/2406.18380/) | Cora | GCN | 0.8778 | 0.7401 | 157 | [Revisiting Heterophily For Graph Neural Networks](/papers/2210.07606/) | already known (2022-10) |
| [2508.11390](/papers/2508.11390/) | PROTEINS | GAT | 0.7634 | 0.6900 | 157 | [HOPSE: Scalable Higher-Order Positional and Structural Encoder for...](/papers/2505.15405/) | already known (2025-05) |
| [2310.03274](/papers/2310.03274/) | ogbg-molhiv | GIN | 0.9680 | 0.7610 | 156 | [No Metric to Rule Them All: Toward Principled...](/papers/2502.02379/) | published later (2025-02-04) |
| [2406.18380](/papers/2406.18380/) | Cora | GAT | 0.8825 | 0.7651 | 156 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2509.01254](/papers/2509.01254/) | ZINC | GCN | 0.0760 | 0.3700 | 155 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2509.01254](/papers/2509.01254/) | ZINC | GCN | 0.0760 | 0.3700 | 155 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2102.08786](/papers/2102.08786/) | ZINC | GCN | 0.0760 | 0.3670 | 155 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2308.11129](/papers/2308.11129/) | ZINC | GCN | 0.0760 | 0.3670 | 155 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2308.11129](/papers/2308.11129/) | ZINC | GCN | 0.0760 | 0.3670 | 155 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.01704](/papers/2310.01704/) | ZINC | GCN | 0.0760 | 0.3670 | 155 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2310.01704](/papers/2310.01704/) | ZINC | GCN | 0.0760 | 0.3670 | 155 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2311.04653](/papers/2311.04653/) | ZINC | GCN | 0.0760 | 0.3670 | 155 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2311.04653](/papers/2311.04653/) | ZINC | GCN | 0.0760 | 0.3670 | 155 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2401.01233](/papers/2401.01233/) | ZINC | GCN | 0.0760 | 0.3670 | 155 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2401.17791](/papers/2401.17791/) | ZINC | GCN | 0.0760 | 0.3670 | 155 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2401.17791](/papers/2401.17791/) | ZINC | GCN | 0.0760 | 0.3670 | 155 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2404.03380](/papers/2404.03380/) | ZINC | GCN | 0.0760 | 0.3670 | 155 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2404.03380](/papers/2404.03380/) | ZINC | GCN | 0.0760 | 0.3670 | 155 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2406.03386](/papers/2406.03386/) | ZINC | GCN | 0.0760 | 0.3670 | 155 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2406.03386](/papers/2406.03386/) | ZINC | GCN | 0.0760 | 0.3670 | 155 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2407.05649](/papers/2407.05649/) | ZINC | GCN | 0.0760 | 0.3670 | 155 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2407.05649](/papers/2407.05649/) | ZINC | GCN | 0.0760 | 0.3670 | 155 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | published later (2025-02) |
| [2502.00282](/papers/2502.00282/) | ZINC | GCN | 0.0760 | 0.3670 | 155 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2502.00282](/papers/2502.00282/) | ZINC | GCN | 0.0760 | 0.3670 | 155 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2502.09365](/papers/2502.09365/) | ZINC | GCN | 0.0760 | 0.3670 | 155 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2502.09365](/papers/2502.09365/) | ZINC | GCN | 0.0760 | 0.3670 | 155 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2504.12588](/papers/2504.12588/) | ZINC | GCN | 0.0760 | 0.3670 | 155 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2508.05070](/papers/2508.05070/) | ZINC | GCN | 0.0760 | 0.3670 | 155 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2508.05070](/papers/2508.05070/) | ZINC | GCN | 0.0760 | 0.3670 | 155 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2604.17324](/papers/2604.17324/) | ZINC | GCN | 0.0760 | 0.3670 | 155 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2604.17324](/papers/2604.17324/) | ZINC | GCN | 0.0760 | 0.3670 | 155 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2605.05689](/papers/2605.05689/) | ZINC | GCN | 0.0760 | 0.3670 | 155 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2605.05689](/papers/2605.05689/) | ZINC | GCN | 0.0760 | 0.3670 | 155 | [Can Classic GNNs Be Strong Baselines for Graph-level...](/papers/2502.09263/) | already known (2025-02) |
| [2506.04765](/papers/2506.04765/) | Cora | Exphormer | 0.8329 | 0.6120 | 155 | [GEN: A Practical Alternative to Graph Transformers for...](/papers/2401.01233/) | already known (2024-01) |
| [2602.02268](/papers/2602.02268/) | Cora | Exphormer | 0.8329 | 0.6120 | 155 | [GEN: A Practical Alternative to Graph Transformers for...](/papers/2401.01233/) | already known (2024-01) |
| [2410.03424](/papers/2410.03424/) | PROTEINS | GCN | 0.7600 | 0.6665 | 153 | [On the Stability of Multiset and Graph Neural...](/papers/2406.06984/) | already known (2024-06) |
| [2310.05174](/papers/2310.05174/) | PROTEINS | GIN | 0.7620 | 0.6907 | 153 | [Probabilistic Graph Rewiring via Virtual Nodes](/papers/2405.17311/) | published later (2024-05) |
| [2508.19071](/papers/2508.19071/) | Cora | FA | 0.8165 | 0.2986 | 152 | [Effects of Dropout on Performance in Long-range Graph...](/papers/2502.07364/) | already known (2025-02) |
| [2506.04765](/papers/2506.04765/) | Cora | SAN | 0.8191 | 0.5403 | 152 | [Hybrid Focal and Full-Range Attention Based Graph Transformers](/papers/2311.04653/) | already known (2023-11) |
| [2602.02268](/papers/2602.02268/) | Cora | SAN | 0.8191 | 0.5403 | 152 | [Hybrid Focal and Full-Range Attention Based Graph Transformers](/papers/2311.04653/) | already known (2023-11) |
| [2506.14098](/papers/2506.14098/) | PubMed | MLP | 0.9476 | 0.6866 | 152 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2412.07188](/papers/2412.07188/) | Cora | GIN | 0.8303 | 0.6098 | 152 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2210.07606](/papers/2210.07606/) | Cora | GAT | 0.8825 | 0.7670 | 152 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2307.07107](/papers/2307.07107/) | Peptides-func | R-GCN (RWSE) | 0.6860 | 0.6067 | 152 | [Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based...](/papers/2501.03113/) | published later (2025-01) |
| [2510.02565](/papers/2510.02565/) | Peptides-func | R-GCN (RWSE) | 0.6860 | 0.6067 | 152 | [Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based...](/papers/2501.03113/) | already known (2025-01) |
| [2310.05174](/papers/2310.05174/) | PROTEINS | GCN | 0.7600 | 0.6752 | 151 | [On the Stability of Multiset and Graph Neural...](/papers/2406.06984/) | published later (2024-06) |
| [2210.07606](/papers/2210.07606/) | CiteSeer | MixHop | 0.7626 | 0.4952 | 150 | [Algorithmic Graph Tasks](/papers/2312.16560/) | published later (2023-12) |
| [2410.05593](/papers/2410.05593/) | PubMed | MLP | 0.9476 | 0.7140 | 150 | [When Structure Doesn’t Help: LLMs Do Not Read...](/papers/2511.16767/) | published later (2025-11) |
| [2410.05499](/papers/2410.05499/) | PROTEINS | GIN | 0.7620 | 0.6970 | 149 | [Probabilistic Graph Rewiring via Virtual Nodes](/papers/2405.17311/) | already known (2024-05) |
=======
| [2509.01254](/papers/2509.01254/) | ZINC | GIN | 0.0140 | 0.5300 | 116 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | already known (2023-06) |
| [2106.05234](/papers/2106.05234/) | ZINC | GIN | 0.0140 | 0.5260 | 115 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | published later (2023-06) |
| [2205.12454](/papers/2205.12454/) | ZINC | GIN | 0.0140 | 0.5260 | 115 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | published later (2023-06) |
| [2301.09505](/papers/2301.09505/) | ZINC | GIN | 0.0140 | 0.5260 | 115 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | published later (2023-06) |
| [2305.06102](/papers/2305.06102/) | ZINC | GIN | 0.0140 | 0.5260 | 115 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | published later (2023-06) |
| [2305.15747](/papers/2305.15747/) | ZINC | GIN | 0.0140 | 0.5260 | 115 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | published later (2023-06) |
| [2401.17791](/papers/2401.17791/) | ZINC | GIN | 0.0140 | 0.5260 | 115 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | already known (2023-06) |
| [2501.18739](/papers/2501.18739/) | ZINC | GIN | 0.0140 | 0.5260 | 115 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | already known (2023-06) |
| [2502.00282](/papers/2502.00282/) | ZINC | GIN | 0.0140 | 0.5260 | 115 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | already known (2023-06) |
| [2508.05070](/papers/2508.05070/) | ZINC | GIN | 0.0140 | 0.5260 | 115 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | already known (2023-06) |
| [2108.03348](/papers/2108.03348/) | ZINC | GraphSAGE | 0.0060 | 0.4680 | 114 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | published later (2023-06) |
| [2002.04025](/papers/2002.04025/) | ZINC | GraphSAGE | 0.0060 | 0.4100 | 113 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | published later (2023-06) |
| [2509.01254](/papers/2509.01254/) | ZINC | GraphSAGE | 0.0060 | 0.4000 | 113 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | already known (2023-06) |
| [2106.05234](/papers/2106.05234/) | ZINC | GraphSAGE | 0.0060 | 0.3980 | 113 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | published later (2023-06) |
| [2301.09505](/papers/2301.09505/) | ZINC | GraphSAGE | 0.0060 | 0.3980 | 113 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | published later (2023-06) |
| [2305.06102](/papers/2305.06102/) | ZINC | GraphSAGE | 0.0060 | 0.3980 | 113 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | published later (2023-06) |
| [2305.15747](/papers/2305.15747/) | ZINC | GraphSAGE | 0.0060 | 0.3980 | 113 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | published later (2023-06) |
| [2002.04025](/papers/2002.04025/) | ZINC | GIN | 0.0140 | 0.4080 | 112 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | published later (2023-06) |
| [2108.03348](/papers/2108.03348/) | ZINC | GatedGCN | 0.0040 | 0.3750 | 112 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | published later (2023-06) |
| [2602.02268](/papers/2602.02268/) | ZINC | GCN | 0.0240 | 0.6090 | 111 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | already known (2023-06) |
| [2002.04025](/papers/2002.04025/) | ZINC | GatedGCN | 0.0040 | 0.3630 | 111 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | published later (2023-06) |
| [2108.03348](/papers/2108.03348/) | ZINC | GIN | 0.0140 | 0.3870 | 110 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | published later (2023-06) |
| [2312.01538](/papers/2312.01538/) | ZINC | GIN | 0.0140 | 0.3870 | 110 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | already known (2023-06) |
| [2002.04025](/papers/2002.04025/) | ZINC | GCN | 0.0240 | 0.4690 | 108 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | published later (2023-06) |
| [2502.01122](/papers/2502.01122/) | ZINC | GCN | 0.0240 | 0.4690 | 108 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | already known (2023-06) |
| [2108.03348](/papers/2108.03348/) | ZINC | GCN | 0.0240 | 0.4590 | 106 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | published later (2023-06) |
| [2006.15107](/papers/2006.15107/) | ZINC | GatedGCN | 0.0040 | 0.2820 | 106 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | published later (2023-06) |
| [2205.12454](/papers/2205.12454/) | ZINC | GatedGCN | 0.0040 | 0.2820 | 106 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | published later (2023-06) |
| [2312.01538](/papers/2312.01538/) | ZINC | GatedGCN | 0.0040 | 0.2820 | 106 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | already known (2023-06) |
| [2401.17791](/papers/2401.17791/) | ZINC | GatedGCN | 0.0040 | 0.2820 | 106 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | already known (2023-06) |
| [2508.05070](/papers/2508.05070/) | ZINC | GatedGCN | 0.0040 | 0.2820 | 106 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | already known (2023-06) |
| [2110.07875](/papers/2110.07875/) | ZINC | GatedGCN | 0.0040 | 0.2510 | 105 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | published later (2023-06) |
| [2310.18716](/papers/2310.18716/) | ZINC | GatedGCN | 0.0040 | 0.2510 | 105 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | already known (2023-06) |
| [2305.15747](/papers/2305.15747/) | ZINC | GCN | 0.0240 | 0.3800 | 104 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | published later (2023-06) |
| [2509.01254](/papers/2509.01254/) | ZINC | GCN | 0.0240 | 0.3700 | 104 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | already known (2023-06) |
| [2305.17589](/papers/2305.17589/) | ZINC | GraphSAGE | 0.0060 | 0.2780 | 104 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | published later (2023-06) |
| [2106.05234](/papers/2106.05234/) | ZINC | GCN | 0.0240 | 0.3670 | 103 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | published later (2023-06) |
| [2110.07875](/papers/2110.07875/) | ZINC | GCN | 0.0240 | 0.3670 | 103 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | published later (2023-06) |
| [2205.12454](/papers/2205.12454/) | ZINC | GCN | 0.0240 | 0.3670 | 103 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | published later (2023-06) |
| [2301.09505](/papers/2301.09505/) | ZINC | GCN | 0.0240 | 0.3670 | 103 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | published later (2023-06) |
| [2302.08647](/papers/2302.08647/) | ZINC | GCN | 0.0240 | 0.3670 | 103 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | published later (2023-06) |
| [2305.06102](/papers/2305.06102/) | ZINC | GCN | 0.0240 | 0.3670 | 103 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | published later (2023-06) |
| [2401.17791](/papers/2401.17791/) | ZINC | GCN | 0.0240 | 0.3670 | 103 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | already known (2023-06) |
| [2502.00282](/papers/2502.00282/) | ZINC | GCN | 0.0240 | 0.3670 | 103 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | already known (2023-06) |
| [2508.05070](/papers/2508.05070/) | ZINC | GCN | 0.0240 | 0.3670 | 103 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | already known (2023-06) |
| [2006.15107](/papers/2006.15107/) | ZINC | GIN | 0.0140 | 0.2520 | 103 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | published later (2023-06) |
| [2302.08647](/papers/2302.08647/) | ZINC | GatedGCN | 0.0040 | 0.2140 | 102 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | published later (2023-06) |
| [2305.06102](/papers/2305.06102/) | ZINC | GatedGCN | 0.0040 | 0.2140 | 102 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | published later (2023-06) |
| [2502.01122](/papers/2502.01122/) | ZINC | GIN | 0.0140 | 0.2090 | 99 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | already known (2023-06) |
| [2305.17589](/papers/2305.17589/) | ZINC | GCN | 0.0240 | 0.2960 | 98 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | published later (2023-06) |
| [2312.01538](/papers/2312.01538/) | ZINC | GCN | 0.0240 | 0.2780 | 97 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | already known (2023-06) |
| [2602.02268](/papers/2602.02268/) | ZINC | GPS | 0.0262 | 0.1968 | 87 | [Union Subgraph Neural Networks](/papers/2305.15747/) | already known (2023-05) |
| [2402.08450](/papers/2402.08450/) | ZINC | GIN | 0.0140 | 0.1630 | 87 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | already known (2023-06) |
| [2602.07256](/papers/2602.07256/) | Cora | GloGNN | 0.8831 | 0.7302 | 86 | [Finding Global Homophily in Graph Neural Networks When...](/papers/2205.07308/) | already known (2022-05-15) |
| [2305.15747](/papers/2305.15747/) | Cora | GraphSAGE | 0.8790 | 0.7060 | 85 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2602.02268](/papers/2602.02268/) | Peptides-struct | GCN | 0.2460 | 0.4347 | 83 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | already known (2023-12-03) |
| [2305.15747](/papers/2305.15747/) | ZINC | GIN | 0.0140 | 0.1552 | 83 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | published later (2023-06) |
| [2602.02268](/papers/2602.02268/) | Cora | GCN | 0.8778 | 0.7180 | 81 | [Language is All a Graph Needs](/papers/2308.07134/) | already known (2023-08) |
| [2205.12454](/papers/2205.12454/) | Peptides-struct | GCN | 0.2460 | 0.3496 | 80 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | published later (2023-12-03) |
| [2206.08164](/papers/2206.08164/) | Peptides-struct | GCN | 0.2460 | 0.3496 | 80 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | published later (2023-12-03) |
| [2302.08647](/papers/2302.08647/) | Peptides-struct | GCN | 0.2460 | 0.3496 | 80 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | published later (2023-12-03) |
| [2303.06147](/papers/2303.06147/) | Peptides-struct | GCN | 0.2460 | 0.3496 | 80 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | published later (2023-12-03) |
| [2306.02866](/papers/2306.02866/) | Peptides-struct | GCN | 0.2460 | 0.3496 | 80 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | published later (2023-12-03) |
| [2401.17791](/papers/2401.17791/) | Peptides-struct | GCN | 0.2460 | 0.3496 | 80 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | already known (2023-12-03) |
| [2402.08450](/papers/2402.08450/) | Peptides-struct | GCN | 0.2460 | 0.3496 | 80 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | already known (2023-12-03) |
| [2405.13806](/papers/2405.13806/) | Peptides-struct | GCN | 0.2460 | 0.3496 | 80 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | already known (2023-12-03) |
| [2502.00282](/papers/2502.00282/) | Peptides-struct | GCN | 0.2460 | 0.3496 | 80 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | already known (2023-12-03) |
| [2508.05070](/papers/2508.05070/) | Peptides-struct | GCN | 0.2460 | 0.3496 | 80 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | already known (2023-12-03) |
| [2605.06462](/papers/2605.06462/) | Peptides-struct | GCN | 0.2460 | 0.3496 | 80 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | already known (2023-12-03) |
| [2305.15747](/papers/2305.15747/) | Cora | GCN | 0.8778 | 0.7256 | 78 | [Language is All a Graph Needs](/papers/2308.07134/) | published later (2023-08) |
| [2110.07875](/papers/2110.07875/) | ZINC | Graph-ViT | 0.0350 | 0.1810 | 77 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2310.18716](/papers/2310.18716/) | ZINC | Graph-ViT | 0.0350 | 0.1810 | 77 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2305.17589](/papers/2305.17589/) | ZINC | PNA | 0.0670 | 0.2450 | 75 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2502.02379](/papers/2502.02379/) | PROTEINS | GIN | 0.7850 | 0.6090 | 75 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | already known (2023-05-27) |
| [2602.02268](/papers/2602.02268/) | Cora | NodeFormer | 0.8744 | 0.7103 | 74 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | already known (2026-02) |
| [2502.02379](/papers/2502.02379/) | PROTEINS | GAT | 0.7790 | 0.6120 | 73 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | already known (2023-05-27) |
| [2205.12454](/papers/2205.12454/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 72 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | published later (2023-12-03) |
| [2206.08164](/papers/2206.08164/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 72 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | published later (2023-12-03) |
| [2302.08647](/papers/2302.08647/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 72 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | published later (2023-12-03) |
| [2303.06147](/papers/2303.06147/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 72 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | published later (2023-12-03) |
| [2306.02866](/papers/2306.02866/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 72 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | published later (2023-12-03) |
| [2401.17791](/papers/2401.17791/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 72 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | already known (2023-12-03) |
| [2405.13806](/papers/2405.13806/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 72 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | already known (2023-12-03) |
| [2508.05070](/papers/2508.05070/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 72 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | already known (2023-12-03) |
| [2605.06462](/papers/2605.06462/) | Peptides-struct | GINE | 0.2473 | 0.3547 | 72 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | already known (2023-12-03) |
| [2301.09505](/papers/2301.09505/) | ZINC | GraphSAGE | 0.0060 | 0.1260 | 71 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | published later (2023-06) |
| [2502.02379](/papers/2502.02379/) | PROTEINS | GCN | 0.7720 | 0.5930 | 70 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | already known (2023-05-27) |
| [2305.15747](/papers/2305.15747/) | ZINC | GraphSAGE | 0.0060 | 0.1205 | 69 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | published later (2023-06) |
| [2305.15747](/papers/2305.15747/) | CiteSeer | GraphSAGE | 0.7643 | 0.5502 | 66 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2602.02268](/papers/2602.02268/) | Cora | GAT | 0.8711 | 0.7460 | 66 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | already known (2026-02) |
| [2006.15107](/papers/2006.15107/) | ZINC | PNA | 0.0670 | 0.1880 | 66 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2108.03348](/papers/2108.03348/) | ZINC | PNA | 0.0670 | 0.1880 | 66 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2205.12454](/papers/2205.12454/) | ZINC | PNA | 0.0670 | 0.1880 | 66 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2312.01538](/papers/2312.01538/) | ZINC | PNA | 0.0670 | 0.1880 | 66 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2401.17791](/papers/2401.17791/) | ZINC | PNA | 0.0670 | 0.1880 | 66 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2508.05070](/papers/2508.05070/) | ZINC | PNA | 0.0670 | 0.1880 | 66 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | already known (2025-01-30) |
| [2305.15747](/papers/2305.15747/) | Cora | GAT | 0.8711 | 0.7482 | 65 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2602.02268](/papers/2602.02268/) | Peptides-struct | Graph-MLPMixer | 0.2475 | 0.3065 | 64 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | already known (2023-12-03) |
| [2602.02268](/papers/2602.02268/) | ZINC | Graphormer | 0.0250 | 0.1305 | 63 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | already known (2025-01-30) |
| [2602.02268](/papers/2602.02268/) | Peptides-func | Graph-MLPMixer | 0.6970 | 0.4225 | 62 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | already known (2023-12-03) |
| [2305.15747](/papers/2305.15747/) | ZINC | Graphormer | 0.0250 | 0.1269 | 62 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2205.12454](/papers/2205.12454/) | Peptides-struct | GatedGCN | 0.2477 | 0.3420 | 62 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | published later (2023-12-03) |
| [2206.08164](/papers/2206.08164/) | Peptides-struct | GatedGCN | 0.2477 | 0.3420 | 62 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | published later (2023-12-03) |
| [2302.08647](/papers/2302.08647/) | Peptides-struct | GatedGCN | 0.2477 | 0.3420 | 62 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | published later (2023-12-03) |
| [2303.06147](/papers/2303.06147/) | Peptides-struct | GatedGCN | 0.2477 | 0.3420 | 62 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | published later (2023-12-03) |
| [2306.02866](/papers/2306.02866/) | Peptides-struct | GatedGCN | 0.2477 | 0.3420 | 62 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | published later (2023-12-03) |
| [2401.17791](/papers/2401.17791/) | Peptides-struct | GatedGCN | 0.2477 | 0.3420 | 62 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | already known (2023-12-03) |
| [2402.08450](/papers/2402.08450/) | Peptides-struct | GatedGCN | 0.2477 | 0.3420 | 62 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | already known (2023-12-03) |
| [2405.13806](/papers/2405.13806/) | Peptides-struct | GatedGCN | 0.2477 | 0.3420 | 62 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | already known (2023-12-03) |
| [2502.00282](/papers/2502.00282/) | Peptides-struct | GatedGCN | 0.2477 | 0.3420 | 62 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | already known (2023-12-03) |
| [2508.05070](/papers/2508.05070/) | Peptides-struct | GatedGCN | 0.2477 | 0.3420 | 62 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | already known (2023-12-03) |
| [2605.06462](/papers/2605.06462/) | Peptides-struct | GatedGCN | 0.2477 | 0.3420 | 62 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | already known (2023-12-03) |
| [2602.02268](/papers/2602.02268/) | Peptides-func | GCN | 0.6860 | 0.3614 | 61 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | already known (2023-12-03) |
| [2002.04025](/papers/2002.04025/) | ZINC | MoNet | 0.0900 | 0.4070 | 61 | [Rethinking the Expressive Power of GNNs via Graph...](/papers/2301.09505/) | published later (2023-01) |
| [2602.02268](/papers/2602.02268/) | PubMed | GCN | 0.8890 | 0.7150 | 61 | [Language is All a Graph Needs](/papers/2308.07134/) | already known (2023-08) |
| [2108.03348](/papers/2108.03348/) | ZINC | Graphormer | 0.0250 | 0.1220 | 61 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2110.07875](/papers/2110.07875/) | ZINC | Graphormer | 0.0250 | 0.1220 | 61 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2205.12454](/papers/2205.12454/) | ZINC | Graphormer | 0.0250 | 0.1220 | 61 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2301.09505](/papers/2301.09505/) | ZINC | Graphormer | 0.0250 | 0.1220 | 61 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2302.08647](/papers/2302.08647/) | ZINC | Graphormer | 0.0250 | 0.1220 | 61 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2305.06102](/papers/2305.06102/) | ZINC | Graphormer | 0.0250 | 0.1220 | 61 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2312.01538](/papers/2312.01538/) | ZINC | Graphormer | 0.0250 | 0.1220 | 61 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2401.17791](/papers/2401.17791/) | ZINC | Graphormer | 0.0250 | 0.1220 | 61 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2402.08450](/papers/2402.08450/) | ZINC | Graphormer | 0.0250 | 0.1220 | 61 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2501.18739](/papers/2501.18739/) | ZINC | Graphormer | 0.0250 | 0.1220 | 61 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | same paper |
| [2305.15747](/papers/2305.15747/) | ZINC | GCN | 0.0240 | 0.1152 | 61 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | published later (2023-06) |
| [2305.15747](/papers/2305.15747/) | PROTEINS | GIN | 0.7850 | 0.7286 | 61 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | published later (2023-05-27) |
| [2502.02379](/papers/2502.02379/) | NCI1 | GAT | 0.8450 | 0.5500 | 60 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | already known (2023-05-27) |
| [2305.15747](/papers/2305.15747/) | D&D | GAT | 0.9000 | 0.7425 | 60 | [Short-Range Oversquashing](/papers/2511.20406/) | published later (2025-11) |
| [2305.15747](/papers/2305.15747/) | CiteSeer | GAT | 0.7643 | 0.6382 | 60 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2501.18739](/papers/2501.18739/) | ZINC | AgentNet | 0.0400 | 0.1440 | 60 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | same paper |
| [2305.15747](/papers/2305.15747/) | ZINC | Unionormer | 0.0252 | 0.1241 | 60 | [Union Subgraph Neural Networks](/papers/2305.15747/) | same paper |
| [2301.09505](/papers/2301.09505/) | ZINC | GCN | 0.0240 | 0.1130 | 59 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | published later (2023-06) |
| [2312.01538](/papers/2312.01538/) | PROTEINS | GIN | 0.7850 | 0.7330 | 59 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | already known (2023-05-27) |
| [2305.15747](/papers/2305.15747/) | NCI1 | GraphSAGE | 0.8380 | 0.6546 | 58 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | published later (2023-05-27) |
| [1904.08082](/papers/1904.08082/) | D&D | DiffPool | 0.8064 | 0.6695 | 58 | [Hierarchical Graph Representation Learning with Differentiable Pooling](/papers/1806.08804/) | already known (2018-06) |
| [2602.07256](/papers/2602.07256/) | Chameleon | MLP | 0.7430 | 0.3844 | 57 | [Beyond Low-frequency Information in Graph Convolutional Networks](/papers/2101.00797/) | already known (2021-01) |
| [2602.02268](/papers/2602.02268/) | Cora | APPNP | 0.8759 | 0.7713 | 57 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | already known (2026-02) |
| [1812.04202](/papers/1812.04202/) | Cora | SGC | 0.8805 | 0.8100 | 56 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2101.00797](/papers/2101.00797/) | Cora | SGC | 0.8805 | 0.8100 | 56 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2410.23686](/papers/2410.23686/) | PROTEINS | GIN | 0.7850 | 0.7384 | 56 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | already known (2023-05-27) |
| [2312.01538](/papers/2312.01538/) | PROTEINS | DiffPool | 0.7810 | 0.7370 | 56 | [Towards Better Graph Representation Learning with Parameterized Decomposition...](/papers/2305.06102/) | already known (2023-05-10) |
| [2602.07256](/papers/2602.07256/) | Chameleon | FAGCN | 0.7610 | 0.3983 | 55 | [Beyond Low-frequency Information in Graph Convolutional Networks](/papers/2101.00797/) | already known (2021-01) |
| [2308.07134](/papers/2308.07134/) | Cora | GAT | 0.8711 | 0.7670 | 55 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2305.06102](/papers/2305.06102/) | PROTEINS | DGCNN | 0.7626 | 0.6129 | 54 | [Graph U-Nets](/papers/1905.05178/) | already known (2019-05-11) |
| [2602.02268](/papers/2602.02268/) | Peptides-struct | Exphormer | 0.2481 | 0.3297 | 54 | [GraphMinNet: Learning Dependencies in Graphs with Light Complexity...](/papers/2502.00282/) | already known (2025-02-01) |
| [1312.6203](/papers/1312.6203/) | Cora | GraphSAGE | 0.8790 | 0.8100 | 54 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [1806.08804](/papers/1806.08804/) | PROTEINS | GraphSAGE | 0.7680 | 0.7048 | 54 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | published later (2023-05-27) |
| [2602.02268](/papers/2602.02268/) | ZINC | GAT | 0.1110 | 0.6225 | 53 | [Rethinking the Expressive Power of GNNs via Graph...](/papers/2301.09505/) | already known (2023-01) |
| [2301.09505](/papers/2301.09505/) | ZINC | MoNet | 0.0900 | 0.2920 | 53 | [Rethinking the Expressive Power of GNNs via Graph...](/papers/2301.09505/) | same paper |
| [2309.09384](/papers/2309.09384/) | MUTAG | GIN | 0.8940 | 0.7340 | 52 | [Coloring graph neural networks for node disambiguation](/papers/1912.06058/) | already known (2019-12) |
| [2106.05234](/papers/2106.05234/) | ZINC | GatedGCN+LapPE | 0.0900 | 0.2140 | 52 | [Recipe for a General, Powerful, Scalable Graph Transformer](/papers/2205.12454/) | published later (2022-05) |
| [2301.09505](/papers/2301.09505/) | ZINC | GatedGCN+LapPE | 0.0900 | 0.2140 | 52 | [Recipe for a General, Powerful, Scalable Graph Transformer](/papers/2205.12454/) | already known (2022-05) |
| [2602.02268](/papers/2602.02268/) | Cora | DIFFormer | 0.8661 | 0.7650 | 52 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | already known (2026-02) |
| [2305.15747](/papers/2305.15747/) | D&D | GIN | 0.7980 | 0.7029 | 52 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | published later (2023-05-27) |
| [2410.23686](/papers/2410.23686/) | PROTEINS | GCN | 0.7720 | 0.7324 | 52 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | already known (2023-05-27) |
| [2602.02268](/papers/2602.02268/) | PubMed | NodeFormer | 0.8150 | 0.6953 | 51 | [Transformers over Directed Acyclic Graphs](/papers/2210.13148/) | already known (2022-10-24) |
| [2310.18716](/papers/2310.18716/) | ZINC | GatedGCN+LapPE | 0.0900 | 0.2020 | 51 | [Recipe for a General, Powerful, Scalable Graph Transformer](/papers/2205.12454/) | already known (2022-05) |
| [2108.03348](/papers/2108.03348/) | ZINC | GAT | 0.1110 | 0.4750 | 50 | [Rethinking the Expressive Power of GNNs via Graph...](/papers/2301.09505/) | published later (2023-01) |
| [2206.08164](/papers/2206.08164/) | Peptides-func | GCN | 0.6860 | 0.5930 | 50 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | published later (2023-12-03) |
| [2302.08647](/papers/2302.08647/) | Peptides-func | GCN | 0.6860 | 0.5930 | 50 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | published later (2023-12-03) |
| [2303.06147](/papers/2303.06147/) | Peptides-func | GCN | 0.6860 | 0.5930 | 50 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | published later (2023-12-03) |
| [2306.02866](/papers/2306.02866/) | Peptides-func | GCN | 0.6860 | 0.5930 | 50 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | published later (2023-12-03) |
| [2401.17791](/papers/2401.17791/) | Peptides-func | GCN | 0.6860 | 0.5930 | 50 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | already known (2023-12-03) |
| [2402.08450](/papers/2402.08450/) | Peptides-func | GCN | 0.6860 | 0.5930 | 50 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | already known (2023-12-03) |
| [2405.13806](/papers/2405.13806/) | Peptides-func | GCN | 0.6860 | 0.5930 | 50 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | already known (2023-12-03) |
| [2502.00282](/papers/2502.00282/) | Peptides-func | GCN | 0.6860 | 0.5930 | 50 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | already known (2023-12-03) |
| [2508.05070](/papers/2508.05070/) | Peptides-func | GCN | 0.6860 | 0.5930 | 50 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | already known (2023-12-03) |
| [2605.06462](/papers/2605.06462/) | Peptides-func | GCN | 0.6860 | 0.5930 | 50 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | already known (2023-12-03) |
| [2301.09505](/papers/2301.09505/) | ZINC | NGNN | 0.0290 | 0.1110 | 50 | [Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via...](/papers/2402.08450/) | published later (2024-02-13) |
| [2402.08450](/papers/2402.08450/) | ZINC | NGNN | 0.0290 | 0.1110 | 50 | [Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via...](/papers/2402.08450/) | same paper |
| [2305.15747](/papers/2305.15747/) | PROTEINS | GAT | 0.7790 | 0.7434 | 50 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | published later (2023-05-27) |
| [2106.05234](/papers/2106.05234/) | ZINC | PNA | 0.0670 | 0.1420 | 49 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2301.09505](/papers/2301.09505/) | ZINC | PNA | 0.0670 | 0.1420 | 49 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2302.08647](/papers/2302.08647/) | ZINC | PNA | 0.0670 | 0.1420 | 49 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2305.06102](/papers/2305.06102/) | ZINC | PNA | 0.0670 | 0.1420 | 49 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2501.18739](/papers/2501.18739/) | ZINC | PNA | 0.0670 | 0.1420 | 49 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | same paper |
| [2110.07875](/papers/2110.07875/) | ZINC | PNA | 0.0670 | 0.1410 | 49 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2310.18716](/papers/2310.18716/) | ZINC | PNA | 0.0670 | 0.1410 | 49 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2305.15747](/papers/2305.15747/) | PROTEINS | GCN | 0.7720 | 0.7389 | 49 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | published later (2023-05-27) |
| [2002.04025](/papers/2002.04025/) | ZINC | GAT | 0.1110 | 0.4630 | 48 | [Rethinking the Expressive Power of GNNs via Graph...](/papers/2301.09505/) | published later (2023-01) |
| [2305.10498](/papers/2305.10498/) | Squirrel | MLP | 0.6310 | 0.2877 | 48 | [Beyond Low-frequency Information in Graph Convolutional Networks](/papers/2101.00797/) | already known (2021-01) |
| [2602.07256](/papers/2602.07256/) | Chameleon | GCN | 0.7230 | 0.4006 | 48 | [Beyond Low-frequency Information in Graph Convolutional Networks](/papers/2101.00797/) | already known (2021-01) |
| [2410.23686](/papers/2410.23686/) | NCI1 | GraphSAGE | 0.8380 | 0.7382 | 48 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | already known (2023-05-27) |
| [1312.6203](/papers/1312.6203/) | Cora | GCN | 0.8778 | 0.8150 | 48 | [Language is All a Graph Needs](/papers/2308.07134/) | published later (2023-08) |
| [1609.02907](/papers/1609.02907/) | Cora | GCN | 0.8778 | 0.8150 | 48 | [Language is All a Graph Needs](/papers/2308.07134/) | published later (2023-08) |
| [1812.04202](/papers/1812.04202/) | Cora | GCN | 0.8778 | 0.8150 | 48 | [Language is All a Graph Needs](/papers/2308.07134/) | published later (2023-08) |
| [1905.05178](/papers/1905.05178/) | Cora | GCN | 0.8778 | 0.8150 | 48 | [Language is All a Graph Needs](/papers/2308.07134/) | published later (2023-08) |
| [2001.05140](/papers/2001.05140/) | Cora | GCN | 0.8778 | 0.8150 | 48 | [Language is All a Graph Needs](/papers/2308.07134/) | published later (2023-08) |
| [2101.00797](/papers/2101.00797/) | Cora | GCN | 0.8778 | 0.8150 | 48 | [Language is All a Graph Needs](/papers/2308.07134/) | published later (2023-08) |
| [2110.09443](/papers/2110.09443/) | Cora | GCN | 0.8778 | 0.8150 | 48 | [Language is All a Graph Needs](/papers/2308.07134/) | published later (2023-08) |
| [2305.17589](/papers/2305.17589/) | Cora | GCN | 0.8778 | 0.8150 | 48 | [Language is All a Graph Needs](/papers/2308.07134/) | published later (2023-08) |
| [2602.02268](/papers/2602.02268/) | Squirrel | GCN | 0.6190 | 0.2917 | 47 | [Beyond Low-frequency Information in Graph Convolutional Networks](/papers/2101.00797/) | already known (2021-01) |
| [2305.17589](/papers/2305.17589/) | COLLAB | GCN | 0.8260 | 0.6380 | 47 | [Scalable Expressiveness through Preprocessed Graph Perturbations](/papers/2406.11714/) | published later (2024-06) |
| [2305.15747](/papers/2305.15747/) | CiteSeer | GCN | 0.7577 | 0.5830 | 47 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2305.15747](/papers/2305.15747/) | Cora | GIN | 0.8565 | 0.7586 | 47 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [1611.08402](/papers/1611.08402/) | Cora | GCN | 0.8778 | 0.8159 | 47 | [Language is All a Graph Needs](/papers/2308.07134/) | published later (2023-08) |
| [2101.00797](/papers/2101.00797/) | Cora | FAGCN | 0.8885 | 0.8410 | 47 | [Language is All a Graph Needs](/papers/2308.07134/) | published later (2023-08) |
| [2106.05234](/papers/2106.05234/) | ZINC | GAT | 0.1110 | 0.3840 | 46 | [Rethinking the Expressive Power of GNNs via Graph...](/papers/2301.09505/) | published later (2023-01) |
| [2110.07875](/papers/2110.07875/) | ZINC | GAT | 0.1110 | 0.3840 | 46 | [Rethinking the Expressive Power of GNNs via Graph...](/papers/2301.09505/) | published later (2023-01) |
| [2205.12454](/papers/2205.12454/) | ZINC | GAT | 0.1110 | 0.3840 | 46 | [Rethinking the Expressive Power of GNNs via Graph...](/papers/2301.09505/) | published later (2023-01) |
| [2301.09505](/papers/2301.09505/) | ZINC | GAT | 0.1110 | 0.3840 | 46 | [Rethinking the Expressive Power of GNNs via Graph...](/papers/2301.09505/) | same paper |
| [2302.08647](/papers/2302.08647/) | ZINC | GAT | 0.1110 | 0.3840 | 46 | [Rethinking the Expressive Power of GNNs via Graph...](/papers/2301.09505/) | already known (2023-01) |
| [2305.06102](/papers/2305.06102/) | ZINC | GAT | 0.1110 | 0.3840 | 46 | [Rethinking the Expressive Power of GNNs via Graph...](/papers/2301.09505/) | already known (2023-01) |
| [2312.01538](/papers/2312.01538/) | ZINC | GAT | 0.1110 | 0.3840 | 46 | [Rethinking the Expressive Power of GNNs via Graph...](/papers/2301.09505/) | already known (2023-01) |
| [2401.17791](/papers/2401.17791/) | ZINC | GAT | 0.1110 | 0.3840 | 46 | [Rethinking the Expressive Power of GNNs via Graph...](/papers/2301.09505/) | already known (2023-01) |
| [2502.00282](/papers/2502.00282/) | ZINC | GAT | 0.1110 | 0.3840 | 46 | [Rethinking the Expressive Power of GNNs via Graph...](/papers/2301.09505/) | already known (2023-01) |
| [2508.05070](/papers/2508.05070/) | ZINC | GAT | 0.1110 | 0.3840 | 46 | [Rethinking the Expressive Power of GNNs via Graph...](/papers/2301.09505/) | already known (2023-01) |
| [2602.02268](/papers/2602.02268/) | ogbg-molhiv | Graphtransformer | 0.8530 | 0.6350 | 46 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | already known (2023-05-27) |
| [2502.02379](/papers/2502.02379/) | NCI1 | GCN | 0.8320 | 0.7170 | 46 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | already known (2023-05-27) |
| [2305.15747](/papers/2305.15747/) | NCI1 | GAT | 0.8450 | 0.7434 | 46 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | published later (2023-05-27) |
| [2301.09505](/papers/2301.09505/) | ZINC | GIN | 0.0140 | 0.0880 | 46 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | published later (2023-06) |
| [2501.18739](/papers/2501.18739/) | ZINC | GIN | 0.0140 | 0.0880 | 46 | [How does over-squashing affect the power of GNNs?](/papers/2306.03589/) | already known (2023-06) |
| [2602.07256](/papers/2602.07256/) | Chameleon | FSGNN | 0.7827 | 0.4330 | 45 | [Edge Directionality Improves Learning on Heterophilic Graphs](/papers/2305.10498/) | already known (2023-05) |
| [2602.07256](/papers/2602.07256/) | Squirrel | GloGNN | 0.6121 | 0.2872 | 45 | [A critical look at the evaluation of GNNs...](/papers/2302.11640/) | already known (2023-02) |
| [2507.00647](/papers/2507.00647/) | Chameleon | GCN | 0.7230 | 0.4089 | 45 | [Beyond Low-frequency Information in Graph Convolutional Networks](/papers/2101.00797/) | already known (2021-01) |
| [2602.07256](/papers/2602.07256/) | Chameleon | GloGNN | 0.7121 | 0.4017 | 45 | [Edge Directionality Improves Learning on Heterophilic Graphs](/papers/2305.10498/) | already known (2023-05) |
| [2305.17589](/papers/2305.17589/) | COLLAB | GIN | 0.8220 | 0.6490 | 45 | [Scalable Expressiveness through Preprocessed Graph Perturbations](/papers/2406.11714/) | published later (2024-06) |
| [1703.06103](/papers/1703.06103/) | MUTAG | WL | 0.9040 | 0.8088 | 45 | [Coloring graph neural networks for node disambiguation](/papers/1912.06058/) | published later (2019-12) |
| [2101.00797](/papers/2101.00797/) | Cora | GraphSAGE | 0.8790 | 0.8230 | 45 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2305.15747](/papers/2305.15747/) | ZINC | UnionSAGE | 0.1146 | 0.3768 | 44 | [Union Subgraph Neural Networks](/papers/2305.15747/) | same paper |
| [2602.02268](/papers/2602.02268/) | Cora | SGFormer | 0.8624 | 0.7703 | 44 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | already known (2026-02) |
| [2602.02268](/papers/2602.02268/) | PubMed | GAT | 0.8328 | 0.7590 | 44 | [Language is All a Graph Needs](/papers/2308.07134/) | already known (2023-08) |
| [2402.08450](/papers/2402.08450/) | ZINC | DS-GNN | 0.0290 | 0.1020 | 44 | [Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via...](/papers/2402.08450/) | same paper |
| [1904.08082](/papers/1904.08082/) | D&D | SortPool | 0.7937 | 0.7253 | 44 | [Hierarchical Graph Representation Learning with Differentiable Pooling](/papers/1806.08804/) | already known (2018-06) |
| [2305.15747](/papers/2305.15747/) | D&D | GraphSAGE | 0.7950 | 0.7310 | 44 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | published later (2023-05-27) |
| [2501.18739](/papers/2501.18739/) | ogbn-arxiv | APPNP | 0.7420 | 0.6940 | 44 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | already known (2023-05-27) |
| [2206.08164](/papers/2206.08164/) | Peptides-func | GatedGCN | 0.6765 | 0.5864 | 43 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | published later (2023-12-03) |
| [2302.08647](/papers/2302.08647/) | Peptides-func | GatedGCN | 0.6765 | 0.5864 | 43 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | published later (2023-12-03) |
| [2303.06147](/papers/2303.06147/) | Peptides-func | GatedGCN | 0.6765 | 0.5864 | 43 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | published later (2023-12-03) |
| [2306.02866](/papers/2306.02866/) | Peptides-func | GatedGCN | 0.6765 | 0.5864 | 43 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | published later (2023-12-03) |
| [2401.17791](/papers/2401.17791/) | Peptides-func | GatedGCN | 0.6765 | 0.5864 | 43 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | already known (2023-12-03) |
| [2402.08450](/papers/2402.08450/) | Peptides-func | GatedGCN | 0.6765 | 0.5864 | 43 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | already known (2023-12-03) |
| [2405.13806](/papers/2405.13806/) | Peptides-func | GatedGCN | 0.6765 | 0.5864 | 43 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | already known (2023-12-03) |
| [2502.00282](/papers/2502.00282/) | Peptides-func | GatedGCN | 0.6765 | 0.5864 | 43 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | already known (2023-12-03) |
| [2508.05070](/papers/2508.05070/) | Peptides-func | GatedGCN | 0.6765 | 0.5864 | 43 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | already known (2023-12-03) |
| [2605.06462](/papers/2605.06462/) | Peptides-func | GatedGCN | 0.6765 | 0.5864 | 43 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | already known (2023-12-03) |
| [2308.07134](/papers/2308.07134/) | Cora | MixHop | 0.8453 | 0.7565 | 43 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2501.18739](/papers/2501.18739/) | Cora | NodeFormer | 0.8744 | 0.8078 | 43 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2305.17589](/papers/2305.17589/) | Cora | GraphSAGE | 0.8790 | 0.8250 | 43 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2305.15747](/papers/2305.15747/) | ogbg-molhiv | GIN | 0.8480 | 0.7060 | 42 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | published later (2023-05-27) |
| [1312.6203](/papers/1312.6203/) | PubMed | GraphSAGE | 0.8685 | 0.7680 | 42 | [Language is All a Graph Needs](/papers/2308.07134/) | published later (2023-08) |
| [2101.00797](/papers/2101.00797/) | Cora | GIN | 0.8565 | 0.7760 | 42 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2301.09505](/papers/2301.09505/) | ZINC | DS-GNN | 0.0290 | 0.0970 | 42 | [Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via...](/papers/2402.08450/) | published later (2024-02-13) |
| [1312.6203](/papers/1312.6203/) | Cora | APPNP | 0.8759 | 0.8150 | 42 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2108.03348](/papers/2108.03348/) | PATTERN | GraphSAGE | 0.8900 | 0.5052 | 41 | [Directional Graph Networks](/papers/2010.02863/) | already known (2020-10) |
| [2305.15747](/papers/2305.15747/) | ogbg-molhiv | GAT | 0.8450 | 0.7060 | 41 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | published later (2023-05-27) |
| [1312.6203](/papers/1312.6203/) | PubMed | GCN | 0.8890 | 0.7770 | 41 | [Language is All a Graph Needs](/papers/2308.07134/) | published later (2023-08) |
| [2501.18739](/papers/2501.18739/) | REDDIT-MULTI-5K | PNA | 0.8560 | 0.3857 | 40 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | already known (2023-05-27) |
| [2602.02268](/papers/2602.02268/) | Cora | Graphormer | 0.8041 | 0.4323 | 40 | [Language is All a Graph Needs](/papers/2308.07134/) | already known (2023-08) |
| [2305.17589](/papers/2305.17589/) | ZINC | GAT | 0.1110 | 0.2850 | 40 | [Rethinking the Expressive Power of GNNs via Graph...](/papers/2301.09505/) | already known (2023-01) |
| [2602.02268](/papers/2602.02268/) | ogbg-molhiv | GCN | 0.8390 | 0.6888 | 40 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | already known (2023-05-27) |
| [2305.15747](/papers/2305.15747/) | ogbg-molhiv | GraphSAGE | 0.8420 | 0.7037 | 40 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | published later (2023-05-27) |
| [1811.05868](/papers/1811.05868/) | PubMed | GCN | 0.8890 | 0.7780 | 40 | [Language is All a Graph Needs](/papers/2308.07134/) | published later (2023-08) |
| [2305.06102](/papers/2305.06102/) | NCI1 | GraphSAGE | 0.8380 | 0.7600 | 40 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | published later (2023-05-27) |
| [2312.01538](/papers/2312.01538/) | NCI1 | GraphSAGE | 0.8380 | 0.7600 | 40 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | already known (2023-05-27) |
| [2602.07256](/papers/2602.07256/) | CiteSeer | GloGNN | 0.7741 | 0.7246 | 40 | [Finding Global Homophily in Graph Neural Networks When...](/papers/2205.07308/) | already known (2022-05-15) |
| [2302.08671](/papers/2302.08671/) | PROTEINS | DiffPool | 0.7810 | 0.7511 | 40 | [Towards Better Graph Representation Learning with Parameterized Decomposition...](/papers/2305.06102/) | published later (2023-05-10) |
| [2502.01122](/papers/2502.01122/) | REDDIT-MULTI-5K | GCN | 0.8350 | 0.2000 | 39 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | already known (2023-05-27) |
| [2602.07256](/papers/2602.07256/) | Squirrel | MLP | 0.6310 | 0.3391 | 39 | [Beyond Low-frequency Information in Graph Convolutional Networks](/papers/2101.00797/) | already known (2021-01) |
| [2108.03348](/papers/2108.03348/) | PATTERN | GCN | 0.8800 | 0.6388 | 39 | [Directional Graph Networks](/papers/2010.02863/) | already known (2020-10) |
| [2108.03348](/papers/2108.03348/) | PATTERN | GAT | 0.9000 | 0.7582 | 39 | [Directional Graph Networks](/papers/2010.02863/) | already known (2020-10) |
| [2303.06147](/papers/2303.06147/) | PATTERN | GAT | 0.9000 | 0.7827 | 39 | [Directional Graph Networks](/papers/2010.02863/) | already known (2020-10) |
| [2002.04025](/papers/2002.04025/) | ogbg-molhiv | GAT | 0.8450 | 0.7290 | 39 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | published later (2023-05-27) |
| [2602.02268](/papers/2602.02268/) | Chameleon | GCN | 0.7230 | 0.4415 | 38 | [Beyond Low-frequency Information in Graph Convolutional Networks](/papers/2101.00797/) | already known (2021-01) |
| [2305.10498](/papers/2305.10498/) | Chameleon | MLP | 0.7430 | 0.4621 | 38 | [Beyond Low-frequency Information in Graph Convolutional Networks](/papers/2101.00797/) | already known (2021-01) |
| [2303.06147](/papers/2303.06147/) | PATTERN | GCN | 0.8800 | 0.7189 | 38 | [Directional Graph Networks](/papers/2010.02863/) | already known (2020-10) |
| [2402.00789](/papers/2402.00789/) | PATTERN | GCN | 0.8800 | 0.7189 | 38 | [Directional Graph Networks](/papers/2010.02863/) | already known (2020-10) |
| [2401.17791](/papers/2401.17791/) | PATTERN | GCN | 0.8800 | 0.7189 | 38 | [Directional Graph Networks](/papers/2010.02863/) | already known (2020-10) |
| [2502.00282](/papers/2502.00282/) | PATTERN | GCN | 0.8800 | 0.7189 | 38 | [Directional Graph Networks](/papers/2010.02863/) | already known (2020-10) |
| [2508.05070](/papers/2508.05070/) | PATTERN | GCN | 0.8800 | 0.7189 | 38 | [Directional Graph Networks](/papers/2010.02863/) | already known (2020-10) |
| [2312.01538](/papers/2312.01538/) | PATTERN | GAT | 0.9000 | 0.7827 | 38 | [Directional Graph Networks](/papers/2010.02863/) | already known (2020-10) |
| [2401.17791](/papers/2401.17791/) | PATTERN | GAT | 0.9000 | 0.7827 | 38 | [Directional Graph Networks](/papers/2010.02863/) | already known (2020-10) |
| [2502.00282](/papers/2502.00282/) | PATTERN | GAT | 0.9000 | 0.7827 | 38 | [Directional Graph Networks](/papers/2010.02863/) | already known (2020-10) |
| [2508.05070](/papers/2508.05070/) | PATTERN | GAT | 0.9000 | 0.7827 | 38 | [Directional Graph Networks](/papers/2010.02863/) | already known (2020-10) |
| [2206.08164](/papers/2206.08164/) | Peptides-func | GINE | 0.6621 | 0.5498 | 38 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | published later (2023-12-03) |
| [2302.08647](/papers/2302.08647/) | Peptides-func | GINE | 0.6621 | 0.5498 | 38 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | published later (2023-12-03) |
| [2303.06147](/papers/2303.06147/) | Peptides-func | GINE | 0.6621 | 0.5498 | 38 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | published later (2023-12-03) |
| [2306.02866](/papers/2306.02866/) | Peptides-func | GINE | 0.6621 | 0.5498 | 38 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | published later (2023-12-03) |
| [2401.17791](/papers/2401.17791/) | Peptides-func | GINE | 0.6621 | 0.5498 | 38 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | already known (2023-12-03) |
| [2405.13806](/papers/2405.13806/) | Peptides-func | GINE | 0.6621 | 0.5498 | 38 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | already known (2023-12-03) |
| [2508.05070](/papers/2508.05070/) | Peptides-func | GINE | 0.6621 | 0.5498 | 38 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | already known (2023-12-03) |
| [2605.06462](/papers/2605.06462/) | Peptides-func | GINE | 0.6621 | 0.5498 | 38 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | already known (2023-12-03) |
| [1611.08402](/papers/1611.08402/) | PubMed | GCN | 0.8890 | 0.7872 | 38 | [Language is All a Graph Needs](/papers/2308.07134/) | published later (2023-08) |
| [1904.08082](/papers/1904.08082/) | D&D | Set2Set | 0.7812 | 0.7127 | 38 | [Hierarchical Graph Representation Learning with Differentiable Pooling](/papers/1806.08804/) | already known (2018-06) |
| [2305.15747](/papers/2305.15747/) | D&D | GCN | 0.7820 | 0.7216 | 38 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | published later (2023-05-27) |
| [2312.01538](/papers/2312.01538/) | Peptides-struct | GRED | 0.2455 | 0.2503 | 38 | [GraphMinNet: Learning Dependencies in Graphs with Light Complexity...](/papers/2502.00282/) | published later (2025-02-01) |
| [2501.18739](/papers/2501.18739/) | REDDIT-MULTI-5K | GIN | 0.8510 | 0.3937 | 37 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | already known (2023-05-27) |
| [2305.15747](/papers/2305.15747/) | ZINC | UnionGCN | 0.1334 | 0.4625 | 37 | [Union Subgraph Neural Networks](/papers/2305.15747/) | same paper |
| [2302.11640](/papers/2302.11640/) | Squirrel | GPR-GNN | 0.5435 | 0.3339 | 37 | [Edge Directionality Improves Learning on Heterophilic Graphs](/papers/2305.10498/) | published later (2023-05) |
| [2406.11714](/papers/2406.11714/) | ogbg-molhiv | GIN | 0.8480 | 0.7400 | 37 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | already known (2023-05-27) |
| [2602.02268](/papers/2602.02268/) | ogbg-molhiv | GAT | 0.8450 | 0.7385 | 37 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | already known (2023-05-27) |
| [2108.03348](/papers/2108.03348/) | PATTERN | GatedGCN | 0.9200 | 0.8448 | 37 | [Directional Graph Networks](/papers/2010.02863/) | already known (2020-10) |
| [2305.15747](/papers/2305.15747/) | NCI1 | GCN | 0.8320 | 0.7591 | 37 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | published later (2023-05-27) |
| [1611.08402](/papers/1611.08402/) | PubMed | DGCNN | 0.8000 | 0.7300 | 37 | [Deep Learning on Graphs: A Survey](/papers/1812.04202/) | published later (2018-12) |
| [2602.02268](/papers/2602.02268/) | PubMed | SGFormer | 0.8030 | 0.7347 | 37 | [Language is All a Graph Needs](/papers/2308.07134/) | already known (2023-08) |
| [2305.17589](/papers/2305.17589/) | MUTAG | GIN | 0.8940 | 0.8300 | 37 | [Coloring graph neural networks for node disambiguation](/papers/1912.06058/) | already known (2019-12) |
| [2410.23686](/papers/2410.23686/) | NCI1 | GIN | 0.8510 | 0.7662 | 36 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | already known (2023-05-27) |
| [2301.09505](/papers/2301.09505/) | ZINC | SUN | 0.0240 | 0.0830 | 36 | [Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via...](/papers/2402.08450/) | published later (2024-02-13) |
| [2402.08450](/papers/2402.08450/) | ZINC | SUN | 0.0240 | 0.0830 | 36 | [Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via...](/papers/2402.08450/) | same paper |
| [2301.09505](/papers/2301.09505/) | ZINC | GNN-AK | 0.0340 | 0.0910 | 36 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2402.08450](/papers/2402.08450/) | ZINC | GNN-AK | 0.0340 | 0.0910 | 36 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [1811.05868](/papers/1811.05868/) | CiteSeer | GAT | 0.7643 | 0.7140 | 36 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2110.09443](/papers/2110.09443/) | CiteSeer | GAT | 0.7643 | 0.7140 | 36 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2101.00797](/papers/2101.00797/) | CiteSeer | FAGCN | 0.7682 | 0.7270 | 36 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2305.15747](/papers/2305.15747/) | ogbg-molhiv | GCN | 0.8390 | 0.7349 | 35 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | published later (2023-05-27) |
| [2002.04025](/papers/2002.04025/) | ogbg-molhiv | GraphSAGE | 0.8420 | 0.7440 | 35 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | published later (2023-05-27) |
| [2005.00687](/papers/2005.00687/) | ogbg-molhiv | GIN | 0.8480 | 0.7520 | 35 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | published later (2023-05-27) |
| [2305.17589](/papers/2305.17589/) | ogbg-molpcba | Graphormer | 0.3139 | 0.2320 | 35 | [Towards Dynamic Message Passing on Graphs](/papers/2410.23686/) | published later (2024-10) |
| [2410.23686](/papers/2410.23686/) | NCI1 | GCN | 0.8320 | 0.7629 | 35 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | already known (2023-05-27) |
| [2501.18739](/papers/2501.18739/) | ZINC | SAT | 0.0360 | 0.0940 | 35 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | same paper |
| [2110.09443](/papers/2110.09443/) | Cora | GAT | 0.8711 | 0.8180 | 35 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2101.00797](/papers/2101.00797/) | CiteSeer | GraphSAGE | 0.7643 | 0.7120 | 35 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2305.17589](/papers/2305.17589/) | CiteSeer | GraphSAGE | 0.7643 | 0.7150 | 35 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [1806.08804](/papers/1806.08804/) | D&D | GraphSAGE | 0.7950 | 0.7542 | 35 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | published later (2023-05-27) |
| [2108.03348](/papers/2108.03348/) | CIFAR10 | GCN | 0.8900 | 0.5571 | 34 | [Spectral Networks and Locally Connected Networks on Graphs](/papers/1312.6203/) | already known (2013-12-21) |
| [2312.01538](/papers/2312.01538/) | CIFAR10 | GCN | 0.8900 | 0.5571 | 34 | [Spectral Networks and Locally Connected Networks on Graphs](/papers/1312.6203/) | already known (2013-12-21) |
| [2401.17791](/papers/2401.17791/) | CIFAR10 | GCN | 0.8900 | 0.5571 | 34 | [Spectral Networks and Locally Connected Networks on Graphs](/papers/1312.6203/) | already known (2013-12-21) |
| [2402.00789](/papers/2402.00789/) | CIFAR10 | GCN | 0.8900 | 0.5571 | 34 | [Spectral Networks and Locally Connected Networks on Graphs](/papers/1312.6203/) | already known (2013-12-21) |
| [2502.00282](/papers/2502.00282/) | CIFAR10 | GCN | 0.8900 | 0.5571 | 34 | [Spectral Networks and Locally Connected Networks on Graphs](/papers/1312.6203/) | already known (2013-12-21) |
| [2508.05070](/papers/2508.05070/) | CIFAR10 | GCN | 0.8900 | 0.5571 | 34 | [Spectral Networks and Locally Connected Networks on Graphs](/papers/1312.6203/) | already known (2013-12-21) |
| [2108.03348](/papers/2108.03348/) | CIFAR10 | GAT | 0.9000 | 0.6422 | 34 | [Spectral Networks and Locally Connected Networks on Graphs](/papers/1312.6203/) | already known (2013-12-21) |
| [2312.01538](/papers/2312.01538/) | CIFAR10 | GAT | 0.9000 | 0.6422 | 34 | [Spectral Networks and Locally Connected Networks on Graphs](/papers/1312.6203/) | already known (2013-12-21) |
| [2401.17791](/papers/2401.17791/) | CIFAR10 | GAT | 0.9000 | 0.6422 | 34 | [Spectral Networks and Locally Connected Networks on Graphs](/papers/1312.6203/) | already known (2013-12-21) |
| [2502.00282](/papers/2502.00282/) | CIFAR10 | GAT | 0.9000 | 0.6422 | 34 | [Spectral Networks and Locally Connected Networks on Graphs](/papers/1312.6203/) | already known (2013-12-21) |
| [2508.05070](/papers/2508.05070/) | CIFAR10 | GAT | 0.9000 | 0.6422 | 34 | [Spectral Networks and Locally Connected Networks on Graphs](/papers/1312.6203/) | already known (2013-12-21) |
| [2406.11714](/papers/2406.11714/) | ogbg-molhiv | GCN | 0.8390 | 0.7410 | 34 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | already known (2023-05-27) |
| [2005.00687](/papers/2005.00687/) | ogbg-molhiv | GCN | 0.8390 | 0.7418 | 34 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | published later (2023-05-27) |
| [2002.04025](/papers/2002.04025/) | ogbg-molhiv | GIN | 0.8480 | 0.7558 | 34 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | published later (2023-05-27) |
| [2210.02997](/papers/2210.02997/) | ogbg-molhiv | GIN | 0.8480 | 0.7558 | 34 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | published later (2023-05-27) |
| [2502.02379](/papers/2502.02379/) | NCI1 | GIN | 0.8510 | 0.7690 | 34 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | already known (2023-05-27) |
| [2103.09430](/papers/2103.09430/) | ogbg-molpcba | Graphormer | 0.3139 | 0.2330 | 34 | [Towards Dynamic Message Passing on Graphs](/papers/2410.23686/) | published later (2024-10) |
| [2309.09384](/papers/2309.09384/) | Cora | GIN | 0.8565 | 0.7920 | 34 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2401.17791](/papers/2401.17791/) | PATTERN | GIN | 0.9100 | 0.8539 | 34 | [Directional Graph Networks](/papers/2010.02863/) | already known (2020-10) |
| [2502.00282](/papers/2502.00282/) | PATTERN | GIN | 0.9100 | 0.8539 | 34 | [Directional Graph Networks](/papers/2010.02863/) | already known (2020-10) |
| [2508.05070](/papers/2508.05070/) | PATTERN | GIN | 0.9100 | 0.8539 | 34 | [Directional Graph Networks](/papers/2010.02863/) | already known (2020-10) |
| [2303.06147](/papers/2303.06147/) | PATTERN | GIN | 0.9100 | 0.8539 | 34 | [Directional Graph Networks](/papers/2010.02863/) | already known (2020-10) |
| [2402.00789](/papers/2402.00789/) | PATTERN | GIN | 0.9100 | 0.8539 | 34 | [Directional Graph Networks](/papers/2010.02863/) | already known (2020-10) |
| [2301.09505](/papers/2301.09505/) | ZINC | Graphormer-GD | 0.0250 | 0.0810 | 34 | [Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via...](/papers/2402.08450/) | published later (2024-02-13) |
| [2401.17791](/papers/2401.17791/) | ZINC | Graphormer-GD | 0.0250 | 0.0810 | 34 | [Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via...](/papers/2402.08450/) | published later (2024-02-13) |
| [2402.08450](/papers/2402.08450/) | ZINC | Graphormer-GD | 0.0250 | 0.0810 | 34 | [Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via...](/papers/2402.08450/) | same paper |
| [2508.05070](/papers/2508.05070/) | ZINC | Graphormer-GD | 0.0250 | 0.0810 | 34 | [Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via...](/papers/2402.08450/) | already known (2024-02-13) |
| [2602.02268](/papers/2602.02268/) | PubMed | DIFFormer | 0.8050 | 0.7587 | 34 | [Transformers over Directed Acyclic Graphs](/papers/2210.13148/) | already known (2022-10-24) |
| [1609.02907](/papers/1609.02907/) | Cornell | LP | 0.7140 | 0.2650 | 33 | [Revisiting Semi-Supervised Learning with Graph Embeddings](/papers/1603.08861/) | already known (2016-03-29) |
| [2108.03348](/papers/2108.03348/) | CIFAR10 | GIN | 0.8900 | 0.5525 | 33 | [Spectral Networks and Locally Connected Networks on Graphs](/papers/1312.6203/) | already known (2013-12-21) |
| [2312.01538](/papers/2312.01538/) | CIFAR10 | GIN | 0.8900 | 0.5525 | 33 | [Spectral Networks and Locally Connected Networks on Graphs](/papers/1312.6203/) | already known (2013-12-21) |
| [2401.17791](/papers/2401.17791/) | CIFAR10 | GIN | 0.8900 | 0.5525 | 33 | [Spectral Networks and Locally Connected Networks on Graphs](/papers/1312.6203/) | already known (2013-12-21) |
| [2502.00282](/papers/2502.00282/) | CIFAR10 | GIN | 0.8900 | 0.5525 | 33 | [Spectral Networks and Locally Connected Networks on Graphs](/papers/1312.6203/) | already known (2013-12-21) |
| [2508.05070](/papers/2508.05070/) | CIFAR10 | GIN | 0.8900 | 0.5525 | 33 | [Spectral Networks and Locally Connected Networks on Graphs](/papers/1312.6203/) | already known (2013-12-21) |
| [2402.00789](/papers/2402.00789/) | CIFAR10 | GIN | 0.8900 | 0.5526 | 33 | [Spectral Networks and Locally Connected Networks on Graphs](/papers/1312.6203/) | already known (2013-12-21) |
| [2305.15747](/papers/2305.15747/) | CiteSeer | GIN | 0.7255 | 0.6310 | 33 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2101.00797](/papers/2101.00797/) | PubMed | GraphSAGE | 0.8685 | 0.7850 | 33 | [Language is All a Graph Needs](/papers/2308.07134/) | published later (2023-08) |
| [2312.01538](/papers/2312.01538/) | PATTERN | GatedGCN | 0.9200 | 0.8557 | 33 | [Directional Graph Networks](/papers/2010.02863/) | already known (2020-10) |
| [2401.17791](/papers/2401.17791/) | PATTERN | GatedGCN | 0.9200 | 0.8557 | 33 | [Directional Graph Networks](/papers/2010.02863/) | already known (2020-10) |
| [2502.00282](/papers/2502.00282/) | PATTERN | GatedGCN | 0.9200 | 0.8557 | 33 | [Directional Graph Networks](/papers/2010.02863/) | already known (2020-10) |
| [2508.05070](/papers/2508.05070/) | PATTERN | GatedGCN | 0.9200 | 0.8557 | 33 | [Directional Graph Networks](/papers/2010.02863/) | already known (2020-10) |
| [2303.06147](/papers/2303.06147/) | PATTERN | GatedGCN | 0.9200 | 0.8557 | 33 | [Directional Graph Networks](/papers/2010.02863/) | already known (2020-10) |
| [2402.00789](/papers/2402.00789/) | PATTERN | GatedGCN | 0.9200 | 0.8557 | 33 | [Directional Graph Networks](/papers/2010.02863/) | already known (2020-10) |
| [1312.6203](/papers/1312.6203/) | PubMed | GAT | 0.8328 | 0.7740 | 33 | [Language is All a Graph Needs](/papers/2308.07134/) | published later (2023-08) |
| [2301.09505](/papers/2301.09505/) | ZINC | URPE | 0.0280 | 0.0860 | 33 | [Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via...](/papers/2402.08450/) | published later (2024-02-13) |
| [2402.08450](/papers/2402.08450/) | ZINC | URPE | 0.0280 | 0.0860 | 33 | [Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via...](/papers/2402.08450/) | same paper |
| [2402.08450](/papers/2402.08450/) | ZINC | PPGN++(6) | 0.0200 | 0.0710 | 33 | [Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via...](/papers/2402.08450/) | same paper |
| [2301.09505](/papers/2301.09505/) | ZINC | CIN (small) | 0.0440 | 0.0940 | 33 | [Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via...](/papers/2402.08450/) | published later (2024-02-13) |
| [2402.08450](/papers/2402.08450/) | ZINC | CIN (small) | 0.0440 | 0.0940 | 33 | [Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via...](/papers/2402.08450/) | same paper |
| [2405.13806](/papers/2405.13806/) | ogbn-arxiv | APPNP | 0.7420 | 0.7190 | 33 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | already known (2023-05-27) |
| [2602.07256](/papers/2602.07256/) | Chameleon | H2GCN | 0.5939 | 0.4089 | 31 | [Edge Directionality Improves Learning on Heterophilic Graphs](/papers/2305.10498/) | already known (2023-05) |
| [1609.02907](/papers/1609.02907/) | PubMed | GCN | 0.8890 | 0.7900 | 31 | [Language is All a Graph Needs](/papers/2308.07134/) | published later (2023-08) |
| [1812.04202](/papers/1812.04202/) | PubMed | GCN | 0.8890 | 0.7900 | 31 | [Language is All a Graph Needs](/papers/2308.07134/) | published later (2023-08) |
| [1902.07153](/papers/1902.07153/) | PubMed | GCN | 0.8890 | 0.7900 | 31 | [Language is All a Graph Needs](/papers/2308.07134/) | published later (2023-08) |
| [1905.05178](/papers/1905.05178/) | PubMed | GCN | 0.8890 | 0.7900 | 31 | [Language is All a Graph Needs](/papers/2308.07134/) | published later (2023-08) |
| [2001.05140](/papers/2001.05140/) | PubMed | GCN | 0.8890 | 0.7900 | 31 | [Language is All a Graph Needs](/papers/2308.07134/) | published later (2023-08) |
| [2101.00797](/papers/2101.00797/) | PubMed | GCN | 0.8890 | 0.7900 | 31 | [Language is All a Graph Needs](/papers/2308.07134/) | published later (2023-08) |
| [2305.17589](/papers/2305.17589/) | Amazon-Computers | GAT | 0.9078 | 0.8230 | 31 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2302.11640](/papers/2302.11640/) | Squirrel | H2GCN | 0.3790 | 0.2945 | 31 | [Edge Directionality Improves Learning on Heterophilic Graphs](/papers/2305.10498/) | published later (2023-05) |
| [2602.02268](/papers/2602.02268/) | ZINC | Exphormer | 0.1110 | 0.1905 | 31 | [GraphMinNet: Learning Dependencies in Graphs with Light Complexity...](/papers/2502.00282/) | already known (2025-02-01) |
| [2302.08671](/papers/2302.08671/) | NCI1 | GCN | 0.8320 | 0.7664 | 31 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | published later (2023-05-27) |
| [2108.03348](/papers/2108.03348/) | PATTERN | GIN | 0.9100 | 0.8559 | 31 | [Directional Graph Networks](/papers/2010.02863/) | already known (2020-10) |
| [2312.01538](/papers/2312.01538/) | PATTERN | GIN | 0.9100 | 0.8559 | 31 | [Directional Graph Networks](/papers/2010.02863/) | already known (2020-10) |
| [2602.17893](/papers/2602.17893/) | ogbn-arxiv | GCN | 0.7310 | 0.6800 | 31 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | already known (2023-05-27) |
| [2305.17589](/papers/2305.17589/) | Cora | APPNP | 0.8759 | 0.8280 | 31 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2501.18739](/papers/2501.18739/) | ZINC | AWE | 0.0590 | 0.0940 | 31 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | same paper |
| [2108.03348](/papers/2108.03348/) | CIFAR10 | GraphSAGE | 0.8800 | 0.6577 | 30 | [Spectral Networks and Locally Connected Networks on Graphs](/papers/1312.6203/) | already known (2013-12-21) |
| [2507.00647](/papers/2507.00647/) | Chameleon | SAGE | 0.5018 | 0.3777 | 30 | [A critical look at the evaluation of GNNs...](/papers/2302.11640/) | already known (2023-02) |
| [2101.00797](/papers/2101.00797/) | PubMed | FAGCN | 0.8998 | 0.7940 | 30 | [Language is All a Graph Needs](/papers/2308.07134/) | published later (2023-08) |
| [2502.00282](/papers/2502.00282/) | ogbg-molhiv | GCN | 0.8390 | 0.7599 | 30 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | already known (2023-05-27) |
| [2002.04025](/papers/2002.04025/) | ogbg-molhiv | GCN | 0.8390 | 0.7606 | 30 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | published later (2023-05-27) |
| [1611.08402](/papers/1611.08402/) | Cora | DGCNN | 0.8350 | 0.7680 | 30 | [Deep Learning on Graphs: A Survey](/papers/1812.04202/) | published later (2018-12) |
| [2402.08450](/papers/2402.08450/) | ZINC | GNN-SSWL | 0.0220 | 0.0700 | 30 | [Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via...](/papers/2402.08450/) | same paper |
| [2501.18739](/papers/2501.18739/) | Cora | GCN | 0.8778 | 0.8414 | 30 | [Language is All a Graph Needs](/papers/2308.07134/) | already known (2023-08) |
| [2602.07256](/papers/2602.07256/) | Squirrel | GCN | 0.6190 | 0.3557 | 29 | [Beyond Low-frequency Information in Graph Convolutional Networks](/papers/2101.00797/) | already known (2021-01) |
| [1811.05868](/papers/1811.05868/) | CiteSeer | MLP | 0.7153 | 0.5910 | 29 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [1811.05868](/papers/1811.05868/) | PubMed | GAT | 0.8328 | 0.7870 | 29 | [Language is All a Graph Needs](/papers/2308.07134/) | published later (2023-08) |
| [2602.07256](/papers/2602.07256/) | Cora | GCNII | 0.8893 | 0.8720 | 29 | [Language is All a Graph Needs](/papers/2308.07134/) | already known (2023-08) |
| [1611.08402](/papers/1611.08402/) | MNIST | ChebNet | 0.9914 | 0.9770 | 29 | [CayleyNets: Graph Convolutional Neural Networks with Complex Rational...](/papers/1705.07664/) | published later (2017-05) |
| [2602.07256](/papers/2602.07256/) | Squirrel | FAGCN | 0.6670 | 0.3652 | 28 | [Beyond Low-frequency Information in Graph Convolutional Networks](/papers/2101.00797/) | already known (2021-01) |
| [2602.07256](/papers/2602.07256/) | Actor | GloGNN | 0.3735 | 0.1980 | 28 | [Finding Global Homophily in Graph Neural Networks When...](/papers/2205.07308/) | already known (2022-05-15) |
| [2502.00282](/papers/2502.00282/) | ogbg-molhiv | GIN | 0.8480 | 0.7707 | 28 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | already known (2023-05-27) |
| [2502.00282](/papers/2502.00282/) | ogbg-molhiv | SAN | 0.8550 | 0.7785 | 28 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | already known (2023-05-27) |
| [1312.6203](/papers/1312.6203/) | CiteSeer | GraphSAGE | 0.7643 | 0.7220 | 28 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [1905.05178](/papers/1905.05178/) | CiteSeer | GAT | 0.7643 | 0.7250 | 28 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2001.05140](/papers/2001.05140/) | CiteSeer | GAT | 0.7643 | 0.7250 | 28 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2101.00797](/papers/2101.00797/) | CiteSeer | GAT | 0.7643 | 0.7250 | 28 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2312.01538](/papers/2312.01538/) | Peptides-struct | DRew | 0.2536 | 0.2781 | 28 | [Invariant-Based Diagnostics for Graph Benchmarks](/papers/2605.06462/) | published later (2026-05) |
| [2312.01538](/papers/2312.01538/) | PATTERN | GCN | 0.8800 | 0.8561 | 28 | [Directional Graph Networks](/papers/2010.02863/) | already known (2020-10) |
| [2005.00687](/papers/2005.00687/) | ogbl-wikikg2 | RotatE | 0.7280 | 0.2530 | 27 | [OGB-LSC: A Large-Scale Challenge for Machine Learning on...](/papers/2103.09430/) | published later (2021-03) |
| [1806.08804](/papers/1806.08804/) | COLLAB | DiffPool | 0.8213 | 0.7548 | 27 | [Towards Dynamic Message Passing on Graphs](/papers/2410.23686/) | published later (2024-10) |
| [1905.05178](/papers/1905.05178/) | COLLAB | DiffPool | 0.8213 | 0.7548 | 27 | [Towards Dynamic Message Passing on Graphs](/papers/2410.23686/) | published later (2024-10) |
| [2101.00797](/papers/2101.00797/) | CiteSeer | GIN | 0.7255 | 0.6610 | 27 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2108.03348](/papers/2108.03348/) | PATTERN | PNA | 0.9300 | 0.8657 | 27 | [Directional Graph Networks](/papers/2010.02863/) | already known (2020-10) |
| [2501.18739](/papers/2501.18739/) | ZINC | GNN-AK | 0.0340 | 0.0800 | 27 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | same paper |
| [2210.13148](/papers/2210.13148/) | Cora | NodeFormer | 0.8744 | 0.8340 | 27 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [1312.6203](/papers/1312.6203/) | CiteSeer | GAT | 0.7643 | 0.7260 | 27 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2305.17589](/papers/2305.17589/) | CiteSeer | GAT | 0.7643 | 0.7280 | 27 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2602.07256](/papers/2602.07256/) | Squirrel | FSGNN | 0.7410 | 0.3728 | 26 | [Edge Directionality Improves Learning on Heterophilic Graphs](/papers/2305.10498/) | already known (2023-05) |
| [2602.02268](/papers/2602.02268/) | Cornell | GCN | 0.6600 | 0.3243 | 26 | [Semi-Supervised Classification with Graph Convolutional Networks](/papers/1609.02907/) | already known (2016-09) |
| [2602.02268](/papers/2602.02268/) | Peptides-func | Exphormer | 0.6527 | 0.4003 | 26 | [GraphMinNet: Learning Dependencies in Graphs with Light Complexity...](/papers/2502.00282/) | already known (2025-02-01) |
| [2302.11640](/papers/2302.11640/) | Chameleon | GCN | 0.7230 | 0.5018 | 26 | [Beyond Low-frequency Information in Graph Convolutional Networks](/papers/2101.00797/) | already known (2021-01) |
| [1904.08082](/papers/1904.08082/) | NCI1 | DiffPool | 0.7690 | 0.6198 | 26 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | published later (2023-12-03) |
| [2602.07256](/papers/2602.07256/) | Chameleon | APPNP | 0.4956 | 0.3793 | 26 | [HopFormer: Sparse Graph Transformers with Explicit Receptive Field...](/papers/2602.02268/) | already known (2026-02) |
| [2305.17589](/papers/2305.17589/) | Amazon-Computers | APPNP | 0.9018 | 0.8280 | 26 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2205.12454](/papers/2205.12454/) | ZINC | CRaWl | 0.0360 | 0.0850 | 26 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2501.18739](/papers/2501.18739/) | ZINC | CRaWl | 0.0360 | 0.0850 | 26 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | same paper |
| [2305.15747](/papers/2305.15747/) | ZINC | GPS | 0.0262 | 0.0740 | 26 | [Union Subgraph Neural Networks](/papers/2305.15747/) | same paper |
| [2602.02268](/papers/2602.02268/) | PubMed | APPNP | 0.8180 | 0.7750 | 26 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | already known (2023-05-27) |
| [1312.6203](/papers/1312.6203/) | Cora | GAT | 0.8711 | 0.8300 | 26 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [1812.04202](/papers/1812.04202/) | Cora | GAT | 0.8711 | 0.8300 | 26 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [1905.05178](/papers/1905.05178/) | Cora | GAT | 0.8711 | 0.8300 | 26 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2001.05140](/papers/2001.05140/) | Cora | GAT | 0.8711 | 0.8300 | 26 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2101.00797](/papers/2101.00797/) | Cora | GAT | 0.8711 | 0.8300 | 26 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2305.17589](/papers/2305.17589/) | Cora | GAT | 0.8711 | 0.8300 | 26 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2405.13806](/papers/2405.13806/) | ogbn-arxiv | GAT | 0.7391 | 0.7182 | 26 | [Training Graph Neural Networks with 1000 Layers](/papers/2106.07476/) | already known (2021-06-14) |
| [2005.00687](/papers/2005.00687/) | ogbl-wikikg2 | DistMult | 0.7210 | 0.3447 | 25 | [OGB-LSC: A Large-Scale Challenge for Machine Learning on...](/papers/2103.09430/) | published later (2021-03) |
| [2005.00687](/papers/2005.00687/) | ogbl-wikikg2 | ComplEx | 0.7250 | 0.3804 | 25 | [OGB-LSC: A Large-Scale Challenge for Machine Learning on...](/papers/2103.09430/) | published later (2021-03) |
| [2305.15747](/papers/2305.15747/) | ENZYMES | GraphSAGE | 0.7180 | 0.5250 | 25 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | published later (2023-05-27) |
| [2305.17589](/papers/2305.17589/) | Amazon-Computers | GCN | 0.8965 | 0.8150 | 25 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2205.07308](/papers/2205.07308/) | ogbn-arxiv | GIN | 0.7380 | 0.7180 | 25 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | published later (2023-05-27) |
| [1609.02907](/papers/1609.02907/) | Cornell | SemiEmb | 0.6540 | 0.2670 | 24 | [Revisiting Semi-Supervised Learning with Graph Embeddings](/papers/1603.08861/) | already known (2016-03-29) |
| [1811.05868](/papers/1811.05868/) | Amazon-Computers | GCN | 0.8965 | 0.8260 | 24 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2110.09443](/papers/2110.09443/) | Amazon-Computers | GCN | 0.8965 | 0.8260 | 24 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | published later (2025-01-30) |
| [2302.11640](/papers/2302.11640/) | Squirrel | CPGNN | 0.3703 | 0.3091 | 24 | [Finding Global Homophily in Graph Neural Networks When...](/papers/2205.07308/) | already known (2022-05-15) |
| [2302.08671](/papers/2302.08671/) | D&D | SAGPool | 0.7645 | 0.7052 | 24 | [Self-Attention Graph Pooling](/papers/1904.08082/) | already known (2019-04-17) |
| [2305.17589](/papers/2305.17589/) | ogbg-molpcba | PNA | 0.2838 | 0.2250 | 24 | [Graph Neural Networks with Learnable Structural and Positional...](/papers/2110.07875/) | already known (2021-10) |
| [2103.09430](/papers/2103.09430/) | ogbg-molpcba | DGN | 0.2885 | 0.2320 | 24 | [Graph Neural Networks with Learnable Structural and Positional...](/papers/2110.07875/) | published later (2021-10) |
| [2110.09443](/papers/2110.09443/) | CiteSeer | CPGNN | 0.7206 | 0.6690 | 24 | [Finding Global Homophily in Graph Neural Networks When...](/papers/2205.07308/) | published later (2022-05-15) |
| [2305.15747](/papers/2305.15747/) | ZINC | UnionGPS | 0.0236 | 0.0681 | 24 | [Union Subgraph Neural Networks](/papers/2305.15747/) | same paper |
| [2101.00797](/papers/2101.00797/) | Cora | APPNP | 0.8759 | 0.8370 | 24 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2009.03509](/papers/2009.03509/) | ogbn-arxiv | JK-Net | 0.7400 | 0.7219 | 24 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | published later (2023-05-27) |
| [2205.07308](/papers/2205.07308/) | ogbn-arxiv | JK-Net | 0.7400 | 0.7220 | 24 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | published later (2023-05-27) |
| [2005.00687](/papers/2005.00687/) | ogbl-wikikg2 | TransE | 0.6850 | 0.2622 | 23 | [OGB-LSC: A Large-Scale Challenge for Machine Learning on...](/papers/2103.09430/) | published later (2021-03) |
| [2305.17589](/papers/2305.17589/) | ogbl-wikikg2 | TransE | 0.6850 | 0.3650 | 23 | [OGB-LSC: A Large-Scale Challenge for Machine Learning on...](/papers/2103.09430/) | already known (2021-03) |
| [2305.17589](/papers/2305.17589/) | ogbl-wikikg2 | RotatE | 0.7280 | 0.4820 | 23 | [OGB-LSC: A Large-Scale Challenge for Machine Learning on...](/papers/2103.09430/) | already known (2021-03) |
| [2305.06102](/papers/2305.06102/) | NCI1 | DGCNN | 0.7640 | 0.5661 | 23 | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | published later (2023-12-03) |
| [2602.07256](/papers/2602.07256/) | Chameleon | NodeFormer | 0.4788 | 0.3492 | 23 | [HopFormer: Sparse Graph Transformers with Explicit Receptive Field...](/papers/2602.02268/) | already known (2026-02) |
| [2108.03348](/papers/2108.03348/) | PATTERN | DGN | 0.9600 | 0.8668 | 23 | [Directional Graph Networks](/papers/2010.02863/) | already known (2020-10) |
| [2303.06147](/papers/2303.06147/) | PATTERN | DGN | 0.9600 | 0.8668 | 23 | [Directional Graph Networks](/papers/2010.02863/) | already known (2020-10) |
| [2401.17791](/papers/2401.17791/) | PATTERN | DGN | 0.9600 | 0.8668 | 23 | [Directional Graph Networks](/papers/2010.02863/) | already known (2020-10) |
| [2508.05070](/papers/2508.05070/) | PATTERN | DGN | 0.9600 | 0.8668 | 23 | [Directional Graph Networks](/papers/2010.02863/) | already known (2020-10) |
| [1312.6203](/papers/1312.6203/) | PubMed | APPNP | 0.8180 | 0.7860 | 23 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | published later (2023-05-27) |
| [2501.18739](/papers/2501.18739/) | ogbn-arxiv | GAT | 0.7391 | 0.7201 | 23 | [Training Graph Neural Networks with 1000 Layers](/papers/2106.07476/) | already known (2021-06-14) |
| [2506.07624](/papers/2506.07624/) | ogbn-arxiv | GAT | 0.7391 | 0.7201 | 23 | [Training Graph Neural Networks with 1000 Layers](/papers/2106.07476/) | already known (2021-06-14) |
| [1806.08804](/papers/1806.08804/) | REDDIT-MULTI-5K | GraphSAGE | 0.8420 | 0.4224 | 22 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | published later (2023-05-27) |
| [1609.02907](/papers/1609.02907/) | Cornell | ManiReg | 0.6340 | 0.2180 | 22 | [Revisiting Semi-Supervised Learning with Graph Embeddings](/papers/1603.08861/) | already known (2016-03-29) |
| [2305.17589](/papers/2305.17589/) | ogbl-wikikg2 | ComplEx | 0.7250 | 0.4510 | 22 | [OGB-LSC: A Large-Scale Challenge for Machine Learning on...](/papers/2103.09430/) | already known (2021-03) |
| [2108.03348](/papers/2108.03348/) | CIFAR10 | PNA | 0.9100 | 0.7035 | 22 | [Spectral Networks and Locally Connected Networks on Graphs](/papers/1312.6203/) | already known (2013-12-21) |
| [2401.17791](/papers/2401.17791/) | CIFAR10 | PNA | 0.9100 | 0.7035 | 22 | [Spectral Networks and Locally Connected Networks on Graphs](/papers/1312.6203/) | already known (2013-12-21) |
| [2508.05070](/papers/2508.05070/) | CIFAR10 | PNA | 0.9100 | 0.7035 | 22 | [Spectral Networks and Locally Connected Networks on Graphs](/papers/1312.6203/) | already known (2013-12-21) |
| [2305.17589](/papers/2305.17589/) | Amazon-Photo | APPNP | 0.9432 | 0.8310 | 22 | [A General Graph Spectral Wavelet Convolution via Chebyshev...](/papers/2405.13806/) | published later (2024-05-22) |
| [2312.01538](/papers/2312.01538/) | NCI1 | GIN | 0.8510 | 0.8000 | 22 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | already known (2023-05-27) |
| [2302.11640](/papers/2302.11640/) | Squirrel | GT | 0.3630 | 0.3161 | 22 | [Cooperative Sheaf Neural Networks](/papers/2507.00647/) | published later (2025-07) |
| [2205.12454](/papers/2205.12454/) | ZINC | GPS | 0.0262 | 0.0700 | 22 | [Union Subgraph Neural Networks](/papers/2305.15747/) | published later (2023-05) |
| [2302.08647](/papers/2302.08647/) | ZINC | GPS | 0.0262 | 0.0700 | 22 | [Union Subgraph Neural Networks](/papers/2305.15747/) | published later (2023-05) |
| [2305.06102](/papers/2305.06102/) | ZINC | GPS | 0.0262 | 0.0700 | 22 | [Union Subgraph Neural Networks](/papers/2305.15747/) | already known (2023-05) |
| [2312.01538](/papers/2312.01538/) | ZINC | GPS | 0.0262 | 0.0700 | 22 | [Union Subgraph Neural Networks](/papers/2305.15747/) | already known (2023-05) |
| [2401.17791](/papers/2401.17791/) | ZINC | GPS | 0.0262 | 0.0700 | 22 | [Union Subgraph Neural Networks](/papers/2305.15747/) | already known (2023-05) |
| [2402.08450](/papers/2402.08450/) | ZINC | GPS | 0.0262 | 0.0700 | 22 | [Union Subgraph Neural Networks](/papers/2305.15747/) | already known (2023-05) |
| [2501.18739](/papers/2501.18739/) | ZINC | GPS | 0.0262 | 0.0700 | 22 | [Union Subgraph Neural Networks](/papers/2305.15747/) | already known (2023-05) |
| [2508.05070](/papers/2508.05070/) | ZINC | GPS | 0.0262 | 0.0700 | 22 | [Union Subgraph Neural Networks](/papers/2305.15747/) | already known (2023-05) |
| [2501.18739](/papers/2501.18739/) | ZINC | GPM | 0.0210 | 0.0640 | 22 | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | same paper |
| [1812.04202](/papers/1812.04202/) | PubMed | GAT | 0.8328 | 0.7900 | 22 | [Language is All a Graph Needs](/papers/2308.07134/) | published later (2023-08) |
| [1902.07153](/papers/1902.07153/) | PubMed | GAT | 0.8328 | 0.7900 | 22 | [Language is All a Graph Needs](/papers/2308.07134/) | published later (2023-08) |
| [1905.05178](/papers/1905.05178/) | PubMed | GAT | 0.8328 | 0.7900 | 22 | [Language is All a Graph Needs](/papers/2308.07134/) | published later (2023-08) |
| [2001.05140](/papers/2001.05140/) | PubMed | GAT | 0.8328 | 0.7900 | 22 | [Language is All a Graph Needs](/papers/2308.07134/) | published later (2023-08) |
| [2101.00797](/papers/2101.00797/) | PubMed | GAT | 0.8328 | 0.7900 | 22 | [Language is All a Graph Needs](/papers/2308.07134/) | published later (2023-08) |
| [2602.07256](/papers/2602.07256/) | Squirrel | H2GCN | 0.3790 | 0.3402 | 22 | [Edge Directionality Improves Learning on Heterophilic Graphs](/papers/2305.10498/) | already known (2023-05) |
| [2305.17589](/papers/2305.17589/) | ogbl-wikikg2 | DistMult | 0.7210 | 0.4380 | 21 | [OGB-LSC: A Large-Scale Challenge for Machine Learning on...](/papers/2103.09430/) | already known (2021-03) |
| [2302.11640](/papers/2302.11640/) | Chameleon | GPR-GNN | 0.6285 | 0.4726 | 21 | [Edge Directionality Improves Learning on Heterophilic Graphs](/papers/2305.10498/) | published later (2023-05) |
| [2302.11640](/papers/2302.11640/) | Chameleon | H2GCN | 0.5939 | 0.4627 | 21 | [Edge Directionality Improves Learning on Heterophilic Graphs](/papers/2305.10498/) | published later (2023-05) |
| [1609.02907](/papers/1609.02907/) | PubMed | DeepWalk | 0.7680 | 0.6530 | 21 | [Simplifying Graph Convolutional Networks](/papers/1902.07153/) | published later (2019-02-19) |
| [1611.08402](/papers/1611.08402/) | PubMed | DeepWalk | 0.7680 | 0.6530 | 21 | [Simplifying Graph Convolutional Networks](/papers/1902.07153/) | published later (2019-02-19) |
| [1905.05178](/papers/1905.05178/) | PubMed | DeepWalk | 0.7680 | 0.6530 | 21 | [Simplifying Graph Convolutional Networks](/papers/1902.07153/) | already known (2019-02-19) |
| [2001.05140](/papers/2001.05140/) | PubMed | DeepWalk | 0.7680 | 0.6530 | 21 | [Simplifying Graph Convolutional Networks](/papers/1902.07153/) | already known (2019-02-19) |
| [2507.00647](/papers/2507.00647/) | Chameleon | GT-sep | 0.5033 | 0.4031 | 21 | [A critical look at the evaluation of GNNs...](/papers/2302.11640/) | already known (2023-02) |
| [1609.02907](/papers/1609.02907/) | CiteSeer | GCN | 0.7577 | 0.7030 | 21 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [1905.05178](/papers/1905.05178/) | CiteSeer | GCN | 0.7577 | 0.7030 | 21 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2001.05140](/papers/2001.05140/) | CiteSeer | GCN | 0.7577 | 0.7030 | 21 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2101.00797](/papers/2101.00797/) | CiteSeer | GCN | 0.7577 | 0.7030 | 21 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2205.07308](/papers/2205.07308/) | ogbn-arxiv | GAT | 0.7391 | 0.7240 | 21 | [Training Graph Neural Networks with 1000 Layers](/papers/2106.07476/) | already known (2021-06-14) |
| [1806.08804](/papers/1806.08804/) | ENZYMES | GraphSAGE | 0.7180 | 0.5425 | 20 | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | published later (2023-05-27) |
| [2305.17589](/papers/2305.17589/) | Amazon-Photo | GAT | 0.9387 | 0.8350 | 20 | [A General Graph Spectral Wavelet Convolution via Chebyshev...](/papers/2405.13806/) | published later (2024-05-22) |
| [2602.07256](/papers/2602.07256/) | Chameleon | DIFFormer | 0.4854 | 0.3916 | 20 | [HopFormer: Sparse Graph Transformers with Explicit Receptive Field...](/papers/2602.02268/) | already known (2026-02) |
>>>>>>> Stashed changes
