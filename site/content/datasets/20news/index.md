---
title: 20News
slug: 20news
benchmark: Other Graph Benchmarks
task_type: graph_classification
description: '20 Newsgroups text classification represented as a graph (nodes = documents,
  edges = TF-IDF similarity). 20 classes.

  '
primary_metric: Accuracy
higher_is_better: true
pyg_url: ''
stats:
  num_graphs: null
  avg_nodes: null
  avg_edges: null
  num_classes: 20
result_count: 9
best_model:
  model: ParaFormer (a)
  value: 0.595
  metric: Accuracy
  arxiv_id: '2512.14619'
  paper_title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
    Learning'
variants:
- slug: standard-split
  name: Standard split
  notes: Used as a heterophilic benchmark in several GNN papers.
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
  - model: ParaFormer (a)
    model_plain: ParaFormer (a)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: ''
    uses_external_data: null
    is_best: true
    metric_values:
    - 0.595
    metric_stds:
    - 0.004
  - model: DIFFomer-a
    model_plain: DIFFomer-a
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.579
    metric_stds:
    - 0.006999999999999999
  - model: DIFFomer-s
    model_plain: DIFFomer-s
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5770000000000001
    metric_stds:
    - 0.003
  - model: ManiReg
    model_plain: ManiReg
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.563
    metric_stds:
    - 0.012
  - model: GLCN
    model_plain: GLCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.562
    metric_stds:
    - 0.008
  - model: GCN-kNN
    model_plain: GCN-kNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.561
    metric_stds:
    - 0.006
  - model: LP
    model_plain: LP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5589999999999999
    metric_stds:
    - null
  - model: GAT-kNN
    model_plain: GAT-kNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.552
    metric_stds:
    - 0.008
  - model: DenseGAT
    model_plain: DenseGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.546
    metric_stds:
    - 0.002
  milestones:
  - value: 0.595
    std: 0.004
    model: ParaFormer (a)
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: 2025-12
---

