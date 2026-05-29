---
title: COCO-SP
slug: coco-sp
benchmark: LRGB
task_type: node_classification
description: Node classification on superpixel graphs derived from MS-COCO.
primary_metric: F1
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.LRGBDataset.html
stats: null
result_count: 49
best_model:
  model: LPE
  value: 0.4483
  metric: F1
  arxiv_id: '2511.08028'
  paper_title: Generalizable Insights for Graph Transformers in Theory and Practice
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
  rows:
  - model: LPE
    model_plain: LPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.4483
    metric_stds:
    - 0.0071
  - model: SPE
    model_plain: SPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.4387
    metric_stds:
    - 0.0054
  - model: RWSE
    model_plain: RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.4382
    metric_stds:
    - 0.0101
  - model: NoPE
    model_plain: NoPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4312
    metric_stds:
    - 0.0085
  - model: RRWP
    model_plain: RRWP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3991
    metric_stds:
    - 0.0107
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
    - 0.3943
    metric_stds:
    - 0.0038
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
    - 0.3909
    metric_stds:
    - 0.0128
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
    - 0.3895
    metric_stds:
    - 0.0125
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
    - 0.3596
    metric_stds:
    - 0.0022
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
    - 0.3455
    metric_stds:
    - 0.0009
  - model: GTs
    model_plain: GTs
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
    - 0.3412
    metric_stds:
    - 0.0044
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
    - 0.3412
    metric_stds:
    - 0.0044
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
    - 0.332
    metric_stds:
    - 0.0032
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
    - 0.3297
    metric_stds:
    - 0.0053
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
    - 0.3027
    metric_stds:
    - 0.006
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
    - 0.3014
    metric_stds:
    - 0.0049
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
    - 0.2641
    metric_stds:
    - 0.0045
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
    - 0.2618
    metric_stds:
    - 0.0031
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
    - 0.2602
    metric_stds:
    - 0.0048
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
    - 0.2592
    metric_stds:
    - 0.0158
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
    - 0.2574
    metric_stds:
    - 0.0034
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
    - 0.2574
    metric_stds:
    - 0.0034
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
    - 0.2434
    metric_stds:
    - 0.0156
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
    - 0.2433
    metric_stds:
    - 0.0023
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
    - 0.2306
    metric_stds:
    - 0.0018
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
    - 0.1644
    metric_stds:
    - 0.0079
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
    - 0.1404
    metric_stds:
    - 0.0011
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
    - 0.1339
    metric_stds:
    - 0.0044
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
    - 0.1339
    metric_stds:
    - 0.0044
  - model: GIN
    model_plain: GIN
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
    - 0.1339
    metric_stds:
    - 0.0044
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
    - 0.133
    metric_stds:
    - 0.021
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
    - 0.132
    metric_stds:
    - 0.018
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
    - 0.132
    metric_stds:
    - 0.021
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
    - 0.131
    metric_stds:
    - 0.019
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
    - 0.129
    metric_stds:
    - 0.018
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
    - 0.1112
    metric_stds:
    - 0.0046
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
    - 0.102
    metric_stds:
    - 0.015
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
    - 0.093
    metric_stds:
    - 0.014
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
    - 0.093
    metric_stds:
    - 0.016
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
    - 0.091
    metric_stds:
    - 0.009
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
    - 0.088
    metric_stds:
    - 0.015
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
    - 0.085
    metric_stds:
    - 0.01
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
    - 0.0841
    metric_stds:
    - 0.001
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
    - 0.083
    metric_stds:
    - 0.012
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
    - 0.081
    metric_stds:
    - 0.015
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
    - 0.078
    metric_stds:
    - 0.004
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
    - 0.056
    metric_stds:
    - 0.011
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
    - 0.044
    metric_stds:
    - 0.015
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
    - 0.031
    metric_stds:
    - 0.016
  milestones:
  - value: 0.3412
    std: 0.0044
    model: GTs
    arxiv_id: '2205.12454'
    title: Recipe for a General, Powerful, Scalable Graph Transformer
    date: 2022-05
  - value: 0.3455
    std: 0.0009
    model: Exphormer
    arxiv_id: '2303.06147'
    title: 'Exphormer: Sparse Transformers for Graphs'
    date: '2023-03-10'
  - value: 0.3596
    std: 0.0022
    model: SGT
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
  - value: 0.3943
    std: 0.0038
    model: GTs
    arxiv_id: '2509.14863'
    title: 'Exploring the Global-to-Local Attention Scheme in Graph Transformers:
      An Empirical Study'
    date: 2025-09
  - value: 0.4483
    std: 0.0071
    model: LPE
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: 2025-11
---

