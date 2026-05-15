---
title: Paper Extraction Status
type: dev
description: Overview of extraction status
---

## Paper Extraction Status

**Total:** 224 papers

This page tracks the extraction pipeline status for all papers in the benchmarking dataset. Each paper goes through several stages: first it must be downloaded from arXiv, then the full text is extracted and parsed (either from HTML, LaTeX source, or PDF), and finally results are extracted using an LLM. The extraction model shown indicates which LLM (if any) was used to extract results.

### Downloaded (6)

Papers that have been downloaded but not yet processed for extraction.

| ArXiv | Title | Model |
|-------|-------|-------|
| 2309.00367 | Where Did the Gap Go?\\ Reassessing the ... | — |
| 2401.01233 | GEN: A Practical Alternative to Graph Tr... | — |
| 2402.00789 | Graph-Mamba: Towards Long-Range Graph Se... | — |
| 2406.18380 | KAGNNs: Kolmogorov-Arnold Networks meet ... | — |
| 2512.12642 | Torch Geometric Pool: the PyTorch librar... | — |
| 2604.00199 | QUEST: A robust attention formulation us... | — |

### Extracted (211)

Papers with successfully extracted results. These papers contribute to the leaderboards.

| ArXiv | Title | Model |
|-------|-------|-------|
| 2102.08786 | arXiv:2102.08786 | qwen3.6-35b-a3b |
| 2205.12454 | arXiv:2205.12454 | qwen3.6-35b-a3b |
| 2206.08164 | LRGB | qwen3.6-35b-a3b |
| 2208.03471 | arXiv:2208.03471 | qwen3.6-35b-a3b |
| 2209.10818 | arXiv:2209.10818 | qwen3.6-35b-a3b |
| 2210.07606 | Revisiting Heterophily For Graph Neural ... | qwen3.6-35b-a3b |
| 2210.13148 | arXiv:2210.13148 | qwen3.6-35b-a3b |
| 2211.15779 | arXiv:2211.15779 | qwen3.6-35b-a3b |
| 2212.02374 | arXiv:2212.02374 | qwen3.6-35b-a3b |
| 2212.13350 | arXiv:2212.13350 | qwen3.6-35b-a3b |
| 2301.10857 | arXiv:2301.10857 | qwen3.6-35b-a3b |
| 2301.11956 | arXiv:2301.11956 | qwen3.6-35b-a3b |
| 2302.06835 | arXiv:2302.06835 | qwen3.6-35b-a3b |
| 2302.08647 | arXiv:2302.08647 | qwen3.6-35b-a3b |
| 2302.08671 | arXiv:2302.08671 | qwen3.6-35b-a3b |
| 2302.08811 | arXiv:2302.08811 | qwen3.6-35b-a3b |
| 2303.00613 | arXiv:2303.00613 | qwen3.6-35b-a3b |
| 2303.06147 | arXiv:2303.06147 | qwen3.6-35b-a3b |
| 2304.10933 | arXiv:2304.10933 | qwen3.6-35b-a3b |
| 2305.08018 | arXiv:2305.08018 | qwen3.6-35b-a3b |
| 2305.17589 | arXiv:2305.17589 | qwen3.6-35b-a3b |
| 2306.02866 | Learning Probabilistic Symmetrization fo... | qwen3.6-35b-a3b |
| 2306.03561 | CIN++: Enhancing Topological Message Pas... | qwen3.6-35b-a3b |
| 2306.04667 | Neural Embeddings for Protein Graphs | qwen3.6-35b-a3b |
| 2306.05955 | Path Neural Networks: Expressive and Acc... | qwen3.6-35b-a3b |
| 2306.08277 | : Frugal Spatio-temporal Forecasting on ... | qwen3.6-35b-a3b |
| 2306.08385 | Align All the Nodes: Scalable Learning o... | qwen3.6-35b-a3b |
| 2306.10759 | SGFormer: Simplifying and Empowering Tra... | qwen3.6-35b-a3b |
| 2306.11681 | arXiv:2306.11681 | qwen3.6-35b-a3b |
| 2307.03393 | Exploring the Potential of Large Languag... | qwen3.6-35b-a3b |
| 2307.07107 | Graph Positional and Structural Encoder | qwen3.6-35b-a3b |
| 2307.09660 | Neural Priority Queues for Graph Neural ... | qwen3.6-35b-a3b |
| 2308.11129 | Enhancing Graph Transformers with Hierar... | qwen3.6-35b-a3b |
| 2309.04082 | Curve Your Attention: Mixed-Curvature Tr... | qwen3.6-35b-a3b |
| 2309.04941 | Distance-Restricted Folklore Weisfeiler-... | qwen3.6-35b-a3b |
| 2309.09384 | Mitigating Over-Smoothing and Over-Squas... | qwen3.6-35b-a3b |
| 2309.16014 | Graph-level Representation Learning with... | qwen3.6-35b-a3b |
| 2309.16685 | Target-aware Variational Auto-encoders f... | qwen3.6-35b-a3b |
| 2310.01267 | Cooperative Graph Neural Networks | qwen3.6-35b-a3b |
| 2310.01618 | Operator Learning Meets Numerical Analys... | qwen3.6-35b-a3b |
| 2310.01668 | Locality-Aware Graph Rewiring in GNNs | qwen3.6-35b-a3b |
| 2310.01704 | Transformers are efficient hierarchical ... | qwen3.6-35b-a3b |
| 2310.02156 | Probabilistically Rewired Message-Passin... | qwen3.6-35b-a3b |
| 2310.02980 | Never Train from Scratch: Fair Compariso... | qwen3.6-35b-a3b |
| 2310.03274 | Fragment-based Pretraining and Finetunin... | qwen3.6-35b-a3b |
| 2310.05174 | GSLB: The Graph Structure Learning Bench... | qwen3.6-35b-a3b |
| 2310.07430 | Non-backtracking Graph Neural Networks | qwen3.6-35b-a3b |
| 2310.10121 | arXiv:2310.10121 | qwen3.6-35b-a3b |
| 2310.15543 | Symmetry-preserving graph attention netw... | qwen3.6-35b-a3b |
| 2310.18777 | Improving Compositional Generalization u... | qwen3.6-35b-a3b |
| 2310.19285 | Facilitating Graph Neural Networks with ... | qwen3.6-35b-a3b |
| 2310.20519 | Enhancing Graph Neural Networks with \\ ... | qwen3.6-35b-a3b |
| 2311.01276 | Neural Atoms: Propagating Long-range \\ ... | qwen3.6-35b-a3b |
| 2311.04653 | Hybrid Focal and Full-Range Attention Ba... | qwen3.6-35b-a3b |
| 2311.05964 | Multiscale Neural Operators for Solving ... | qwen3.6-35b-a3b |
| 2311.07073 | arXiv:2311.07073 | qwen3.6-35b-a3b |
| 2311.07966 | Higher-Order Expander Graph Propagation | qwen3.6-35b-a3b |
| 2311.12399 | arXiv:2311.12399 | qwen3.6-35b-a3b |
| 2311.14864 | Effective Structural Encodings via Local... | qwen3.6-35b-a3b |
| 2311.16605 | arXiv:2311.16605 | qwen3.6-35b-a3b |
| 2312.01538 | Recurrent Distance Filtering for Graph R... | qwen3.6-35b-a3b |
| 2312.04234 | Graph Convolutions Enrich the Self-Atten... | qwen3.6-35b-a3b |
| 2312.09676 | arXiv:2312.09676 | qwen3.6-35b-a3b |
| 2312.11109 | Graph Transformers for Large Graphs | qwen3.6-35b-a3b |
| 2312.11730 | Stronger Graph Transformer with Regulari... | qwen3.6-35b-a3b |
| 2401.03350 | Accurate and Scalable Estimation of Epis... | qwen3.6-35b-a3b |
| 2401.14580 | Design Your Own Universe: A Physics-Info... | qwen3.6-35b-a3b |
| 2401.17791 | Graph Transformers without Positional En... | qwen3.6-35b-a3b |
| 2401.18054 | Benchmarking Sensitivity of Continual Gr... | qwen3.6-35b-a3b |
| 2402.04821 | E(3)-Equivariant Mesh Neural Networks | qwen3.6-35b-a3b |
| 2402.08450 | Subgraphormer: Unifying Subgraph GNNs an... | qwen3.6-35b-a3b |
| 2402.08678 | Graph Mamba: Towards Learning on Graphs ... | qwen3.6-35b-a3b |
| 2402.10793 | An end-to-end attention-based approach f... | qwen3.6-35b-a3b |
| 2403.06687 | arXiv:2403.06687 | qwen3.6-35b-a3b |
| 2403.11199 | arXiv:2403.11199 | qwen3.6-35b-a3b |
| 2403.13749 | Weisfeiler and Leman Go Loopy: A New Hie... | qwen3.6-35b-a3b |
| 2403.16030 | VCR-Graphormer: A Mini-batch Graph Trans... | qwen3.6-35b-a3b |
| 2404.00477 | DE-HNN: An effective neural model for Ci... | qwen3.6-35b-a3b |
| 2404.03380 | On the Theoretical Expressive Power and ... | qwen3.6-35b-a3b |
| 2404.09774 | RandAlign: A Parameter-Free Method for R... | qwen3.6-35b-a3b |
| 2404.13604 | arXiv:2404.13604 | qwen3.6-35b-a3b |
| 2405.02795 | Graph as Point Set | qwen3.6-35b-a3b |
| 2405.03481 | AnchorGT: Efficient and Flexible Attenti... | qwen3.6-35b-a3b |
| 2405.11951 | Distinguished In Uniform:\\ Self-Attenti... | qwen3.6-35b-a3b |
| 2405.13526 | Understanding Virtual Nodes: Oversquashi... | qwen3.6-35b-a3b |
| 2405.13806 | A General Graph Spectral Wavelet Convolu... | qwen3.6-35b-a3b |
| 2405.15540 | Bundle Neural Networks \\ for message di... | qwen3.6-35b-a3b |
| 2405.17311 | Probabilistic Graph Rewiring via Virtual... | qwen3.6-35b-a3b |
| 2405.17404 | Spectral Greedy Coresets for Graph Neura... | qwen3.6-35b-a3b |
| 2405.19121 | Spatio-Spectral Graph Neural Networks | qwen3.6-35b-a3b |
| 2405.21061 | arXiv:2405.21061 | qwen3.6-35b-a3b |
| 2406.01977 | arXiv:2406.01977 | qwen3.6-35b-a3b |
| 2406.02269 | arXiv:2406.02269 | qwen3.6-35b-a3b |
| 2406.02740 | Long Range Propagation on Continuous-Tim... | qwen3.6-35b-a3b |
| 2406.03386 | Learning Long Range Dependencies on Grap... | qwen3.6-35b-a3b |
| 2406.03671 | PANDA: Expanded Width-Aware Message Pass... | qwen3.6-35b-a3b |
| 2406.04377 | Combining Graph Neural Network and Mamba... | qwen3.6-35b-a3b |
| 2406.05815 | What Can We Learn from State Space Model... | qwen3.6-35b-a3b |
| 2406.06984 | On the Stability of Multiset and Graph N... | qwen3.6-35b-a3b |
| 2406.08993 | Classic GNNs are Strong Baselines:\\ Rea... | glm-4.7 |
| 2406.09291 | A Flexible, Equivariant Framework for Su... | qwen3.6-35b-a3b |
| 2406.09639 | TGB 2.0: A Benchmark for Learning on Tem... | qwen3.6-35b-a3b |
| 2406.12059 | A Scalable and Effective Alternative to ... | qwen3.6-35b-a3b |
| 2406.16321 | Mosaic of Modalities: A Comprehensive Be... | qwen3.6-35b-a3b |
| 2406.16722 | center Venturing into Uncharted Waters: ... | qwen3.6-35b-a3b |
| 2407.00494 | Graph Neural Networks Gone Hogwild | qwen3.6-35b-a3b |
| 2407.02758 | Differential Encoding for Improved Repre... | qwen3.6-35b-a3b |
| 2407.04236 | Graph Pooling via Ricci Flow | qwen3.6-35b-a3b |
| 2407.05649 | Greener GRASS: Enhancing GNNs with \ , R... | qwen3.6-35b-a3b |
| 2407.08762 | arXiv:2407.08762 | qwen3.6-35b-a3b |
| 2407.12136 | Molecular Topological Profile (MOLTOP) -... | qwen3.6-35b-a3b |
| 2407.12419 | Dirac--Bianconi Graph Neural Networks --... | qwen3.6-35b-a3b |
| 2407.18480 | Scalable Graph Compressed Convolutions | qwen3.6-35b-a3b |
| 2408.05822 | arXiv:2408.05822 | Kimi-K2.6 |
| 2408.12169 | arXiv:2408.12169 | Kimi-K2.6 |
| 2409.08023 | arXiv:2409.08023 | Kimi-K2.6 |
| 2409.11504 | Preventing Representational Rank Collaps... | Kimi-K2.6 |
| 2409.19117 | Range-aware Positional Encoding via\\ Hi... | Kimi-K2.6 |
| 2409.19414 | arXiv:2409.19414 | Kimi-K2.6 |
| 2409.20212 | arXiv:2409.20212 | Kimi-K2.6 |
| 2410.03424 | Cayley Graph Propagation | Kimi-K2.6 |
| 2410.05499 | Unitary convolutions for learning on gra... | Kimi-K2.6 |
| 2410.05593 | When Graph Neural Networks Meet Dynamic ... | MiniMaxAI/MiniMax-M2.5 |
| 2410.05697 | Diffusing to the Top: Boost Graph Neural... | qwen3.6-35b-a3b |
| 2410.06460 | A Benchmark on Directed Graph Representa... | MiniMaxAI/MiniMax-M2.5 |
| 2410.09737 | Towards Stable, Globally Expressive Grap... | MiniMaxAI/MiniMax-M2.5 |
| 2410.13798 | Learning Graph Quantized Tokenizers | MiniMaxAI/MiniMax-M2.5 |
| 2410.18676 | Homomorphism Counts as Structural \\ Enc... | MiniMaxAI/MiniMax-M2.5 |
| 2410.20516 | A Cosmic-Scale Benchmark for Symmetry-Pr... | MiniMaxAI/MiniMax-M2.5 |
| 2410.23686 | Towards Dynamic Message Passing on Graph... | MiniMaxAI/MiniMax-M2.5 |
| 2411.15671 | Best of Both Worlds: Advantages of Hybri... | MiniMaxAI/MiniMax-M2.5 |
| 2411.17296 | GrokFormer: Graph Fourier Kolmogorov-Arn... | MiniMaxAI/MiniMax-M2.5 |
| 2412.01519 | : Linear Complexity Graph Transformers \... | MiniMaxAI/MiniMax-M2.5 |
| 2412.03783 | Expressivity of Representation Learning ... | MiniMaxAI/MiniMax-M2.5 |
| 2412.07188 | Graph Neural Networks Are More Than Filt... | MiniMaxAI/MiniMax-M2.5 |
| 2412.17609 | arXiv:2412.17609 | MiniMaxAI/MiniMax-M2.5 |
| 2501.03113 | Balancing Efficiency and Expressiveness:... | MiniMaxAI/MiniMax-M2.5 |
| 2501.09821 | bnpool: Bayesian Nonparametric Pooling f... | MiniMaxAI/MiniMax-M2.5 |
| 2501.17901 | Molecular Fingerprints Are Strong Models... | MiniMaxAI/MiniMax-M2.5 |
| 2501.18739 | Beyond Message Passing: Neural Graph Pat... | MiniMaxAI/MiniMax-M2.5 |
| 2502.00282 | GraphMinNet: Learning Dependencies in Gr... | MiniMaxAI/MiniMax-M2.5 |
| 2502.01122 | Learning Efficient Positional Encodings ... | MiniMaxAI/MiniMax-M2.5 |
| 2502.02379 | No Metric to Rule Them All: Toward Princ... | MiniMaxAI/MiniMax-M2.5 |
| 2502.07364 | Effects of Dropout on Performance in \\ ... | MiniMaxAI/MiniMax-M2.5 |
| 2502.09263 | Can Classic GNNs Be Strong Baselines for... | MiniMaxAI/MiniMax-M2.5 |
| 2502.09365 | Simple Path Structural Encoding for Grap... | MiniMaxAI/MiniMax-M2.5 |
| 2502.09570 | Enhancing the Utility of Higher-Order In... | MiniMaxAI/MiniMax-M2.5 |
| 2502.10818 | On Vanishing Gradients, Over-Smoothing, ... | qwen3.6-35b-a3b |
| 2503.09008 | Towards Quantifying Long-Range Interacti... | MiniMaxAI/MiniMax-M2.5 |
| 2504.12588 | Plain Transformers Can be Powerful Graph... | MiniMaxAI/MiniMax-M2.5 |
| 2505.15405 | HOPSE: Scalable Higher-Order Positional ... | MiniMaxAI/MiniMax-M2.5 |
| 2505.23185 | Improving the Effective Receptive Field ... | MiniMaxAI/MiniMax-M2.5 |
| 2505.23345 | Graph Positional Autoencoders as Self-su... | MiniMaxAI/MiniMax-M2.5 |
| 2505.23875 | A Benchmark Dataset for Graph Regression... | MiniMaxAI/MiniMax-M2.5 |
| 2506.04765 | OpenGT: A Comprehensive Benchmark For Gr... | qwen3.6-35b-a3b |
| 2506.05393 | Are Large Language Models Good Temporal ... | qwen3.6-35b-a3b |
| 2506.05971 | On Measuring Long-Range Interactions in ... | qwen3.6-35b-a3b |
| 2506.07624 | Return of ChebNet: Understanding and Imp... | qwen3.6-35b-a3b |
| 2506.08618 | HSG-12M | qwen3.6-35b-a3b |
| 2506.11869 | How do Probabilistic Graphical Models an... | qwen3.6-35b-a3b |
| 2506.13912 | Density-aware Walks for Coordinated Camp... | qwen3.6-35b-a3b |
| 2506.14098 | Toward a Graph Foundation Model: \\ Pre-... | qwen3.6-35b-a3b |
| 2506.19862 | DualEquiNet RNA Benchmarks | qwen3.6-35b-a3b |
| 2506.22727 | Convergent Privacy Framework for Multi-l... | qwen3.6-35b-a3b |
| 2507.00647 | Cooperative Sheaf Neural Networks | qwen3.6-35b-a3b |
| 2507.03707 | CosmoBench | qwen3.6-35b-a3b |
| 2507.19382 | Learning Long-Range Representations with... | qwen3.6-35b-a3b |
| 2508.05070 | Tango: Graph Neural Dynamics via Learned... | qwen3.6-35b-a3b |
| 2508.10651 | Graph Learning via Logic-Based Weisfeile... | qwen3.6-35b-a3b |
| 2508.11390 | A Remedy for Over-Squashing in Graph Lea... | qwen3.6-35b-a3b |
| 2508.14097 | Non-Dissipative Graph Propagation for No... | qwen3.6-35b-a3b |
| 2508.17630 | Quantum Graph Attention Network: A Novel... | qwen3.6-35b-a3b |
| 2508.19071 | Dynamic Triangulation-Based Graph Rewiri... | qwen3.6-35b-a3b |
| 2509.01254 | What Expressivity Theory Misses:\\ Messa... | qwen3.6-35b-a3b |
| 2509.06743 | Long-Range Graph Wavelet Networks | qwen3.6-35b-a3b |
| 2509.06777 | Asynchronous Message Passing for Address... | qwen3.6-35b-a3b |
| 2509.22100 | SHAKE-GNN: Scalable Hierarchical Kirchho... | qwen3.6-35b-a3b |
| 2509.22259 | Rotary Position Encodings for Graphs | qwen3.6-35b-a3b |
| 2510.02259 | Transformers Discover Molecular Structur... | qwen3.6-35b-a3b |
| 2510.02565 | On The Expressive Power of GNN Derivativ... | qwen3.6-35b-a3b |
| 2510.07716 | Computationally-efficient Graph Modeling... | qwen3.6-35b-a3b |
| 2510.08450 | gLSTM: Mitigating Over-Squashing by Incr... | qwen3.6-35b-a3b |
| 2510.12111 | Chimera: State Space Models Beyond Seque... | qwen3.6-35b-a3b |
| 2510.14336 | DARTS-GT: Differentiable Architecture Se... | qwen3.6-35b-a3b |
| 2510.22520 | Random Search Neural Networks for Effici... | qwen3.6-35b-a3b |
| 2511.03824 | Sketch-Augmented Features Improve Learni... | qwen3.6-35b-a3b |
| 2511.08028 | Generalizable Insights for Graph Transfo... | qwen3.6-35b-a3b |
| 2511.16767 | When Structure Doesn’t Help: LLMs Do Not... | qwen3.6-35b-a3b |
| 2511.20406 | Short-Range Oversquashing | qwen3.6-35b-a3b |
| 2512.04475 | GraphBench | qwen3.6-35b-a3b |
| 2512.14619 | ParaFormer: A Generalized PageRank Graph... | qwen3.6-35b-a3b |
| 2512.15549 | Photonics-Enhanced Graph Convolutional N... | qwen3.6-35b-a3b |
| 2512.17762 | ECHO Benchmark | qwen3.6-35b-a3b |
| 2601.01387 | Power Flow Benchmarks | qwen3.6-35b-a3b |
| 2601.07419 | Position: Don't be Afraid of Over-Smooth... | qwen3.6-35b-a3b |
| 2601.18917 | GraIP: A Benchmarking Framework For Neur... | qwen3.6-35b-a3b |
| 2601.19094 | FloydNet: A Learning Paradigm for Global... | qwen3.6-35b-a3b |
| 2602.02268 | HopFormer: Sparse Graph Transformers \ E... | qwen3.6-35b-a3b |
| 2602.15239 | Size Transferability of Graph Transforme... | qwen3.6-35b-a3b |
| 2602.17893 | COMBA: Cross Batch Aggregation for Learn... | qwen3.6-35b-a3b |
| 2602.18837 | L2G-Net: Local to Global Spectral Graph ... | qwen3.6-35b-a3b |
| 2602.21092 | Probing Graph Neural Network Activation ... | qwen3.6-35b-a3b |
| 2603.00599 | Heterophily-Agnostic Hypergraph Neural N... | qwen3.6-35b-a3b |
| 2603.27529 | Cross-attentive Cohesive Subgraph Embedd... | qwen3.6-35b-a3b |
| 2604.03815 | k-Maximum Inner Product Attention for Gr... | qwen3.6-35b-a3b |
| 2604.06336 | BiScale-GTR: Fragment-Aware Graph Transf... | qwen3.6-35b-a3b |
| 2604.17324 | SigGate-GT: Taming Over-Smoothing in Gra... | qwen3.6-35b-a3b |
| 2604.24293 | Latent-Hysteresis Graph ODEs: Modeling C... | qwen3.6-35b-a3b |
| 2605.04834 | Bridging Input Feature Spaces Towards Gr... | qwen3.6-35b-a3b |
| 2605.05689 | GCCM: Enhancing Generative Graph Predict... | qwen3.6-35b-a3b |
| 2605.06462 | Invariant-Based Diagnostics for Graph Be... | qwen3.6-35b-a3b |

### Pending (7)

Papers that have been identified but not yet downloaded from arXiv.

| ArXiv | Title | Model |
|-------|-------|-------|
| 1703.00564 | MoleculeNet | — |
| 2002.01680 | Heterogeneous Graph Benchmarks | — |
| 2003.00982 | GNNBenchmark | — |
| 2005.00687 | OGB-Link | — |
| 2103.09430 | OGB-LSC | — |
| 2110.14446 | LINKX Benchmarks | — |
| 2312.16560 | Algorithmic Graph Tasks | — |
