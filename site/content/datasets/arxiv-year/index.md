---
title: arxiv-year
slug: arxiv-year
benchmark: LINKX Benchmarks
task_type: node_classification
description: OGB-arXiv node classification by publication year (5 classes, heterophilic
  variant).
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.LINKXDataset.html
stats:
  num_graphs: 1
  avg_nodes: 169343.0
  avg_edges: 1166243.0
  num_classes: 40
result_count: 36
best_model:
  model: Dir-GNN
  value: 0.6408
  metric: Accuracy
  arxiv_id: '2305.10498'
  paper_title: Edge Directionality Improves Learning on Heterophilic Graphs
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
  - model: Dir-GNN
    model_plain: Dir-GNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.10498'
    title: Edge Directionality Improves Learning on Heterophilic Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/emalgorithm/directed-graph-neural-network
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.6408
    metric_stds:
    - 0.0026
  - model: Gradient Gating
    model_plain: Gradient Gating
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.10498'
    title: Edge Directionality Improves Learning on Heterophilic Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/emalgorithm/directed-graph-neural-network
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.633
    metric_stds:
    - 0.0184
  - model: MagNet
    model_plain: MagNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.10498'
    title: Edge Directionality Improves Learning on Heterophilic Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/emalgorithm/directed-graph-neural-network
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6029
    metric_stds:
    - 0.0027
  - model: LINKX
    model_plain: LINKX
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.10498'
    title: Edge Directionality Improves Learning on Heterophilic Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/emalgorithm/directed-graph-neural-network
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.56
    metric_stds:
    - 0.0017
  - model: GloGNN
    model_plain: GloGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.10498'
    title: Edge Directionality Improves Learning on Heterophilic Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/emalgorithm/directed-graph-neural-network
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5479
    metric_stds:
    - 0.0025
  - model: SpaM
    model_plain: SpaM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01207'
    title: Sparse Bayesian Message Passing under Structural Uncertainty
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.521
    metric_stds:
    - 0.0059
  - model: FSGNN
    model_plain: FSGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.10498'
    title: Edge Directionality Improves Learning on Heterophilic Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/emalgorithm/directed-graph-neural-network
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5047
    metric_stds:
    - 0.0021
  - model: H2GCN
    model_plain: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.10498'
    title: Edge Directionality Improves Learning on Heterophilic Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/emalgorithm/directed-graph-neural-network
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4909
    metric_stds:
    - 0.001
  - model: H2GCN
    model_plain: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01207'
    title: Sparse Bayesian Message Passing under Structural Uncertainty
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.476
    metric_stds:
    - 0.0041
  - model: ACMGCN
    model_plain: ACMGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.10498'
    title: Edge Directionality Improves Learning on Heterophilic Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/emalgorithm/directed-graph-neural-network
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4737
    metric_stds:
    - 0.0059
  - model: GCNII
    model_plain: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01207'
    title: Sparse Bayesian Message Passing under Structural Uncertainty
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.461
    metric_stds:
    - 0.0072
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.10498'
    title: Edge Directionality Improves Learning on Heterophilic Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/emalgorithm/directed-graph-neural-network
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4602
    metric_stds:
    - 0.0026
  - model: GPR-GNN
    model_plain: GPR-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.10498'
    title: Edge Directionality Improves Learning on Heterophilic Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/emalgorithm/directed-graph-neural-network
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4507
    metric_stds:
    - 0.0021
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01207'
    title: Sparse Bayesian Message Passing under Structural Uncertainty
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.45
    metric_stds:
    - 0.0053
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01207'
    title: Sparse Bayesian Message Passing under Structural Uncertainty
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.445
    metric_stds:
    - 0.0058
  - model: GPRGNN
    model_plain: GPRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01207'
    title: Sparse Bayesian Message Passing under Structural Uncertainty
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.439
    metric_stds:
    - 0.0084
  - model: Acc(GCN)
    model_plain: Acc(GCN)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.09125'
    title: arXiv:2401.09125
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4244
    metric_stds:
    - null
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.10498'
    title: Edge Directionality Improves Learning on Heterophilic Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/emalgorithm/directed-graph-neural-network
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.367
    metric_stds:
    - 0.0021
  - model: Acc(MLP)
    model_plain: Acc(MLP)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.09125'
    title: arXiv:2401.09125
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.364
    metric_stds:
    - null
  - model: GFMate
    model_plain: GFMate
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3019
    metric_stds:
    - 0.0365
  - model: GFMate-0%
    model_plain: GFMate-0%
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2973
    metric_stds:
    - 0.0407
  - model: BRIDGE
    model_plain: BRIDGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2447
    metric_stds:
    - 0.0668
  - model: DAGPrompt
    model_plain: DAGPrompt
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.23079999999999998
    metric_stds:
    - 0.0814
  - model: GraphPrompt
    model_plain: GraphPrompt
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2261
    metric_stds:
    - 0.0466
  - model: GPF
    model_plain: GPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2089
    metric_stds:
    - 0.08199999999999999
  - model: SAGE
    model_plain: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2075
    metric_stds:
    - 0.0499
  - model: GPPT
    model_plain: GPPT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1996
    metric_stds:
    - 0.07629999999999999
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1993
    metric_stds:
    - 0.054000000000000006
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1864
    metric_stds:
    - 0.0691
  - model: DGI+FT
    model_plain: DGI+FT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.18059999999999998
    metric_stds:
    - 0.0622
  - model: GCOPE
    model_plain: GCOPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.17980000000000002
    metric_stds:
    - 0.055099999999999996
  - model: LP+FT
    model_plain: LP+FT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1794
    metric_stds:
    - 0.060599999999999994
  - model: H2GCN
    model_plain: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.15539999999999998
    metric_stds:
    - 0.0733
  - model: GCL+FT
    model_plain: GCL+FT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1553
    metric_stds:
    - 0.0889
  - model: All-In-One
    model_plain: All-In-One
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.15289999999999998
    metric_stds:
    - 0.0755
  - model: GPR
    model_plain: GPR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1081
    metric_stds:
    - 0.09939999999999999
  milestones:
  - value: 0.6408
    std: 0.0026
    model: Dir-GNN
    arxiv_id: '2305.10498'
    title: Edge Directionality Improves Learning on Heterophilic Graphs
    date: 2023-05
---

