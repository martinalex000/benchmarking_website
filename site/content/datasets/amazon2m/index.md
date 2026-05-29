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
stats:
  num_graphs: 1
  avg_nodes: 2000000.0
  avg_edges: 61000000.0
  num_classes: null
result_count: 19
best_model:
  model: SGFormer
  value: 0.8909
  metric: Accuracy
  arxiv_id: '2306.10759'
  paper_title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph
    Representations'
variants:
- slug: standard-split
  name: Standard split
  notes: ~2M nodes, ~61M edges.
  is_standard: true
  primary_metric: Accuracy
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - Accuracy
  - F1
  rows:
  - model: SGFormer
    model_plain: SGFormer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.10759'
    title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/qitianwu/SGFormer
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.8909
    - null
    metric_stds:
    - 0.001
    - null
  - model: NodeFormer
    model_plain: NodeFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.10759'
    title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/qitianwu/SGFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8785
    - null
    metric_stds:
    - 0.0024
    - null
  - model: GAT-NSampler
    model_plain: GAT-NSampler
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.10759'
    title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/qitianwu/SGFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8517
    - null
    metric_stds:
    - 0.0032
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.10759'
    title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/qitianwu/SGFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.839
    - null
    metric_stds:
    - 0.001
    - null
  - model: GCN-NSampler
    model_plain: GCN-NSampler
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.10759'
    title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/qitianwu/SGFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8384
    - null
    metric_stds:
    - 0.0042
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.10759'
    title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/qitianwu/SGFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8121
    - null
    metric_stds:
    - 0.0012
    - null
  - model: SIGN
    model_plain: SIGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.10759'
    title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/qitianwu/SGFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8098
    - null
    metric_stds:
    - 0.0031
    - null
  - model: DAM-GT
    model_plain: DAM-GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7892
    - null
    metric_stds:
    - 0.0033
    - null
  - model: NAGphormer
    model_plain: NAGphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7743
    - null
    metric_stds:
    - 0.0024
    - null
  - model: ANS-GT
    model_plain: ANS-GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7629
    - null
    metric_stds:
    - 0.0032
    - null
  - model: VCR-Graphormer
    model_plain: VCR-Graphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7609
    - null
    metric_stds:
    - 0.0016
    - null
  - model: GRAND
    model_plain: GRAND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7549
    - null
    metric_stds:
    - 0.0011
    - null
  - model: GraphSAINT
    model_plain: GraphSAINT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7521
    - null
    metric_stds:
    - 0.0015
    - null
  - model: SGFormer
    model_plain: SGFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7422
    - null
    metric_stds:
    - 0.0036
    - null
  - model: NodeFormer
    model_plain: NodeFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7156
    - null
    metric_stds:
    - 0.0042
    - null
  - model: PPRGo
    model_plain: PPRGo
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6612
    - null
    metric_stds:
    - 0.0059
    - null
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.10759'
    title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/qitianwu/SGFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6346
    - null
    metric_stds:
    - 0.001
    - null
  - model: VRGCN (2-layer)
    model_plain: VRGCN (2-layer)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.07953'
    title: 'Cluster-GCN: An Efficient Algorithm for Training Deep and Large Graph
      Convolutional Networks'
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/google-research/google-research
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9021
    metric_stds:
    - null
    - null
  - model: Cluster-GCN (2-layer)
    model_plain: Cluster-GCN (2-layer)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.07953'
    title: 'Cluster-GCN: An Efficient Algorithm for Training Deep and Large Graph
      Convolutional Networks'
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/google-research/google-research
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9041
    metric_stds:
    - null
    - null
  milestones:
  - value: 0.8909
    std: 0.001
    model: SGFormer
    arxiv_id: '2306.10759'
    title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
    date: 2023-06
---

