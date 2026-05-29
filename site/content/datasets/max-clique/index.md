---
title: Max Clique
slug: max-clique
benchmark: GraphBench
task_type: graph_classification
description: Maximum clique node prediction (GraphBench algorithmic task).
primary_metric: F1
higher_is_better: true
pyg_url: https://graphbench.github.io/website/datasets.html
stats:
  num_graphs: 21000000
  avg_nodes: 264.0
  avg_edges: 3667.0
  num_classes: null
result_count: 14
best_model:
  model: GraphGPS
  value: 0.754
  metric: F1
  arxiv_id: '1710.10321'
  paper_title: arXiv:1710.10321
variants:
- slug: hard
  name: Hard
  notes: Large graph instances.
  is_standard: false
  primary_metric: F1
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - F1
  - Accuracy
  rows:
  - model: GraphGPS
    model_plain: GraphGPS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1710.10321'
    title: arXiv:1710.10321
    date: Oct 2017
    date_iso: 2017-10
    date_display: Oct 2017
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.754
    - null
    metric_stds:
    - 0.006
    - null
  - model: SAN
    model_plain: SAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1710.10321'
    title: arXiv:1710.10321
    date: Oct 2017
    date_iso: 2017-10
    date_display: Oct 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.738
    - null
    metric_stds:
    - 0.008
    - null
  - model: DGN
    model_plain: DGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1710.10321'
    title: arXiv:1710.10321
    date: Oct 2017
    date_iso: 2017-10
    date_display: Oct 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.725
    - null
    metric_stds:
    - 0.011
    - null
  - model: PNA
    model_plain: PNA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1710.10321'
    title: arXiv:1710.10321
    date: Oct 2017
    date_iso: 2017-10
    date_display: Oct 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.712
    - null
    metric_stds:
    - 0.009
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1710.10321'
    title: arXiv:1710.10321
    date: Oct 2017
    date_iso: 2017-10
    date_display: Oct 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.701
    - null
    metric_stds:
    - 0.018
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1710.10321'
    title: arXiv:1710.10321
    date: Oct 2017
    date_iso: 2017-10
    date_display: Oct 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.695
    - null
    metric_stds:
    - 0.012
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1710.10321'
    title: arXiv:1710.10321
    date: Oct 2017
    date_iso: 2017-10
    date_display: Oct 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.682
    - null
    metric_stds:
    - 0.015
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1710.10321'
    title: arXiv:1710.10321
    date: Oct 2017
    date_iso: 2017-10
    date_display: Oct 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.678
    - null
    metric_stds:
    - 0.021
    - null
  - model: GNN
    model_plain: GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12245'
    title: Asynchronous Neural Networks for Learning in Graphs
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/beabevi/ESAN
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.05
    metric_stds:
    - null
    - 0.0
  - model: PPGN
    model_plain: PPGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12245'
    title: Asynchronous Neural Networks for Learning in Graphs
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/beabevi/ESAN
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.36
    metric_stds:
    - null
    - 0.16
  - model: SMP
    model_plain: SMP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12245'
    title: Asynchronous Neural Networks for Learning in Graphs
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/beabevi/ESAN
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.74
    metric_stds:
    - null
    - 0.24
  - model: DropGNN
    model_plain: DropGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12245'
    title: Asynchronous Neural Networks for Learning in Graphs
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/beabevi/ESAN
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.27
    metric_stds:
    - null
    - 0.07
  - model: ESAN*
    model_plain: ESAN*
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12245'
    title: Asynchronous Neural Networks for Learning in Graphs
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/beabevi/ESAN
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.05
    metric_stds:
    - null
    - 0.0
  - model: AMP
    model_plain: AMP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12245'
    title: Asynchronous Neural Networks for Learning in Graphs
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/beabevi/ESAN
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 1.0
    metric_stds:
    - null
    - 0.0
  milestones:
  - value: 0.754
    std: 0.006
    model: GraphGPS
    arxiv_id: '1710.10321'
    title: arXiv:1710.10321
    date: 2017-10
---

