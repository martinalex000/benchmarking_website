---
title: Page of Shame
type: dev
description: Papers whose reported model values materially disagree with the stored
  benchmark values
---

## Page of Shame: Papers Using Wrong Model Values

This page lists papers whose reported primary-metric value for a model disagrees with the stored global benchmark value by more than the reported std, or differs at all when no std is given.

**Flagged papers:** 434
**Flagged rows:** 6249
**Rows where a better value was already known at publication time:** 3014
**Rows whose current best source is from a later paper:** 3197
**Rows whose current best source is the same paper:** 38
**Rows with unknown timing:** 0

### Most affected datasets

| Dataset | Wrong Rows | Papers | Models | Worst Rank Shift | Earlier-known Rows |
|---|---:|---:|---:|---:|---:|
| Cora | 818 | 169 | 161 | 925 | 246 |
| PubMed | 676 | 130 | 122 | 711 | 264 |
| CiteSeer | 662 | 137 | 126 | 801 | 344 |
| ogbn-arxiv | 269 | 64 | 71 | 415 | 88 |
| Chameleon | 240 | 42 | 46 | 242 | 173 |
| ZINC | 234 | 31 | 48 | 150 | 80 |
| Squirrel | 227 | 38 | 44 | 203 | 157 |
| Actor | 170 | 27 | 40 | 189 | 77 |
| Amazon-Computers | 147 | 36 | 39 | 226 | 48 |
| Texas | 146 | 35 | 28 | 229 | 88 |
| Cornell | 135 | 36 | 32 | 242 | 78 |
| Amazon-Photo | 125 | 36 | 37 | 259 | 48 |
| PROTEINS | 124 | 47 | 31 | 309 | 84 |
| Wisconsin | 121 | 31 | 28 | 235 | 67 |
| QM9 | 118 | 27 | 35 | 148 | 61 |
| MUTAG | 108 | 41 | 33 | 319 | 53 |
| NCI1 | 103 | 31 | 26 | 210 | 74 |
| Coauthor-CS | 99 | 26 | 27 | 192 | 35 |
| D&D | 94 | 36 | 45 | 325 | 53 |
| ogbg-molhiv | 74 | 24 | 24 | 172 | 31 |
| BBBP | 72 | 23 | 29 | 124 | 35 |
| ogbn-products | 68 | 24 | 23 | 131 | 26 |
| IMDB-BINARY | 64 | 27 | 25 | 265 | 35 |
| Peptides-func | 60 | 18 | 12 | 77 | 39 |
| WikiCS | 55 | 15 | 26 | 169 | 38 |

### Most affected models

| Model | Wrong Rows | Papers | Datasets | Worst Rank Shift | Earlier-known Rows |
|---|---:|---:|---:|---:|---:|
| GCN | 966 | 265 | 70 | 925 | 550 |
| GAT | 697 | 197 | 63 | 891 | 271 |
| GraphSAGE | 311 | 109 | 46 | 910 | 110 |
| GIN | 282 | 101 | 50 | 736 | 161 |
| APPNP | 239 | 61 | 19 | 763 | 109 |
| MLP | 188 | 50 | 21 | 653 | 68 |
| SGC | 159 | 57 | 18 | 843 | 50 |
| DGI | 129 | 42 | 23 | 701 | 86 |
| H2GCN | 109 | 30 | 15 | 855 | 36 |
| GPRGNN | 89 | 22 | 16 | 748 | 56 |
| GCNII | 83 | 27 | 16 | 606 | 53 |
| DeepWalk | 81 | 35 | 9 | 543 | 17 |
| FAGCN | 71 | 17 | 13 | 805 | 37 |
| ChebNet | 71 | 28 | 13 | 803 | 18 |
| GRACE | 70 | 20 | 11 | 905 | 24 |
| GatedGCN | 66 | 28 | 9 | 148 | 40 |
| DGCNN | 61 | 27 | 13 | 509 | 40 |
| GraphCL | 55 | 21 | 19 | 777 | 26 |
| GloGNN | 55 | 15 | 16 | 616 | 33 |
| JK-Net | 55 | 23 | 11 | 476 | 21 |
| PNA | 50 | 29 | 22 | 151 | 20 |
| BGRL | 48 | 12 | 12 | 515 | 19 |
| MixHop | 46 | 15 | 9 | 579 | 13 |
| DiffPool | 44 | 22 | 7 | 284 | 24 |
| NodeFormer | 43 | 14 | 14 | 751 | 26 |

