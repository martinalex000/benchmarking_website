---
title: Max Matching
slug: max-matching
benchmark: GraphBench
task_type: graph_classification
description: Maximum matching edge prediction (GraphBench algorithmic task).
primary_metric: F1
higher_is_better: true
pyg_url: https://graphbench.github.io/website/datasets.html
stats:
  num_graphs: 21000000
  avg_nodes: 264.0
  avg_edges: 3667.0
  num_classes: null
result_count: 15
best_model:
  model: GraphGPS
  value: 0.985
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
    - 0.985
    - null
    metric_stds:
    - 0.002
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
    - 0.978
    - null
    metric_stds:
    - 0.003
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
    - 0.965
    - null
    metric_stds:
    - 0.004
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
    - 0.952
    - null
    metric_stds:
    - 0.005
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
    - 0.948
    - null
    metric_stds:
    - 0.006
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
    - 0.941
    - null
    metric_stds:
    - 0.007
    - null
  - model: ChebNet
    model_plain: ChebNet
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
    - 0.935
    - null
    metric_stds:
    - 0.008
    - null
  - model: MLP
    model_plain: MLP
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
    - 0.89
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
    arxiv_id: '2508.11513'
    title: Towards Faithful Class-level Self-explainability in Graph Neural Networks
      by Subgraph Dependencies
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/FanzhenLiu/GraphOracle
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.8625
    metric_stds:
    - null
    - 0.0116
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.11513'
    title: Towards Faithful Class-level Self-explainability in Graph Neural Networks
      by Subgraph Dependencies
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/FanzhenLiu/GraphOracle
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.8523
    metric_stds:
    - null
    - 0.008
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.11513'
    title: Towards Faithful Class-level Self-explainability in Graph Neural Networks
      by Subgraph Dependencies
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/FanzhenLiu/GraphOracle
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.8511
    metric_stds:
    - null
    - 0.0104
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.11513'
    title: Towards Faithful Class-level Self-explainability in Graph Neural Networks
      by Subgraph Dependencies
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/FanzhenLiu/GraphOracle
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.8625
    metric_stds:
    - null
    - 0.022
  - model: ProtGNN
    model_plain: ProtGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.11513'
    title: Towards Faithful Class-level Self-explainability in Graph Neural Networks
      by Subgraph Dependencies
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/FanzhenLiu/GraphOracle
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.8614
    metric_stds:
    - null
    - 0.0142
  - model: PGIB
    model_plain: PGIB
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.11513'
    title: Towards Faithful Class-level Self-explainability in Graph Neural Networks
      by Subgraph Dependencies
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/FanzhenLiu/GraphOracle
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.8636
    metric_stds:
    - null
    - 0.0119
  - model: novel masking-based evaluation strategy
    model_plain: novel masking-based evaluation strategy
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.11513'
    title: Towards Faithful Class-level Self-explainability in Graph Neural Networks
      by Subgraph Dependencies
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/FanzhenLiu/GraphOracle
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.8818
    metric_stds:
    - null
    - 0.0258
  milestones:
  - value: 0.985
    std: 0.002
    model: GraphGPS
    arxiv_id: '1710.10321'
    title: arXiv:1710.10321
    date: 2017-10
---

