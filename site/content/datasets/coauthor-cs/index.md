---
title: Coauthor-CS
slug: coauthor-cs
benchmark: Classic
task_type: node_classification
description: Co-authorship graph (CS) node classification from the "Pitfalls of Graph
  Neural Network Evaluation" paper.
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.Coauthor.html
stats: null
result_count: 306
best_model:
  model: DAM-GT
  value: 0.9626
  metric: Accuracy
  arxiv_id: '2505.17660'
  paper_title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
    for Node Classification'
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
  - Macro-F1
  - Micro-F1
  - NDCG
  - mAP
  rows:
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
    is_best: true
    metric_values:
    - 0.9626
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0008
    - null
    - null
    - null
    - null
  - model: SGT
    model_plain: SGT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: May 22, 2024
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: https://github.com/liun-online/WaveGC
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9589
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0034
    - null
    - null
    - null
    - null
  - model: Exphormer
    model_plain: Exphormer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.06147'
    title: 'Exphormer: Sparse Transformers for Graphs'
    date: Mar 10, 2023
    date_iso: '2023-03-10'
    date_display: Mar 2023
    codebase_url: https://github.com/hamed1375/Exphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9577
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0015
    - null
    - null
    - null
    - null
  - model: NAGphormer
    model_plain: NAGphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.06147'
    title: 'Exphormer: Sparse Transformers for Graphs'
    date: Mar 10, 2023
    date_iso: '2023-03-10'
    date_display: Mar 2023
    codebase_url: https://github.com/hamed1375/Exphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9575
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0009
    - null
    - null
    - null
    - null
  - model: H2GCN
    model_plain: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9571
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
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
    - 0.9568
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0008
    - null
    - null
    - null
    - null
  - model: novel graph MLP mixer
    model_plain: novel graph MLP mixer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16358'
    title: 'ChebMixer: Efficient Graph Representation Learning with MLP Mixer'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9553
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0013
    - null
    - null
    - null
    - null
  - model: GRACE
    model_plain: GRACE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.12140'
    title: Graph Few-Shot Learning via Adaptive Spectrum Experts and Cross-Set Distribution
      Calibration
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/KEAML-JLU/GRACE
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.955
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.013
    - null
    - null
    - null
    - null
  - model: UFGConvS
    model_plain: UFGConvS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: May 22, 2024
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: https://github.com/liun-online/WaveGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9546
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0033
    - null
    - null
    - null
    - null
  - model: SimMLP
    model_plain: SimMLP
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
    - 0.9543
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0015
    - null
    - null
    - null
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
    - 0.9537
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0004
    - null
    - null
    - null
    - null
  - model: LSGNN
    model_plain: LSGNN
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
    - 0.9519
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0042
    - null
    - null
    - null
    - null
  - model: Scattering GCN
    model_plain: Scattering GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: May 22, 2024
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: https://github.com/liun-online/WaveGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9518
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
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
    - 0.9517
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0014
    - null
    - null
    - null
    - null
  - model: GPRGNN
    model_plain: GPRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16358'
    title: 'ChebMixer: Efficient Graph Representation Learning with MLP Mixer'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9513
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0006
    - null
    - null
    - null
    - null
  - model: SEA-GWNN
    model_plain: SEA-GWNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: May 22, 2024
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: https://github.com/liun-online/WaveGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9511
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0037
    - null
    - null
    - null
    - null
  - model: DEFT
    model_plain: DEFT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: May 22, 2024
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: https://github.com/liun-online/WaveGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9504
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0032
    - null
    - null
    - null
    - null
  - model: FOSSIL v2
    model_plain: FOSSIL v2
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9504
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0003
    - null
    - null
    - null
    - null
  - model: WaveNet
    model_plain: WaveNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: May 22, 2024
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: https://github.com/liun-online/WaveGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9491
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0029
    - null
    - null
    - null
    - null
  - model: WaveShrink-ChebNet
    model_plain: WaveShrink-ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: May 22, 2024
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: https://github.com/liun-online/WaveGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.949
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
  - model: G-Zoom
    model_plain: G-Zoom
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.10698'
    title: Towards Graph Self-Supervised Learning with Contrastive Adjusted Zooming
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.949
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
  - model: Local-GCL
    model_plain: Local-GCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.04604'
    title: Localized Graph Contrastive Learning
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.949
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0019
    - null
    - null
    - null
    - null
  - model: LaplaceGNN
    model_plain: LaplaceGNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.20362'
    title: Self-Supervised Graph Learning via Spectral Bootstrapping and Laplacian-Based
      Augmentations
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9486
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0016
    - null
    - null
    - null
    - null
  - model: SGWT
    model_plain: SGWT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: May 22, 2024
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: https://github.com/liun-online/WaveGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9481
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0023
    - null
    - null
    - null
    - null
  - model: Scattering
    model_plain: Scattering
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: May 22, 2024
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: https://github.com/liun-online/WaveGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9477
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0033
    - null
    - null
    - null
    - null
  - model: GLR
    model_plain: GLR
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9468
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16358'
    title: 'ChebMixer: Efficient Graph Representation Learning with MLP Mixer'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9461
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0003
    - null
    - null
    - null
    - null
  - model: ChebNet
    model_plain: ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16358'
    title: 'ChebMixer: Efficient Graph Representation Learning with MLP Mixer'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9453
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0028
    - null
    - null
    - null
    - null
  - model: SAN
    model_plain: SAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.06147'
    title: 'Exphormer: Sparse Transformers for Graphs'
    date: Mar 10, 2023
    date_iso: '2023-03-10'
    date_display: Mar 2023
    codebase_url: https://github.com/hamed1375/Exphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9451
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0015
    - null
    - null
    - null
    - null
  - model: MLP
    model_plain: MLP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16358'
    title: 'ChebMixer: Efficient Graph Representation Learning with MLP Mixer'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9451
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0015
    - null
    - null
    - null
    - null
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: May 22, 2024
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: https://github.com/liun-online/WaveGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9449
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0007
    - null
    - null
    - null
    - null
  - model: FOSSIL
    model_plain: FOSSIL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9449
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0004
    - null
    - null
    - null
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
    - 0.9441
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0009
    - null
    - null
    - null
    - null
  - model: GCNII
    model_plain: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9416
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
  - model: ES-MLP
    model_plain: ES-MLP
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
    - 0.9415
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0011
    - null
    - null
    - null
    - null
  - model: SUGRL
    model_plain: SUGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9415
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0004
    - null
    - null
    - null
    - null
  - model: JK
    model_plain: JK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.941
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
  - model: Logistic Reg.-X
    model_plain: Logistic Reg.-X
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.941
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
  - model: SubG-Con
    model_plain: SubG-Con
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.10698'
    title: Towards Graph Self-Supervised Learning with Contrastive Adjusted Zooming
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.94
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
  - model: HyperGRL
    model_plain: HyperGRL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.94
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
  - model: GraphGPS
    model_plain: GraphGPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.06147'
    title: 'Exphormer: Sparse Transformers for Graphs'
    date: Mar 10, 2023
    date_iso: '2023-03-10'
    date_display: Mar 2023
    codebase_url: https://github.com/hamed1375/Exphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9393
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0012
    - null
    - null
    - null
    - null
  - model: Ada-Ugnn
    model_plain: Ada-Ugnn
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.01777'
    title: A Unified View on Graph Neural Networks as Graph Signal Denoising
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: https://github.com/alge24/ADA-UGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9392
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
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
    - 0.9392
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0008
    - null
    - null
    - null
    - null
  - model: Str-GCL
    model_plain: Str-GCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9389
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0004
    - null
    - null
    - null
    - null
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.01777'
    title: A Unified View on Graph Neural Networks as Graph Signal Denoising
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: https://github.com/alge24/ADA-UGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9384
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
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
    - 0.9362
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0005
    - null
    - null
    - null
    - null
  - model: GraphSAGE + MH-Aug (w/ Reg)
    model_plain: GraphSAGE + MH-Aug (w/ Reg)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9361
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0058
    - null
    - null
    - null
    - null
  - model: BNLL
    model_plain: BNLL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.936
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0003
    - null
    - null
    - null
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.03147'
    title: Learning Conjoint Attentions for Graph Neural Nets
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.936
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0001
    - null
    - null
    - null
    - null
  - model: Unifying Graph Contrastive Learning
    model_plain: Unifying Graph Contrastive Learning
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.08792'
    title: Unifying Graph Contrastive Learning with Flexible Contextual Scopes
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: https://github.com/zyzisastudyreallyhardguy/UGCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.934
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
  - model: CAT-I-MF
    model_plain: CAT-I-MF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.03147'
    title: Learning Conjoint Attentions for Graph Neural Nets
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.934
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0012
    - null
    - null
    - null
    - null
  - model: CCA-SSG
    model_plain: CCA-SSG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.04604'
    title: Localized Graph Contrastive Learning
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9331
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0022
    - null
    - null
    - null
    - null
  - model: GCA
    model_plain: GCA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.08792'
    title: Unifying Graph Contrastive Learning with Flexible Contextual Scopes
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: https://github.com/zyzisastudyreallyhardguy/UGCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.933
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
  - model: BGRL
    model_plain: BGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.08792'
    title: Unifying Graph Contrastive Learning with Flexible Contextual Scopes
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: https://github.com/zyzisastudyreallyhardguy/UGCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.933
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
  - model: CAT-I-SC
    model_plain: CAT-I-SC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.03147'
    title: Learning Conjoint Attentions for Graph Neural Nets
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.933
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0011
    - null
    - null
    - null
    - null
  - model: ADGCN-R
    model_plain: ADGCN-R
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.07295'
    title: Adversarial Graph Disentanglement with Component-specific Aggregation
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/SsGood/ADGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.933
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
  - model: SGCL
    model_plain: SGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9329
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0017
    - null
    - null
    - null
    - null
  - model: AFGRL
    model_plain: AFGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.04604'
    title: Localized Graph Contrastive Learning
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9327
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0017
    - null
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.01777'
    title: A Unified View on Graph Neural Networks as Graph Signal Denoising
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: https://github.com/alge24/ADA-UGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9323
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.07295'
    title: Adversarial Graph Disentanglement with Component-specific Aggregation
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/SsGood/ADGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.932
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
  - model: HAT-GAE
    model_plain: HAT-GAE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.12063'
    title: 'HAT-GAE: Self-Supervised Graph Auto-encoders with Hierarchical Adaptive
      Masking and Trainable Corruption'
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9317
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0025
    - null
    - null
    - null
    - null
  - model: GAT-NetMF
    model_plain: GAT-NetMF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.03147'
    title: Learning Conjoint Attentions for Graph Neural Nets
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9316
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0027
    - null
    - null
    - null
    - null
  - model: PaGCL
    model_plain: PaGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9315
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0017
    - null
    - null
    - null
    - null
  - model: rLap
    model_plain: rLap
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.04004'
    title: Randomized Schur Complement Views for Graph Contrastive Learning
    date: Jun 6, 2023
    date_iso: '2023-06-06'
    date_display: Jun 2023
    codebase_url: https://github.com/kvignesh1420/rlap
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.931
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0054
    - null
    - null
    - null
    - null
  - model: GCA
    model_plain: GCA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.04604'
    title: Localized Graph Contrastive Learning
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.931
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0001
    - null
    - null
    - null
    - null
  - model: lrGAE (8)
    model_plain: lrGAE (8)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.931
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
  - model: S^3-CL
    model_plain: S^3-CL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.08480'
    title: Eliciting Structural and Semantic Global Knowledge in Unsupervised Graph
      Contrastive Learning
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/kaize0409/S-3-CL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.931
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
  - model: SSGE
    model_plain: SSGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.20362'
    title: Self-Supervised Graph Learning via Spectral Bootstrapping and Laplacian-Based
      Augmentations
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9306
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0041
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.03147'
    title: Learning Conjoint Attentions for Graph Neural Nets
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9306
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
  - model: Supervised GCN
    model_plain: Supervised GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.20362'
    title: Self-Supervised Graph Learning via Spectral Bootstrapping and Laplacian-Based
      Augmentations
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9303
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0031
    - null
    - null
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.03147'
    title: Learning Conjoint Attentions for Graph Neural Nets
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9303
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0074
    - null
    - null
    - null
    - null
  - model: GRACE
    model_plain: GRACE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9301
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0003
    - null
    - null
    - null
    - null
  - model: GRACE
    model_plain: GRACE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.04604'
    title: Localized Graph Contrastive Learning
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9293
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0001
    - null
    - null
    - null
    - null
  - model: GAT-Deep
    model_plain: GAT-Deep
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.03147'
    title: Learning Conjoint Attentions for Graph Neural Nets
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9293
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0017
    - null
    - null
    - null
    - null
  - model: BLEND
    model_plain: BLEND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.09443'
    title: Beltrami Flow and Neural Diffusion on Graphs
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: https://github.com/twitter-research/graph-neural-pde
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.929
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
  - model: MaskGAE
    model_plain: MaskGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.929
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
  - model: lrGAE (6)
    model_plain: lrGAE (6)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.929
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
  - model: AD-GCN
    model_plain: AD-GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.07295'
    title: Adversarial Graph Disentanglement with Component-specific Aggregation
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/SsGood/ADGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.929
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.01777'
    title: A Unified View on Graph Neural Networks as Graph Signal Denoising
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: https://github.com/alge24/ADA-UGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9286
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
  - model: GraphSAGE + UDA*
    model_plain: GraphSAGE + UDA*
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9283
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0039
    - null
    - null
    - null
    - null
  - model: NodeDropping
    model_plain: NodeDropping
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.04004'
    title: Randomized Schur Complement Views for Graph Contrastive Learning
    date: Jun 6, 2023
    date_iso: '2023-06-06'
    date_display: Jun 2023
    codebase_url: https://github.com/kvignesh1420/rlap
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9281
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0089
    - null
    - null
    - null
    - null
  - model: GRACE
    model_plain: GRACE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.10698'
    title: Towards Graph Self-Supervised Learning with Contrastive Adjusted Zooming
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.928
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
  - model: FMLP-O
    model_plain: FMLP-O
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.06631'
    title: Frameless Graph Knowledge Distillation
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: https://github.com/dshi3553usyd/Frameless_Graph_Distillation.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.928
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0037
    - null
    - null
    - null
    - null
  - model: SeeGera
    model_plain: SeeGera
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.928
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
  - model: lrGAE (7)
    model_plain: lrGAE (7)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.928
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
  - model: GraphMAE
    model_plain: GraphMAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.12063'
    title: 'HAT-GAE: Self-Supervised Graph Auto-encoders with Hierarchical Adaptive
      Masking and Trainable Corruption'
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9279
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
  - model: PPRDiffusion
    model_plain: PPRDiffusion
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.04004'
    title: Randomized Schur Complement Views for Graph Contrastive Learning
    date: Jun 6, 2023
    date_iso: '2023-06-06'
    date_display: Jun 2023
    codebase_url: https://github.com/kvignesh1420/rlap
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9275
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0058
    - null
    - null
    - null
    - null
  - model: GPT-GNN
    model_plain: GPT-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.12063'
    title: 'HAT-GAE: Self-Supervised Graph Auto-encoders with Hierarchical Adaptive
      Masking and Trainable Corruption'
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9271
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0009
    - null
    - null
    - null
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.10698'
    title: Towards Graph Self-Supervised Learning with Contrastive Adjusted Zooming
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.927
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
  - model: GAT-k-Lap
    model_plain: GAT-k-Lap
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.03147'
    title: Learning Conjoint Attentions for Graph Neural Nets
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.927
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0031
    - null
    - null
    - null
    - null
  - model: LGD-GCN
    model_plain: LGD-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.07295'
    title: Adversarial Graph Disentanglement with Component-specific Aggregation
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/SsGood/ADGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.927
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
  - model: MarkovDiffusion
    model_plain: MarkovDiffusion
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.04004'
    title: Randomized Schur Complement Views for Graph Contrastive Learning
    date: Jun 6, 2023
    date_iso: '2023-06-06'
    date_display: Jun 2023
    codebase_url: https://github.com/kvignesh1420/rlap
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9269
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0059
    - null
    - null
    - null
    - null
  - model: GCA
    model_plain: GCA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9265
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0032
    - null
    - null
    - null
    - null
  - model: GraphSAGE + BVAT
    model_plain: GraphSAGE + BVAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9263
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0048
    - null
    - null
    - null
    - null
  - model: SP^2GCL
    model_plain: SP^2GCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.20362'
    title: Self-Supervised Graph Learning via Spectral Bootstrapping and Laplacian-Based
      Augmentations
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9261
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0024
    - null
    - null
    - null
    - null
  - model: PaGCL
    model_plain: PaGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.926
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
  - model: S2GAE
    model_plain: S2GAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.926
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
  - model: BGRL
    model_plain: BGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.04604'
    title: Localized Graph Contrastive Learning
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9259
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0017
    - null
    - null
    - null
    - null
  - model: KNN w/ sp.-X
    model_plain: KNN w/ sp.-X
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9258
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
  - model: PushNet-TPP
    model_plain: PushNet-TPP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.02228'
    title: 'PushNet: Efficient and Adaptive Neural Message Passing'
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: https://github.com/buschju/pushnet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9254
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0034
    - null
    - null
    - null
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
    - 0.9252
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0015
    - null
    - null
    - null
    - null
  - model: RandomWalkSubgraph
    model_plain: RandomWalkSubgraph
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.04004'
    title: Randomized Schur Complement Views for Graph Contrastive Learning
    date: Jun 6, 2023
    date_iso: '2023-06-06'
    date_display: Jun 2023
    codebase_url: https://github.com/kvignesh1420/rlap
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9251
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0029
    - null
    - null
    - null
    - null
  - model: FS-GCN
    model_plain: FS-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.925
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0002
    - null
    - null
    - null
    - null
  - model: GRACE
    model_plain: GRACE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.925
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
  - model: SGCL
    model_plain: SGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.925
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
  - model: EdgeDroppingPR
    model_plain: EdgeDroppingPR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.04004'
    title: Randomized Schur Complement Views for Graph Contrastive Learning
    date: Jun 6, 2023
    date_iso: '2023-06-06'
    date_display: Jun 2023
    codebase_url: https://github.com/kvignesh1420/rlap
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9245
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0051
    - null
    - null
    - null
    - null
  - model: GGD
    model_plain: GGD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.924
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
  - model: GiGaMAE
    model_plain: GiGaMAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.924
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
  - model: MERIT
    model_plain: MERIT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.08480'
    title: Eliciting Structural and Semantic Global Knowledge in Unsupervised Graph
      Contrastive Learning
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/kaize0409/S-3-CL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.924
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
  - model: ARMA
    model_plain: ARMA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.07295'
    title: Adversarial Graph Disentanglement with Component-specific Aggregation
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/SsGood/ADGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.924
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
  - model: PushNet
    model_plain: PushNet
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.02228'
    title: 'PushNet: Efficient and Adaptive Neural Message Passing'
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: https://github.com/buschju/pushnet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.924
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0052
    - null
    - null
    - null
    - null
  - model: TEG
    model_plain: TEG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.12140'
    title: Graph Few-Shot Learning via Adaptive Spectrum Experts and Cross-Set Distribution
      Calibration
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/KEAML-JLU/GRACE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9236
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0159
    - null
    - null
    - null
    - null
  - model: CoATA
    model_plain: CoATA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.22299'
    title: 'CoATA: Effective Co-Augmentation of Topology and Attribute for Graph Neural
      Networks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9231
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0029
    - null
    - null
    - null
    - null
  - model: CPGNN
    model_plain: CPGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.09443'
    title: Beltrami Flow and Neural Diffusion on Graphs
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: https://github.com/twitter-research/graph-neural-pde
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.923
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
  - model: BLEND-kNN
    model_plain: BLEND-kNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.09443'
    title: Beltrami Flow and Neural Diffusion on Graphs
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: https://github.com/twitter-research/graph-neural-pde
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.923
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
  - model: CG3
    model_plain: CG3
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.10698'
    title: Towards Graph Self-Supervised Learning with Contrastive Adjusted Zooming
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.923
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
  - model: EdgeDroppingEVC
    model_plain: EdgeDroppingEVC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.04004'
    title: Randomized Schur Complement Views for Graph Contrastive Learning
    date: Jun 6, 2023
    date_iso: '2023-06-06'
    date_display: Jun 2023
    codebase_url: https://github.com/kvignesh1420/rlap
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.923
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0031
    - null
    - null
    - null
    - null
  - model: SpatUFG
    model_plain: SpatUFG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.06631'
    title: Frameless Graph Knowledge Distillation
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: https://github.com/dshi3553usyd/Frameless_Graph_Distillation.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.923
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0044
    - null
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.06972'
    title: Towards Deeper Graph Neural Networks with Differentiable Group Normalization
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9229999999999999
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
  - model: DGN
    model_plain: DGN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.06972'
    title: Towards Deeper Graph Neural Networks with Differentiable Group Normalization
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9229999999999999
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
  - model: GCN + UDA*
    model_plain: GCN + UDA*
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9226
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0037
    - null
    - null
    - null
    - null
  - model: GeoMix
    model_plain: GeoMix
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.22299'
    title: 'CoATA: Effective Co-Augmentation of Topology and Attribute for Graph Neural
      Networks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9223
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0014
    - null
    - null
    - null
    - null
  - model: GCN-DVAT
    model_plain: GCN-DVAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9221
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0037
    - null
    - null
    - null
    - null
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.10698'
    title: Towards Graph Self-Supervised Learning with Contrastive Adjusted Zooming
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.922
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
  - model: SUGRL
    model_plain: SUGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.08480'
    title: Eliciting Structural and Semantic Global Knowledge in Unsupervised Graph
      Contrastive Learning
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/kaize0409/S-3-CL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.922
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
  - model: AP-GCN
    model_plain: AP-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.07295'
    title: Adversarial Graph Disentanglement with Component-specific Aggregation
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/SsGood/ADGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.922
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
  - model: JK-GAT
    model_plain: JK-GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.02228'
    title: 'PushNet: Efficient and Adaptive Neural Message Passing'
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: https://github.com/buschju/pushnet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.922
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0043
    - null
    - null
    - null
    - null
  - model: G-Meta
    model_plain: G-Meta
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.12140'
    title: Graph Few-Shot Learning via Adaptive Spectrum Experts and Cross-Set Distribution
      Calibration
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/KEAML-JLU/GRACE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9214
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.039
    - null
    - null
    - null
    - null
  - model: MVGRL
    model_plain: MVGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.10698'
    title: Towards Graph Self-Supervised Learning with Contrastive Adjusted Zooming
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.921
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
  - model: VGAE
    model_plain: VGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.08792'
    title: Unifying Graph Contrastive Learning with Flexible Contextual Scopes
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: https://github.com/zyzisastudyreallyhardguy/UGCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.921
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
  - model: GCN + MH-Aug (w/ Reg)
    model_plain: GCN + MH-Aug (w/ Reg)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9208
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0058
    - null
    - null
    - null
    - null
  - model: FS-MLP
    model_plain: FS-MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9205
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0006
    - null
    - null
    - null
    - null
  - model: CCA-SSG
    model_plain: CCA-SSG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.12063'
    title: 'HAT-GAE: Self-Supervised Graph Auto-encoders with Hierarchical Adaptive
      Masking and Trainable Corruption'
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9205
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0019
    - null
    - null
    - null
    - null
  - model: GATNE
    model_plain: GATNE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.12063'
    title: 'HAT-GAE: Self-Supervised Graph Auto-encoders with Hierarchical Adaptive
      Masking and Trainable Corruption'
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9204
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0011
    - null
    - null
    - null
    - null
  - model: GAE
    model_plain: GAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.92
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
  - model: AF-GCL
    model_plain: AF-GCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.04604'
    title: Localized Graph Contrastive Learning
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9192
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
  - model: SUFG
    model_plain: SUFG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.06631'
    title: Frameless Graph Knowledge Distillation
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: https://github.com/dshi3553usyd/Frameless_Graph_Distillation.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.919
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0125
    - null
    - null
    - null
    - null
  - model: GraphMixer
    model_plain: GraphMixer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.22299'
    title: 'CoATA: Effective Co-Augmentation of Topology and Attribute for Graph Neural
      Networks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9189
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0036
    - null
    - null
    - null
    - null
  - model: InfoGCL
    model_plain: InfoGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.12063'
    title: 'HAT-GAE: Self-Supervised Graph Auto-encoders with Hierarchical Adaptive
      Masking and Trainable Corruption'
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9189
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0024
    - null
    - null
    - null
    - null
  - model: GraphSAGE + DropEdge
    model_plain: GraphSAGE + DropEdge
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9184
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0076
    - null
    - null
    - null
    - null
  - model: GCN + GraphMix
    model_plain: GCN + GraphMix
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9183
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0051
    - null
    - null
    - null
    - null
  - model: BGRL
    model_plain: BGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9181
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0022
    - null
    - null
    - null
    - null
  - model: PL
    model_plain: PL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.09532'
    title: Pseudo Contrastive Learning for Graph-based Semi-supervised Learning
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9181
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.08480'
    title: Eliciting Structural and Semantic Global Knowledge in Unsupervised Graph
      Contrastive Learning
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/kaize0409/S-3-CL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.918
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
  - model: GAT + UDA*
    model_plain: GAT + UDA*
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9178
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0023
    - null
    - null
    - null
    - null
  - model: GCN + DropEdge
    model_plain: GCN + DropEdge
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9169
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0043
    - null
    - null
    - null
    - null
  - model: GDE
    model_plain: GDE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.09443'
    title: Beltrami Flow and Neural Diffusion on Graphs
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: https://github.com/twitter-research/graph-neural-pde
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.916
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
  - model: GCNJK
    model_plain: GCNJK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.02228'
    title: 'PushNet: Efficient and Adaptive Neural Message Passing'
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: https://github.com/buschju/pushnet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.916
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0054
    - null
    - null
    - null
    - null
  - model: Diffusion-A
    model_plain: Diffusion-A
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9155
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.06972'
    title: Towards Deeper Graph Neural Networks with Differentiable Group Normalization
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.915
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.915
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.02228'
    title: 'PushNet: Efficient and Adaptive Neural Message Passing'
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: https://github.com/buschju/pushnet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9146
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0054
    - null
    - null
    - null
    - null
  - model: GCN + Vanilla
    model_plain: GCN + Vanilla
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9145
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0028
    - null
    - null
    - null
    - null
  - model: MixUp
    model_plain: MixUp
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.22299'
    title: 'CoATA: Effective Co-Augmentation of Topology and Attribute for Graph Neural
      Networks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9136
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0037
    - null
    - null
    - null
    - null
  - model: GraphSAGE + Vanilla
    model_plain: GraphSAGE + Vanilla
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9135
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
    - null
    - null
  - model: EdgeDroppingDegree
    model_plain: EdgeDroppingDegree
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.04004'
    title: Randomized Schur Complement Views for Graph Contrastive Learning
    date: Jun 6, 2023
    date_iso: '2023-06-06'
    date_display: Jun 2023
    codebase_url: https://github.com/kvignesh1420/rlap
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9132
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0052
    - null
    - null
    - null
    - null
  - model: GS-mean
    model_plain: GS-mean
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.05868'
    title: Pitfalls of Graph Neural Network Evaluation
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.913
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.028
    - null
    - null
    - null
    - null
  - model: GAT-ppr
    model_plain: GAT-ppr
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.09443'
    title: Beltrami Flow and Neural Diffusion on Graphs
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: https://github.com/twitter-research/graph-neural-pde
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.913
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
  - model: MVGRL
    model_plain: MVGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.08480'
    title: Eliciting Structural and Semantic Global Knowledge in Unsupervised Graph
      Contrastive Learning
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/kaize0409/S-3-CL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.913
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
  - model: SAGE-mean
    model_plain: SAGE-mean
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.07295'
    title: Adversarial Graph Disentanglement with Component-specific Aggregation
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/SsGood/ADGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.913
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.028
    - null
    - null
    - null
    - null
  - model: S^3-CL
    model_plain: S^3-CL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.22299'
    title: 'CoATA: Effective Co-Augmentation of Topology and Attribute for Graph Neural
      Networks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9129
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0017
    - null
    - null
    - null
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.02228'
    title: 'PushNet: Efficient and Adaptive Neural Message Passing'
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: https://github.com/buschju/pushnet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9127
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0058
    - null
    - null
    - null
    - null
  - model: Meta-BP
    model_plain: Meta-BP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.12140'
    title: Graph Few-Shot Learning via Adaptive Spectrum Experts and Cross-Set Distribution
      Calibration
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/KEAML-JLU/GRACE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9119
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0221
    - null
    - null
    - null
    - null
  - model: GRACE
    model_plain: GRACE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.20362'
    title: Self-Supervised Graph Learning via Spectral Bootstrapping and Laplacian-Based
      Augmentations
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9112
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.05868'
    title: Pitfalls of Graph Neural Network Evaluation
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.911
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
  - model: GAT + DropEdge
    model_plain: GAT + DropEdge
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.911
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0037
    - null
    - null
    - null
    - null
  - model: STGCN
    model_plain: STGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.07295'
    title: Adversarial Graph Disentanglement with Component-specific Aggregation
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/SsGood/ADGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.911
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.017
    - null
    - null
    - null
    - null
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.02228'
    title: 'PushNet: Efficient and Adaptive Neural Message Passing'
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: https://github.com/buschju/pushnet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.911
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0112
    - null
    - null
    - null
    - null
  - model: PushNet-PTP
    model_plain: PushNet-PTP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.02228'
    title: 'PushNet: Efficient and Adaptive Neural Message Passing'
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: https://github.com/buschju/pushnet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9104
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0076
    - null
    - null
    - null
    - null
  - model: GMI
    model_plain: GMI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.08480'
    title: Eliciting Structural and Semantic Global Knowledge in Unsupervised Graph
      Contrastive Learning
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/kaize0409/S-3-CL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.91
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0
    - null
    - null
    - null
    - null
  - model: X-FNC
    model_plain: X-FNC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.12140'
    title: Graph Few-Shot Learning via Adaptive Spectrum Experts and Cross-Set Distribution
      Calibration
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/KEAML-JLU/GRACE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9095
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0429
    - null
    - null
    - null
    - null
  - model: GAT + Vanilla
    model_plain: GAT + Vanilla
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.909
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0031
    - null
    - null
    - null
    - null
  - model: FactorGCN
    model_plain: FactorGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.07295'
    title: Adversarial Graph Disentanglement with Component-specific Aggregation
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/SsGood/ADGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.909
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.023
    - null
    - null
    - null
    - null
  - model: GloGNN
    model_plain: GloGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.22299'
    title: 'CoATA: Effective Co-Augmentation of Topology and Attribute for Graph Neural
      Networks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9082
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0045
    - null
    - null
    - null
    - null
  - model: MoNet
    model_plain: MoNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.05868'
    title: Pitfalls of Graph Neural Network Evaluation
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.908
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
  - model: GWNN
    model_plain: GWNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: May 22, 2024
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: https://github.com/liun-online/WaveGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9075
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0059
    - null
    - null
    - null
    - null
  - model: SimP-GCN
    model_plain: SimP-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.22299'
    title: 'CoATA: Effective Co-Augmentation of Topology and Attribute for Graph Neural
      Networks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9054
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0045
    - null
    - null
    - null
    - null
  - model: PSAGNN
    model_plain: PSAGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.22299'
    title: 'CoATA: Effective Co-Augmentation of Topology and Attribute for Graph Neural
      Networks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9052
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0032
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.05868'
    title: Pitfalls of Graph Neural Network Evaluation
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.905
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.08792'
    title: Unifying Graph Contrastive Learning with Flexible Contextual Scopes
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: https://github.com/zyzisastudyreallyhardguy/UGCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.904
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
  - model: TLP
    model_plain: TLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.12140'
    title: Graph Few-Shot Learning via Adaptive Spectrum Experts and Cross-Set Distribution
      Calibration
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/KEAML-JLU/GRACE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9035
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0449
    - null
    - null
    - null
    - null
  - model: GCN + AdaEdge
    model_plain: GCN + AdaEdge
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.903
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
  - model: GraphSAGE + AdaEdge
    model_plain: GraphSAGE + AdaEdge
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.903
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
  - model: GLNN
    model_plain: GLNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.06631'
    title: Frameless Graph Knowledge Distillation
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: https://github.com/dshi3553usyd/Frameless_Graph_Distillation.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.903
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0081
    - null
    - null
    - null
    - null
  - model: GSC
    model_plain: GSC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9016
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0006
    - null
    - null
    - null
    - null
  - model: Meta-GPS
    model_plain: Meta-GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.12140'
    title: Graph Few-Shot Learning via Adaptive Spectrum Experts and Cross-Set Distribution
      Calibration
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/KEAML-JLU/GRACE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9016
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0272
    - null
    - null
    - null
    - null
  - model: GRACE
    model_plain: GRACE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.08480'
    title: Eliciting Structural and Semantic Global Knowledge in Unsupervised Graph
      Contrastive Learning
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/kaize0409/S-3-CL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.901
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
  - model: GAE
    model_plain: GAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.08792'
    title: Unifying Graph Contrastive Learning with Flexible Contextual Scopes
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: https://github.com/zyzisastudyreallyhardguy/UGCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.08480'
    title: Eliciting Structural and Semantic Global Knowledge in Unsupervised Graph
      Contrastive Learning
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/kaize0409/S-3-CL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
  - model: EdgeAddition
    model_plain: EdgeAddition
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.04004'
    title: Randomized Schur Complement Views for Graph Contrastive Learning
    date: Jun 6, 2023
    date_iso: '2023-06-06'
    date_display: Jun 2023
    codebase_url: https://github.com/kvignesh1420/rlap
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8994
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0072
    - null
    - null
    - null
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.06972'
    title: Towards Deeper Graph Neural Networks with Differentiable Group Normalization
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.899
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
  - model: JK-Net
    model_plain: JK-Net
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.03147'
    title: Learning Conjoint Attentions for Graph Neural Nets
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8962
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0001
    - null
    - null
    - null
    - null
  - model: GS-meanpool
    model_plain: GS-meanpool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.05868'
    title: Pitfalls of Graph Neural Network Evaluation
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.896
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
    - null
    - null
  - model: SAGE-maxpool
    model_plain: SAGE-maxpool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.07295'
    title: Adversarial Graph Disentanglement with Component-specific Aggregation
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/SsGood/ADGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.896
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
    - null
    - null
  - model: TENT
    model_plain: TENT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.12140'
    title: Graph Few-Shot Learning via Adaptive Spectrum Experts and Cross-Set Distribution
      Calibration
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/KEAML-JLU/GRACE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8935
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0449
    - null
    - null
    - null
    - null
  - model: COSMIC
    model_plain: COSMIC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.12140'
    title: Graph Few-Shot Learning via Adaptive Spectrum Experts and Cross-Set Distribution
      Calibration
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/KEAML-JLU/GRACE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8935
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0449
    - null
    - null
    - null
    - null
  - model: GraphSAGE + GraphMix
    model_plain: GraphSAGE + GraphMix
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8929
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0045
    - null
    - null
    - null
    - null
  - model: GSC+Cheb
    model_plain: GSC+Cheb
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.892
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0014
    - null
    - null
    - null
    - null
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.03147'
    title: Learning Conjoint Attentions for Graph Neural Nets
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8916
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0065
    - null
    - null
    - null
    - null
  - model: Diffusion-X
    model_plain: Diffusion-X
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8847
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.05868'
    title: Pitfalls of Graph Neural Network Evaluation
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.883
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
  - model: DSSL
    model_plain: DSSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8773
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0008
    - null
    - null
    - null
    - null
  - model: GraphMAE
    model_plain: GraphMAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.20362'
    title: Self-Supervised Graph Learning via Spectral Bootstrapping and Laplacian-Based
      Augmentations
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.877
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0004
    - null
    - null
    - null
    - null
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8738
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0006
    - null
    - null
    - null
    - null
  - model: GAT + AdaEdge
    model_plain: GAT + AdaEdge
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.866
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0016
    - null
    - null
    - null
    - null
  - model: LogReg
    model_plain: LogReg
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.05868'
    title: Pitfalls of Graph Neural Network Evaluation
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.864
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
    - null
    - null
  - model: ARMA
    model_plain: ARMA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.03147'
    title: Learning Conjoint Attentions for Graph Neural Nets
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8628
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0075
    - null
    - null
    - null
    - null
  - model: ILLS
    model_plain: ILLS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.862
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
  - model: GCL-LR-Attention
    model_plain: GCL-LR-Attention
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.861
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
  - model: GRAND
    model_plain: GRAND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.858
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
  - model: GCL-LRR
    model_plain: GCL-LRR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.858
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
  - model: Meta-GNN
    model_plain: Meta-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.12140'
    title: Graph Few-Shot Learning via Adaptive Spectrum Experts and Cross-Set Distribution
      Calibration
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/KEAML-JLU/GRACE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8576
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0274
    - null
    - null
    - null
    - null
  - model: GPN
    model_plain: GPN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.12140'
    title: Graph Few-Shot Learning via Adaptive Spectrum Experts and Cross-Set Distribution
      Calibration
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/KEAML-JLU/GRACE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.856
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0215
    - null
    - null
    - null
    - null
  - model: KNN w/ sp.-A
    model_plain: KNN w/ sp.-A
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8522
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
  - model: PNA
    model_plain: PNA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.851
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
  - model: Node2Vec
    model_plain: Node2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.08792'
    title: Unifying Graph Contrastive Learning with Flexible Contextual Scopes
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: https://github.com/zyzisastudyreallyhardguy/UGCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.851
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
  - model: GS-maxpool
    model_plain: GS-maxpool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.05868'
    title: Pitfalls of Graph Neural Network Evaluation
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.85
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
    - null
    - null
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.848
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
  - model: UGMAE
    model_plain: UGMAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.20362'
    title: Self-Supervised Graph Learning via Spectral Bootstrapping and Laplacian-Based
      Augmentations
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8461
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0022
    - null
    - null
    - null
    - null
  - model: DeepWalk
    model_plain: DeepWalk
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.08792'
    title: Unifying Graph Contrastive Learning with Flexible Contextual Scopes
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: https://github.com/zyzisastudyreallyhardguy/UGCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.846
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
  - model: ARIEL
    model_plain: ARIEL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.843
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.842
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
  - model: CRGNN
    model_plain: CRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.842
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.839
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
  - model: SFA
    model_plain: SFA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.839
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
    - null
    - null
  - model: GFSA
    model_plain: GFSA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.837
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.835
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
  - model: S^2GC
    model_plain: S^2GC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.835
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
  - model: CPGNN
    model_plain: CPGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.835
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
  - model: SUGRL
    model_plain: SUGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.834
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
  - model: HONGAT
    model_plain: HONGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.833
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
  - model: Logistic Reg.-A
    model_plain: Logistic Reg.-A
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8319
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.831
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
  - model: MERIT
    model_plain: MERIT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.831
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
  - model: RTGNN
    model_plain: RTGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.828
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
  - model: Sel-Cl
    model_plain: Sel-Cl
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.828
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
  - model: Jo-SRC
    model_plain: Jo-SRC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.825
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
  - model: SubG-Con
    model_plain: SubG-Con
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8229
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0054
    - null
    - null
    - null
    - null
  - model: NGNN
    model_plain: NGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.822
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
  - model: UnionNET
    model_plain: UnionNET
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.82
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
  - model: GCE
    model_plain: GCE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.819
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.815
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
  - model: FMLP-S
    model_plain: FMLP-S
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.06631'
    title: Frameless Graph Knowledge Distillation
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: https://github.com/dshi3553usyd/Frameless_Graph_Distillation.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.802
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0321
    - null
    - null
    - null
    - null
  - model: GAE_f
    model_plain: GAE_f
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
  - model: LabelProp NL
    model_plain: LabelProp NL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.05868'
    title: Pitfalls of Graph Neural Network Evaluation
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.767
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
    - null
    - null
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.08480'
    title: Eliciting Structural and Semantic Global Knowledge in Unsupervised Graph
      Contrastive Learning
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/kaize0409/S-3-CL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.765
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.12140'
    title: Graph Few-Shot Learning via Adaptive Spectrum Experts and Cross-Set Distribution
      Calibration
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/KEAML-JLU/GRACE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7549
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0215
    - null
    - null
    - null
    - null
  - model: LP
    model_plain: LP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.05868'
    title: Pitfalls of Graph Neural Network Evaluation
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.736
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.039
    - null
    - null
    - null
    - null
  - model: LabelProp
    model_plain: LabelProp
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.07295'
    title: Adversarial Graph Disentanglement with Component-specific Aggregation
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/SsGood/ADGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.736
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.039
    - null
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.12140'
    title: Graph Few-Shot Learning via Adaptive Spectrum Experts and Cross-Set Distribution
      Calibration
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/KEAML-JLU/GRACE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7352
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0197
    - null
    - null
    - null
    - null
  - model: ProtoNet
    model_plain: ProtoNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.12140'
    title: Graph Few-Shot Learning via Adaptive Spectrum Experts and Cross-Set Distribution
      Calibration
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/KEAML-JLU/GRACE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7118
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0382
    - null
    - null
    - null
    - null
  - model: k-means+EGG 0.8 (99.48%)
    model_plain: k-means+EGG 0.8 (99.48%)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15068'
    title: Embedding Graphs on Grassmann Manifold
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/conf20/Egg
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.67
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0201
    - null
    - null
    - null
    - null
  - model: GraphMAE SpikingGPF
    model_plain: GraphMAE SpikingGPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6453
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0601
    - null
    - null
    - null
    - null
  - model: K-means
    model_plain: K-means
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15068'
    title: Embedding Graphs on Grassmann Manifold
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/conf20/Egg
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.641
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0171
    - null
    - null
    - null
    - null
  - model: EdgePred SpikingGPF
    model_plain: EdgePred SpikingGPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6332
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0654
    - null
    - null
    - null
    - null
  - model: GraphCL SpikingGPF
    model_plain: GraphCL SpikingGPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6248
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0372
    - null
    - null
    - null
    - null
  - model: GraphMAE GPF-plus
    model_plain: GraphMAE GPF-plus
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6239
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0575
    - null
    - null
    - null
    - null
  - model: MAML
    model_plain: MAML
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.12140'
    title: Graph Few-Shot Learning via Adaptive Spectrum Experts and Cross-Set Distribution
      Calibration
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/KEAML-JLU/GRACE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6232
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.046
    - null
    - null
    - null
    - null
  - model: GraphMAE GPF
    model_plain: GraphMAE GPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6177
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0534
    - null
    - null
    - null
    - null
  - model: EdgePred GPF
    model_plain: EdgePred GPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6043
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0844
    - null
    - null
    - null
    - null
  - model: EdgePred GPF-plus
    model_plain: EdgePred GPF-plus
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6025
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0671
    - null
    - null
    - null
    - null
  - model: GPPT
    model_plain: GPPT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.5997
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0582
    - null
    - null
    - null
    - null
  - model: DeepWalk
    model_plain: DeepWalk
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.12140'
    title: Graph Few-Shot Learning via Adaptive Spectrum Experts and Cross-Set Distribution
      Calibration
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/KEAML-JLU/GRACE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5952
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0272
    - null
    - null
    - null
    - null
  - model: k-means+EGG 0.5 (90.73%)
    model_plain: k-means+EGG 0.5 (90.73%)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15068'
    title: Embedding Graphs on Grassmann Manifold
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/conf20/Egg
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5878
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0188
    - null
    - null
    - null
    - null
  - model: GraphCL GPF
    model_plain: GraphCL GPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.5778
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0819
    - null
    - null
    - null
    - null
  - model: Node2Vec
    model_plain: Node2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.12140'
    title: Graph Few-Shot Learning via Adaptive Spectrum Experts and Cross-Set Distribution
      Calibration
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/KEAML-JLU/GRACE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5616
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0419
    - null
    - null
    - null
    - null
  - model: GraphCL GPF-plus
    model_plain: GraphCL GPF-plus
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.5564
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0681
    - null
    - null
    - null
    - null
  - model: GraphPrompt
    model_plain: GraphPrompt
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.556
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0521
    - null
    - null
    - null
    - null
  - model: k-means+EGG 0.2 (45.05%)
    model_plain: k-means+EGG 0.2 (45.05%)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15068'
    title: Embedding Graphs on Grassmann Manifold
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/conf20/Egg
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5483
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.025
    - null
    - null
    - null
    - null
  - model: MUSE
    model_plain: MUSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5432
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0176
    - null
    - null
    - null
    - null
  - model: GraphCL Fine-Tuning
    model_plain: GraphCL Fine-Tuning
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.5123
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0505
    - null
    - null
    - null
    - null
  - model: GraphMAE Fine-Tuning
    model_plain: GraphMAE Fine-Tuning
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.503
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0477
    - null
    - null
    - null
    - null
  - model: EdgePred Fine-Tuning
    model_plain: EdgePred Fine-Tuning
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.4948
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0596
    - null
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4794
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0489
    - null
    - null
    - null
    - null
  - model: SimGRACE SpikingGPF
    model_plain: SimGRACE SpikingGPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.4525
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.1054
    - null
    - null
    - null
    - null
  - model: SimGRACE Fine-Tuning
    model_plain: SimGRACE Fine-Tuning
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.4368
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0578
    - null
    - null
    - null
    - null
  - model: SimGRACE GPF-plus
    model_plain: SimGRACE GPF-plus
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.4299
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0402
    - null
    - null
    - null
    - null
  - model: GraphMAE All-in-One
    model_plain: GraphMAE All-in-One
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.4153
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.1035
    - null
    - null
    - null
    - null
  - model: SimGRACE GPF
    model_plain: SimGRACE GPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.3947
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0846
    - null
    - null
    - null
    - null
  - model: GraphCL All-in-One
    model_plain: GraphCL All-in-One
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.3581
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0932
    - null
    - null
    - null
    - null
  - model: EdgePred All-in-One
    model_plain: EdgePred All-in-One
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.3504
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0946
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3265
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0511
    - null
    - null
    - null
    - null
  - model: SimGRACE All-in-One
    model_plain: SimGRACE All-in-One
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.2951
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0889
    - null
    - null
    - null
    - null
  - model: HGT
    model_plain: HGT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.01332'
    title: Heterogeneous Graph Transformer
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: https://github.com/acbull/pyHGT
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.718
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.014
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.01332'
    title: Heterogeneous Graph Transformer
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: https://github.com/acbull/pyHGT
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.608
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.062
    - null
  - model: RGCN
    model_plain: RGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.01332'
    title: Heterogeneous Graph Transformer
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: https://github.com/acbull/pyHGT
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.603
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.065
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.01332'
    title: Heterogeneous Graph Transformer
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: https://github.com/acbull/pyHGT
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.622
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.071
    - null
  - model: HetGNN
    model_plain: HetGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.01332'
    title: Heterogeneous Graph Transformer
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: https://github.com/acbull/pyHGT
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.612
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.063
    - null
  - model: HAN
    model_plain: HAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.01332'
    title: Heterogeneous Graph Transformer
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: https://github.com/acbull/pyHGT
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.618
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.058
    - null
  - model: RawFeatures
    model_plain: RawFeatures
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.14863'
    title: Graph Communal Contrastive Learning
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.8901
    - 0.904
    - null
    - null
    metric_stds:
    - null
    - 0.0006
    - 0.0002
    - null
    - null
  - model: Node2Vec
    model_plain: Node2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.14863'
    title: Graph Communal Contrastive Learning
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.8293
    - 0.8511
    - null
    - null
    metric_stds:
    - null
    - 0.0011
    - 0.0006
    - null
    - null
  - model: DeepWalk
    model_plain: DeepWalk
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.14863'
    title: Graph Communal Contrastive Learning
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.8263
    - 0.8471
    - null
    - null
    metric_stds:
    - null
    - 0.0019
    - 0.0023
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.14863'
    title: Graph Communal Contrastive Learning
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9102
    - 0.9304
    - null
    - null
    metric_stds:
    - null
    - 0.0038
    - 0.0028
    - null
    - null
  - model: MVGRL
    model_plain: MVGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.14863'
    title: Graph Communal Contrastive Learning
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.905
    - 0.9211
    - null
    - null
    metric_stds:
    - null
    - 0.0012
    - 0.001
    - null
    - null
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.14863'
    title: Graph Communal Contrastive Learning
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9078
    - 0.9208
    - null
    - null
    metric_stds:
    - null
    - 0.0068
    - 0.0068
    - null
    - null
  - model: HDI
    model_plain: HDI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.14863'
    title: Graph Communal Contrastive Learning
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.8673
    - 0.8998
    - null
    - null
    metric_stds:
    - null
    - 0.0017
    - 0.0014
    - null
    - null
  - model: GAE
    model_plain: GAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.14863'
    title: Graph Communal Contrastive Learning
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.8831
    - 0.9
    - null
    - null
    metric_stds:
    - null
    - 0.0068
    - 0.0075
    - null
    - null
  - model: VGAE
    model_plain: VGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.14863'
    title: Graph Communal Contrastive Learning
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9011
    - 0.9208
    - null
    - null
    metric_stds:
    - null
    - 0.0006
    - 0.0008
    - null
    - null
  - model: GCA
    model_plain: GCA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.14863'
    title: Graph Communal Contrastive Learning
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9076
    - 0.9287
    - null
    - null
    metric_stds:
    - null
    - 0.0001
    - 0.0003
    - null
    - null
  - model: gCooL_c
    model_plain: gCooL_c
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.14863'
    title: Graph Communal Contrastive Learning
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9165
    - 0.9332
    - null
    - null
    metric_stds:
    - null
    - 0.0003
    - 0.0002
    - null
    - null
  - model: gCooL_e
    model_plain: gCooL_e
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.14863'
    title: Graph Communal Contrastive Learning
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9163
    - 0.9331
    - null
    - null
    metric_stds:
    - null
    - 0.0003
    - 0.0001
    - null
    - null
  - model: HolE
    model_plain: HolE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17003'
    title: Graph Condensation for Open-World Graph Learning
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.9363
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.0014
  - model: GCOND
    model_plain: GCOND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17003'
    title: Graph Condensation for Open-World Graph Learning
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.8821
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.0151
  - model: GCDM
    model_plain: GCDM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17003'
    title: Graph Condensation for Open-World Graph Learning
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.876
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.0015
  - model: SFGC
    model_plain: SFGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17003'
    title: Graph Condensation for Open-World Graph Learning
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.8981
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.0031
  - model: OpenGC
    model_plain: OpenGC
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17003'
    title: Graph Condensation for Open-World Graph Learning
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.9093
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.0049
  milestones:
  - value: 0.913
    std: 0.028
    model: GS-mean
    arxiv_id: '1811.05868'
    title: Pitfalls of Graph Neural Network Evaluation
    date: 2018-11
  - value: 0.9254
    std: 0.0034
    model: PushNet-TPP
    arxiv_id: '2003.02228'
    title: 'PushNet: Efficient and Adaptive Neural Message Passing'
    date: 2020-03
  - value: 0.9392
    std: 0.006
    model: Ada-Ugnn
    arxiv_id: '2010.01777'
    title: A Unified View on Graph Neural Networks as Graph Signal Denoising
    date: 2020-10
  - value: 0.949
    std: 0.003
    model: G-Zoom
    arxiv_id: '2111.10698'
    title: Towards Graph Self-Supervised Learning with Contrastive Adjusted Zooming
    date: 2021-11
  - value: 0.9577
    std: 0.0015
    model: Exphormer
    arxiv_id: '2303.06147'
    title: 'Exphormer: Sparse Transformers for Graphs'
    date: '2023-03-10'
  - value: 0.9589
    std: 0.0034
    model: SGT
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
  - value: 0.9626
    std: 0.0008
    model: DAM-GT
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: 2025-05
---

