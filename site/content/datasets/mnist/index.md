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
result_count: 47
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
    metric_stds:
    - null
  - model: LeNet5
    model_plain: LeNet5
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 1.66
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
    metric_stds:
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
    metric_stds:
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
    metric_stds:
    - null
  - model: ChebNet
    model_plain: ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 1.66
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
    metric_stds:
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
    metric_stds:
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
    metric_stds:
    - 0.00138
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
    metric_stds:
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
    metric_stds:
    - 0.00039
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
    metric_stds:
    - 0.00051
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
    metric_stds:
    - 0.0004
  - model: Graph-Mamba
    model_plain: Graph-Mamba
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.285125
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
    metric_stds:
    - 0.0008
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
    metric_stds:
    - 0.00012
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
    metric_stds:
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
    metric_stds:
    - 0.0003
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
    metric_stds:
    - 0.0004
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
    metric_stds:
    - 0.0006
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
    metric_stds:
    - 0.0005
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
    metric_stds:
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
    metric_stds:
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
    metric_stds:
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
    metric_stds:
    - 0.0011
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
    metric_stds:
    - 0.00087
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
    metric_stds:
    - 0.0001
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
    metric_stds:
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
    metric_stds:
    - 0.0014
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
    metric_stds:
    - 0.00183
  - model: GPS+Transformer
    model_plain: GPS+Transformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.286725
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
    metric_stds:
    - 0.0011
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
    metric_stds:
    - 0.00111
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
    metric_stds:
    - 0.00126
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
    metric_stds:
    - 0.00126
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
    metric_stds:
    - 0.0005
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
    metric_stds:
    - 0.0005
<<<<<<< Updated upstream
    - null
    - null
    - null
  - model: CRaWl
    model_plain: CRaWl
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.08786'
    title: 'Walking Out of the Weisfeiler Leman Hierarchy: Graph Learning Beyond Message
      Passing'
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/toenshoff/CRaWl
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.97944
    - null
    - null
    - null
    metric_stds:
    - 0.0005
    - null
    - null
    - null
=======
>>>>>>> Stashed changes
  - model: PNA
    model_plain: PNA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
<<<<<<< Updated upstream
    arxiv_id: '2102.08786'
    title: 'Walking Out of the Weisfeiler Leman Hierarchy: Graph Learning Beyond Message
      Passing'
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/toenshoff/CRaWl
=======
    arxiv_id: '2205.12454'
    title: Recipe for a General, Powerful, Scalable Graph Transformer
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/rampasek/GraphGPS
>>>>>>> Stashed changes
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9794
    metric_stds:
    - 0.0012
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
    metric_stds:
    - 0.00176
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
    metric_stds:
    - 0.00105
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
    metric_stds:
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
    metric_stds:
    - 0.00022
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
    metric_stds:
    - null
<<<<<<< Updated upstream
  - model: GatedGCN-16
    model_plain: GatedGCN-16
=======
  - model: GatedGCN
    model_plain: GatedGCN
>>>>>>> Stashed changes
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
<<<<<<< Updated upstream
    arxiv_id: '2404.09774'
    title: 'RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional
      Networks'
    date: Apr 2024
    date_iso: 2024-04
    date_display: Apr 2024
    codebase_url: ''
=======
    arxiv_id: '2108.03348'
    title: Global Self-Attention as a Replacement for Graph Convolution
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/shamim-hussain/egt
>>>>>>> Stashed changes
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9734
<<<<<<< Updated upstream
    - null
    - null
    - null
    metric_stds:
    - 0.00143
    - null
    - null
    - null
  - model: GatedGCN
    model_plain: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.08786'
    title: 'Walking Out of the Weisfeiler Leman Hierarchy: Graph Learning Beyond Message
      Passing'
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/toenshoff/CRaWl
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9734
    - null
    - null
    - null
    metric_stds:
    - 0.00143
    - null
    - null
    - null
=======
    metric_stds:
    - 0.00143
>>>>>>> Stashed changes
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
<<<<<<< Updated upstream
    arxiv_id: '2102.08786'
    title: 'Walking Out of the Weisfeiler Leman Hierarchy: Graph Learning Beyond Message
      Passing'
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/toenshoff/CRaWl
=======
    arxiv_id: '2108.03348'
    title: Global Self-Attention as a Replacement for Graph Convolution
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/shamim-hussain/egt
>>>>>>> Stashed changes
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.97312
    metric_stds:
    - 0.00097
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
    metric_stds:
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
<<<<<<< Updated upstream
    arxiv_id: '2102.08786'
    title: 'Walking Out of the Weisfeiler Leman Hierarchy: Graph Learning Beyond Message
      Passing'
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/toenshoff/CRaWl
=======
    arxiv_id: '2108.03348'
    title: Global Self-Attention as a Replacement for Graph Convolution
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/shamim-hussain/egt
>>>>>>> Stashed changes
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.96485
<<<<<<< Updated upstream
    - null
    - null
    - null
    metric_stds:
    - 0.00252
    - null
    - null
    - null
  - model: S4G
    model_plain: S4G
