---
title: Size Transferability of Graph Transformers with Convolutional Positional Encodings
arxiv_id: '2602.15239'
authors: []
published_date: Feb 2026
abstract: Transformers have achieved remarkable success across domains, motivating
  the rise of Graph Transformers (GTs) as attention-based architectures for graph-structured
  data. A key design choice in GTs is the use of Graph Neural Network (GNN)-based
  positional encodings to incorporate structural information. In this work, we study
  GTs through the lens of manifold limit models for graph sequences and establish
  a theoretical connection between GTs with GNN positional encodings and Manifold
  Neural Networks (MNNs). Building on transferability results for GNNs under manifold
  convergence, we show that GTs inherit transferability guarantees from their positional
  encodings. In particular, GTs trained on small graphs provably generalize to larger
  graphs under mild assumptions. We complement our theory with extensive experiments
  on standard graph benchmarks, demonstrating that GTs exhibit scalable behavior on
  par with GNNs. To further show the efficiency in a real-world scenario, we implement
  GTs for shortest path distance estimation over terrains to better illustrate the
  efficiency of the transferable GTs. Our results provide new insights into the understanding
  of GTs and suggest practical directions for efficient training of GTs in large-scale
  settings.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
proposed_models:
- GT + Mask + RPEARL
mrr: 0.0667
results:
- &id001
  dataset: snap-patents
  rows:
  - model: MRS-Dir-GCN_DA
    value: 0.7472
    std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: Dir-GNN
    value: 0.7395
    std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: LargeGT-full
    value: 0.7021
    std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11109'
    title: Graph Transformers for Large Graphs
    date: Dec 2023
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: GT + Mask + RPEARL
    value: 0.46549999999999997
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 15
    is_best: false
  - model: GT + Mask
    value: 0.3969
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 20
    is_best: false
  - model: GT + RPEARL
    value: 0.34630000000000005
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 21
    is_best: false
  - model: GT (no PE)
    value: 0.31329999999999997
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 23
    is_best: false
  - model: GT + Mask + RE
    value: 0.31010000000000004
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 24
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: LINKX Benchmarks
  datasets:
  - *id001
single_proposed_model: GT + Mask + RPEARL
main_figure: /figures/2602.15239/main_figure.png
---

