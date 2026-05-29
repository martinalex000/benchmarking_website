---
title: RB graph
slug: rb-graph
benchmark: GraphBench
task_type: graph_classification
description: Node classification on Random Bipartite graphs (GraphBench algorithmic
  reasoning).
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://graphbench.github.io/website/datasets.html
stats:
  num_graphs: 21000000
  avg_nodes: 264.0
  avg_edges: 3667.0
  num_classes: null
result_count: 7
best_model:
  model: MGNN
  value: 0.815
  metric: Accuracy
  arxiv_id: '2006.15646'
  paper_title: Expressive Power of Invariant and Equivariant Graph Neural Networks
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: Accuracy
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - Accuracy
  rows:
  - model: MGNN
    model_plain: MGNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15646'
    title: Expressive Power of Invariant and Equivariant Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/mlelarge/graph_neural_net
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.815
    metric_stds:
    - 0.009
  - model: PNA
    model_plain: PNA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15646'
    title: Expressive Power of Invariant and Equivariant Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/mlelarge/graph_neural_net
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.801
    metric_stds:
    - 0.011
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15646'
    title: Expressive Power of Invariant and Equivariant Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/mlelarge/graph_neural_net
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.795
    metric_stds:
    - 0.012
  - model: GINE
    model_plain: GINE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15646'
    title: Expressive Power of Invariant and Equivariant Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/mlelarge/graph_neural_net
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.792
    metric_stds:
    - 0.013
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15646'
    title: Expressive Power of Invariant and Equivariant Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/mlelarge/graph_neural_net
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.788
    metric_stds:
    - 0.014
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15646'
    title: Expressive Power of Invariant and Equivariant Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/mlelarge/graph_neural_net
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.782
    metric_stds:
    - 0.015
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15646'
    title: Expressive Power of Invariant and Equivariant Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/mlelarge/graph_neural_net
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.771
    metric_stds:
    - 0.018
  milestones:
  - value: 0.815
    std: 0.009
    model: MGNN
    arxiv_id: '2006.15646'
    title: Expressive Power of Invariant and Equivariant Graph Neural Networks
    date: 2020-06
---

