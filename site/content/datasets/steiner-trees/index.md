---
title: Steiner Trees
slug: steiner-trees
benchmark: GraphBench
task_type: graph_classification
description: Steiner tree node prediction (GraphBench algorithmic task).
primary_metric: F1
higher_is_better: true
pyg_url: https://graphbench.github.io/website/datasets.html
stats:
  num_graphs: 21000000
  avg_nodes: 264.0
  avg_edges: 3667.0
  num_classes: null
result_count: 13
best_model:
  model: Graph Transformer with Laplacian PE
  value: 0.841
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
  - A.Ratio
  rows:
  - model: Graph Transformer with Laplacian PE
    model_plain: Graph Transformer with Laplacian PE
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
    is_best: true
    metric_values:
    - 0.841
    - null
    metric_stds:
    - 0.006
    - null
  - model: LapPE
    model_plain: LapPE
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
    - 0.825
    - null
    metric_stds:
    - 0.008
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
    - 0.812
    - null
    metric_stds:
    - 0.009
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
    - 0.798
    - null
    metric_stds:
    - 0.011
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
    - 0.795
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
    - 0.782
    - null
    metric_stds:
    - 0.015
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
    - 0.771
    - null
    metric_stds:
    - 0.018
    - null
  - model: DiGress (CAVG)
    model_plain: DiGress (CAVG)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.14020'
    title: Bures-Wasserstein Flow Matching for Graph Generation
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 8.9
    metric_stds:
    - null
    - 3.2
  - model: SPECTRE
    model_plain: SPECTRE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.14020'
    title: Bures-Wasserstein Flow Matching for Graph Generation
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 2.1
    metric_stds:
    - null
    - null
  - model: GruM (CAVG)
    model_plain: GruM (CAVG)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.14020'
    title: Bures-Wasserstein Flow Matching for Graph Generation
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 2.4
    metric_stds:
    - null
    - 0.7
  - model: Cometh (CAVG)
    model_plain: Cometh (CAVG)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.14020'
    title: Bures-Wasserstein Flow Matching for Graph Generation
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 2.0
    metric_stds:
    - null
    - 0.4
  - model: DeFoG (CAVG)
    model_plain: DeFoG (CAVG)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.14020'
    title: Bures-Wasserstein Flow Matching for Graph Generation
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 1.9
    metric_stds:
    - null
    - 0.4
  - model: BWFlow (CAVG)
    model_plain: BWFlow (CAVG)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.14020'
    title: Bures-Wasserstein Flow Matching for Graph Generation
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 1.3
    metric_stds:
    - null
    - 0.2
  milestones:
  - value: 0.841
    std: 0.006
    model: Graph Transformer with Laplacian PE
    arxiv_id: '1710.10321'
    title: arXiv:1710.10321
    date: 2017-10
---

