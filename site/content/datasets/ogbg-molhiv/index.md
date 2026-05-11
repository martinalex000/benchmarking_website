---
title: ogbg-molhiv
slug: ogbg-molhiv
benchmark: OGB
task_type: graph_classification
description: Binary graph classification on HIV inhibition (molecules).
primary_metric: ROC-AUC
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.OGBDataset.html
stats: null
result_count: 7
best_model:
  model: ContextPred
  value: 68.9
  metric: ROC-AUC
variants:
- slug: standard-split
  name: Standard split
  notes: 'Scaffold split. Metric: ROC-AUC.'
  is_standard: true
  primary_metric: ROC-AUC
  higher_is_better: true
  metrics:
  - ROC-AUC
  rows:
  - model: ContextPred
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16435'
    title: 'Node Identifiers: Compact, Discrete Representations for Efficient Graph
      Learning'
    date: May 2024
    date_iso: '2024-05-26'
    codebase_url: https://github.com/LUOyk1999/NodeID
    uses_external_data: null
    is_best: true
    metric_values:
    - 68.9
    metric_stds:
    - 0.4
  - model: JOAO
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16435'
    title: 'Node Identifiers: Compact, Discrete Representations for Efficient Graph
      Learning'
    date: May 2024
    date_iso: '2024-05-26'
    codebase_url: https://github.com/LUOyk1999/NodeID
    uses_external_data: null
    is_best: true
    metric_values:
    - 68.1
    metric_stds:
    - 0.9
  - model: SimGRACE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16435'
    title: 'Node Identifiers: Compact, Discrete Representations for Efficient Graph
      Learning'
    date: May 2024
    date_iso: '2024-05-26'
    codebase_url: https://github.com/LUOyk1999/NodeID
    uses_external_data: null
    is_best: false
    metric_values:
    - 66.3
    metric_stds:
    - 1.5
  - model: EdgePred
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16435'
    title: 'Node Identifiers: Compact, Discrete Representations for Efficient Graph
      Learning'
    date: May 2024
    date_iso: '2024-05-26'
    codebase_url: https://github.com/LUOyk1999/NodeID
    uses_external_data: null
    is_best: false
    metric_values:
    - 64.9
    metric_stds:
    - 2.0
  - model: NID_CL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16435'
    title: 'Node Identifiers: Compact, Discrete Representations for Efficient Graph
      Learning'
    date: May 2024
    date_iso: '2024-05-26'
    codebase_url: https://github.com/LUOyk1999/NodeID
    uses_external_data: null
    is_best: false
    metric_values:
    - 64.3
    metric_stds:
    - 0.8
  - model: GraphCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16435'
    title: 'Node Identifiers: Compact, Discrete Representations for Efficient Graph
      Learning'
    date: May 2024
    date_iso: '2024-05-26'
    codebase_url: https://github.com/LUOyk1999/NodeID
    uses_external_data: null
    is_best: false
    metric_values:
    - 63.7
    metric_stds:
    - 2.3
  - model: AttrMask
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16435'
    title: 'Node Identifiers: Compact, Discrete Representations for Efficient Graph
      Learning'
    date: May 2024
    date_iso: '2024-05-26'
    codebase_url: https://github.com/LUOyk1999/NodeID
    uses_external_data: null
    is_best: false
    metric_values:
    - 60.9
    metric_stds:
    - 1.3
  milestones:
  - value: 68.9
    std: 0.4
    model: ContextPred
    arxiv_id: '2405.16435'
    title: 'Node Identifiers: Compact, Discrete Representations for Efficient Graph
      Learning'
    date: '2024-05-26'
---

