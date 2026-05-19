---
title: BA graph
slug: ba-graph
benchmark: GraphBench
task_type: graph_classification
description: Node classification on Barabási–Albert random graphs (GraphBench algorithmic
  reasoning).
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://graphbench.github.io/website/datasets.html
stats: null
result_count: 14
best_model:
  model: GIN
  value: 0.292
  metric: Accuracy
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: Accuracy
  higher_is_better: true
  metrics:
  - Accuracy
  - MSE
  rows:
  - model: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.292
    - null
    metric_stds:
    - 0.041
    - null
  - model: GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.03481
    - null
    metric_stds:
    - 0.034460000000000005
    - null
  - model: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.02825
    - null
    metric_stds:
    - 0.00949
    - null
  - model: DeepSets
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.023039999999999998
    - null
    metric_stds:
    - 0.00262
    - null
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 5.526
    metric_stds:
    - null
    - 0.1107
  - model: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 6.641
    metric_stds:
    - null
    - 1.189
  - model: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 7.318
    metric_stds:
    - null
    - 0.873
  - model: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.242
    metric_stds:
    - null
    - 2.619
  - model: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.492
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.0338
    metric_stds:
    - null
    - 0.0036
  - model: DGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.708
    metric_stds:
    - null
    - 0.0115
  - model: GRAND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.469
    metric_stds:
    - null
    - 2.449
  - model: A-DGN w/ GCN backbone
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.1687
    metric_stds:
    - null
    - 0.0599
  - model: ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.705
    metric_stds:
    - null
    - 0.0859
  - model: Stable-ChebNet
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.565
    metric_stds:
    - null
    - 0.0345
  milestones:
  - value: 0.292
    std: 0.041
    model: GIN
    arxiv_id: '2512.04475'
    title: GraphBench
    date: 2025-12
---

