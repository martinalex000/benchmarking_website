---
title: snap-patents
slug: snap-patents
benchmark: LINKX Benchmarks
task_type: node_classification
description: USPTO patent citation graph node classification (5 time-based classes).
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.LINKXDataset.html
stats:
  num_graphs: 1
  avg_nodes: 2745480.0
  avg_edges: 12800500.0
  num_classes: 5
result_count: 33
best_model:
  model: GloGNN
  value: 0.912
  metric: Accuracy
  arxiv_id: '2205.07308'
  paper_title: Finding Global Homophily in Graph Neural Networks When Meeting Heterophily
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
  - model: GloGNN
    model_plain: GloGNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.07308'
    title: Finding Global Homophily in Graph Neural Networks When Meeting Heterophily
    date: May 15, 2022
    date_iso: '2022-05-15'
    date_display: May 2022
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.912
    metric_stds:
    - 0.002
  - model: DGN
    model_plain: DGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.07308'
    title: Finding Global Homophily in Graph Neural Networks When Meeting Heterophily
    date: May 15, 2022
    date_iso: '2022-05-15'
    date_display: May 2022
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.908
    metric_stds:
    - 0.002
  - model: PNA
    model_plain: PNA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.07308'
    title: Finding Global Homophily in Graph Neural Networks When Meeting Heterophily
    date: May 15, 2022
    date_iso: '2022-05-15'
    date_display: May 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.905
    metric_stds:
    - 0.003
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.07308'
    title: Finding Global Homophily in Graph Neural Networks When Meeting Heterophily
    date: May 15, 2022
    date_iso: '2022-05-15'
    date_display: May 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.901
    metric_stds:
    - 0.004
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.07308'
    title: Finding Global Homophily in Graph Neural Networks When Meeting Heterophily
    date: May 15, 2022
    date_iso: '2022-05-15'
    date_display: May 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.898
    metric_stds:
    - 0.002
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.07308'
    title: Finding Global Homophily in Graph Neural Networks When Meeting Heterophily
    date: May 15, 2022
    date_iso: '2022-05-15'
    date_display: May 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.895
    metric_stds:
    - 0.003
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.07308'
    title: Finding Global Homophily in Graph Neural Networks When Meeting Heterophily
    date: May 15, 2022
    date_iso: '2022-05-15'
    date_display: May 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.892
    metric_stds:
    - 0.005
  - model: Dir-GNN
    model_plain: Dir-GNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.10498'
    title: Edge Directionality Improves Learning on Heterophilic Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/emalgorithm/directed-graph-neural-network
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7395
    metric_stds:
    - 0.0005
  - model: FL
    model_plain: FL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.13009'
    title: My Publication Title --- Single Author
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: https://github.com/yuetan031/FedStar
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7216
    metric_stds:
    - 0.0243
  - model: GCFL
    model_plain: GCFL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.13009'
    title: My Publication Title --- Single Author
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: https://github.com/yuetan031/FedStar
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7065
    metric_stds:
    - 0.0184
  - model: FedSage
    model_plain: FedSage
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.13009'
    title: My Publication Title --- Single Author
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: https://github.com/yuetan031/FedStar
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6955
    metric_stds:
    - 0.0215
  - model: Gradient Gating
    model_plain: Gradient Gating
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.10498'
    title: Edge Directionality Improves Learning on Heterophilic Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/emalgorithm/directed-graph-neural-network
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.695
    metric_stds:
    - 0.0039
  - model: Local
    model_plain: Local
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.13009'
    title: My Publication Title --- Single Author
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: https://github.com/yuetan031/FedStar
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6937
    metric_stds:
    - 0.0305
  - model: FedPer
    model_plain: FedPer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.13009'
    title: My Publication Title --- Single Author
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: https://github.com/yuetan031/FedStar
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6937
    metric_stds:
    - 0.0292
  - model: FedProx
    model_plain: FedProx
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.13009'
    title: My Publication Title --- Single Author
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: https://github.com/yuetan031/FedStar
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6921
    metric_stds:
    - 0.0263
  - model: FedAvg
    model_plain: FedAvg
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.13009'
    title: My Publication Title --- Single Author
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: https://github.com/yuetan031/FedStar
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6892
    metric_stds:
    - 0.0212
  - model: FSGNN
    model_plain: FSGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.10498'
    title: Edge Directionality Improves Learning on Heterophilic Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/emalgorithm/directed-graph-neural-network
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6507
    metric_stds:
    - 0.0003
  - model: GloGNN
    model_plain: GloGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.10498'
    title: Edge Directionality Improves Learning on Heterophilic Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/emalgorithm/directed-graph-neural-network
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6209
    metric_stds:
    - 0.0027
  - model: LINKX
    model_plain: LINKX
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.10498'
    title: Edge Directionality Improves Learning on Heterophilic Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/emalgorithm/directed-graph-neural-network
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6195
    metric_stds:
    - 0.0012
  - model: GraphSAGE-SVD
    model_plain: GraphSAGE-SVD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.07767'
    title: How does Heterophily Impact the Robustness of Graph Neural Networks? Theoretical
      Connections and Practical Implications
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/jianhao2016/GPRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6
    metric_stds:
    - 0.0136
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
    - 0.552
    metric_stds:
    - 0.0055
  - model: ACMGCN
    model_plain: ACMGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.10498'
    title: Edge Directionality Improves Learning on Heterophilic Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/emalgorithm/directed-graph-neural-network
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5514
    metric_stds:
    - 0.0016
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.10498'
    title: Edge Directionality Improves Learning on Heterophilic Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/emalgorithm/directed-graph-neural-network
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5102
    metric_stds:
    - 0.0006
  - model: GCNII
    model_plain: GCNII
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
    - 0.475
    metric_stds:
    - 0.006
  - model: H2GCN-SMGDC
    model_plain: H2GCN-SMGDC
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.07767'
    title: How does Heterophily Impact the Robustness of Graph Neural Networks? Theoretical
      Connections and Practical Implications
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/jianhao2016/GPRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4722
    metric_stds:
    - 0.0157
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
    - 0.452
    metric_stds:
    - 0.0047
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
    - 0.439
    metric_stds:
    - 0.0042
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
    - 0.417
    metric_stds:
    - 0.0034
  - model: GPR-GNN
    model_plain: GPR-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.10498'
    title: Edge Directionality Improves Learning on Heterophilic Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/emalgorithm/directed-graph-neural-network
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4019
    metric_stds:
    - 0.0003
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
    - 0.3442
    metric_stds:
    - null
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
    - 0.315
    metric_stds:
    - null
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.10498'
    title: Edge Directionality Improves Learning on Heterophilic Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/emalgorithm/directed-graph-neural-network
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3134
    metric_stds:
    - 0.0005
  - model: GCN-SVD
    model_plain: GCN-SVD
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.07767'
    title: How does Heterophily Impact the Robustness of Graph Neural Networks? Theoretical
      Connections and Practical Implications
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/jianhao2016/GPRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2889
    metric_stds:
    - 0.0342
  milestones:
  - value: 0.6
    std: 0.0136
    model: GraphSAGE-SVD
    arxiv_id: '2106.07767'
    title: How does Heterophily Impact the Robustness of Graph Neural Networks? Theoretical
      Connections and Practical Implications
    date: 2021-06
  - value: 0.912
    std: 0.002
    model: GloGNN
    arxiv_id: '2205.07308'
    title: Finding Global Homophily in Graph Neural Networks When Meeting Heterophily
    date: '2022-05-15'
---

