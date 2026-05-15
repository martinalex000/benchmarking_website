---
title: Amazon2M
slug: amazon2m
benchmark: Other Graph Benchmarks
task_type: node_classification
description: 'Large-scale Amazon co-purchase graph with ~2M nodes. Node classification
  (product category). Used to benchmark scalable GNNs and graph transformers.

  '
primary_metric: Accuracy
higher_is_better: true
pyg_url: ''
stats: null
result_count: 13
best_model:
  model: ParaFormer (a)
  value: 0.8936
  metric: Accuracy
variants:
- slug: standard-split
  name: Standard split
  notes: ~2M nodes, ~61M edges.
  is_standard: true
  primary_metric: Accuracy
  higher_is_better: true
  metrics:
  - Accuracy
  rows:
  - model: ParaFormer (a)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.8936
    metric_stds:
    - 0.0014000000000000002
  - model: SGFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8909
    metric_stds:
    - 0.001
  - model: NodeFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8785
    metric_stds:
    - 0.0024
  - model: GAT-NSampler
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8517
    metric_stds:
    - 0.0032
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8390000000000001
    metric_stds:
    - 0.001
  - model: GCN-Nsampler
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8384
    metric_stds:
    - 0.0042
  - model: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8120999999999999
    metric_stds:
    - 0.0012
  - model: SIGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8098000000000001
    metric_stds:
    - 0.0031
  - model: Nagphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16030'
    title: 'VCR-Graphormer: A Mini-batch Graph Transformer via Virtual Connections'
    date: Mar 2024
    date_iso: 2024-03
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7743
    metric_stds:
    - 0.0011
  - model: VCR-Graphormer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16030'
    title: 'VCR-Graphormer: A Mini-batch Graph Transformer via Virtual Connections'
    date: Mar 2024
    date_iso: 2024-03
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7609
    metric_stds:
    - 0.0016
  - model: GRAND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16030'
    title: 'VCR-Graphormer: A Mini-batch Graph Transformer via Virtual Connections'
    date: Mar 2024
    date_iso: 2024-03
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7549
    metric_stds:
    - 0.0011
  - model: GraphSAINT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16030'
    title: 'VCR-Graphormer: A Mini-batch Graph Transformer via Virtual Connections'
    date: Mar 2024
    date_iso: 2024-03
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7521
    metric_stds:
    - 0.0015
  - model: PPRGo
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16030'
    title: 'VCR-Graphormer: A Mini-batch Graph Transformer via Virtual Connections'
    date: Mar 2024
    date_iso: 2024-03
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6612
    metric_stds:
    - 0.0059
  milestones:
  - value: 0.7743
    std: 0.0011
    model: Nagphormer
    arxiv_id: '2403.16030'
    title: 'VCR-Graphormer: A Mini-batch Graph Transformer via Virtual Connections'
    date: 2024-03
  - value: 0.8936
    std: 0.0014000000000000002
    model: ParaFormer (a)
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: 2025-12
---

