---
title: 'Design Your Own Universe: A Physics-Informed Agnostic Method for Enhancing
  Graph Neural Networks'
arxiv_id: '2401.14580'
authors: []
published_date: '2024-01-26'
abstract: Physics-informed Graph Neural Networks have achieved remarkable performance
  in learning through graph-structured data by mitigating common GNN challenges such
  as over-smoothing, over-squashing, and heterophily adaption. Despite these advancements,
  the development of a simple yet effective paradigm that appropriately integrates
  previous methods for handling all these challenges is still underway. In this paper,
  we draw an analogy between the propagation of GNNs and particle systems in physics,
  proposing a model-agnostic enhancement framework. This framework enriches the graph
  structure by introducing additional nodes and rewiring connections with both positive
  and negative weights, guided by node labeling information. We theoretically verify
  that GNNs enhanced through our approach can effectively circumvent the over-smoothing
  issue and exhibit robustness against over-squashing. Moreover, we conduct a spectral
  analysis on the rewired graph to demonstrate that the corresponding GNNs can fit
  both homophilic and heterophilic graphs. Empirical validations on benchmarks for
  homophilic, heterophilic graphs, and long-term graph datasets show that GNNs enhanced
  by our method significantly outperform their original counterparts.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
proposed_models:
- UYGCN
- UYGAT
mrr: 0.125
results:
- &id001
  dataset: ogbn-arxiv
  rows:
  - model: GLEM-GNN
    value: 0.7593
    std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: Stable-ChebNet
    value: 0.7573
    std: 0.0051
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: GLEM-LM
    value: 0.7571
    std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: Jul 2023
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: UYGCN
    value: 0.744
    std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 8
    is_best: false
  - model: LEGCN
    value: 0.733
    std: 0.003
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
  - model: H2GCN
    value: 0.728
    std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 29
    is_best: false
  - model: GCN
    value: 0.727
    std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 14
    is_best: false
  - model: UYGAT
    value: 0.723
    std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 46
    is_best: false
  - model: GAT
    value: 0.72
    std: 0.005
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
  - model: SJLR
    value: 0.72
    std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 54
    is_best: false
  - model: Replusion
    value: 0.719
    std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 60
    is_best: false
  - model: GRAND
    value: 0.712
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
  - model: GPRGNN
    value: 0.704
    std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 75
    is_best: false
  - model: APPNP
    value: 0.703
    std: 0.025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 58
    is_best: false
  - model: ACMP
    value: 0.689
    std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 81
    is_best: false
  - model: GIN
    value: 0.645
    std: 0.025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 96
    is_best: false
  - model: MLP
    value: 0.55
    std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 91
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: OGB
  datasets:
  - *id001
main_figure: /figures/2401.14580/main_figure.png
---

