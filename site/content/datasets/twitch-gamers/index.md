---
title: twitch-gamers
slug: twitch-gamers
benchmark: LINKX Benchmarks
task_type: node_classification
description: Twitch streamer network binary node classification (streaming language).
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.LINKXDataset.html
stats:
  num_graphs: 1
  avg_nodes: 168114.0
  avg_edges: 6797557.0
  num_classes: 2
result_count: 49
best_model:
  model: GloGNN
  value: 0.986
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
  - ROC-AUC
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
    - 0.986
    - null
    metric_stds:
    - 0.001
    - null
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
    - 0.983
    - null
    metric_stds:
    - 0.001
    - null
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
    - 0.982
    - null
    metric_stds:
    - 0.002
    - null
  - model: APPNP
    model_plain: APPNP
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
    - 0.981
    - null
    metric_stds:
    - 0.002
    - null
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
    - 0.98
    - null
    metric_stds:
    - 0.002
    - null
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
    - 0.979
    - null
    metric_stds:
    - 0.002
    - null
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
    - 0.978
    - null
    metric_stds:
    - 0.002
    - null
  - model: ChebNet
    model_plain: ChebNet
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
    - 0.975
    - null
    metric_stds:
    - 0.003
    - null
  - model: MLP
    model_plain: MLP
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
    - 0.965
    - null
    metric_stds:
    - 0.003
    - null
  - model: NewtonNet
    model_plain: NewtonNet
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.10064'
    title: arXiv:2310.10064
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/junjie-xu/NewtonNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6792
    - null
    metric_stds:
    - 0.003
    - null
  - model: JacobiConv
    model_plain: JacobiConv
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.10064'
    title: arXiv:2310.10064
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/junjie-xu/NewtonNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6768
    - null
    metric_stds:
    - 0.002
    - null
  - model: GloGNN
    model_plain: GloGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.10064'
    title: arXiv:2310.10064
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/junjie-xu/NewtonNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.675
    - null
    metric_stds:
    - 0.003
    - null
  - model: MixHop
    model_plain: MixHop
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.10064'
    title: arXiv:2310.10064
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/junjie-xu/NewtonNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6727
    - null
    metric_stds:
    - 0.002
    - null
  - model: OptBasis
    model_plain: OptBasis
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.15354'
    title: 'Polynomial Selection in Spectral Graph Neural Networks: An Error-Sum of
      Function Slices Approach'
    date: Apr 2024
    date_iso: 2024-04
    date_display: Apr 2024
    codebase_url: https://github.com/vasile-paskardlgm/TFGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6681
    - null
    metric_stds:
    - 0.004
    - null
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.10064'
    title: arXiv:2310.10064
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/junjie-xu/NewtonNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6676
    - null
    metric_stds:
    - 0.002
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.10064'
    title: arXiv:2310.10064
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/junjie-xu/NewtonNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6658
    - null
    metric_stds:
    - 0.002
    - null
  - model: ChebNet
    model_plain: ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.15354'
    title: 'Polynomial Selection in Spectral Graph Neural Networks: An Error-Sum of
      Function Slices Approach'
    date: Apr 2024
    date_iso: 2024-04
    date_display: Apr 2024
    codebase_url: https://github.com/vasile-paskardlgm/TFGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6644
    - null
    metric_stds:
    - 0.005
    - null
  - model: GloGNN
    model_plain: GloGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.20724'
    title: on Large Graphs using Intersecting Communities
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: https://github.com/benfinkelshtein/ICGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6634
    - null
    metric_stds:
    - 0.0029
    - null
  - model: LRGNN
    model_plain: LRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.15354'
    title: 'Polynomial Selection in Spectral Graph Neural Networks: An Error-Sum of
      Function Slices Approach'
    date: Apr 2024
    date_iso: 2024-04
    date_display: Apr 2024
    codebase_url: https://github.com/vasile-paskardlgm/TFGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6629
    - null
    metric_stds:
    - 0.005
    - null
  - model: GPRGNN
    model_plain: GPRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.15354'
    title: 'Polynomial Selection in Spectral Graph Neural Networks: An Error-Sum of
      Function Slices Approach'
    date: Apr 2024
    date_iso: 2024-04
    date_display: Apr 2024
    codebase_url: https://github.com/vasile-paskardlgm/TFGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6623
    - null
    metric_stds:
    - 0.001
    - null
  - model: OrderedGNN
    model_plain: OrderedGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.15354'
    title: 'Polynomial Selection in Spectral Graph Neural Networks: An Error-Sum of
      Function Slices Approach'
    date: Apr 2024
    date_iso: 2024-04
    date_display: Apr 2024
    codebase_url: https://github.com/vasile-paskardlgm/TFGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6609
    - null
    metric_stds:
    - 0.003
    - null
  - model: ICG_u-NN
    model_plain: ICG_u-NN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.20724'
    title: on Large Graphs using Intersecting Communities
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: https://github.com/benfinkelshtein/ICGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6608
    - null
    metric_stds:
    - 0.0074
    - null
  - model: LINKX
    model_plain: LINKX
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.15354'
    title: 'Polynomial Selection in Spectral Graph Neural Networks: An Error-Sum of
      Function Slices Approach'
    date: Apr 2024
    date_iso: 2024-04
    date_display: Apr 2024
    codebase_url: https://github.com/vasile-paskardlgm/TFGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6582
    - null
    metric_stds:
    - 0.004
    - null
  - model: SpecFormer
    model_plain: SpecFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.15354'
    title: 'Polynomial Selection in Spectral Graph Neural Networks: An Error-Sum of
      Function Slices Approach'
    date: Apr 2024
    date_iso: 2024-04
    date_display: Apr 2024
    codebase_url: https://github.com/vasile-paskardlgm/TFGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.658
    - null
    metric_stds:
    - 0.002
    - null
  - model: BernNet
    model_plain: BernNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.15354'
    title: 'Polynomial Selection in Spectral Graph Neural Networks: An Error-Sum of
      Function Slices Approach'
    date: Apr 2024
    date_iso: 2024-04
    date_display: Apr 2024
    codebase_url: https://github.com/vasile-paskardlgm/TFGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6574
    - null
    metric_stds:
    - 0.003
    - null
  - model: GloGNN
    model_plain: GloGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.15354'
    title: 'Polynomial Selection in Spectral Graph Neural Networks: An Error-Sum of
      Function Slices Approach'
    date: Apr 2024
    date_iso: 2024-04
    date_display: Apr 2024
    codebase_url: https://github.com/vasile-paskardlgm/TFGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6562
    - null
    metric_stds:
    - 0.003
    - null
  - model: ICG-NN
    model_plain: ICG-NN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.20724'
    title: on Large Graphs using Intersecting Communities
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: https://github.com/benfinkelshtein/ICGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6527
    - null
    metric_stds:
    - 0.0082
    - null
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.10064'
    title: arXiv:2310.10064
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/junjie-xu/NewtonNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6524
    - null
    metric_stds:
    - 0.002
    - null
  - model: GCNII
    model_plain: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.15354'
    title: 'Polynomial Selection in Spectral Graph Neural Networks: An Error-Sum of
      Function Slices Approach'
    date: Apr 2024
    date_iso: 2024-04
    date_display: Apr 2024
    codebase_url: https://github.com/vasile-paskardlgm/TFGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6511
    - null
    metric_stds:
    - 0.003
    - null
  - model: ACMGCN
    model_plain: ACMGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.15354'
    title: 'Polynomial Selection in Spectral Graph Neural Networks: An Error-Sum of
      Function Slices Approach'
    date: Apr 2024
    date_iso: 2024-04
    date_display: Apr 2024
    codebase_url: https://github.com/vasile-paskardlgm/TFGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6473
    - null
    metric_stds:
    - 0.003
    - null
  - model: H2GCN
    model_plain: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.15354'
    title: 'Polynomial Selection in Spectral Graph Neural Networks: An Error-Sum of
      Function Slices Approach'
    date: Apr 2024
    date_iso: 2024-04
    date_display: Apr 2024
    codebase_url: https://github.com/vasile-paskardlgm/TFGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6471
    - null
    metric_stds:
    - 0.004
    - null
  - model: GPRGNN
    model_plain: GPRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.10064'
    title: arXiv:2310.10064
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/junjie-xu/NewtonNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6444
    - null
    metric_stds:
    - 0.003
    - null
  - model: JacobiConv
    model_plain: JacobiConv
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.15354'
    title: 'Polynomial Selection in Spectral Graph Neural Networks: An Error-Sum of
      Function Slices Approach'
    date: Apr 2024
    date_iso: 2024-04
    date_display: Apr 2024
    codebase_url: https://github.com/vasile-paskardlgm/TFGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6417
    - null
    metric_stds:
    - 0.003
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.15354'
    title: 'Polynomial Selection in Spectral Graph Neural Networks: An Error-Sum of
      Function Slices Approach'
    date: Apr 2024
    date_iso: 2024-04
    date_display: Apr 2024
    codebase_url: https://github.com/vasile-paskardlgm/TFGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6329
    - null
    metric_stds:
    - 0.005
    - null
  - model: BernNet
    model_plain: BernNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.10064'
    title: arXiv:2310.10064
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/junjie-xu/NewtonNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.629
    - null
    metric_stds:
    - 0.002
    - null
  - model: ChebNet
    model_plain: ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.10064'
    title: arXiv:2310.10064
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/junjie-xu/NewtonNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6253
    - null
    metric_stds:
    - 0.002
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.20724'
    title: on Large Graphs using Intersecting Communities
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: https://github.com/benfinkelshtein/ICGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6218
    - null
    metric_stds:
    - 0.0026
    - null
  - model: GPR-GNN
    model_plain: GPR-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.20724'
    title: on Large Graphs using Intersecting Communities
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: https://github.com/benfinkelshtein/ICGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6189
    - null
    metric_stds:
    - 0.0029
    - null
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.20724'
    title: on Large Graphs using Intersecting Communities
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: https://github.com/benfinkelshtein/ICGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6092
    - null
    metric_stds:
    - 0.0007
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.20724'
    title: on Large Graphs using Intersecting Communities
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: https://github.com/benfinkelshtein/ICGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5989
    - null
    metric_stds:
    - 0.0412
    - null
  - model: ERM
    model_plain: ERM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.07968'
    title: Generative Risk Minimization for Out-of-Distribution Generalization on
      Graphs
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/SongW-SW/GRM
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.497
    metric_stds:
    - null
    - 0.011
  - model: DCRNN
    model_plain: DCRNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.07968'
    title: Generative Risk Minimization for Out-of-Distribution Generalization on
      Graphs
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/SongW-SW/GRM
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.44
    metric_stds:
    - null
    - 0.005
  - model: MMD
    model_plain: MMD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.07968'
    title: Generative Risk Minimization for Out-of-Distribution Generalization on
      Graphs
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/SongW-SW/GRM
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.428
    metric_stds:
    - null
    - 0.006
  - model: ARM
    model_plain: ARM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.07968'
    title: Generative Risk Minimization for Out-of-Distribution Generalization on
      Graphs
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/SongW-SW/GRM
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.432
    metric_stds:
    - null
    - 0.015
  - model: EERM
    model_plain: EERM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.07968'
    title: Generative Risk Minimization for Out-of-Distribution Generalization on
      Graphs
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/SongW-SW/GRM
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.516
    metric_stds:
    - null
    - 0.008
  - model: LiSA
    model_plain: LiSA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.07968'
    title: Generative Risk Minimization for Out-of-Distribution Generalization on
      Graphs
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/SongW-SW/GRM
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.486
    metric_stds:
    - null
    - 0.012
  - model: IS-GIB
    model_plain: IS-GIB
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.07968'
    title: Generative Risk Minimization for Out-of-Distribution Generalization on
      Graphs
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/SongW-SW/GRM
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.512
    metric_stds:
    - null
    - 0.019
  - model: MARIO
    model_plain: MARIO
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.07968'
    title: Generative Risk Minimization for Out-of-Distribution Generalization on
      Graphs
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/SongW-SW/GRM
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.507
    metric_stds:
    - null
    - 0.02
  - model: GRM
    model_plain: GRM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.07968'
    title: Generative Risk Minimization for Out-of-Distribution Generalization on
      Graphs
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/SongW-SW/GRM
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.525
    metric_stds:
    - null
    - 0.017
  milestones:
  - value: 0.986
    std: 0.001
    model: GloGNN
    arxiv_id: '2205.07308'
    title: Finding Global Homophily in Graph Neural Networks When Meeting Heterophily
    date: '2022-05-15'
---

