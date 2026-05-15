---
title: Amazon-Photo
slug: amazon-photo
benchmark: Classic
task_type: node_classification
description: Amazon co-purchase graph (Photo) node classification.
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.Amazon.html
stats:
  num_graphs: null
  avg_nodes: 7650.0
  avg_edges: 238162.0
  num_classes: 8
result_count: 83
best_model:
  model: GENs
  value: 0.9712000000000001
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
  - MRR
  rows:
  - model: GENs
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9712000000000001
    - null
    metric_stds:
    - 0.0024
    - null
  - model: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9678
    - null
    metric_stds:
    - 0.0023
    - null
  - model: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.966
    - null
    metric_stds:
    - 0.0033
    - null
  - model: Polynormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9656999999999999
    - null
    metric_stds:
    - 0.0023
    - null
  - model: Nagphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9614
    - null
    metric_stds:
    - 0.0016
    - null
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.961
    - null
    metric_stds:
    - 0.0046
    - null
  - model: CARIBOU
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.22727'
    title: Convergent Privacy Framework for Multi-layer GNNs through Contractive Message
      Passing
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.958
    - null
    metric_stds:
    - null
    - null
  - model: Exphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9569
    - null
    metric_stds:
    - 0.0039000000000000003
    - null
  - model: SGFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9558
    - null
    metric_stds:
    - 0.0036
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
    is_best: false
    metric_values:
    - 0.9552
    - null
    metric_stds:
    - 0.0052
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
    - 0.9549
    - null
    metric_stds:
    - 0.0011
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
    - 0.9548
    - null
    metric_stds:
    - 0.0032
    - null
  - model: H2GCN
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
    - 0.9545
    - null
    metric_stds:
    - 0.0067
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
    is_best: false
    metric_values:
    - 0.9543
    - null
    metric_stds:
    - 0.0023
    - null
  - model: M
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9537
    - null
    metric_stds:
    - 0.0044
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
    - 0.9533
    - null
    metric_stds:
    - 0.0037
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
    - 0.9527
    - null
    metric_stds:
    - 0.0022
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
    is_best: false
    metric_values:
    - 0.951
    - null
    metric_stds:
    - 0.0078
    - null
  - model: GraphGPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9489
    - null
    metric_stds:
    - 0.0014000000000000002
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
    - 0.9449
    - null
    metric_stds:
    - 0.0033
    - null
  - model: GWNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9445
    - null
    metric_stds:
    - 0.0045
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
    - 0.9435
    - null
    metric_stds:
    - 0.0025
    - null
  - model: DEFT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9435
    - null
    metric_stds:
    - 0.0044
    - null
  - model: SEA-GWNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9435
    - null
    metric_stds:
    - 0.005
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
    - 0.9434
    - null
    metric_stds:
    - 0.0023
    - null
  - model: UFGConvS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9434
    - null
    metric_stds:
    - 0.0034
    - null
  - model: GOAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9433
    - null
    metric_stds:
    - 0.0021
    - null
  - model: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9432
    - null
    metric_stds:
    - 0.0014
    - null
  - model: WaveNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9409
    - null
    metric_stds:
    - 0.0063
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
    - 0.9408
    - null
    metric_stds:
    - 0.0137
    - null
  - model: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9387
    - null
    metric_stds:
    - 0.0011
    - null
  - model: GPRGNN
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
    - 0.9385
    - null
    metric_stds:
    - 0.0028
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
    - 0.9377
    - null
    metric_stds:
    - 0.0032
    - null
  - model: BernNet
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
    - 0.9363
    - null
    metric_stds:
    - 0.0035
    - null
  - model: WaveShrink-ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9354
    - null
    metric_stds:
    - 0.009
    - null
  - model: NodeFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9343
    - null
    metric_stds:
    - 0.005600000000000001
    - null
  - model: Scattering GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9307
    - null
    metric_stds:
    - 0.0042
    - null
  - model: GAP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.22727'
    title: Convergent Privacy Framework for Multi-layer GNNs through Contractive Message
      Passing
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.93
    - null
    metric_stds:
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
    - 0.9298000000000001
    - null
    metric_stds:
    - null
    - null
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.927
    - null
    metric_stds:
    - 0.002
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
    - 0.9251
    - null
    metric_stds:
    - null
    - null
  - model: DPDGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.22727'
    title: Convergent Privacy Framework for Multi-layer GNNs through Contractive Message
      Passing
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.925
    - null
    metric_stds:
    - null
    - null
  - model: SGWT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9245
    - null
    metric_stds:
    - 0.0062
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
    - 0.9212
    - null
    metric_stds:
    - null
    - null
  - model: Scattering
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.921
    - null
    metric_stds:
    - 0.0061
    - null
  - model: GAT
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
    - 0.9201
    - null
    metric_stds:
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
    - 0.9193000000000001
    - null
    metric_stds:
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
    - 0.9183
    - null
    metric_stds:
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
    - 0.9176000000000001
    - null
    metric_stds:
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
    - 0.9170999999999999
    - null
    metric_stds:
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
    - 0.9158
    - null
    metric_stds:
    - null
    - null
  - model: GAT
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
    - 0.9094
    - null
    metric_stds:
    - 0.0068
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
    is_best: false
    metric_values:
    - 0.8958
    - null
    metric_stds:
    - 0.0105
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
    - 0.8958
    - null
    metric_stds:
    - 0.0105
    - null
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: '2024-11-26'
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8826
    - null
    metric_stds:
    - 0.0073
    - null
  - model: GCN + SDRF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.07419'
    title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    date: Jan 2026
    date_iso: 2026-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.858
    - null
    metric_stds:
    - 0.040999999999999995
    - null
  - model: PertGraph
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.22727'
    title: Convergent Privacy Framework for Multi-layer GNNs through Contractive Message
      Passing
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.824
    - null
    metric_stds:
    - null
    - null
  - model: GCN + BORF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.07419'
    title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    date: Jan 2026
    date_iso: 2026-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.82
    - null
    metric_stds:
    - 0.057
    - null
  - model: DR
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
    - 0.7986
    - null
    metric_stds:
    - null
    - null
  - model: EGP (GCN)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.07419'
    title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    date: Jan 2026
    date_iso: 2026-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.779
    - null
    metric_stds:
    - 0.131
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
    - 0.7404000000000001
    - null
    metric_stds:
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
    - 0.6736
    - null
    metric_stds:
    - null
    - null
  - model: MMGCN + CLIP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 0.3138
    metric_stds:
    - null
    - 0.0008
  - model: MMGCN + ViT/T5
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 0.3083
    metric_stds:
    - null
    - 0.0007
  - model: MMGCN + ImageBind
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 0.3174
    metric_stds:
    - null
    - 0.0021
  - model: MMGCN + DINOv2/T5
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 0.3042
    metric_stds:
    - null
    - 0.0002
  - model: MGAT + CLIP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 0.2756
    metric_stds:
    - null
    - 0.003
  - model: MGAT + ViT/T5
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 0.3015
    metric_stds:
    - null
    - 0.0034
  - model: MGAT + ImageBind
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 0.3015
    metric_stds:
    - null
    - 0.0012
  - model: MGAT + DINOv2/T5
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 0.2891
    metric_stds:
    - null
    - 0.0009
  - model: GCN + ImageBind
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 0.3167
    metric_stds:
    - null
    - 0.0009
  - model: SAGE + CLIP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 0.3383
    metric_stds:
    - null
    - 0.0008
  - model: SAGE + ViT/T5
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 0.3201
    metric_stds:
    - null
    - 0.001
  - model: SAGE + ImageBind
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 0.3432
    metric_stds:
    - null
    - 0.0011
  - model: SAGE + DINOv2/T5
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 0.322
    metric_stds:
    - null
    - 0.0012
  - model: BUDDY + CLIP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 0.3155
    metric_stds:
    - null
    - 0.0013
  - model: BUDDY + ViT/T5
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 0.3041
    metric_stds:
    - null
    - 0.004
  - model: BUDDY + ImageBind
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 0.3302
    metric_stds:
    - null
    - 0.0044
  - model: BUDDY + DINOv2/T5
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 0.3002
    metric_stds:
    - null
    - 0.0034
  - model: MLP + CLIP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 0.2822
    metric_stds:
    - null
    - 0.0009
  - model: MLP + ViT/T5
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 0.2481
    metric_stds:
    - null
    - 0.0005
  - model: MLP + ImageBind
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 0.3045
    metric_stds:
    - null
    - 0.0014
  - model: MLP + DINOv2/T5
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 0.2481
    metric_stds:
    - null
    - 0.0016
  milestones:
  - value: 0.9712000000000001
    std: 0.0024
    model: GENs
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: 2024-01
---

