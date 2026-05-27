---
title: snap-patents
slug: snap-patents
benchmark: LINKX Benchmarks
task_type: node_classification
description: USPTO patent citation graph node classification (5 time-based classes).
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.LINKXDataset.html
stats:
  num_graphs: 1
  avg_nodes: 2745480.0
  avg_edges: 12800500.0
  num_classes: 5
result_count: 24
best_model:
  model: MRS-Dir-GCN_DA
  value: 0.7472
  metric: Accuracy
  arxiv_id: '2409.11504'
  paper_title: Preventing Representational Rank Collapse in MPNNs by Splitting the
    Computational Graph
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
  - model: MRS-Dir-GCN_DA
    model_plain: MRS-Dir-GCN_DA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.7472
    metric_stds:
    - 0.0005
  - model: Dir-GNN
    model_plain: Dir-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7395
    metric_stds:
    - 0.0005
  - model: LargeGT-full
    model_plain: LargeGT-full
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11109'
    title: Graph Transformers for Large Graphs
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7021
    metric_stds:
    - 0.0012
  - model: Grad. Gating
    model_plain: Grad. Gating
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.695
    metric_stds:
    - 0.0039
  - model: LargeGT-local
    model_plain: LargeGT-local
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11109'
    title: Graph Transformers for Large Graphs
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6819
    metric_stds:
    - 0.0311
  - model: FSGNN
    model_plain: FSGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6507
    metric_stds:
    - 0.0003
  - model: GLoGNN
    model_plain: GLoGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6209
    metric_stds:
    - 0.0027
  - model: LINKX
    model_plain: LINKX
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6195
    metric_stds:
    - 0.0012
  - model: Nagphormer
    model_plain: Nagphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11109'
    title: Graph Transformers for Large Graphs
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6011
    metric_stds:
    - 0.0005
  - model: ACMGCN
    model_plain: ACMGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5514
    metric_stds:
    - 0.0016
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5102
    metric_stds:
    - 0.0006
  - model: GOAT-full-δ
    model_plain: GOAT-full-δ
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11109'
    title: Graph Transformers for Large Graphs
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5028
    metric_stds:
    - 0.0014
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11109'
    title: Graph Transformers for Large Graphs
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4843
    metric_stds:
    - 0.0021
  - model: GT-sparse-δ
    model_plain: GT-sparse-δ
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11109'
    title: Graph Transformers for Large Graphs
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4781
    metric_stds:
    - 0.0
  - model: GT + Mask + RPEARL
    model_plain: GT + Mask + RPEARL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.15239'
    title: Size Transferability of Graph Transformers with Convolutional Positional
      Encodings
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.46549999999999997
    metric_stds:
    - null
  - model: GAT-δ
    model_plain: GAT-δ
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11109'
    title: Graph Transformers for Large Graphs
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4592
    metric_stds:
    - 0.0022
  - model: GOAT-global-δ
    model_plain: GOAT-global-δ
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11109'
    title: Graph Transformers for Large Graphs
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4265
    metric_stds:
    - 0.0007
  - model: GOAT-local-δ
    model_plain: GOAT-local-δ
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11109'
    title: Graph Transformers for Large Graphs
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4095
    metric_stds:
    - 0.0016
  - model: GPR-GNN
    model_plain: GPR-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4019
    metric_stds:
    - 0.0003
  - model: GT + Mask
    model_plain: GT + Mask
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.15239'
    title: Size Transferability of Graph Transformers with Convolutional Positional
      Encodings
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3969
    metric_stds:
    - null
  - model: GT + RPEARL
    model_plain: GT + RPEARL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.15239'
    title: Size Transferability of Graph Transformers with Convolutional Positional
      Encodings
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.34630000000000005
    metric_stds:
    - null
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3134
    metric_stds:
    - 0.0005
  - model: GT (no PE)
    model_plain: GT (no PE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.15239'
    title: Size Transferability of Graph Transformers with Convolutional Positional
      Encodings
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.31329999999999997
    metric_stds:
    - null
  - model: GT + Mask + RE
    model_plain: GT + Mask + RE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.15239'
    title: Size Transferability of Graph Transformers with Convolutional Positional
      Encodings
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
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

