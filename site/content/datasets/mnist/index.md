---
title: MNIST
slug: mnist
benchmark: GNNBenchmark
task_type: graph_classification
description: Graph classification on MNIST superpixel graphs (10 digit classes, 70k
  graphs).
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.GNNBenchmarkDataset.html
stats: null
result_count: 127
best_model:
  model: Classical CNN
  value: 0.9933
  metric: Accuracy
  arxiv_id: '1606.09375'
  paper_title: Convolutional Neural Networks on Graphs with Fast Localized Spectral
    Filtering
variants:
- slug: standard-split
  name: Standard split
  notes: Fixed 55k/5k/10k split.
  is_standard: true
  primary_metric: Accuracy
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - Accuracy
  - Chamfer loss
  - Cross-Entropy
  rows:
  - model: Classical CNN
    model_plain: Classical CNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1606.09375'
    title: Convolutional Neural Networks on Graphs with Fast Localized Spectral Filtering
    date: Jun 2016
    date_iso: 2016-06
    date_display: Jun 2016
    codebase_url: https://github.com/mdeff/cnn_graph
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9933
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: LeNet5
    model_plain: LeNet5
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1705.07664'
    title: 'CayleyNets: Graph Convolutional Neural Networks with Complex Rational
      Spectral Filters'
    date: May 2017
    date_iso: 2017-05
    date_display: May 2017
    codebase_url: https://github.com/fmonti/mgcnn
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9933
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: CayleyNets
    model_plain: CayleyNets
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1705.07664'
    title: 'CayleyNets: Graph Convolutional Neural Networks with Complex Rational
      Spectral Filters'
    date: May 2017
    date_iso: 2017-05
    date_display: May 2017
    codebase_url: https://github.com/fmonti/mgcnn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9918
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: Proposed graph CNN
    model_plain: Proposed graph CNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1606.09375'
    title: Convolutional Neural Networks on Graphs with Fast Localized Spectral Filtering
    date: Jun 2016
    date_iso: 2016-06
    date_display: Jun 2016
    codebase_url: https://github.com/mdeff/cnn_graph
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9914
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: ChebNet
    model_plain: ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1705.07664'
    title: 'CayleyNets: Graph Convolutional Neural Networks with Complex Rational
      Spectral Filters'
    date: May 2017
    date_iso: 2017-05
    date_display: May 2017
    codebase_url: https://github.com/fmonti/mgcnn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9914
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: 400-LRF3200-MP800-LRF800-MP400-10
    model_plain: 400-LRF3200-MP800-LRF800-MP400-10
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1312.6203'
    title: Spectral Networks and Locally Connected Networks on Graphs
    date: Dec 21, 2013
    date_iso: '2013-12-21'
    date_display: Dec 2013
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.987
    - null
    - null
    metric_stds:
    - null
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
    - 0.98598
    - null
    - null
    metric_stds:
    - 0.00138
    - null
    - null
  - model: LeNet5
    model_plain: LeNet5
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1611.08402'
    title: Geometric deep learning on graphs and manifolds using mixture model CNNs
    date: Nov 2016
    date_iso: 2016-11
    date_display: Nov 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9859
    - null
    - null
    metric_stds:
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
    - 0.9855
    - null
    - null
    metric_stds:
    - 0.00039
    - null
    - null
  - model: CNNs
    model_plain: CNNs
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1806.09231'
    title: 'Clebsch--Gordan Nets: a Fully Fourier Space Spherical Convolutional Neural
      Network'
    date: Jun 2018
    date_iso: 2018-06
    date_display: Jun 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.985
    - null
    - null
    metric_stds:
    - 0.002
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
    - 0.98492
    - null
    - null
    metric_stds:
    - 0.00051
    - null
    - null
  - model: Exphormer
    model_plain: Exphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.00789'
    title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective
      State Spaces'
    date: Feb 1, 2024
    date_iso: '2024-02-01'
    date_display: Feb 2024
    codebase_url: https://github.com/bowang-lab/Graph-Mamba
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9843
    - null
    - null
    metric_stds:
    - 0.0004
    - null
    - null
  - model: Graph-Mamba
    model_plain: Graph-Mamba
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.285
    arxiv_id: '2402.00789'
    title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective
      State Spaces'
    date: Feb 1, 2024
    date_iso: '2024-02-01'
    date_display: Feb 2024
    codebase_url: https://github.com/bowang-lab/Graph-Mamba
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9842
    - null
    - null
    metric_stds:
    - 0.0008
    - null
    - null
  - model: GRED
    model_plain: GRED
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
    - 0.98383
    - null
    - null
    metric_stds:
    - 0.00012
    - null
    - null
  - model: Eigenformer (feat.)
    model_plain: Eigenformer (feat.)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.17791'
    title: Graph Transformers without Positional Encodings
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.98362
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GPS+Performer
    model_plain: GPS+Performer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.00789'
    title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective
      State Spaces'
    date: Feb 1, 2024
    date_iso: '2024-02-01'
    date_display: Feb 2024
    codebase_url: https://github.com/bowang-lab/Graph-Mamba
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9834
    - null
    - null
    metric_stds:
    - 0.0003
    - null
    - null
  - model: GRIT-SPSE
    model_plain: GRIT-SPSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: Feb 13, 2025
    date_iso: '2025-02-13'
    date_display: Feb 2025
    codebase_url: https://github.com/LouisBearing/Graph-SPSE-Encoding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.98294
    - null
    - null
    metric_stds:
    - 0.00147
    - null
    - null
  - model: CSA-SPSE
    model_plain: CSA-SPSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: Feb 13, 2025
    date_iso: '2025-02-13'
    date_display: Feb 2025
    codebase_url: https://github.com/LouisBearing/Graph-SPSE-Encoding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.98269
    - null
    - null
    metric_stds:
    - 0.00078
    - null
    - null
  - model: Graph-ViT + GFSA
    model_plain: Graph-ViT + GFSA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.04234'
    title: Graph Convolutions Enrich the Self-Attention in Transformers!
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/jeongwhanchoi/GFSA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9826
    - null
    - null
    metric_stds:
    - 0.0004
    - null
    - null
  - model: GPS-GCCM
    model_plain: GPS-GCCM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05689'
    title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency
      Model'
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.98236
    - null
    - null
    metric_stds:
    - 0.0006
    - null
    - null
  - model: GRIT-RWSE
    model_plain: GRIT-RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: Feb 13, 2025
    date_iso: '2025-02-13'
    date_display: Feb 2025
    codebase_url: https://github.com/LouisBearing/Graph-SPSE-Encoding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.98231
    - null
    - null
    metric_stds:
    - 0.00197
    - null
    - null
  - model: Graph-ViT
    model_plain: Graph-ViT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.04234'
    title: Graph Convolutions Enrich the Self-Attention in Transformers!
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/jeongwhanchoi/GFSA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.982
    - null
    - null
    metric_stds:
    - 0.0005
    - null
    - null
  - model: 400-FC800-FC50-10
    model_plain: 400-FC800-FC50-10
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1312.6203'
    title: Spectral Networks and Locally Connected Networks on Graphs
    date: Dec 21, 2013
    date_iso: '2013-12-21'
    date_display: Dec 2013
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.982
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: 400-LRF1600-MP800-10
    model_plain: 400-LRF1600-MP800-10
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1312.6203'
    title: Spectral Networks and Locally Connected Networks on Graphs
    date: Dec 21, 2013
    date_iso: '2013-12-21'
    date_display: Dec 2013
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.982
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: 400-SP4800-10 (d1 = 300, q = 20)
    model_plain: 400-SP4800-10 (d1 = 300, q = 20)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1312.6203'
    title: Spectral Networks and Locally Connected Networks on Graphs
    date: Dec 21, 2013
    date_iso: '2013-12-21'
    date_display: Dec 2013
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.982
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: Tango_GPS
    model_plain: Tango_GPS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.05070'
    title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential Flows'
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.98197
    - null
    - null
    metric_stds:
    - 0.0011
    - null
    - null
  - model: EGT
    model_plain: EGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.03348'
    title: Global Self-Attention as a Replacement for Graph Convolution
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/shamim-hussain/egt
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.98173
    - null
    - null
    metric_stds:
    - 0.00087
    - null
    - null
  - model: GPS+BigBird
    model_plain: GPS+BigBird
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.00789'
    title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective
      State Spaces'
    date: Feb 1, 2024
    date_iso: '2024-02-01'
    date_display: Feb 2024
    codebase_url: https://github.com/bowang-lab/Graph-Mamba
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9817
    - null
    - null
    metric_stds:
    - 0.0001
    - null
    - null
  - model: MoNet
    model_plain: MoNet
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1611.08402'
    title: Geometric deep learning on graphs and manifolds using mixture model CNNs
    date: Nov 2016
    date_iso: 2016-11
    date_display: Nov 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9816
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GPS + GFSA
    model_plain: GPS + GFSA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.04234'
    title: Graph Convolutions Enrich the Self-Attention in Transformers!
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/jeongwhanchoi/GFSA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9814
    - null
    - null
    metric_stds:
    - 0.0014
    - null
    - null
  - model: CSA-RWSE
    model_plain: CSA-RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: Feb 13, 2025
    date_iso: '2025-02-13'
    date_display: Feb 2025
    codebase_url: https://github.com/LouisBearing/Graph-SPSE-Encoding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.98127
    - null
    - null
    metric_stds:
    - 0.00123
    - null
    - null
  - model: GPS-PCL
    model_plain: GPS-PCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05689'
    title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency
      Model'
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.98114
    - null
    - null
    metric_stds:
    - 0.00183
    - null
    - null
  - model: GPS+Transformer
    model_plain: GPS+Transformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.287
    arxiv_id: '2402.00789'
    title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective
      State Spaces'
    date: Feb 1, 2024
    date_iso: '2024-02-01'
    date_display: Feb 2024
    codebase_url: https://github.com/bowang-lab/Graph-Mamba
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9811
    - null
    - null
    metric_stds:
    - 0.0011
    - null
    - null
  - model: GRIT
    model_plain: GRIT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.17791'
    title: Graph Transformers without Positional Encodings
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.98108
    - null
    - null
    metric_stds:
    - 0.00111
    - null
    - null
  - model: GPS + GPSE
    model_plain: GPS + GPSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: Feb 13, 2025
    date_iso: '2025-02-13'
    date_display: Feb 2025
    codebase_url: https://github.com/LouisBearing/Graph-SPSE-Encoding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.98105
    - null
    - null
    metric_stds:
    - 0.00158
    - null
    - null
  - model: PNA
    model_plain: PNA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1806.09231'
    title: 'Clebsch--Gordan Nets: a Fully Fourier Space Spherical Convolutional Neural
      Network'
    date: Jun 2018
    date_iso: 2018-06
    date_display: Jun 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.981
    - null
    - null
    metric_stds:
    - 0.002
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
    - 0.98051
    - null
    - null
    metric_stds:
    - 0.00126
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
    - 0.9805
    - null
    - null
    metric_stds:
    - 0.00126
    - null
    - null
  - model: CRaWl
    model_plain: CRaWl
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
    - 0.97944
    - null
    - null
    metric_stds:
    - 0.0005
    - null
    - null
  - model: CRaW1
    model_plain: CRaW1
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.17791'
    title: Graph Transformers without Positional Encodings
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.97944
    - null
    - null
    metric_stds:
    - 0.0005
    - null
    - null
  - model: Graphormer
    model_plain: Graphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.03348'
    title: Global Self-Attention as a Replacement for Graph Convolution
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/shamim-hussain/egt
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.97905
    - null
    - null
    metric_stds:
    - 0.00176
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1806.09231'
    title: 'Clebsch--Gordan Nets: a Fully Fourier Space Spherical Convolutional Neural
      Network'
    date: Jun 2018
    date_iso: 2018-06
    date_display: Jun 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.979
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1806.09231'
    title: 'Clebsch--Gordan Nets: a Fully Fourier Space Spherical Convolutional Neural
      Network'
    date: Jun 2018
    date_iso: 2018-06
    date_display: Jun 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.978
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
  - model: Tango_GatedGCN
    model_plain: Tango_GatedGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.05070'
    title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential Flows'
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.97788
    - null
    - null
    metric_stds:
    - 0.00105
    - null
    - null
  - model: SoGCN-GRU
    model_plain: SoGCN-GRU
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.07141'
    title: 'SoGCN: Second-Order Graph Convolutional Networks'
    date: Oct 14, 2021
    date_iso: '2021-10-14'
    date_display: Oct 2021
    codebase_url: https://github.com/yuehaowang/SoGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.97729
    - null
    - null
    metric_stds:
    - 0.00159
    - null
    - null
  - model: ChebNet
    model_plain: ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1611.08402'
    title: Geometric deep learning on graphs and manifolds using mixture model CNNs
    date: Nov 2016
    date_iso: 2016-11
    date_display: Nov 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.977
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: PNA
    model_plain: PNA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.03348'
    title: Global Self-Attention as a Replacement for Graph Convolution
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/shamim-hussain/egt
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9769
    - null
    - null
    metric_stds:
    - 0.00022
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1806.09231'
    title: 'Clebsch--Gordan Nets: a Fully Fourier Space Spherical Convolutional Neural
      Network'
    date: Jun 2018
    date_iso: 2018-06
    date_display: Jun 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.975
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
  - model: Graph-ViT
    model_plain: Graph-ViT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: Feb 13, 2025
    date_iso: '2025-02-13'
    date_display: Feb 2025
    codebase_url: https://github.com/LouisBearing/Graph-SPSE-Encoding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.97422
    - null
    - null
    metric_stds:
    - 0.0011
    - null
    - null
  - model: 400-SP1600-10 (d1 = 300, q = 32)
    model_plain: 400-SP1600-10 (d1 = 300, q = 32)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1312.6203'
    title: Spectral Networks and Locally Connected Networks on Graphs
    date: Dec 21, 2013
    date_iso: '2013-12-21'
    date_display: Dec 2013
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9740000000000001
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: ChebyGIN
    model_plain: ChebyGIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.02850'
    title: Understanding Attention and Generalization in Graph Neural Networks
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/bknyaz/graph_attention_pool
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.974
    - null
    - null
    metric_stds:
    - 0.0
    - null
    - null
  - model: GatedGCN
    model_plain: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.03348'
    title: Global Self-Attention as a Replacement for Graph Convolution
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/shamim-hussain/egt
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9734
    - null
    - null
    metric_stds:
    - 0.00143
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1806.09231'
    title: 'Clebsch--Gordan Nets: a Fully Fourier Space Spherical Convolutional Neural
      Network'
    date: Jun 2018
    date_iso: 2018-06
    date_display: Jun 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.972
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
  - model: Eigenformer
    model_plain: Eigenformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.17791'
    title: Graph Transformers without Positional Encodings
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.97142
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: SoGCN
    model_plain: SoGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.07141'
    title: 'SoGCN: Second-Order Graph Convolutional Networks'
    date: Oct 14, 2021
    date_iso: '2021-10-14'
    date_display: Oct 2021
    codebase_url: https://github.com/yuehaowang/SoGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.96785
    - null
    - null
    metric_stds:
    - 0.00113
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.03348'
    title: Global Self-Attention as a Replacement for Graph Convolution
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/shamim-hussain/egt
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.96485
    - null
    - null
    metric_stds:
    - 0.00097
    - null
    - null
  - model: Vanilla GCN + GRU
    model_plain: Vanilla GCN + GRU
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.07141'
    title: 'SoGCN: Second-Order Graph Convolutional Networks'
    date: Oct 14, 2021
    date_iso: '2021-10-14'
    date_display: Oct 2021
    codebase_url: https://github.com/yuehaowang/SoGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9602
    - null
    - null
    metric_stds:
    - 0.0009
    - null
    - null
  - model: Nearest Neighbors
    model_plain: Nearest Neighbors
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1312.6203'
    title: Spectral Networks and Locally Connected Networks on Graphs
    date: Dec 21, 2013
    date_iso: '2013-12-21'
    date_display: Dec 2013
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9589
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.03348'
    title: Global Self-Attention as a Replacement for Graph Convolution
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/shamim-hussain/egt
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.95535
    - null
    - null
    metric_stds:
    - 0.00205
    - null
    - null
  - model: GPS-LGD
    model_plain: GPS-LGD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05689'
    title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency
      Model'
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.95461
    - null
    - null
    metric_stds:
    - 0.00613
    - null
    - null
  - model: ChebyGIN, top-k
    model_plain: ChebyGIN, top-k
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.02850'
    title: Understanding Attention and Generalization in Graph Neural Networks
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/bknyaz/graph_attention_pool
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.951
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
  - model: 3WLGNN
    model_plain: 3WLGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.07141'
    title: 'SoGCN: Second-Order Graph Convolutional Networks'
    date: Oct 14, 2021
    date_iso: '2021-10-14'
    date_display: Oct 2021
    codebase_url: https://github.com/yuehaowang/SoGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.95075
    - null
    - null
    metric_stds:
    - 0.00961
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.20815'
    title: GNN Explanations that do not Explain and How to find Them
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: https://github.com/steveazzolin/gnn_deg_expl
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9470000000000001
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
  - model: ChebyGIN, ours
    model_plain: ChebyGIN, ours
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.02850'
    title: Understanding Attention and Generalization in Graph Neural Networks
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/bknyaz/graph_attention_pool
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.946
    - null
    - null
    metric_stds:
    - 0.03
    - null
    - null
  - model: MoNet
    model_plain: MoNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.07141'
    title: 'SoGCN: Second-Order Graph Convolutional Networks'
    date: Oct 14, 2021
    date_iso: '2021-10-14'
    date_display: Oct 2021
    codebase_url: https://github.com/yuehaowang/SoGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.90805
    - null
    - null
    metric_stds:
    - 0.00032
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.03348'
    title: Global Self-Attention as a Replacement for Graph Convolution
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/shamim-hussain/egt
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.90705
    - null
    - null
    metric_stds:
    - 0.00218
    - null
    - null
  - model: GCN + Vanilla
    model_plain: GCN + Vanilla
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.07141'
    title: 'SoGCN: Second-Order Graph Convolutional Networks'
    date: Oct 14, 2021
    date_iso: '2021-10-14'
    date_display: Oct 2021
    codebase_url: https://github.com/yuehaowang/SoGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.90705
    - null
    - null
    metric_stds:
    - 0.00218
    - null
    - null
  - model: GIN, topk
    model_plain: GIN, topk
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.02850'
    title: Understanding Attention and Generalization in Graph Neural Networks
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/bknyaz/graph_attention_pool
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.905
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.02850'
    title: Understanding Attention and Generalization in Graph Neural Networks
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/bknyaz/graph_attention_pool
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.876
    - null
    - null
    metric_stds:
    - 0.03
    - null
    - null
  - model: MGNN
    model_plain: MGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.20815'
    title: GNN Explanations that do not Explain and How to find Them
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: https://github.com/steveazzolin/gnn_deg_expl
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.868
    - null
    - null
    metric_stds:
    - 0.08
    - null
    - null
  - model: GIN, top-k
    model_plain: GIN, top-k
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.02850'
    title: Understanding Attention and Generalization in Graph Neural Networks
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/bknyaz/graph_attention_pool
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.86
    - null
    - null
    metric_stds:
    - 0.06
    - null
    - null
  - model: GCN-3-TOGL-1
    model_plain: GCN-3-TOGL-1
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.07835'
    title: Topological Graph Neural Networks
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/BorgwardtLab/TOGL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.844
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
  - model: GIN-4
    model_plain: GIN-4
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.07835'
    title: Topological Graph Neural Networks
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/BorgwardtLab/TOGL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.834
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
  - model: GIN, ours
    model_plain: GIN, ours
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.02850'
    title: Understanding Attention and Generalization in Graph Neural Networks
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/bknyaz/graph_attention_pool
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.826
    - null
    - null
    metric_stds:
    - 0.08
    - null
    - null
  - model: MSE-GNN (GIN)
    model_plain: MSE-GNN (GIN)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.07340'
    title: Towards Few-shot Self-explaining Graph Neural Networks
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: https://github.com/jypeng28/MSE-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8222
    - null
    - null
    metric_stds:
    - 0.03
    - null
    - null
  - model: GREA_Meta (GIN)
    model_plain: GREA_Meta (GIN)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.07340'
    title: Towards Few-shot Self-explaining Graph Neural Networks
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: https://github.com/jypeng28/MSE-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7855
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
    arxiv_id: '1905.02850'
    title: Understanding Attention and Generalization in Graph Neural Networks
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/bknyaz/graph_attention_pool
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.783
    - null
    - null
    metric_stds:
    - 0.02
    - null
    - null
  - model: GAT-3-TOGL-1
    model_plain: GAT-3-TOGL-1
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.07835'
    title: Topological Graph Neural Networks
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/BorgwardtLab/TOGL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.772
    - null
    - null
    metric_stds:
    - 0.105
    - null
    - null
  - model: GCN-4
    model_plain: GCN-4
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.07835'
    title: Topological Graph Neural Networks
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/BorgwardtLab/TOGL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.762
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
  - model: MSE-GNN (GraphSAGE)
    model_plain: MSE-GNN (GraphSAGE)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.07340'
    title: Towards Few-shot Self-explaining Graph Neural Networks
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: https://github.com/jypeng28/MSE-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7077
    - null
    - null
    metric_stds:
    - 0.038
    - null
    - null
  - model: GALA
    model_plain: GALA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19035'
    title: Does Invariant Graph Learning via Environment Augmentation Learn Invariance?
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/LFhase/GALA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6894
    - null
    - null
    metric_stds:
    - 0.0056
    - null
    - null
  - model: Oracle
    model_plain: Oracle
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19035'
    title: Does Invariant Graph Learning via Environment Augmentation Learn Invariance?
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/LFhase/GALA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6776
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
  - model: CAL_Meta (GraphSAGE)
    model_plain: CAL_Meta (GraphSAGE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.07340'
    title: Towards Few-shot Self-explaining Graph Neural Networks
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: https://github.com/jypeng28/MSE-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6613
    - null
    - null
    metric_stds:
    - 0.229
    - null
    - null
  - model: GREA_Meta (GraphSAGE)
    model_plain: GREA_Meta (GraphSAGE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.07340'
    title: Towards Few-shot Self-explaining Graph Neural Networks
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: https://github.com/jypeng28/MSE-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6513
    - null
    - null
    metric_stds:
    - 0.04
    - null
    - null
  - model: GAT-4
    model_plain: GAT-4
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.07835'
    title: Topological Graph Neural Networks
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/BorgwardtLab/TOGL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.632
    - null
    - null
    metric_stds:
    - 0.104
    - null
    - null
  - model: GREA_Raw (GraphSAGE)
    model_plain: GREA_Raw (GraphSAGE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.07340'
    title: Towards Few-shot Self-explaining Graph Neural Networks
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: https://github.com/jypeng28/MSE-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5496
    - null
    - null
    metric_stds:
    - 0.064
    - null
    - null
  - model: DisC
    model_plain: DisC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19035'
    title: Does Invariant Graph Learning via Environment Augmentation Learn Invariance?
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/LFhase/GALA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5026
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
  - model: CAL_Raw (GraphSAGE)
    model_plain: CAL_Raw (GraphSAGE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.07340'
    title: Towards Few-shot Self-explaining Graph Neural Networks
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: https://github.com/jypeng28/MSE-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4906
    - null
    - null
    metric_stds:
    - 0.116
    - null
    - null
  - model: GREA_Raw (GIN)
    model_plain: GREA_Raw (GIN)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.07340'
    title: Towards Few-shot Self-explaining Graph Neural Networks
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: https://github.com/jypeng28/MSE-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4789
    - null
    - null
    metric_stds:
    - 0.044
    - null
    - null
  - model: CAL_Raw (GIN)
    model_plain: CAL_Raw (GIN)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.07340'
    title: Towards Few-shot Self-explaining Graph Neural Networks
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: https://github.com/jypeng28/MSE-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4395
    - null
    - null
    metric_stds:
    - 0.039
    - null
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
    - 0.3122
    - null
    - null
    metric_stds:
    - 0.0264
    - null
    - null
  - model: GSAT
    model_plain: GSAT
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
    - 0.2501
    - null
    - null
    metric_stds:
    - 0.0324
    - null
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
    - 0.2481
    - null
    - null
    metric_stds:
    - 0.0157
    - null
    - null
  - model: CAL+
    model_plain: CAL+
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19035'
    title: Does Invariant Graph Learning via Environment Augmentation Learn Invariance?
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/LFhase/GALA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2368
    - null
    - null
    metric_stds:
    - 0.0468
    - null
    - null
  - model: IB-IRM
    model_plain: IB-IRM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19035'
    title: Does Invariant Graph Learning via Environment Augmentation Learn Invariance?
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/LFhase/GALA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2358
    - null
    - null
    metric_stds:
    - 0.0796
    - null
    - null
  - model: EIIL
    model_plain: EIIL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19035'
    title: Does Invariant Graph Learning via Environment Augmentation Learn Invariance?
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/LFhase/GALA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2355
    - null
    - null
    metric_stds:
    - 0.0768
    - null
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
    - 0.2194
    - null
    - null
    metric_stds:
    - 0.0376
    - null
    - null
  - model: ERM
    model_plain: ERM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19035'
    title: Does Invariant Graph Learning via Environment Augmentation Learn Invariance?
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/LFhase/GALA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2156
    - null
    - null
    metric_stds:
    - 0.0538
    - null
    - null
  - model: MoleOOD
    model_plain: MoleOOD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19035'
    title: Does Invariant Graph Learning via Environment Augmentation Learn Invariance?
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/LFhase/GALA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2104
    - null
    - null
    metric_stds:
    - 0.0336
    - null
    - null
  - model: XGNN
    model_plain: XGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19035'
    title: Does Invariant Graph Learning via Environment Augmentation Learn Invariance?
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/LFhase/GALA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2096
    - null
    - null
    metric_stds:
    - 0.08
    - null
    - null
  - model: DIR
    model_plain: DIR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.12872'
    title: Discovering Invariant Rationales for Graph Neural Networks
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: https://github.com/Wuyxin/DIR-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2036
    - null
    - null
    metric_stds:
    - 0.0178
    - null
    - null
  - model: GSN
    model_plain: GSN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.12872'
    title: Discovering Invariant Rationales for Graph Neural Networks
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: https://github.com/Wuyxin/DIR-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1903
    - null
    - null
    metric_stds:
    - 0.0239
    - null
    - null
  - model: V-REx
    model_plain: V-REx
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.12872'
    title: Discovering Invariant Rationales for Graph Neural Networks
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: https://github.com/Wuyxin/DIR-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1892
    - null
    - null
    metric_stds:
    - 0.0141
    - null
    - null
  - model: IRM
    model_plain: IRM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.12872'
    title: Discovering Invariant Rationales for Graph Neural Networks
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: https://github.com/Wuyxin/DIR-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1862
    - null
    - null
    metric_stds:
    - 0.0122
    - null
    - null
  - model: DIR-Var
    model_plain: DIR-Var
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.12872'
    title: Discovering Invariant Rationales for Graph Neural Networks
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: https://github.com/Wuyxin/DIR-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1774
    - null
    - null
    metric_stds:
    - 0.0417
    - null
    - null
  - model: CAL_Meta (GIN)
    model_plain: CAL_Meta (GIN)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.07340'
    title: Towards Few-shot Self-explaining Graph Neural Networks
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: https://github.com/jypeng28/MSE-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1707
    - null
    - null
    metric_stds:
    - 0.0243
    - null
    - null
  - model: CIGA
    model_plain: CIGA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19035'
    title: Does Invariant Graph Learning via Environment Augmentation Learn Invariance?
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/LFhase/GALA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1583
    - null
    - null
    metric_stds:
    - 0.0256
    - null
    - null
  - model: ASAP
    model_plain: ASAP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.12872'
    title: Discovering Invariant Rationales for Graph Neural Networks
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: https://github.com/Wuyxin/DIR-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1554
    - null
    - null
    metric_stds:
    - 0.0187
    - null
    - null
  - model: GSAT
    model_plain: GSAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19035'
    title: Does Invariant Graph Learning via Environment Augmentation Learn Invariance?
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/LFhase/GALA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1524
    - null
    - null
    metric_stds:
    - 0.0372
    - null
    - null
  - model: Attention
    model_plain: Attention
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.12872'
    title: Discovering Invariant Rationales for Graph Neural Networks
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: https://github.com/Wuyxin/DIR-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1519
    - null
    - null
    metric_stds:
    - 0.0262
    - null
    - null
  - model: Group DRO
    model_plain: Group DRO
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.12872'
    title: Discovering Invariant Rationales for Graph Neural Networks
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: https://github.com/Wuyxin/DIR-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1513
    - null
    - null
    metric_stds:
    - 0.0283
    - null
    - null
  - model: Top-k Pool
    model_plain: Top-k Pool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.12872'
    title: Discovering Invariant Rationales for Graph Neural Networks
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: https://github.com/Wuyxin/DIR-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1491
    - null
    - null
    metric_stds:
    - 0.0325
    - null
    - null
  - model: SAG Pool
    model_plain: SAG Pool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.12872'
    title: Discovering Invariant Rationales for Graph Neural Networks
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: https://github.com/Wuyxin/DIR-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1431
    - null
    - null
    metric_stds:
    - 0.0244
    - null
    - null
  - model: GREA
    model_plain: GREA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19035'
    title: Does Invariant Graph Learning via Environment Augmentation Learn Invariance?
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/LFhase/GALA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1277
    - null
    - null
    metric_stds:
    - 0.0171
    - null
    - null
  - model: ERM
    model_plain: ERM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.12872'
    title: Discovering Invariant Rationales for Graph Neural Networks
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: https://github.com/Wuyxin/DIR-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1271
    - null
    - null
    metric_stds:
    - 0.0143
    - null
    - null
  - model: GIL
    model_plain: GIL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19035'
    title: Does Invariant Graph Learning via Environment Augmentation Learn Invariance?
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/LFhase/GALA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1255
    - null
    - null
    metric_stds:
    - 0.0126
    - null
    - null
  - model: FC-LSTM
    model_plain: FC-LSTM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1612.07659'
    title: Structured Sequence Modeling with Graph Convolutional Recurrent Networks
    date: Dec 2016
    date_iso: 2016-12
    date_display: Dec 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 48.32
    metric_stds:
    - null
    - null
    - null
  - model: LSTM+CNN
    model_plain: LSTM+CNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1612.07659'
    title: Structured Sequence Modeling with Graph Convolutional Recurrent Networks
    date: Dec 2016
    date_iso: 2016-12
    date_display: Dec 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 38.66
    metric_stds:
    - null
    - null
    - null
  - model: ELBO (i.i.d. sampling)
    model_plain: ELBO (i.i.d. sampling)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.02096'
    title: 'Top-N: Equivariant set and graph generation without exchangeability'
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.0001642
    - null
    metric_stds:
    - null
    - 5.3e-06
    - null
  - model: ELBO (First-n)
    model_plain: ELBO (First-n)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.02096'
    title: 'Top-N: Equivariant set and graph generation without exchangeability'
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.0001545
    - null
    metric_stds:
    - null
    - 1.41e-05
    - null
  - model: ELBO (Top-n)
    model_plain: ELBO (Top-n)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.02096'
    title: 'Top-N: Equivariant set and graph generation without exchangeability'
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.0001498
    - null
    metric_stds:
    - null
    - 5.9e-06
    - null
  - model: TSPN (i.i.d. sampling)
    model_plain: TSPN (i.i.d. sampling)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.02096'
    title: 'Top-N: Equivariant set and graph generation without exchangeability'
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.0001642
    - null
    metric_stds:
    - null
    - 5.3e-06
    - null
  - model: TSPN (First-n)
    model_plain: TSPN (First-n)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.02096'
    title: 'Top-N: Equivariant set and graph generation without exchangeability'
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.0001545
    - null
    metric_stds:
    - null
    - 1.41e-05
    - null
  - model: TSPN (Top-n)
    model_plain: TSPN (Top-n)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.02096'
    title: 'Top-N: Equivariant set and graph generation without exchangeability'
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.0001498
    - null
    metric_stds:
    - null
    - 5.9e-06
    - null
  - model: DSPN (i.i.d. sampling)
    model_plain: DSPN (i.i.d. sampling)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.02096'
    title: 'Top-N: Equivariant set and graph generation without exchangeability'
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.0002856
    - null
    metric_stds:
    - null
    - 1.23e-05
    - null
  - model: DSPN (First-n)
    model_plain: DSPN (First-n)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.02096'
    title: 'Top-N: Equivariant set and graph generation without exchangeability'
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.0002661
    - null
    metric_stds:
    - null
    - 5.4e-06
    - null
  - model: DSPN (Top-n)
    model_plain: DSPN (Top-n)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.02096'
    title: 'Top-N: Equivariant set and graph generation without exchangeability'
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.0002259
    - null
    metric_stds:
    - null
    - 1.71e-05
    - null
  milestones:
  - value: 0.987
    std: null
    model: 400-LRF3200-MP800-LRF800-MP400-10
    arxiv_id: '1312.6203'
    title: Spectral Networks and Locally Connected Networks on Graphs
    date: '2013-12-21'
  - value: 0.9933
    std: null
    model: Classical CNN
    arxiv_id: '1606.09375'
    title: Convolutional Neural Networks on Graphs with Fast Localized Spectral Filtering
    date: 2016-06
---

