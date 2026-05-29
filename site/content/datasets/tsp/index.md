---
title: TSP
slug: tsp
benchmark: GNNBenchmark
task_type: link_prediction
description: Travelling salesman problem — edge classification (in/not in optimal
  tour).
primary_metric: F1
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.GNNBenchmarkDataset.html
stats: null
result_count: 20
best_model:
  model: ARGNP
  value: 0.855
  metric: F1
  arxiv_id: '2402.04538'
  paper_title: 'Triplet Interaction Improves Graph Transformers: Accurate Molecular
    Graph Learning with Triplet Graph Transformers'
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: F1
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - F1
  - Approximation Ratio
  rows:
  - model: ARGNP
    model_plain: ARGNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.04538'
    title: 'Triplet Interaction Improves Graph Transformers: Accurate Molecular Graph
      Learning with Triplet Graph Transformers'
    date: Feb 7, 2024
    date_iso: '2024-02-07'
    date_display: Feb 2024
    codebase_url: https://github.com/shamim-hussain/tgt
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.855
    - null
    metric_stds:
    - 0.001
    - null
  - model: TGT-Agx2
    model_plain: TGT-Agx2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.04538'
    title: 'Triplet Interaction Improves Graph Transformers: Accurate Molecular Graph
      Learning with Triplet Graph Transformers'
    date: Feb 7, 2024
    date_iso: '2024-02-07'
    date_display: Feb 2024
    codebase_url: https://github.com/shamim-hussain/tgt
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.854
    - null
    metric_stds:
    - 0.001
    - null
  - model: TGT-At
    model_plain: TGT-At
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.04538'
    title: 'Triplet Interaction Improves Graph Transformers: Accurate Molecular Graph
      Learning with Triplet Graph Transformers'
    date: Feb 7, 2024
    date_iso: '2024-02-07'
    date_display: Feb 2024
    codebase_url: https://github.com/shamim-hussain/tgt
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.833
    - null
    metric_stds:
    - 0.001
    - null
  - model: TGT-Ag
    model_plain: TGT-Ag
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.04538'
    title: 'Triplet Interaction Improves Graph Transformers: Accurate Molecular Graph
      Learning with Triplet Graph Transformers'
    date: Feb 7, 2024
    date_iso: '2024-02-07'
    date_display: Feb 2024
    codebase_url: https://github.com/shamim-hussain/tgt
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.832
    - null
    metric_stds:
    - 0.001
    - null
  - model: this assumption the convolutional inductive bias
    model_plain: this assumption the convolutional inductive bias
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.03348'
    title: Global Self-Attention as a Replacement for Graph Convolution
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/shamim-hussain/egt
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.822
    - null
    metric_stds:
    - 0.0
    - null
  - model: EGT
    model_plain: EGT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.04538'
    title: 'Triplet Interaction Improves Graph Transformers: Accurate Molecular Graph
      Learning with Triplet Graph Transformers'
    date: Feb 7, 2024
    date_iso: '2024-02-07'
    date_display: Feb 2024
    codebase_url: https://github.com/shamim-hussain/tgt
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.822
    - null
    metric_stds:
    - 0.0
    - null
  - model: GatedGCN
    model_plain: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.03348'
    title: Global Self-Attention as a Replacement for Graph Convolution
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/shamim-hussain/egt
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.808
    - null
    metric_stds:
    - 0.003
    - null
  - model: Graphormer
    model_plain: Graphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.03348'
    title: Global Self-Attention as a Replacement for Graph Convolution
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/shamim-hussain/egt
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.698
    - null
    metric_stds:
    - 0.007
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.03348'
    title: Global Self-Attention as a Replacement for Graph Convolution
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/shamim-hussain/egt
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.671
    - null
    metric_stds:
    - 0.002
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.03348'
    title: Global Self-Attention as a Replacement for Graph Convolution
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/shamim-hussain/egt
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.665
    - null
    metric_stds:
    - 0.003
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.03348'
    title: Global Self-Attention as a Replacement for Graph Convolution
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/shamim-hussain/egt
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.656
    - null
    metric_stds:
    - 0.003
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.03348'
    title: Global Self-Attention as a Replacement for Graph Convolution
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/shamim-hussain/egt
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.63
    - null
    metric_stds:
    - 0.001
    - null
  - model: S2V-DQN
    model_plain: S2V-DQN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1704.01665'
    title: Learning Combinatorial Optimization Algorithms over Graphs
    date: Apr 2017
    date_iso: 2017-04
    date_display: Apr 2017
    codebase_url: https://github.com/Hanjun-Dai/graphnn
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.0105
    metric_stds:
    - null
    - null
  - model: Farthest
    model_plain: Farthest
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1704.01665'
    title: Learning Combinatorial Optimization Algorithms over Graphs
    date: Apr 2017
    date_iso: 2017-04
    date_display: Apr 2017
    codebase_url: https://github.com/Hanjun-Dai/graphnn
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.0108
    metric_stds:
    - null
    - null
  - model: 2-opt
    model_plain: 2-opt
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1704.01665'
    title: Learning Combinatorial Optimization Algorithms over Graphs
    date: Apr 2017
    date_iso: 2017-04
    date_display: Apr 2017
    codebase_url: https://github.com/Hanjun-Dai/graphnn
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.0109
    metric_stds:
    - null
    - null
  - model: Cheapest
    model_plain: Cheapest
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1704.01665'
    title: Learning Combinatorial Optimization Algorithms over Graphs
    date: Apr 2017
    date_iso: 2017-04
    date_display: Apr 2017
    codebase_url: https://github.com/Hanjun-Dai/graphnn
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.0118
    metric_stds:
    - null
    - null
  - model: Christofides
    model_plain: Christofides
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1704.01665'
    title: Learning Combinatorial Optimization Algorithms over Graphs
    date: Apr 2017
    date_iso: 2017-04
    date_display: Apr 2017
    codebase_url: https://github.com/Hanjun-Dai/graphnn
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.012
    metric_stds:
    - null
    - null
  - model: Closest
    model_plain: Closest
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1704.01665'
    title: Learning Combinatorial Optimization Algorithms over Graphs
    date: Apr 2017
    date_iso: 2017-04
    date_display: Apr 2017
    codebase_url: https://github.com/Hanjun-Dai/graphnn
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.0121
    metric_stds:
    - null
    - null
  - model: Nearest
    model_plain: Nearest
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1704.01665'
    title: Learning Combinatorial Optimization Algorithms over Graphs
    date: Apr 2017
    date_iso: 2017-04
    date_display: Apr 2017
    codebase_url: https://github.com/Hanjun-Dai/graphnn
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.0124
    metric_stds:
    - null
    - null
  - model: MST
    model_plain: MST
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1704.01665'
    title: Learning Combinatorial Optimization Algorithms over Graphs
    date: Apr 2017
    date_iso: 2017-04
    date_display: Apr 2017
    codebase_url: https://github.com/Hanjun-Dai/graphnn
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.0137
    metric_stds:
    - null
    - null
  milestones:
  - value: 0.822
    std: null
    model: this assumption the convolutional inductive bias
    arxiv_id: '2108.03348'
    title: Global Self-Attention as a Replacement for Graph Convolution
    date: 2021-08
  - value: 0.855
    std: 0.001
    model: ARGNP
    arxiv_id: '2402.04538'
    title: 'Triplet Interaction Improves Graph Transformers: Accurate Molecular Graph
      Learning with Triplet Graph Transformers'
    date: '2024-02-07'
---

