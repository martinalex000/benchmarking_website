---
title: Skipped Papers
type: dev
description: Papers rejected by LLM screening
---

## Skipped Papers

This page shows papers that were identified but rejected by the LLM screening pipeline. The screening happens in two stages: Stage 1 filters for general relevance to graph neural network research, and Stage 2 checks whether the paper evaluates results on known benchmarks. Papers that pass both stages proceed to full result extraction.

### Stage 1 Rejections: 25

Stage 1 rejects papers that are deemed not relevant to graph neural networks. These are typically papers in unrelated fields that happened to mention GNNs or graph concepts, but don't focus on benchmarking graph neural network models.

| ArXiv | Title | Reason |
|-------|-------|--------|
| 2502.02479 | Using Random Noise Equivariantly to Boos | The paper mentions experiments demonstrating performance on 'node-level, link-le |
| 2411.17429 | Graph Rewiring in GNNs to Mitigate Over- | This is a survey paper that reviews existing graph rewiring techniques without p |
| 2411.05274 | Distributed-Order Fractional Graph Opera | The paper mentions empirical evaluations across 'a range of graph learning tasks |
| 2410.09118 | FSW-GNN: A Bi-Lipschitz WL-Equivalent Gr | The paper mentions empirical evaluation but does not specify which standard data |
| 2506.04653 | The Oversmoothing Fallacy: A Misguided N | The paper is a position paper that discusses theoretical aspects of GNNs and doe |
| 2506.01231 | Towards Efficient Few-shot Graph Neural  | The paper mentions experimental results and SOTA performance but does not specif |
| 2505.20215 | Dependency Parsing is More Parameter-Eff | Paper mentions experiments on 'semantic and syntactic dependency parsing in mult |
| 2505.18728 | Message-Passing State-Space Models: Impr | Paper mentions validation across 'wide range of tasks' including node classifica |
| 2505.18088 | Early-Exit Graph Neural Networks | The paper mentions experiments and competitive results but does not specify whic |
| 2505.15547 | Oversmoothing, Oversquashing, Heterophil | The paper focuses on conceptual analysis and refuting common beliefs in graph ML |
| 2505.14606 | Electrostatics from Laplacian Eigenbasis | The paper focuses on introducing a new method (Phi-Module) for learning electros |
| 2505.12880 | AdS-GNN -- a Conformally Equivariant Gra | Paper focuses on theoretical development of AdS-GNN and demonstrates performance |
| 2505.11346 | What Can We Learn From MIMO Graph Convol | The paper focuses on deriving and analyzing MIMO graph convolutions theoreticall |
| 2504.19649 | Intelligent4DSE: Optimizing High-Level S | The paper evaluates its methods on a specific domain (HLS DSE) but does not ment |
| 2504.10917 | Towards A Universal Graph Structural Enc | The paper mentions 'synthetic and real-world datasets' but does not specify any  |
| 2504.08802 | InfoGain Wavelets: Furthering the Design | The paper mentions 'graph classification experiments' but does not specify which |
| 2502.16533 | A Survey of Graph Transformers: Architec | This is a survey paper that reviews existing work on graph transformers without  |
| 2502.16454 | MAPN: Enhancing Heterogeneous Sparse Gra | The paper mentions 'extensive experiments across diverse datasets' but does not  |
| 2502.14546 | Position: Graph Learning Will Lose Relev | This is a position paper that critiques current benchmarking practices rather th |
| 2408.05391 | SAMSA: Efficient Transformer for Many Da | While the paper mentions 'many benchmarks' and reports competitive SOTA results, |
| 2402.02287 | Future Directions in the Theory of Graph | The paper is explicitly identified as a 'position paper' arguing for theoretical |
| 2604.00199 | QUEST: A robust attention formulation us | The paper focuses on Transformer attention mechanisms for vision and general dee |
| 2512.12642 | Torch Geometric Pool: the PyTorch librar | This is a software library/tooling paper (Torch Geometric Pool) providing a unif |
| 2310.11829 | Graph Foundation Models: Concepts, Oppor | This is a survey/review paper discussing concepts and opportunities of Graph Fou |
| 2309.08478 | Current and future directions in network | This is a perspective/roadmap paper on network biology. It discusses research di |

### Stage 2 Rejections: 0

Stage 2 rejects papers that are relevant to GNNs but don't evaluate models on any known benchmarks. This includes position papers, theoretical papers, survey papers, or papers that only propose new datasets without evaluating existing models. The 'Datasets Found' column shows how many benchmark datasets the LLM detected in the paper (if any).


### No Datasets/Results Discovered: 0

These papers passed Stage 2 screening (were deemed relevant and benchmarking-focused) but the extraction pipeline was unable to discover any benchmark datasets or results. This could mean: the paper's results are too noisy for extraction, the datasets used have non-standard names, or the extraction model failed to parse the paper format. These papers may still be worth investigating manually.
