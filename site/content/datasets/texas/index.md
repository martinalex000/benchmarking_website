---
title: Texas
slug: texas
benchmark: Heterophilic Graphs
task_type: node_classification
description: WebKB node classification on Texas university webpages (5 classes).
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.WebKB.html
stats:
  num_graphs: null
  avg_nodes: 183.0
  avg_edges: 325.0
  num_classes: 5
result_count: 218
best_model:
  model: ACMGCN
  value: 0.9656
  metric: Accuracy
variants:
- slug: standard-split
  name: Standard split
  notes: Geom-GCN 10 fixed splits; results typically averaged.
  is_standard: true
  primary_metric: Accuracy
  higher_is_better: true
  metrics:
  - Accuracy
  - F1
  - NMI
  rows:
  - model: ACMGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9656
    - null
    - null
    metric_stds:
    - 0.02
    - null
    - null
  - model: ACM-Snowball-2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9574
    - null
    - null
    metric_stds:
    - 0.0222
    - null
    - null
  - model: ACMII-Snowball-3
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9475
    - null
    - null
    metric_stds:
    - 0.0309
    - null
    - null
  - model: ACMII-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9475
    - null
    - null
    metric_stds:
    - 0.0291
    - null
    - null
  - model: GrokFormer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: '2024-11-26'
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9459
    - null
    - null
    metric_stds:
    - 0.0208
    - null
    - null
  - model: GrokFilter
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: '2024-11-26'
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9362
    - null
    - null
    metric_stds:
    - 0.0304
    - null
    - null
  - model: ACM-SGC-1
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9344
    - null
    - null
    metric_stds:
    - 0.0254
    - null
    - null
  - model: JacobiConv
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: '2024-11-26'
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9344
    - null
    - null
    metric_stds:
    - 0.0213
    - null
    - null
  - model: ACM-GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9328
    - null
    - null
    metric_stds:
    - 0.0279
    - null
    - null
  - model: BernNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9312
    - null
    - null
    metric_stds:
    - 0.0065
    - null
    - null
  - model: GPRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9292
    - null
    - null
    metric_stds:
    - 0.0061
    - null
    - null
  - model: DMD++
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.926
    - null
    - null
    metric_stds:
    - 0.034
    - null
    - null
  - model: SGFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: '2024-11-26'
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9246
    - null
    - null
    metric_stds:
    - 0.0148
    - null
    - null
  - model: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.923
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
  - model: MLP-2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9226
    - null
    - null
    metric_stds:
    - 0.0071
    - null
    - null
  - model: HiGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: '2024-11-26'
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9215
    - null
    - null
    metric_stds:
    - 0.0073
    - null
    - null
  - model: Nagphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: '2024-11-26'
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.918
    - null
    - null
    metric_stds:
    - 0.0185
    - null
    - null
  - model: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9118
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
  - model: '*-w/o-GrokFilter'
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: '2024-11-26'
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9033
    - null
    - null
    metric_stds:
    - 0.0236
    - null
    - null
  - model: DMD-ACMP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.894
    - null
    - null
    metric_stds:
    - 0.038
    - null
    - null
  - model: HopGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: '2024-11-26'
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8915
    - null
    - null
    metric_stds:
    - 0.0404
    - null
    - null
  - model: Polynormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: '2024-11-26'
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8902
    - null
    - null
    metric_stds:
    - 0.0544
    - null
    - null
  - model: FAGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8885
    - null
    - null
    metric_stds:
    - 0.0439
    - null
    - null
  - model: Transformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: '2024-11-26'
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.8875
    - null
    - null
    metric_stds:
    - 0.063
    - null
    - null
  - model: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.492
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8852
    - null
    - null
    metric_stds:
    - 0.0302
    - null
    - null
  - model: SpecFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: '2024-11-26'
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8823
    - null
    - null
    metric_stds:
    - 0.0038
    - null
    - null
  - model: ACMGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8784000000000001
    - null
    - null
    metric_stds:
    - 0.044000000000000004
    - null
    - null
  - model: FSGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8756999999999999
    - null
    - null
    metric_stds:
    - 0.048600000000000004
    - null
    - null
  - model: CSNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.873
    - null
    - null
    metric_stds:
    - 0.0593
    - null
    - null
  - model: ACMII-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.18480'
    title: Scalable Graph Compressed Convolutions
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8676
    - null
    - null
    metric_stds:
    - 0.0475
    - null
    - null
  - model: ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: '2024-11-26'
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8622
    - null
    - null
    metric_stds:
    - 0.0245
    - null
    - null
  - model: O(d)-NSD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8595
    - null
    - null
    metric_stds:
    - 0.055099999999999996
    - null
    - null
  - model: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.859
    - null
    - null
    metric_stds:
    - 0.0353
    - null
    - null
  - model: Diag-NSD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8567
    - null
    - null
    metric_stds:
    - 0.0695
    - null
    - null
  - model: CoCN vanilla
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.18480'
    title: Scalable Graph Compressed Convolutions
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8521
    - null
    - null
    metric_stds:
    - 0.0049
    - null
    - null
  - model: GPRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8514
    - null
    - null
    metric_stds:
    - 0.0368
    - null
    - null
  - model: CoCN expanded
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.18480'
    title: Scalable Graph Compressed Convolutions
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.849
    - null
    - null
    metric_stds:
    - 0.0105
    - null
    - null
  - model: H2GCN-1
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16560'
    title: Algorithmic Graph Tasks
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: https://github.com/nec-research/Adaptive-Message-Passing
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8486
    - null
    - null
    metric_stds:
    - 0.0677
    - null
    - null
  - model: GGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.18480'
    title: Scalable Graph Compressed Convolutions
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8486
    - null
    - null
    metric_stds:
    - 0.0455
    - null
    - null
  - model: NodeFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: '2024-11-26'
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8463
    - null
    - null
    metric_stds:
    - 0.0347
    - null
    - null
  - model: AERO-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.18480'
    title: Scalable Graph Compressed Convolutions
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8435
    - null
    - null
    metric_stds:
    - 0.052
    - null
    - null
  - model: GLoGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8432
    - null
    - null
    metric_stds:
    - 0.0415
    - null
    - null
  - model: DMD-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.842
    - null
    - null
    metric_stds:
    - 0.026
    - null
    - null
  - model: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.839
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
  - model: GraphSAGE+JK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16560'
    title: Algorithmic Graph Tasks
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: https://github.com/nec-research/Adaptive-Message-Passing
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8378
    - null
    - null
    metric_stds:
    - 0.022099999999999998
    - null
    - null
  - model: GraphGPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: '2024-11-26'
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8371
    - null
    - null
    metric_stds:
    - 0.0585
    - null
    - null
  - model: SGC-1
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8328
    - null
    - null
    metric_stds:
    - 0.0543
    - null
    - null
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8311
    - null
    - null
    metric_stds:
    - 0.032
    - null
    - null
  - model: Snowball-2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8311
    - null
    - null
    metric_stds:
    - 0.032
    - null
    - null
  - model: Gen-NSD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8297
    - null
    - null
    metric_stds:
    - 0.0513
    - null
    - null
  - model: SIMPLE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.18917'
    title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse Problems'
    date: Jan 2026
    date_iso: 2026-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.827
    - null
    - null
    metric_stds:
    - 0.032
    - null
    - null
  - model: PR-MPNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.827
    - null
    - null
    metric_stds:
    - 0.032
    - null
    - null
  - model: Framelets
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.823
    - null
    - null
    metric_stds:
    - 0.025
    - null
    - null
  - model: H2GCN-2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16560'
    title: Algorithmic Graph Tasks
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: https://github.com/nec-research/Adaptive-Message-Passing
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8216
    - null
    - null
    metric_stds:
    - 0.0528
    - null
    - null
  - model: AMP_GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16560'
    title: Algorithmic Graph Tasks
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: https://github.com/nec-research/Adaptive-Message-Passing
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8146
    - null
    - null
    metric_stds:
    - 0.030600000000000002
    - null
    - null
  - model: GRAND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.814
    - null
    - null
    metric_stds:
    - 0.035
    - null
    - null
  - model: GPRGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.18480'
    title: Scalable Graph Compressed Convolutions
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8135
    - null
    - null
    metric_stds:
    - 0.0532
    - null
    - null
  - model: SGC-2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8131
    - null
    - null
    metric_stds:
    - 0.033
    - null
    - null
  - model: DMD-SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.812
    - null
    - null
    metric_stds:
    - 0.025
    - null
    - null
  - model: GPRGNN_knn
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8108
    - null
    - null
    metric_stds:
    - 0.0418
    - null
    - null
  - model: IPR-MPNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.808
    - null
    - null
    metric_stds:
    - 0.052
    - null
    - null
  - model: GCN+JK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8066
    - null
    - null
    metric_stds:
    - 0.0191
    - null
    - null
  - model: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.492
    arxiv_id: '2407.18480'
    title: Scalable Graph Compressed Convolutions
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8039
    - null
    - null
    metric_stds:
    - 0.0383
    - null
    - null
  - model: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8027
    - null
    - null
    metric_stds:
    - 0.0593
    - null
    - null
  - model: HopFormer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.02268'
    title: 'HopFormer: Sparse Graph Transformers Explicit Receptive Field Control'
    date: Feb 2026
    date_iso: 2026-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7937
    - null
    - null
    metric_stds:
    - 0.027
    - null
    - null
  - model: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.793
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
  - model: SLAPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7919
    - null
    - null
    metric_stds:
    - 0.0499
    - null
    - null
  - model: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7903
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
  - model: Gumbel
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.18917'
    title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse Problems'
    date: Jan 2026
    date_iso: 2026-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.789
    - null
    - null
    metric_stds:
    - 0.067
    - null
    - null
  - model: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7887
    - null
    - null
    metric_stds:
    - 0.0086
    - null
    - null
  - model: I-MLE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.18917'
    title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse Problems'
    date: Jan 2026
    date_iso: 2026-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.784
    - null
    - null
    metric_stds:
    - 0.033
    - null
    - null
  - model: SpecFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.04765'
    title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7838
    - null
    - null
    metric_stds:
    - 0.0221
    - null
    - null
  - model: Cheby+JK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16560'
    title: Algorithmic Graph Tasks
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: https://github.com/nec-research/Adaptive-Message-Passing
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7837999999999999
    - null
    - null
    metric_stds:
    - 0.0637
    - null
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
    is_best: false
    metric_values:
    - 0.7784
    - null
    - null
    metric_stds:
    - 0.0108
    - null
    - null
  - model: GPS+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.778
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
  - model: CO-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7757
    - null
    - null
    metric_stds:
    - 0.0541
    - null
    - null
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
    is_best: false
    metric_values:
    - 0.7757
    - null
    - null
    metric_stds:
    - 0.0124
    - null
    - null
  - model: GPS+RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.775
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
  - model: GCN-Cheby
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16560'
    title: Algorithmic Graph Tasks
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: https://github.com/nec-research/Adaptive-Message-Passing
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.773
    - null
    - null
    metric_stds:
    - 0.0407
    - null
    - null
  - model: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.773
    - null
    - null
    metric_stds:
    - 0.013
    - null
    - null
  - model: Transformer+DEG
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
    - 0.773
    - null
    - null
    metric_stds:
    - 0.0132
    - null
    - null
  - model: GPS (DEG)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.773
    - null
    - null
    metric_stds:
    - 0.013
    - null
    - null
  - model: SUBLIME
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7703
    - null
    - null
    metric_stds:
    - 0.0423
    - null
    - null
  - model: AS_0:1+attn.bias+RWSE
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
    is_best: false
    metric_values:
    - 0.7684
    - null
    - null
    metric_stds:
    - 0.0166
    - null
    - null
  - model: Graphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.767
    - null
    - null
    metric_stds:
    - 0.017
    - null
    - null
  - model: Graphormer-GD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.767
    - null
    - null
    metric_stds:
    - 0.017
    - null
    - null
  - model: Graphormer+attn.bias
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.767
    - null
    - null
    metric_stds:
    - 0.017
    - null
    - null
  - model: FAGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.18480'
    title: Scalable Graph Compressed Convolutions
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7649
    - null
    - null
    metric_stds:
    - 0.0287
    - null
    - null
  - model: GAT-kNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7649
    - null
    - null
    metric_stds:
    - 0.0499
    - null
    - null
  - model: MixHop
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7639
    - null
    - null
    metric_stds:
    - 0.0766
    - null
    - null
  - model: TRIGON
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7574
    - null
    - null
    metric_stds:
    - 0.0161
    - null
    - null
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.757
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
  - model: ChebNet + NBA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7568
    - null
    - null
    metric_stds:
    - 0.0468
    - null
    - null
  - model: SGFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.04765'
    title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7568
    - null
    - null
    metric_stds:
    - 0.0221
    - null
    - null
  - model: GAT+JK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7541
    - null
    - null
    metric_stds:
    - 0.0718
    - null
    - null
  - model: GPS(GCN+Transformer)+LapPE
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
    - 0.7541
    - null
    - null
    metric_stds:
    - 0.0146
    - null
    - null
  - model: IDGL_knn
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.754
    - null
    - null
    metric_stds:
    - 0.0475
    - null
    - null
  - model: GraphSAGE + LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7486
    - null
    - null
    metric_stds:
    - 0.0612
    - null
    - null
  - model: GSR_knn
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7486
    - null
    - null
    metric_stds:
    - 0.0363
    - null
    - null
  - model: LINKX
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.18480'
    title: Scalable Graph Compressed Convolutions
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.746
    - null
    - null
    metric_stds:
    - 0.0837
    - null
    - null
  - model: GEN_knn
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7459
    - null
    - null
    metric_stds:
    - 0.0346
    - null
    - null
  - model: GCN-kNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7432
    - null
    - null
    metric_stds:
    - 0.0502
    - null
    - null
  - model: HES-GSL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7405
    - null
    - null
    metric_stds:
    - 0.0642
    - null
    - null
  - model: CoBFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.04765'
    title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7387
    - null
    - null
    metric_stds:
    - 0.0637
    - null
    - null
  - model: Random rewire
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.18917'
    title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse Problems'
    date: Jan 2026
    date_iso: 2026-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.738
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
  - model: BS-KAGAT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.18380'
    title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: https://github.com/RomanBresson/KAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7378
    - null
    - null
    metric_stds:
    - 0.0639
    - null
    - null
  - model: RBF-KAGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.18380'
    title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: https://github.com/RomanBresson/KAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.736
    - null
    - null
    metric_stds:
    - 0.050499999999999996
    - null
    - null
  - model: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.18380'
    title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: https://github.com/RomanBresson/KAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7351000000000001
    - null
    - null
    metric_stds:
    - 0.0587
    - null
    - null
  - model: GPS(GCN+Transformer)+RWSE
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
    - 0.7351
    - null
    - null
    metric_stds:
    - 0.0265
    - null
    - null
  - model: GPS(GCN+Transformer)+DEG
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
    - 0.7351
    - null
    - null
    metric_stds:
    - 0.0359
    - null
    - null
  - model: BS-KAGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.18380'
    title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: https://github.com/RomanBresson/KAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7297
    - null
    - null
    metric_stds:
    - 0.056299999999999996
    - null
    - null
  - model: GraphSAGE + NBA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.727
    - null
    - null
    metric_stds:
    - 0.0905
    - null
    - null
  - model: CoGSL_knn
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.727
    - null
    - null
    metric_stds:
    - 0.0426
    - null
    - null
  - model: ChebNet + NBA+LapPE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7243
    - null
    - null
    metric_stds:
    - 0.052
    - null
    - null
  - model: DIFFormer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.04765'
    title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7207
    - null
    - null
    metric_stds:
    - 0.0337
    - null
    - null
  - model: ProGNN_knn
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7189
    - null
    - null
    metric_stds:
    - 0.0569
    - null
    - null
  - model: RBF-KAGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.18380'
    title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: https://github.com/RomanBresson/KAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7171
    - null
    - null
    metric_stds:
    - 0.0649
    - null
    - null
  - model: NBA-GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7108
    - null
    - null
    metric_stds:
    - 0.0796
    - null
    - null
  - model: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7108
    - null
    - null
    metric_stds:
    - 0.0556
    - null
    - null
  - model: DR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7045999999999999
    - null
    - null
    metric_stds:
    - 0.0161
    - null
    - null
  - model: SDRF + Undirected
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.703
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
  - model: GRIT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.04765'
    title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7027
    - null
    - null
    metric_stds:
    - 0.0382
    - null
    - null
  - model: JDR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6956
    - null
    - null
    metric_stds:
    - 0.0171
    - null
    - null
  - model: NodeFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.04765'
    title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6937
    - null
    - null
    metric_stds:
    - 0.0255
    - null
    - null
  - model: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.18380'
    title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: https://github.com/RomanBresson/KAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6901
    - null
    - null
    metric_stds:
    - 0.061399999999999996
    - null
    - null
  - model: GCN (AFR-3)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.687
    - null
    - null
    metric_stds:
    - 0.031
    - null
    - null
  - model: NBA-GCN+LapPE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6811
    - null
    - null
    metric_stds:
    - 0.0595
    - null
    - null
  - model: ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6811
    - null
    - null
    metric_stds:
    - 0.0554
    - null
    - null
  - model: Geom-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.676
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: Geom-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6757
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: Baseline (GINE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.18917'
    title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse Problems'
    date: Jan 2026
    date_iso: 2026-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.674
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
  - model: Base
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.674
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
  - model: GAT + NBA+LapPE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.673
    - null
    - null
    metric_stds:
    - 0.0348
    - null
    - null
  - model: GCN (DEG)
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
    - 0.6676
    - null
    - null
    metric_stds:
    - 0.0272
    - null
    - null
  - model: SAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.04765'
    title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6667
    - null
    - null
    metric_stds:
    - 0.0337
    - null
    - null
  - model: GCN+JK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16560'
    title: Algorithmic Graph Tasks
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: https://github.com/nec-research/Adaptive-Message-Passing
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6648999999999999
    - null
    - null
    metric_stds:
    - 0.0664
    - null
    - null
  - model: GAT + NBA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6622
    - null
    - null
    metric_stds:
    - 0.0514
    - null
    - null
  - model: EGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6595
    - null
    - null
    metric_stds:
    - 0.0527
    - null
    - null
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2404.03380'
    title: On the Theoretical Expressive Power and the Design Space of Higher-Order
      Graph Transformers
    date: '2024-04-04'
    date_iso: '2024-04-04'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6595
    - null
    - null
    metric_stds:
    - 0.0367
    - null
    - null
  - model: GEN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6594
    - null
    - null
    metric_stds:
    - 0.0138
    - null
    - null
  - model: Base w. PE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.654
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
  - model: GINE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.65
    - null
    - null
    metric_stds:
    - 0.068
    - null
    - null
  - model: SDRF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.644
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
  - model: CensNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6405
    - null
    - null
    metric_stds:
    - 0.051
    - null
    - null
  - model: GIN (AFR-4)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.638
    - null
    - null
    metric_stds:
    - 0.038
    - null
    - null
  - model: DIGL + Undirected
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.635
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
  - model: ChebNet + LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6324
    - null
    - null
    metric_stds:
    - 0.0308
    - null
    - null
  - model: R-GCN (RWSE)
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
    - 0.6297
    - null
    - null
    metric_stds:
    - 0.0321
    - null
    - null
  - model: IDGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6243
    - null
    - null
    metric_stds:
    - 0.0609
    - null
    - null
  - model: GCN + BORF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.623
    - null
    - null
    metric_stds:
    - 0.02
    - null
    - null
  - model: GCN+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.501066
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6216
    - null
    - null
    metric_stds:
    - 0.0584
    - null
    - null
  - model: GRCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6216
    - null
    - null
    metric_stds:
    - 0.0705
    - null
    - null
  - model: + DIGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.62
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
  - model: FOSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6135
    - null
    - null
    metric_stds:
    - 0.0125
    - null
    - null
  - model: GAT (LapPE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6135
    - null
    - null
    metric_stds:
    - 0.0404
    - null
    - null
  - model: DeGTA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.04765'
    title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6126
    - null
    - null
    metric_stds:
    - 0.0127
    - null
    - null
  - model: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6108
    - null
    - null
    metric_stds:
    - 0.0652
    - null
    - null
  - model: GSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6081
    - null
    - null
    metric_stds:
    - 0.0487
    - null
    - null
  - model: Graph transformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.04765'
    title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6036
    - null
    - null
    metric_stds:
    - 0.0255
    - null
    - null
  - model: + PairNorm
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.6027
    - null
    - null
    metric_stds:
    - 0.0434
    - null
    - null
  - model: SRDF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5979
    - null
    - null
    metric_stds:
    - 0.0171
    - null
    - null
  - model: CoGSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5946
    - null
    - null
    metric_stds:
    - 0.0436
    - null
    - null
  - model: LDS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5892
    - null
    - null
    metric_stds:
    - 0.0432
    - null
    - null
  - model: NodeFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5892
    - null
    - null
    metric_stds:
    - 0.0432
    - null
    - null
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5783
    - null
    - null
    metric_stds:
    - 0.0276
    - null
    - null
  - model: LRGB
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.27529'
    title: Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in
      GNNs
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5736
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GTR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5718
    - null
    - null
    metric_stds:
    - 0.016399999999999998
    - null
    - null
  - model: Base (GAT)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5684
    - null
    - null
    metric_stds:
    - 0.0161
    - null
    - null
  - model: BORF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.563
    - null
    - null
    metric_stds:
    - 0.0161
    - null
    - null
  - model: Base (GCN)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5619
    - null
    - null
    metric_stds:
    - 0.0161
    - null
    - null
  - model: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.27529'
    title: Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in
      GNNs
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5605
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: FA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5593
    - null
    - null
    metric_stds:
    - 0.0176
    - null
    - null
  - model: + PANDA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03671'
    title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    date: '2024-06-06'
    date_iso: '2024-06-06'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.554
    - null
    - null
    metric_stds:
    - 0.016
    - null
    - null
  - model: STABLE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5524
    - null
    - null
    metric_stds:
    - 0.0604
    - null
    - null
  - model: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.18480'
    title: Scalable Graph Compressed Convolutions
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.551
    - null
    - null
    metric_stds:
    - 0.0623
    - null
    - null
  - model: CaCoSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.27529'
    title: Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in
      GNNs
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5447
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: BORF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.27529'
    title: Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in
      GNNs
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5421
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5405
    - null
    - null
    metric_stds:
    - 0.0735
    - null
    - null
  - model: GIN-E
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.538
    - null
    - null
    metric_stds:
    - 0.03
    - null
    - null
  - model: + DIGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03671'
    title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    date: '2024-06-06'
    date_iso: '2024-06-06'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.536
    - null
    - null
    metric_stds:
    - 0.015
    - null
    - null
  - model: SDRF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.27529'
    title: Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in
      GNNs
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5263
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: FOSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.27529'
    title: Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in
      GNNs
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5236999999999999
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GTR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.27529'
    title: Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in
      GNNs
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5236999999999999
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2603.27529'
    title: Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in
      GNNs
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5236
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GIN-SDRF-R
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.502
    - null
    - null
    metric_stds:
    - 0.034
    - null
    - null
  - model: BORF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03671'
    title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    date: '2024-06-06'
    date_iso: '2024-06-06'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.494
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
  - model: ProGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4837
    - null
    - null
    metric_stds:
    - 0.1217
    - null
    - null
  - model: GIN-FOSR-R
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.472
    - null
    - null
    metric_stds:
    - 0.036
    - null
    - null
  - model: GCN + FoSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.469
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
  - model: FOSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03671'
    title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    date: '2024-06-06'
    date_iso: '2024-06-06'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.46
    - null
    - null
    metric_stds:
    - 0.016
    - null
    - null
  - model: + DIGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4595
    - null
    - null
    metric_stds:
    - 0.0158
    - null
    - null
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.441
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
  - model: SDRF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03671'
    title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    date: '2024-06-06'
    date_iso: '2024-06-06'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.439
    - null
    - null
    metric_stds:
    - 0.016
    - null
    - null
  - model: GCN + SDRF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.436
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
  - model: Exphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.04765'
    title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3784
    - null
    - null
    metric_stds:
    - 0.0221
    - null
    - null
  - model: GOKU
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.27529'
    title: Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in
      GNNs
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.371
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: LASER
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.27529'
    title: Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in
      GNNs
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.32630000000000003
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: DAEGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.35
    - 0.14
    metric_stds:
    - null
    - 0.05
    - 0.02
  - model: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.31
    - 0.12
    metric_stds:
    - null
    - 0.03
    - 0.02
  - model: DMON
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.33
    - 0.21
    metric_stds:
    - null
    - 0.02
    - 0.04
  - model: GRACE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.29
    - 0.15
    metric_stds:
    - null
    - 0.08
    - 0.0
  - model: MVGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.29
    - 0.1
    metric_stds:
    - null
    - 0.02
    - 0.02
  - model: SUBLIME
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.21
    - 0.03
    metric_stds:
    - null
    - 0.03
    - 0.01
  - model: BGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.24
    - 0.06
    metric_stds:
    - null
    - 0.03
    - 0.03
  - model: VGAER
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.24
    - 0.08
    metric_stds:
    - null
    - 0.03
    - 0.02
  - model: uAGNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.33
    - 0.22
    metric_stds:
    - null
    - 0.09
    - 0.07
  - model: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04082'
    title: 'Curve Your Attention: Mixed-Curvature Transformers for Graph Representation
      Learning'
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7054
    - null
    metric_stds:
    - null
    - 0.03
    - null
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2309.04082'
    title: 'Curve Your Attention: Mixed-Curvature Transformers for Graph Representation
      Learning'
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.5784
    - null
    metric_stds:
    - null
    - 0.0162
    - null
  - model: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04082'
    title: 'Curve Your Attention: Mixed-Curvature Transformers for Graph Representation
      Learning'
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.5946
    - null
    metric_stds:
    - null
    - 0.0112
    - null
  - model: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04082'
    title: 'Curve Your Attention: Mixed-Curvature Transformers for Graph Representation
      Learning'
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.6838
    - null
    metric_stds:
    - null
    - 0.0354
    - null
  - model: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04082'
    title: 'Curve Your Attention: Mixed-Curvature Transformers for Graph Representation
      Learning'
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.5757
    - null
    metric_stds:
    - null
    - 0.0296
    - null
  - model: TokenGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04082'
    title: 'Curve Your Attention: Mixed-Curvature Transformers for Graph Representation
      Learning'
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.8865
    - null
    metric_stds:
    - null
    - 0.0206
    - null
  - model: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04082'
    title: 'Curve Your Attention: Mixed-Curvature Transformers for Graph Representation
      Learning'
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.5459
    - null
    metric_stds:
    - null
    - 0.0393
    - null
  - model: HGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04082'
    title: 'Curve Your Attention: Mixed-Curvature Transformers for Graph Representation
      Learning'
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.5081
    - null
    metric_stds:
    - null
    - 0.036
    - null
  - model: HAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04082'
    title: 'Curve Your Attention: Mixed-Curvature Transformers for Graph Representation
      Learning'
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.8216
    - null
    metric_stds:
    - null
    - 0.0252
    - null
  - model: \kappa-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04082'
    title: 'Curve Your Attention: Mixed-Curvature Transformers for Graph Representation
      Learning'
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.5622
    - null
    metric_stds:
    - null
    - 0.0438
    - null
  - model: \mathcal{Q}-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04082'
    title: 'Curve Your Attention: Mixed-Curvature Transformers for Graph Representation
      Learning'
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.5135
    - null
    metric_stds:
    - null
    - 0.0344
    - null
  - model: \modelname{}
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04082'
    title: 'Curve Your Attention: Mixed-Curvature Transformers for Graph Representation
      Learning'
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.8919
    - null
    metric_stds:
    - null
    - 0.0237
    - null
  milestones:
  - value: 0.9656
    std: 0.02
    model: ACMGCN
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: 2022-10
---