| ArXiv | Title | Wrong Rows | Earlier-known Rows | Worst Rank Shift | Datasets | Models |
|---|---|---:|---:|---:|---|---|
| [2305.17589](/papers/2305.17589/) | [Graph Inductive Biases in Transformers without Message Passing](/papers/2305.17589/) | 102 | 56 | 486 | Amazon-Computers, Amazon-Photo, COLLAB, CiteSeer | APPNP, ChebNet, CompGCN, ComplEx |
| [2211.15081](/papers/2211.15081/) | [Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane...](/papers/2211.15081/) | 98 | 26 | 628 | Actor, Chameleon, CiteSeer, Cora | ACMGCN, APPNP, Auto-HeG, FAGCN |
| [2601.01207](/papers/2601.01207/) | [Sparse Bayesian Message Passing under Structural Uncertainty](/papers/2601.01207/) | 97 | 95 | 490 | Actor, Amazon-ratings, Chameleon, Cora | ACMGCN, Auto-HeG, CPGNN, Dir-GNN |
| [2602.07256](/papers/2602.07256/) | [Graph homophily booster: Reimagining the role of discrete features in...](/papers/2602.07256/) | 83 | 81 | 616 | Actor, Chameleon, CiteSeer, Cora | APPNP, ChebNet, DAGNN, DIFFormer |
| [2205.13700](/papers/2205.13700/) | [ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge Splitting](/papers/2205.13700/) | 71 | 13 | 634 | Actor, Chameleon, CiteSeer, Cora | ACMGCN, DisGNN, DisenGCN, FAGCN |
| [2205.15127](/papers/2205.15127/) | [Universal Deep GNNs: Rethinking Residual Connection in GNNs from a...](/papers/2205.15127/) | 68 | 16 | 376 | Actor, Chameleon, CiteSeer, Cora | APPNP, DAGNN, FAGCN, GAT |
| [2209.15454](/papers/2209.15454/) | [GPNet: Simplifying Graph Neural Networks via Multi-channel Geometric Polynomials](/papers/2209.15454/) | 61 | 29 | 486 | Chameleon, CiteSeer, Cora, Cornell | APPNP, FAGCN, GAT, GCN |
| [2512.24062](/papers/2512.24062/) | [Energy-Balanced Hyperspherical Graph Representation Learning via Structural Binding and Entropic...](/papers/2512.24062/) | 58 | 57 | 640 | Amazon-Computers, Amazon-Photo, CiteSeer, Coauthor-CS | BGRL, CCA-SSG, DGI, DeepWalk |
| [2206.08005](/papers/2206.08005/) | [Evaluating Self-Supervised Learning for Molecular Graph Embeddings](/papers/2206.08005/) | 56 | 3 | 102 | BACE, BBBP, ClinTox, SIDER | AttrMask, EdgePred, GPT-GNN, GROVER |
| [2602.02268](/papers/2602.02268/) | [HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control](/papers/2602.02268/) | 55 | 54 | 803 | Chameleon, Cora, Cornell, Peptides-func | APPNP, DIFFormer, Exphormer, GAT |
| [2307.16026](/papers/2307.16026/) | [MUSE: Multi-View Contrastive Learning for Heterophilic Graphs](/papers/2307.16026/) | 55 | 32 | 613 | Actor, Chameleon, CiteSeer, Cora | BGRL, DGI, GAT, GCN |
| [2305.15747](/papers/2305.15747/) | [Union Subgraph Neural Networks](/papers/2305.15747/) | 53 | 13 | 726 | Amazon-Computers, Amazon-Photo, BBBP, CiteSeer | GAT, GCN, GIN, GPS |
| [2404.15354](/papers/2404.15354/) | [Polynomial Selection in Spectral Graph Neural Networks: An Error-Sum of...](/papers/2404.15354/) | 52 | 30 | 259 | Amazon-Computers, Amazon-Photo, CiteSeer, Cora | ACMGCN, BernNet, ChebNet, GCN |
| [2402.08023](/papers/2402.08023/) | [UGMAE: A Unified Framework for Graph Masked Autoencoders](/papers/2402.08023/) | 51 | 34 | 486 | BACE, BBBP, COLLAB, CiteSeer | BGRL, CCA-SSG, ContextPred, DGI |
| [2210.08792](/papers/2210.08792/) | [Unifying Graph Contrastive Learning with Flexible Contextual Scopes](/papers/2210.08792/) | 50 | 12 | 613 | Amazon-Computers, Amazon-Photo, CiteSeer, Coauthor-CS | BGRL, DGI, DeepWalk, GAE |
| [2202.08480](/papers/2202.08480/) | [Eliciting Structural and Semantic Global Knowledge in Unsupervised Graph Contrastive...](/papers/2202.08480/) | 47 | 10 | 648 | Amazon-Photo, CiteSeer, Coauthor-CS, Cora | DGI, GAT, GCN, GMI |
| [2311.05767](/papers/2311.05767/) | [Dirichlet Energy Enhancement of Graph Neural Networks by Framelet Augmentation](/papers/2311.05767/) | 47 | 22 | 559 | Chameleon, CiteSeer, Cora, PubMed | EGNN, FAGCN, GAT, GCN |
| [2306.10759](/papers/2306.10759/) | [SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations](/papers/2306.10759/) | 46 | 14 | 482 | Actor, CiteSeer, Cora, Pokec | APPNP, CPGNN, GAT, GCN |
| [2301.12063](/papers/2301.12063/) | [HAT-GAE: Self-Supervised Graph Auto-encoders with Hierarchical Adaptive Masking and Trainable...](/papers/2301.12063/) | 46 | 15 | 471 | Amazon-Computers, CiteSeer, Coauthor-CS, Coauthor-Physics | BGRL, CCA-SSG, DGI, GAE |
| [2306.07608](/papers/2306.07608/) | [Finding the Missing-half: Graph Complementary Learning for Homophily-prone and Heterophily-prone...](/papers/2306.07608/) | 46 | 17 | 271 | Actor, Amazon-Computers, Amazon-Photo, Chameleon | APPNP, ChebNet, GAT, GCN |
| [2305.06142](/papers/2305.06142/) | [arXiv:2305.06142](/papers/2305.06142/) | 46 | 12 | 156 | Actor, Amazon-Computers, Amazon-Photo, Chameleon | APPNP, BernNet, ChebNet, FSGNN |
| [2206.14418](/papers/2206.14418/) | [Optimization-Induced Graph Implicit Nonlinear Diffusion](/papers/2206.14418/) | 45 | 27 | 239 | Chameleon, CiteSeer, Cora, Cornell | APPNP, DGCNN, GAT, GCN |
| [2302.09755](/papers/2302.09755/) | [Finding Heterophilic Neighbors via Confidence-based Subgraph Matching for Semi-supervised Node...](/papers/2302.09755/) | 44 | 17 | 628 | Actor, Chameleon, CiteSeer, PubMed | APPNP, DropEdge, FAGCN, GAT |
| [2411.02279](/papers/2411.02279/) | [arXiv:2411.02279](/papers/2411.02279/) | 44 | 34 | 527 | Amazon-Computers, Amazon-Photo, Chameleon, CiteSeer | APPNP, CoGSL, GAT, GCN |
| [2412.17856](/papers/2412.17856/) | [Graph Structure Refinement with Energy-based Contrastive Learning](/papers/2412.17856/) | 43 | 37 | 521 | Actor, CiteSeer, Cornell, MUTAG | CoGSL, DGCNN, GAT, GCN |
| [2605.14809](/papers/2605.14809/) | [arXiv:2605.14809](/papers/2605.14809/) | 42 | 41 | 923 | Amazon-Photo, Chameleon, Cora, Cornell | All-In-One, DGI, GAT, GCN |
| [2505.19024](/papers/2505.19024/) | [arXiv:2505.19024](/papers/2505.19024/) | 42 | 35 | 384 | Amazon-Photo, CiteSeer, Coauthor-Physics, Cora | AD-GCL, BGRL, DGI, GAT |
| [2508.05070](/papers/2508.05070/) | [Tango: Graph Neural Dynamics via Learned Energy and Tangential Flows](/papers/2508.05070/) | 42 | 31 | 149 | Amazon-ratings, CIFAR10, CLUSTER, MNIST | DGN, DRew-GCN, GAT, GCN |
| [2310.10064](/papers/2310.10064/) | [arXiv:2310.10064](/papers/2310.10064/) | 41 | 21 | 337 | Chameleon, CiteSeer, Cora, Cornell | APPNP, BernNet, ChebNet, GCN |
| [2501.18739](/papers/2501.18739/) | [Beyond Message Passing: Neural Graph Pattern Machine](/papers/2501.18739/) | 40 | 20 | 468 | Amazon-Computers, COLLAB, Cora, IMDB-BINARY | APPNP, AWE, AgentNet, CRaWl |
| [2502.20885](/papers/2502.20885/) | [A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning](/papers/2502.20885/) | 39 | 33 | 551 | Actor, Chameleon, CiteSeer, Coauthor-CS | BGRL, DGI, DSSL, GRACE |
| [2407.07457](/papers/2407.07457/) | [GLBench: A Comprehensive Benchmark for Graph with Large Language Models](/papers/2407.07457/) | 38 | 23 | 663 | CiteSeer, Cora, PubMed, Reddit | ENGINE, GAT, GCN, GIANT |
| [2108.00955](/papers/2108.00955/) | [Evaluating Deep Graph Neural Networks](/papers/2108.00955/) | 37 | 4 | 559 | CiteSeer, Cora, PubMed, ogbn-arxiv | AP-GCN, APPNP, DAGNN, GCN |
| [2411.12330](/papers/2411.12330/) | [Graph as a Feature: A Graph-Aware Non-Neural Model for Node...](/papers/2411.12330/) | 37 | 35 | 528 | Actor, Amazon-Photo, CiteSeer, Coauthor-CS | APPNP, GAT, GCN, GCNII |
| [1710.10321](/papers/1710.10321/) | [arXiv:1710.10321](/papers/1710.10321/) | 37 | 0 | 502 | CiteSeer, Cora, PPI, Reddit | APPNP, ChebNet, GAT, GCN |
| [2502.11836](/papers/2502.11836/) | [Model Generalization on Text Attribute Graphs: Principles with Large Language...](/papers/2502.11836/) | 36 | 24 | 902 | CiteSeer, Cora, Cornell, D&D | DGI, GPT-3.5-turbo, GraphGPS, GraphMAE |
| [2102.03147](/papers/2102.03147/) | [Learning Conjoint Attentions for Graph Neural Nets](/papers/2102.03147/) | 36 | 2 | 500 | CiteSeer, Coauthor-CS, Cora, PubMed | APPNP, ARMA, GAT, GCN |
| [2602.00064](/papers/2602.00064/) | [SPGCL: Simple yet Powerful Graph Contrastive Learning via SVD-Guided Structural...](/papers/2602.00064/) | 35 | 33 | 843 | Actor, Amazon-Photo, Chameleon, CiteSeer | DropEdge, GAT, GCN, Geom-GCN |
| [2410.05593](/papers/2410.05593/) | [When Graph Neural Networks Meet Dynamic Mode Decomposition](/papers/2410.05593/) | 35 | 28 | 597 | CiteSeer, Cora, Cornell, PubMed | APPNP, GAT, GCN, GPRGNN |
| [2105.07634](/papers/2105.07634/) | [Improving Graph Neural Networks with Simple Architecture Design](/papers/2105.07634/) | 35 | 5 | 376 | Actor, Chameleon, CiteSeer, Cora | GAT, GCN, GCNII, Geom-GCN |
| [2108.01660](/papers/2108.01660/) | [Graph Neural Networks With Lifting-based Adaptive Graph Wavelets](/papers/2108.01660/) | 34 | 10 | 656 | Cora, D&D, MUTAG, NCI1 | CayleyNets, ChebNet, DeepWalk, GAT |
| [2603.00568](/papers/2603.00568/) | [Enhancing Molecular Property Predictions by Learning from Bond Modelling and...](/papers/2603.00568/) | 34 | 34 | 93 | BACE, BBBP, ClinTox, PCQM4Mv2 | 3D-MGP, ALIGNN, AttrMask, ContextPred |
| [2305.13315](/papers/2305.13315/) | [3D Molecular Geometry Analysis with 2D Graphs](/papers/2305.13315/) | 34 | 5 | 85 | BACE, BBBP, ClinTox, Tox21 | AttrMask, ContextPred, EdgePred, GraphCL |
| [2503.12563](/papers/2503.12563/) | [Diffusion on Graph: Augmentation of Graph Structure for Node Classification](/papers/2503.12563/) | 33 | 21 | 476 | Chameleon, CiteSeer, Cora, PubMed | ACMGCN, APPNP, BGRL, DGI |
| [2212.04604](/papers/2212.04604/) | [Localized Graph Contrastive Learning](/papers/2212.04604/) | 33 | 9 | 437 | Actor, Amazon-Photo, Chameleon, CiteSeer | BGRL, CCA-SSG, DGI, GCA |
| [2401.17791](/papers/2401.17791/) | [Graph Transformers without Positional Encodings](/papers/2401.17791/) | 33 | 26 | 149 | CIFAR10, CLUSTER, MNIST, PATTERN | CIN, DGN, GAT, GCN |
| [2506.20362](/papers/2506.20362/) | [Self-Supervised Graph Learning via Spectral Bootstrapping and Laplacian-Based Augmentations](/papers/2506.20362/) | 32 | 30 | 265 | Amazon-Computers, Amazon-Photo, BBBP, Coauthor-CS | AD-GCL, DGI, GAT, GCA |
| [2108.03348](/papers/2108.03348/) | [Global Self-Attention as a Replacement for Graph Convolution](/papers/2108.03348/) | 32 | 18 | 148 | CIFAR10, MNIST, PATTERN, PCQM4Mv2 | DGN, EGT, GAT, GCN |
| [2410.10320](/papers/2410.10320/) | [DiRW: Path-Aware Digraph Learning for Heterophily](/papers/2410.10320/) | 31 | 16 | 645 | Actor, Amazon-Computers, Chameleon, CiteSeer | ADPA, DGCNN, DIMPA, DiGCN |
| [2506.08871](/papers/2506.08871/) | [Adapting to Heterophilic Graph Data with Structure-Guided Neighbor Discovery](/papers/2506.08871/) | 31 | 28 | 611 | Actor, Chameleon, CiteSeer, Cora | Dir-GNN, FAGCN, GAT, GCN |
| [2207.08629](/papers/2207.08629/) | [Comprehensive Graph Gradual Pruning for Sparse Training in Graph Neural...](/papers/2207.08629/) | 30 | 9 | 242 | Actor, Cornell, Texas, Wisconsin | APPNP, FAGCN, GCN, GPRGNN |
| [1911.05954](/papers/1911.05954/) | [Hierarchical Graph Pooling with Structure Learning](/papers/1911.05954/) | 30 | 13 | 226 | D&D, ENZYMES, MUTAG, NCI1 | DGCNN, DiffPool, GAT, GCN |
| [2202.10720](/papers/2202.10720/) | [EIGNN: Efficient Infinite-Depth Graph Neural Networks](/papers/2202.10720/) | 30 | 6 | 189 | Chameleon, Cornell, Squirrel, Texas | APPNP, GAT, GCN, GCNII |
| [2601.02662](/papers/2601.02662/) | [When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph...](/papers/2601.02662/) | 29 | 23 | 884 | Amazon-Computers, Amazon-Photo, CiteSeer, Coauthor-CS | GAT, GCN, GPPT, GraphPrompt |
| [2403.16358](/papers/2403.16358/) | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | 29 | 13 | 284 | Amazon-Computers, Amazon-Photo, CiteSeer, Coauthor-CS | APPNP, ChebNet, GAT, GCN |
| [2103.07295](/papers/2103.07295/) | [Adversarial Graph Disentanglement with Component-specific Aggregation](/papers/2103.07295/) | 28 | 4 | 570 | Amazon-Computers, Amazon-Photo, CiteSeer, Coauthor-CS | AD-GCN, AP-GCN, APPNP, ChebNet |
| [2506.22299](/papers/2506.22299/) | [CoATA: Effective Co-Augmentation of Topology and Attribute for Graph Neural...](/papers/2506.22299/) | 28 | 26 | 482 | CiteSeer, Coauthor-CS, Coauthor-Physics, Cora | APPNP, GAT, GCN, GloGNN |
| [2209.08264](/papers/2209.08264/) | [Make Heterophily Graphs Better Fit GNN: A Graph Rewiring Approach](/papers/2209.08264/) | 28 | 18 | 228 | Chameleon, CiteSeer, Cornell, Squirrel | APPNP, GAT, GAT + Vanilla, GCN |
| [2510.17185](/papers/2510.17185/) | [Robustness in Text-Attributed Graph Learning: Insights, Trade-offs, and New Defenses](/papers/2510.17185/) | 27 | 26 | 766 | CiteSeer, Cora, PubMed, WikiCS | APPNP, EvenNet, GAT, GCN |
| [2004.13970](/papers/2004.13970/) | [Directed Graph Convolutional Network](/papers/2004.13970/) | 27 | 3 | 685 | Amazon-Computers, Amazon-Photo, CiteSeer, Cora | ChebNet, DGCNN, GAT, GCN |
| [2105.11689](/papers/2105.11689/) | [Self-Supervised Graph Representation Learning via Topology Transformations](/papers/2105.11689/) | 27 | 3 | 486 | CiteSeer, Cora, PubMed | CNNs, DGI, DeepWalk, GAT |
| [2302.11640](/papers/2302.11640/) | [A critical look at the evaluation of GNNs under heterophily:...](/papers/2302.11640/) | 27 | 8 | 143 | Amazon-ratings, Chameleon, Roman-empire, Squirrel | CPGNN, FAGCN, FSGNN, GAT |
| [2505.22362](/papers/2505.22362/) | [Directed Homophily-Aware Graph Neural Network](/papers/2505.22362/) | 26 | 18 | 865 | Chameleon, Cora, Roman-empire, Squirrel | ACMGCN, Dir-GNN, FSGNN, GAT |
| [2102.06986](/papers/2102.06986/) | [How Framelets Enhance Graph Neural Networks](/papers/2102.06986/) | 26 | 5 | 656 | CiteSeer, Cora, D&D, PROTEINS | DGCNN, DeepWalk, DeeperGCN, GAT |
| [2601.08230](/papers/2601.08230/) | [GADPN: Graph Adaptive Denoising and Perturbation Networks via Singular Value...](/papers/2601.08230/) | 26 | 19 | 539 | Chameleon, CiteSeer, Cora | APPNP, DAGNN, FAGCN, GAT |
| [2410.08524](/papers/2410.08524/) | [IGNN-Solver: A Graph Neural Solver for Implicit Graph Neural Networks](/papers/2410.08524/) | 26 | 19 | 270 | Amazon-Computers, MUTAG, NCI1, PROTEINS | ACMGCN, APPNP, DGCNN, EGNN |
| [2005.00687](/papers/2005.00687/) | [Open Graph Benchmark: Datasets for Machine Learning on Graphs](/papers/2005.00687/) | 26 | 0 | 226 | Code, ogbg-molhiv, ogbg-molpcba, ogbl-ddi | Cluster-GCN, ComplEx, DistMult, GCN |
| [2312.01538](/papers/2312.01538/) | [Recurrent Distance Filtering for Graph Representation Learning](/papers/2312.01538/) | 26 | 18 | 218 | CIFAR10, NCI1, PATTERN, PROTEINS | DGCNN, DRew, DiffPool, GAT |
| [2507.00647](/papers/2507.00647/) | [Cooperative Sheaf Neural Networks](/papers/2507.00647/) | 26 | 26 | 201 | Amazon-ratings, Chameleon, Cornell, Film | ACMGCN, GAT, GCN, GPR-GNN |
| [2209.05481](/papers/2209.05481/) | [A Molecular Multimodal Foundation Model Associating Molecule Graphs with Natural...](/papers/2209.05481/) | 26 | 10 | 113 | BACE, BBBP, ClinTox, ESOL | GAT, GCN, GIN, GraphSAGE |
| [2502.08092](/papers/2502.08092/) | [GCoT: Chain-of-Thought Prompt Learning for Graphs](/papers/2502.08092/) | 25 | 16 | 919 | Amazon-Photo, Chameleon, CiteSeer, Cora | DGI, GAT, GCN, GPF |
| [2505.17660](/papers/2505.17660/) | [DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer for Node...](/papers/2505.17660/) | 25 | 22 | 801 | Amazon-Computers, Amazon-Photo, Amazon2M, Coauthor-CS | ANS-GT, APPNP, GAT, GCN |
| [2402.11235](/papers/2402.11235/) | [ZeroG: Investigating Cross-dataset Zero-shot Transferability in Graphs](/papers/2402.11235/) | 25 | 14 | 774 | CiteSeer, Cora, PubMed | DGI, GAT, GCN, GraphCL |
| [2411.17676](/papers/2411.17676/) | [Instance-Aware Graph Prompt Learning](/papers/2411.17676/) | 25 | 24 | 597 | BACE, BBBP, CiteSeer, ClinTox | GAT, GCN, GIN, GraphSAGE |
| [2101.00797](/papers/2101.00797/) | [Beyond Low-frequency Information in Graph Convolutional Networks](/papers/2101.00797/) | 25 | 1 | 526 | CiteSeer, Cora, PubMed | APPNP, ChebNet, FAGCN, GAT |
| [2007.02133](/papers/2007.02133/) | [arXiv:2007.02133](/papers/2007.02133/) | 25 | 1 | 486 | Chameleon, Cora, Cornell, PPI | APPNP, GAT, GCN, GCNII |
| [2406.08210](/papers/2406.08210/) | [arXiv:2406.08210](/papers/2406.08210/) | 25 | 16 | 149 | Peptides-func, Peptides-struct, ZINC | AUTOBAHN, CIN, CIN (small), FragNet |
| [2502.09365](/papers/2502.09365/) | [Simple Path Structural Encoding for Graph Transformers](/papers/2502.09365/) | 25 | 24 | 149 | CIFAR10, CLUSTER, MNIST, PATTERN | GAT, GCN, GIN, GINE |
| [2309.04589](/papers/2309.04589/) | [Motif-aware Attribute Masking for Molecular Graph Pre-training](/papers/2309.04589/) | 25 | 11 | 123 | BACE, BBBP, ClinTox, SIDER | AttrMask, ContextPred, GROVER, JOAO |
| [2410.23686](/papers/2410.23686/) | [Towards Dynamic Message Passing on Graphs](/papers/2410.23686/) | 24 | 24 | 262 | COLLAB, IMDB-BINARY, IMDB-MULTI, NCI1 | DiffPool, GCN, GIN, GraphSAGE |
| [2205.12454](/papers/2205.12454/) | [Recipe for a General, Powerful, Scalable Graph Transformer](/papers/2205.12454/) | 24 | 4 | 149 | COCO-SP, MNIST, PCQM4Mv2, PascalVOC-SP | CIN, CRaWl, DGN, EGT |
| [2502.00282](/papers/2502.00282/) | [GraphMinNet: Learning Dependencies in Graphs with Light Complexity Minimal Architecture](/papers/2502.00282/) | 24 | 24 | 149 | CIFAR10, CLUSTER, MNIST, PATTERN | GAT, GCN, GIN, GRIT |
| [2110.07141](/papers/2110.07141/) | [SoGCN: Second-Order Graph Convolutional Networks](/papers/2110.07141/) | 24 | 13 | 147 | CIFAR10, CLUSTER, MNIST, PATTERN | 3WLGNN, APPNP, GAT, GIN |
| [2306.01631](/papers/2306.01631/) | [Bi-level Contrastive Learning for Knowledge-Enhanced Molecule Representations](/papers/2306.01631/) | 24 | 17 | 113 | BACE, BBBP, ClinTox, ESOL | D-MPNN, GCN, GIN, MPNN |
| [2206.02386](/papers/2206.02386/) | [Restructuring Graphs for Higher Homophily via Adaptive Spectral Clustering](/papers/2206.02386/) | 24 | 9 | 109 | Actor, Chameleon, Cornell, Squirrel | APPNP, BernNet, GAT, GCN |
| [2207.11996](/papers/2207.11996/) | [Generative Subgraph Contrast for Self-Supervised Graph Representation Learning](/papers/2207.11996/) | 23 | 14 | 631 | CiteSeer, Cora, PPI, PubMed | DGI, DeepWalk, GAT, GCN |
| [2302.12357](/papers/2302.12357/) | [Auto-HeG: Automated Graph Neural Network on Heterophilic Graphs](/papers/2302.12357/) | 23 | 7 | 576 | Actor, CiteSeer, Cora, Cornell | FAGCN, GAT, GCN, GCNII |
| [2410.12096](/papers/2410.12096/) | [Bridging Large Language Models and Graph Structure Learning Models for...](/papers/2410.12096/) | 23 | 18 | 574 | Cora, PubMed, ogbn-arxiv | GAT, GCN, GEN, GIANT |
| [2007.08025](/papers/2007.08025/) | [GraphCL: Contrastive Self-Supervised Learning of Graph Representations](/papers/2007.08025/) | 23 | 6 | 486 | CiteSeer, Cora, PPI, PubMed | DGI, DeepWalk, GAT, GCN |
| [2511.06443](/papers/2511.06443/) | [How Wide and How Deep? Mitigating Over-Squashing of GNNs via...](/papers/2511.06443/) | 23 | 22 | 349 | Amazon-Computers, Amazon-Photo, CiteSeer, Cora | APPNP, ChebNet, GCN, GPRGNN |
| [2401.15569](/papers/2401.15569/) | [Efficient Tuning and Inference for Large Language Models on Textual...](/papers/2401.15569/) | 23 | 13 | 311 | Amazon-Photo, Cora, ogbn-arxiv, ogbn-products | GAT, GCN, GIANT, GLEM |
| [2506.07624](/papers/2506.07624/) | [Return of ChebNet: Understanding and Improving an Overlooked GNN on...](/papers/2506.07624/) | 23 | 7 | 290 | Amazon-ratings, Roman-empire, Tolokers, ogbn-arxiv | CPGNN, ChebNet, Exphormer, GAT |
| [2409.08676](/papers/2409.08676/) | [Redesigning graph filter-based GNNs to relax the homophily assumption This...](/papers/2409.08676/) | 22 | 16 | 653 | CiteSeer, Cora, Cornell, Texas | GAT, GCN, GIN, MLP |
| [2308.07134](/papers/2308.07134/) | [Language is All a Graph Needs](/papers/2308.07134/) | 22 | 5 | 587 | Cora, PubMed, ogbn-arxiv | ANS-GT, BernNet, DeeperGCN, GAT |
| [2306.03506](/papers/2306.03506/) | [Subgraph Networks Based Contrastive Learning](/papers/2306.03506/) | 22 | 11 | 259 | BACE, BBBP, ClinTox, D&D | AD-GCL, ContextPred, GraphCL, InfoGraph |
| [2510.12140](/papers/2510.12140/) | [Graph Few-Shot Learning via Adaptive Spectrum Experts and Cross-Set Distribution...](/papers/2510.12140/) | 21 | 17 | 917 | CiteSeer, Coauthor-CS, Cora, ogbn-arxiv | DeepWalk, G-Meta, GCN, GPN |
| [2302.14806](/papers/2302.14806/) | [Framelet Message Passing](/papers/2302.14806/) | 21 | 10 | 567 | CiteSeer, Cornell, Texas, Wisconsin | APPNP, CPGNN, GAT, GCN |
| [2009.06211](/papers/2009.06211/) | [Implicit Graph Neural Networks](/papers/2009.06211/) | 21 | 12 | 307 | ACM, DBLP, IMDB, MUTAG | DGCNN, DGI, DMGI, DeepWalk |
| [2402.08450](/papers/2402.08450/) | [Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph Products](/papers/2402.08450/) | 21 | 8 | 114 | BACE, Peptides-func, Peptides-struct, ZINC | CIN (small), DS-GNN, GCN, GIN |
| [2206.12547](/papers/2206.12547/) | [Geometry Contrastive Learning on Heterogeneous Graphs](/papers/2206.12547/) | 21 | 18 | 47 | ACM, DBLP, IMDB | DGI, DMGI, DeepWalk, GAT |
| [2511.05592](/papers/2511.05592/) | [Graver: Generative Graph Vocabularies for Robust Graph Foundation Models Fine-tuning](/papers/2511.05592/) | 20 | 15 | 891 | Cora, PubMed, WikiCS, ogbn-arxiv | DGI, DSSL, GAT, GCN |
| [2406.19258](/papers/2406.19258/) | [Leveraging Contrastive Learning for Enhanced Node Representations in Tokenized Graph...](/papers/2406.19258/) | 20 | 8 | 805 | Amazon-Computers, Amazon-Photo, Cora, Roman-empire | ACMGCN, ANS-GT, APPNP, FAGCN |
| [1911.11430](/papers/1911.11430/) | [Independence Promoted Graph Disentangled Networks](/papers/1911.11430/) | 20 | 4 | 648 | CiteSeer, Cora, PubMed | ChebNet, DeepWalk, GAT, GCN |
| [2402.09600](/papers/2402.09600/) | [Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention for...](/papers/2402.09600/) | 20 | 14 | 544 | CiteSeer, Coauthor-CS, Cora, PubMed | ARIEL, CPGNN, GCN, GRAND |
| [2006.15097](/papers/2006.15097/) | [Policy-GNN: Aggregation Optimization for Graph Neural Networks](/papers/2006.15097/) | 20 | 1 | 486 | CiteSeer, Cora, PubMed | DAGNN, DeepWalk, GAT, GCN |
| [2305.06102](/papers/2305.06102/) | [Towards Better Graph Representation Learning with Parameterized Decomposition & Filtering](/papers/2305.06102/) | 20 | 12 | 307 | ENZYMES, MUTAG, NCI1, PROTEINS | DGCNN, ECC, GAT, GCN |
| [2402.15326](/papers/2402.15326/) | [Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective of Operator...](/papers/2402.15326/) | 20 | 15 | 167 | CiteSeer, Cora, Cornell, PubMed | CPGNN, GAT, GCN, GRAND |
| [2601.15124](/papers/2601.15124/) | [RAG-GFM: Overcoming In-Memory Bottlenecks in Graph Foundation Models via Retrieval-Augmented...](/papers/2601.15124/) | 19 | 16 | 925 | CiteSeer, Cora, WikiCS, ogbn-products | DGI, GAT, GCN, GraphCL |
| [1906.01210](/papers/1906.01210/) | [Attributed Graph Clustering via Adaptive Graph Convolution](/papers/1906.01210/) | 19 | 2 | 627 | CiteSeer, Cora, PubMed | DNGR, DeepWalk, GAE, K-means |
| [2002.10306](/papers/2002.10306/) | [Adaptive Propagation Graph Convolutional Network](/papers/2002.10306/) | 19 | 2 | 525 | Amazon-Computers, Amazon-Photo, Cora, PubMed | AP-GCN, APPNP, ARMA, GAT |
| [2111.10698](/papers/2111.10698/) | [Towards Graph Self-Supervised Learning with Contrastive Adjusted Zooming](/papers/2111.10698/) | 19 | 2 | 515 | CiteSeer, Coauthor-CS, Cora, ogbn-arxiv | DGI, GAT, GCN, GRACE |
| [2010.01777](/papers/2010.01777/) | [A Unified View on Graph Neural Networks as Graph Signal...](/papers/2010.01777/) | 19 | 1 | 492 | Amazon-Computers, Amazon-Photo, CiteSeer, Coauthor-CS | APPNP, Ada-Ugnn, GAT, GCN |
| [2206.08583](/papers/2206.08583/) | [arXiv:2206.08583](/papers/2206.08583/) | 19 | 3 | 471 | CiteSeer, Cora, PubMed | APPNP, DAGNN, GAT, GCN |
| [2010.05563](/papers/2010.05563/) | [Graph Information Bottleneck for Subgraph Recognition](/papers/2010.05563/) | 19 | 6 | 264 | D&D, IMDB-BINARY, MUTAG, PROTEINS | DiffPool, EdgePool, GAT, GCN |
| [2103.11155](/papers/2103.11155/) | [Recognizing Predictive Substructures with Subgraph Information Bottleneck](/papers/2103.11155/) | 19 | 6 | 264 | D&D, IMDB-BINARY, MUTAG, PROTEINS | DiffPool, EdgePool, GAT, GCN |
| [2008.05089](/papers/2008.05089/) | [Quaternion Graph Neural Networks](/papers/2008.05089/) | 19 | 1 | 239 | COLLAB, CiteSeer, Cora, D&D | DGCNN, GAT, GCN, GraphSAGE |
| [2203.10866](/papers/2203.10866/) | [Unsupervised Network Embedding Beyond Homophily](/papers/2203.10866/) | 19 | 4 | 223 | Actor, DBLP, Texas, Wisconsin | DGI, FAGCN, GMI, GPRGNN |
| [2306.13089](/papers/2306.13089/) | [gimlet: A Unified Graph-Text Model for Instruction-Based Molecule Zero-Shot Learning](/papers/2306.13089/) | 19 | 15 | 151 | BACE, BBBP, ESOL, ToxCast | GAT, GCN, GIN, Gimlet |
| [2301.09505](/papers/2301.09505/) | [Rethinking the Expressive Power of GNNs via Graph Biconnectivity](/papers/2301.09505/) | 19 | 1 | 149 | ZINC | CIN (small), DS-GNN, GAT, GCN |
| [2007.16002](/papers/2007.16002/) | [Graph Convolutional Networks using Heat Kernel for Semi-supervised Learning](/papers/2007.16002/) | 18 | 4 | 648 | CiteSeer, Cora, PubMed | ChebNet, DeepWalk, GAT, GCN |
| [2106.04051](/papers/2106.04051/) | [Graph-MLP: Node Classification without Message Passing in Graph](/papers/2106.04051/) | 18 | 1 | 623 | CiteSeer, Cora, PubMed | DGI, DeepWalk, GAT, GCN |
| [2305.08048](/papers/2305.08048/) | [Towards Understanding the Generalization of Graph Neural Networks](/papers/2305.08048/) | 18 | 3 | 586 | CiteSeer, Cora, PubMed | APPNP, GAT, GCN, GCNII |
| [2511.06608](/papers/2511.06608/) | [Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification...](/papers/2511.06608/) | 18 | 18 | 382 | Amazon-Photo, Chameleon, CiteSeer, PubMed | AD-GraphSAGE, Dir-GNN, GAT, GATv2 |
| [2002.05287](/papers/2002.05287/) | [Geom-GCN: Geometric Graph Convolutional Networks](/papers/2002.05287/) | 18 | 1 | 239 | Actor, Chameleon, CiteSeer, Cora | GAT, GCN |
| [2403.07954](/papers/2403.07954/) | [Optimizing Polynomial Graph Filters: A Novel Adaptive Krylov Subspace Approach](/papers/2403.07954/) | 18 | 12 | 187 | Actor, Chameleon, CiteSeer, Cora | ASGC, BernNet, ChebNet, GCN |
| [2509.14863](/papers/2509.14863/) | [Exploring the Global-to-Local Attention Scheme in Graph Transformers: An Empirical...](/papers/2509.14863/) | 18 | 17 | 111 | PascalVOC-SP, Peptides-func, Peptides-struct, Pokec | Exphormer, GAT, GCN, GIN |
| [2402.04538](/papers/2402.04538/) | [Triplet Interaction Improves Graph Transformers: Accurate Molecular Graph Learning with...](/papers/2402.04538/) | 18 | 12 | 58 | PCQM4Mv2, QM9 | 3D Infomax, Cormorant, DimeNet++, EGNN |
| [2505.00983](/papers/2505.00983/) | [Toward Data-centric Directed Graph Learning: An Entropy-driven Approach](/papers/2505.00983/) | 17 | 14 | 606 | Amazon-ratings, CiteSeer, Cora, Roman-empire | DGCNN, DIMPA, DiGCN, Dir-GNN |
| [2111.12952](/papers/2111.12952/) | [AutoHEnsGNN: Winning Solution to AutoGraph Challenge for KDD Cup 2020](/papers/2111.12952/) | 17 | 1 | 570 | Cora, ogbn-arxiv | APPNP, DeeperGCN, GAT, GCN |
| [2009.14332](/papers/2009.14332/) | [Multi-hop Attention Graph Neural Networks](/papers/2009.14332/) | 17 | 0 | 486 | Cora, FB15k-237, PubMed, WN18RR | APPNP, ComplEx, ConvE, DistMult |
| [2306.11264](/papers/2306.11264/) | [GraphGLOW: Open-World Graph Structure Learning for Cross-Graph Topology Refinement](/papers/2306.11264/) | 17 | 3 | 482 | CiteSeer, Cora, PubMed | APPNP, CPGNN, GAT, GCN |
| [2403.03483](/papers/2403.03483/) | [A Teacher-Free Graph Knowledge Distillation Framework with Dual Self-Distillation](/papers/2403.03483/) | 17 | 10 | 324 | Amazon-Computers, Coauthor-Physics, PubMed | APPNP, ChebNet, GAT, GCN |
| [2211.14425](/papers/2211.14425/) | [PatchGT: Transformer over Non-trainable Clusters for Learning Graph Representations](/papers/2211.14425/) | 17 | 5 | 319 | ENZYMES, MUTAG, PROTEINS, Tox21 | DiffPool, GAT, GCN, GCN-VN |
| [2111.10657](/papers/2111.10657/) | [Generalizing Graph Neural Networks on Out-Of-Distribution Graphs](/papers/2111.10657/) | 17 | 6 | 223 | BACE, BBBP, MUTAG | CIGA, DIR, DiffPool, GAT |
| [2305.10498](/papers/2305.10498/) | [Edge Directionality Improves Learning on Heterophilic Graphs](/papers/2305.10498/) | 17 | 7 | 179 | Chameleon, Roman-empire, Squirrel, snap-patents | DiGCN, GCN, GPR-GNN, GloGNN |
| [2110.00973](/papers/2110.00973/) | [Graph Pointer Neural Networks](/papers/2110.00973/) | 17 | 3 | 174 | Chameleon, Cornell, Texas, Wisconsin | GAT, GCN, Geom-GCN, GraphSAGE |
| [2303.06147](/papers/2303.06147/) | [Exphormer: Sparse Transformers for Graphs](/papers/2303.06147/) | 17 | 10 | 89 | CLUSTER, MNIST, PATTERN, PascalVOC-SP | DGN, GAT, GCN, GIN |
| [2605.06462](/papers/2605.06462/) | [Invariant-Based Diagnostics for Graph Benchmarks](/papers/2605.06462/) | 17 | 13 | 89 | BACE, BBBP, Flow, Peptides-func | D-MPNN, GCN, GIN, GINE |
| [2410.10241](/papers/2410.10241/) | [Revisiting Graph Autoencoders as Implicit Contrastive Learners](/papers/2410.10241/) | 17 | 3 | 83 | Amazon-Computers, Amazon-Photo, Coauthor-CS, Coauthor-Physics | BGRL, GAE, GRACE, GraphMAE |
| [2208.10010](/papers/2208.10010/) | [NOSMOG: Learning Noise-robust and Structure-aware MLPs on Graphs](/papers/2208.10010/) | 16 | 1 | 601 | Amazon-Computers, Amazon-Photo, CiteSeer, Cora | GLNN, MLP, SAGE |
| [1811.05868](/papers/1811.05868/) | [Pitfalls of Graph Neural Network Evaluation](/papers/1811.05868/) | 16 | 1 | 597 | Amazon-Computers, Amazon-Photo, CiteSeer, Coauthor-CS | GAT, GCN, MLP, MoNet |
| [1812.04202](/papers/1812.04202/) | [Deep Learning on Graphs: A Survey](/papers/1812.04202/) | 16 | 1 | 526 | Cora, PubMed | CayleyNets, ChebNet, DGI, FastGCN |
| [2209.07754](/papers/2209.07754/) | [On the Robustness of Graph Neural Diffusion to Topology Perturbations](/papers/2209.07754/) | 15 | 3 | 617 | CiteSeer, Cora, PubMed | APPNP, GAT, GCN-SVD, GIN |
| [1312.6203](/papers/1312.6203/) | [Spectral Networks and Locally Connected Networks on Graphs](/papers/1312.6203/) | 15 | 0 | 572 | CiteSeer, Cora, PubMed | APPNP, ChebNet, GAT, GCN |
| [2207.12931](/papers/2207.12931/) | [Demystifying Graph Convolution with a Simple Concatenation](/papers/2207.12931/) | 15 | 3 | 530 | CiteSeer, Cora, PubMed | ChebNet, GCN, GIN, GraphSAGE |
| [1609.02907](/papers/1609.02907/) | [Semi-Supervised Classification with Graph Convolutional Networks](/papers/1609.02907/) | 15 | 4 | 486 | CiteSeer, Cora, Cornell, PubMed | DeepWalk, GCN, LP, ManiReg |
| [1802.08888](/papers/1802.08888/) | [N-GCN: Multi-scale Graph Convolution for Semi-supervised Node Classification](/papers/1802.08888/) | 15 | 1 | 486 | CiteSeer, Cora, PPI, PubMed | DeepWalk, GCN, GCN-VN, LP |
| [2204.06127](/papers/2204.06127/) | [Reinforcement learning on graphs: A survey](/papers/2204.06127/) | 15 | 5 | 486 | CiteSeer, Cora, PubMed, WN18RR | ComplEx, ConvE, DAGNN, DGI |
| [2008.12578](/papers/2008.12578/) | [Graph Convolutional Neural Networks with Node Transition Probability-based Message Passing...](/papers/2008.12578/) | 15 | 6 | 471 | CiteSeer, Cora, NCI1, PROTEINS | DGCNN, DGI, GAT, GCN |
| [2408.14134](/papers/2408.14134/) | [Exploring the Potential of Large Language Models for Heterophilic Graphs](/papers/2408.14134/) | 15 | 9 | 214 | Amazon-Computers, Cornell, Texas, Wisconsin | FAGCN, GAT, GCN, GraphSAGE |
| [2202.13248](/papers/2202.13248/) | [Automated Data Augmentations for Graph Classification](/papers/2202.13248/) | 15 | 4 | 210 | COLLAB, IMDB-BINARY, MUTAG, NCI1 | AD-GCL, AutoGCL, DropEdge, JOAOv2 |
| [2012.08734](/papers/2012.08734/) | [Hierarchical Graph Capsule Network](/papers/2012.08734/) | 15 | 5 | 185 | COLLAB, ENZYMES, IMDB-BINARY, IMDB-MULTI | DGCNN, DiffPool, GCN, GIN |
| [2106.06218](/papers/2106.06218/) | [Graph Transformer Networks: Learning Meta-path Graphs to Improve GNNs](/papers/2106.06218/) | 15 | 7 | 104 | ACM, DBLP, IMDB, PPI | GAT, GCN, GCNII, GTN |
| [2202.13060](/papers/2202.13060/) | [Graph Attention Retrospective](/papers/2202.13060/) | 14 | 2 | 520 | CiteSeer, Cora, PubMed | APPNP, GAT, GCN, GIN |
| [1905.05178](/papers/1905.05178/) | [Graph U-Nets](/papers/1905.05178/) | 14 | 1 | 486 | COLLAB, CiteSeer, Cora, PROTEINS | DGCNN, DeepWalk, DiffPool, GAT |
| [2001.05140](/papers/2001.05140/) | [Graph-Bert: Only Attention is Needed for Learning Graph Representations](/papers/2001.05140/) | 14 | 4 | 486 | CiteSeer, Cora, PubMed | DeepWalk, GAT, GCN, LP |
| [2403.03670](/papers/2403.03670/) | [CDC: A Simple Framework for Complex Data Clustering This work...](/papers/2403.03670/) | 14 | 11 | 486 | CiteSeer, PubMed, ogbn-papers100M, ogbn-products | BGRL, DGI, GRACE, MVGRL |
| [2311.14324](/papers/2311.14324/) | [Large Language Models as Topological Structure Enhancers for Text-Attributed Graphs](/papers/2311.14324/) | 14 | 2 | 308 | CiteSeer, Cora, PubMed | DeBERTa, GAT, GCN, GIANT |
| [2205.07308](/papers/2205.07308/) | [Finding Global Homophily in Graph Neural Networks When Meeting Heterophily](/papers/2205.07308/) | 14 | 0 | 291 | Chameleon, CiteSeer, Cora, PubMed | APPNP, CPGNN, ChebNet, GAT |
| [2503.00547](/papers/2503.00547/) | [Performance Heterogeneity in Graph Neural Networks: Lessons for Architecture Design...](/papers/2503.00547/) | 14 | 13 | 282 | ENZYMES, IMDB-BINARY, MUTAG, PROTEINS | GAT, GCN, GIN, R-GIN + FoSR |
| [2309.13944](/papers/2309.13944/) | [Provable Training for Graph Contrastive Learning](/papers/2309.13944/) | 14 | 7 | 188 | Amazon-Computers, Amazon-Photo | APPNP, ChebNet, GAT, GCN |
| [1905.04579](/papers/1905.04579/) | [Are Powerful Graph Neural Nets Necessary? A Dissection on Graph...](/papers/1905.04579/) | 14 | 1 | 185 | COLLAB, ENZYMES, IMDB-BINARY, IMDB-MULTI | DGCNN, GCN, GIN, WL |
| [2405.13806](/papers/2405.13806/) | [A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition](/papers/2405.13806/) | 14 | 8 | 177 | Amazon-Computers, Amazon-Photo, Coauthor-CS, PascalVOC-SP | APPNP, GAT, GCN, GINE |
| [2405.18581](/papers/2405.18581/) | [Unleashing the Potential of Text-attributed Graphs: Automatic Relation Decomposition via...](/papers/2405.18581/) | 14 | 12 | 159 | Cora, Cornell, PubMed, Texas | GAT, GCN, JK-Net, UniMP |
| [2202.04139](/papers/2202.04139/) | [Simplified Graph Convolution with Heterophily](/papers/2202.04139/) | 14 | 0 | 148 | Actor, Amazon-Computers, Texas | APPNP, GAT, GCN, GPRGNN |
| [2101.03464](/papers/2101.03464/) | [SPAGAN: Shortest Path Graph Attention Network](/papers/2101.03464/) | 13 | 1 | 648 | CiteSeer, Cora, PubMed | DeepWalk, GAT, GCN, MLP |
| [1908.05081](/papers/1908.05081/) | [AdaGCN: Adaboosting Graph Convolutional Networks into Deep Models](/papers/1908.05081/) | 13 | 3 | 515 | CiteSeer, Cora, PubMed | APPNP, GAT, GCN, GCN-VN |
| [2003.02228](/papers/2003.02228/) | [PushNet: Efficient and Adaptive Neural Message Passing](/papers/2003.02228/) | 13 | 0 | 501 | Coauthor-CS, Coauthor-Physics, PubMed | APPNP, GAT, GCN, GIN |
| [2202.09025](/papers/2202.09025/) | [Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction](/papers/2202.09025/) | 13 | 9 | 359 | Chameleon, CiteSeer, Cora, Cornell | ARGVA, DGI, DeepWalk, GAE |
| [2406.08897](/papers/2406.08897/) | [Motif-driven Subgraph Structure Learning for Graph Classification](/papers/2406.08897/) | 13 | 13 | 267 | ENZYMES, IMDB-BINARY, IMDB-MULTI, PROTEINS | EdgePool, GCN, GIN, HGP-SL |
| [2512.04530](/papers/2512.04530/) | [Explainable Graph Representation Learning via Graph Pattern Analysis](/papers/2512.04530/) | 13 | 13 | 166 | COLLAB, D&D, IMDB-BINARY, NCI1 | DGCNN, DiffPool, GIN, GraphSAGE |
| [2305.15745](/papers/2305.15745/) | [Robust Ante-hoc Graph Explainer using Bilevel Optimization](/papers/2305.15745/) | 13 | 6 | 106 | BBBP, Tox21, ToxCast | GAT, GCN, GIN, GMT |
| [2012.10024](/papers/2012.10024/) | [Leveraging Meta-path Contexts for Classification in Heterogeneous Information Networks](/papers/2012.10024/) | 13 | 0 | 30 | DBLP, Freebase | GAT, GCN, H2GCN, HAN |
| [2405.16800](/papers/2405.16800/) | [TAGA: Text-Attributed Graph Self-Supervised Learning by Synergizing Graph and Text...](/papers/2405.16800/) | 12 | 4 | 905 | Amazon-Computers, Cora, PubMed, ogbn-arxiv | G2P2, GRACE, GraphCL, GraphMAE |
| [2210.10946](/papers/2210.10946/) | [Causally-guided Regularization of Graph Attention Improves Generalizability](/papers/2210.10946/) | 12 | 4 | 795 | Chameleon, CiteSeer, Cora, Cornell | GAT, GATv2 |
| [2006.13009](/papers/2006.13009/) | [Iterative Deep Graph Learning for Graph Neural Networks: Better and...](/papers/2006.13009/) | 12 | 1 | 609 | CiteSeer, Cora, PubMed | APPNP, GAT, GCN, GraphSAGE |
| [2206.04739](/papers/2206.04739/) | [I'm Me, We're Us, and I'm Us: Tri-directional Contrastive Learning...](/papers/2206.04739/) | 12 | 5 | 596 | CiteSeer, PubMed | DGI, GAT, GCN, GRACE |
| [2405.20445](/papers/2405.20445/) | [Fully-inductive Node Classification on Arbitrary Graphs](/papers/2405.20445/) | 12 | 6 | 490 | Cora, Wisconsin, ogbn-arxiv, ogbn-products | GAT, GCN, Linear, MLP |
| [1611.08402](/papers/1611.08402/) | [Geometric deep learning on graphs and manifolds using mixture model...](/papers/1611.08402/) | 12 | 0 | 485 | Cora, MNIST, PubMed | ChebNet, DGCNN, DeepWalk, GCN |
| [2210.11879](/papers/2210.11879/) | [GLCC: A General Framework for Graph-Level Clustering](/papers/2210.11879/) | 12 | 4 | 229 | D&D, IMDB-BINARY | GraphCL, Graphlet, InfoGraph, JOAO |
| [2010.05421](/papers/2010.05421/) | [Factorizable Graph Convolutional Networks](/papers/2010.05421/) | 12 | 5 | 182 | COLLAB, IMDB-BINARY, MUTAG, PATTERN | GAT, GCN, GIN, GatedGCN |
| [2304.02806](/papers/2304.02806/) | [Graph Mixture of Experts: Learning on Large-Scale Graphs with Explicit...](/papers/2304.02806/) | 12 | 3 | 177 | BBBP, ESOL, Tox21, ToxCast | GCN, GIN |
| [2405.20724](/papers/2405.20724/) | [on Large Graphs using Intersecting Communities](/papers/2405.20724/) | 12 | 8 | 175 | Reddit, Squirrel, twitch-gamers | Coarsening, GAT, GCN, GPR-GNN |
| [2106.05234](/papers/2106.05234/) | [Do Transformers Really Perform Bad for Graph Representation?](/papers/2106.05234/) | 12 | 0 | 149 | PCQM4Mv2, ZINC | DeeperGCN-VN, GAT, GCN, GCN-VN |
| [2302.08647](/papers/2302.08647/) | [Multiresolution Graph Transformers and Wavelet Positional Encoding for Learning Hierarchical...](/papers/2302.08647/) | 12 | 1 | 133 | Peptides-func, Peptides-struct, ZINC | GAT, GCN, GINE, GPS |
| [2108.10097](/papers/2108.10097/) | [Graph Attention MLP with Reliable Label Utilization](/papers/2108.10097/) | 12 | 3 | 64 | ogbn-mag, ogbn-papers100M, ogbn-products | GAMLP, GCN, GraphSAGE, HGT |
| [2402.00789](/papers/2402.00789/) | [Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective State Spaces](/papers/2402.00789/) | 12 | 9 | 53 | CIFAR10, CLUSTER, MNIST, PATTERN | Exphormer, GCN, GIN, GatedGCN |
| [2201.02534](/papers/2201.02534/) | [MGAE: Masked Autoencoders for Self-Supervised Learning on Graphs](/papers/2201.02534/) | 11 | 2 | 687 | CiteSeer, PubMed, ogbl-ddi, ogbn-arxiv | DGI, GCN, GraphSAGE |
| [2507.13368](/papers/2507.13368/) | [Scalable Attribute-Missing Graph Clustering via Neighborhood Differentiation](/papers/2507.13368/) | 11 | 9 | 643 | Amazon-Photo, CiteSeer, Cora, Reddit | CCGC, DGI, K-means, MVGRL |
| [2110.09443](/papers/2110.09443/) | [Beltrami Flow and Neural Diffusion on Graphs](/papers/2110.09443/) | 11 | 3 | 514 | Amazon-Computers, CiteSeer, Coauthor-CS, Cora | CPGNN, GAT, GAT-ppr, GCN |
| [2407.14996](/papers/2407.14996/) | [All Against Some: Efficient Integration of Large Language Models for...](/papers/2407.14996/) | 11 | 8 | 502 | Cora, PubMed, ogbn-arxiv, ogbn-products | GAT, GCN, GCNII, GraphSAGE |
| [1901.08150](/papers/1901.08150/) | [Hypergraph Convolution and Hypergraph Attention](/papers/1901.08150/) | 11 | 1 | 486 | CiteSeer, Cora, PubMed | CNNs, DeepWalk, GAT, GCN |
| [2603.01385](/papers/2603.01385/) | [Toward Graph-Tokenizing Large Language Models with Reconstructive Graph Instruction Tuning](/papers/2603.01385/) | 11 | 8 | 362 | Cora, ogbn-arxiv | DIFFormer, GAT, GCN, GraphGPS |
| [1911.07979](/papers/1911.07979/) | [ASAP: Adaptive Structure Aware Pooling for Learning Hierarchical Graph Representations](/papers/1911.07979/) | 11 | 10 | 284 | D&D, NCI1, PROTEINS | DiffPool, SAGPool, Set2Set, SortPool |
| [2302.08671](/papers/2302.08671/) | [Search to Capture Long-range Dependency with Stacking GNNs for Graph...](/papers/2302.08671/) | 11 | 11 | 254 | D&D, IMDB-BINARY, NCI1, PROTEINS | DGCNN, DiffPool, GCN, SAGPool |
| [2104.05960](/papers/2104.05960/) | [Hierarchical Adaptive Pooling by Capturing High-order Dependency for Graph Representation...](/papers/2104.05960/) | 11 | 6 | 247 | COLLAB, IMDB-MULTI, MUTAG, PROTEINS | DiffPool, SAGPool, Set2Set, StructPool |
| [2002.04025](/papers/2002.04025/) | [Can Graph Neural Networks Count Substructures?](/papers/2002.04025/) | 11 | 0 | 151 | ZINC, ogbg-molhiv | GAT, GCN, GIN, GatedGCN |
| [2310.01704](/papers/2310.01704/) | [Transformers are efficient hierarchical chemical graph learners](/papers/2310.01704/) | 11 | 8 | 146 | ToxCast, ZINC, ogbg-molhiv | AUTOBAHN, GAT, GCN, GIN |
| [2110.07875](/papers/2110.07875/) | [Graph Neural Networks with Learnable Structural and Positional Representations](/papers/2110.07875/) | 11 | 1 | 133 | Tox21, ZINC, ogbg-molpcba | GAT, GCN, GIN, GIN-VN |
| [2202.03341](/papers/2202.03341/) | [Neighbor2Seq: Deep Learning on Massive Graphs by Transforming Neighbors to...](/papers/2202.03341/) | 11 | 4 | 72 | Reddit, ogbn-papers100M, ogbn-products | Cluster-GCN, FastGCN, GCN, GraphSAGE |
| [2212.05767](/papers/2212.05767/) | [A Survey of Knowledge Graph Reasoning on Graph Types: Static,...](/papers/2212.05767/) | 11 | 8 | 55 | FB15k-237, WN18RR | ComplEx, ConvE, DistMult, HAKE |
| [1905.10990](/papers/1905.10990/) | [Edge Contraction Pooling for Graph Neural Networks](/papers/1905.10990/) | 10 | 0 | 736 | COLLAB, Cora | DiffPool, EdgePool, GAT, GCN |
| [2407.11025](/papers/2407.11025/) | [Backdoor Graph Condensation](/papers/2407.11025/) | 10 | 9 | 540 | CiteSeer, Cora | APPNP, Cheby, GCN, MLP |
| [1902.08226](/papers/1902.08226/) | [Graph Adversarial Training: Dynamically Regularizing Based on Graph Structure](/papers/1902.08226/) | 10 | 5 | 522 | CiteSeer, Cora, Cornell | DeepWalk, GCN, LP, Planetoid* |
| [1802.04407](/papers/1802.04407/) | [Adversarially Regularized Graph Autoencoder for Graph Embedding](/papers/1802.04407/) | 10 | 0 | 490 | CiteSeer, Cora | DNGR, DeepWalk, GAE, K-means |
| [1910.02370](/papers/1910.02370/) | [GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph...](/papers/1910.02370/) | 10 | 1 | 382 | CiteSeer, Cora, PPI, PubMed | DGI, DeepWalk, GraphSAGE-LSTM, Node2Vec |
| [2310.04668](/papers/2310.04668/) | [Label-free Node Classification on Graphs with Large Language Models (LLMs)](/papers/2310.04668/) | 10 | 10 | 333 | CiteSeer, Cora, PubMed | AGE, Degree, Pagerank, Random |
| [2209.14402](/papers/2209.14402/) | [L2XGNN: Learning to Explain Graph Neural Networks](/papers/2209.14402/) | 10 | 3 | 247 | IMDB-BINARY, IMDB-MULTI, MUTAG, PROTEINS | GCN, GIN, GraphSAGE |
| [2201.12994](/papers/2201.12994/) | [MGNN: Graph Neural Networks Inspired by Distance Geometry Problem](/papers/2201.12994/) | 10 | 1 | 233 | ogbn-arxiv | APPNP, CPGNN, GAT, GCN |
| [1806.08804](/papers/1806.08804/) | [Hierarchical Graph Representation Learning with Differentiable Pooling](/papers/1806.08804/) | 10 | 0 | 210 | COLLAB, D&D, ENZYMES, PROTEINS | DiffPool, GraphSAGE, Graphlet, Set2Set |
| [2603.02025](/papers/2603.02025/) | [arXiv:2603.02025](/papers/2603.02025/) | 10 | 10 | 209 | COLLAB, IMDB-BINARY, IMDB-MULTI, PROTEINS | ASAP, DropGIN, GIN, Graphormer |
| [2406.11714](/papers/2406.11714/) | [Scalable Expressiveness through Preprocessed Graph Perturbations](/papers/2406.11714/) | 10 | 8 | 145 | COLLAB, IMDB-BINARY, IMDB-MULTI, PROTEINS | DGCNN, GCN, GIN |
| [2502.08209](/papers/2502.08209/) | [Equivariant Masked position prediction for efficient molecular representation](/papers/2502.08209/) | 10 | 8 | 89 | MD17, QM9 | AttrMask, DimeNet++, Equiformer, PaiNN |
| [2112.04319](/papers/2112.04319/) | [SCR: Training Graph Neural Networks with Consistency Regularization](/papers/2112.04319/) | 10 | 2 | 64 | ogbn-mag, ogbn-papers100M, ogbn-products | GAMLP, GCN, GraphSAGE, R-GCN |
| [2502.12638](/papers/2502.12638/) | [NExT-Mol: 3D Diffusion Meets 1D Language Modeling for 3D Molecule...](/papers/2502.12638/) | 10 | 10 | 51 | ESOL, FreeSolv, Lipophilicity | 3D Infomax, D-MPNN, GCN, GIN |
| [2207.08824](/papers/2207.08824/) | [Energy-Motivated Equivariant Pretraining for 3D Molecular Graphs](/papers/2207.08824/) | 10 | 0 | 48 | QM9 | 3D Infomax, 3D-MGP, AttrMask, EdgePred |
| [2405.01927](/papers/2405.01927/) | [arXiv:2405.01927](/papers/2405.01927/) | 10 | 10 | 48 | ACM, DBLP, IMDB | GAT, GCN, GTN, HAN |
| [2206.04216](/papers/2206.04216/) | [Neo-GNNs: Neighborhood Overlap-aware Graph Neural Networks for Link Prediction](/papers/2206.04216/) | 10 | 1 | 35 | ogbl-citation2, ogbl-collab, ogbl-ddi | GAT, GCN, GraphSAGE, Node2Vec |
| [2310.19035](/papers/2310.19035/) | [Does Invariant Graph Learning via Environment Augmentation Learn Invariance?](/papers/2310.19035/) | 10 | 0 | 21 | BA graph, MNIST | CIGA, DisC, EIIL, ERM |
| [1905.09718](/papers/1905.09718/) | [Meta-GNN: On Few-shot Node Classification in Graph Meta-learning](/papers/1905.09718/) | 9 | 1 | 809 | Cora, Reddit | DeepWalk, GCN, GraphSAGE-mean, GraphSAGE-pool |
| [2106.04714](/papers/2106.04714/) | [NRGNN: Learning a Label Noise-Resistant Graph Neural Network on Sparsely...](/papers/2106.04714/) | 9 | 2 | 685 | CiteSeer, Cora, PubMed | GCN, GIN, NGNN, Self-training |
| [2307.06631](/papers/2307.06631/) | [Frameless Graph Knowledge Distillation](/papers/2307.06631/) | 9 | 5 | 594 | Actor, Amazon-Computers, Amazon-Photo, CiteSeer | GLNN, MLP |
| [2010.12811](/papers/2010.12811/) | [Graph Information Bottleneck](/papers/2010.12811/) | 9 | 1 | 570 | CiteSeer, Cora, PubMed | GAT, GCN, GCN-Jaccard, RGCN |
| [1906.02174](/papers/1906.02174/) | [Break the Ceiling: Stronger Multi-scale Deep Graph Convolutional Networks](/papers/1906.02174/) | 9 | 2 | 559 | CiteSeer, Cora, PubMed | Cheby, GCN, GCN-DVAT, LP |
| [2006.08550](/papers/2006.08550/) | [Optimization and Generalization Analysis of Transduction through Gradient Boosting and...](/papers/2006.08550/) | 9 | 1 | 486 | CiteSeer, Cora, PubMed | APPNP, DGI, GAT, GCN |
| [2006.02380](/papers/2006.02380/) | [Self-supervised Training of Graph Convolutional Networks](/papers/2006.02380/) | 9 | 3 | 482 | CiteSeer, PubMed | DeepWalk, GAT, GCN, LP |
| [2005.10203](/papers/2005.10203/) | [Graph Structure Learning for Robust Graph Neural Networks](/papers/2005.10203/) | 9 | 1 | 364 | CiteSeer, Cora, PubMed | GAT, GCN, GCN-Jaccard, GCN-SVD |
| [2410.01778](/papers/2410.01778/) | [TopER: Topological Embeddings in Graph Representation Learning](/papers/2410.01778/) | 9 | 7 | 255 | IMDB-BINARY, MUTAG, PROTEINS, ogbg-molhiv | DGN, DiffPool, Graphormer, PNA |
| [2205.09802](/papers/2205.09802/) | [Label-invariant Augmentation for Semi-Supervised Graph Classification](/papers/2205.09802/) | 9 | 1 | 213 | D&D, MUTAG, NCI1 | GAE, GraphCL, JOAOv2, MVGRL |
| [1703.06103](/papers/1703.06103/) | [Modeling Relational Data with Graph Convolutional Networks](/papers/1703.06103/) | 9 | 0 | 207 | FB15k-237, MUTAG, WN18 | ComplEx, DistMult, HolE, R-GCN |
| [2509.21489](/papers/2509.21489/) | [GraphPFN: A Prior-Data Fitted Graph Foundation Model](/papers/2509.21489/) | 9 | 9 | 195 | Amazon-ratings, PubMed, WikiCS | GAT, GCN, GT, GraphSAGE |
| [2207.08806](/papers/2207.08806/) | [Unified 2D and 3D Pre-Training of Molecular Representations](/papers/2207.08806/) | 9 | 0 | 85 | BACE, BBBP, ClinTox, SIDER | GROVER, GraphCL, GraphMVP |
| [2603.19596](/papers/2603.19596/) | [CO-EVOLVE: Bidirectional Co-Evolution of Graph Structure and Semantics for Heterophilous...](/papers/2603.19596/) | 9 | 9 | 85 | Reddit, WikiCS | GAT, GCN, InstructGLM, LLaGA |
| [2109.11730](/papers/2109.11730/) | [GeomGCL: Geometric Graph Contrastive Learning for Molecular Property Prediction](/papers/2109.11730/) | 9 | 3 | 61 | ClinTox, ESOL, FreeSolv, Lipophilicity | D-MPNN, DimeNet++, InfoGraph |
| [2307.08430](/papers/2307.08430/) | [Long-range Meta-path Search on Large-scale Heterogeneous Graphs](/papers/2307.08430/) | 9 | 8 | 48 | Freebase, IMDB | GAT, GCN, HAN, HGT |
| [2601.22327](/papers/2601.22327/) | [arXiv:2601.22327](/papers/2601.22327/) | 9 | 9 | 37 | QM9 | Cormorant, DimeNet++, EGNN, EQGAT |
| [2605.11749](/papers/2605.11749/) | [Learning Feature Encoder with Synthetic Anomalies for Weakly Supervised Graph...](/papers/2605.11749/) | 9 | 9 | 37 | Questions | BWGNN, CPGNN, GAT, GATSep |
| [2312.03475](/papers/2312.03475/) | [Molecule Joint Auto-Encoding: Trajectory Pretraining with 2D and 3D Diffusion](/papers/2312.03475/) | 9 | 9 | 20 | MD17, QM9 | 3D InfoGraph, 3D Infomax, Angle Prediction, GeoSSL-EBM-NCE |
| [2102.05034](/papers/2102.05034/) | [SLAPS: Self-Supervision Improves Structure Learning for Graph Neural Networks](/papers/2102.05034/) | 8 | 2 | 674 | Cora, ogbn-arxiv | DGCNN, GCN_kNN, GRCN, IDGL |
| [2112.03968](/papers/2112.03968/) | [Learning Theory Can (Sometimes) Explain Generalisation in Graph Neural Networks](/papers/2112.03968/) | 8 | 1 | 586 | Cora | APPNP, ChebNet, GAT, GCN |
| [1902.07153](/papers/1902.07153/) | [Simplifying Graph Convolutional Networks](/papers/1902.07153/) | 8 | 0 | 502 | PubMed | DAGNN, DGI, DeepWalk, FastGCN |
| [1808.03965](/papers/1808.03965/) | [Large-Scale Learnable Graph Convolutional Networks](/papers/1808.03965/) | 8 | 1 | 486 | CiteSeer, Cora, PPI, PubMed | DeepWalk, GCN, GraphSAGE-GCN, GraphSAGE-pool |
| [2402.15183](/papers/2402.15183/) | [GraphEdit: Large Language Models for Graph Structure Learning](/papers/2402.15183/) | 8 | 7 | 413 | CiteSeer, Cora, PubMed | GCN, GRCN, GT, NodeFormer |
| [2502.02379](/papers/2502.02379/) | [No Metric to Rule Them All: Toward Principled Evaluations of...](/papers/2502.02379/) | 8 | 7 | 293 | MUTAG, NCI1, PROTEINS | GAT, GCN, GIN |
| [2305.15792](/papers/2305.15792/) | [IDEA: Invariant Defense for Graph Adversarial Robustness](/papers/2305.15792/) | 8 | 2 | 279 | CiteSeer, Cora | GAT, GCN, ProtGNN, RGCN |
| [2602.17893](/papers/2602.17893/) | [COMBA: Cross Batch Aggregation for Learning Large Graphs with Context...](/papers/2602.17893/) | 8 | 8 | 266 | Amazon-ratings, Minesweeper, ogbn-arxiv, ogbn-products | Cluster-GCN, GCN, Graph-Mamba, NAGphormer |
| [2012.06922](/papers/2012.06922/) | [Decimated Framelet System on Graphs and Fast $ $-Framelet Transforms](/papers/2012.06922/) | 8 | 6 | 247 | D&D, MUTAG, PROTEINS | DGCNN, DiffPool, EigenPool, GIN |
| [2308.08344](/papers/2308.08344/) | [Graph Out-of-Distribution Generalization with Controllable Data Augmentation](/papers/2308.08344/) | 8 | 4 | 205 | COLLAB, D&D, IMDB-BINARY | Attention, ERM, FLAG, Group DRO |
| [1802.00543](/papers/1802.00543/) | [Modeling polypharmacy side effects with graph convolutional networks](/papers/1802.00543/) | 8 | 0 | 118 | BACE, BBBP, ToxCast | DimeNet++, GCN, GIN, Graphormer |
| [2206.08164](/papers/2206.08164/) | [Long Range Graph Benchmark](/papers/2206.08164/) | 8 | 0 | 89 | PascalVOC-SP, Peptides-func, Peptides-struct | GCN, GINE, GatedGCN, SAN+RWSE |
| [2302.13083](/papers/2302.13083/) | [Knowledge Graph Completion with Counterfactual Augmentation](/papers/2302.13083/) | 8 | 8 | 55 | FB15k-237, WN18RR | ComplEx, ConvE, DistMult, NeuralLP |
| [2103.09430](/papers/2103.09430/) | [OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs](/papers/2103.09430/) | 8 | 0 | 47 | ogbg-molpcba, ogbn-mag | DGN, GAT, GCN, GIN |
| [2305.03324](/papers/2305.03324/) | [Augmenting Low-Resource Text Classification with Graph-Grounded Pre-training and Prompting](/papers/2305.03324/) | 7 | 4 | 901 | Cora, D&D | DGI, GCN, GPT-GNN, Roberta |
| [2503.19382](/papers/2503.19382/) | [Causal invariant geographic network representations with feature and structural distribution...](/papers/2503.19382/) | 7 | 6 | 620 | Cora, D&D, PubMed | AD-GraphSAGE, DAGNN, GCN, GraphSAGE |
| [2108.12055](/papers/2108.12055/) | [Towards Self-Explainable Graph Neural Network](/papers/2108.12055/) | 7 | 1 | 513 | CiteSeer, Cora, PubMed | GCN, GIN, Pro-GNN, SuperGAT |
| [2003.08414](/papers/2003.08414/) | [Scattering GCN: Overcoming Oversmoothness in Graph Convolutional Networks](/papers/2003.08414/) | 7 | 2 | 486 | CiteSeer, Cora, PubMed | Chebyshev, GAT, GCN |
| [2209.03473](/papers/2209.03473/) | [Higher-order Clustering and Pooling for Graph Neural Networks](/papers/2209.03473/) | 7 | 3 | 303 | D&D, MUTAG, PROTEINS | DiffPool, EigenPool, GAT, GIN |
| [2101.08170](/papers/2101.08170/) | [SUGAR: Subgraph Neural Network with Reinforcement Pooling and Self-Supervised Mutual...](/papers/2101.08170/) | 7 | 7 | 255 | D&D, MUTAG, PROTEINS | DiffPool, ECC, EigenPool, GK |
| [2211.10738](/papers/2211.10738/) | [Knowledge Graph Contrastive Learning based on Relation-Symmetrical Structure](/papers/2211.10738/) | 7 | 6 | 207 | Amazon-Computers, FB15k-237, MUTAG, WN18RR | DistMult, HAKE, R-GCN, RDF2Vec |
| [1603.08861](/papers/1603.08861/) | [Revisiting Semi-Supervised Learning with Graph Embeddings](/papers/1603.08861/) | 7 | 0 | 190 | CiteSeer, Cora, PubMed | LP, Planetoid*, SemiEmb |
| [2502.01122](/papers/2502.01122/) | [Learning Efficient Positional Encodings with Graph Neural Networks](/papers/2502.01122/) | 7 | 7 | 140 | Peptides-struct, REDDIT-BINARY, REDDIT-MULTI-5K, ZINC | GCN, GIN, GPS |
| [2310.18716](/papers/2310.18716/) | [Laplacian Canonization: A Minimalist Approach to Sign and Basis Invariant...](/papers/2310.18716/) | 7 | 3 | 133 | ZINC, ogbg-molpcba | GatedGCN, GatedGCN + MAP, GatedGCN+LapPE, Graph-ViT |
| [2306.02866](/papers/2306.02866/) | [Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance](/papers/2306.02866/) | 7 | 1 | 89 | Peptides-func, Peptides-struct | GCN, GINE, GatedGCN, SAN+RWSE |
| [2308.00887](/papers/2308.00887/) | [Factor Graph Neural Networks](/papers/2308.00887/) | 7 | 4 | 76 | QM9 | 123-gnn, DimeNet++, EGNN, MPNN |
| [2004.11198](/papers/2004.11198/) | [SIGN: Scalable Inception Graph Neural Networks](/papers/2004.11198/) | 7 | 4 | 59 | PPI, Reddit | Cluster-GCN, FastGCN, GCN, GraphSAGE |
| [1902.10197](/papers/1902.10197/) | [RotatE: Knowledge Graph Embedding by Relational Rotation in Complex Space](/papers/1902.10197/) | 7 | 1 | 55 | FB15k-237, WN18, WN18RR | ComplEx, ConvE, DistMult, TransE |
| [2106.07767](/papers/2106.07767/) | [How does Heterophily Impact the Robustness of Graph Neural Networks?...](/papers/2106.07767/) | 6 | 0 | 910 | CiteSeer, Cora | GCN-SVD, GraphSAGE, H2GCN |
| [2502.03251](/papers/2502.03251/) | [RiemannGFM: Learning a Graph Foundation Model from Riemannian Geometry](/papers/2502.03251/) | 6 | 4 | 597 | PubMed | DGI, GCN, GraphMAE, LLaGA |
| [1907.04786](/papers/1907.04786/) | [Fast Haar Transforms for Graph Neural Networks](/papers/1907.04786/) | 6 | 1 | 526 | PubMed | ChebNet, DeepWalk, GCN, LP |
| [2010.15421](/papers/2010.15421/) | [Scalable Graph Neural Networks via Bidirectional Propagation](/papers/2010.15421/) | 6 | 0 | 503 | PubMed | APPNP, GAT, GCN, GraphSAINT |
| [2501.11817](/papers/2501.11817/) | [Toward Effective Digraph Representation Learning: A Magnetic Adaptive Propagation based...](/papers/2501.11817/) | 6 | 2 | 502 | Cora | D-HYPR, DGCNN, Dir-GNN, GATv2 |
| [1803.10459](/papers/1803.10459/) | [Graphite: Iterative Generative Modeling of Graphs](/papers/1803.10459/) | 6 | 0 | 486 | CiteSeer, Cora | DeepWalk, GCN, GRAPHITE |
| [2309.09384](/papers/2309.09384/) | [Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci Curvature](/papers/2309.09384/) | 6 | 3 | 431 | Cora, Cornell, MUTAG | GCN, GIN |
| [2012.09600](/papers/2012.09600/) | [Deep Fusion Clustering Network](/papers/2012.09600/) | 6 | 1 | 430 | CiteSeer, DBLP | AE, ARGVA, GAE, K-means |
| [2306.13854](/papers/2306.13854/) | [arXiv:2306.13854](/papers/2306.13854/) | 6 | 0 | 424 | Cora, PubMed | ARIEL, BGRL, GCA, GRACE |
| [2207.00012](/papers/2207.00012/) | [Reliable Representations Make A Stronger Defender: Unsupervised Structure Refinement for...](/papers/2207.00012/) | 6 | 1 | 332 | CiteSeer, Cora | GCN, GNNGuard, ProtGNN, RGCN |
| [2501.16944](/papers/2501.16944/) | [Exact Computation of Any-Order Shapley Interactions for Graph Neural Networks](/papers/2501.16944/) | 6 | 5 | 264 | ENZYMES, MUTAG | GAT, GCN, GIN |
| [2206.07161](/papers/2206.07161/) | [arXiv:2206.07161](/papers/2206.07161/) | 6 | 1 | 224 | ogbn-arxiv, ogbn-products | Cluster-GCN, GraphSAGE, GraphSAINT, SIGN |
| [1904.08082](/papers/1904.08082/) | [Self-Attention Graph Pooling](/papers/1904.08082/) | 6 | 3 | 187 | D&D, NCI1 | DiffPool, SAGPool, Set2Set, SortPool |
| [2110.09344](/papers/2110.09344/) | [ifMixup: Interpolating Graph Pair to Regularize Graph Classification](/papers/2110.09344/) | 6 | 0 | 154 | ENZYMES, IMDB-BINARY, IMDB-MULTI, MUTAG | GAT, GCN |
| [2509.01254](/papers/2509.01254/) | [What Expressivity Theory Misses: Message Passing Complexity for GNNs](/papers/2509.01254/) | 6 | 6 | 150 | ZINC | CIN, FragNet, GCN, GIN |
| [2109.12872](/papers/2109.12872/) | [Meta-Aggregator: Learning to Aggregate for 1-bit Graph Neural Networks](/papers/2109.12872/) | 6 | 0 | 149 | ZINC | GAT, GCN, GIN, GatedGCN |
| [2505.11356](/papers/2505.11356/) | [Fractal Graph Contrastive Learning](/papers/2505.11356/) | 6 | 6 | 148 | MUTAG, NCI1, PROTEINS | GAE, GraphCL, SimGRACE |
| [1603.06186](/papers/1603.06186/) | [arXiv:1603.06186](/papers/1603.06186/) | 6 | 3 | 120 | ENZYMES, MUTAG, NCI1, PROTEINS | Graphlet, WL, sp |
| [1805.09076](/papers/1805.09076/) | [Constrained Graph Variational Autoencoders for Molecule Design](/papers/1805.09076/) | 6 | 0 | 115 | QM9, ZINC | DimeNet++, GCN, GIN, PNA |
| [2012.07219](/papers/2012.07219/) | [Breaking the Expressive Bottlenecks of Graph Neural Networks](/papers/2012.07219/) | 6 | 1 | 111 | COLLAB, REDDIT-MULTI-5K, ogbg-molpcba | DiffPool, GCN, GIN, GraphSAGE |
| [2205.12245](/papers/2205.12245/) | [Asynchronous Neural Networks for Learning in Graphs](/papers/2205.12245/) | 6 | 1 | 111 | IMDB-BINARY, IMDB-MULTI, PROTEINS | DGCNN, GAT, GCN, GIN |
| [2106.09553](/papers/2106.09553/) | [How Much Structural Information Large Scale Molecular Language Representations Can...](/papers/2106.09553/) | 6 | 3 | 73 | ESOL, FreeSolv, Lipophilicity, QM9 | 123-gnn, DimeNet++, GC, MPNN |
| [2407.12136](/papers/2407.12136/) | [Molecular Topological Profile (MOLTOP) - Simple and Strong Baseline for...](/papers/2407.12136/) | 6 | 6 | 57 | Peptides-func, ogbg-molhiv | GCN, GINE, GatedGCN, Graphormer |
| [1707.01476](/papers/1707.01476/) | [Convolutional 2D Knowledge Graph Embeddings](/papers/1707.01476/) | 6 | 2 | 49 | FB15k-237, WN18, WN18RR | ComplEx, ConvE, DistMult, R-GCN |
| [2102.07835](/papers/2102.07835/) | [Topological Graph Neural Networks](/papers/2102.07835/) | 6 | 3 | 48 | CLUSTER, D&D, ENZYMES | GAT, GCN, GIN, WL |
| [2302.11329](/papers/2302.11329/) | [HINormer: Representation Learning On Heterogeneous Information Networks with Graph Transformer](/papers/2302.11329/) | 6 | 6 | 48 | DBLP, IMDB | GAT, GCN, HGT, HetSANN |
| [2103.05872](/papers/2103.05872/) | [Sampling methods for efficient training of graph convolutional networks: A...](/papers/2103.05872/) | 6 | 6 | 46 | PPI, Reddit | AS-GCN, Cluster-GCN, FastGCN, LADIES |
| [1911.08538](/papers/1911.08538/) | [Heterogeneous Deep Graph Infomax](/papers/1911.08538/) | 6 | 0 | 42 | ACM, IMDB | DGI, GAT, GCN, HAN |
| [2405.16511](/papers/2405.16511/) | [SE3Set: Harnessing equivariant hypergraph neural networks for molecular representation learning](/papers/2405.16511/) | 6 | 6 | 36 | QM9 | ComENet, DimeNet++, Equiformer, PaiNN |
| [2312.17679](/papers/2312.17679/) | [Data Augmentation for Supervised Graph Outlier Detection via Latent Diffusion...](/papers/2312.17679/) | 6 | 0 | 34 | Questions, Tolokers | GAT, GCN, GT |
| [2510.09767](/papers/2510.09767/) | [HeSRN: Representation Learning On Heterogeneous Graphs via Slot-Aware Retentive Network](/papers/2510.09767/) | 6 | 6 | 15 | ACM, DBLP, Freebase, IMDB | GTN, HAN, HGT, HINormer |
| [2006.15646](/papers/2006.15646/) | [Expressive Power of Invariant and Equivariant Graph Neural Networks](/papers/2006.15646/) | 6 | 0 | 8 | ER graph | DGN, GAT, GCN, GIN |
| [2510.22555](/papers/2510.22555/) | [Cross-Paradigm Graph Backdoor Attacks with Promptable Subgraph Triggers](/papers/2510.22555/) | 5 | 5 | 676 | PubMed | GAT, GCN, GRACE, GraphPrompt |
| [2312.09041](/papers/2312.09041/) | [Graph Neural Networks with Diverse Spectral Filtering](/papers/2312.09041/) | 5 | 4 | 587 | Amazon-Computers, Amazon-Photo, CiteSeer, Cora | GPR-GNN |
| [2210.01002](/papers/2210.01002/) | [ASGNN: Graph Neural Networks with Adaptive Structure](/papers/2210.01002/) | 5 | 1 | 359 | CiteSeer, Cora | GCN, GCN-Jaccard, GCN-SVD, Pro-GNN |
| [2106.07476](/papers/2106.07476/) | [Training Graph Neural Networks with 1000 Layers](/papers/2106.07476/) | 5 | 0 | 226 | ogbn-arxiv, ogbn-proteins | GAT, GCN, GraphSAGE |
| [2605.24867](/papers/2605.24867/) | [Clustering as Reasoning: A $k$-Means Interpretation of Chain-of-Thought Graph Learning](/papers/2605.24867/) | 5 | 5 | 153 | Cora, ogbn-arxiv | GAT, GCN, GraphSAGE, SGC |
| [2209.08179](/papers/2209.08179/) | [Cell Attention Networks](/papers/2209.08179/) | 5 | 4 | 151 | MUTAG, NCI1, PROTEINS | DGCNN, GIN, PK |
| [2305.13987](/papers/2305.13987/) | [On Structural Expressive Power of Graph Transformers](/papers/2305.13987/) | 5 | 1 | 147 | ZINC | GAT, GCN, GIN, GraphSAGE |
| [2304.10668](/papers/2304.10668/) | [Train Your Own GNN Teacher: Graph-Aware Distillation on Textual Graphs](/papers/2304.10668/) | 5 | 2 | 118 | ogbn-arxiv, ogbn-products | GIANT, GLEM, GLEM-GNN |
| [2305.07100](/papers/2305.07100/) | [arXiv:2305.07100](/papers/2305.07100/) | 5 | 5 | 118 | QM9 | DimeNet++, EGNN, PaiNN, SchNet |
| [2312.07633](/papers/2312.07633/) | [SE(3)-Invariant Multiparameter Persistent Homology for Chiral-Sensitive Molecular Property Prediction](/papers/2312.07633/) | 5 | 3 | 92 | BBBP, ClinTox, ESOL, Lipophilicity | 3D Infomax, D-MPNN, GraphCL |
| [2410.10516](/papers/2410.10516/) | [UniGEM: A Unified Approach to Generation and Property Prediction for...](/papers/2410.10516/) | 5 | 4 | 66 | QM9 | 3D Infomax, 3D-MGP, EGNN, GEM |
| [1806.09231](/papers/1806.09231/) | [Clebsch--Gordan Nets: a Fully Fourier Space Spherical Convolutional Neural Network](/papers/1806.09231/) | 5 | 2 | 62 | QM9 | DimeNet++, E(3)-Equivariant GP, NequIP, PaiNN |
| [1912.10832](/papers/1912.10832/) | [An Attention-based Graph Neural Network for Heterogeneous Structural Learning](/papers/1912.10832/) | 5 | 0 | 30 | DBLP, IMDB | GAT, GCN, HAN |
| [2201.08821](/papers/2201.08821/) | [Representing Long-Range Context for Graph Neural Networks with Global Attention](/papers/2201.08821/) | 5 | 5 | 22 | Code, NCI1 | DAGNN, GCN, GIN, SAGPool |
| [2107.09422](/papers/2107.09422/) | [Large-scale graph representation learning with very deep GNNs and self-supervision](/papers/2107.09422/) | 5 | 2 | 17 | ogbn-mag | GAT, GCN, GraphSAGE, HAN |
| [1911.07323](/papers/1911.07323/) | [Layer-Dependent Importance Sampling for Training Deep and Large Graph Convolutional...](/papers/1911.07323/) | 4 | 0 | 700 | CiteSeer, Cora, PubMed, Reddit | GraphSAGE |
| [2411.17063](/papers/2411.17063/) | [Contrastive Graph Condensation: Advancing Data Versatility through Self-Supervised Learning](/papers/2411.17063/) | 4 | 4 | 666 | CiteSeer, Reddit, ogbn-arxiv | GCOND, Whole Dataset |
| [2403.09171](/papers/2403.09171/) | [ADEdgeDrop: Adversarial Edge Dropping for Robust Graph Neural Networks](/papers/2403.09171/) | 4 | 4 | 585 | Cora | GAT + DropEdge, GCN + DropEdge, GCN_n + DropNode, GraphSAGE + DropEdge |
| [2310.00800](/papers/2310.00800/) | [GraphPatcher: Mitigating Degree Bias for Graph Neural Networks via Test-time...](/papers/2310.00800/) | 4 | 3 | 576 | Cora, PubMed | DGI, GRACE |
| [2305.10758](/papers/2305.10758/) | [Extracting Low-/High- Frequency Knowledge from Graph Neural Networks and Injecting...](/papers/2305.10758/) | 4 | 0 | 486 | Cora | GAT, GCN, GLNN, GraphSAGE |
| [1910.03053](/papers/1910.03053/) | [Graph Few-shot Learning via Knowledge Transfer](/papers/1910.03053/) | 4 | 2 | 450 | PubMed | DeepWalk, LP, Node2Vec, Planetoid* |
| [2207.04396](/papers/2207.04396/) | [arXiv:2207.04396](/papers/2207.04396/) | 4 | 0 | 350 | Cora | GAT, GCN, GIN, SGC |
| [2508.00304](/papers/2508.00304/) | [Invariant Graph Transformer for Out-of-Distribution Generalization](/papers/2508.00304/) | 4 | 4 | 325 | D&D | CIGA, DIR, GIL, GSAT |
| [2406.13200](/papers/2406.13200/) | [RobGC: Towards Robust Graph Condensation](/papers/2406.13200/) | 4 | 4 | 309 | Cora, PubMed | GCN-Jaccard, GCN-SVD |
| [2210.13148](/papers/2210.13148/) | [Transformers over Directed Acyclic Graphs](/papers/2210.13148/) | 4 | 0 | 305 | CiteSeer, Cora, MalNet-Tiny, PubMed | GraphGPS, NodeFormer |
| [2203.07691](/papers/2203.07691/) | [Supervised Contrastive Learning with Structure Inference for Graph Classification](/papers/2203.07691/) | 4 | 2 | 252 | IMDB-BINARY, PROTEINS | GraphSAGE, SAGPool |
| [2502.02719](/papers/2502.02719/) | [Beyond Topological Self-Explainable GNNs: A Formal Explainability Perspective](/papers/2502.02719/) | 4 | 4 | 181 | BBBP, MUTAG | DIR, GIN, GSAT |
| [2205.15068](/papers/2205.15068/) | [Embedding Graphs on Grassmann Manifold](/papers/2205.15068/) | 4 | 4 | 170 | D&D, PROTEINS | EdgePool, SAGPool |
| [2402.08170](/papers/2402.08170/) | [arXiv:2402.08170](/papers/2402.08170/) | 4 | 0 | 153 | PubMed, ogbn-arxiv | GAT, GCN, SGC |
| [2304.03724](/papers/2304.03724/) | [GeoTMI: Predicting Quantum Chemical Property with Easy-to-Obtain Geometry via Positional...](/papers/2304.03724/) | 4 | 0 | 148 | QM9 | DimeNet++, EGNN, SchNet, Transformer |
| [2006.15107](/papers/2006.15107/) | [Building powerful and equivariant graph neural networks with structural message-passing](/papers/2006.15107/) | 4 | 0 | 134 | ZINC | GIN, GatedGCN, MPNN, PNA |
| [2312.13583](/papers/2312.13583/) | [Fine-tuning Graph Neural Networks by Preserving Graph Generative Patterns](/papers/2312.13583/) | 4 | 4 | 118 | BACE, BBBP, Tox21, ToxCast | Supervised |
| [2009.03509](/papers/2009.03509/) | [Masked Label Prediction: Unified Message Passing Model for Semi-Supervised Classification](/papers/2009.03509/) | 4 | 0 | 101 | ogbn-arxiv, ogbn-products, ogbn-proteins | Cluster-GCN, DeeperGCN, JK-Net |
| [2305.18758](/papers/2305.18758/) | [Task-Equivariant Graph Few-shot Learning](/papers/2305.18758/) | 4 | 1 | 84 | Cora | G-Meta, MAML, Meta-GNN, TENT |
| [2502.19693](/papers/2502.19693/) | [Accurate and Scalable Graph Neural Networks via Message Invariance](/papers/2502.19693/) | 4 | 2 | 56 | ogbn-papers100M, ogbn-products | Cluster-GCN, GraphSAINT, SGC, SIGN |
| [2006.04804](/papers/2006.04804/) | [Optimal Transport Graph Neural Networks](/papers/2006.04804/) | 4 | 0 | 43 | ESOL, Lipophilicity | D-MPNN, GAT, GIN |
| [2308.02565](/papers/2308.02565/) | [SimTeG: A Frustratingly ple Approach Improves xtual raph Learning](/papers/2308.02565/) | 4 | 4 | 42 | ogbl-citation2, ogbn-products | GraphSAGE, MLP, SAGN+SCR |
| [2303.00170](/papers/2303.00170/) | [Asymmetric Learning for Graph Neural Network based Link Prediction](/papers/2303.00170/) | 4 | 0 | 20 | ogbl-collab | AA, CN, GAT, SEAL |
| [2206.08515](/papers/2206.08515/) | [ComENet: Towards Complete and Efficient Message Passing for 3D Molecular...](/papers/2206.08515/) | 4 | 0 | 7 | QM9 | DimeNet++, PaiNN, SchNet, SphereNet |
| [1911.07532](/papers/1911.07532/) | [Graph Neural Ordinary Differential Equations](/papers/1911.07532/) | 3 | 1 | 418 | CiteSeer, Cora, PubMed | GCN |
| [2110.14038](/papers/2110.14038/) | [Robustness of Graph Neural Networks at Scale](/papers/2110.14038/) | 3 | 0 | 416 | CiteSeer | GCN + Vanilla, GCN-Jaccard, RGCN |
| [2504.15920](/papers/2504.15920/) | [ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order Neighboring...](/papers/2504.15920/) | 3 | 3 | 323 | CiteSeer | GRAND, RGCN, SIGN |
| [1910.11945](/papers/1910.11945/) | [Improving Graph Attention Networks with Large Margin-based Constraints](/papers/1910.11945/) | 3 | 0 | 157 | Cora | GAT, GCN, GraphSAGE |
| [2212.05517](/papers/2212.05517/) | [SchNetPack 2.0: A neural network toolbox for atomistic machine learning](/papers/2212.05517/) | 3 | 1 | 148 | MD17, QM9 | PaiNN, SchNet |
| [2206.02789](/papers/2206.02789/) | [Efficient and Accurate Physics-aware Multiplex Graph Neural Networks for 3D...](/papers/2206.02789/) | 3 | 0 | 139 | QM9 | DimeNet++, PhysNet, SchNet |
| [2310.10434](/papers/2310.10434/) | [Equivariant Matrix Function Neural Networks](/papers/2310.10434/) | 3 | 2 | 133 | ZINC | GAT, GCN, Graphormer |
| [2210.02997](/papers/2210.02997/) | [Expander Graph Propagation](/papers/2210.02997/) | 3 | 1 | 126 | Code, ogbg-molhiv, ogbg-molpcba | GIN |
| [2506.13911](/papers/2506.13911/) | [Logical Expressiveness of Graph Neural Networks with Hierarchical Node Individualization](/papers/2506.13911/) | 3 | 3 | 122 | ZINC | GCN, GIN, PNA |
| [2102.09844](/papers/2102.09844/) | [arXiv:2102.09844](/papers/2102.09844/) | 3 | 0 | 118 | QM9 | DimeNet++, EGNN, SchNet |
| [2106.09575](/papers/2106.09575/) | [Rotation Invariant Graph Neural Networks using Spin Convolutions](/papers/2106.09575/) | 3 | 0 | 118 | QM9 | DimeNet++, EGNN, SchNet |
| [2203.14082](/papers/2203.14082/) | [Metropolis-Hastings Data Augmentation for Graph Neural Networks](/papers/2203.14082/) | 3 | 1 | 115 | CiteSeer, Cora | GCN + DropEdge, GCN + Vanilla, GraphSAGE + Vanilla |
| [2006.06972](/papers/2006.06972/) | [Towards Deeper Graph Neural Networks with Differentiable Group Normalization](/papers/2006.06972/) | 3 | 0 | 110 | Coauthor-CS | GAT, GCN, SGC |
| [2407.12419](/papers/2407.12419/) | [arXiv:2407.12419](/papers/2407.12419/) | 3 | 3 | 89 | Peptides-struct | GCN, GINE, GatedGCN |
| [2410.21043](/papers/2410.21043/) | [Disentangled and Self-Explainable Node Representation Learning](/papers/2410.21043/) | 3 | 3 | 80 | PPI | DeepWalk, GraphMAE, GraphSAGE |
| [2401.14578](/papers/2401.14578/) | [GOAt: Explaining Graph Neural Networks via Graph Output Attribution](/papers/2401.14578/) | 3 | 3 | 65 | NCI1 | GCN, GIN, GraphSAGE |
| [2111.06483](/papers/2111.06483/) | [arXiv:2111.06483](/papers/2111.06483/) | 3 | 0 | 60 | ogbn-papers100M, ogbn-products | GAT, GraphSAGE |
| [2206.13602](/papers/2206.13602/) | [Molecular Geometry Pretraining with SE(3)-Invariant Denoising Distance Matching](/papers/2206.13602/) | 3 | 0 | 53 | MD17, QM9 | Distance Prediction, PaiNN, Type Prediction |
| [2110.13197](/papers/2110.13197/) | [Nested Graph Neural Networks](/papers/2110.13197/) | 3 | 3 | 51 | QM9 | 123-gnn, DTNN, MPNN |
| [1803.07294](/papers/1803.07294/) | [GaAN: Gated Attention Networks for Learning on Large and Spatiotemporal...](/papers/1803.07294/) | 3 | 1 | 49 | PPI, Reddit | GaAN, GraphSAGE |
| [2402.08824](/papers/2402.08824/) | [Disambiguated Node Classification with Graph Neural Networks](/papers/2402.08824/) | 3 | 2 | 48 | Actor, Amazon-Computers, Chameleon | DGI, GCN |
| [2302.09532](/papers/2302.09532/) | [Pseudo Contrastive Learning for Graph-based Semi-supervised Learning](/papers/2302.09532/) | 3 | 3 | 45 | Cora | Co-training, Intersection, Union |
| [1711.10907](/papers/1711.10907/) | [Deep Reinforcement Learning for De-Novo Drug Design](/papers/1711.10907/) | 3 | 0 | 33 | QM9 | DimeNet++, Equiformer, PaiNN |
| [2106.01829](/papers/2106.01829/) | [arXiv:2106.01829](/papers/2106.01829/) | 3 | 0 | 32 | QM9 | ALIGNN, DimeNet++, SchNet |
| [1905.02850](/papers/1905.02850/) | [Understanding Attention and Generalization in Graph Neural Networks](/papers/1905.02850/) | 3 | 2 | 24 | MNIST, SAT Solving | GCN, GIN |
| [2212.12488](/papers/2212.12488/) | [Bring Your Own View: Graph Neural Networks for Link Prediction...](/papers/2212.12488/) | 3 | 0 | 20 | ogbl-collab, ogbl-ddi | GraphSAGE, SEAL |
| [2302.06299](/papers/2302.06299/) | [Homophily-oriented Heterogeneous Graph Rewiring](/papers/2302.06299/) | 3 | 3 | 15 | DBLP | GAT, GCN, RGCN |
| [2605.05689](/papers/2605.05689/) | [GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency Model](/papers/2605.05689/) | 3 | 3 | 15 | MNIST | GAT, GCN, GIN |
| [2409.08023](/papers/2409.08023/) | [Edge-Wise Graph-Instructed Neural Networks](/papers/2409.08023/) | 3 | 3 | 3 | BA graph | GraphGPS, GraphSAGE, SAN |
| [1905.07953](/papers/1905.07953/) | [Cluster-GCN: An Efficient Algorithm for Training Deep and Large Graph...](/papers/1905.07953/) | 3 | 1 | 2 | Reddit | GaAN, GraphSAGE, R-GCN |
| [2302.13522](/papers/2302.13522/) | [IGB: Addressing The Gaps In Labeling, Features, Heterogeneity, and Size...](/papers/2302.13522/) | 3 | 0 | 2 | SAT Solving | GAT, GCN, GraphSAGE |
| [2202.08057](/papers/2202.08057/) | [Understanding and Improving Graph Injection Attack by Promoting Unnoticeability](/papers/2202.08057/) | 2 | 0 | 503 | CiteSeer, Cora | MLP |
| [2110.15174](/papers/2110.15174/) | [On Provable Benefits of Depth in Training Graph Convolutional Networks](/papers/2110.15174/) | 2 | 0 | 237 | ogbn-arxiv | APPNP, GCN |
| [2212.08174](/papers/2212.08174/) | [Non-IID Transfer Learning on Graphs](/papers/2212.08174/) | 2 | 2 | 228 | D&D | GCN, SGC |
| [1711.08267](/papers/1711.08267/) | [GraphGAN: Graph Representation Learning with Generative Adversarial Nets](/papers/1711.08267/) | 2 | 0 | 210 | D&D | DeepWalk, Node2Vec |
| [1908.01000](/papers/1908.01000/) | [InfoGraph: Unsupervised and Semi-supervised Graph-Level Representation Learning via Mutual Information...](/papers/1908.01000/) | 2 | 0 | 208 | MUTAG, QM9 | InfoGraph, WL |
| [2406.08709](/papers/2406.08709/) | [Introducing Diminutive Causal Structure into Graph Representation Learning](/papers/2406.08709/) | 2 | 1 | 186 | BA graph, D&D | GAT |
| [2312.08852](/papers/2312.08852/) | [ERASE: Error-Resilient Representation Learning on Graphs for Label Noise Tolerance](/papers/2312.08852/) | 2 | 0 | 185 | Cora, ogbn-arxiv | GCE |
| [2310.00183](/papers/2310.00183/) | [On the Equivalence of Graph Convolution and Mixup](/papers/2310.00183/) | 2 | 0 | 184 | Cora | MLP, SGC |
| [2106.09078](/papers/2106.09078/) | [Probing GNN Explainers: A Rigorous Theoretical and Empirical Analysis of...](/papers/2106.09078/) | 2 | 0 | 182 | Cora, PubMed | GraphSAGE |
| [2605.05534](/papers/2605.05534/) | [Adversarial Graph Neural Network Benchmarks: Towards Practical and Fair Evaluation](/papers/2605.05534/) | 2 | 2 | 167 | Chameleon, Squirrel | GCN |
| [2508.11513](/papers/2508.11513/) | [Towards Faithful Class-level Self-explainability in Graph Neural Networks by Subgraph...](/papers/2508.11513/) | 2 | 2 | 164 | MUTAG | GCN, PGIB |
| [1711.08920](/papers/1711.08920/) | [SplineCNN: Fast Geometric Deep Learning with Continuous B-Spline Kernels](/papers/1711.08920/) | 2 | 0 | 126 | Cora | ChebNet, GCN |
| [2010.09885](/papers/2010.09885/) | [ChemBERTa: Large-Scale Self-Supervised Pretraining for Molecular Property Prediction](/papers/2010.09885/) | 2 | 0 | 124 | BBBP, Tox21 | D-MPNN |
| [1912.06058](/papers/1912.06058/) | [Coloring graph neural networks for node disambiguation](/papers/1912.06058/) | 2 | 1 | 111 | IMDB-BINARY, PROTEINS | DGCNN |
| [2102.13085](/papers/2102.13085/) | [Towards Robust Graph Contrastive Learning](/papers/2102.13085/) | 2 | 0 | 102 | Amazon-Photo | GCA, GRACE |
| [2205.15653](/papers/2205.15653/) | [Label-Enhanced Graph Neural Network for Semi-supervised Node Classification](/papers/2205.15653/) | 2 | 1 | 101 | ogbn-arxiv | DeeperGCN, JK-Net |
| [2402.07568](/papers/2402.07568/) | [--Leman at the margin: When more expressivity matters](/papers/2402.07568/) | 2 | 2 | 93 | ENZYMES, PROTEINS | 1-WL |
| [2002.12880](/papers/2002.12880/) | [arXiv:2002.12880](/papers/2002.12880/) | 2 | 0 | 89 | QM9 | Cormorant, SchNet |
| [2301.10857](/papers/2301.10857/) | [arXiv:2301.10857](/papers/2301.10857/) | 2 | 0 | 72 | Peptides-func | GCN, GIN |
| [2601.20815](/papers/2601.20815/) | [GNN Explanations that do not Explain and How to find...](/papers/2601.20815/) | 2 | 2 | 70 | MNIST, MUTAG | DIR, GAT |
| [2412.14451](/papers/2412.14451/) | [CLDG: Contrastive Learning on Dynamic Graphs](/papers/2412.14451/) | 2 | 2 | 64 | Reddit | DGI, GraphSAGE |
| [2405.18378](/papers/2405.18378/) | [A Canonicalization Perspective on Invariant and Equivariant Learning](/papers/2405.18378/) | 2 | 2 | 54 | Tox21, ogbg-molpcba | PNA |
| [2007.02901](/papers/2007.02901/) | [Wiki-CS: A Wikipedia-Based Benchmark for Graph Neural Networks](/papers/2007.02901/) | 2 | 0 | 52 | WikiCS | GAT, GCN |
| [2212.10789](/papers/2212.10789/) | [Multi-modal Molecule Structure-text Model for Text-based Retrieval and Editing](/papers/2212.10789/) | 2 | 0 | 52 | BBBP, SIDER | GraphMVP |
| [2309.00976](/papers/2309.00976/) | [Pure Message Passing Can Estimate Common Neighbor for Link Prediction](/papers/2309.00976/) | 2 | 2 | 39 | ogbl-collab | GCN, SAGE |
| [2510.08450](/papers/2510.08450/) | [: Mitigating by Increasing Storage Capacity](/papers/2510.08450/) | 2 | 2 | 31 | Peptides-func, Peptides-struct | DRew-GCN, MPNN |
| [2511.03824](/papers/2511.03824/) | [Sketch-Augmented Features Improve Learning Long-Range Dependencies in Graph Neural Networks](/papers/2511.03824/) | 2 | 2 | 31 | Peptides-struct, REDDIT-MULTI-5K | GPS, SignNet-8S |
| [2312.10988](/papers/2312.10988/) | [Graph Invariant Learning with Subgraph Co-mixup for Out-Of-Distribution Generalization](/papers/2312.10988/) | 2 | 0 | 16 | BA graph | DIR, V-REx |
| [1603.05629](/papers/1603.05629/) | [Discriminative Embeddings of Latent Variable Models for Structured Data](/papers/1603.05629/) | 2 | 2 | 12 | NCI1 | WL edge, sp |
| [2101.07965](/papers/2101.07965/) | [Directed Acyclic Graph Neural Networks](/papers/2101.07965/) | 2 | 2 | 12 | Code | GCN, GIN |
| [2208.09957](/papers/2208.09957/) | [Heterogeneous Graph Masked Autoencoders](/papers/2208.09957/) | 2 | 0 | 11 | Freebase | HAN, HetGNN |
| [1802.01572](/papers/1802.01572/) | [MotifNet: a motif-based Graph Convolutional Network for directed graphs](/papers/1802.01572/) | 1 | 0 | 803 | Cora | ChebNet |
| [2003.13663](/papers/2003.13663/) | [Revisiting Oversmoothing in Deep GCNs](/papers/2003.13663/) | 1 | 0 | 495 | Cora | GCN |
| [2407.09468](/papers/2407.09468/) | [Beyond Euclid: An Illustrated Guide to Modern Machine Learning with...](/papers/2407.09468/) | 1 | 0 | 361 | Cora | DHGNN |
| [2006.04064](/papers/2006.04064/) | [Bayesian Graph Neural Networks with Adaptive Connection Sampling](/papers/2006.04064/) | 1 | 0 | 233 | CiteSeer | DoG (GCN) |
| [2203.14303](/papers/2203.14303/) | [TREND: TempoRal Event and Node Dynamics for Graph Representation Learning](/papers/2203.14303/) | 1 | 0 | 228 | D&D | GraphSAGE |
| [2402.12984](/papers/2402.12984/) | [Can GNN be Good Adapter for LLMs?](/papers/2402.12984/) | 1 | 1 | 220 | ogbn-arxiv | BERT-GNN |
| [1905.13728](/papers/1905.13728/) | [Pre-Training Graph Neural Networks for Generic Structural Feature Extraction](/papers/1905.13728/) | 1 | 1 | 207 | PubMed | Graph Convolutional Network |
| [2412.16435](/papers/2412.16435/) | [THeGCN: Temporal Heterophilic Graph Convolutional Network](/papers/2412.16435/) | 1 | 1 | 204 | D&D | TGAT |
| [2408.13661](/papers/2408.13661/) | [Hierarchical Network Fusion for Multi-Modal Electron Micrograph Representation Learning with...](/papers/2408.13661/) | 1 | 1 | 160 | D&D | NEST |
| [2110.14363](/papers/2110.14363/) | [VQ-GNN: A Universal Framework to Scale-up Graph Neural Networks using...](/papers/2110.14363/) | 1 | 0 | 128 | ogbn-arxiv | Cluster-GCN |
| [1410.3314](/papers/1410.3314/) | [Propagation Kernels](/papers/1410.3314/) | 1 | 0 | 126 | MUTAG | WL |
| [2006.05057](/papers/2006.05057/) | [Towards More Practical Adversarial Attacks on Graph Neural Networks](/papers/2006.05057/) | 1 | 0 | 125 | CiteSeer | Degree |
| [1901.00596](/papers/1901.00596/) | [A Comprehensive Survey on Graph Neural Networks](/papers/1901.00596/) | 1 | 0 | 110 | PROTEINS | DGCNN |
| [2410.13974](/papers/2410.13974/) | [Are You Using Reliable Graph Prompts? Trojan Prompt Attacks on...](/papers/2410.13974/) | 1 | 1 | 75 | CiteSeer | DC-Graph (Clean) |
| [1909.00958](/papers/1909.00958/) | [Graph Representation Learning: A Survey](/papers/1909.00958/) | 1 | 0 | 67 | Cora | Node2Vec |
| [2412.19211](/papers/2412.19211/) | [Large Language Models Meet Graph Neural Networks: A Perspective of...](/papers/2412.19211/) | 1 | 1 | 54 | ogbn-arxiv | GraDBERT |
| [2111.05639](/papers/2111.05639/) | [Graph Transplant: Node Saliency-Guided Graph Mixup with Local Structure Preservation](/papers/2111.05639/) | 1 | 1 | 51 | D&D | Vanilla |
| [1904.05003](/papers/1904.05003/) | [Semi-Supervised Graph Classification: A Hierarchical Graph Perspective](/papers/1904.05003/) | 1 | 0 | 46 | D&D | WL |
| [2108.00219](/papers/2108.00219/) | [Grain: Improving Data Efficiency of Graph Neural Networks via Diversified...](/papers/2108.00219/) | 1 | 1 | 43 | CiteSeer | Random |
| [2305.07521](/papers/2305.07521/) | [AGFormer: Efficient Graph Representation with Anchor-Graph Transformer](/papers/2305.07521/) | 1 | 0 | 25 | NCI1 | GIN |
| [2401.09125](/papers/2401.09125/) | [arXiv:2401.09125](/papers/2401.09125/) | 1 | 0 | 25 | Cora | MLP |
| [2011.09679](/papers/2011.09679/) | [Scalable Graph Neural Networks for Heterogeneous Graphs](/papers/2011.09679/) | 1 | 0 | 22 | ogbn-mag | HGT |
| [2306.08385](/papers/2306.08385/) | [Align All the Nodes: Scalable Learning of Flexible Latent Structure...](/papers/2306.08385/) | 1 | 1 | 21 | 20News | IDGL |
| [2401.11772](/papers/2401.11772/) | [LightDiC: A Simple yet Effective Approach for Large-scale Digraph Representation...](/papers/2401.11772/) | 1 | 0 | 21 | WikiCS | MGC |
| [2308.06960](/papers/2308.06960/) | [Search to Fine-tune Pre-trained Graph Neural Networks for Graph-level Tasks](/papers/2308.06960/) | 1 | 0 | 20 | ClinTox | ContextPred |
| [2312.04234](/papers/2312.04234/) | [Graph Convolutions Enrich the Self-Attention in Transformers!](/papers/2312.04234/) | 1 | 0 | 19 | CIFAR10 | Graph-ViT |
| [2006.07889](/papers/2006.07889/) | [Graph Meta Learning via Local Subgraphs](/papers/2006.07889/) | 1 | 0 | 18 | ogbn-arxiv | Meta-GNN |
| [2201.12872](/papers/2201.12872/) | [Discovering Invariant Rationales for Graph Neural Networks](/papers/2201.12872/) | 1 | 0 | 13 | MNIST | ERM |
| [2501.04102](/papers/2501.04102/) | [Enhancing Distribution and Label Consistency for Graph Out-of-Distribution Generalization](/papers/2501.04102/) | 1 | 1 | 13 | MNIST | ERM |
| [2409.17475](/papers/2409.17475/) | [On the Impact of Feature Heterophily on Link Prediction with...](/papers/2409.17475/) | 1 | 1 | 7 | ogbl-collab | CN |
| [2209.05710](/papers/2209.05710/) | [MDM: Molecular Diffusion Model for 3D Molecule Generation](/papers/2209.05710/) | 1 | 0 | 5 | QM9 | EDM |
| [2302.06835](/papers/2302.06835/) | [Understanding Oversquashing in GNNs through the Lens of Effective Resistance](/papers/2302.06835/) | 1 | 0 | 2 | IMDB-BINARY | GCN + FoSR |
| [2307.14613](/papers/2307.14613/) | [Self-Contrastive Graph Diffusion Network](/papers/2307.14613/) | 1 | 0 | 1 | AMAP | MVGRL |
| [2505.20853](/papers/2505.20853/) | [arXiv:2505.20853](/papers/2505.20853/) | 1 | 1 | 1 | ogbn-mag | GCN |
| [2312.13136](/papers/2312.13136/) | [Molecular Hypergraph Neural Networks](/papers/2312.13136/) | 1 | 1 | 0 | PCQM4Mv2 | GCN |

### Flagged Rows

| ArXiv | Dataset | Model | Actual | Paper | Rank Shift | Actual Source | Timing |
|---|---|---|---:|---:|---:|---|---|
| [2601.15124](/papers/2601.15124/) | Cora | GCN | 0.9004 | 0.2840 | 925 | [arXiv:2401.09125](/papers/2401.09125/) | already known (2024-01) |
| [2605.14809](/papers/2605.14809/) | Cora | GCN | 0.9004 | 0.2985 | 923 | [arXiv:2401.09125](/papers/2401.09125/) | already known (2024-01) |
| [2502.08092](/papers/2502.08092/) | Cora | GCN | 0.9004 | 0.3250 | 919 | [arXiv:2401.09125](/papers/2401.09125/) | already known (2024-01) |
| [2510.12140](/papers/2510.12140/) | Cora | GCN | 0.9004 | 0.3465 | 917 | [arXiv:2401.09125](/papers/2401.09125/) | already known (2024-01) |
| [2106.07767](/papers/2106.07767/) | Cora | GraphSAGE | 0.8998 | 0.3667 | 910 | [SPGCL: Simple yet Powerful Graph Contrastive Learning via...](/papers/2602.00064/) | published later (2026-02) |
| [2405.16800](/papers/2405.16800/) | Cora | GRACE | 0.8911 | 0.1460 | 905 | [Toward Graph-Tokenizing Large Language Models with Reconstructive Graph...](/papers/2603.01385/) | published later (2026-03) |
| [2502.11836](/papers/2502.11836/) | Cora | LLaGA | 0.8900 | 0.1162 | 902 | [Adversarial Attacks and Defenses on Graph-aware Large Language...](/papers/2508.04894/) | published later (2025-08) |
| [2305.03324](/papers/2305.03324/) | Cora | GCN | 0.9004 | 0.4115 | 901 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2601.15124](/papers/2601.15124/) | Cora | GAT | 0.8897 | 0.2970 | 891 | [Clustering as Reasoning: A $k$-Means Interpretation of Chain-of-Thought...](/papers/2605.24867/) | published later (2026-05-24) |
| [2511.05592](/papers/2511.05592/) | Cora | GAT | 0.8897 | 0.2972 | 891 | [Clustering as Reasoning: A $k$-Means Interpretation of Chain-of-Thought...](/papers/2605.24867/) | published later (2026-05-24) |
| [2502.08092](/papers/2502.08092/) | Cora | GAT | 0.8897 | 0.3100 | 890 | [Clustering as Reasoning: A $k$-Means Interpretation of Chain-of-Thought...](/papers/2605.24867/) | published later (2026-05-24) |
| [2605.14809](/papers/2605.14809/) | Cora | GAT | 0.8897 | 0.3325 | 887 | [Clustering as Reasoning: A $k$-Means Interpretation of Chain-of-Thought...](/papers/2605.24867/) | published later (2026-05-24) |
| [2601.02662](/papers/2601.02662/) | Cora | GCN | 0.9004 | 0.4592 | 884 | [arXiv:2401.09125](/papers/2401.09125/) | already known (2024-01) |
| [2502.11836](/papers/2502.11836/) | Cora | GraphGPS | 0.8845 | 0.1748 | 876 | [Clustering as Reasoning: A $k$-Means Interpretation of Chain-of-Thought...](/papers/2605.24867/) | published later (2026-05-24) |
| [2505.22362](/papers/2505.22362/) | Cora | GCN | 0.9004 | 0.5237 | 865 | [arXiv:2401.09125](/papers/2401.09125/) | already known (2024-01) |
| [2605.14809](/papers/2605.14809/) | Cora | H2GCN | 0.8829 | 0.3090 | 855 | [Adapting to Heterophilic Graph Data with Structure-Guided Neighbor...](/papers/2506.08871/) | already known (2025-06) |
| [2601.02662](/papers/2601.02662/) | Cora | GAT | 0.8897 | 0.4573 | 853 | [Clustering as Reasoning: A $k$-Means Interpretation of Chain-of-Thought...](/papers/2605.24867/) | published later (2026-05-24) |
| [2602.00064](/papers/2602.00064/) | Cora | SGC | 0.8805 | 0.3205 | 843 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | already known (2026-02) |
| [2106.07767](/papers/2106.07767/) | Cora | H2GCN | 0.8829 | 0.3889 | 841 | [Adapting to Heterophilic Graph Data with Structure-Guided Neighbor...](/papers/2506.08871/) | published later (2025-06) |
| [2510.12140](/papers/2510.12140/) | Cora | SGC | 0.8805 | 0.3956 | 828 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2505.22362](/papers/2505.22362/) | Cora | GAT | 0.8897 | 0.5412 | 825 | [Clustering as Reasoning: A $k$-Means Interpretation of Chain-of-Thought...](/papers/2605.24867/) | published later (2026-05-24) |
| [1905.09718](/papers/1905.09718/) | Cora | GCN | 0.9004 | 0.6033 | 809 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2406.19258](/papers/2406.19258/) | Cora | FAGCN | 0.8885 | 0.5661 | 805 | [Language is All a Graph Needs](/papers/2308.07134/) | already known (2023-08) |
| [2602.02268](/papers/2602.02268/) | Cora | SpecFormer | 0.8819 | 0.4883 | 803 | [Polynomial Selection in Spectral Graph Neural Networks: An...](/papers/2404.15354/) | already known (2024-04) |
| [1802.01572](/papers/1802.01572/) | Cora | ChebNet | 0.8969 | 0.6000 | 803 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | published later (2024-03) |
| [2502.08092](/papers/2502.08092/) | CiteSeer | GCN | 0.8800 | 0.2636 | 801 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2505.17660](/papers/2505.17660/) | Cora | GCN | 0.9004 | 0.6176 | 801 | [arXiv:2401.09125](/papers/2401.09125/) | already known (2024-01) |
| [2601.15124](/papers/2601.15124/) | CiteSeer | GCN | 0.8800 | 0.2930 | 798 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2502.08092](/papers/2502.08092/) | CiteSeer | GAT | 0.8227 | 0.2771 | 796 | [Instance-Aware Graph Prompt Learning](/papers/2411.17676/) | already known (2024-11) |
| [2210.10946](/papers/2210.10946/) | Cora | GAT | 0.8897 | 0.5800 | 795 | [Clustering as Reasoning: A $k$-Means Interpretation of Chain-of-Thought...](/papers/2605.24867/) | published later (2026-05-24) |
| [2601.15124](/papers/2601.15124/) | CiteSeer | GAT | 0.8227 | 0.2930 | 793 | [Instance-Aware Graph Prompt Learning](/papers/2411.17676/) | already known (2024-11) |
| [2505.17660](/papers/2505.17660/) | Cora | GraphGPS | 0.8845 | 0.5576 | 793 | [Clustering as Reasoning: A $k$-Means Interpretation of Chain-of-Thought...](/papers/2605.24867/) | published later (2026-05-24) |
| [2601.02662](/papers/2601.02662/) | CiteSeer | GCN | 0.8800 | 0.3217 | 791 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2106.07767](/papers/2106.07767/) | CiteSeer | GraphSAGE | 0.8269 | 0.3167 | 788 | [Probing GNN Explainers: A Rigorous Theoretical and Empirical...](/papers/2106.09078/) | published later (2021-06-16) |
| [2601.02662](/papers/2601.02662/) | CiteSeer | GAT | 0.8227 | 0.3231 | 786 | [Instance-Aware Graph Prompt Learning](/papers/2411.17676/) | already known (2024-11) |
| [2405.16800](/papers/2405.16800/) | Cora | GraphCL | 0.8653 | 0.1760 | 777 | [Toward Graph-Tokenizing Large Language Models with Reconstructive Graph...](/papers/2603.01385/) | published later (2026-03) |
| [2402.11235](/papers/2402.11235/) | Cora | GraphCL | 0.8653 | 0.2622 | 774 | [Toward Graph-Tokenizing Large Language Models with Reconstructive Graph...](/papers/2603.01385/) | published later (2026-03) |
| [2406.19258](/papers/2406.19258/) | Cora | ACMGCN | 0.8975 | 0.6511 | 773 | [Language is All a Graph Needs](/papers/2308.07134/) | already known (2023-08) |
| [2510.17185](/papers/2510.17185/) | CiteSeer | GAT | 0.8227 | 0.4143 | 766 | [Instance-Aware Graph Prompt Learning](/papers/2411.17676/) | already known (2024-11) |
| [2406.19258](/papers/2406.19258/) | Cora | APPNP | 0.8904 | 0.6337 | 763 | [arXiv:2310.10064](/papers/2310.10064/) | already known (2023-10) |
| [2511.05592](/papers/2511.05592/) | Cora | GraphCL | 0.8653 | 0.3592 | 759 | [Toward Graph-Tokenizing Large Language Models with Reconstructive Graph...](/papers/2603.01385/) | published later (2026-03) |
| [2210.10946](/papers/2210.10946/) | CiteSeer | GAT | 0.8227 | 0.4600 | 752 | [Instance-Aware Graph Prompt Learning](/papers/2411.17676/) | published later (2024-11) |
| [2505.17660](/papers/2505.17660/) | Cora | APPNP | 0.8904 | 0.6516 | 752 | [arXiv:2310.10064](/papers/2310.10064/) | already known (2023-10) |
| [2505.17660](/papers/2505.17660/) | Cora | NodeFormer | 0.8856 | 0.6182 | 751 | [Bridging Large Language Models and Graph Structure Learning...](/papers/2410.12096/) | already known (2024-10) |
| [2505.17660](/papers/2505.17660/) | Cora | GAT | 0.8897 | 0.6447 | 751 | [Clustering as Reasoning: A $k$-Means Interpretation of Chain-of-Thought...](/papers/2605.24867/) | published later (2026-05-24) |
| [2505.17660](/papers/2505.17660/) | Cora | GPRGNN | 0.8929 | 0.6712 | 748 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | already known (2024-03) |
| [2510.17185](/papers/2510.17185/) | CiteSeer | GCN | 0.8800 | 0.5078 | 743 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2406.19258](/papers/2406.19258/) | Cora | GraphGPS | 0.8845 | 0.6208 | 743 | [Clustering as Reasoning: A $k$-Means Interpretation of Chain-of-Thought...](/papers/2605.24867/) | published later (2026-05-24) |
| [2510.12140](/papers/2510.12140/) | Cora | GRACE | 0.8911 | 0.6648 | 743 | [Toward Graph-Tokenizing Large Language Models with Reconstructive Graph...](/papers/2603.01385/) | published later (2026-03) |
| [2510.17185](/papers/2510.17185/) | CiteSeer | GPRGNN | 0.8033 | 0.4498 | 741 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | already known (2024-03) |
| [2510.12140](/papers/2510.12140/) | CiteSeer | GCN | 0.8800 | 0.5195 | 739 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2106.07767](/papers/2106.07767/) | CiteSeer | H2GCN | 0.7711 | 0.2722 | 738 | [Optimization-Induced Graph Implicit Nonlinear Diffusion](/papers/2206.14418/) | published later (2022-06-29) |
| [1905.10990](/papers/1905.10990/) | Cora | GIN | 0.8705 | 0.5210 | 736 | [Unleashing the Potential of Text-attributed Graphs: Automatic Relation...](/papers/2405.18581/) | published later (2024-05) |
| [2505.22362](/papers/2505.22362/) | Cora | GPRGNN | 0.8929 | 0.6888 | 728 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | already known (2024-03) |
| [2505.22362](/papers/2505.22362/) | Cora | ACMGCN | 0.8975 | 0.6996 | 728 | [Language is All a Graph Needs](/papers/2308.07134/) | already known (2023-08) |
| [2605.14809](/papers/2605.14809/) | Cora | SAGE | 0.8573 | 0.3576 | 727 | [Efficient Tuning and Inference for Large Language Models...](/papers/2401.15569/) | already known (2024-01) |
| [2505.22362](/papers/2505.22362/) | Cora | H2GCN | 0.8829 | 0.6286 | 727 | [Adapting to Heterophilic Graph Data with Structure-Guided Neighbor...](/papers/2506.08871/) | published later (2025-06) |
| [2406.19258](/papers/2406.19258/) | Cora | GPRGNN | 0.8929 | 0.6908 | 727 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | already known (2024-03) |
| [2305.15747](/papers/2305.15747/) | CiteSeer | GraphSAGE | 0.8269 | 0.5502 | 726 | [Probing GNN Explainers: A Rigorous Theoretical and Empirical...](/papers/2106.09078/) | already known (2021-06-16) |
| [1905.09718](/papers/1905.09718/) | Cora | SGC | 0.8805 | 0.6164 | 723 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2305.15747](/papers/2305.15747/) | Cora | GraphSAGE | 0.8998 | 0.7060 | 723 | [SPGCL: Simple yet Powerful Graph Contrastive Learning via...](/papers/2602.00064/) | published later (2026-02) |
| [1905.10990](/papers/1905.10990/) | Cora | GAT | 0.8897 | 0.6800 | 721 | [Clustering as Reasoning: A $k$-Means Interpretation of Chain-of-Thought...](/papers/2605.24867/) | published later (2026-05-24) |
| [2406.19258](/papers/2406.19258/) | Cora | SGC | 0.8805 | 0.6277 | 716 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2502.08092](/papers/2502.08092/) | Cora | GraphCL | 0.8653 | 0.5196 | 713 | [Toward Graph-Tokenizing Large Language Models with Reconstructive Graph...](/papers/2603.01385/) | published later (2026-03) |
| [2502.08092](/papers/2502.08092/) | CiteSeer | GPF | 0.7767 | 0.4328 | 712 | [Instance-Aware Graph Prompt Learning](/papers/2411.17676/) | already known (2024-11) |
| [2511.05592](/papers/2511.05592/) | PubMed | GPF | 0.9330 | 0.4758 | 711 | [Cross-Paradigm Graph Backdoor Attacks with Promptable Subgraph Triggers](/papers/2510.22555/) | already known (2025-10) |
| [2305.15747](/papers/2305.15747/) | CiteSeer | GCN | 0.8800 | 0.5830 | 709 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2511.05592](/papers/2511.05592/) | PubMed | GAT | 0.9233 | 0.4051 | 708 | [arXiv:2402.08170](/papers/2402.08170/) | already known (2024-02) |
| [2402.11235](/papers/2402.11235/) | PubMed | Sbert | 0.9058 | 0.3479 | 706 | [Large Language Models as Topological Structure Enhancers for...](/papers/2311.14324/) | already known (2023-11) |
| [1905.10990](/papers/1905.10990/) | Cora | GCN | 0.9004 | 0.7180 | 706 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2602.02268](/papers/2602.02268/) | Cora | GCN | 0.9004 | 0.7180 | 706 | [arXiv:2401.09125](/papers/2401.09125/) | already known (2024-01) |
| [2601.15124](/papers/2601.15124/) | Cora | GraphCL | 0.8653 | 0.5390 | 705 | [Toward Graph-Tokenizing Large Language Models with Reconstructive Graph...](/papers/2603.01385/) | published later (2026-03) |
| [2510.17185](/papers/2510.17185/) | CiteSeer | APPNP | 0.7933 | 0.5240 | 705 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | already known (2024-03) |
| [2210.10946](/papers/2210.10946/) | Cora | GATv2 | 0.8766 | 0.6000 | 703 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2510.12140](/papers/2510.12140/) | CiteSeer | SGC | 0.7965 | 0.5372 | 703 | [Optimizing Polynomial Graph Filters: A Novel Adaptive Krylov...](/papers/2403.07954/) | already known (2024-03) |
| [2502.11836](/papers/2502.11836/) | Cora | DGI | 0.8476 | 0.1679 | 701 | [Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction](/papers/2202.09025/) | already known (2022-02) |
| [2402.11235](/papers/2402.11235/) | Cora | DGI | 0.8476 | 0.1997 | 701 | [Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction](/papers/2202.09025/) | already known (2022-02) |
| [2502.08092](/papers/2502.08092/) | PubMed | GAT | 0.9233 | 0.5002 | 700 | [arXiv:2402.08170](/papers/2402.08170/) | already known (2024-02) |
| [1911.07323](/papers/1911.07323/) | CiteSeer | GraphSAGE | 0.8269 | 0.5940 | 700 | [Probing GNN Explainers: A Rigorous Theoretical and Empirical...](/papers/2106.09078/) | published later (2021-06-16) |
| [2502.08092](/papers/2502.08092/) | PubMed | GCN | 0.9296 | 0.5218 | 696 | [arXiv:2402.08170](/papers/2402.08170/) | already known (2024-02) |
| [2502.08092](/papers/2502.08092/) | PubMed | GPF | 0.9330 | 0.5716 | 696 | [Cross-Paradigm Graph Backdoor Attacks with Promptable Subgraph Triggers](/papers/2510.22555/) | published later (2025-10) |
| [2511.05592](/papers/2511.05592/) | Cora | DGI | 0.8476 | 0.3077 | 692 | [Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction](/papers/2202.09025/) | already known (2022-02) |
| [2601.15124](/papers/2601.15124/) | Cora | DGI | 0.8476 | 0.3080 | 692 | [Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction](/papers/2202.09025/) | already known (2022-02) |
| [2502.11836](/papers/2502.11836/) | PubMed | LLaGA | 0.9000 | 0.0756 | 691 | [Adversarial Attacks and Defenses on Graph-aware Large Language...](/papers/2508.04894/) | published later (2025-08) |
| [2305.15747](/papers/2305.15747/) | Cora | GCN | 0.9004 | 0.7256 | 690 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2601.02662](/papers/2601.02662/) | PubMed | GCN | 0.9296 | 0.5714 | 689 | [arXiv:2402.08170](/papers/2402.08170/) | already known (2024-02) |
| [2201.02534](/papers/2201.02534/) | CiteSeer | GraphSAGE | 0.8269 | 0.6020 | 687 | [Probing GNN Explainers: A Rigorous Theoretical and Empirical...](/papers/2106.09078/) | already known (2021-06-16) |
| [2601.02662](/papers/2601.02662/) | PubMed | GAT | 0.9233 | 0.5760 | 686 | [arXiv:2402.08170](/papers/2402.08170/) | already known (2024-02) |
| [2004.13970](/papers/2004.13970/) | CiteSeer | ChebNet | 0.8094 | 0.5970 | 685 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | published later (2024-03) |
| [2106.04714](/papers/2106.04714/) | Cora | GCN | 0.9004 | 0.7280 | 685 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2602.02268](/papers/2602.02268/) | Cora | Graphormer | 0.8510 | 0.4323 | 682 | [arXiv:1710.10321](/papers/1710.10321/) | already known (2017-10) |
| [2502.11836](/papers/2502.11836/) | Cora | GraphMAE | 0.8440 | 0.1513 | 676 | [UGMAE: A Unified Framework for Graph Masked Autoencoders](/papers/2402.08023/) | already known (2024-02) |
| [2405.16800](/papers/2405.16800/) | Cora | GraphMAE | 0.8440 | 0.1940 | 676 | [UGMAE: A Unified Framework for Graph Masked Autoencoders](/papers/2402.08023/) | already known (2024-02) |
| [2510.22555](/papers/2510.22555/) | PubMed | GraphPrompt | 0.9000 | 0.4250 | 676 | [Adversarial Attacks and Defenses on Graph-aware Large Language...](/papers/2508.04894/) | already known (2025-08) |
| [2511.05592](/papers/2511.05592/) | PubMed | GraphPrompt | 0.9000 | 0.4619 | 675 | [Adversarial Attacks and Defenses on Graph-aware Large Language...](/papers/2508.04894/) | already known (2025-08) |
| [2102.05034](/papers/2102.05034/) | Cora | IDGL | 0.8863 | 0.7090 | 674 | [Bridging Large Language Models and Graph Structure Learning...](/papers/2410.12096/) | published later (2024-10) |
| [2406.19258](/papers/2406.19258/) | Cora | SpecFormer | 0.8819 | 0.6918 | 670 | [Polynomial Selection in Spectral Graph Neural Networks: An...](/papers/2404.15354/) | already known (2024-04) |
| [2602.02268](/papers/2602.02268/) | Cora | NodeFormer | 0.8856 | 0.7103 | 668 | [Bridging Large Language Models and Graph Structure Learning...](/papers/2410.12096/) | already known (2024-10) |
| [2510.17185](/papers/2510.17185/) | PubMed | GCN | 0.9296 | 0.6332 | 666 | [arXiv:2402.08170](/papers/2402.08170/) | already known (2024-02) |
| [2210.10946](/papers/2210.10946/) | CiteSeer | GATv2 | 0.7659 | 0.4700 | 666 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2602.02268](/papers/2602.02268/) | PubMed | NodeFormer | 0.9490 | 0.6953 | 666 | [arXiv:2402.08170](/papers/2402.08170/) | already known (2024-02) |
| [2411.17063](/papers/2411.17063/) | CiteSeer | Whole Dataset | 0.7770 | 0.5720 | 666 | [RobGC: Towards Robust Graph Condensation](/papers/2406.13200/) | already known (2024-06) |
| [2505.22362](/papers/2505.22362/) | Cora | FSGNN | 0.8781 | 0.6751 | 666 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2407.07457](/papers/2407.07457/) | PubMed | LLaGA | 0.9000 | 0.5246 | 663 | [Adversarial Attacks and Defenses on Graph-aware Large Language...](/papers/2508.04894/) | published later (2025-08) |
| [2402.11235](/papers/2402.11235/) | Cora | GraphMAE | 0.8440 | 0.3479 | 662 | [UGMAE: A Unified Framework for Graph Masked Autoencoders](/papers/2402.08023/) | already known (2024-02) |
| [1911.07323](/papers/1911.07323/) | PubMed | GraphSAGE | 0.9487 | 0.7010 | 660 | [arXiv:2402.08170](/papers/2402.08170/) | published later (2024-02) |
| [2601.02662](/papers/2601.02662/) | PubMed | GraphPrompt | 0.9000 | 0.5629 | 659 | [Adversarial Attacks and Defenses on Graph-aware Large Language...](/papers/2508.04894/) | already known (2025-08) |
| [2602.00064](/papers/2602.00064/) | CiteSeer | Geom-GCN | 0.7799 | 0.5917 | 657 | [Improving Graph Neural Networks with Simple Architecture Design](/papers/2105.07634/) | already known (2021-05) |
| [2510.17185](/papers/2510.17185/) | CiteSeer | EvenNet | 0.7851 | 0.5977 | 657 | [Optimizing Polynomial Graph Filters: A Novel Adaptive Krylov...](/papers/2403.07954/) | already known (2024-03) |
| [2102.06986](/papers/2102.06986/) | Cora | GraphSAGE | 0.8998 | 0.7450 | 656 | [SPGCL: Simple yet Powerful Graph Contrastive Learning via...](/papers/2602.00064/) | published later (2026-02) |
| [2108.01660](/papers/2108.01660/) | Cora | GraphSAGE | 0.8998 | 0.7450 | 656 | [SPGCL: Simple yet Powerful Graph Contrastive Learning via...](/papers/2602.00064/) | published later (2026-02) |
| [2409.08676](/papers/2409.08676/) | CiteSeer | MLP | 0.7618 | 0.4530 | 653 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | already known (2024-03) |
| [2004.13970](/papers/2004.13970/) | CiteSeer | GraphSAGE | 0.8269 | 0.6280 | 652 | [Probing GNN Explainers: A Rigorous Theoretical and Empirical...](/papers/2106.09078/) | published later (2021-06-16) |
| [1911.11430](/papers/1911.11430/) | CiteSeer | MLP | 0.7618 | 0.4650 | 648 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | published later (2024-03) |
| [2007.16002](/papers/2007.16002/) | CiteSeer | MLP | 0.7618 | 0.4650 | 648 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | published later (2024-03) |
| [2101.03464](/papers/2101.03464/) | CiteSeer | MLP | 0.7618 | 0.4650 | 648 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | published later (2024-03) |
| [2102.06986](/papers/2102.06986/) | CiteSeer | MLP | 0.7618 | 0.4650 | 648 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | published later (2024-03) |
| [2202.08480](/papers/2202.08480/) | CiteSeer | MLP | 0.7618 | 0.4650 | 648 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | published later (2024-03) |
| [2510.17185](/papers/2510.17185/) | PubMed | GAT | 0.9233 | 0.6659 | 648 | [arXiv:2402.08170](/papers/2402.08170/) | already known (2024-02) |
| [2201.02534](/papers/2201.02534/) | CiteSeer | GCN | 0.8800 | 0.6337 | 648 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2410.10320](/papers/2410.10320/) | CiteSeer | GAT | 0.8227 | 0.6312 | 645 | [Instance-Aware Graph Prompt Learning](/papers/2411.17676/) | published later (2024-11) |
| [2210.10946](/papers/2210.10946/) | PubMed | GAT | 0.9233 | 0.6900 | 644 | [arXiv:2402.08170](/papers/2402.08170/) | published later (2024-02) |
| [1911.07323](/papers/1911.07323/) | Cora | GraphSAGE | 0.8998 | 0.7520 | 644 | [SPGCL: Simple yet Powerful Graph Contrastive Learning via...](/papers/2602.00064/) | published later (2026-02) |
| [2409.08676](/papers/2409.08676/) | Cora | GCN | 0.9004 | 0.7530 | 644 | [arXiv:2401.09125](/papers/2401.09125/) | already known (2024-01) |
| [2507.13368](/papers/2507.13368/) | Cora | MVGRL | 0.8623 | 0.6126 | 643 | [Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction](/papers/2202.09025/) | already known (2022-02) |
| [2510.17185](/papers/2510.17185/) | PubMed | EvenNet | 0.9087 | 0.6591 | 642 | [Optimizing Polynomial Graph Filters: A Novel Adaptive Krylov...](/papers/2403.07954/) | already known (2024-03) |
| [2512.24062](/papers/2512.24062/) | CiteSeer | MLP | 0.7618 | 0.4931 | 640 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | already known (2024-03) |
| [2004.13970](/papers/2004.13970/) | CiteSeer | SGC | 0.7965 | 0.6140 | 639 | [Optimizing Polynomial Graph Filters: A Novel Adaptive Krylov...](/papers/2403.07954/) | published later (2024-03) |
| [2004.13970](/papers/2004.13970/) | CiteSeer | GAT | 0.8227 | 0.6370 | 636 | [Instance-Aware Graph Prompt Learning](/papers/2411.17676/) | published later (2024-11) |
| [2406.19258](/papers/2406.19258/) | Cora | NAGphormer | 0.8768 | 0.6934 | 636 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | already known (2024-03) |
| [2502.08092](/papers/2502.08092/) | PubMed | GraphPrompt | 0.9000 | 0.6311 | 635 | [Adversarial Attacks and Defenses on Graph-aware Large Language...](/papers/2508.04894/) | published later (2025-08) |
| [2305.15747](/papers/2305.15747/) | CiteSeer | GAT | 0.8227 | 0.6382 | 634 | [Instance-Aware Graph Prompt Learning](/papers/2411.17676/) | published later (2024-11) |
| [2205.13700](/papers/2205.13700/) | Cora | WRGAT | 0.8820 | 0.7170 | 634 | [MUSE: Multi-View Contrastive Learning for Heterophilic Graphs](/papers/2307.16026/) | published later (2023-07) |
| [2409.08676](/papers/2409.08676/) | CiteSeer | GCN | 0.8800 | 0.6400 | 633 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2207.11996](/papers/2207.11996/) | PubMed | GraphSAGE | 0.9487 | 0.7310 | 631 | [arXiv:2402.08170](/papers/2402.08170/) | published later (2024-02) |
| [2407.07457](/papers/2407.07457/) | Cora | LLaGA | 0.8900 | 0.7442 | 629 | [Adversarial Attacks and Defenses on Graph-aware Large Language...](/papers/2508.04894/) | published later (2025-08) |
| [2211.15081](/papers/2211.15081/) | CiteSeer | MLP | 0.7618 | 0.5370 | 628 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | published later (2024-03) |
| [2302.09755](/papers/2302.09755/) | CiteSeer | MLP | 0.7618 | 0.5370 | 628 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | published later (2024-03) |
| [1906.01210](/papers/1906.01210/) | Cora | MGAE | 0.8615 | 0.6343 | 627 | [MGAE: Masked Autoencoders for Self-Supervised Learning on Graphs](/papers/2201.02534/) | published later (2022-01) |
| [2409.08676](/papers/2409.08676/) | CiteSeer | GAT | 0.8227 | 0.6410 | 627 | [Instance-Aware Graph Prompt Learning](/papers/2411.17676/) | published later (2024-11) |
| [2409.08676](/papers/2409.08676/) | Cora | GAT | 0.8897 | 0.7440 | 626 | [Clustering as Reasoning: A $k$-Means Interpretation of Chain-of-Thought...](/papers/2605.24867/) | published later (2026-05-24) |
| [2602.02268](/papers/2602.02268/) | Cora | GAT | 0.8897 | 0.7460 | 625 | [Clustering as Reasoning: A $k$-Means Interpretation of Chain-of-Thought...](/papers/2605.24867/) | published later (2026-05-24) |
| [2602.02268](/papers/2602.02268/) | PubMed | GCN | 0.9296 | 0.7150 | 624 | [arXiv:2402.08170](/papers/2402.08170/) | already known (2024-02) |
| [2004.13970](/papers/2004.13970/) | CiteSeer | GCN | 0.8800 | 0.6470 | 623 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2106.04051](/papers/2106.04051/) | CiteSeer | MLP | 0.7618 | 0.5470 | 623 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | published later (2024-03) |
| [2502.11836](/papers/2502.11836/) | PubMed | Sbert | 0.9058 | 0.7057 | 623 | [Large Language Models as Topological Structure Enhancers for...](/papers/2311.14324/) | already known (2023-11) |
| [2502.11836](/papers/2502.11836/) | CiteSeer | DGI | 0.7451 | 0.1524 | 621 | [MGAE: Masked Autoencoders for Self-Supervised Learning on Graphs](/papers/2201.02534/) | already known (2022-01) |
| [2406.19258](/papers/2406.19258/) | Cora | SGFormer | 0.8624 | 0.6462 | 621 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2503.19382](/papers/2503.19382/) | Cora | GraphSAGE | 0.8998 | 0.7650 | 620 | [SPGCL: Simple yet Powerful Graph Contrastive Learning via...](/papers/2602.00064/) | published later (2026-02) |
| [2502.11836](/papers/2502.11836/) | PubMed | GraphGPS | 0.8894 | 0.4294 | 619 | [DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer...](/papers/2505.17660/) | published later (2025-05) |
| [2106.04714](/papers/2106.04714/) | CiteSeer | GCN | 0.8800 | 0.6490 | 619 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2305.15747](/papers/2305.15747/) | Cora | GAT | 0.8897 | 0.7482 | 619 | [Clustering as Reasoning: A $k$-Means Interpretation of Chain-of-Thought...](/papers/2605.24867/) | published later (2026-05-24) |
| [2402.11235](/papers/2402.11235/) | CiteSeer | DGI | 0.7451 | 0.2112 | 618 | [MGAE: Masked Autoencoders for Self-Supervised Learning on Graphs](/papers/2201.02534/) | already known (2022-01) |
| [2507.13368](/papers/2507.13368/) | Cora | DGI | 0.8476 | 0.5574 | 618 | [Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction](/papers/2202.09025/) | already known (2022-02) |
| [2505.17660](/papers/2505.17660/) | Cora | SGFormer | 0.8624 | 0.6532 | 617 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2209.07754](/papers/2209.07754/) | Cora | GraphSAGE | 0.8998 | 0.7675 | 617 | [SPGCL: Simple yet Powerful Graph Contrastive Learning via...](/papers/2602.00064/) | published later (2026-02) |
| [2409.08676](/papers/2409.08676/) | Cora | GIN | 0.8705 | 0.6890 | 616 | [Unleashing the Potential of Text-attributed Graphs: Automatic Relation...](/papers/2405.18581/) | already known (2024-05) |
| [2602.07256](/papers/2602.07256/) | Cora | GloGNN | 0.8833 | 0.7302 | 616 | [GPNet: Simplifying Graph Neural Networks via Multi-channel Geometric...](/papers/2209.15454/) | already known (2022-09) |
| [2210.08792](/papers/2210.08792/) | CiteSeer | MLP | 0.7618 | 0.5690 | 613 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | published later (2024-03) |
| [2307.16026](/papers/2307.16026/) | CiteSeer | MLP | 0.7618 | 0.5691 | 613 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | published later (2024-03) |
| [2410.10320](/papers/2410.10320/) | CiteSeer | GCN | 0.8800 | 0.6526 | 612 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2102.06986](/papers/2102.06986/) | Cora | MPNN | 0.9220 | 0.7800 | 612 | [Beyond Euclid: An Illustrated Guide to Modern Machine...](/papers/2407.09468/) | published later (2024-07) |
| [2506.08871](/papers/2506.08871/) | Cora | FAGCN | 0.8885 | 0.7515 | 611 | [Language is All a Graph Needs](/papers/2308.07134/) | already known (2023-08) |
| [2006.13009](/papers/2006.13009/) | Cora | GraphSAGE | 0.8998 | 0.7740 | 609 | [SPGCL: Simple yet Powerful Graph Contrastive Learning via...](/papers/2602.00064/) | published later (2026-02) |
| [2601.15124](/papers/2601.15124/) | CiteSeer | DGI | 0.7451 | 0.3140 | 606 | [MGAE: Masked Autoencoders for Self-Supervised Learning on Graphs](/papers/2201.02534/) | already known (2022-01) |
| [2510.17185](/papers/2510.17185/) | PubMed | APPNP | 0.8940 | 0.6194 | 606 | [Optimization-Induced Graph Implicit Nonlinear Diffusion](/papers/2206.14418/) | already known (2022-06-29) |
| [2602.00064](/papers/2602.00064/) | Cora | LDS | 0.8771 | 0.7162 | 606 | [Bridging Large Language Models and Graph Structure Learning...](/papers/2410.12096/) | already known (2024-10) |
| [2505.00983](/papers/2505.00983/) | CiteSeer | GCNII | 0.7768 | 0.6250 | 606 | [Graph as a Feature: A Graph-Aware Non-Neural Model...](/papers/2411.12330/) | already known (2024-11) |
| [2505.17660](/papers/2505.17660/) | Cora | NAGphormer | 0.8768 | 0.7151 | 603 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | already known (2024-03) |
| [2505.22362](/papers/2505.22362/) | Cora | GloGNN | 0.8833 | 0.7378 | 602 | [GPNet: Simplifying Graph Neural Networks via Multi-channel Geometric...](/papers/2209.15454/) | already known (2022-09) |
| [2208.10010](/papers/2208.10010/) | CiteSeer | MLP | 0.7618 | 0.5850 | 601 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | published later (2024-03) |
| [2602.07256](/papers/2602.07256/) | CiteSeer | ChebNet | 0.8094 | 0.6518 | 599 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | already known (2024-03) |
| [2004.13970](/papers/2004.13970/) | PubMed | GraphSAGE | 0.9487 | 0.7520 | 597 | [arXiv:2402.08170](/papers/2402.08170/) | published later (2024-02) |
| [2502.03251](/papers/2502.03251/) | PubMed | LLaGA | 0.9000 | 0.7121 | 597 | [Adversarial Attacks and Defenses on Graph-aware Large Language...](/papers/2508.04894/) | published later (2025-08) |
| [1811.05868](/papers/1811.05868/) | CiteSeer | MLP | 0.7618 | 0.5910 | 597 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | published later (2024-03) |
| [2410.05593](/papers/2410.05593/) | CiteSeer | MLP | 0.7618 | 0.5910 | 597 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | already known (2024-03) |
| [2411.17676](/papers/2411.17676/) | Cora | GCN | 0.9004 | 0.7806 | 597 | [arXiv:2401.09125](/papers/2401.09125/) | already known (2024-01) |
| [2206.04739](/papers/2206.04739/) | CiteSeer | GCN | 0.8800 | 0.6607 | 596 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2307.06631](/papers/2307.06631/) | CiteSeer | MLP | 0.7618 | 0.5960 | 594 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | published later (2024-03) |
| [2102.05034](/papers/2102.05034/) | Cora | GRCN | 0.8612 | 0.6740 | 592 | [Reliable Representations Make A Stronger Defender: Unsupervised Structure...](/papers/2207.00012/) | published later (2022-07) |
| [2410.10320](/papers/2410.10320/) | CiteSeer | Dir-GNN | 0.7771 | 0.6374 | 592 | [Beyond Fixed Depth: Adaptive Graph Neural Networks for...](/papers/2511.06608/) | published later (2025-11) |
| [2510.17185](/papers/2510.17185/) | PubMed | GPRGNN | 0.8950 | 0.6568 | 591 | [arXiv:2310.10064](/papers/2310.10064/) | already known (2023-10) |
| [2505.17660](/papers/2505.17660/) | Cora | GRAND | 0.8736 | 0.7137 | 590 | [Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective...](/papers/2402.15326/) | already known (2024-02) |
| [2312.09041](/papers/2312.09041/) | CiteSeer | GPR-GNN | 0.8013 | 0.6539 | 587 | [Optimizing Polynomial Graph Filters: A Novel Adaptive Krylov...](/papers/2403.07954/) | published later (2024-03) |
| [2312.09041](/papers/2312.09041/) | Cora | GPR-GNN | 0.8865 | 0.7605 | 587 | [Finding the Missing-half: Graph Complementary Learning for Homophily-prone...](/papers/2306.07608/) | already known (2023-06-13) |
| [2308.07134](/papers/2308.07134/) | Cora | GAT | 0.8897 | 0.7670 | 587 | [Clustering as Reasoning: A $k$-Means Interpretation of Chain-of-Thought...](/papers/2605.24867/) | published later (2026-05-24) |
| [2305.08048](/papers/2305.08048/) | CiteSeer | GCN | 0.8800 | 0.6674 | 586 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2602.02268](/papers/2602.02268/) | Cora | APPNP | 0.8904 | 0.7713 | 586 | [arXiv:2310.10064](/papers/2310.10064/) | already known (2023-10) |
| [2112.03968](/papers/2112.03968/) | Cora | ChebNet | 0.8969 | 0.7820 | 586 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | published later (2024-03) |
| [2403.09171](/papers/2403.09171/) | Cora | GCN_n + DropNode | 0.8460 | 0.5789 | 585 | [Graph Convolutional Neural Networks with Node Transition Probability-based...](/papers/2008.12578/) | already known (2020-08) |
| [2006.13009](/papers/2006.13009/) | CiteSeer | GraphSAGE | 0.8269 | 0.6700 | 579 | [Probing GNN Explainers: A Rigorous Theoretical and Empirical...](/papers/2106.09078/) | published later (2021-06-16) |
| [2505.00983](/papers/2505.00983/) | CiteSeer | Dir-GNN | 0.7771 | 0.6450 | 579 | [Beyond Fixed Depth: Adaptive Graph Neural Networks for...](/papers/2511.06608/) | published later (2025-11) |
| [2308.07134](/papers/2308.07134/) | Cora | MixHop | 0.8836 | 0.7565 | 579 | [Adapting to Heterophilic Graph Data with Structure-Guided Neighbor...](/papers/2506.08871/) | published later (2025-06) |
| [2302.12357](/papers/2302.12357/) | CiteSeer | GraphSAGE | 0.8269 | 0.6718 | 576 | [Probing GNN Explainers: A Rigorous Theoretical and Empirical...](/papers/2106.09078/) | already known (2021-06-16) |
| [2310.00800](/papers/2310.00800/) | Cora | GRACE | 0.8911 | 0.7781 | 576 | [Toward Graph-Tokenizing Large Language Models with Reconstructive Graph...](/papers/2603.01385/) | published later (2026-03) |
| [2102.06986](/papers/2102.06986/) | CiteSeer | GraphSAGE | 0.8269 | 0.6720 | 575 | [Probing GNN Explainers: A Rigorous Theoretical and Empirical...](/papers/2106.09078/) | published later (2021-06-16) |
| [2407.07457](/papers/2407.07457/) | PubMed | GraphSAGE | 0.9487 | 0.7679 | 574 | [arXiv:2402.08170](/papers/2402.08170/) | already known (2024-02) |
| [2410.12096](/papers/2410.12096/) | PubMed | GraphSAGE | 0.9487 | 0.7679 | 574 | [arXiv:2402.08170](/papers/2402.08170/) | already known (2024-02) |
| [1312.6203](/papers/1312.6203/) | PubMed | GraphSAGE | 0.9487 | 0.7680 | 572 | [arXiv:2402.08170](/papers/2402.08170/) | published later (2024-02) |
| [2102.06986](/papers/2102.06986/) | PubMed | GraphSAGE | 0.9487 | 0.7680 | 572 | [arXiv:2402.08170](/papers/2402.08170/) | published later (2024-02) |
| [2108.01660](/papers/2108.01660/) | PubMed | GraphSAGE | 0.9487 | 0.7680 | 572 | [arXiv:2402.08170](/papers/2402.08170/) | published later (2024-02) |
| [2211.15081](/papers/2211.15081/) | CiteSeer | GCN | 0.8800 | 0.6750 | 571 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2302.09755](/papers/2302.09755/) | CiteSeer | GCN | 0.8800 | 0.6750 | 571 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2103.07295](/papers/2103.07295/) | CiteSeer | MLP | 0.7618 | 0.6100 | 570 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | published later (2024-03) |
| [2010.12811](/papers/2010.12811/) | Cora | GAT | 0.8897 | 0.7780 | 570 | [Clustering as Reasoning: A $k$-Means Interpretation of Chain-of-Thought...](/papers/2605.24867/) | published later (2026-05-24) |
| [2111.12952](/papers/2111.12952/) | Cora | GraphSAGE | 0.8998 | 0.7890 | 570 | [SPGCL: Simple yet Powerful Graph Contrastive Learning via...](/papers/2602.00064/) | published later (2026-02) |
| [2505.00983](/papers/2505.00983/) | CiteSeer | GATv2 | 0.7659 | 0.6280 | 569 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2510.17185](/papers/2510.17185/) | PubMed | GRAND | 0.8902 | 0.6535 | 568 | [Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective...](/papers/2402.15326/) | already known (2024-02) |
| [2106.04714](/papers/2106.04714/) | Cora | GIN | 0.8705 | 0.7230 | 568 | [Unleashing the Potential of Text-attributed Graphs: Automatic Relation...](/papers/2405.18581/) | published later (2024-05) |
| [2211.15081](/papers/2211.15081/) | Cora | GCN | 0.9004 | 0.7910 | 568 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2302.14806](/papers/2302.14806/) | CiteSeer | MLP | 0.7618 | 0.6120 | 567 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | published later (2024-03) |
| [2602.02268](/papers/2602.02268/) | PubMed | GAT | 0.9233 | 0.7590 | 565 | [arXiv:2402.08170](/papers/2402.08170/) | already known (2024-02) |
| [2206.04739](/papers/2206.04739/) | CiteSeer | GAT | 0.8227 | 0.6762 | 565 | [Instance-Aware Graph Prompt Learning](/papers/2411.17676/) | published later (2024-11) |
| [2211.15081](/papers/2211.15081/) | CiteSeer | GAT | 0.8227 | 0.6800 | 559 | [Instance-Aware Graph Prompt Learning](/papers/2411.17676/) | published later (2024-11) |
| [2206.04739](/papers/2206.04739/) | CiteSeer | MLP | 0.7618 | 0.6206 | 559 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | published later (2024-03) |
| [2108.00955](/papers/2108.00955/) | Cora | GraphSAGE | 0.8998 | 0.7920 | 559 | [SPGCL: Simple yet Powerful Graph Contrastive Learning via...](/papers/2602.00064/) | published later (2026-02) |
| [2207.11996](/papers/2207.11996/) | Cora | GraphSAGE | 0.8998 | 0.7920 | 559 | [SPGCL: Simple yet Powerful Graph Contrastive Learning via...](/papers/2602.00064/) | published later (2026-02) |
| [2311.05767](/papers/2311.05767/) | Cora | GraphSAGE | 0.8998 | 0.7920 | 559 | [SPGCL: Simple yet Powerful Graph Contrastive Learning via...](/papers/2602.00064/) | published later (2026-02) |
| [1906.02174](/papers/1906.02174/) | Cora | GCN | 0.9004 | 0.7930 | 559 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2205.13700](/papers/2205.13700/) | CiteSeer | WRGAT | 0.7681 | 0.6410 | 558 | [MUSE: Multi-View Contrastive Learning for Heterophilic Graphs](/papers/2307.16026/) | published later (2023-07) |
| [2210.10946](/papers/2210.10946/) | PubMed | GATv2 | 0.8877 | 0.6900 | 554 | [Beyond Fixed Depth: Adaptive Graph Neural Networks for...](/papers/2511.06608/) | published later (2025-11) |
| [2407.07457](/papers/2407.07457/) | CiteSeer | GraphSAGE | 0.8269 | 0.6823 | 554 | [Probing GNN Explainers: A Rigorous Theoretical and Empirical...](/papers/2106.09078/) | already known (2021-06-16) |
| [1906.02174](/papers/1906.02174/) | PubMed | GCN | 0.9296 | 0.7660 | 553 | [arXiv:2402.08170](/papers/2402.08170/) | published later (2024-02) |
| [2004.13970](/papers/2004.13970/) | Cora | ChebNet | 0.8969 | 0.7920 | 553 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | published later (2024-03) |
| [2402.11235](/papers/2402.11235/) | CiteSeer | GraphCL | 0.7351 | 0.2059 | 551 | [Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction](/papers/2202.09025/) | already known (2022-02) |
| [2502.20885](/papers/2502.20885/) | Cora | SubG-Con | 0.8350 | 0.4432 | 551 | [Towards Graph Self-Supervised Learning with Contrastive Adjusted Zooming](/papers/2111.10698/) | already known (2021-11) |
| [2004.13970](/papers/2004.13970/) | PubMed | GAT | 0.9233 | 0.7650 | 551 | [arXiv:2402.08170](/papers/2402.08170/) | published later (2024-02) |
| [2205.13700](/papers/2205.13700/) | Cora | GCN | 0.9004 | 0.7970 | 551 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2004.13970](/papers/2004.13970/) | PubMed | GCN | 0.9296 | 0.7680 | 550 | [arXiv:2402.08170](/papers/2402.08170/) | published later (2024-02) |
| [2207.11996](/papers/2207.11996/) | PubMed | GCN | 0.9296 | 0.7680 | 550 | [arXiv:2402.08170](/papers/2402.08170/) | published later (2024-02) |
| [2108.00955](/papers/2108.00955/) | PubMed | GraphSAGE | 0.9487 | 0.7740 | 549 | [arXiv:2402.08170](/papers/2402.08170/) | published later (2024-02) |
| [2311.05767](/papers/2311.05767/) | PubMed | GraphSAGE | 0.9487 | 0.7740 | 549 | [arXiv:2402.08170](/papers/2402.08170/) | published later (2024-02) |
| [2503.19382](/papers/2503.19382/) | PubMed | GraphSAGE | 0.9487 | 0.7740 | 549 | [arXiv:2402.08170](/papers/2402.08170/) | already known (2024-02) |
| [2602.07256](/papers/2602.07256/) | Cora | H2GCN | 0.8829 | 0.7689 | 549 | [Adapting to Heterophilic Graph Data with Structure-Guided Neighbor...](/papers/2506.08871/) | already known (2025-06) |
| [2502.11836](/papers/2502.11836/) | CiteSeer | GraphMAE | 0.7341 | 0.0811 | 548 | [HAT-GAE: Self-Supervised Graph Auto-encoders with Hierarchical Adaptive Masking...](/papers/2301.12063/) | already known (2023-01) |
| [2507.13368](/papers/2507.13368/) | CiteSeer | DGI | 0.7451 | 0.5360 | 548 | [MGAE: Masked Autoencoders for Self-Supervised Learning on Graphs](/papers/2201.02534/) | already known (2022-01) |
| [2602.02268](/papers/2602.02268/) | PubMed | SpecFormer | 0.8874 | 0.6973 | 548 | [Polynomial Selection in Spectral Graph Neural Networks: An...](/papers/2404.15354/) | already known (2024-04) |
| [1906.01210](/papers/1906.01210/) | PubMed | MGAE | 0.8691 | 0.4388 | 547 | [MGAE: Masked Autoencoders for Self-Supervised Learning on Graphs](/papers/2201.02534/) | published later (2022-01) |
| [2502.11836](/papers/2502.11836/) | PubMed | DGI | 0.8595 | 0.2510 | 545 | [MGAE: Masked Autoencoders for Self-Supervised Learning on Graphs](/papers/2201.02534/) | already known (2022-01) |
| [2407.07457](/papers/2407.07457/) | Cora | GraphSAGE | 0.8998 | 0.7988 | 545 | [SPGCL: Simple yet Powerful Graph Contrastive Learning via...](/papers/2602.00064/) | published later (2026-02) |
| [2511.05592](/papers/2511.05592/) | Cora | DSSL | 0.8306 | 0.2976 | 544 | [MUSE: Multi-View Contrastive Learning for Heterophilic Graphs](/papers/2307.16026/) | already known (2023-07) |
| [2402.09600](/papers/2402.09600/) | PubMed | GCN | 0.9296 | 0.7700 | 544 | [arXiv:2402.08170](/papers/2402.08170/) | already known (2024-02) |
| [1905.09718](/papers/1905.09718/) | Cora | DeepWalk | 0.8297 | 0.1606 | 543 | [Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction](/papers/2202.09025/) | published later (2022-02) |
| [2405.16800](/papers/2405.16800/) | PubMed | GRACE | 0.8590 | 0.3350 | 543 | [arXiv:2306.13854](/papers/2306.13854/) | already known (2023-06) |
| [2407.07457](/papers/2407.07457/) | PubMed | GAT | 0.9233 | 0.7693 | 543 | [arXiv:2402.08170](/papers/2402.08170/) | already known (2024-02) |
| [2410.12096](/papers/2410.12096/) | PubMed | GAT | 0.9233 | 0.7693 | 543 | [arXiv:2402.08170](/papers/2402.08170/) | already known (2024-02) |
| [2510.12140](/papers/2510.12140/) | Cora | DeepWalk | 0.8297 | 0.2362 | 542 | [Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction](/papers/2202.09025/) | already known (2022-02) |
| [2010.12811](/papers/2010.12811/) | Cora | GCN | 0.9004 | 0.8000 | 541 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2407.11025](/papers/2407.11025/) | Cora | APPNP | 0.8904 | 0.7910 | 540 | [arXiv:2310.10064](/papers/2310.10064/) | already known (2023-10) |
| [2601.08230](/papers/2601.08230/) | Cora | GraphSAGE | 0.8998 | 0.8000 | 539 | [SPGCL: Simple yet Powerful Graph Contrastive Learning via...](/papers/2602.00064/) | published later (2026-02) |
| [2305.08048](/papers/2305.08048/) | Cora | APPNP | 0.8904 | 0.7914 | 539 | [arXiv:2310.10064](/papers/2310.10064/) | published later (2023-10) |
| [2602.00064](/papers/2602.00064/) | Cora | GCN | 0.9004 | 0.8013 | 537 | [arXiv:2401.09125](/papers/2401.09125/) | already known (2024-01) |
| [2605.14809](/papers/2605.14809/) | Cora | GPR | 0.8310 | 0.3899 | 536 | [GraphGLOW: Open-World Graph Structure Learning for Cross-Graph Topology...](/papers/2306.11264/) | already known (2023-06) |
| [2511.05592](/papers/2511.05592/) | PubMed | DGI | 0.8595 | 0.3997 | 535 | [MGAE: Masked Autoencoders for Self-Supervised Learning on Graphs](/papers/2201.02534/) | already known (2022-01) |
| [2106.04714](/papers/2106.04714/) | PubMed | GCN | 0.9296 | 0.7730 | 535 | [arXiv:2402.08170](/papers/2402.08170/) | published later (2024-02) |
| [2407.07457](/papers/2407.07457/) | CiteSeer | GAT | 0.8227 | 0.6878 | 533 | [Instance-Aware Graph Prompt Learning](/papers/2411.17676/) | published later (2024-11) |
| [2402.11235](/papers/2402.11235/) | PubMed | DGI | 0.8595 | 0.4389 | 531 | [MGAE: Masked Autoencoders for Self-Supervised Learning on Graphs](/papers/2201.02534/) | already known (2022-01) |
| [2602.02268](/papers/2602.02268/) | Cora | Exphormer | 0.8410 | 0.6120 | 531 | [Diffusion on Graph: Augmentation of Graph Structure for...](/papers/2503.12563/) | already known (2025-03) |
| [2602.02268](/papers/2602.02268/) | PubMed | SGFormer | 0.8931 | 0.7347 | 531 | [DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer...](/papers/2505.17660/) | already known (2025-05) |
| [2207.12931](/papers/2207.12931/) | PubMed | SGC | 0.8800 | 0.6554 | 530 | [All Against Some: Efficient Integration of Large Language...](/papers/2407.14996/) | published later (2024-07) |
| [2302.09755](/papers/2302.09755/) | CiteSeer | GCNII | 0.7768 | 0.6700 | 530 | [Graph as a Feature: A Graph-Aware Non-Neural Model...](/papers/2411.12330/) | published later (2024-11) |
| [2004.13970](/papers/2004.13970/) | Cora | GraphSAGE | 0.8998 | 0.8020 | 530 | [SPGCL: Simple yet Powerful Graph Contrastive Learning via...](/papers/2602.00064/) | published later (2026-02) |
| [2602.00064](/papers/2602.00064/) | CiteSeer | GAT | 0.8227 | 0.6890 | 529 | [Instance-Aware Graph Prompt Learning](/papers/2411.17676/) | already known (2024-11) |
| [2411.12330](/papers/2411.12330/) | PubMed | SGC | 0.8800 | 0.6635 | 528 | [All Against Some: Efficient Integration of Large Language...](/papers/2407.14996/) | already known (2024-07) |
| [2411.02279](/papers/2411.02279/) | CiteSeer | GPRGNN | 0.8033 | 0.6857 | 527 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | already known (2024-03) |
| [1812.04202](/papers/1812.04202/) | PubMed | ChebNet | 0.8951 | 0.7440 | 526 | [arXiv:2310.10064](/papers/2310.10064/) | published later (2023-10) |
| [1907.04786](/papers/1907.04786/) | PubMed | ChebNet | 0.8951 | 0.7440 | 526 | [arXiv:2310.10064](/papers/2310.10064/) | published later (2023-10) |
| [2007.16002](/papers/2007.16002/) | PubMed | ChebNet | 0.8951 | 0.7440 | 526 | [arXiv:2310.10064](/papers/2310.10064/) | published later (2023-10) |
| [2101.00797](/papers/2101.00797/) | PubMed | ChebNet | 0.8951 | 0.7440 | 526 | [arXiv:2310.10064](/papers/2310.10064/) | published later (2023-10) |
| [2108.01660](/papers/2108.01660/) | PubMed | ChebNet | 0.8951 | 0.7440 | 526 | [arXiv:2310.10064](/papers/2310.10064/) | published later (2023-10) |
| [2112.03968](/papers/2112.03968/) | Cora | APPNP | 0.8904 | 0.7950 | 526 | [arXiv:2310.10064](/papers/2310.10064/) | published later (2023-10) |
| [1312.6203](/papers/1312.6203/) | PubMed | GAT | 0.9233 | 0.7740 | 525 | [arXiv:2402.08170](/papers/2402.08170/) | published later (2024-02) |
| [2002.10306](/papers/2002.10306/) | PubMed | GAT | 0.9233 | 0.7746 | 525 | [arXiv:2402.08170](/papers/2402.08170/) | published later (2024-02) |
| [2211.15081](/papers/2211.15081/) | Cora | ACMGCN | 0.8975 | 0.8020 | 525 | [Language is All a Graph Needs](/papers/2308.07134/) | published later (2023-08) |
| [2402.11235](/papers/2402.11235/) | CiteSeer | GraphMAE | 0.7341 | 0.3462 | 524 | [HAT-GAE: Self-Supervised Graph Auto-encoders with Hierarchical Adaptive Masking...](/papers/2301.12063/) | already known (2023-01) |
| [1902.08226](/papers/1902.08226/) | CiteSeer | GCN | 0.8800 | 0.6930 | 522 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2004.13970](/papers/2004.13970/) | PubMed | ChebNet | 0.8951 | 0.7460 | 522 | [arXiv:2310.10064](/papers/2310.10064/) | published later (2023-10) |
| [2411.02279](/papers/2411.02279/) | PubMed | NodeFormer | 0.9490 | 0.7821 | 521 | [arXiv:2402.08170](/papers/2402.08170/) | already known (2024-02) |
| [2412.17856](/papers/2412.17856/) | PubMed | NodeFormer | 0.9490 | 0.7821 | 521 | [arXiv:2402.08170](/papers/2402.08170/) | already known (2024-02) |
| [2112.03968](/papers/2112.03968/) | Cora | GraphSAGE | 0.8998 | 0.8050 | 521 | [SPGCL: Simple yet Powerful Graph Contrastive Learning via...](/papers/2602.00064/) | published later (2026-02) |
| [2202.13060](/papers/2202.13060/) | PubMed | GraphSAGE | 0.9487 | 0.7820 | 520 | [arXiv:2402.08170](/papers/2402.08170/) | published later (2024-02) |
| [2302.12357](/papers/2302.12357/) | Cora | GraphSAGE | 0.8998 | 0.8060 | 520 | [SPGCL: Simple yet Powerful Graph Contrastive Learning via...](/papers/2602.00064/) | published later (2026-02) |
| [2402.11235](/papers/2402.11235/) | CiteSeer | Sbert | 0.7317 | 0.2376 | 519 | [Large Language Models as Topological Structure Enhancers for...](/papers/2311.14324/) | already known (2023-11) |
| [2411.17676](/papers/2411.17676/) | Cora | GAT | 0.8897 | 0.7971 | 519 | [Clustering as Reasoning: A $k$-Means Interpretation of Chain-of-Thought...](/papers/2605.24867/) | published later (2026-05-24) |
| [2601.15124](/papers/2601.15124/) | CiteSeer | GraphCL | 0.7351 | 0.4060 | 518 | [Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction](/papers/2202.09025/) | already known (2022-02) |
| [2209.07754](/papers/2209.07754/) | Cora | GAT | 0.8897 | 0.7974 | 518 | [Clustering as Reasoning: A $k$-Means Interpretation of Chain-of-Thought...](/papers/2605.24867/) | published later (2026-05-24) |
| [2502.20885](/papers/2502.20885/) | CiteSeer | SubG-Con | 0.7320 | 0.3007 | 517 | [Towards Graph Self-Supervised Learning with Contrastive Adjusted Zooming](/papers/2111.10698/) | already known (2021-11) |
| [1312.6203](/papers/1312.6203/) | PubMed | GCN | 0.9296 | 0.7770 | 517 | [arXiv:2402.08170](/papers/2402.08170/) | published later (2024-02) |
| [2202.13060](/papers/2202.13060/) | PubMed | GCN | 0.9296 | 0.7770 | 517 | [arXiv:2402.08170](/papers/2402.08170/) | published later (2024-02) |
| [1911.11430](/papers/1911.11430/) | PubMed | ChebNet | 0.8951 | 0.7500 | 517 | [arXiv:2310.10064](/papers/2310.10064/) | published later (2023-10) |
| [2302.09755](/papers/2302.09755/) | CiteSeer | GAT | 0.8227 | 0.6930 | 517 | [Instance-Aware Graph Prompt Learning](/papers/2411.17676/) | published later (2024-11) |
| [2502.20885](/papers/2502.20885/) | CiteSeer | BGRL | 0.7340 | 0.3802 | 515 | [arXiv:2306.13854](/papers/2306.13854/) | already known (2023-06) |
| [2205.13700](/papers/2205.13700/) | CiteSeer | GCN | 0.8800 | 0.6950 | 515 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [1908.05081](/papers/1908.05081/) | PubMed | GAT | 0.9233 | 0.7776 | 515 | [arXiv:2402.08170](/papers/2402.08170/) | published later (2024-02) |
| [1312.6203](/papers/1312.6203/) | Cora | ChebNet | 0.8969 | 0.8050 | 515 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | published later (2024-03) |
| [2111.10698](/papers/2111.10698/) | Cora | GRACE | 0.8911 | 0.8000 | 515 | [Toward Graph-Tokenizing Large Language Models with Reconstructive Graph...](/papers/2603.01385/) | published later (2026-03) |
| [2202.08480](/papers/2202.08480/) | Cora | GRACE | 0.8911 | 0.8000 | 515 | [Toward Graph-Tokenizing Large Language Models with Reconstructive Graph...](/papers/2603.01385/) | published later (2026-03) |
| [2210.08792](/papers/2210.08792/) | Cora | GRACE | 0.8911 | 0.8000 | 515 | [Toward Graph-Tokenizing Large Language Models with Reconstructive Graph...](/papers/2603.01385/) | published later (2026-03) |
| [1811.05868](/papers/1811.05868/) | PubMed | GCN | 0.9296 | 0.7780 | 514 | [arXiv:2402.08170](/papers/2402.08170/) | published later (2024-02) |
| [2211.15081](/papers/2211.15081/) | PubMed | GCN | 0.9296 | 0.7780 | 514 | [arXiv:2402.08170](/papers/2402.08170/) | published later (2024-02) |
| [2110.09443](/papers/2110.09443/) | CiteSeer | CPGNN | 0.7691 | 0.6690 | 514 | [Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective...](/papers/2402.15326/) | published later (2024-02) |
| [2502.08092](/papers/2502.08092/) | CiteSeer | GraphCL | 0.7351 | 0.4312 | 513 | [Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction](/papers/2202.09025/) | already known (2022-02) |
| [2108.12055](/papers/2108.12055/) | Cora | GCN | 0.9004 | 0.8080 | 513 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2211.15081](/papers/2211.15081/) | CiteSeer | H2GCN | 0.7711 | 0.6740 | 512 | [Optimization-Induced Graph Implicit Nonlinear Diffusion](/papers/2206.14418/) | already known (2022-06-29) |
| [2307.16026](/papers/2307.16026/) | Cora | GRACE | 0.8911 | 0.8008 | 512 | [Toward Graph-Tokenizing Large Language Models with Reconstructive Graph...](/papers/2603.01385/) | published later (2026-03) |
| [1906.02174](/papers/1906.02174/) | CiteSeer | GCN | 0.8800 | 0.6960 | 511 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2412.17856](/papers/2412.17856/) | PubMed | GAT | 0.9233 | 0.7785 | 511 | [arXiv:2402.08170](/papers/2402.08170/) | already known (2024-02) |
| [2209.07754](/papers/2209.07754/) | PubMed | GIN | 0.8977 | 0.7671 | 511 | [Unleashing the Potential of Text-attributed Graphs: Automatic Relation...](/papers/2405.18581/) | published later (2024-05) |
| [2102.05034](/papers/2102.05034/) | Cora | DGCNN | 0.8350 | 0.5650 | 509 | [Deep Learning on Graphs: A Survey](/papers/1812.04202/) | already known (2018-12) |
| [2601.08230](/papers/2601.08230/) | CiteSeer | FAGCN | 0.7682 | 0.6700 | 509 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2302.09755](/papers/2302.09755/) | PubMed | GIN | 0.8977 | 0.7680 | 508 | [Unleashing the Potential of Text-attributed Graphs: Automatic Relation...](/papers/2405.18581/) | published later (2024-05) |
| [2307.06631](/papers/2307.06631/) | PubMed | MLP | 0.8747 | 0.6760 | 505 | [Finding the Missing-half: Graph Complementary Learning for Homophily-prone...](/papers/2306.07608/) | already known (2023-06-13) |
| [2101.00797](/papers/2101.00797/) | PubMed | GraphSAGE | 0.9487 | 0.7850 | 505 | [arXiv:2402.08170](/papers/2402.08170/) | published later (2024-02) |
| [2205.13700](/papers/2205.13700/) | PubMed | WRGAT | 0.8852 | 0.7330 | 505 | [MUSE: Multi-View Contrastive Learning for Heterophilic Graphs](/papers/2307.16026/) | published later (2023-07) |
| [2305.15747](/papers/2305.15747/) | Cora | GIN | 0.8705 | 0.7586 | 505 | [Unleashing the Potential of Text-attributed Graphs: Automatic Relation...](/papers/2405.18581/) | published later (2024-05) |
| [2211.15081](/papers/2211.15081/) | Cora | GAT | 0.8897 | 0.8010 | 505 | [Clustering as Reasoning: A $k$-Means Interpretation of Chain-of-Thought...](/papers/2605.24867/) | published later (2026-05-24) |
| [2411.02279](/papers/2411.02279/) | Cora | GPRGNN | 0.8929 | 0.8055 | 505 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | already known (2024-03) |
| [2112.03968](/papers/2112.03968/) | Cora | GCN | 0.9004 | 0.8100 | 504 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2601.08230](/papers/2601.08230/) | Cora | GCN | 0.9004 | 0.8100 | 504 | [arXiv:2401.09125](/papers/2401.09125/) | already known (2024-01) |
| [2211.15081](/papers/2211.15081/) | Cora | GCNII | 0.8967 | 0.8080 | 504 | [Graph as a Feature: A Graph-Aware Non-Neural Model...](/papers/2411.12330/) | published later (2024-11) |
| [2505.00983](/papers/2505.00983/) | Cora | GCNII | 0.8967 | 0.8080 | 504 | [Graph as a Feature: A Graph-Aware Non-Neural Model...](/papers/2411.12330/) | already known (2024-11) |
| [2010.15421](/papers/2010.15421/) | PubMed | GAT | 0.9233 | 0.7800 | 503 | [arXiv:2402.08170](/papers/2402.08170/) | published later (2024-02) |
| [2211.15081](/papers/2211.15081/) | PubMed | GAT | 0.9233 | 0.7800 | 503 | [arXiv:2402.08170](/papers/2402.08170/) | published later (2024-02) |
| [2209.07754](/papers/2209.07754/) | CiteSeer | GraphSAGE | 0.8269 | 0.6978 | 503 | [Probing GNN Explainers: A Rigorous Theoretical and Empirical...](/papers/2106.09078/) | already known (2021-06-16) |
| [2202.08057](/papers/2202.08057/) | CiteSeer | MLP | 0.7618 | 0.6555 | 503 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | published later (2024-03) |
| [2208.10010](/papers/2208.10010/) | PubMed | MLP | 0.8747 | 0.6839 | 502 | [Finding the Missing-half: Graph Complementary Learning for Homophily-prone...](/papers/2306.07608/) | published later (2023-06-13) |
| [1902.07153](/papers/1902.07153/) | PubMed | GIN | 0.8977 | 0.7700 | 502 | [Unleashing the Potential of Text-attributed Graphs: Automatic Relation...](/papers/2405.18581/) | published later (2024-05) |
| [2101.00797](/papers/2101.00797/) | PubMed | GIN | 0.8977 | 0.7700 | 502 | [Unleashing the Potential of Text-attributed Graphs: Automatic Relation...](/papers/2405.18581/) | published later (2024-05) |
| [1312.6203](/papers/1312.6203/) | Cora | GraphSAGE | 0.8998 | 0.8100 | 502 | [SPGCL: Simple yet Powerful Graph Contrastive Learning via...](/papers/2602.00064/) | published later (2026-02) |
| [1710.10321](/papers/1710.10321/) | Cora | GraphSAGE | 0.8998 | 0.8100 | 502 | [SPGCL: Simple yet Powerful Graph Contrastive Learning via...](/papers/2602.00064/) | published later (2026-02) |
| [2202.13060](/papers/2202.13060/) | Cora | GraphSAGE | 0.8998 | 0.8100 | 502 | [SPGCL: Simple yet Powerful Graph Contrastive Learning via...](/papers/2602.00064/) | published later (2026-02) |
| [2407.14996](/papers/2407.14996/) | Cora | GCN | 0.9004 | 0.8110 | 502 | [arXiv:2401.09125](/papers/2401.09125/) | already known (2024-01) |
| [2501.11817](/papers/2501.11817/) | Cora | GCNII | 0.8967 | 0.8084 | 502 | [Graph as a Feature: A Graph-Aware Non-Neural Model...](/papers/2411.12330/) | already known (2024-11) |
| [2407.07457](/papers/2407.07457/) | CiteSeer | GCN | 0.8800 | 0.6984 | 501 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2211.15081](/papers/2211.15081/) | PubMed | GIN | 0.8977 | 0.7710 | 501 | [Unleashing the Potential of Text-attributed Graphs: Automatic Relation...](/papers/2405.18581/) | published later (2024-05) |
| [2003.02228](/papers/2003.02228/) | PubMed | GIN | 0.8977 | 0.7719 | 501 | [Unleashing the Potential of Text-attributed Graphs: Automatic Relation...](/papers/2405.18581/) | published later (2024-05) |
| [1911.11430](/papers/1911.11430/) | CiteSeer | ChebNet | 0.8094 | 0.6950 | 501 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | published later (2024-03) |
| [2211.15081](/papers/2211.15081/) | CiteSeer | APPNP | 0.7933 | 0.6890 | 501 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | published later (2024-03) |
| [2512.24062](/papers/2512.24062/) | PubMed | MLP | 0.8747 | 0.6914 | 500 | [Finding the Missing-half: Graph Complementary Learning for Homophily-prone...](/papers/2306.07608/) | already known (2023-06-13) |
| [2102.03147](/papers/2102.03147/) | Cora | GraphSAGE | 0.8998 | 0.8112 | 500 | [SPGCL: Simple yet Powerful Graph Contrastive Learning via...](/papers/2602.00064/) | published later (2026-02) |
| [2201.02534](/papers/2201.02534/) | PubMed | GCN | 0.9296 | 0.7823 | 498 | [arXiv:2402.08170](/papers/2402.08170/) | published later (2024-02) |
| [2003.02228](/papers/2003.02228/) | PubMed | GCN | 0.9296 | 0.7829 | 498 | [arXiv:2402.08170](/papers/2402.08170/) | published later (2024-02) |
| [2407.07457](/papers/2407.07457/) | Cora | GAT | 0.8897 | 0.8031 | 498 | [Clustering as Reasoning: A $k$-Means Interpretation of Chain-of-Thought...](/papers/2605.24867/) | published later (2026-05-24) |
| [2502.20885](/papers/2502.20885/) | Cora | BGRL | 0.8380 | 0.6295 | 497 | [arXiv:2505.19024](/papers/2505.19024/) | published later (2025-05) |
| [2211.15081](/papers/2211.15081/) | PubMed | MLP | 0.8747 | 0.6970 | 497 | [Finding the Missing-half: Graph Complementary Learning for Homophily-prone...](/papers/2306.07608/) | published later (2023-06-13) |
| [2302.09755](/papers/2302.09755/) | PubMed | MLP | 0.8747 | 0.6970 | 497 | [Finding the Missing-half: Graph Complementary Learning for Homophily-prone...](/papers/2306.07608/) | published later (2023-06-13) |
| [2103.07295](/papers/2103.07295/) | CiteSeer | ChebNet | 0.8094 | 0.6960 | 497 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | published later (2024-03) |
| [2407.07457](/papers/2407.07457/) | Cora | ENGINE | 0.9148 | 0.8154 | 497 | [Efficient Tuning and Inference for Large Language Models...](/papers/2401.15569/) | already known (2024-01) |
| [2003.02228](/papers/2003.02228/) | PubMed | GAT | 0.9233 | 0.7821 | 496 | [arXiv:2402.08170](/papers/2402.08170/) | published later (2024-02) |
| [2209.07754](/papers/2209.07754/) | CiteSeer | GAT | 0.8227 | 0.6981 | 496 | [Instance-Aware Graph Prompt Learning](/papers/2411.17676/) | published later (2024-11) |
| [2205.13700](/papers/2205.13700/) | PubMed | GloGNN | 0.8962 | 0.7680 | 495 | [Finding Global Homophily in Graph Neural Networks When...](/papers/2205.07308/) | published later (2022-05-15) |
| [2003.13663](/papers/2003.13663/) | Cora | GCN | 0.9004 | 0.8123 | 495 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2502.20885](/papers/2502.20885/) | CiteSeer | GSC | 0.7370 | 0.5456 | 494 | [Generative Subgraph Contrast for Self-Supervised Graph Representation Learning](/papers/2207.11996/) | already known (2022-07) |
| [1811.05868](/papers/1811.05868/) | PubMed | MLP | 0.8747 | 0.7000 | 494 | [Finding the Missing-half: Graph Complementary Learning for Homophily-prone...](/papers/2306.07608/) | published later (2023-06-13) |
| [1812.04202](/papers/1812.04202/) | PubMed | FastGCN | 0.8800 | 0.7210 | 494 | [Policy-GNN: Aggregation Optimization for Graph Neural Networks](/papers/2006.15097/) | published later (2020-06) |
| [2211.15081](/papers/2211.15081/) | PubMed | ACMGCN | 0.9096 | 0.7810 | 494 | [Language is All a Graph Needs](/papers/2308.07134/) | published later (2023-08) |
| [2601.08230](/papers/2601.08230/) | CiteSeer | GraphSAGE | 0.8269 | 0.6990 | 494 | [Probing GNN Explainers: A Rigorous Theoretical and Empirical...](/papers/2106.09078/) | already known (2021-06-16) |
| [2211.15081](/papers/2211.15081/) | CiteSeer | JacobiConv | 0.8078 | 0.6960 | 494 | [Optimizing Polynomial Graph Filters: A Novel Adaptive Krylov...](/papers/2403.07954/) | published later (2024-03) |
| [2302.14806](/papers/2302.14806/) | CiteSeer | CPGNN | 0.7691 | 0.6810 | 494 | [Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective...](/papers/2402.15326/) | published later (2024-02) |
| [2407.11025](/papers/2407.11025/) | Cora | GCN | 0.9004 | 0.8127 | 494 | [arXiv:2401.09125](/papers/2401.09125/) | already known (2024-01) |
| [1906.01210](/papers/1906.01210/) | Cora | DeepWalk | 0.8297 | 0.4674 | 493 | [Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction](/papers/2202.09025/) | published later (2022-02) |
| [1312.6203](/papers/1312.6203/) | PubMed | ChebNet | 0.8951 | 0.7650 | 493 | [arXiv:2310.10064](/papers/2310.10064/) | published later (2023-10) |
| [2010.01777](/papers/2010.01777/) | CiteSeer | GCN | 0.8800 | 0.7013 | 492 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2205.13700](/papers/2205.13700/) | CiteSeer | GAT | 0.8227 | 0.6990 | 492 | [Instance-Aware Graph Prompt Learning](/papers/2411.17676/) | published later (2024-11) |
| [2302.09755](/papers/2302.09755/) | CiteSeer | APPNP | 0.7933 | 0.6920 | 491 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | published later (2024-03) |
| [2407.11025](/papers/2407.11025/) | Cora | SGC | 0.8805 | 0.7897 | 491 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [1802.04407](/papers/1802.04407/) | Cora | DeepWalk | 0.8297 | 0.4840 | 490 | [Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction](/papers/2202.09025/) | published later (2022-02) |
| [2108.12055](/papers/2108.12055/) | PubMed | GCN | 0.9296 | 0.7840 | 490 | [arXiv:2402.08170](/papers/2402.08170/) | published later (2024-02) |
| [2302.09755](/papers/2302.09755/) | PubMed | GCN | 0.9296 | 0.7840 | 490 | [arXiv:2402.08170](/papers/2402.08170/) | published later (2024-02) |
| [2510.17185](/papers/2510.17185/) | CiteSeer | GRAND | 0.7646 | 0.6693 | 490 | [Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective...](/papers/2402.15326/) | already known (2024-02) |
| [1902.08226](/papers/1902.08226/) | Cora | GCN | 0.9004 | 0.8140 | 490 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [1911.11430](/papers/1911.11430/) | Cora | GCN | 0.9004 | 0.8140 | 490 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2207.11996](/papers/2207.11996/) | Cora | GCN | 0.9004 | 0.8140 | 490 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2405.20445](/papers/2405.20445/) | Cora | GCN | 0.9004 | 0.8140 | 490 | [arXiv:2401.09125](/papers/2401.09125/) | already known (2024-01) |
| [2601.01207](/papers/2601.01207/) | Cora | GCN | 0.9004 | 0.8140 | 490 | [arXiv:2401.09125](/papers/2401.09125/) | already known (2024-01) |
| [2205.13700](/papers/2205.13700/) | Cora | SGC | 0.8805 | 0.7910 | 489 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2102.03147](/papers/2102.03147/) | Cora | GCN | 0.9004 | 0.8142 | 489 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2205.13700](/papers/2205.13700/) | CiteSeer | GEN | 0.8038 | 0.6970 | 488 | [GraphEdit: Large Language Models for Graph Structure Learning](/papers/2402.15183/) | published later (2024-02) |
| [2209.07754](/papers/2209.07754/) | Cora | GIN | 0.8705 | 0.7679 | 488 | [Unleashing the Potential of Text-attributed Graphs: Automatic Relation...](/papers/2405.18581/) | published later (2024-05) |
| [1812.04202](/papers/1812.04202/) | Cora | ChebNet | 0.8969 | 0.8120 | 488 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | published later (2024-03) |
| [1911.11430](/papers/1911.11430/) | Cora | ChebNet | 0.8969 | 0.8120 | 488 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | published later (2024-03) |
| [2007.16002](/papers/2007.16002/) | Cora | ChebNet | 0.8969 | 0.8120 | 488 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | published later (2024-03) |
| [2101.00797](/papers/2101.00797/) | Cora | ChebNet | 0.8969 | 0.8120 | 488 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | published later (2024-03) |
| [2108.01660](/papers/2108.01660/) | Cora | ChebNet | 0.8969 | 0.8120 | 488 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | published later (2024-03) |
| [2602.00064](/papers/2602.00064/) | CiteSeer | GCN | 0.8800 | 0.7020 | 487 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2507.13368](/papers/2507.13368/) | CiteSeer | MVGRL | 0.7381 | 0.5720 | 487 | [Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction](/papers/2202.09025/) | already known (2022-02) |
| [2601.08230](/papers/2601.08230/) | CiteSeer | GAT | 0.8227 | 0.7010 | 487 | [Instance-Aware Graph Prompt Learning](/papers/2411.17676/) | already known (2024-11) |
| [2007.16002](/papers/2007.16002/) | CiteSeer | ChebNet | 0.8094 | 0.6980 | 487 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | published later (2024-03) |
| [2101.00797](/papers/2101.00797/) | CiteSeer | ChebNet | 0.8094 | 0.6980 | 487 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | published later (2024-03) |
| [2211.15081](/papers/2211.15081/) | Cora | H2GCN | 0.8829 | 0.7950 | 487 | [Adapting to Heterophilic Graph Data with Structure-Guided Neighbor...](/papers/2506.08871/) | published later (2025-06) |
| [2403.03670](/papers/2403.03670/) | PubMed | GRACE | 0.8590 | 0.6370 | 486 | [arXiv:2306.13854](/papers/2306.13854/) | already known (2023-06) |
| [2205.13700](/papers/2205.13700/) | CiteSeer | GPR-GNN | 0.8013 | 0.6960 | 486 | [Optimizing Polynomial Graph Filters: A Novel Adaptive Krylov...](/papers/2403.07954/) | published later (2024-03) |
| [1312.6203](/papers/1312.6203/) | Cora | GCN | 0.9004 | 0.8150 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [1609.02907](/papers/1609.02907/) | Cora | GCN | 0.9004 | 0.8150 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [1710.10321](/papers/1710.10321/) | Cora | GCN | 0.9004 | 0.8150 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [1802.08888](/papers/1802.08888/) | Cora | GCN | 0.9004 | 0.8150 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [1803.10459](/papers/1803.10459/) | Cora | GCN | 0.9004 | 0.8150 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [1808.03965](/papers/1808.03965/) | Cora | GCN | 0.9004 | 0.8150 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [1812.04202](/papers/1812.04202/) | Cora | GCN | 0.9004 | 0.8150 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [1901.08150](/papers/1901.08150/) | Cora | GCN | 0.9004 | 0.8150 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [1905.05178](/papers/1905.05178/) | Cora | GCN | 0.9004 | 0.8150 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2001.05140](/papers/2001.05140/) | Cora | GCN | 0.9004 | 0.8150 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2003.08414](/papers/2003.08414/) | Cora | GCN | 0.9004 | 0.8150 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2006.08550](/papers/2006.08550/) | Cora | GCN | 0.9004 | 0.8150 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2006.13009](/papers/2006.13009/) | Cora | GCN | 0.9004 | 0.8150 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2006.15097](/papers/2006.15097/) | Cora | GCN | 0.9004 | 0.8150 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2007.02133](/papers/2007.02133/) | Cora | GCN | 0.9004 | 0.8150 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2007.08025](/papers/2007.08025/) | Cora | GCN | 0.9004 | 0.8150 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2007.16002](/papers/2007.16002/) | Cora | GCN | 0.9004 | 0.8150 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2009.14332](/papers/2009.14332/) | Cora | GCN | 0.9004 | 0.8150 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2101.00797](/papers/2101.00797/) | Cora | GCN | 0.9004 | 0.8150 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2101.03464](/papers/2101.03464/) | Cora | GCN | 0.9004 | 0.8150 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2102.06986](/papers/2102.06986/) | Cora | GCN | 0.9004 | 0.8150 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2105.11689](/papers/2105.11689/) | Cora | GCN | 0.9004 | 0.8150 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2106.04051](/papers/2106.04051/) | Cora | GCN | 0.9004 | 0.8150 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2108.01660](/papers/2108.01660/) | Cora | GCN | 0.9004 | 0.8150 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2110.09443](/papers/2110.09443/) | Cora | GCN | 0.9004 | 0.8150 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2111.10698](/papers/2111.10698/) | Cora | GCN | 0.9004 | 0.8150 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2111.12952](/papers/2111.12952/) | Cora | GCN | 0.9004 | 0.8150 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2202.13060](/papers/2202.13060/) | Cora | GCN | 0.9004 | 0.8150 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2204.06127](/papers/2204.06127/) | Cora | GCN | 0.9004 | 0.8150 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2209.15454](/papers/2209.15454/) | Cora | GCN | 0.9004 | 0.8150 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2210.08792](/papers/2210.08792/) | Cora | GCN | 0.9004 | 0.8150 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2305.10758](/papers/2305.10758/) | Cora | GCN | 0.9004 | 0.8150 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2305.17589](/papers/2305.17589/) | Cora | GCN | 0.9004 | 0.8150 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2307.16026](/papers/2307.16026/) | Cora | GCN | 0.9004 | 0.8150 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2311.05767](/papers/2311.05767/) | Cora | GCN | 0.9004 | 0.8150 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2402.08023](/papers/2402.08023/) | Cora | GCN | 0.9004 | 0.8150 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | already known (2024-01) |
| [2402.09600](/papers/2402.09600/) | Cora | GCN | 0.9004 | 0.8150 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | already known (2024-01) |
| [2402.11235](/papers/2402.11235/) | Cora | GCN | 0.9004 | 0.8150 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | already known (2024-01) |
| [2410.05593](/papers/2410.05593/) | Cora | GCN | 0.9004 | 0.8150 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | already known (2024-01) |
| [2512.24062](/papers/2512.24062/) | Cora | GCN | 0.9004 | 0.8154 | 486 | [arXiv:2401.09125](/papers/2401.09125/) | already known (2024-01) |
| [2402.11235](/papers/2402.11235/) | CiteSeer | OFA | 0.7304 | 0.3792 | 485 | [GLBench: A Comprehensive Benchmark for Graph with Large...](/papers/2407.07457/) | published later (2024-07) |
| [2601.15124](/papers/2601.15124/) | CiteSeer | OFA | 0.7304 | 0.3800 | 485 | [GLBench: A Comprehensive Benchmark for Graph with Large...](/papers/2407.07457/) | already known (2024-07) |
| [2106.04714](/papers/2106.04714/) | PubMed | GIN | 0.8977 | 0.7740 | 485 | [Unleashing the Potential of Text-attributed Graphs: Automatic Relation...](/papers/2405.18581/) | published later (2024-05) |
| [1611.08402](/papers/1611.08402/) | Cora | GCN | 0.9004 | 0.8159 | 485 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2502.20885](/papers/2502.20885/) | Cora | GRACE | 0.8911 | 0.8086 | 485 | [Toward Graph-Tokenizing Large Language Models with Reconstructive Graph...](/papers/2603.01385/) | published later (2026-03) |
| [2411.02279](/papers/2411.02279/) | PubMed | GPRGNN | 0.8950 | 0.7702 | 483 | [arXiv:2310.10064](/papers/2310.10064/) | already known (2023-10) |
| [2205.13700](/papers/2205.13700/) | Cora | ACMGCN | 0.8975 | 0.8130 | 483 | [Language is All a Graph Needs](/papers/2308.07134/) | published later (2023-08) |
| [2205.13700](/papers/2205.13700/) | Cora | GOAL | 0.8875 | 0.8060 | 483 | [Finding the Missing-half: Graph Complementary Learning for Homophily-prone...](/papers/2306.07608/) | published later (2023-06-13) |
| [1609.02907](/papers/1609.02907/) | CiteSeer | GCN | 0.8800 | 0.7030 | 482 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | published later (2018-05) |
| [1802.08888](/papers/1802.08888/) | CiteSeer | GCN | 0.8800 | 0.7030 | 482 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | published later (2018-05) |
| [1803.10459](/papers/1803.10459/) | CiteSeer | GCN | 0.8800 | 0.7030 | 482 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | published later (2018-05) |
| [1808.03965](/papers/1808.03965/) | CiteSeer | GCN | 0.8800 | 0.7030 | 482 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [1901.08150](/papers/1901.08150/) | CiteSeer | GCN | 0.8800 | 0.7030 | 482 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [1905.05178](/papers/1905.05178/) | CiteSeer | GCN | 0.8800 | 0.7030 | 482 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2001.05140](/papers/2001.05140/) | CiteSeer | GCN | 0.8800 | 0.7030 | 482 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2003.08414](/papers/2003.08414/) | CiteSeer | GCN | 0.8800 | 0.7030 | 482 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2006.02380](/papers/2006.02380/) | CiteSeer | GCN | 0.8800 | 0.7030 | 482 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2006.08550](/papers/2006.08550/) | CiteSeer | GCN | 0.8800 | 0.7030 | 482 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2006.13009](/papers/2006.13009/) | CiteSeer | GCN | 0.8800 | 0.7030 | 482 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2006.15097](/papers/2006.15097/) | CiteSeer | GCN | 0.8800 | 0.7030 | 482 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2007.08025](/papers/2007.08025/) | CiteSeer | GCN | 0.8800 | 0.7030 | 482 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2007.16002](/papers/2007.16002/) | CiteSeer | GCN | 0.8800 | 0.7030 | 482 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2101.00797](/papers/2101.00797/) | CiteSeer | GCN | 0.8800 | 0.7030 | 482 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2101.03464](/papers/2101.03464/) | CiteSeer | GCN | 0.8800 | 0.7030 | 482 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2102.06986](/papers/2102.06986/) | CiteSeer | GCN | 0.8800 | 0.7030 | 482 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2105.11689](/papers/2105.11689/) | CiteSeer | GCN | 0.8800 | 0.7030 | 482 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2106.04051](/papers/2106.04051/) | CiteSeer | GCN | 0.8800 | 0.7030 | 482 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2111.10698](/papers/2111.10698/) | CiteSeer | GCN | 0.8800 | 0.7030 | 482 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2204.06127](/papers/2204.06127/) | CiteSeer | GCN | 0.8800 | 0.7030 | 482 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2207.11996](/papers/2207.11996/) | CiteSeer | GCN | 0.8800 | 0.7030 | 482 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2209.15454](/papers/2209.15454/) | CiteSeer | GCN | 0.8800 | 0.7030 | 482 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2210.08792](/papers/2210.08792/) | CiteSeer | GCN | 0.8800 | 0.7030 | 482 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2307.16026](/papers/2307.16026/) | CiteSeer | GCN | 0.8800 | 0.7030 | 482 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2402.08023](/papers/2402.08023/) | CiteSeer | GCN | 0.8800 | 0.7030 | 482 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2402.09600](/papers/2402.09600/) | CiteSeer | GCN | 0.8800 | 0.7030 | 482 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2402.11235](/papers/2402.11235/) | CiteSeer | GCN | 0.8800 | 0.7030 | 482 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2010.01777](/papers/2010.01777/) | PubMed | GCN | 0.9296 | 0.7856 | 482 | [arXiv:2402.08170](/papers/2402.08170/) | published later (2024-02) |
| [2211.15081](/papers/2211.15081/) | Cora | GIN | 0.8705 | 0.7730 | 482 | [Unleashing the Potential of Text-attributed Graphs: Automatic Relation...](/papers/2405.18581/) | published later (2024-05) |
| [2306.10759](/papers/2306.10759/) | Cora | GCN | 0.9004 | 0.8160 | 482 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2306.11264](/papers/2306.11264/) | Cora | GCN | 0.9004 | 0.8160 | 482 | [arXiv:2401.09125](/papers/2401.09125/) | published later (2024-01) |
| [2411.02279](/papers/2411.02279/) | Cora | GCN | 0.9004 | 0.8161 | 482 | [arXiv:2401.09125](/papers/2401.09125/) | already known (2024-01) |
| [2506.22299](/papers/2506.22299/) | Cora | GCN | 0.9004 | 0.8163 | 482 | [arXiv:2401.09125](/papers/2401.09125/) | already known (2024-01) |
| [2411.02279](/papers/2411.02279/) | Cora | NodeFormer | 0.8856 | 0.8028 | 482 | [Bridging Large Language Models and Graph Structure Learning...](/papers/2410.12096/) | already known (2024-10) |
| [2411.02279](/papers/2411.02279/) | CiteSeer | GCN | 0.8800 | 0.7035 | 481 | [Adversarial Attacks on Neural Networks for Graph Data](/papers/1805.07984/) | already known (2018-05) |
| [2007.02133](/papers/2007.02133/) | PubMed | GAT | 0.9233 | 0.7850 | 481 | [arXiv:2402.08170](/papers/2402.08170/) | published later (2024-02) |
| [2410.05593](/papers/2410.05593/) | PubMed | GAT | 0.9233 | 0.7850 | 481 | [arXiv:2402.08170](/papers/2402.08170/) | already known (2024-02) |
| [2503.19382](/papers/2503.19382/) | PubMed | AD-GraphSAGE | 0.9026 | 0.7810 | 481 | [CAP: Co-Adversarial Perturbation on Weights and Features for...](/papers/2110.14855/) | already known (2021-10) |
| [2211.15081](/papers/2211.15081/) | CiteSeer | FAGCN | 0.7682 | 0.6830 | 481 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [2307.16026](/papers/2307.16026/) | PubMed | MLP | 0.8747 | 0.7135 | 480 | [Finding the Missing-half: Graph Complementary Learning for Homophily-prone...](/papers/2306.07608/) | already known (2023-06-13) |
| [2506.22299](/papers/2506.22299/) | PubMed | GAT | 0.9233 | 0.7858 | 480 | [arXiv:2402.08170](/papers/2402.08170/) | already known (2024-02) |
| [2403.03670](/papers/2403.03670/) | CiteSeer | GRACE | 0.7490 | 0.6310 | 480 | [arXiv:2306.13854](/papers/2306.13854/) | already known (2023-06) |
| [2407.14996](/papers/2407.14996/) | Cora | SGC | 0.8805 | 0.7930 | 480 | [Graph homophily booster: Reimagining the role of discrete...](/papers/2602.07256/) | published later (2026-02) |
| [1907.04786](/papers/1907.04786/) | PubMed | MLP | 0.8747 | 0.7140 | 479 | [Finding the Missing-half: Graph Complementary Learning for Homophily-prone...](/papers/2306.07608/) | published later (2023-06-13) |
| [1911.11430](/papers/1911.11430/) | PubMed | MLP | 0.8747 | 0.7140 | 479 | [Finding the Missing-half: Graph Complementary Learning for Homophily-prone...](/papers/2306.07608/) | published later (2023-06-13) |
| [2007.16002](/papers/2007.16002/) | PubMed | MLP | 0.8747 | 0.7140 | 479 | [Finding the Missing-half: Graph Complementary Learning for Homophily-prone...](/papers/2306.07608/) | published later (2023-06-13) |
| [2101.03464](/papers/2101.03464/) | PubMed | MLP | 0.8747 | 0.7140 | 479 | [Finding the Missing-half: Graph Complementary Learning for Homophily-prone...](/papers/2306.07608/) | published later (2023-06-13) |
| [2102.06986](/papers/2102.06986/) | PubMed | MLP | 0.8747 | 0.7140 | 479 | [Finding the Missing-half: Graph Complementary Learning for Homophily-prone...](/papers/2306.07608/) | published later (2023-06-13) |
| [2108.01660](/papers/2108.01660/) | PubMed | MLP | 0.8747 | 0.7140 | 479 | [Finding the Missing-half: Graph Complementary Learning for Homophily-prone...](/papers/2306.07608/) | published later (2023-06-13) |
| [2202.08480](/papers/2202.08480/) | PubMed | MLP | 0.8747 | 0.7140 | 479 | [Finding the Missing-half: Graph Complementary Learning for Homophily-prone...](/papers/2306.07608/) | published later (2023-06-13) |
| [2410.05593](/papers/2410.05593/) | PubMed | MLP | 0.8747 | 0.7140 | 479 | [Finding the Missing-half: Graph Complementary Learning for Homophily-prone...](/papers/2306.07608/) | already known (2023-06-13) |
| [2211.15081](/papers/2211.15081/) | CiteSeer | GCNII | 0.7768 | 0.6900 | 479 | [Graph as a Feature: A Graph-Aware Non-Neural Model...](/papers/2411.12330/) | published later (2024-11) |
| [1812.04202](/papers/1812.04202/) | Cora | FastGCN | 0.8500 | 0.7230 | 477 | [Policy-GNN: Aggregation Optimization for Graph Neural Networks](/papers/2006.15097/) | published later (2020-06) |
| [2205.13700](/papers/2205.13700/) | CiteSeer | H2GCN | 0.7711 | 0.6870 | 477 | [Optimization-Induced Graph Implicit Nonlinear Diffusion](/papers/2206.14418/) | published later (2022-06-29) |
| [2602.07256](/papers/2602.07256/) | Cora | ChebNet | 0.8969 | 0.8158 | 477 | [ChebMixer: Efficient Graph Representation Learning with MLP Mixer](/papers/2403.16358/) | already known (2024-03) |
| [2502.11836](/papers/2502.11836/) | CiteSeer | OFA | 0.7304 | 0.4131 | 476 | [GLBench: A Comprehensive Benchmark for Graph with Large...](/papers/2407.07457/) | already known (2024-07) |
| [2403.03670](/papers/2403.03670/) | PubMed | DGI | 0.8595 | 0.6570 | 476 | [MGAE: Masked Autoencoders for Self-Supervised Learning on Graphs](/papers/2201.02534/) | already known (2022-01) |
| [2502.20885](/papers/2502.20885/) | CiteSeer | DSSL | 0.7351 | 0.5416 | 476 | [MUSE: Multi-View Contrastive Learning for Heterophilic Graphs](/papers/2307.16026/) | already known (2023-07) |
| [2102.03147](/papers/2102.03147/) | CiteSeer | GAT | 0.8227 | 0.7036 | 476 | [Instance-Aware Graph Prompt Learning](/papers/2411.17676/) | published later (2024-11) |