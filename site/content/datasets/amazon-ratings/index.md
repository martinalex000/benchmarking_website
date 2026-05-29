---
title: Amazon-ratings
slug: amazon-ratings
benchmark: Heterophilic Graphs
task_type: node_classification
description: Amazon product co-purchase node classification (5 rating classes) from
  the heterophilic benchmark.
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.HeterophilousGraphDataset.html
stats: null
result_count: 111
best_model:
  model: here instead
  value: 0.909
  metric: Accuracy
  arxiv_id: '1506.04757'
  paper_title: Image-based Recommendations on Styles and Substitutes
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
  - model: here instead
    model_plain: here instead
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1506.04757'
    title: Image-based Recommendations on Styles and Substitutes
    date: Jun 2015
    date_iso: 2015-06
    date_display: Jun 2015
    codebase_url: ''
    uses_external_data: null
    is_best: true
    metric_values:
    - 0.909
    metric_stds:
    - null
  - model: CT
    model_plain: CT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1506.04757'
    title: Image-based Recommendations on Styles and Substitutes
    date: Jun 2015
    date_iso: 2015-06
    date_display: Jun 2015
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.848
    metric_stds:
    - null
  - model: WNN
    model_plain: WNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1506.04757'
    title: Image-based Recommendations on Styles and Substitutes
    date: Jun 2015
    date_iso: 2015-06
    date_display: Jun 2015
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.843
    metric_stds:
    - null
  - model: DiSRW
    model_plain: DiSRW
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10320'
    title: 'DiRW: Path-Aware Digraph Learning for Heterophily'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/dhsiuu/DiRW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.835
    metric_stds:
    - 0.0068
  - model: MagNet
    model_plain: MagNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10320'
    title: 'DiRW: Path-Aware Digraph Learning for Heterophily'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/dhsiuu/DiRW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8341
    metric_stds:
    - 0.0099
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10320'
    title: 'DiRW: Path-Aware Digraph Learning for Heterophily'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/dhsiuu/DiRW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8326
    metric_stds:
    - 0.0051
  - model: DGCNN
    model_plain: DGCNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10320'
    title: 'DiRW: Path-Aware Digraph Learning for Heterophily'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/dhsiuu/DiRW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8295
    metric_stds:
    - 0.0113
  - model: DiGCNappr
    model_plain: DiGCNappr
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10320'
    title: 'DiRW: Path-Aware Digraph Learning for Heterophily'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/dhsiuu/DiRW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8153
    metric_stds:
    - 0.0127
  - model: Dir-GNN
    model_plain: Dir-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10320'
    title: 'DiRW: Path-Aware Digraph Learning for Heterophily'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/dhsiuu/DiRW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8134
    metric_stds:
    - 0.0092
  - model: MGC
    model_plain: MGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10320'
    title: 'DiRW: Path-Aware Digraph Learning for Heterophily'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/dhsiuu/DiRW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8126
    metric_stds:
    - 0.008
  - model: G2P2
    model_plain: G2P2
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.03324'
    title: Augmenting Low-Resource Text Classification with Graph-Grounded Pre-training
      and Prompting
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8103
    metric_stds:
    - 0.0043
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10320'
    title: 'DiRW: Path-Aware Digraph Learning for Heterophily'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/dhsiuu/DiRW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8016
    metric_stds:
    - 0.0232
  - model: DiGCN
    model_plain: DiGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10320'
    title: 'DiRW: Path-Aware Digraph Learning for Heterophily'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/dhsiuu/DiRW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8002
    metric_stds:
    - 0.0152
  - model: LightDiC
    model_plain: LightDiC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10320'
    title: 'DiRW: Path-Aware Digraph Learning for Heterophily'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/dhsiuu/DiRW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7987
    metric_stds:
    - 0.0068
  - model: NSTE
    model_plain: NSTE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10320'
    title: 'DiRW: Path-Aware Digraph Learning for Heterophily'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/dhsiuu/DiRW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.785
    metric_stds:
    - 0.0187
  - model: DIMPA
    model_plain: DIMPA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10320'
    title: 'DiRW: Path-Aware Digraph Learning for Heterophily'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/dhsiuu/DiRW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.778
    metric_stds:
    - 0.0142
  - model: ADPA
    model_plain: ADPA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10320'
    title: 'DiRW: Path-Aware Digraph Learning for Heterophily'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/dhsiuu/DiRW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7325
    metric_stds:
    - 0.0426
  - model: RAWGNN
    model_plain: RAWGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10320'
    title: 'DiRW: Path-Aware Digraph Learning for Heterophily'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/dhsiuu/DiRW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7276
    metric_stds:
    - 0.0067
  - model: PathNet
    model_plain: PathNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10320'
    title: 'DiRW: Path-Aware Digraph Learning for Heterophily'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/dhsiuu/DiRW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6878
    metric_stds:
    - 0.0213
  - model: Polynormer
    model_plain: Polynormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5481
    metric_stds:
    - 0.0049
  - model: CO-GNN
    model_plain: CO-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.542
    metric_stds:
    - 0.0034
  - model: CO-GNN(μ, μ)
    model_plain: CO-GNN(μ, μ)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5417
    metric_stds:
    - 0.0037
  - model: GMN
    model_plain: GMN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5407
    metric_stds:
    - 0.0031
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
    - 0.5383
    metric_stds:
    - 0.0032
  - model: BuNN
    model_plain: BuNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5374
    metric_stds:
    - 0.0051
  - model: MP-SSM
    model_plain: MP-SSM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5365
    metric_stds:
    - 0.0071
  - model: SAGE
    model_plain: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11640'
    title: 'A critical look at the evaluation of GNNs under heterophily: Are we really
      making progress?'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/yandex-research/heterophilous-graphs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5363
    metric_stds:
    - 0.0039
  - model: Exphormer
    model_plain: Exphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5351
    metric_stds:
    - 0.0046
  - model: GRAMA_GCNI
    model_plain: GRAMA_GCNI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5348
    metric_stds:
    - 0.0062
  - model: Stable-ChebNet
    model_plain: Stable-ChebNet
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5315
    metric_stds:
    - 0.0021
  - model: GPS
    model_plain: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.531
    metric_stds:
    - 0.0042
  - model: FSGNN
    model_plain: FSGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11640'
    title: 'A critical look at the evaluation of GNNs under heterophily: Are we really
      making progress?'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/yandex-research/heterophilous-graphs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5274
    metric_stds:
    - 0.0083
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
    - 0.526
    metric_stds:
    - 0.0053
  - model: GT-sep
    model_plain: GT-sep
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11640'
    title: 'A critical look at the evaluation of GNNs under heterophily: Are we really
      making progress?'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/yandex-research/heterophilous-graphs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5218
    metric_stds:
    - 0.008
  - model: CSNN
    model_plain: CSNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5207
    metric_stds:
    - 0.01
  - model: SNNs
    model_plain: SNNs
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5207
    metric_stds:
    - 0.01
  - model: ResNet+adj
    model_plain: ResNet+adj
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11640'
    title: 'A critical look at the evaluation of GNNs under heterophily: Are we really
      making progress?'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/yandex-research/heterophilous-graphs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5183
    metric_stds:
    - 0.0057
  - model: CO-GNN(Σ, Σ)
    model_plain: CO-GNN(Σ, Σ)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5128
    metric_stds:
    - 0.0056
  - model: NAGphormer
    model_plain: NAGphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5126
    metric_stds:
    - 0.0072
  - model: GT
    model_plain: GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11640'
    title: 'A critical look at the evaluation of GNNs under heterophily: Are we really
      making progress?'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/yandex-research/heterophilous-graphs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5117
    metric_stds:
    - 0.0066
  - model: COMBA
    model_plain: COMBA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.17893'
    title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs with Context
      Gating State Space Models'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.507
    metric_stds:
    - 0.0025
  - model: ResNet+SGC
    model_plain: ResNet+SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11640'
    title: 'A critical look at the evaluation of GNNs under heterophily: Are we really
      making progress?'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/yandex-research/heterophilous-graphs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5066
    metric_stds:
    - 0.0048
  - model: Acc(MLP)
    model_plain: Acc(MLP)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.09125'
    title: arXiv:2401.09125
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5058
    metric_stds:
    - null
  - model: GPS_GCNI+Performer (RWSE)
    model_plain: GPS_GCNI+Performer (RWSE)
    is_baseline: true
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
    - 0.4992
    metric_stds:
    - 0.0068
  - model: MLP-2
    model_plain: MLP-2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4955
    metric_stds:
    - 0.0081
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11640'
    title: 'A critical look at the evaluation of GNNs under heterophily: Are we really
      making progress?'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/yandex-research/heterophilous-graphs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4909
    metric_stds:
    - 0.0063
  - model: Graph-Mamba
    model_plain: Graph-Mamba
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.17893'
    title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs with Context
      Gating State Space Models'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.49
    metric_stds:
    - 0.0036
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11640'
    title: 'A critical look at the evaluation of GNNs under heterophily: Are we really
      making progress?'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/yandex-research/heterophilous-graphs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.487
    metric_stds:
    - 0.0063
  - model: GDT + RWSE
    model_plain: GDT + RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4858
    metric_stds:
    - 0.0041
  - model: GPS_GCNI+Performer (LapPE)
    model_plain: GPS_GCNI+Performer (LapPE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.482
    metric_stds:
    - 0.0067
  - model: GatedGCN
    model_plain: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.17893'
    title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs with Context
      Gating State Space Models'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.481
    metric_stds:
    - 0.0071
  - model: GPS_GCNI+Performer (RWSE)
    model_plain: GPS_GCNI+Performer (RWSE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4808
    metric_stds:
    - 0.0085
  - model: Acc(GCN)
    model_plain: Acc(GCN)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.09125'
    title: arXiv:2401.09125
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4801
    metric_stds:
    - null
  - model: Cluster-GCN
    model_plain: Cluster-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.17893'
    title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs with Context
      Gating State Space Models'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.476
    metric_stds:
    - 0.0047
  - model: GCN (RWSE)
    model_plain: GCN (RWSE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.464
    metric_stds:
    - 0.0055
  - model: EDEN
    model_plain: EDEN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.00983'
    title: 'Toward Data-centric Directed Graph Learning: An Entropy-driven Approach'
    date: May 2, 2025
    date_iso: '2025-05-02'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.463
    metric_stds:
    - 0.004
  - model: SpaM
    model_plain: SpaM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01207'
    title: Sparse Bayesian Message Passing under Structural Uncertainty
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.463
    metric_stds:
    - 0.0088
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.17893'
    title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs with Context
      Gating State Space Models'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.462
    metric_stds:
    - 0.008
  - model: G2T-LimiX (FT)
    model_plain: G2T-LimiX (FT)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.21489'
    title: 'GraphPFN: A Prior-Data Fitted Graph Foundation Model'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: https://github.com/yandex-research/graphpfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4605
    metric_stds:
    - 0.0023
  - model: GBK-GNN
    model_plain: GBK-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11640'
    title: 'A critical look at the evaluation of GNNs under heterophily: Are we really
      making progress?'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/yandex-research/heterophilous-graphs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4598
    metric_stds:
    - 0.0071
  - model: ResNet
    model_plain: ResNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11640'
    title: 'A critical look at the evaluation of GNNs under heterophily: Are we really
      making progress?'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/yandex-research/heterophilous-graphs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.459
    metric_stds:
    - 0.0052
  - model: GraphPFN (FT)
    model_plain: GraphPFN (FT)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.21489'
    title: 'GraphPFN: A Prior-Data Fitted Graph Foundation Model'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: https://github.com/yandex-research/graphpfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4589
    metric_stds:
    - 0.0053
  - model: GPS + Mamba
    model_plain: GPS + Mamba
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4513
    metric_stds:
    - 0.0097
  - model: GAT (LapPE)
    model_plain: GAT (LapPE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.449
    metric_stds:
    - 0.0073
  - model: D-HYPR
    model_plain: D-HYPR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.00983'
    title: 'Toward Data-centric Directed Graph Learning: An Entropy-driven Approach'
    date: May 2, 2025
    date_iso: '2025-05-02'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.449
    metric_stds:
    - 0.005
  - model: TAG-LimiX (ICL, E)
    model_plain: TAG-LimiX (ICL, E)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.21489'
    title: 'GraphPFN: A Prior-Data Fitted Graph Foundation Model'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: https://github.com/yandex-research/graphpfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4489
    metric_stds:
    - 0.0015
  - model: GPR-GNN
    model_plain: GPR-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11640'
    title: 'A critical look at the evaluation of GNNs under heterophily: Are we really
      making progress?'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/yandex-research/heterophilous-graphs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4488
    metric_stds:
    - 0.0034
  - model: DGCNN
    model_plain: DGCNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.00983'
    title: 'Toward Data-centric Directed Graph Learning: An Entropy-driven Approach'
    date: May 2, 2025
    date_iso: '2025-05-02'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.447
    metric_stds:
    - 0.006
  - model: MagNet
    model_plain: MagNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.00983'
    title: 'Toward Data-centric Directed Graph Learning: An Entropy-driven Approach'
    date: May 2, 2025
    date_iso: '2025-05-02'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.447
    metric_stds:
    - 0.006
  - model: G2T-LimiX (ICL)
    model_plain: G2T-LimiX (ICL)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.21489'
    title: 'GraphPFN: A Prior-Data Fitted Graph Foundation Model'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: https://github.com/yandex-research/graphpfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4465
    metric_stds:
    - 0.0018
  - model: GOAT
    model_plain: GOAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4461
    metric_stds:
    - 0.005
  - model: DIMPA
    model_plain: DIMPA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.00983'
    title: 'Toward Data-centric Directed Graph Learning: An Entropy-driven Approach'
    date: May 2, 2025
    date_iso: '2025-05-02'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.446
    metric_stds:
    - 0.005
  - model: GraphPFN (ICL)
    model_plain: GraphPFN (ICL)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.21489'
    title: 'GraphPFN: A Prior-Data Fitted Graph Foundation Model'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: https://github.com/yandex-research/graphpfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4452
    metric_stds:
    - 0.0027
  - model: HoloNet
    model_plain: HoloNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.00983'
    title: 'Toward Data-centric Directed Graph Learning: An Entropy-driven Approach'
    date: May 2, 2025
    date_iso: '2025-05-02'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.445
    metric_stds:
    - 0.006
  - model: GCN (LapPE)
    model_plain: GCN (LapPE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4435
    metric_stds:
    - 0.0036
  - model: DiGCN
    model_plain: DiGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.00983'
    title: 'Toward Data-centric Directed Graph Learning: An Entropy-driven Approach'
    date: May 2, 2025
    date_iso: '2025-05-02'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.443
    metric_stds:
    - 0.007
  - model: FAGCN
    model_plain: FAGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11640'
    title: 'A critical look at the evaluation of GNNs under heterophily: Are we really
      making progress?'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/yandex-research/heterophilous-graphs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4412
    metric_stds:
    - 0.003
  - model: TAG-TabPFNv2 (ICL, E)
    model_plain: TAG-TabPFNv2 (ICL, E)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.21489'
    title: 'GraphPFN: A Prior-Data Fitted Graph Foundation Model'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: https://github.com/yandex-research/graphpfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4397
    metric_stds:
    - 0.0052
  - model: CPGNN
    model_plain: CPGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01207'
    title: Sparse Bayesian Message Passing under Structural Uncertainty
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.439
    metric_stds:
    - 0.0075
  - model: GATv2
    model_plain: GATv2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.00983'
    title: 'Toward Data-centric Directed Graph Learning: An Entropy-driven Approach'
    date: May 2, 2025
    date_iso: '2025-05-02'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.438
    metric_stds:
    - 0.006
  - model: TFE-GNN
    model_plain: TFE-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01207'
    title: Sparse Bayesian Message Passing under Structural Uncertainty
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.437
    metric_stds:
    - 0.0072
  - model: AGT
    model_plain: AGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.00983'
    title: 'Toward Data-centric Directed Graph Learning: An Entropy-driven Approach'
    date: May 2, 2025
    date_iso: '2025-05-02'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.436
    metric_stds:
    - 0.004
  - model: JacobiConv
    model_plain: JacobiConv
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11640'
    title: 'A critical look at the evaluation of GNNs under heterophily: Are we really
      making progress?'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/yandex-research/heterophilous-graphs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4355
    metric_stds:
    - 0.0048
  - model: Dir-GNN
    model_plain: Dir-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01207'
    title: Sparse Bayesian Message Passing under Structural Uncertainty
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.434
    metric_stds:
    - 0.0071
  - model: L2DGCN
    model_plain: L2DGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01207'
    title: Sparse Bayesian Message Passing under Structural Uncertainty
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.432
    metric_stds:
    - 0.0067
  - model: GatedGCN
    model_plain: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.43
    metric_stds:
    - 0.0032
  - model: TS-GNN (ICL)
    model_plain: TS-GNN (ICL)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.21489'
    title: 'GraphPFN: A Prior-Data Fitted Graph Foundation Model'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: https://github.com/yandex-research/graphpfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.43
    metric_stds:
    - 0.0013
  - model: O(d)-NSD
    model_plain: O(d)-NSD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4276
    metric_stds:
    - 0.0054
  - model: Auto-HeG
    model_plain: Auto-HeG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01207'
    title: Sparse Bayesian Message Passing under Structural Uncertainty
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.427
    metric_stds:
    - 0.0068
  - model: ACMGCN
    model_plain: ACMGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01207'
    title: Sparse Bayesian Message Passing under Structural Uncertainty
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.424
    metric_stds:
    - 0.0061
  - model: GCNII
    model_plain: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.00983'
    title: 'Toward Data-centric Directed Graph Learning: An Entropy-driven Approach'
    date: May 2, 2025
    date_iso: '2025-05-02'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.423
    metric_stds:
    - 0.005
  - model: PCNet
    model_plain: PCNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01207'
    title: Sparse Bayesian Message Passing under Structural Uncertainty
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.423
    metric_stds:
    - 0.0064
  - model: GPRGNN
    model_plain: GPRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01207'
    title: Sparse Bayesian Message Passing under Structural Uncertainty
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.42
    metric_stds:
    - 0.0063
  - model: MagNet
    model_plain: MagNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01207'
    title: Sparse Bayesian Message Passing under Structural Uncertainty
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.419
    metric_stds:
    - 0.0071
  - model: GloGNN
    model_plain: GloGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01207'
    title: Sparse Bayesian Message Passing under Structural Uncertainty
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.419
    metric_stds:
    - 0.0067
  - model: GT
    model_plain: GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.21489'
    title: 'GraphPFN: A Prior-Data Fitted Graph Foundation Model'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: https://github.com/yandex-research/graphpfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4156
    metric_stds:
    - 0.004
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.21489'
    title: 'GraphPFN: A Prior-Data Fitted Graph Foundation Model'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: https://github.com/yandex-research/graphpfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4143
    metric_stds:
    - 0.0049
  - model: H2GCN
    model_plain: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01207'
    title: Sparse Bayesian Message Passing under Structural Uncertainty
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.413
    metric_stds:
    - 0.0062
  - model: FAGCN
    model_plain: FAGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01207'
    title: Sparse Bayesian Message Passing under Structural Uncertainty
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.409
    metric_stds:
    - 0.0059
  - model: SGC-1
    model_plain: SGC-1
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4069
    metric_stds:
    - 0.0042
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.21489'
    title: 'GraphPFN: A Prior-Data Fitted Graph Foundation Model'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: https://github.com/yandex-research/graphpfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4067
    metric_stds:
    - 0.0055
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.21489'
    title: 'GraphPFN: A Prior-Data Fitted Graph Foundation Model'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: https://github.com/yandex-research/graphpfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4007
    metric_stds:
    - 0.0053
  - model: GCOPE (FT)
    model_plain: GCOPE (FT)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.21489'
    title: 'GraphPFN: A Prior-Data Fitted Graph Foundation Model'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: https://github.com/yandex-research/graphpfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.399
    metric_stds:
    - 0.0043
  - model: CPGNN
    model_plain: CPGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11640'
    title: 'A critical look at the evaluation of GNNs under heterophily: Are we really
      making progress?'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/yandex-research/heterophilous-graphs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3979
    metric_stds:
    - 0.0077
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01207'
    title: Sparse Bayesian Message Passing under Structural Uncertainty
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.39
    metric_stds:
    - 0.0052
  - model: MLP-1
    model_plain: MLP-1
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.386
    metric_stds:
    - 0.0041
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01207'
    title: Sparse Bayesian Message Passing under Structural Uncertainty
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.385
    metric_stds:
    - 0.0045
  - model: GloGNN
    model_plain: GloGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11640'
    title: 'A critical look at the evaluation of GNNs under heterophily: Are we really
      making progress?'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/yandex-research/heterophilous-graphs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3689
    metric_stds:
    - 0.0014
  - model: H2GCN
    model_plain: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11640'
    title: 'A critical look at the evaluation of GNNs under heterophily: Are we really
      making progress?'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/yandex-research/heterophilous-graphs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3647
    metric_stds:
    - 0.0023
  - model: AnyGraph (ICL)
    model_plain: AnyGraph (ICL)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.21489'
    title: 'GraphPFN: A Prior-Data Fitted Graph Foundation Model'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: https://github.com/yandex-research/graphpfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3349
    metric_stds:
    - 0.0344
  - model: OpenGraph (ICL)
    model_plain: OpenGraph (ICL)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.21489'
    title: 'GraphPFN: A Prior-Data Fitted Graph Foundation Model'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: https://github.com/yandex-research/graphpfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2936
    metric_stds:
    - 0.0124
  milestones:
  - value: 0.909
    std: null
    model: here instead
    arxiv_id: '1506.04757'
    title: Image-based Recommendations on Styles and Substitutes
    date: 2015-06
---

