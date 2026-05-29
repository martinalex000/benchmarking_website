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

**Flagged papers:** 44
**Flagged rows:** 170

| ArXiv | Title | Dataset | Metric | Model | Value | Dataset Median | Reason |
|-------|-------|---------|--------|-------|------:|---------------:|--------|
| 1603.05629 | Discriminative Embeddings of Latent Variable Mod | ECHO-Energy | MAE | Predict mean | 1.9864 | 0.0962 | 20.6x above dataset median |
| 1703.06114 | Deep Sets | D&D | Recall@10 | Random | 0.0001 | 0.0604 | 604.0x below dataset median |
| 1703.06114 | Deep Sets | D&D | Recall@100 | Random | 0.002 | 0.285 | 142.5x below dataset median |
| 1703.06114 | Deep Sets | D&D | Recall@1k | Random | 0.016 | 0.494 | 30.9x below dataset median |
| 1707.01476 | Convolutional 2D Knowledge Graph Embeddings | FB15k-237 | MRR | Inverse Model | 0.01 | 0.335 | 33.5x below dataset median |
| 1710.10321 | arXiv:1710.10321 | Flow | MAE | DimeNet++ | 0.068 | 1.79 | 26.3x below dataset median |
| 1710.10321 | arXiv:1710.10321 | Flow | MAE | GCN | 0.085 | 1.79 | 21.1x below dataset median |
| 1710.10321 | arXiv:1710.10321 | Flow | MAE | GIN | 0.079 | 1.79 | 22.7x below dataset median |
| 1710.10321 | arXiv:1710.10321 | Flow | MAE | Graphormer | 0.062 | 1.79 | 28.9x below dataset median |
| 1710.10321 | arXiv:1710.10321 | Flow | MAE | PNA | 0.071 | 1.79 | 25.2x below dataset median |
| 1710.10321 | arXiv:1710.10321 | Flow | MAE | SphereNet | 0.065 | 1.79 | 27.5x below dataset median |
| 1802.08786 | Syntax-Directed Variational Autoencoder for Stru | ZINC | RMSE | CVAE | 1.504 | 0.0085 | 176.9x above dataset median |
| 1802.08786 | Syntax-Directed Variational Autoencoder for Stru | ZINC | RMSE | GVAE | 1.404 | 0.0085 | 165.2x above dataset median |
| 1802.08786 | Syntax-Directed Variational Autoencoder for Stru | ZINC | RMSE | SD-VAE | 1.366 | 0.0085 | 160.7x above dataset median |
| 1811.00855 | Session-based Recommendation with Graph Neural N | Case 1 | P@20 | FPMC | 0.4562 | 27.08 | 59.4x below dataset median |
| 1811.00855 | Session-based Recommendation with Graph Neural N | Case 1 | P@20 | POP | 1.33 | 27.08 | 20.4x below dataset median |
| 1811.00855 | Session-based Recommendation with Graph Neural N | Case 1 | P@20 | SR-GNN-ATT | 0.7031 | 27.08 | 38.5x below dataset median |
| 1811.00855 | Session-based Recommendation with Graph Neural N | Case 1 | P@20 | SR-GNN-L | 0.7011 | 27.08 | 38.6x below dataset median |
| 1811.00855 | Session-based Recommendation with Graph Neural N | D&D | P@20 | POP | 0.0089 | 0.2945 | 33.1x below dataset median |
| 1907.04786 | Fast Haar Transforms for Graph Neural Networks | QM7b | MAE | ANI-1 | 2.86 | 95.3 | 33.3x below dataset median |
| 2007.02842 | Adaptive Graph Convolutional Recurrent Network f | D&D | MAE | AGCRN | 15.95 | 0.6 | 26.6x above dataset median |
| 2007.02842 | Adaptive Graph Convolutional Recurrent Network f | D&D | MAE | DCRNN | 16.82 | 0.6 | 28.0x above dataset median |
| 2007.02842 | Adaptive Graph Convolutional Recurrent Network f | D&D | MAE | DSANet | 17.14 | 0.6 | 28.6x above dataset median |
| 2007.02842 | Adaptive Graph Convolutional Recurrent Network f | D&D | MAE | FastGCN | 18.25 | 0.6 | 30.4x above dataset median |
| 2007.02842 | Adaptive Graph Convolutional Recurrent Network f | D&D | MAE | GRU-ED | 22 | 0.6 | 36.7x above dataset median |
| 2007.02842 | Adaptive Graph Convolutional Recurrent Network f | D&D | MAE | HA | 34.86 | 0.6 | 58.1x above dataset median |
| 2007.02842 | Adaptive Graph Convolutional Recurrent Network f | D&D | MAE | STGCN | 17.13 | 0.6 | 28.6x above dataset median |
| 2007.02842 | Adaptive Graph Convolutional Recurrent Network f | D&D | MAE | VAR | 19.19 | 0.6 | 32.0x above dataset median |
| 2010.15421 | Scalable Graph Neural Networks via Bidirectional | D&D | F1 | PPRGo | 0.016 | 0.46 | 28.7x below dataset median |
| 2105.07246 | arXiv:2105.07246 | QM9 | COV | CGCF | 0.696 | 81.84 | 117.6x below dataset median |
| 2105.07246 | arXiv:2105.07246 | QM9 | COV | CGCF + FF | 0.7352 | 81.84 | 111.3x below dataset median |
| 2105.07246 | arXiv:2105.07246 | QM9 | COV | CVAE | 0.0852 | 81.84 | 960.6x below dataset median |
| 2105.07246 | arXiv:2105.07246 | QM9 | COV | CVGAE + FF | 0.631 | 81.84 | 129.7x below dataset median |
| 2105.07246 | arXiv:2105.07246 | QM9 | COV | ConfVAE | 0.7798 | 81.84 | 104.9x below dataset median |
| 2105.07246 | arXiv:2105.07246 | QM9 | COV | ConfVAE- + FF | 0.8146 | 81.84 | 100.5x below dataset median |
| 2105.07246 | arXiv:2105.07246 | QM9 | COV | GraphDG | 0.5509 | 81.84 | 148.6x below dataset median |
| 2105.07246 | arXiv:2105.07246 | QM9 | COV | GraphDG + FF | 0.7067 | 81.84 | 115.8x below dataset median |
| 2105.07246 | arXiv:2105.07246 | QM9 | COV | RDKit | 0.7994 | 81.84 | 102.4x below dataset median |
| 2106.09553 | How Much Structural Information Large Scale Mole | QM9 | MAE | 123-gnn | 1.9995 | 0.058 | 34.5x above dataset median |
| 2106.09553 | How Much Structural Information Large Scale Mole | QM9 | MAE | A-FP | 2.6355 | 0.058 | 45.4x above dataset median |
| 2106.09553 | How Much Structural Information Large Scale Mole | QM9 | MAE | ChemBERTa | 8.7067 | 0.058 | 150.1x above dataset median |
| 2106.09553 | How Much Structural Information Large Scale Mole | QM9 | MAE | GC | 4.3536 | 0.058 | 75.1x above dataset median |
| 2106.09553 | How Much Structural Information Large Scale Mole | QM9 | MAE | MPNN | 3.1898 | 0.058 | 55.0x above dataset median |
| 2106.09553 | How Much Structural Information Large Scale Mole | QM9 | MAE | MoLFormer-Base | 2.25 | 0.058 | 38.8x above dataset median |
| 2106.09553 | How Much Structural Information Large Scale Mole | QM9 | MAE | MoLFormer-XL | 1.5894 | 0.058 | 27.4x above dataset median |
| 2106.09575 | Rotation Invariant Graph Neural Networks using S | MD17 | MAE | GDML | 0.02 | 0.556 | 27.8x below dataset median |
| 2106.15098 | Molecule Generation by Principal Subgraph Mining | QM9 | FCD | GA | 0.004 | 0.49 | 122.5x below dataset median |
| 2106.15098 | Molecule Generation by Principal Subgraph Mining | QM9 | Novelty | GA | 0.008 | 0.523 | 65.4x below dataset median |
| 2106.15098 | Molecule Generation by Principal Subgraph Mining | QM9 | Uniqueness | GA | 0.008 | 0.6595 | 82.4x below dataset median |
| 2106.15098 | Molecule Generation by Principal Subgraph Mining | ZINC | FCD | F-VAE* | 0.085 | 14.439 | 169.9x below dataset median |
| 2106.15098 | Molecule Generation by Principal Subgraph Mining | ZINC | FCD | GA | 0.001 | 14.439 | 14439.0x below dataset median |
| 2106.15098 | Molecule Generation by Principal Subgraph Mining | ZINC | FCD | GCPN | 0.003 | 14.439 | 4813.0x below dataset median |
| 2106.15098 | Molecule Generation by Principal Subgraph Mining | ZINC | FCD | GraphAF | 0.023 | 14.439 | 627.8x below dataset median |
| 2106.15098 | Molecule Generation by Principal Subgraph Mining | ZINC | FCD | GraphDF | 0.001 | 14.439 | 14439.0x below dataset median |
| 2106.15098 | Molecule Generation by Principal Subgraph Mining | ZINC | FCD | H-VAE* | 0.037 | 14.439 | 390.2x below dataset median |
| 2106.15098 | Molecule Generation by Principal Subgraph Mining | ZINC | FCD | HierVAE | 0.001 | 14.439 | 14439.0x below dataset median |
| 2106.15098 | Molecule Generation by Principal Subgraph Mining | ZINC | FCD | JT-VAE | 0.263 | 14.439 | 54.9x below dataset median |
| 2106.15098 | Molecule Generation by Principal Subgraph Mining | ZINC | FCD | MARS | 0.271 | 14.439 | 53.3x below dataset median |
| 2106.15098 | Molecule Generation by Principal Subgraph Mining | ZINC | FCD | PS-VAE | 0.318 | 14.439 | 45.4x below dataset median |
| 2109.04200 | Double-Scale Self-Supervised Hypergraph Learning | D&D | NDCG@20 | Popular | 0.003 | 0.075 | 25.0x below dataset median |
| 2201.02534 | MGAE: Masked Autoencoders for Self-Supervised Le | ogbl-citation2 | Hits@10 | SelfTask-GNN | 0.65 | 0.0325 | 20.0x above dataset median |
| 2202.01356 | Direct Molecular Conformation Generation | D&D | COV | CVAE | 0 | 67.16 | zero value against positive dataset median |
| 2202.01356 | Direct Molecular Conformation Generation | QM9 | COV | CVAE | 0.09 | 81.84 | 909.3x below dataset median |
| 2202.09025 | Graph Auto-Encoder Via Neighborhood Wasserstein  | House | Completeness | DeepWalk | 0.01 | 1 | 100.0x below dataset median |
| 2202.09025 | Graph Auto-Encoder Via Neighborhood Wasserstein  | House | Completeness | Node2Vec | 0.01 | 1 | 100.0x below dataset median |
| 2203.02923 | GeoDiff: a Geometric Diffusion Model for Molecul | D&D | COV-R | CVAE | 0 | 67.16 | zero value against positive dataset median |
| 2206.04216 | Neo-GNNs: Neighborhood Overlap-aware Graph Neura | ogbl-citation2 | Hits@100 | MLP | 0.0047 | 0.20755 | 44.2x below dataset median |
| 2209.03473 | Higher-order Clustering and Pooling for Graph Ne | DBLP | NMI | MSC | 0.005 | 0.284 | 56.8x below dataset median |
| 2209.03473 | Higher-order Clustering and Pooling for Graph Ne | PubMed | NMI | MSC | 0.002 | 0.212 | 106.0x below dataset median |
| 2209.05710 | MDM: Molecular Diffusion Model for 3D Molecule G | QM9 | MAE | #Atoms | 3.862 | 0.058 | 66.6x above dataset median |
| 2209.05710 | MDM: Molecular Diffusion Model for 3D Molecule G | QM9 | MAE | EDM | 2.76 | 0.058 | 47.6x above dataset median |
| 2209.05710 | MDM: Molecular Diffusion Model for 3D Molecule G | QM9 | MAE | MDM | 1.591 | 0.058 | 27.4x above dataset median |
| 2209.05710 | MDM: Molecular Diffusion Model for 3D Molecule G | QM9 | MAE | Naive (U-bound) | 9.013 | 0.058 | 155.4x above dataset median |
| 2210.15304 | Explaining the Explainers in Graph Neural Networ | House | Plausibility | CAM | 0.02 | 0.4 | 20.0x below dataset median |
| 2210.15304 | Explaining the Explainers in Graph Neural Networ | House | Plausibility | GradExpl-Node | 0 | 0.4 | zero value against positive dataset median |
| 2210.15304 | Explaining the Explainers in Graph Neural Networ | House | Plausibility | GuidedBp | 0 | 0.4 | zero value against positive dataset median |
| 2211.14425 | PatchGT: Transformer over Non-trainable Clusters | MUTAG | Accuracy | DiffPool-NoLP | 0 | 0.8292 | zero value against positive dataset median |
| 2211.14425 | PatchGT: Transformer over Non-trainable Clusters | MUTAG | Accuracy | EigenGCN | 0 | 0.8292 | zero value against positive dataset median |
| 2211.14425 | PatchGT: Transformer over Non-trainable Clusters | MUTAG | Accuracy | GAT | 0 | 0.8292 | zero value against positive dataset median |
| 2211.14425 | PatchGT: Transformer over Non-trainable Clusters | MUTAG | Accuracy | GCN | 0 | 0.8292 | zero value against positive dataset median |
| 2211.14425 | PatchGT: Transformer over Non-trainable Clusters | MUTAG | Accuracy | GIN | 0 | 0.8292 | zero value against positive dataset median |
| 2211.14425 | PatchGT: Transformer over Non-trainable Clusters | MUTAG | Accuracy | Graph U-Net | 0 | 0.8292 | zero value against positive dataset median |
| 2211.14425 | PatchGT: Transformer over Non-trainable Clusters | MUTAG | Accuracy | GraphSAGE | 0 | 0.8292 | zero value against positive dataset median |
| 2211.14425 | PatchGT: Transformer over Non-trainable Clusters | MUTAG | Accuracy | Nested GIN | 0 | 0.8292 | zero value against positive dataset median |
| 2211.14425 | PatchGT: Transformer over Non-trainable Clusters | MUTAG | Accuracy | SEG-BERT | 0 | 0.8292 | zero value against positive dataset median |
| 2211.14425 | PatchGT: Transformer over Non-trainable Clusters | MUTAG | Accuracy | UGNN | 0 | 0.8292 | zero value against positive dataset median |
| 2212.05517 | SchNetPack 2.0: A neural network toolbox for ato | QM9 | MAE | PaiNN | 5.7 | 0.058 | 98.3x above dataset median |
| 2212.05517 | SchNetPack 2.0: A neural network toolbox for ato | QM9 | MAE | SO3net (l_max=1) | 6.4 | 0.058 | 110.3x above dataset median |
| 2212.05517 | SchNetPack 2.0: A neural network toolbox for ato | QM9 | MAE | SchNet | 9.6 | 0.058 | 165.5x above dataset median |
| 2303.16458 | When to Pre-Train Graph Neural Networks? From Da | ogbg-molhiv | Pearson correlation coefficient | Graph Statistics | 0.0174 | 0.57845 | 33.2x below dataset median |
| 2303.16458 | When to Pre-Train Graph Neural Networks? From Da | ogbg-molhiv | Pearson correlation coefficient | Spectrum of Graph Laplacian | -0.1125 | 0.57845 | -5.1x below dataset median |
| 2304.03724 | GeoTMI: Predicting Quantum Chemical Property wit | QM9 | MAE | DimeNet++ | 8.99 | 0.058 | 155.0x above dataset median |
| 2304.03724 | GeoTMI: Predicting Quantum Chemical Property wit | QM9 | MAE | EGNN | 12.9 | 0.058 | 222.4x above dataset median |
| 2304.03724 | GeoTMI: Predicting Quantum Chemical Property wit | QM9 | MAE | EGNN + GeoTMI | 14.5 | 0.058 | 250.0x above dataset median |
| 2304.03724 | GeoTMI: Predicting Quantum Chemical Property wit | QM9 | MAE | SchNet | 16.96 | 0.058 | 292.4x above dataset median |
| 2304.03724 | GeoTMI: Predicting Quantum Chemical Property wit | QM9 | MAE | Transformer | 14.78 | 0.058 | 254.8x above dataset median |
| 2305.13987 | On Structural Expressive Power of Graph Transfor | QM9 | MAE | Graphormer-Neighbor | 1.799 | 0.058 | 31.0x above dataset median |
| 2305.13987 | On Structural Expressive Power of Graph Transfor | QM9 | MAE | Graphormer-id | 3.176 | 0.058 | 54.8x above dataset median |
| 2306.03589 | How does over-squashing affect the power of GNNs | ZINC | MAE | GatedGCN | 0.004 | 0.139 | 34.8x below dataset median |
| 2306.03589 | How does over-squashing affect the power of GNNs | ZINC | MAE | GraphSAGE | 0.006 | 0.139 | 23.2x below dataset median |
| 2309.16685 | Target-aware Variational Auto-encoders for Ligan | D&D | MSE | AttentionDTA | 0.216 | 0.010275 | 21.0x above dataset median |
| 2309.16685 | Target-aware Variational Auto-encoders for Ligan | D&D | MSE | BiCompDTA | 0.237 | 0.010275 | 23.1x above dataset median |
| 2309.16685 | Target-aware Variational Auto-encoders for Ligan | D&D | MSE | DeepDTA | 0.261 | 0.010275 | 25.4x above dataset median |
| 2309.16685 | Target-aware Variational Auto-encoders for Ligan | D&D | MSE | FusionDTA | 0.22 | 0.010275 | 21.4x above dataset median |
| 2309.16685 | Target-aware Variational Auto-encoders for Ligan | D&D | MSE | GraphDTA | 0.258 | 0.010275 | 25.1x above dataset median |
| 2309.16685 | Target-aware Variational Auto-encoders for Ligan | D&D | MSE | KronRLS | 0.379 | 0.010275 | 36.9x above dataset median |
| 2309.16685 | Target-aware Variational Auto-encoders for Ligan | D&D | MSE | MATT-DTI | 0.227 | 0.010275 | 22.1x above dataset median |
| 2309.16685 | Target-aware Variational Auto-encoders for Ligan | D&D | MSE | SimBoost | 0.282 | 0.010275 | 27.4x above dataset median |
| 2309.16685 | Target-aware Variational Auto-encoders for Ligan | D&D | MSE | SimCNN-DTA | 0.319 | 0.010275 | 31.0x above dataset median |
| 2309.16685 | Target-aware Variational Auto-encoders for Ligan | D&D | MSE | WideDTA | 0.886 | 0.010275 | 86.2x above dataset median |
| 2311.17932 | Swallowing the Bitter Pill: Simplified Scalable  | D&D | COV-R | GeoDiff | 0.421 | 67.16 | 159.5x below dataset median |
| 2311.17932 | Swallowing the Bitter Pill: Simplified Scalable  | D&D | COV-R | GeoMol | 0.446 | 67.16 | 150.6x below dataset median |
| 2311.17932 | Swallowing the Bitter Pill: Simplified Scalable  | D&D | COV-R | MCF-B | 0.84 | 67.16 | 80.0x below dataset median |
| 2311.17932 | Swallowing the Bitter Pill: Simplified Scalable  | D&D | COV-R | MCF-L | 0.847 | 67.16 | 79.3x below dataset median |
| 2311.17932 | Swallowing the Bitter Pill: Simplified Scalable  | D&D | COV-R | MCF-S | 0.794 | 67.16 | 84.6x below dataset median |
| 2311.17932 | Swallowing the Bitter Pill: Simplified Scalable  | D&D | COV-R | Tors. Diff. | 0.727 | 67.16 | 92.4x below dataset median |
| 2312.11529 | Efficient and Scalable Graph Generation through  | BA graph | V.U.N. | BwR (EDP-GNN) | 0 | 0.15 | zero value against positive dataset median |
| 2312.11529 | Efficient and Scalable Graph Generation through  | BA graph | V.U.N. | EDGE | 0 | 0.15 | zero value against positive dataset median |
| 2312.11529 | Efficient and Scalable Graph Generation through  | BA graph | V.U.N. | GRAND | 0 | 0.15 | zero value against positive dataset median |
| 2312.11529 | Efficient and Scalable Graph Generation through  | BA graph | V.U.N. | GraphSNN | 0 | 0.15 | zero value against positive dataset median |
| 2312.11529 | Efficient and Scalable Graph Generation through  | D&D | V.U.N. | EDGE | 0 | 0.175 | zero value against positive dataset median |
| 2312.14439 | PUMA: Efficient Continual Graph Learning for Nod | Cora | AP | DSLR | 0.039 | 0.8813 | 22.6x below dataset median |
| 2312.14439 | PUMA: Efficient Continual Graph Learning for Nod | Cora | AP | ER-LS-GS | 0.03 | 0.8813 | 29.4x below dataset median |
| 2312.14439 | PUMA: Efficient Continual Graph Learning for Nod | Cora | AP | EWC | 0.029 | 0.8813 | 30.4x below dataset median |
| 2312.14439 | PUMA: Efficient Continual Graph Learning for Nod | Cora | AP | Fine Tuning | 0.022 | 0.8813 | 40.1x below dataset median |
| 2312.14439 | PUMA: Efficient Continual Graph Learning for Nod | Cora | AP | GEM | 0.025 | 0.8813 | 35.3x below dataset median |
| 2312.14439 | PUMA: Efficient Continual Graph Learning for Nod | Cora | AP | GNN+ERM | 0.031 | 0.8813 | 28.4x below dataset median |
| 2312.14439 | PUMA: Efficient Continual Graph Learning for Nod | Cora | AP | LwF | 0.022 | 0.8813 | 40.1x below dataset median |
| 2312.14439 | PUMA: Efficient Continual Graph Learning for Nod | Cora | AP | MAS | 0.022 | 0.8813 | 40.1x below dataset median |
| 2312.14439 | PUMA: Efficient Continual Graph Learning for Nod | Cora | AP | SSM | 0.035 | 0.8813 | 25.2x below dataset median |
| 2402.04538 | Triplet Interaction Improves Graph Transformers: | PCQM4Mv2 | MAE | EGT | 86.2 | 0.1153 | 747.6x above dataset median |
| 2402.04538 | Triplet Interaction Improves Graph Transformers: | PCQM4Mv2 | MAE | GCN-VN | 115.2 | 0.1153 | 999.1x above dataset median |
| 2402.04538 | Triplet Interaction Improves Graph Transformers: | PCQM4Mv2 | MAE | GEM-2 (+RDKit) | 80.6 | 0.1153 | 699.0x above dataset median |
| 2402.04538 | Triplet Interaction Improves Graph Transformers: | PCQM4Mv2 | MAE | GIN-VN | 108.4 | 0.1153 | 940.2x above dataset median |
| 2402.04538 | Triplet Interaction Improves Graph Transformers: | PCQM4Mv2 | MAE | GPS | 72 | 0.1153 | 624.5x above dataset median |
| 2402.04538 | Triplet Interaction Improves Graph Transformers: | PCQM4Mv2 | MAE | GRPE | 87.6 | 0.1153 | 759.8x above dataset median |
| 2402.04538 | Triplet Interaction Improves Graph Transformers: | PCQM4Mv2 | MAE | GraphGPS | 86.2 | 0.1153 | 747.6x above dataset median |
| 2402.04538 | Triplet Interaction Improves Graph Transformers: | PCQM4Mv2 | MAE | TGT-At | 69.8 | 0.1153 | 605.4x above dataset median |
| 2402.04538 | Triplet Interaction Improves Graph Transformers: | PCQM4Mv2 | MAE | TGT-At (+RDKit) | 68.3 | 0.1153 | 592.4x above dataset median |
| 2402.04538 | Triplet Interaction Improves Graph Transformers: | PCQM4Mv2 | MAE | TokenGT | 91.9 | 0.1153 | 797.1x above dataset median |
| 2402.04538 | Triplet Interaction Improves Graph Transformers: | PCQM4Mv2 | MAE | Transformer | 78.2 | 0.1153 | 678.2x above dataset median |
| 2402.04538 | Triplet Interaction Improves Graph Transformers: | PCQM4Mv2 | MAE | Uni-Mol+ (+RDKit) | 70.5 | 0.1153 | 611.4x above dataset median |
| 2402.08703 | A Survey of Generative AI for de novo Drug Desig | D&D | COV | CVAE | 0 | 67.16 | zero value against positive dataset median |
| 2402.08785 | InstructGraph: Boosting Large Language Models vi | Flow | Accuracy | LLaMA2 w/. CoT | 0 | 0.70205 | zero value against positive dataset median |
| 2402.08785 | InstructGraph: Boosting Large Language Models vi | Flow | Accuracy | LLaMA2 w/. GTM | 0 | 0.70205 | zero value against positive dataset median |
| 2402.08785 | InstructGraph: Boosting Large Language Models vi | Flow | Accuracy | Vicuna w/. CoT | 0 | 0.70205 | zero value against positive dataset median |
| 2402.08785 | InstructGraph: Boosting Large Language Models vi | Flow | Accuracy | Vicuna w/. GTM | 0 | 0.70205 | zero value against positive dataset median |
| 2402.18974 | Generating Graphs via Spectral Diffusion | PROTEINS | Deg. MMD | GGSD | 0.0014 | 0.03255 | 23.3x below dataset median |
| 2402.18974 | Generating Graphs via Spectral Diffusion | ToxCast | Deg. | GGSD | 0.0005 | 0.0166 | 33.2x below dataset median |
| 2402.18974 | Generating Graphs via Spectral Diffusion | ToxCast | Spect. | GDSS | 0.278 | 0.0064 | 43.4x above dataset median |
| 2402.18974 | Generating Graphs via Spectral Diffusion | ToxCast | Spect. | GSDM | 0.1578 | 0.0064 | 24.7x above dataset median |
| 2405.20445 | Fully-inductive Node Classification on Arbitrary | ogbn-arxiv | Accuracy | LabelProp | 0.0098 | 0.716 | 73.1x below dataset median |
| 2502.01171 | arXiv:2502.01171 | D&D | MAE | QHNet | 0.0001201 | 0.6 | 4995.8x below dataset median |
| 2502.01171 | arXiv:2502.01171 | D&D | MAE | SPHNet | 0.00010819 | 0.6 | 5545.8x below dataset median |
| 2502.01171 | arXiv:2502.01171 | D&D | MAE | WANet | 7.474e-05 | 0.6 | 8027.8x below dataset median |
| 2502.01171 | arXiv:2502.01171 | MD17 | MAE | PhiSNet | 1.865e-05 | 0.556 | 29812.3x below dataset median |
| 2502.01171 | arXiv:2502.01171 | MD17 | MAE | QHNet | 2.012e-05 | 0.556 | 27634.2x below dataset median |
| 2502.01171 | arXiv:2502.01171 | MD17 | MAE | SPHNet | 1.936e-05 | 0.556 | 28719.0x below dataset median |
| 2502.01171 | arXiv:2502.01171 | MD17 | MAE | SchNOrb | 0.0002278 | 0.556 | 2440.7x below dataset median |
| 2502.11836 | Model Generalization on Text Attribute Graphs: P | D&D | Accuracy | DGI | 0.0222 | 0.741 | 33.4x below dataset median |
| 2502.11836 | Model Generalization on Text Attribute Graphs: P | D&D | Accuracy | OFA | 0.0305 | 0.741 | 24.3x below dataset median |
| 2506.07624 | Return of ChebNet: Understanding and Improving a | BA graph | MAE | A-DGN w/ GCN backbone | 0.1913 | 4.05685 | 21.2x below dataset median |
| 2507.08005 | Unraveling the Potential of Diffusion Models in  | D&D | idity3D | DecompOPT | 0 | 0.009 | zero value against positive dataset median |
| 2510.08450 | : Mitigating by Increasing Storage Capacity | D&D | MSE | A-DGN | 0.00028 | 0.010275 | 36.7x below dataset median |
| 2510.08450 | : Mitigating by Increasing Storage Capacity | D&D | MSE | gLSTM | 0.00019 | 0.010275 | 54.1x below dataset median |
| 2510.08450 | : Mitigating by Increasing Storage Capacity | SSSP | MSE | A-DGN | 4e-07 | 0.002 | 5000.0x below dataset median |
| 2510.08450 | : Mitigating by Increasing Storage Capacity | SSSP | MSE | GCNII | 7.4e-06 | 0.002 | 270.3x below dataset median |
| 2510.08450 | : Mitigating by Increasing Storage Capacity | SSSP | MSE | gLSTM | 1.5e-06 | 0.002 | 1333.3x below dataset median |
| 2510.10211 | Transport-Coupled Bayesian Flows for Molecular G | ZINC | NSPDK | EDP-GNN | 0.0485 | 0.0018 | 26.9x above dataset median |
| 2601.02662 | When Prompting Meets Spiking: Graph Sparse Promp | ogbn-arxiv | Accuracy | GraphCL All-in-One | 0.0339 | 0.716 | 21.1x below dataset median |