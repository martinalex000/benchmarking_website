---
title: Graph Transformers for Large Graphs
arxiv_id: '2312.11109'
authors: []
published_date: Dec 2023
abstract: 'Transformers have recently emerged as powerful neural networks for graph
  learning, showcasing state-of-the-art performance on several graph property prediction
  tasks. However, these results have been limited to small-scale graphs, such as ligand
  molecules with fewer than a hundred atoms, where the computational feasibility of
  the global attention mechanism is possible. The next goal is to scale up these architectures
  to handle very large graphs on the scale of millions or even billions of nodes.
  With large-scale graphs, global attention learning is proven impractical due to
  its quadratic complexity w.r.t. the number of nodes. On the other hand, neighborhood
  sampling techniques become essential to manage large graph sizes, yet finding the
  optimal trade-off between speed and accuracy with sampling techniques remains challenging.
  This work advances representation learning on single large-scale graphs with a focus
  on identifying model characteristics and critical design constraints for developing
  scalable graph transformer (GT) architectures. We argue such GT requires layers
  that can adeptly learn both local and global graph representations while swiftly
  sampling the graph topology. As such, a key innovation of this work lies in the
  creation of a fast neighborhood sampling technique coupled with a local attention
  mechanism that encompasses a 4-hop reception field, but achieved through just 2-hop
  operations. This local node embedding is then integrated with a global node embedding,
  acquired via another self-attention layer with an approximate global codebook, before
  finally sent through a downstream layer for node predictions. The proposed GT framework,
  named , overcomes previous computational bottlenecks and is validated on three large-scale
  node classification benchmarks. We report a $3 $ speedup and $16.8\ Source code
  available at: https://github.com/snap-research/LargeGT'
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
proposed_models:
- LargeGT-local
- LargeGT-full
mrr: 0.1357
results:
- &id002
  dataset: ogbn-papers100M
  rows:
  - model: LargeGT-full
    value: 0.6473
    std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 1
    is_best: true
  - model: GOAT-full-δ
    value: 0.6112
    std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 2
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: ogbn-products
  rows:
  - model: SAGE
    value: 0.9334
    std: 0.0006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05697'
    title: 'Diffusing to the Top: Boost Graph Neural Networks with Minimal Hyperparameter
      Tuning'
    date: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: GCN
    value: 0.9115
    std: 0.0004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2410.05697'
    title: 'Diffusing to the Top: Boost Graph Neural Networks with Minimal Hyperparameter
      Tuning'
    date: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: GPM
    value: 0.8262
    std: 0.0039
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: GOAT-local-δ
    value: 0.8117
    std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 6
    is_best: false
  - model: GOAT-full-δ
    value: 0.7988
    std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 9
    is_best: false
  - model: LargeGT-full
    value: 0.7981
    std: 0.0025
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 10
    is_best: false
  - model: LargeGT-local
    value: 0.7895
    std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 14
    is_best: false
  - model: GAT-δ
    value: 0.7738
    std: 0.0059
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 18
    is_best: false
  - model: GraphSAGE
    value: 0.7662
    std: 0.0093
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 19
    is_best: false
  - model: Nagphormer
    value: 0.7528
    std: 0.0004
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
  - model: GOAT-global-δ
    value: 0.7028
    std: 0.0195
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
  - model: GT-sparse-δ
    value: 0.6076
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
- &id003
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
    table_ref: Table 1
    source_ref: this paper
    global_rank: 3
    is_best: false
  - model: Grad. Gating
    value: 0.695
    std: 0.0039
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
    global_rank: 4
    is_best: false
  - model: LargeGT-local
    value: 0.6819
    std: 0.0311
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 5
    is_best: false
  - model: Nagphormer
    value: 0.6011
    std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 9
    is_best: false
  - model: GOAT-full-δ
    value: 0.5028
    std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 12
    is_best: false
  - model: GraphSAGE
    value: 0.4843
    std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 13
    is_best: false
  - model: GT-sparse-δ
    value: 0.4781
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 14
    is_best: false
  - model: GAT-δ
    value: 0.4592
    std: 0.0022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 16
    is_best: false
  - model: GOAT-global-δ
    value: 0.4265
    std: 0.0007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 17
    is_best: false
  - model: GOAT-local-δ
    value: 0.4095
    std: 0.0016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 18
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: OGB
  datasets:
  - *id001
  - *id002
- benchmark: LINKX Benchmarks
  datasets:
  - *id003
main_figure: /figures/2312.11109/main_figure.png
---