=======
    metric_stds:
    - 0.00097
  - model: Nearest Neighbors
    model_plain: Nearest Neighbors
>>>>>>> Stashed changes
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
    metric_stds:
    - null
<<<<<<< Updated upstream
  - model: GAT-16
    model_plain: GAT-16
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.09774'
    title: 'RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional
      Networks'
    date: Apr 2024
    date_iso: 2024-04
    date_display: Apr 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.95535
    - null
    - null
    - null
    metric_stds:
    - 0.00205
    - null
    - null
    - null
=======
>>>>>>> Stashed changes
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
<<<<<<< Updated upstream
    arxiv_id: '2102.08786'
    title: 'Walking Out of the Weisfeiler Leman Hierarchy: Graph Learning Beyond Message
      Passing'
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/toenshoff/CRaWl
=======
    arxiv_id: '2108.03348'
    title: Global Self-Attention as a Replacement for Graph Convolution
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/shamim-hussain/egt
>>>>>>> Stashed changes
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.95535
<<<<<<< Updated upstream
    - null
    - null
    - null
    metric_stds:
    - 0.00205
    - null
    - null
    - null
=======
    metric_stds:
    - 0.00205
>>>>>>> Stashed changes
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
    metric_stds:
    - 0.00613
<<<<<<< Updated upstream
    - null
    - null
    - null
  - model: GatedGCN-DENS + LPE + G-\DeltaUQ
    model_plain: GatedGCN-DENS + LPE + G-\DeltaUQ
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.03350'
    title: Accurate and Scalable Estimation of Epistemic Uncertainty for Graph Neural
      Networks
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.954
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
  - model: 3WLGNN
    model_plain: 3WLGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.08786'
    title: 'Walking Out of the Weisfeiler Leman Hierarchy: Graph Learning Beyond Message
      Passing'
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/toenshoff/CRaWl
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.95075
    - null
    - null
    - null
    metric_stds:
    - 0.00961
    - null
    - null
    - null
  - model: GatedGCN + G-\DeltaUQ
    model_plain: GatedGCN + G-\DeltaUQ
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.03350'
    title: Accurate and Scalable Estimation of Epistemic Uncertainty for Graph Neural
      Networks
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.949
    - null
    - 0.022
    - null
    metric_stds:
    - 0.008
    - null
    - 0.007
    - null
  - model: GatedGCN+LapPE
    model_plain: GatedGCN+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.03350'
    title: Accurate and Scalable Estimation of Epistemic Uncertainty for Graph Neural
      Networks
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.949
    - null
    - 0.036
    - null
    metric_stds:
    - 0.002
    - null
    - 0.003
    - null
  - model: GatedGCN
    model_plain: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.03350'
    title: Accurate and Scalable Estimation of Epistemic Uncertainty for Graph Neural
      Networks
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.947
    - null
    - 0.038
    - null
    metric_stds:
    - 0.002
    - null
    - 0.001
    - null
  - model: GT
    model_plain: GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.90831
    - null
    - null
    - null
    metric_stds:
    - 0.00161
    - null
    - null
    - null
  - model: MoNet
    model_plain: MoNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.09774'
    title: 'RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional
      Networks'
    date: Apr 2024
    date_iso: 2024-04
    date_display: Apr 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.90805
    - null
    - null
    - null
    metric_stds:
    - 0.00032
    - null
    - null
    - null
=======
>>>>>>> Stashed changes
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
<<<<<<< Updated upstream
    arxiv_id: '2102.08786'
    title: 'Walking Out of the Weisfeiler Leman Hierarchy: Graph Learning Beyond Message
      Passing'
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/toenshoff/CRaWl
=======
    arxiv_id: '2108.03348'
    title: Global Self-Attention as a Replacement for Graph Convolution
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/shamim-hussain/egt
>>>>>>> Stashed changes
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.90705
    metric_stds:
    - 0.00218
  milestones:
<<<<<<< Updated upstream
  - value: 0.97944
    std: 0.0005
    model: CRaWl
    arxiv_id: '2102.08786'
    title: 'Walking Out of the Weisfeiler Leman Hierarchy: Graph Learning Beyond Message
      Passing'
    date: 2021-02
  - value: 0.9835
    std: 0.001
    model: Graph MLP-Mixer
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
  - value: 0.9855
    std: 0.00039
    model: Exphormer
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: 2023-08
  - value: 0.98692
    std: 0.00079
    model: NeuralWalker
    arxiv_id: '2406.03386'
    title: Learning Long Range Dependencies on Graphs via Random Walks
    date: 2024-06
  - value: 0.98932
    std: 0.00076
    model: GRASS
    arxiv_id: '2407.05649'
    title: 'Greener GRASS: Enhancing GNNs with Encoding, Rewiring, and Attention'
    date: 2024-07
=======
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
>>>>>>> Stashed changes
---

