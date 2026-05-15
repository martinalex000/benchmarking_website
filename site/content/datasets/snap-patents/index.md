---
title: snap-patents
slug: snap-patents
benchmark: LINKX Benchmarks
task_type: node_classification
description: USPTO patent citation graph node classification (5 time-based classes).
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.LINKXDataset.html
stats: null
result_count: 24
best_model:
  model: MRS-Dir-GCN_DA
  value: 0.7472
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
  - model: MRS-Dir-GCN_DA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.7472
    metric_stds:
    - 0.0005
  - model: Dir-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7395
    metric_stds:
    - 0.0005
  - model: LargeGT-full
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11109'
    title: Graph Transformers for Large Graphs
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7021
    metric_stds:
    - 0.0012
  - model: Grad. Gating
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.695
    metric_stds:
    - 0.0039
  - model: LargeGT-local
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11109'
    title: Graph Transformers for Large Graphs
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6819
    metric_stds:
    - 0.0311
  - model: FSGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6507
    metric_stds:
    - 0.0003
  - model: GLoGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6209
    metric_stds:
    - 0.0027
  - model: LINKX
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6195
    metric_stds:
    - 0.0012
  - model: Nagphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11109'
    title: Graph Transformers for Large Graphs
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6011
    metric_stds:
    - 0.0005
  - model: ACMGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5514
    metric_stds:
    - 0.0016
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5102
    metric_stds:
    - 0.0006
  - model: GOAT-full-δ
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11109'
    title: Graph Transformers for Large Graphs
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5028
    metric_stds:
    - 0.0014
  - model: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11109'
    title: Graph Transformers for Large Graphs
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4843
    metric_stds:
    - 0.0021
  - model: GT-sparse-δ
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11109'
    title: Graph Transformers for Large Graphs
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4781
    metric_stds:
    - 0.0
  - model: GT + Mask + RPEARL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.15239'
    title: Size Transferability of Graph Transformers with Convolutional Positional
      Encodings
    date: Feb 2026
    date_iso: 2026-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.46549999999999997
    metric_stds:
    - null
  - model: GAT-δ
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11109'
    title: Graph Transformers for Large Graphs
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4592
    metric_stds:
    - 0.0022
  - model: GOAT-global-δ
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11109'
    title: Graph Transformers for Large Graphs
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4265
    metric_stds:
    - 0.0007
  - model: GOAT-local-δ
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11109'
    title: Graph Transformers for Large Graphs
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4095
    metric_stds:
    - 0.0016
  - model: GPR-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4019
    metric_stds:
    - 0.0003
  - model: GT + Mask
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.15239'
    title: Size Transferability of Graph Transformers with Convolutional Positional
      Encodings
    date: Feb 2026
    date_iso: 2026-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3969
    metric_stds:
    - null
  - model: GT + RPEARL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.15239'
    title: Size Transferability of Graph Transformers with Convolutional Positional
      Encodings
    date: Feb 2026
    date_iso: 2026-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.34630000000000005
    metric_stds:
    - null
  - model: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3134
    metric_stds:
    - 0.0005
  - model: GT (no PE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.15239'
    title: Size Transferability of Graph Transformers with Convolutional Positional
      Encodings
    date: Feb 2026
    date_iso: 2026-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.31329999999999997
    metric_stds:
    - null
  - model: GT + Mask + RE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.15239'
    title: Size Transferability of Graph Transformers with Convolutional Positional
      Encodings
    date: Feb 2026
    date_iso: 2026-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.31010000000000004
    metric_stds:
    - null
  milestones:
  - value: 0.7021
    std: 0.0012
    model: LargeGT-full
    arxiv_id: '2312.11109'
    title: Graph Transformers for Large Graphs
    date: 2023-12
  - value: 0.7472
    std: 0.0005
    model: MRS-Dir-GCN_DA
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: 2024-09
---

