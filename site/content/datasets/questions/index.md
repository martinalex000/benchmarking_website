---
title: Questions
slug: questions
benchmark: Heterophilic Graphs
task_type: node_classification
description: Yandex Q&A expert network binary node classification from the heterophilic
  benchmark.
primary_metric: ROC-AUC
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.HeterophilousGraphDataset.html
stats:
  num_graphs: null
  avg_nodes: 48921.0
  avg_edges: 153540.0
  num_classes: 2
result_count: 65
best_model:
  model: IM-CO-GNN(Σ,Σ)
  value: 0.8049
  metric: ROC-AUC
  arxiv_id: '2505.23185'
  paper_title: Improving the Effective Receptive Field of Message-Passing Neural Networks
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: ROC-AUC
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - ROC-AUC
  rows:
  - model: IM-CO-GNN(Σ,Σ)
    model_plain: IM-CO-GNN(Σ,Σ)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: May 29, 2025
    date_iso: '2025-05-29'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: null
    is_best: true
    metric_values:
    - 0.8049
    metric_stds:
    - 0.0092
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
    is_best: true
    metric_values:
    - 0.8039000000000001
    metric_stds:
    - 0.0104
  - model: Tango<sub>GatedGCN</sub>
    model_plain: TangoGatedGCN
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
    is_best: true
    metric_values:
    - 0.8039
    metric_stds:
    - 0.0104
  - model: Tango<sub>GPS</sub>
    model_plain: TangoGPS
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
    is_best: true
    metric_values:
    - 0.8032
    metric_stds:
    - 0.0107
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
    is_best: true
    metric_values:
    - 0.8031999999999999
    metric_stds:
    - 0.010700000000000001
  - model: CO-GNN(Σ, Σ)
    model_plain: CO-GNN(Σ, Σ)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01267'
    title: Cooperative Graph Neural Networks
    date: Oct 2, 2023
    date_iso: '2023-10-02'
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.8002
    metric_stds:
    - 0.0086
  - model: CO-GNN(\Sigma, \Sigma)
    model_plain: CO-GNN(\Sigma, \Sigma)
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
    is_best: true
    metric_values:
    - 0.8002
    metric_stds:
    - 0.0086
  - model: Lie Unitary GCN
    model_plain: Lie Unitary GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05499'
    title: Unitary convolutions for learning on graphs and groups
    date: Oct 7, 2024
    date_iso: '2024-10-07'
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.8001
    metric_stds:
    - 0.0043
  - model: CSNN
    model_plain: CSNN
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
    is_best: true
    metric_values:
    - 0.7931
    metric_stds:
    - 0.012199999999999999
  - model: IM-GatedGCN
    model_plain: IM-GatedGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: May 29, 2025
    date_iso: '2025-05-29'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: null
    is_best: true
    metric_values:
    - 0.7927
    metric_stds:
    - 0.0091
  - model: GENs
    model_plain: GENs
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.7922
    metric_stds:
    - 0.0074
  - model: Unitary GCN
    model_plain: Unitary GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05499'
    title: Unitary convolutions for learning on graphs and groups
    date: Oct 7, 2024
    date_iso: '2024-10-07'
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.7921
    metric_stds:
    - 0.0079
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.7902
    metric_stds:
    - 0.006
  - model: Polynormer
    model_plain: Polynormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.7894
    metric_stds:
    - 0.0078
  - model: IM-CO-GNN(μ,μ)
    model_plain: IM-CO-GNN(μ,μ)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: May 29, 2025
    date_iso: '2025-05-29'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: null
    is_best: true
    metric_values:
    - 0.7892
    metric_stds:
    - 0.0087
  - model: FSGNN
    model_plain: FSGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.7886
    metric_stds:
    - 0.0292
  - model: BuNN
    model_plain: BuNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.15540'
    title: Bundle Neural Networks for message diffusion on graphs
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.7875
    metric_stds:
    - 0.0109
  - model: NeuralWalker
    model_plain: NeuralWalker
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03386'
    title: Learning Long Range Dependencies on Graphs via Random Walks
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.7852
    metric_stds:
    - 0.0113
  - model: IM-GCN
    model_plain: IM-GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: May 29, 2025
    date_iso: '2025-05-29'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7817
    metric_stds:
    - 0.0089
  - model: IM-FAGCN
    model_plain: IM-FAGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: May 29, 2025
    date_iso: '2025-05-29'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7817
    metric_stds:
    - 0.0106
  - model: GAT-sep
    model_plain: GAT-sep
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01267'
    title: Cooperative Graph Neural Networks
    date: Oct 2, 2023
    date_iso: '2023-10-02'
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7805
    metric_stds:
    - 0.0093
  - model: IM-GAT
    model_plain: IM-GAT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: May 29, 2025
    date_iso: '2025-05-29'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7798
    metric_stds:
    - 0.0101
  - model: GT
    model_plain: GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01267'
    title: Cooperative Graph Neural Networks
    date: Oct 2, 2023
    date_iso: '2023-10-02'
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7795
    metric_stds:
    - 0.0068
  - model: IM-GAT-sep
    model_plain: IM-GAT-sep
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: May 29, 2025
    date_iso: '2025-05-29'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7792
    metric_stds:
    - 0.0083
  - model: GPS₃₀GCN+Performer
    model_plain: GPS₃₀GCN+Performer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: May 29, 2025
    date_iso: '2025-05-29'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7785
    metric_stds:
    - 0.0125
  - model: GDT (RWSE)
    model_plain: GDT (RWSE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: May 29, 2025
    date_iso: '2025-05-29'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7783
    metric_stds:
    - 0.0122
  - model: Gated + RWSE
    model_plain: Gated + RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: May 29, 2025
    date_iso: '2025-05-29'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7783
    metric_stds:
    - 0.0122
  - model: GIN + RWSE
    model_plain: GIN + RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: May 29, 2025
    date_iso: '2025-05-29'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7781
    metric_stds:
    - 0.014
  - model: R-GCN (RWSE)
    model_plain: R-GCN (RWSE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: May 29, 2025
    date_iso: '2025-05-29'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7781
    metric_stds:
    - 0.014
  - model: GCN+LapPE
    model_plain: GCN+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: May 29, 2025
    date_iso: '2025-05-29'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7779
    metric_stds:
    - 0.0134
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01267'
    title: Cooperative Graph Neural Networks
    date: Oct 2, 2023
    date_iso: '2023-10-02'
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7743
    metric_stds:
    - 0.012
  - model: FAGCN
    model_plain: FAGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: May 29, 2025
    date_iso: '2025-05-29'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7724
    metric_stds:
    - 0.0126
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7721
    metric_stds:
    - 0.0128
  - model: GPS_GAT+Performer (RWSE)
    model_plain: GPS_GAT+Performer (RWSE)
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
    - 0.7714
    metric_stds:
    - 0.0149
  - model: GPS₃₀GAT+Performer (RWSE)
    model_plain: GPS₃₀GAT+Performer (RWSE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: May 29, 2025
    date_iso: '2025-05-29'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7714
    metric_stds:
    - 0.0149
  - model: GPS<sub>GAT+Performer</sub> (RWSE)
    model_plain: GPSGAT+Performer (RWSE)
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
    - 0.7714
    metric_stds:
    - 0.0149
  - model: GAT (DEG)
    model_plain: GAT (DEG)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: May 29, 2025
    date_iso: '2025-05-29'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.771
    metric_stds:
    - 0.0123
  - model: GCN (DEG)
    model_plain: GCN (DEG)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: May 29, 2025
    date_iso: '2025-05-29'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7696
    metric_stds:
    - 0.0121
  - model: GPS₃₂GAT+Performer (LapPE)
    model_plain: GPS₃₂GAT+Performer (LapPE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: May 29, 2025
    date_iso: '2025-05-29'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7671
    metric_stds:
    - 0.0098
  - model: GatedGCN
    model_plain: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: May 29, 2025
    date_iso: '2025-05-29'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7661
    metric_stds:
    - 0.0113
  - model: GAT (LapPE)
    model_plain: GAT (LapPE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: May 29, 2025
    date_iso: '2025-05-29'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7655
    metric_stds:
    - 0.0084
  - model: CO-GNN(μ, μ)
    model_plain: CO-GNN(μ, μ)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01267'
    title: Cooperative Graph Neural Networks
    date: Oct 2, 2023
    date_iso: '2023-10-02'
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7654
    metric_stds:
    - 0.0095
  - model: CO-GNN(\mu, \mu)
    model_plain: CO-GNN(\mu, \mu)
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
    - 0.7654
    metric_stds:
    - 0.0095
  - model: GPS₃₂GAT+Performer
    model_plain: GPS₃₂GAT+Performer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: May 29, 2025
    date_iso: '2025-05-29'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7651
    metric_stds:
    - 0.0119
  - model: GPS₃₂GCN+Performer (RWSE)
    model_plain: GPS₃₂GCN+Performer (RWSE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: May 29, 2025
    date_iso: '2025-05-29'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7645
    metric_stds:
    - 0.0151
  - model: SAGE
    model_plain: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01267'
    title: Cooperative Graph Neural Networks
    date: Oct 2, 2023
    date_iso: '2023-10-02'
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7644
    metric_stds:
    - 0.0062
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01267'
    title: Cooperative Graph Neural Networks
    date: Oct 2, 2023
    date_iso: '2023-10-02'
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7609
    metric_stds:
    - 0.0127
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
    - 0.7597
    metric_stds:
    - 0.0089
  - model: GOAT
    model_plain: GOAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: May 29, 2025
    date_iso: '2025-05-29'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7576
    metric_stds:
    - 0.0166
  - model: NodeFormer
    model_plain: NodeFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7502
    metric_stds:
    - 0.0161
  - model: GBK-GNN
    model_plain: GBK-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: May 29, 2025
    date_iso: '2025-05-29'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7447
    metric_stds:
    - 0.0086
  - model: GPS₃₂GCN+Performer (DEG)
    model_plain: GPS₃₂GCN+Performer (DEG)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: May 29, 2025
    date_iso: '2025-05-29'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7424
    metric_stds:
    - 0.0118
  - model: Exphormer
    model_plain: Exphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03386'
    title: Learning Long Range Dependencies on Graphs via Random Walks
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7394
    metric_stds:
    - 0.0106
  - model: JacobiConv
    model_plain: JacobiConv
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: May 29, 2025
    date_iso: '2025-05-29'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7388
    metric_stds:
    - 0.0116
  - model: SGFormer
    model_plain: SGFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7381
    metric_stds:
    - 0.0059
  - model: GraphGPS
    model_plain: GraphGPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7256
    metric_stds:
    - 0.0133
  - model: GPS
    model_plain: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03386'
    title: Learning Long Range Dependencies on Graphs via Random Walks
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7173
    metric_stds:
    - 0.0147
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
    - 0.6969
    metric_stds:
    - 0.0146
  - model: NSD
    model_plain: NSD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.15540'
    title: Bundle Neural Networks for message diffusion on graphs
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6969
    metric_stds:
    - 0.0146
  - model: Nagphormer
    model_plain: Nagphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03386'
    title: Learning Long Range Dependencies on Graphs via Random Walks
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6817
    metric_stds:
    - 0.0153
  - model: CPGNN
    model_plain: CPGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6596
    metric_stds:
    - 0.0195
  - model: GLoGNN
    model_plain: GLoGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6574
    metric_stds:
    - 0.0119
  - model: H2GCN
    model_plain: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6359
    metric_stds:
    - 0.0146
  - model: GPRGNN
    model_plain: GPRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5548
    metric_stds:
    - 0.0091
  - model: GPR-GNN
    model_plain: GPR-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: May 29, 2025
    date_iso: '2025-05-29'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.5548
    metric_stds:
    - 0.0091
  milestones:
  - value: 0.8002
    std: 0.0086
    model: CO-GNN(Σ, Σ)
    arxiv_id: '2310.01267'
    title: Cooperative Graph Neural Networks
    date: '2023-10-02'
  - value: 0.8049
    std: 0.0092
    model: IM-CO-GNN(Σ,Σ)
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: '2025-05-29'
---

