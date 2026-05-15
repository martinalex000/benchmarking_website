---
title: CSL
slug: csl
benchmark: GNNBenchmark
task_type: graph_classification
description: Circular skip link graphs — tests graph isomorphism discrimination (10
  classes).
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.GNNBenchmarkDataset.html
stats:
  num_graphs: 150
  avg_nodes: 41.0
  avg_edges: 164.0
  num_classes: 10
result_count: 27
best_model:
  model: B-method
  value: 1.0
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
  rows:
  - model: B-method
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 1.0
    metric_stds:
    - null
  - model: R-method
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 1.0
    metric_stds:
    - null
  - model: Transformer+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.501
    arxiv_id: '2404.03380'
    title: On the Theoretical Expressive Power and the Design Space of Higher-Order
      Graph Transformers
    date: '2024-04-04'
    date_iso: '2024-04-04'
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 1.0
    metric_stds:
    - 0.0
  - model: Transformer+RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.03380'
    title: On the Theoretical Expressive Power and the Design Space of Higher-Order
      Graph Transformers
    date: '2024-04-04'
    date_iso: '2024-04-04'
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 1.0
    metric_stds:
    - 0.0
  - model: A_2+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.03380'
    title: On the Theoretical Expressive Power and the Design Space of Higher-Order
      Graph Transformers
    date: '2024-04-04'
    date_iso: '2024-04-04'
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 1.0
    metric_stds:
    - 0.0
  - model: A_2+RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.03380'
    title: On the Theoretical Expressive Power and the Design Space of Higher-Order
      Graph Transformers
    date: '2024-04-04'
    date_iso: '2024-04-04'
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 1.0
    metric_stds:
    - 0.0
  - model: A_2^LN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.03380'
    title: On the Theoretical Expressive Power and the Design Space of Higher-Order
      Graph Transformers
    date: '2024-04-04'
    date_iso: '2024-04-04'
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 1.0
    metric_stds:
    - 0.0
  - model: A_2^LN+LapPE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.03380'
    title: On the Theoretical Expressive Power and the Design Space of Higher-Order
      Graph Transformers
    date: '2024-04-04'
    date_iso: '2024-04-04'
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 1.0
    metric_stds:
    - 0.0
  - model: A_2^LN+RWSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.03380'
    title: On the Theoretical Expressive Power and the Design Space of Higher-Order
      Graph Transformers
    date: '2024-04-04'
    date_iso: '2024-04-04'
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 1.0
    metric_stds:
    - 0.0
  - model: AS_0:1+attn.bias+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.03380'
    title: On the Theoretical Expressive Power and the Design Space of Higher-Order
      Graph Transformers
    date: '2024-04-04'
    date_iso: '2024-04-04'
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 1.0
    metric_stds:
    - 0.0
  - model: AS_0:1+attn.bias+RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.03380'
    title: On the Theoretical Expressive Power and the Design Space of Higher-Order
      Graph Transformers
    date: '2024-04-04'
    date_iso: '2024-04-04'
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 1.0
    metric_stds:
    - 0.0
  - model: AS_0:1^SN+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.03380'
    title: On the Theoretical Expressive Power and the Design Space of Higher-Order
      Graph Transformers
    date: '2024-04-04'
    date_iso: '2024-04-04'
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 1.0
    metric_stds:
    - 0.0
  - model: AS_0:1^SN+RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.03380'
    title: On the Theoretical Expressive Power and the Design Space of Higher-Order
      Graph Transformers
    date: '2024-04-04'
    date_iso: '2024-04-04'
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 1.0
    metric_stds:
    - 0.0
  - model: GIN + RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 1.0
    metric_stds:
    - 0.0
  - model: PathNN-SP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: '2023-06-09'
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 1.0
    metric_stds:
    - 0.0
  - model: PathNN-AP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: '2023-06-09'
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 1.0
    metric_stds:
    - 0.0
  - model: 3WLGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: '2023-06-09'
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.978
    metric_stds:
    - 0.109
  - model: GINE + LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.925
    metric_stds:
    - 0.042
  - model: Graphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.03380'
    title: On the Theoretical Expressive Power and the Design Space of Higher-Order
      Graph Transformers
    date: '2024-04-04'
    date_iso: '2024-04-04'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9
    metric_stds:
    - 0.0
  - model: GINE+GPSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.429
    metric_stds:
    - 0.079
  - model: AS_0:1+attn.bias
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.03380'
    title: On the Theoretical Expressive Power and the Design Space of Higher-Order
      Graph Transformers
    date: '2024-04-04'
    date_iso: '2024-04-04'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3667
    metric_stds:
    - 0.0
  - model: AS_0:1^SN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.03380'
    title: On the Theoretical Expressive Power and the Design Space of Higher-Order
      Graph Transformers
    date: '2024-04-04'
    date_iso: '2024-04-04'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2
    metric_stds:
    - 0.0
  - model: GIN+rand
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.127
    metric_stds:
    - 0.064
  - model: Message-passing GNNs with WL-related PEs
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1
    metric_stds:
    - null
  - model: Transformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.03380'
    title: On the Theoretical Expressive Power and the Design Space of Higher-Order
      Graph Transformers
    date: '2024-04-04'
    date_iso: '2024-04-04'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1
    metric_stds:
    - 0.0
  - model: A_2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.03380'
    title: On the Theoretical Expressive Power and the Design Space of Higher-Order
      Graph Transformers
    date: '2024-04-04'
    date_iso: '2024-04-04'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1
    metric_stds:
    - 0.0
  - model: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: '2023-06-09'
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1
    metric_stds:
    - 0.0
  milestones:
  - value: 1.0
    std: null
    model: PathNN-SP
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: '2023-06-09'
---

