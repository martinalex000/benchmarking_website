---
title: Reddit
slug: reddit
benchmark: Classic
task_type: node_classification
description: Reddit posts node classification (41 community labels) from the GraphSAGE
  paper.
primary_metric: F1
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.Reddit.html
stats:
  num_graphs: null
  avg_nodes: 232965.0
  avg_edges: 114615892.0
  num_classes: 41
result_count: 116
best_model:
  model: GCN (LCP-ORC)
  value: 0.8719
  metric: F1
  arxiv_id: '2502.09570'
  paper_title: Enhancing the Utility of Higher-Order Information in Relational Learning
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: F1
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - F1
  - AUC
  - AUROC
  - Accuracy
  - MRR
  rows:
  - model: GCN (LCP-ORC)
    model_plain: GCN (LCP-ORC)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.8719
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0156
    - null
    - null
    - null
    - null
  - model: GIN (HCP-ORC)
    model_plain: GIN (HCP-ORC)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.8482
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0162
    - null
    - null
    - null
    - null
  - model: GPS (EN H-19-RWPE)
    model_plain: GPS (EN H-19-RWPE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8425
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0113
    - null
    - null
    - null
    - null
  - model: GPS (LCP-ORC)
    model_plain: GPS (LCP-ORC)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8307
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0124
    - null
    - null
    - null
    - null
  - model: GPS (20-LAPE)
    model_plain: GPS (20-LAPE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8205
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0129
    - null
    - null
    - null
    - null
  - model: GPS (19-RWPE)
    model_plain: GPS (19-RWPE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8192
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0131
    - null
    - null
    - null
    - null
  - model: GPS (LCP-FRC)
    model_plain: GPS (LCP-FRC)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8168
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0116
    - null
    - null
    - null
    - null
  - model: GPS (No Encoding)
    model_plain: GPS (No Encoding)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8094
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0142
    - null
    - null
    - null
    - null
  - model: GCN (Hodge H-20-LAPE)
    model_plain: GCN (Hodge H-20-LAPE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7994
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0181
    - null
    - null
    - null
    - null
  - model: GCN (Norm. H-20-LAPE)
    model_plain: GCN (Norm. H-20-LAPE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7915
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0154
    - null
    - null
    - null
    - null
  - model: GCN (EE H-19-RWPE)
    model_plain: GCN (EE H-19-RWPE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7746
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0153
    - null
    - null
    - null
    - null
  - model: GCN (20-LAPE)
    model_plain: GCN (20-LAPE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7584
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0165
    - null
    - null
    - null
    - null
  - model: GCN (No Encoding)
    model_plain: GCN (No Encoding)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7538
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0127
    - null
    - null
    - null
    - null
  - model: GCN (19-RWPE)
    model_plain: GCN (19-RWPE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.744
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0168
    - null
    - null
    - null
    - null
  - model: GIN (HCP-FRC)
    model_plain: GIN (HCP-FRC)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7053
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0148
    - null
    - null
    - null
    - null
  - model: GCN (LCP-FRC)
    model_plain: GCN (LCP-FRC)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6966
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0162
    - null
    - null
    - null
    - null
  - model: Original Graph
    model_plain: Original Graph
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.22100'
    title: 'SHAKE-GNN: Scalable Hierarchical Kirchhoff-Forest Graph Neural Network'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.749
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
  - model: Coarsened Graph
    model_plain: Coarsened Graph
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.22100'
    title: 'SHAKE-GNN: Scalable Hierarchical Kirchhoff-Forest Graph Neural Network'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.74
    - null
    metric_stds:
    - null
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
    arxiv_id: '2406.18380'
    title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/RomanBresson/KAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.6587000000000001
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0633
    - null
  - model: BS-KAGCN
    model_plain: BS-KAGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.18380'
    title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/RomanBresson/KAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.7606
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.051
    - null
  - model: RBF-KAGCN
    model_plain: RBF-KAGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.18380'
    title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/RomanBresson/KAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.7592
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0349
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.18380'
    title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/RomanBresson/KAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.7192000000000001
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0588
    - null
  - model: BS-KAGAT
    model_plain: BS-KAGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.18380'
    title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/RomanBresson/KAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.7827
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.023700000000000002
    - null
  - model: RBF-KAGAT
    model_plain: RBF-KAGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.18380'
    title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/RomanBresson/KAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.7342
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.047599999999999996
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.18380'
    title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/RomanBresson/KAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.7478
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0382
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.02379'
    title: 'No Metric to Rule Them All: Toward Principled Evaluations of Graph-Learning
      Datasets'
    date: Feb 4, 2025
    date_iso: '2025-02-04'
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.422
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.021
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.02379'
    title: 'No Metric to Rule Them All: Toward Principled Evaluations of Graph-Learning
      Datasets'
    date: Feb 4, 2025
    date_iso: '2025-02-04'
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.472
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.017
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.02379'
    title: 'No Metric to Rule Them All: Toward Principled Evaluations of Graph-Learning
      Datasets'
    date: Feb 4, 2025
    date_iso: '2025-02-04'
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.474
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.027
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.2
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.569
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.02
    - null
  - model: GIN + rand id
    model_plain: GIN + rand id
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.57
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.021
    - null
  - model: GSN with cliques
    model_plain: GSN with cliques
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.562
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.018
    - null
  - model: SignNet-8S
    model_plain: SignNet-8S
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.552
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.029
    - null
  - model: R-method
    model_plain: R-method
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.606
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.003
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.3937
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.014
    - null
  - model: DGK
    model_plain: DGK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.3222
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.001
    - null
  - model: PNA
    model_plain: PNA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.3857
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0186
    - null
  - model: GNN (a)
    model_plain: GNN (a)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.406
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0099
    - null
  - model: AWE
    model_plain: AWE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.392
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0209
    - null
  - model: CRaWl
    model_plain: CRaWl
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.4072
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0065
    - null
  - model: AgentNet
    model_plain: AgentNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.4215
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0013
    - null
  - model: RUM
    model_plain: RUM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.4166
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0015
    - null
  - model: GMT
    model_plain: GMT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.4063
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0094
    - null
  - model: SAN
    model_plain: SAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.3992
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0102
    - null
  - model: Graphormer
    model_plain: Graphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.4142
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0042
    - null
  - model: GPS
    model_plain: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.4155
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0016
    - null
  - model: SAT
    model_plain: SAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.4214
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0007
    - null
  - model: Graph ViT
    model_plain: Graph ViT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.4017
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0052
    - null
  - model: GPM
    model_plain: GPM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.4307
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0029
    - null
  - model: --
    model_plain: --
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.86
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.01
    - null
  - model: Graclus
    model_plain: Graclus
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.03
    - null
  - model: ECPool
    model_plain: ECPool
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.91
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.02
    - null
  - model: KMIS
    model_plain: KMIS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.02
    - null
  - model: TopK
    model_plain: TopK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.77
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.02
    - null
  - model: SEP
    model_plain: SEP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.01
    - null
  - model: DiffPool
    model_plain: DiffPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.02
    - null
  - model: MinCut
    model_plain: MinCut
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.87
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.02
    - null
  - model: DMON
    model_plain: DMON
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.88
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.02
    - null
  - model: JBGNN
    model_plain: JBGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.01
    - null
  - model: Eigen
    model_plain: Eigen
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.89
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.03
    - null
  - model: HOSC
    model_plain: HOSC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.02
    - null
  - model: BNPool
    model_plain: BNPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.91
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.02
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.12059'
    title: A Scalable and Effective Alternative to Graph Transformers
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9278
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0011
    - null
  - model: SAGE
    model_plain: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.12059'
    title: A Scalable and Effective Alternative to Graph Transformers
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.965
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0003
    - null
  - model: GraphSAINT
    model_plain: GraphSAINT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.12059'
    title: A Scalable and Effective Alternative to Graph Transformers
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9558
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0007
    - null
  - model: Cluster-GCN
    model_plain: Cluster-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.12059'
    title: A Scalable and Effective Alternative to Graph Transformers
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.957
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0006
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.12059'
    title: A Scalable and Effective Alternative to Graph Transformers
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.965
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0011
    - null
  - model: Graphormer-SAMPLE
    model_plain: Graphormer-SAMPLE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.12059'
    title: A Scalable and Effective Alternative to Graph Transformers
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9305
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0022
    - null
  - model: SAT-SAMPLE
    model_plain: SAT-SAMPLE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.12059'
    title: A Scalable and Effective Alternative to Graph Transformers
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9337
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0032
    - null
  - model: ANS-GT
    model_plain: ANS-GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.12059'
    title: A Scalable and Effective Alternative to Graph Transformers
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.953
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0081
    - null
  - model: Exphormer
    model_plain: Exphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.12059'
    title: A Scalable and Effective Alternative to Graph Transformers
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.959
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0015
    - null
  - model: GECO
    model_plain: GECO
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.12059'
    title: A Scalable and Effective Alternative to Graph Transformers
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9665
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0005
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
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9751
    - null
    - null
    - null
    metric_stds:
    - null
    - 0.001
    - null
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
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9634
    - null
    - null
    - null
    metric_stds:
    - null
    - 0.0083
    - null
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
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9818
    - null
    - null
    - null
    metric_stds:
    - null
    - 0.0005
    - null
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
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9823
    - null
    - null
    - null
    metric_stds:
    - null
    - 0.001
    - null
    - null
    - null
  - model: Our
    model_plain: Our
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_iso: '2024-06-04'
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9861
    - null
    - null
    - null
    metric_stds:
    - null
    - 0.0004
    - null
    - null
    - null
  - model: EdgeBank
    model_plain: EdgeBank
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_iso: '2024-06-04'
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9642
    - null
    - null
    - null
    metric_stds:
    - null
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
    arxiv_id: '2403.16030'
    title: 'VCR-Graphormer: A Mini-batch Graph Transformer via Virtual Connections'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9038
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0011
    - null
  - model: GraphSAINT
    model_plain: GraphSAINT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16030'
    title: 'VCR-Graphormer: A Mini-batch Graph Transformer via Virtual Connections'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9235
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0008
    - null
  - model: GRAND
    model_plain: GRAND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16030'
    title: 'VCR-Graphormer: A Mini-batch Graph Transformer via Virtual Connections'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9281
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0003
    - null
  - model: Nagphormer
    model_plain: Nagphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16030'
    title: 'VCR-Graphormer: A Mini-batch Graph Transformer via Virtual Connections'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9358
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0005
    - null
  - model: VCR-Graphormer
    model_plain: VCR-Graphormer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16030'
    title: 'VCR-Graphormer: A Mini-batch Graph Transformer via Virtual Connections'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9369
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0008
    - null
  - model: CARIBOU (EDP)
    model_plain: CARIBOU (EDP)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.22727'
    title: Convergent Privacy Framework for Multi-layer GNNs through Contractive Message
      Passing
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.637
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
  - model: TGTalker (Qwen3-1.7B)
    model_plain: TGTalker (Qwen3-1.7B)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.05393'
    title: Are Large Language Models Good Temporal Graph Learners?
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.617
    metric_stds:
    - null
    - null
    - null
    - null
    - null
  - model: TGTalker (Mistral-7B-v0.3)
    model_plain: TGTalker (Mistral-7B-v0.3)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.05393'
    title: Are Large Language Models Good Temporal Graph Learners?
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.612
    metric_stds:
    - null
    - null
    - null
    - null
    - null
  - model: TGTalker (Llama3-8B)
    model_plain: TGTalker (Llama3-8B)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.05393'
    title: Are Large Language Models Good Temporal Graph Learners?
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.613
    metric_stds:
    - null
    - null
    - null
    - null
    - null
  - model: TGTalker (GPT-4.1-mini)
    model_plain: TGTalker (GPT-4.1-mini)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.05393'
    title: Are Large Language Models Good Temporal Graph Learners?
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.225
    metric_stds:
    - null
    - null
    - null
    - null
    - null
  - model: TGN
    model_plain: TGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.05393'
    title: Are Large Language Models Good Temporal Graph Learners?
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.499
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.011
  - model: TNCN
    model_plain: TNCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.05393'
    title: Are Large Language Models Good Temporal Graph Learners?
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.696
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.02
  - model: GraphMixer
    model_plain: GraphMixer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.05393'
    title: Are Large Language Models Good Temporal Graph Learners?
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.136
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.078
  - model: EdgeBank
    model_plain: EdgeBank
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.05393'
    title: Are Large Language Models Good Temporal Graph Learners?
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.485
    metric_stds:
    - null
    - null
    - null
    - null
    - null
  - model: HTGN
    model_plain: HTGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.05393'
    title: Are Large Language Models Good Temporal Graph Learners?
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.533
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.007
  - model: GCLSTM
    model_plain: GCLSTM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.05393'
    title: Are Large Language Models Good Temporal Graph Learners?
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.467
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.004
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.05393'
    title: Are Large Language Models Good Temporal Graph Learners?
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.242
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.005
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05697'
    title: 'Diffusing to the Top: Boost Graph Neural Networks with Minimal Hyperparameter
      Tuning'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9101
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0009
    - null
  - model: SAGE
    model_plain: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05697'
    title: 'Diffusing to the Top: Boost Graph Neural Networks with Minimal Hyperparameter
      Tuning'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9326
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0002
    - null
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05697'
    title: 'Diffusing to the Top: Boost Graph Neural Networks with Minimal Hyperparameter
      Tuning'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.8794
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0007
    - null
  - model: GNNDiff
    model_plain: GNNDiff
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05697'
    title: 'Diffusing to the Top: Boost Graph Neural Networks with Minimal Hyperparameter
      Tuning'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9115
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0004
    - null
  - model: Grid Search
    model_plain: Grid Search
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05697'
    title: 'Diffusing to the Top: Boost Graph Neural Networks with Minimal Hyperparameter
      Tuning'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9101
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0009
    - null
  - model: Random Search
    model_plain: Random Search
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05697'
    title: 'Diffusing to the Top: Boost Graph Neural Networks with Minimal Hyperparameter
      Tuning'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9107
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0005
    - null
  - model: Coarse Search
    model_plain: Coarse Search
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05697'
    title: 'Diffusing to the Top: Boost Graph Neural Networks with Minimal Hyperparameter
      Tuning'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9112
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0007
    - null
  - model: C2F
    model_plain: C2F
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05697'
    title: 'Diffusing to the Top: Boost Graph Neural Networks with Minimal Hyperparameter
      Tuning'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9112
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0007
    - null
  - model: DGCNN
    model_plain: DGCNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: Jun 9, 2023
    date_iso: '2023-06-09'
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.766
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.045
    - null
  - model: DiffPool
    model_plain: DiffPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: Jun 9, 2023
    date_iso: '2023-06-09'
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.75
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.043
    - null
  - model: ECC
    model_plain: ECC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: Jun 9, 2023
    date_iso: '2023-06-09'
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.726
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.041
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: Jun 9, 2023
    date_iso: '2023-06-09'
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.753
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.029
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: Jun 9, 2023
    date_iso: '2023-06-09'
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.729
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.02
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: Jun 9, 2023
    date_iso: '2023-06-09'
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.739
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.034
    - null
  - model: SPN (K=1)
    model_plain: SPN (K=1)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: Jun 9, 2023
    date_iso: '2023-06-09'
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.727
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.026
    - null
  - model: SPN(k=5)
    model_plain: SPN(k=5)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: Jun 9, 2023
    date_iso: '2023-06-09'
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.774
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.038
    - null
  - model: Nested-GNN
    model_plain: Nested-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: Jun 9, 2023
    date_iso: '2023-06-09'
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.778
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.039
    - null
  - model: PathNN-P (K=1)
    model_plain: PathNN-P (K=1)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: Jun 9, 2023
    date_iso: '2023-06-09'
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.769
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.037
    - null
  - model: PathNN-SP (K=2)
    model_plain: PathNN-SP (K=2)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: Jun 9, 2023
    date_iso: '2023-06-09'
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.765
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.046
    - null
  - model: PathNN-AP (K=2)
    model_plain: PathNN-AP (K=2)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: Jun 9, 2023
    date_iso: '2023-06-09'
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.75
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.044
    - null
  - model: S² GCN
    model_plain: S² GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.22100'
    title: 'SHAKE-GNN: Scalable Hierarchical Kirchhoff-Forest Graph Neural Network'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.749
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
  milestones:
  - value: 0.8719
    std: 0.0156
    model: GCN (LCP-ORC)
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: 2025-02
---

