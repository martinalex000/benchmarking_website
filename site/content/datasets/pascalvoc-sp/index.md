---
title: PascalVOC-SP
slug: pascalvoc-sp
benchmark: LRGB
task_type: node_classification
description: Node classification on superpixel graphs derived from PascalVOC 2011.
primary_metric: F1
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.LRGBDataset.html
stats: null
result_count: 74
best_model:
  model: PGMs
  value: 0.806
  metric: F1
  arxiv_id: '2308.00887'
  paper_title: Factor Graph Neural Networks
variants:
- slug: standard-split
  name: Standard split
  notes: 'Official split. Metric: macro F1.'
  is_standard: true
  primary_metric: F1
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - F1
  - Accuracy
  - MAP
  rows:
  - model: PGMs
    model_plain: PGMs
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.00887'
    title: Factor Graph Neural Networks
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/andre-martins/AD3
    uses_external_data: true
    is_best: true
    metric_values:
    - 0.806
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GSSC
    model_plain: GSSC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.00282'
    title: 'GraphMinNet: Learning Dependencies in Graphs with Light Complexity Minimal
      Architecture'
    date: Feb 1, 2025
    date_iso: '2025-02-01'
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4561
    - null
    - null
    metric_stds:
    - 0.0039
    - null
    - null
  - model: GTs
    model_plain: GTs
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.14863'
    title: 'Exploring the Global-to-Local Attention Scheme in Graph Transformers:
      An Empirical Study'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4375
    - null
    - null
    metric_stds:
    - 0.0029
    - null
    - null
  - model: LRDs
    model_plain: LRDs
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.00282'
    title: 'GraphMinNet: Learning Dependencies in Graphs with Light Complexity Minimal
      Architecture'
    date: Feb 1, 2025
    date_iso: '2025-02-01'
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4352
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
  - model: GECO
    model_plain: GECO
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.14863'
    title: 'Exploring the Global-to-Local Attention Scheme in Graph Transformers:
      An Empirical Study'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.421
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
  - model: GMN
    model_plain: GMN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.14863'
    title: 'Exploring the Global-to-Local Attention Scheme in Graph Transformers:
      An Empirical Study'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4192
    - null
    - null
    metric_stds:
    - 0.0108
    - null
    - null
  - model: Graph-Mamba
    model_plain: Graph-Mamba
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.00282'
    title: 'GraphMinNet: Learning Dependencies in Graphs with Light Complexity Minimal
      Architecture'
    date: Feb 1, 2025
    date_iso: '2025-02-01'
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4191
    - null
    - null
    metric_stds:
    - 0.0126
    - null
    - null
  - model: GPS + Mamba
    model_plain: GPS + Mamba
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.14863'
    title: 'Exploring the Global-to-Local Attention Scheme in Graph Transformers:
      An Empirical Study'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.418
    - null
    - null
    metric_stds:
    - 0.012
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
    is_best: false
    metric_values:
    - 0.4163
    - null
    - null
    metric_stds:
    - 0.0019
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
    - 0.3975
    - null
    - null
    metric_stds:
    - 0.0037
    - null
    - null
  - model: GPS
    model_plain: GPS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12454'
    title: Recipe for a General, Powerful, Scalable Graph Transformer
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/rampasek/GraphGPS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3748
    - null
    - null
    metric_stds:
    - 0.0109
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
    - 0.3748
    - null
    - null
    metric_stds:
    - 0.0109
    - null
    - null
  - model: GPS+Transformer
    model_plain: GPS+Transformer
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
    - 0.3736
    - null
    - null
    metric_stds:
    - 0.0158
    - null
    - null
  - model: GPS+Performer
    model_plain: GPS+Performer
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
    - 0.3724
    - null
    - null
    metric_stds:
    - 0.0131
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
    - 0.3598
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
  - model: Exphormer
    model_plain: Exphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.14863'
    title: 'Exploring the Global-to-Local Attention Scheme in Graph Transformers:
      An Empirical Study'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3446
    - null
    - null
    metric_stds:
    - 0.0064
    - null
    - null
  - model: SAN+LapPE
    model_plain: SAN+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12454'
    title: Recipe for a General, Powerful, Scalable Graph Transformer
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/rampasek/GraphGPS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.323
    - null
    - null
    metric_stds:
    - 0.0039
    - null
    - null
  - model: SAN+RWSE
    model_plain: SAN+RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12454'
    title: Recipe for a General, Powerful, Scalable Graph Transformer
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/rampasek/GraphGPS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3216
    - null
    - null
    metric_stds:
    - 0.0027
    - null
    - null
  - model: SAN
    model_plain: SAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.00282'
    title: 'GraphMinNet: Learning Dependencies in Graphs with Light Complexity Minimal
      Architecture'
    date: Feb 1, 2025
    date_iso: '2025-02-01'
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3216
    - null
    - null
    metric_stds:
    - 0.0027
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
    - 0.3197
    - null
    - null
    metric_stds:
    - 0.0055
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
    - 0.3122
    - null
    - null
    metric_stds:
    - 0.0056
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
    - 0.3108
    - null
    - null
    metric_stds:
    - 0.0033
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
    - 0.3045
    - null
    - null
    metric_stds:
    - 0.0036
    - null
    - null
  - model: GPS (MPNN-only)
    model_plain: GPS (MPNN-only)
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
    - 0.3016
    - null
    - null
    metric_stds:
    - 0.0031
    - null
    - null
  - model: GatedGCN
    model_plain: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12454'
    title: Recipe for a General, Powerful, Scalable Graph Transformer
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/rampasek/GraphGPS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2873
    - null
    - null
    metric_stds:
    - 0.0219
    - null
    - null
  - model: GatedGCN+LapPE
    model_plain: GatedGCN+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.286
    - null
    - null
    metric_stds:
    - 0.0085
    - null
    - null
  - model: GatedGCN+RWSE
    model_plain: GatedGCN+RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12454'
    title: Recipe for a General, Powerful, Scalable Graph Transformer
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/rampasek/GraphGPS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.286
    - null
    - null
    metric_stds:
    - 0.0085
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
    - 0.286
    - null
    - null
    metric_stds:
    - 0.0015
    - null
    - null
  - model: GPS+BigBird
    model_plain: GPS+BigBird
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
    - 0.2762
    - null
    - null
    metric_stds:
    - 0.0069
    - null
    - null
  - model: Transformer+LapPE
    model_plain: Transformer+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12454'
    title: Recipe for a General, Powerful, Scalable Graph Transformer
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/rampasek/GraphGPS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2694
    - null
    - null
    metric_stds:
    - 0.0098
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
    - 0.256
    - null
    - null
    metric_stds:
    - 0.0056
    - null
    - null
  - model: DMD-GCN
    model_plain: DMD-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.243
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
  - model: DMD++
    model_plain: DMD++
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.241
    - null
    - null
    metric_stds:
    - 0.017
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.238
    - null
    - null
    metric_stds:
    - 0.016
    - null
    - null
  - model: DMD-SGC
    model_plain: DMD-SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.217
    - null
    - null
    metric_stds:
    - 0.036
    - null
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.216
    - null
    - null
    metric_stds:
    - 0.039
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
    - 0.188
    - null
    - null
    metric_stds:
    - 0.0085
    - null
    - null
  - model: GCNII
    model_plain: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1698
    - null
    - null
    metric_stds:
    - 0.008
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
    - 0.1658
    - null
    - null
    metric_stds:
    - 0.0049
    - null
    - null
  - model: GCN + BORF
    model_plain: GCN + BORF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/Weber-GeoML/AFRC_Rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.163
    - null
    - null
    metric_stds:
    - 0.021
    - null
    - null
  - model: GIN + AFR-3
    model_plain: GIN + AFR-3
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/Weber-GeoML/AFRC_Rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.162
    - null
    - null
    metric_stds:
    - 0.02
    - null
    - null
  - model: GCN + AFR-3 (heuristic add)
    model_plain: GCN + AFR-3 (heuristic add)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/Weber-GeoML/AFRC_Rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.161
    - null
    - null
    metric_stds:
    - 0.015
    - null
    - null
  - model: GCN + AFR-4
    model_plain: GCN + AFR-4
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/Weber-GeoML/AFRC_Rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.159
    - null
    - null
    metric_stds:
    - 0.019
    - null
    - null
  - model: GCN + BORF (heuristic add)
    model_plain: GCN + BORF (heuristic add)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/Weber-GeoML/AFRC_Rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.159
    - null
    - null
    metric_stds:
    - 0.015
    - null
    - null
  - model: GPRGNN
    model_plain: GPRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.152
    - null
    - null
    metric_stds:
    - 0.024
    - null
    - null
  - model: R-GIN + FoSR
    model_plain: R-GIN + FoSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/Weber-GeoML/AFRC_Rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.144
    - null
    - null
    metric_stds:
    - 0.017
    - null
    - null
  - model: GCN + FoSR
    model_plain: GCN + FoSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/Weber-GeoML/AFRC_Rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.138
    - null
    - null
    metric_stds:
    - 0.013
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12454'
    title: Recipe for a General, Powerful, Scalable Graph Transformer
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/rampasek/GraphGPS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1268
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
  - model: GINE
    model_plain: GINE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12454'
    title: Recipe for a General, Powerful, Scalable Graph Transformer
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/rampasek/GraphGPS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1265
    - null
    - null
    metric_stds:
    - 0.0076
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.00282'
    title: 'GraphMinNet: Learning Dependencies in Graphs with Light Complexity Minimal
      Architecture'
    date: Feb 1, 2025
    date_iso: '2025-02-01'
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1265
    - null
    - null
    metric_stds:
    - 0.0076
    - null
    - null
  - model: R-GIN + None
    model_plain: R-GIN + None
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/Weber-GeoML/AFRC_Rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.123
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
  - model: R-GIN + SDRF
    model_plain: R-GIN + SDRF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/Weber-GeoML/AFRC_Rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.122
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
  - model: GCN + SDRF
    model_plain: GCN + SDRF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/Weber-GeoML/AFRC_Rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.117
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.114
    - null
    - null
    metric_stds:
    - 0.023
    - null
    - null
  - model: GCN + None
    model_plain: GCN + None
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/Weber-GeoML/AFRC_Rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.104
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
  - model: DGNs
    model_plain: DGNs
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_iso: '2024-06-04'
    date_display: Jun 2024
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0998
    - null
    - null
    metric_stds:
    - 0.0033
    - null
    - null
  - model: DyGFormer
    model_plain: DyGFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_iso: '2024-06-04'
    date_display: Jun 2024
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0807
    - null
    - null
    metric_stds:
    - 0.0027
    - null
    - null
  - model: TGAT
    model_plain: TGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_iso: '2024-06-04'
    date_display: Jun 2024
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0604
    - null
    - null
    metric_stds:
    - 0.0026
    - null
    - null
  - model: GraphMixer
    model_plain: GraphMixer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_iso: '2024-06-04'
    date_display: Jun 2024
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0588
    - null
    - null
    metric_stds:
    - 0.0008
    - null
    - null
  - model: JODIE
    model_plain: JODIE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_iso: '2024-06-04'
    date_display: Jun 2024
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0576
    - null
    - null
    metric_stds:
    - 0.0035
    - null
    - null
  - model: TGN
    model_plain: TGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_iso: '2024-06-04'
    date_display: Jun 2024
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0559
    - null
    - null
    metric_stds:
    - 0.0024
    - null
    - null
  - model: DyRep
    model_plain: DyRep
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_iso: '2024-06-04'
    date_display: Jun 2024
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0523
    - null
    - null
    metric_stds:
    - 0.0011
    - null
    - null
  - model: ERM
    model_plain: ERM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.04102'
    title: Enhancing Distribution and Label Consistency for Graph Out-of-Distribution
      Generalization
    date: Jan 2025
    date_iso: 2025-01
    date_display: Jan 2025
    codebase_url: https://github.com/SongW-SW/DLG
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.3881
    - null
    metric_stds:
    - null
    - 0.0161
    - null
  - model: IRM
    model_plain: IRM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.04102'
    title: Enhancing Distribution and Label Consistency for Graph Out-of-Distribution
      Generalization
    date: Jan 2025
    date_iso: 2025-01
    date_display: Jan 2025
    codebase_url: https://github.com/SongW-SW/DLG
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.3971
    - null
    metric_stds:
    - null
    - 0.0211
    - null
  - model: V-REx
    model_plain: V-REx
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.04102'
    title: Enhancing Distribution and Label Consistency for Graph Out-of-Distribution
      Generalization
    date: Jan 2025
    date_iso: 2025-01
    date_display: Jan 2025
    codebase_url: https://github.com/SongW-SW/DLG
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.3904
    - null
    metric_stds:
    - null
    - 0.0197
    - null
  - model: DIR
    model_plain: DIR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.04102'
    title: Enhancing Distribution and Label Consistency for Graph Out-of-Distribution
      Generalization
    date: Jan 2025
    date_iso: 2025-01
    date_display: Jan 2025
    codebase_url: https://github.com/SongW-SW/DLG
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.4394
    - null
    metric_stds:
    - null
    - 0.017
    - null
  - model: GIL
    model_plain: GIL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.04102'
    title: Enhancing Distribution and Label Consistency for Graph Out-of-Distribution
      Generalization
    date: Jan 2025
    date_iso: 2025-01
    date_display: Jan 2025
    codebase_url: https://github.com/SongW-SW/DLG
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.5229
    - null
    metric_stds:
    - null
    - 0.0296
    - null
  - model: CIGA
    model_plain: CIGA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.04102'
    title: Enhancing Distribution and Label Consistency for Graph Out-of-Distribution
      Generalization
    date: Jan 2025
    date_iso: 2025-01
    date_display: Jan 2025
    codebase_url: https://github.com/SongW-SW/DLG
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.6986
    - null
    metric_stds:
    - null
    - 0.0341
    - null
  - model: DLG
    model_plain: DLG
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.04102'
    title: Enhancing Distribution and Label Consistency for Graph Out-of-Distribution
      Generalization
    date: Jan 2025
    date_iso: 2025-01
    date_display: Jan 2025
    codebase_url: https://github.com/SongW-SW/DLG
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7334
    - null
    metric_stds:
    - null
    - 0.0284
    - null
  - model: GF_align
    model_plain: GF_align
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1805.11273'
    title: 'DynGEM: Deep Embedding Method for Dynamic Graphs'
    date: May 2018
    date_iso: 2018-05
    date_display: May 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.164
    metric_stds:
    - null
    - null
    - null
  - model: GF_init
    model_plain: GF_init
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1805.11273'
    title: 'DynGEM: Deep Embedding Method for Dynamic Graphs'
    date: May 2018
    date_iso: 2018-05
    date_display: May 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.164
    metric_stds:
    - null
    - null
    - null
  - model: SDNE_align
    model_plain: SDNE_align
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1805.11273'
    title: 'DynGEM: Deep Embedding Method for Dynamic Graphs'
    date: May 2018
    date_iso: 2018-05
    date_display: May 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.07
    metric_stds:
    - null
    - null
    - null
  - model: SDNE
    model_plain: SDNE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1805.11273'
    title: 'DynGEM: Deep Embedding Method for Dynamic Graphs'
    date: May 2018
    date_iso: 2018-05
    date_display: May 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.214
    metric_stds:
    - null
    - null
    - null
  - model: DynGEM
    model_plain: DynGEM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1805.11273'
    title: 'DynGEM: Deep Embedding Method for Dynamic Graphs'
    date: May 2018
    date_iso: 2018-05
    date_display: May 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.216
    metric_stds:
    - null
    - null
    - null
  milestones:
  - value: 0.3748
    std: 0.0109
    model: GPS
    arxiv_id: '2205.12454'
    title: Recipe for a General, Powerful, Scalable Graph Transformer
    date: 2022-05
  - value: 0.3975
    std: 0.0037
    model: Exphormer
    arxiv_id: '2303.06147'
    title: 'Exphormer: Sparse Transformers for Graphs'
    date: '2023-03-10'
  - value: 0.806
    std: null
    model: PGMs
    arxiv_id: '2308.00887'
    title: Factor Graph Neural Networks
    date: 2023-08
---

