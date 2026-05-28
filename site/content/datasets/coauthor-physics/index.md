---
title: Coauthor-Physics
slug: coauthor-physics
benchmark: Classic
task_type: node_classification
description: Co-authorship graph (Physics) node classification from the "Pitfalls
  of Graph Neural Network Evaluation" paper.
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.Coauthor.html
stats:
  num_graphs: null
  avg_nodes: 18333.0
  avg_edges: 163788.0
  num_classes: 15
result_count: 38
best_model:
  model: GrokFormer
  value: 0.9831
  metric: Accuracy
  arxiv_id: '2411.17296'
  paper_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
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
  - model: GrokFormer
    model_plain: GrokFormer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: Nov 26, 2024
    date_iso: '2024-11-26'
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9831
    metric_stds:
    - 0.0018
  - model: Polynormer
    model_plain: Polynormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: Nov 26, 2024
    date_iso: '2024-11-26'
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9808
    metric_stds:
    - 0.0027
  - model: SGFormer
    model_plain: SGFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: Nov 26, 2024
    date_iso: '2024-11-26'
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9796
    metric_stds:
    - 0.0081
  - model: HopGNN
    model_plain: HopGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: Nov 26, 2024
    date_iso: '2024-11-26'
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9786
    metric_stds:
    - 0.0016
  - model: Nagphormer
    model_plain: Nagphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: Nov 26, 2024
    date_iso: '2024-11-26'
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9785
    metric_stds:
    - 0.0026
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: Nov 26, 2024
    date_iso: '2024-11-26'
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9782
    metric_stds:
    - 0.0028
  - model: SpecFormer
    model_plain: SpecFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: Nov 26, 2024
    date_iso: '2024-11-26'
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9775
    metric_stds:
    - 0.0053
  - model: HiGCN
    model_plain: HiGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: Nov 26, 2024
    date_iso: '2024-11-26'
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9765
    metric_stds:
    - 0.0035
  - model: GraphGPS
    model_plain: GraphGPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: Nov 26, 2024
    date_iso: '2024-11-26'
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.976
    metric_stds:
    - 0.0005
  - model: JacobiConv
    model_plain: JacobiConv
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: Nov 26, 2024
    date_iso: '2024-11-26'
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9756
    metric_stds:
    - 0.0028
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.9746
    metric_stds:
    - 0.001
  - model: BernNet
    model_plain: BernNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: Nov 26, 2024
    date_iso: '2024-11-26'
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9736
    metric_stds:
    - 0.003
  - model: Nagphormer
    model_plain: Nagphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.9735
    metric_stds:
    - 0.0012
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.9725
    metric_stds:
    - 0.0006
  - model: ChebNet
    model_plain: ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: Nov 26, 2024
    date_iso: '2024-11-26'
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9725
    metric_stds:
    - 0.0078
  - model: GPRGNN
    model_plain: GPRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: Nov 26, 2024
    date_iso: '2024-11-26'
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9725
    metric_stds:
    - 0.0013
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.9719
    metric_stds:
    - 0.0005
  - model: H2GCN
    model_plain: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: Nov 26, 2024
    date_iso: '2024-11-26'
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9719
    metric_stds:
    - 0.0013
  - model: Polynormer
    model_plain: Polynormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.9718
    metric_stds:
    - 0.0011
  - model: Exphormer
    model_plain: Exphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.9706
    metric_stds:
    - 0.0013
  - model: SGFormer
    model_plain: SGFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.9675
    metric_stds:
    - 0.0026
  - model: GraphGPS
    model_plain: GraphGPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.9671
    metric_stds:
    - 0.0015
  - model: NodeFormer
    model_plain: NodeFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.9648
    metric_stds:
    - 0.0034
  - model: GOAT
    model_plain: GOAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.9647
    metric_stds:
    - 0.0016
  - model: GCNII
    model_plain: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.6655
    metric_stds:
    - 0.025
  - model: 1-GNN
    model_plain: 1-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.6516
    metric_stds:
    - 0.0277
  - model: SAGE
    model_plain: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.6429
    metric_stds:
    - 0.021
  - model: Cheb
    model_plain: Cheb
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.6295
    metric_stds:
    - 0.0206
  - model: GPS
    model_plain: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.629
    metric_stds:
    - 0.0152
  - model: GATv2
    model_plain: GATv2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.6258
    metric_stds:
    - 0.0212
  - model: Transformer
    model_plain: Transformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.6093
    metric_stds:
    - 0.0149
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.6038
    metric_stds:
    - 0.021
  - model: GatedGraph
    model_plain: GatedGraph
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.602
    metric_stds:
    - 0.0286
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.5965
    metric_stds:
    - 0.0327
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.5949
    metric_stds:
    - 0.0361
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.5887
    metric_stds:
    - 0.0338
  - model: FA
    model_plain: FA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.5581
    metric_stds:
    - 0.0233
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.536
    metric_stds:
    - 0.0138
  milestones:
  - value: 0.9746
    std: 0.001
    model: GCN
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification'
    date: 2024-06
  - value: 0.9831
    std: 0.0018
    model: GrokFormer
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: '2024-11-26'
---

