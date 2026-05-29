---
title: Skipped Papers
type: dev
description: Papers rejected by LLM screening
---

## Skipped Papers

This page shows papers that were identified but rejected by the LLM screening pipeline. The screening happens in two stages: Stage 1 filters for general relevance to graph neural network research, and Stage 2 checks whether the paper evaluates results on known benchmarks. Papers that pass both stages proceed to full result extraction.

### Stage 1 Rejections: 40

Stage 1 rejects papers that are deemed not relevant to graph neural networks. These are typically papers in unrelated fields that happened to mention GNNs or graph concepts, but don't focus on benchmarking graph neural network models.

| ArXiv | Title | Reason |
|-------|-------|--------|
| 2404.13604 | Formatting Instructions For NeurIPS 2024 | This is a formatting instruction template for a conference submission, not a res |
| 1706.03762 | Attention Is All You Need | This paper introduces the Transformer architecture for sequence transduction (NL |
| 2302.02941 | arXiv:2302.02941 | The paper is explicitly stated as a 'theoretical work' that proves properties ab |
| 1912.01703 | PyTorch: An Imperative Style, High-Performance Deep Learning Library | This is a systems/framework paper describing the PyTorch library itself. While i |
| 2010.11929 | An Image is Worth 16x16 Words: Transformers for... | This is a computer vision paper (Vision Transformer) using image classification  |
| 2407.03125 | Foundations and Frontiers of Graph Learning Theory | This is a survey/theoretical overview paper focusing on theoretical foundations  |
| 2506.05971 | arXiv:2506.05971 | The paper is theoretical/methodological, focusing on formalizing a 'range measur |
| 2505.15547 | Oversmoothing, ``Oversquashing'', Heterophily, Long-Range, and more: Demystifying Common... | The paper is a theoretical/position paper focused on clarifying conceptual belie |
| 2202.11097 | Message passing all the way up | The paper is explicitly identified as a position paper arguing against terminolo |
| 2303.00613 | Formatting Instructions for ICLR 2023 Conference Submissions | This is a formatting instruction document for conference submissions, not a rese |
| 1806.01261 | Relational inductive biases, deep learning, and graph networks | This is a position/review paper introducing the 'graph network' architecture con |
| 1907.03199 | What Graph Neural Networks Cannot Learn: Depth vs... | The paper is purely theoretical, focusing on expressive power, Turing universali |
| 2201.12884 | A Theoretical Comparison of Graph Neural Network Extensions | Purely theoretical paper focusing on expressivity comparisons via mathematical c |
| 1901.09342 | arXiv:1901.09342 | Purely theoretical paper on universality of invariant networks; no experiments o |
| 1512.03385 | Deep Residual Learning for Image Recognition | Paper is about image recognition (CNNs) on ImageNet and CIFAR-10, not graph mach |
| 2402.02287 | Directions in the Theory of Graph Machine Learning | The paper is explicitly identified as a 'position paper' arguing for a shift in  |
| 2602.10031 | arXiv:2602.10031 | Purely theoretical and conceptual paper arguing for unification of MPNN and spec |
| 2002.06157 | Generalization and Representational Limits of Graph Neural Networks | The paper is purely theoretical, focusing on mathematical proofs of representati |
| 1905.04943 | Universal Invariant and Equivariant Graph Neural Networks | Purely theoretical paper proving universality theorems for invariant and equivar |
| 1502.03167 | Batch Normalization: Accelerating Deep Network Training by Reducing... | Paper focuses on image classification (Computer Vision) using ImageNet. It does  |
| 2406.04336 | arXiv:2406.04336 | The paper is purely theoretical, focusing on the expressive power and unificatio |
| 2005.03675 | Machine Learning on Graphs: A Model and Comprehensive... | This is a theoretical survey and taxonomy paper proposing a unifying framework ( |
| 2006.13318 | arXiv:2006.13318 | The paper is purely theoretical, focusing on analyzing the over-smoothing effect |
| 1810.04805 | BERT: Pre-training of Deep Bidirectional Transformers for Language... | This is a natural language processing (NLP) paper focused on text transformers.  |
| 1709.05584 | Representation Learning on Graphs: Methods and Applications | This is a conceptual review/survey paper. While it discusses methods and applica |
| 2402.02216 | arXiv:2402.02216 | This is a perspective/theoretical paper proposing a 'graph vocabulary' concept f |
| 2502.14546 | arXiv:2502.14546 | The abstract explicitly identifies the paper as a 'position paper' calling for a |
| 2205.09702 | Parallel and Distributed Graph Neural Networks: An In-Depth... | The paper is a theoretical concurrency analysis and taxonomy of GNN parallelism. |
| 1211.0053 | The Emerging Field of Signal Processing on Graphs... | This is a tutorial/overview paper on signal processing on graphs (SPG). It surve |
| 0912.3848 | Wavelets on Graphs via Spectral Graph Theory | The paper proposes a theoretical method for constructing spectral graph wavelets |
| 2007.12035 | The expressive power of kth-order invariant graph networks | Purely theoretical paper proving expressivity bounds between k-IGNs and k-WL; no |
| 1607.06450 | Layer Normalization | This paper introduces Layer Normalization, a general neural network optimization |
| 1811.04801 | On Weisfeiler-Leman Invariance: Subgraph Counts and Related Graph... | Purely theoretical paper on Weisfeiler-Leman invariance and subgraph counts. No  |
| 2605.08291 | Graph Computation Meets Circuit Algebra: A Task-Aligned Analysis... | The paper is a position/analysis paper reviewing GNN applications in EDA. It exp |
| 2305.16102 | Demystifying Oversmoothing in Attention-Based Graph Neural Networks | The paper is purely theoretical, focusing on mathematical analysis of oversmooth |
| 2204.10037 | AAAI Press Formatting Instructions for Authors Using ---... | This is a formatting guide for AAAI submissions, not a research paper with bench |
| 2204.07697 | Theory of Graph Neural Networks: Representation and Learning | The paper is a theoretical survey summarizing approximation and learning propert |
| 2007.14062 | Big Bird: Transformers for Longer Sequences | Paper focuses on NLP transformers and sequence modeling, not graph machine learn |
| 1310.4546 | Distributed Representations of Words and Phrases and their... | This paper introduces Word2Vec, a method for learning word embeddings from text  |
| 1905.10261 | Approximation Ratios of Graph Neural Networks for Combinatorial... | Purely theoretical paper establishing approximation ratios for GNNs on combinato |

### Stage 2 Rejections: 0

Stage 2 rejects papers that are relevant to GNNs but don't evaluate models on any known benchmarks. This includes position papers, theoretical papers, survey papers, or papers that only propose new datasets without evaluating existing models. The 'Datasets Found' column shows how many benchmark datasets the LLM detected in the paper (if any).


### No Datasets/Results Discovered: 0

These papers passed Stage 2 screening (were deemed relevant and benchmarking-focused) but the extraction pipeline was unable to discover any benchmark datasets or results. This could mean: the paper's results are too noisy for extraction, the datasets used have non-standard names, or the extraction model failed to parse the paper format. These papers may still be worth investigating manually.
