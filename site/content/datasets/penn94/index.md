---
title: Penn94
slug: penn94
benchmark: LINKX Benchmarks
task_type: node_classification
description: Facebook100 Penn94 social network node classification (binary gender).
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.LINKXDataset.html
stats:
  num_graphs: 1
  avg_nodes: 41554.0
  avg_edges: 1362229.0
  num_classes: 2
result_count: 39
best_model:
  model: CSNN
  value: 0.86
  metric: Accuracy
  arxiv_id: '2507.00647'
  paper_title: Cooperative Sheaf Neural Networks
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
  - MRR
  rows:
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
    is_best: true
    metric_values:
    - 0.86
    - null
    metric_stds:
    - 0.0039
    - null
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8557
    - null
    metric_stds:
    - null
    - null
  - model: AdaptKry
    model_plain: AdaptKry
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.07954'
    title: 'Optimizing Polynomial Graph Filters: A Novel Adaptive Krylov Subspace
      Approach'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/kkhuang81/AdaptKry
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8497
    - null
    metric_stds:
    - 0.0036
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
    - 0.8494
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
    arxiv_id: '2403.07954'
    title: 'Optimizing Polynomial Graph Filters: A Novel Adaptive Krylov Subspace
      Approach'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/kkhuang81/AdaptKry
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8486
    - null
    metric_stds:
    - 0.0033
    - null
  - model: OptBasisGNN
    model_plain: OptBasisGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.07954'
    title: 'Optimizing Polynomial Graph Filters: A Novel Adaptive Krylov Subspace
      Approach'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/kkhuang81/AdaptKry
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8485
    - null
    metric_stds:
    - 0.0039
    - null
  - model: LINKX
    model_plain: LINKX
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
    - 0.8471
    - null
    metric_stds:
    - 0.0052
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
    - 0.8456
    - null
    metric_stds:
    - 0.001
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
    - 0.8409
    - null
    metric_stds:
    - 0.002
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
    - 0.8408
    - null
    metric_stds:
    - 0.002
    - null
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
    - 0.837
    - null
    metric_stds:
    - 0.0038
    - null
  - model: GPR-GNN
    model_plain: GPR-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.07954'
    title: 'Optimizing Polynomial Graph Filters: A Novel Adaptive Krylov Subspace
      Approach'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/kkhuang81/AdaptKry
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8354
    - null
    metric_stds:
    - 0.0032
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
    - 0.8352
    - null
    metric_stds:
    - 0.002
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
    - 0.8328
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
    arxiv_id: '2310.10064'
    title: arXiv:2310.10064
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/junjie-xu/NewtonNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8323
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
    arxiv_id: '2310.10064'
    title: arXiv:2310.10064
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/junjie-xu/NewtonNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8304
    - null
    metric_stds:
    - 0.001
    - null
  - model: GCNII
    model_plain: GCNII
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
    - 0.8292
    - null
    metric_stds:
    - 0.0059
    - null
  - model: ACMGCN
    model_plain: ACMGCN
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
    - 0.8252
    - null
    metric_stds:
    - 0.0096
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.07954'
    title: 'Optimizing Polynomial Graph Filters: A Novel Adaptive Krylov Subspace
      Approach'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/kkhuang81/AdaptKry
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8247
    - null
    metric_stds:
    - 0.0027
    - null
  - model: MLP for adjacency matrix only
    model_plain: MLP for adjacency matrix only
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8225
    - null
    metric_stds:
    - null
    - null
  - model: SIGN
    model_plain: SIGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.07954'
    title: 'Optimizing Polynomial Graph Filters: A Novel Adaptive Krylov Subspace
      Approach'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/kkhuang81/AdaptKry
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8213
    - null
    metric_stds:
    - 0.0028
    - null
  - model: GAT
    model_plain: GAT
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
    - 0.8153
    - null
    metric_stds:
    - 0.0055
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.07954'
    title: 'Optimizing Polynomial Graph Filters: A Novel Adaptive Krylov Subspace
      Approach'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/kkhuang81/AdaptKry
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8144
    - null
    metric_stds:
    - 0.0015
    - null
  - model: GPR-GNN
    model_plain: GPR-GNN
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
    - 0.8138
    - null
    metric_stds:
    - 0.0016
    - null
  - model: H2GCN
    model_plain: H2GCN
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
    - 0.8131
    - null
    metric_stds:
    - 0.006
    - null
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
    - 0.813
    - null
    metric_stds:
    - 0.0073
    - null
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
    - 0.811
    - null
    metric_stds:
    - 0.0055
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
    - 0.7591
    - null
    metric_stds:
    - 0.002
    - null
  - model: WRGAT
    model_plain: WRGAT
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
    - 0.7432
    - null
    metric_stds:
    - 0.0053
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
    - 0.7418
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
    arxiv_id: '2106.06218'
    title: 'Graph Transformer Networks: Learning Meta-path Graphs to Improve GNNs'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/seongjunyun/Graph_Transformer_Networks
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.1203
    metric_stds:
    - null
    - 0.002
  - model: Node2Vec
    model_plain: Node2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.06218'
    title: 'Graph Transformer Networks: Learning Meta-path Graphs to Improve GNNs'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/seongjunyun/Graph_Transformer_Networks
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.1127
    metric_stds:
    - null
    - 0.007
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.06218'
    title: 'Graph Transformer Networks: Learning Meta-path Graphs to Improve GNNs'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/seongjunyun/Graph_Transformer_Networks
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.1589
    metric_stds:
    - null
    - 0.003
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.06218'
    title: 'Graph Transformer Networks: Learning Meta-path Graphs to Improve GNNs'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/seongjunyun/Graph_Transformer_Networks
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.1403
    metric_stds:
    - null
    - 0.009
  - model: RGCN
    model_plain: RGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.06218'
    title: 'Graph Transformer Networks: Learning Meta-path Graphs to Improve GNNs'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/seongjunyun/Graph_Transformer_Networks
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.1476
    metric_stds:
    - null
    - 0.007
  - model: HGT
    model_plain: HGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.06218'
    title: 'Graph Transformer Networks: Learning Meta-path Graphs to Improve GNNs'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/seongjunyun/Graph_Transformer_Networks
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.137
    metric_stds:
    - null
    - 0.014
  - model: GTN_-I
    model_plain: GTN_-I
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.06218'
    title: 'Graph Transformer Networks: Learning Meta-path Graphs to Improve GNNs'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/seongjunyun/Graph_Transformer_Networks
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.1633
    metric_stds:
    - null
    - 0.003
  - model: GTN
    model_plain: GTN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.06218'
    title: 'Graph Transformer Networks: Learning Meta-path Graphs to Improve GNNs'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/seongjunyun/Graph_Transformer_Networks
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.1649
    metric_stds:
    - null
    - 0.008
  - model: Fast-GTN
    model_plain: Fast-GTN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.06218'
    title: 'Graph Transformer Networks: Learning Meta-path Graphs to Improve GNNs'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/seongjunyun/Graph_Transformer_Networks
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.1672
    metric_stds:
    - null
    - 0.006
  milestones:
  - value: 0.8557
    std: null
    model: GloGNN
    arxiv_id: '2205.07308'
    title: Finding Global Homophily in Graph Neural Networks When Meeting Heterophily
    date: '2022-05-15'
  - value: 0.86
    std: 0.0039
    model: CSNN
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: 2025-07
---

