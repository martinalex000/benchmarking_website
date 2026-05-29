---
title: CiteSeer
slug: citeseer
benchmark: Classic
task_type: node_classification
description: Citation network node classification (6 classes).
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.Planetoid.html
stats:
  num_graphs: null
  avg_nodes: null
  avg_edges: null
  num_classes: 6
result_count: 1149
best_model:
  model: S-VAE/VGAE
  value: 0.952
  metric: Accuracy
  arxiv_id: '2407.09468'
  paper_title: 'Beyond Euclid: An Illustrated Guide to Modern Machine Learning with
    Geometric, Topological, and Algebraic Structures'
variants:
- slug: planetoid-split
  name: Planetoid split
  notes: Yang et al. 2016 fixed split.
  is_standard: true
  primary_metric: Accuracy
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - Accuracy
  - AP
  - ARI
  - AUC
  - AUC-ROC
  - AUROC
  - F1
  - NMI
  rows:
  - model: S-VAE/VGAE
    model_plain: S-VAE/VGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.09468'
    title: 'Beyond Euclid: An Illustrated Guide to Modern Machine Learning with Geometric,
      Topological, and Algebraic Structures'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.952
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Policy-GNN
    model_plain: Policy-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15097'
    title: 'Policy-GNN: Aggregation Optimization for Graph Neural Networks'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.897
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.021
    - null
    - null
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
    arxiv_id: '1805.07984'
    title: Adversarial Attacks on Neural Networks for Graph Data
    date: May 2018
    date_iso: 2018-05
    date_display: May 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.88
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.8378
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0038
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TRIGON
    model_plain: TRIGON
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8285
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0038
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.09078'
    title: 'Probing GNN Explainers: A Rigorous Theoretical and Empirical Analysis
      of GNN Explanation Methods'
    date: Jun 16, 2021
    date_iso: '2021-06-16'
    date_display: Jun 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8269
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TransformerConv
    model_plain: TransformerConv
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17676'
    title: Instance-Aware Graph Prompt Learning
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8266
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0036
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17676'
    title: Instance-Aware Graph Prompt Learning
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8227
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0068
    - null
    - null
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
    arxiv_id: '2411.17676'
    title: Instance-Aware Graph Prompt Learning
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8211
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0102
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Linear Probing
    model_plain: Linear Probing
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17676'
    title: Instance-Aware Graph Prompt Learning
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8205
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: IDEA
    model_plain: IDEA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15792'
    title: 'IDEA: Invariant Defense for Graph Adversarial Robustness'
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.82
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.019
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphEdit
    model_plain: GraphEdit
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15183'
    title: 'GraphEdit: Large Language Models for Graph Structure Learning'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/HKUDS/GraphEdit
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8185
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: IA-GPL
    model_plain: IA-GPL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17676'
    title: Instance-Aware Graph Prompt Learning
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8133
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: DR
    model_plain: DR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8114
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0034
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: novel graph MLP mixer
    model_plain: novel graph MLP mixer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16358'
    title: 'ChebMixer: Efficient Graph Representation Learning with MLP Mixer'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8104
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0028
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AD-MixHop
    model_plain: AD-MixHop
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8101
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0136
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AD-MixHop_fast
    model_plain: AD-MixHop_fast
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8095
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0133
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: WSGNN
    model_plain: WSGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15183'
    title: 'GraphEdit: Large Language Models for Graph Structure Learning'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/HKUDS/GraphEdit
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8088
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0048
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: IDGL
    model_plain: IDGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15183'
    title: 'GraphEdit: Large Language Models for Graph Structure Learning'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/HKUDS/GraphEdit
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8085
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: JacobiConv
    model_plain: JacobiConv
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
    - 0.8078
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0079
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.8058
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0082
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.8053
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0079
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GEN
    model_plain: GEN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15183'
    title: 'GraphEdit: Large Language Models for Graph Structure Learning'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/HKUDS/GraphEdit
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8038
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0072
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: All-In-One
    model_plain: All-In-One
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17676'
    title: Instance-Aware Graph Prompt Learning
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8038
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPRGNN
    model_plain: GPRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16358'
    title: 'ChebMixer: Efficient Graph Representation Learning with MLP Mixer'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8033
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0009
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Fine Tuning
    model_plain: Fine Tuning
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17676'
    title: Instance-Aware Graph Prompt Learning
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8033
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NodeFormer
    model_plain: NodeFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15183'
    title: 'GraphEdit: Large Language Models for Graph Structure Learning'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/HKUDS/GraphEdit
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8028
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0057
    - null
    - null
    - null
    - null
    - null
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
    - 0.8014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0087
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.8013
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0084
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AD-GATv2
    model_plain: AD-GATv2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.801
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0099
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: BernNet
    model_plain: BernNet
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
    - 0.8008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0075
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AD-GAT
    model_plain: AD-GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7992
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0076
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AD-GraphSAGE_fast
    model_plain: AD-GraphSAGE_fast
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7988
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: AD-GraphSAGE
    model_plain: AD-GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7984
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0126
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.7965
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0102
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Adapt
    model_plain: Adapt
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15097'
    title: 'Policy-GNN: Aggregation Optimization for Graph Neural Networks'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.796
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16358'
    title: 'ChebMixer: Efficient Graph Representation Learning with MLP Mixer'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7948
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0066
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16358'
    title: 'ChebMixer: Efficient Graph Representation Learning with MLP Mixer'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7933
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0084
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AD-GCN
    model_plain: AD-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7914
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AD-GCN_fast
    model_plain: AD-GCN_fast
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7913
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0099
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AD-GAT_fast
    model_plain: AD-GAT_fast
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7911
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: SEGSL
    model_plain: SEGSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15183'
    title: 'GraphEdit: Large Language Models for Graph Structure Learning'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/HKUDS/GraphEdit
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7891
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0052
    - null
    - null
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
    arxiv_id: '2402.15183'
    title: 'GraphEdit: Large Language Models for Graph Structure Learning'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/HKUDS/GraphEdit
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7887
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0218
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CoGSL
    model_plain: CoGSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15183'
    title: 'GraphEdit: Large Language Models for Graph Structure Learning'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/HKUDS/GraphEdit
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7884
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0011
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GSR
    model_plain: GSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15183'
    title: 'GraphEdit: Large Language Models for Graph Structure Learning'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/HKUDS/GraphEdit
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7877
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: GCN-LPA
    model_plain: GCN-LPA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.06755'
    title: Unifying Graph Convolutional Neural Networks and Label Propagation
    date: Feb 17, 2020
    date_iso: '2020-02-17'
    date_display: Feb 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.787
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPF-plus
    model_plain: GPF-plus
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17676'
    title: Instance-Aware Graph Prompt Learning
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7867
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0092
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: EvenNet
    model_plain: EvenNet
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
    - 0.7851
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0063
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GT
    model_plain: GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15183'
    title: 'GraphEdit: Large Language Models for Graph Structure Learning'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/HKUDS/GraphEdit
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7846
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0048
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AD-DirGNN
    model_plain: AD-DirGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7836
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0182
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AD-DirGNN_fast
    model_plain: AD-DirGNN_fast
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7835
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.018
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Geom-GCN
    model_plain: Geom-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07634'
    title: Improving Graph Neural Networks with Simple Architecture Design
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/sunilkmaurya/FSGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7799
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.7787
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.019
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Geom-GCN-I-s
    model_plain: Geom-GCN-I-s
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.05287'
    title: 'Geom-GCN: Geometric Graph Convolutional Networks'
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7783
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Dir-GNN
    model_plain: Dir-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7771
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0078
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Whole Dataset
    model_plain: Whole Dataset
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.13200'
    title: 'RobGC: Towards Robust Graph Condensation'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/XYGaoG/RobGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.777
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: N.S.-GCN
    model_plain: N.S.-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08871'
    title: Adapting to Heterophilic Graph Data with Structure-Guided Neighbor Discovery
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7769
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0028
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPF
    model_plain: GPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17676'
    title: Instance-Aware Graph Prompt Learning
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7767
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: GAUG
    model_plain: GAUG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15183'
    title: 'GraphEdit: Large Language Models for Graph Structure Learning'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/HKUDS/GraphEdit
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7761
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0102
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FastGCN
    model_plain: FastGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15097'
    title: 'Policy-GNN: Aggregation Optimization for Graph Neural Networks'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.776
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: S-GCN
    model_plain: S-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08871'
    title: Adapting to Heterophilic Graph Data with Structure-Guided Neighbor Discovery
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7757
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0024
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.7749
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
    - null
    - null
    - null
    - null
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7741
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: simple GNN model (3-hop)
    model_plain: simple GNN model (3-hop)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07634'
    title: Improving Graph Neural Networks with Simple Architecture Design
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/sunilkmaurya/FSGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.774
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0193
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SSGC
    model_plain: SSGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08871'
    title: Adapting to Heterophilic Graph Data with Structure-Guided Neighbor Discovery
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7731
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0024
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GOAL
    model_plain: GOAL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.07608'
    title: 'Finding the Missing-half: Graph Complementary Learning for Homophily-prone
      and Heterophily-prone Graphs'
    date: Jun 13, 2023
    date_iso: '2023-06-13'
    date_display: Jun 2023
    codebase_url: https://github.com/zyzisastudyreallyhardguy/GOAL-Graph-Complementary-Learning
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7715
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0095
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GGCN
    model_plain: GGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.15454'
    title: 'GPNet: Simplifying Graph Neural Networks via Multi-channel Geometric Polynomials'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7714
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.015
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCNII
    model_plain: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07634'
    title: Improving Graph Neural Networks with Simple Architecture Design
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/sunilkmaurya/FSGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7713
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0138
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NAGphormer
    model_plain: NAGphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16358'
    title: 'ChebMixer: Efficient Graph Representation Learning with MLP Mixer'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7712
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: H-GCN
    model_plain: H-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.15454'
    title: 'GPNet: Simplifying Graph Neural Networks via Multi-channel Geometric Polynomials'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7711
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.016
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: H2GCN
    model_plain: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.14418'
    title: Optimization-Induced Graph Implicit Nonlinear Diffusion
    date: Jun 29, 2022
    date_iso: '2022-06-29'
    date_display: Jun 2022
    codebase_url: https://github.com/7qchen/GIND
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7711
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRED
    model_plain: GRED
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15326'
    title: Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective
      of Operator Semigroup Theory
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LOGO-CUHKSZ/SGOS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7709
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0178
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: H2GCN-1
    model_plain: H2GCN-1
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07634'
    title: Improving Graph Neural Networks with Simple Architecture Design
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/sunilkmaurya/FSGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7707
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0164
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PDE-Log
    model_plain: PDE-Log
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15326'
    title: Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective
      of Operator Semigroup Theory
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LOGO-CUHKSZ/SGOS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7707
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.016
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TAPE_GCN + LLM-based LPA
    model_plain: TAPE_GCN + LLM-based LPA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14324'
    title: Large Language Models as Topological Structure Enhancers for Text-Attributed
      Graphs
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/sunshy-1/LLM4GraphTopology
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7692
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0059
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CPGNN
    model_plain: CPGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15326'
    title: Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective
      of Operator Semigroup Theory
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LOGO-CUHKSZ/SGOS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7691
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: ALT
    model_plain: ALT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.07256'
    title: 'Graph homophily booster: Reimagining the role of discrete features in
      heterophilic graph learning'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/q-rz/ICLR26-GRAPHITE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7688
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: H2GCN-2
    model_plain: H2GCN-2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7688
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0177
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TAPE_GCN + LLM-based A-D
    model_plain: TAPE_GCN + LLM-based A-D
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14324'
    title: Large Language Models as Topological Structure Enhancers for Text-Attributed
      Graphs
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/sunshy-1/LLM4GraphTopology
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7684
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0076
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FAGCN
    model_plain: FAGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.07256'
    title: 'Graph homophily booster: Reimagining the role of discrete features in
      heterophilic graph learning'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/q-rz/ICLR26-GRAPHITE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7682
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: WRGAT
    model_plain: WRGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.16026'
    title: 'MUSE: Multi-View Contrastive Learning for Heterophilic Graphs'
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7681
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0189
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GIND
    model_plain: GIND
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.14418'
    title: Optimization-Induced Graph Implicit Nonlinear Diffusion
    date: Jun 29, 2022
    date_iso: '2022-06-29'
    date_display: Jun 2022
    codebase_url: https://github.com/7qchen/GIND
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7681
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SBM
    model_plain: SBM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.13060'
    title: Graph Attention Retrospective
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.768
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FSGNN
    model_plain: FSGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.07256'
    title: 'Graph homophily booster: Reimagining the role of discrete features in
      heterophilic graph learning'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/q-rz/ICLR26-GRAPHITE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7677
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: PDE-Expn
    model_plain: PDE-Expn
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15326'
    title: Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective
      of Operator Semigroup Theory
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LOGO-CUHKSZ/SGOS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7675
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0176
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: H2GCN
    model_plain: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08871'
    title: Adapting to Heterophilic Graph Data with Structure-Guided Neighbor Discovery
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7672
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0021
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ARIEL
    model_plain: ARIEL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.13854'
    title: arXiv:2306.13854
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/yeonjun-in/torch-SP-AGCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.767
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DAGCN
    model_plain: DAGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1908.05081'
    title: 'AdaGCN: Adaboosting Graph Convolutional Networks into Deep Models'
    date: Aug 2019
    date_iso: 2019-08
    date_display: Aug 2019
    codebase_url: https://github.com/datake/AdaGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7668
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: gfNN
    model_plain: gfNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08871'
    title: Adapting to Heterophilic Graph Data with Structure-Guided Neighbor Discovery
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7666
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0018
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Dir-GNN
    model_plain: Dir-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08871'
    title: Adapting to Heterophilic Graph Data with Structure-Guided Neighbor Discovery
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7666
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0026
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SG-FBGNN_N
    model_plain: SG-FBGNN_N
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08871'
    title: Adapting to Heterophilic Graph Data with Structure-Guided Neighbor Discovery
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7665
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0021
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGI-ADV
    model_plain: DGI-ADV
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.13854'
    title: arXiv:2306.13854
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/yeonjun-in/torch-SP-AGCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.766
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.14418'
    title: Optimization-Induced Graph Implicit Nonlinear Diffusion
    date: Jun 29, 2022
    date_iso: '2022-06-29'
    date_display: Jun 2022
    codebase_url: https://github.com/7qchen/GIND
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7653
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TAPE_GCN-LPA
    model_plain: TAPE_GCN-LPA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14324'
    title: Large Language Models as Topological Structure Enhancers for Text-Attributed
      Graphs
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/sunshy-1/LLM4GraphTopology
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7653
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0073
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ASGC
    model_plain: ASGC
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
    - 0.7652
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0036
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCDM - GSL
    model_plain: GCDM - GSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.13200'
    title: 'RobGC: Towards Robust Graph Condensation'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/XYGaoG/RobGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.765
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: BORF
    model_plain: BORF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7649
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0028
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TAGCN
    model_plain: TAGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.07256'
    title: 'Graph homophily booster: Reimagining the role of discrete features in
      heterophilic graph learning'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/q-rz/ICLR26-GRAPHITE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7649
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0141
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ACM-GNN
    model_plain: ACM-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.07256'
    title: 'Graph homophily booster: Reimagining the role of discrete features in
      heterophilic graph learning'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/q-rz/ICLR26-GRAPHITE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7647
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0099
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DAGNN
    model_plain: DAGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7644
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0197
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SRDF
    model_plain: SRDF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7643
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0032
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRAPHITE
    model_plain: GRAPHITE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.07256'
    title: 'Graph homophily booster: Reimagining the role of discrete features in
      heterophilic graph learning'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/q-rz/ICLR26-GRAPHITE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7641
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0157
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GIC
    model_plain: GIC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.02534'
    title: 'MGAE: Masked Autoencoders for Self-Supervised Learning on Graphs'
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7639
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FOSR
    model_plain: FOSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7634
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0027
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: novel all-pair message passing scheme
    model_plain: novel all-pair message passing scheme
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.08385'
    title: 'Align All the Nodes: Scalable Learning of Flexible Latent Structure for
      Graph Neural Networks'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/qitianwu/NodeFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7633
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0059
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN + LLM-based A-D
    model_plain: GCN + LLM-based A-D
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14324'
    title: Large Language Models as Topological Structure Enhancers for Text-Attributed
      Graphs
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/sunshy-1/LLM4GraphTopology
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7633
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0117
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GATv2
    model_plain: GATv2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7631
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: MixHop
    model_plain: MixHop
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07634'
    title: Improving Graph Neural Networks with Simple Architecture Design
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/sunilkmaurya/FSGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7626
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0133
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DIGL
    model_plain: DIGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7622
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0034
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.7622
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Base (GAT)
    model_plain: Base (GAT)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.762
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0027
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DAG + DIFFORMER-a
    model_plain: DAG + DIFFORMER-a
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.13148'
    title: Transformers over Directed Acyclic Graphs
    date: Oct 24, 2022
    date_iso: '2022-10-24'
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.762
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCDM Jaccard
    model_plain: GCDM Jaccard
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.13200'
    title: 'RobGC: Towards Robust Graph Condensation'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/XYGaoG/RobGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.762
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MLP
    model_plain: MLP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16358'
    title: 'ChebMixer: Efficient Graph Representation Learning with MLP Mixer'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7618
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SG-GCN_L
    model_plain: SG-GCN_L
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08871'
    title: Adapting to Heterophilic Graph Data with Structure-Guided Neighbor Discovery
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7615
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0022
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN + LLM-based LPA
    model_plain: GCN + LLM-based LPA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14324'
    title: Large Language Models as Topological Structure Enhancers for Text-Attributed
      Graphs
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/sunshy-1/LLM4GraphTopology
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7614
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0149
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GTR
    model_plain: GTR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7612
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0028
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCL-LR-Attention
    model_plain: GCL-LR-Attention
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.761
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TAPE_GAT
    model_plain: TAPE_GAT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14324'
    title: Large Language Models as Topological Structure Enhancers for Text-Attributed
      Graphs
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/sunshy-1/LLM4GraphTopology
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.761
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0107
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: JDR
    model_plain: JDR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7609
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0029
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08871'
    title: Adapting to Heterophilic Graph Data with Structure-Guided Neighbor Discovery
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7608
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0022
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: UDGNN_GCN
    model_plain: UDGNN_GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7605
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0183
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07634'
    title: Improving Graph Neural Networks with Simple Architecture Design
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/sunilkmaurya/FSGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7604
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.013
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.7603
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: QGNN
    model_plain: QGNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.05089'
    title: Quaternion Graph Neural Networks
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: https://github.com/daiquocnguyen/QGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7603
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Base (GCN)
    model_plain: Base (GCN)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7601
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0025
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CLN
    model_plain: CLN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1805.07984'
    title: Adversarial Attacks on Neural Networks for Graph Data
    date: May 2018
    date_iso: 2018-05
    date_display: May 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.76
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: BLEND
    model_plain: BLEND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.09443'
    title: Beltrami Flow and Neural Diffusion on Graphs
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: https://github.com/twitter-research/graph-neural-pde
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.759
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.013
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GSL
    model_plain: GSL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.13200'
    title: 'RobGC: Towards Robust Graph Condensation'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/XYGaoG/RobGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.759
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCDM Plain
    model_plain: GCDM Plain
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.13200'
    title: 'RobGC: Towards Robust Graph Condensation'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/XYGaoG/RobGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.759
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SP-AGCL
    model_plain: SP-AGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.13854'
    title: arXiv:2306.13854
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/yeonjun-in/torch-SP-AGCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.759
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Clean
    model_plain: Clean
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.08057'
    title: Understanding and Improving Graph Injection Attack by Promoting Unnoticeability
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/LFhase/GIA-HAO
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7587
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.7587
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.015
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: UDGNN*_SAGE
    model_plain: UDGNN*_SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7585
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0169
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: JK-Net
    model_plain: JK-Net
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.14418'
    title: Optimization-Induced Graph Implicit Nonlinear Diffusion
    date: Jun 29, 2022
    date_iso: '2022-06-29'
    date_display: Jun 2022
    codebase_url: https://github.com/7qchen/GIND
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7585
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: contrastive method w
    model_plain: contrastive method w
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.00012'
    title: 'Reliable Representations Make A Stronger Defender: Unsupervised Structure
      Refinement for Robust GNN'
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: https://github.com/likuanppd/STABLE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7582
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0041
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Auto-HeG
    model_plain: Auto-HeG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.12357'
    title: 'Auto-HeG: Automated Graph Neural Network on Heterophilic Graphs'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7581
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0152
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ILLS
    model_plain: ILLS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.758
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCL-LRR
    model_plain: GCL-LRR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.758
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.7576
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.019
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Geom-GCN-I-g
    model_plain: Geom-GCN-I-g
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.05287'
    title: 'Geom-GCN: Geometric Graph Convolutional Networks'
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7573
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TAPE_GCN
    model_plain: TAPE_GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14324'
    title: Large Language Models as Topological Structure Enhancers for Text-Attributed
      Graphs
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/sunshy-1/LLM4GraphTopology
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7571
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0046
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Geom-GCN-IP
    model_plain: Geom-GCN-IP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.05287'
    title: 'Geom-GCN: Geometric Graph Convolutional Networks'
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7571
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DIFFormer
    model_plain: DIFFormer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.13148'
    title: Transformers over Directed Acyclic Graphs
    date: Oct 24, 2022
    date_iso: '2022-10-24'
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.757
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPR-GNN
    model_plain: GPR-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.07608'
    title: 'Finding the Missing-half: Graph Complementary Learning for Homophily-prone
      and Heterophily-prone Graphs'
    date: Jun 13, 2023
    date_iso: '2023-06-13'
    date_display: Jun 2023
    codebase_url: https://github.com/zyzisastudyreallyhardguy/GOAL-Graph-Complementary-Learning
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.757
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0081
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: APPNP Paper
    model_plain: APPNP Paper
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.757
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.12931'
    title: Demystifying Graph Convolution with a Simple Concatenation
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: https://bitbucket.org/gconcat2021/graph-concatenation
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.757
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRCN
    model_plain: GRCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.00012'
    title: 'Reliable Representations Make A Stronger Defender: Unsupervised Structure
      Refinement for Robust GNN'
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: https://github.com/likuanppd/STABLE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7565
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0021
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Conn-NSD
    model_plain: Conn-NSD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.15454'
    title: 'GPNet: Simplifying Graph Neural Networks via Multi-channel Geometric Polynomials'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7561
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.019
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Graphormer
    model_plain: Graphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1710.10321'
    title: arXiv:1710.10321
    date: Oct 2017
    date_iso: 2017-10
    date_display: Oct 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.756
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN-LPA_DeBERTa
    model_plain: GCN-LPA_DeBERTa
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14324'
    title: Large Language Models as Topological Structure Enhancers for Text-Attributed
      Graphs
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/sunshy-1/LLM4GraphTopology
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7559
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0104
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DeepGCNs
    model_plain: DeepGCNs
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.15454'
    title: 'GPNet: Simplifying Graph Neural Networks via Multi-channel Geometric Polynomials'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7558
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DeeperGCN
    model_plain: DeeperGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7558
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0118
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPRGNN
    model_plain: GPRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7556
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: GraphSAGE + MH-Aug (w/ Reg)
    model_plain: GraphSAGE + MH-Aug (w/ Reg)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7555
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0044
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN + MH-Aug (w/ Reg)
    model_plain: GCN + MH-Aug (w/ Reg)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7553
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0032
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TADA (EXPHORMER)
    model_plain: TADA (EXPHORMER)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: Mar 2025
    date_iso: 2025-03
    date_display: Mar 2025
    codebase_url: https://github.com/Statistical-Deep-Learning/DoG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.755
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ChebNet
    model_plain: ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.07608'
    title: 'Finding the Missing-half: Graph Complementary Learning for Homophily-prone
      and Heterophily-prone Graphs'
    date: Jun 13, 2023
    date_iso: '2023-06-13'
    date_display: Jun 2023
    codebase_url: https://github.com/zyzisastudyreallyhardguy/GOAL-Graph-Complementary-Learning
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.755
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0087
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCond Plain
    model_plain: GCond Plain
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.13200'
    title: 'RobGC: Towards Robust Graph Condensation'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/XYGaoG/RobGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.755
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT_DeBERTa
    model_plain: GAT_DeBERTa
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14324'
    title: Large Language Models as Topological Structure Enhancers for Text-Attributed
      Graphs
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/sunshy-1/LLM4GraphTopology
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7547
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0231
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.7546
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: RGCN
    model_plain: RGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.00012'
    title: 'Reliable Representations Make A Stronger Defender: Unsupervised Structure
      Refinement for Robust GNN'
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: https://github.com/likuanppd/STABLE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7541
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1908.05081'
    title: 'AdaGCN: Adaboosting Graph Convolutional Networks into Deep Models'
    date: Aug 2019
    date_iso: 2019-08
    date_display: Aug 2019
    codebase_url: https://github.com/datake/AdaGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7541
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0035
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FLAG (EXPHORMER)
    model_plain: FLAG (EXPHORMER)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: Mar 2025
    date_iso: 2025-03
    date_display: Mar 2025
    codebase_url: https://github.com/Statistical-Deep-Learning/DoG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.754
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
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
    arxiv_id: '1908.05081'
    title: 'AdaGCN: Adaboosting Graph Convolutional Networks into Deep Models'
    date: Aug 2019
    date_iso: 2019-08
    date_display: Aug 2019
    codebase_url: https://github.com/datake/AdaGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.754
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1908.05081'
    title: 'AdaGCN: Adaboosting Graph Convolutional Networks into Deep Models'
    date: Aug 2019
    date_iso: 2019-08
    date_display: Aug 2019
    codebase_url: https://github.com/datake/AdaGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7539
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0027
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CoATA
    model_plain: CoATA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.22299'
    title: 'CoATA: Effective Co-Augmentation of Topology and Attribute for Graph Neural
      Networks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7537
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0021
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: EGNN
    model_plain: EGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.14418'
    title: Optimization-Induced Graph Implicit Nonlinear Diffusion
    date: Jun 29, 2022
    date_iso: '2022-06-29'
    date_display: Jun 2022
    codebase_url: https://github.com/7qchen/GIND
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7531
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GeoMix (EXPHORMER)
    model_plain: GeoMix (EXPHORMER)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: Mar 2025
    date_iso: 2025-03
    date_display: Mar 2025
    codebase_url: https://github.com/Statistical-Deep-Learning/DoG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.753
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AGIA
    model_plain: AGIA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.08057'
    title: Understanding and Improving Graph Injection Attack by Promoting Unnoticeability
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/LFhase/GIA-HAO
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7529
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.7529
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRAFF
    model_plain: GRAFF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15326'
    title: Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective
      of Operator Semigroup Theory
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LOGO-CUHKSZ/SGOS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7527
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0145
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: IGNN
    model_plain: IGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.14418'
    title: Optimization-Induced Graph Implicit Nonlinear Diffusion
    date: Jun 29, 2022
    date_iso: '2022-06-29'
    date_display: Jun 2022
    codebase_url: https://github.com/7qchen/GIND
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7524
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NodeFormer
    model_plain: NodeFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.07256'
    title: 'Graph homophily booster: Reimagining the role of discrete features in
      heterophilic graph learning'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/q-rz/ICLR26-GRAPHITE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.752
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: NODEDUP (EXPHORMER)
    model_plain: NODEDUP (EXPHORMER)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: Mar 2025
    date_iso: 2025-03
    date_display: Mar 2025
    codebase_url: https://github.com/Statistical-Deep-Learning/DoG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.752
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphMix (EXPHORMER)
    model_plain: GraphMix (EXPHORMER)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: Mar 2025
    date_iso: 2025-03
    date_display: Mar 2025
    codebase_url: https://github.com/Statistical-Deep-Learning/DoG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.752
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: STABLE
    model_plain: STABLE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15792'
    title: 'IDEA: Invariant Defense for Graph Adversarial Robustness'
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.752
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PGD
    model_plain: PGD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.08057'
    title: Understanding and Improving Graph Injection Attack by Promoting Unnoticeability
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/LFhase/GIA-HAO
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7519
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE + UDA*
    model_plain: GraphSAGE + UDA*
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7516
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0016
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MetaGIA
    model_plain: MetaGIA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.08057'
    title: Understanding and Improving Graph Injection Attack by Promoting Unnoticeability
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/LFhase/GIA-HAO
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7515
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TDGIA
    model_plain: TDGIA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.08057'
    title: Understanding and Improving Graph Injection Attack by Promoting Unnoticeability
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/LFhase/GIA-HAO
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7512
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GeoMix
    model_plain: GeoMix
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.22299'
    title: 'CoATA: Effective Co-Augmentation of Topology and Attribute for Graph Neural
      Networks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7512
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0026
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LGGD (EXPHORMER)
    model_plain: LGGD (EXPHORMER)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: Mar 2025
    date_iso: 2025-03
    date_display: Mar 2025
    codebase_url: https://github.com/Statistical-Deep-Learning/DoG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.751
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: None
    model_plain: None
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.05057'
    title: Towards More Practical Adversarial Attacks on Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/Mark12Ding/GNN-Practical-Attack
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.751
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: UDGNN*_GAT
    model_plain: UDGNN*_GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7509
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0175
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN_DeBERTa
    model_plain: GCN_DeBERTa
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14324'
    title: Large Language Models as Topological Structure Enhancers for Text-Attributed
      Graphs
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/sunshy-1/LLM4GraphTopology
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7508
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0066
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Cheby+JK
    model_plain: Cheby+JK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07634'
    title: Improving Graph Neural Networks with Simple Architecture Design
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/sunilkmaurya/FSGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7498
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0118
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: S3-CL
    model_plain: S3-CL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.22299'
    title: 'CoATA: Effective Co-Augmentation of Topology and Attribute for Graph Neural
      Networks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7497
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0052
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRACE
    model_plain: GRACE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.13854'
    title: arXiv:2306.13854
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/yeonjun-in/torch-SP-AGCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.749
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Elastic
    model_plain: Elastic
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.00012'
    title: 'Reliable Representations Make A Stronger Defender: Unsupervised Structure
      Refinement for Robust GNN'
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: https://github.com/likuanppd/STABLE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7486
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0053
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: H2GCN
    model_plain: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.05089'
    title: Quaternion Graph Neural Networks
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: https://github.com/daiquocnguyen/QGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7484
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGM
    model_plain: DGM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.04999'
    title: Differentiable Graph Module (DGM) for Graph Convolutional Networks
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: https://github.com/lcosmo/DGM_pytorch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.748
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00924
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LDS
    model_plain: LDS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.13009'
    title: 'Iterative Deep Graph Learning for Graph Neural Networks: Better and Robust
      Node Embeddings'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/hugochan/IDGL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.748
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DoG (EXPHORMER)
    model_plain: DoG (EXPHORMER)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: Mar 2025
    date_iso: 2025-03
    date_display: Mar 2025
    codebase_url: https://github.com/Statistical-Deep-Learning/DoG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.748
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DL
    model_plain: DL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.15454'
    title: 'GPNet: Simplifying Graph Neural Networks via Multi-channel Geometric Polynomials'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.748
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCond STABLE_G
    model_plain: GCond STABLE_G
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.13200'
    title: 'RobGC: Towards Robust Graph Condensation'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/XYGaoG/RobGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.748
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ProtGNN
    model_plain: ProtGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.00012'
    title: 'Reliable Representations Make A Stronger Defender: Unsupervised Structure
      Refinement for Robust GNN'
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: https://github.com/likuanppd/STABLE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7473
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0031
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Geom-GCN
    model_plain: Geom-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.12357'
    title: 'Auto-HeG: Automated Graph Neural Network on Heterophilic Graphs'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7471
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN + GraphMix
    model_plain: GCN + GraphMix
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.747
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0059
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.7468
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.013
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SimPGCN
    model_plain: SimPGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.00012'
    title: 'Reliable Representations Make A Stronger Defender: Unsupervised Structure
      Refinement for Robust GNN'
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: https://github.com/likuanppd/STABLE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7466
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0079
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HyperGRL
    model_plain: HyperGRL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7465
    - null
    - null
    - null
    - 0.9901
    - null
    - null
    - null
    metric_stds:
    - 0.0016
    - null
    - null
    - null
    - 0.0014
    - null
    - null
    - null
  - model: GCDM SVD
    model_plain: GCDM SVD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.13200'
    title: 'RobGC: Towards Robust Graph Condensation'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/XYGaoG/RobGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.746
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: RTGNN
    model_plain: RTGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.746
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: S^3-CL
    model_plain: S^3-CL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.08480'
    title: Eliciting Structural and Semantic Global Knowledge in Unsupervised Graph
      Contrastive Learning
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/kaize0409/S-3-CL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.746
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: RGCN
    model_plain: RGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15792'
    title: 'IDEA: Invariant Defense for Graph Adversarial Robustness'
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.746
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MGAE
    model_plain: MGAE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.02534'
    title: 'MGAE: Masked Autoencoders for Self-Supervised Learning on Graphs'
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.746
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Diffusion-X
    model_plain: Diffusion-X
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7456
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.015
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN-JKNet
    model_plain: GCN-JKNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7451
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0175
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.02534'
    title: 'MGAE: Masked Autoencoders for Self-Supervised Learning on Graphs'
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7451
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0051
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CNNs
    model_plain: CNNs
    is_baseline: false
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
    - 0.745
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FMLP-O
    model_plain: FMLP-O
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.06631'
    title: Frameless Graph Knowledge Distillation
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: https://github.com/dshi3553usyd/Frameless_Graph_Distillation.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.745
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0071
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ADGCN-R
    model_plain: ADGCN-R
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.07295'
    title: Adversarial Graph Disentanglement with Component-specific Aggregation
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/SsGood/ADGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.745
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SANE-hete
    model_plain: SANE-hete
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.12357'
    title: 'Auto-HeG: Automated Graph Neural Network on Heterophilic Graphs'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7446
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0159
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LCS
    model_plain: LCS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.15920'
    title: 'ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order
      Neighboring Feature Fusion'
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/lx970414/ScaleGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7444
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DoG (GGD)
    model_plain: DoG (GGD)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: Mar 2025
    date_iso: 2025-03
    date_display: Mar 2025
    codebase_url: https://github.com/Statistical-Deep-Learning/DoG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.744
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SANE
    model_plain: SANE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.12357'
    title: 'Auto-HeG: Automated Graph Neural Network on Heterophilic Graphs'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7433
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.05287'
    title: 'Geom-GCN: Geometric Graph Convolutional Networks'
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7432
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DoG (GraphMAE)
    model_plain: DoG (GraphMAE)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: Mar 2025
    date_iso: 2025-03
    date_display: Mar 2025
    codebase_url: https://github.com/Statistical-Deep-Learning/DoG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.743
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN_n + DropNode
    model_plain: GCN_n + DropNode
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.12578'
    title: Graph Convolutional Neural Networks with Node Transition Probability-based
      Message Passing and DropNode Regularization
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.743
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PGCN_n + DropNode
    model_plain: PGCN_n + DropNode
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.12578'
    title: Graph Convolutional Neural Networks with Node Transition Probability-based
      Message Passing and DropNode Regularization
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.743
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPNet-ReLU
    model_plain: GPNet-ReLU
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.15454'
    title: 'GPNet: Simplifying Graph Neural Networks via Multi-channel Geometric Polynomials'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.743
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN-SVD
    model_plain: GCN-SVD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.13200'
    title: 'RobGC: Towards Robust Graph Condensation'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/XYGaoG/RobGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.743
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN_kNN
    model_plain: GCN_kNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.13200'
    title: 'RobGC: Towards Robust Graph Condensation'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/XYGaoG/RobGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.743
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LGD-GCN
    model_plain: LGD-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.07295'
    title: Adversarial Graph Disentanglement with Component-specific Aggregation
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/SsGood/ADGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.743
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AD-GCN
    model_plain: AD-GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.07295'
    title: Adversarial Graph Disentanglement with Component-specific Aggregation
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/SsGood/ADGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.743
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCL
    model_plain: GCL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.00064'
    title: 'SPGCL: Simple yet Powerful Graph Contrastive Learning via SVD-Guided Structural
      Perturbation'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.743
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphMixer
    model_plain: GraphMixer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.22299'
    title: 'CoATA: Effective Co-Augmentation of Topology and Attribute for Graph Neural
      Networks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7428
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0045
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HAT-GAE
    model_plain: HAT-GAE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.12063'
    title: 'HAT-GAE: Self-Supervised Graph Auto-encoders with Hierarchical Adaptive
      Masking and Trainable Corruption'
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7428
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0022
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PaGCL
    model_plain: PaGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7427
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0021
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN-VN
    model_plain: GCN-VN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1908.05081'
    title: 'AdaGCN: Adaboosting Graph Convolutional Networks into Deep Models'
    date: Aug 2019
    date_iso: 2019-08
    date_display: Aug 2019
    codebase_url: https://github.com/datake/AdaGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7425
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ELU-GCN
    model_plain: ELU-GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.02279'
    title: arXiv:2411.02279
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/huangJC0429/label-utilize-GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7423
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0062
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRCN
    model_plain: GRCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15183'
    title: 'GraphEdit: Large Language Models for Graph Structure Learning'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/HKUDS/GraphEdit
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7423
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0118
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: EE-UFG
    model_plain: EE-UFG
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.05767'
    title: Dirichlet Energy Enhancement of Graph Neural Networks by Framelet Augmentation
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.742
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.013
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: G-Zoom
    model_plain: G-Zoom
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.10698'
    title: Towards Graph Self-Supervised Learning with Contrastive Adjusted Zooming
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.742
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CRGNN
    model_plain: CRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.742
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DFNet
    model_plain: DFNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.11689'
    title: Self-Supervised Graph Representation Learning via Topology Transformations
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/gyshgx868/topo-ter
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.742
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCA
    model_plain: GCA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.13854'
    title: arXiv:2306.13854
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/yeonjun-in/torch-SP-AGCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.742
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Grain(ball-D)
    model_plain: Grain(ball-D)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.00219'
    title: 'Grain: Improving Data Efficiency of Graph Neural Networks via Diversified
      Influence Maximization'
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/zwt233/Grain
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.742
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: IDGL
    model_plain: IDGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.13009'
    title: 'Iterative Deep Graph Learning for Graph Neural Networks: Better and Robust
      Node Embeddings'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/hugochan/IDGL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.741
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRAND
    model_plain: GRAND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.05767'
    title: Dirichlet Energy Enhancement of Graph Neural Networks by Framelet Augmentation
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.741
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.017
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Unifying Graph Contrastive Learning
    model_plain: Unifying Graph Contrastive Learning
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.08792'
    title: Unifying Graph Contrastive Learning with Flexible Contextual Scopes
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: https://github.com/zyzisastudyreallyhardguy/UGCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.741
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCDM kNN
    model_plain: GCDM kNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.13200'
    title: 'RobGC: Towards Robust Graph Condensation'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/XYGaoG/RobGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.741
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DoG (MVGRL)
    model_plain: DoG (MVGRL)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: Mar 2025
    date_iso: 2025-03
    date_display: Mar 2025
    codebase_url: https://github.com/Statistical-Deep-Learning/DoG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.74
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN-DVAT
    model_plain: GCN-DVAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.74
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SpatUFG
    model_plain: SpatUFG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.06631'
    title: Frameless Graph Knowledge Distillation
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: https://github.com/dshi3553usyd/Frameless_Graph_Distillation.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.74
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0036
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GLNN
    model_plain: GLNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.06631'
    title: Frameless Graph Knowledge Distillation
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: https://github.com/dshi3553usyd/Frameless_Graph_Distillation.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.74
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN-Jaccard
    model_plain: GCN-Jaccard
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.13200'
    title: 'RobGC: Towards Robust Graph Condensation'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/XYGaoG/RobGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.74
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SFA
    model_plain: SFA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.74
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MERIT
    model_plain: MERIT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.08480'
    title: Eliciting Structural and Semantic Global Knowledge in Unsupervised Graph
      Contrastive Learning
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/kaize0409/S-3-CL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.74
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Soft-Median
    model_plain: Soft-Median
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15792'
    title: 'IDEA: Invariant Defense for Graph Adversarial Robustness'
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.74
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.013
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: IPGDN
    model_plain: IPGDN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.11430'
    title: Independence Promoted Graph Disentangled Networks
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.74
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ASGNN
    model_plain: ASGNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.01002'
    title: 'ASGNN: Graph Neural Networks with Adaptive Structure'
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7399
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0093
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphGLOW
    model_plain: GraphGLOW
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.11264'
    title: 'GraphGLOW: Open-World Graph Structure Learning for Cross-Graph Topology
      Refinement'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/WtaoZhao/GraphGLOW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.739
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: UGMAE
    model_plain: UGMAE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08023'
    title: 'UGMAE: A Unified Framework for Graph Masked Autoencoders'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.739
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Elastic GNN
    model_plain: Elastic GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.01002'
    title: 'ASGNN: Graph Neural Networks with Adaptive Structure'
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7382
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0043
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Self-Explainable GNN
    model_plain: Self-Explainable GNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.12055'
    title: Towards Self-Explainable Graph Neural Network
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/EnyanDai/SEGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.738
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SUFG
    model_plain: SUFG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.06631'
    title: Frameless Graph Knowledge Distillation
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: https://github.com/dshi3553usyd/Frameless_Graph_Distillation.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.738
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0073
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DAGNN
    model_plain: DAGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15097'
    title: 'Policy-GNN: Aggregation Optimization for Graph Neural Networks'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.738
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPR-GNN
    model_plain: GPR-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.08048'
    title: Towards Understanding the Generalization of Graph Neural Networks
    date: May 14, 2023
    date_iso: '2023-05-14'
    date_display: May 2023
    codebase_url: https://github.com/jianhao2016/GPRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7379
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0067
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NOSMOG
    model_plain: NOSMOG
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2208.10010'
    title: 'NOSMOG: Learning Noise-robust and Structure-aware MLPs on Graphs'
    date: Aug 2022
    date_iso: 2022-08
    date_display: Aug 2022
    codebase_url: https://github.com/meettyj/NOSMOG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7378
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: Clean GNN (GCond)
    model_plain: Clean GNN (GCond)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.11025'
    title: Backdoor Graph Condensation
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/JiahaoWuGit/BGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7376
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0021
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCat
    model_plain: GCat
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.12931'
    title: Demystifying Graph Convolution with a Simple Concatenation
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: https://bitbucket.org/gconcat2021/graph-concatenation
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7372
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0083
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphVAT
    model_plain: GraphVAT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1902.08226'
    title: 'Graph Adversarial Training: Dynamically Regularizing Based on Graph Structure'
    date: Feb 2019
    date_iso: 2019-02
    date_display: Feb 2019
    codebase_url: https://github.com/fulifeng/GraphAT
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.737
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GFSA
    model_plain: GFSA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.737
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ECL-GSR
    model_plain: ECL-GSR
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.737
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0075
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GSC
    model_plain: GSC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.11996'
    title: Generative Subgraph Contrast for Self-Supervised Graph Representation Learning
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: https://github.com/yh-han/GSC.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.737
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Grain(NN-D)
    model_plain: Grain(NN-D)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.00219'
    title: 'Grain: Improving Data Efficiency of Graph Neural Networks via Diversified
      Influence Maximization'
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/zwt233/Grain
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.737
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.05287'
    title: 'Geom-GCN: Geometric Graph Convolutional Networks'
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7368
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Jaccard
    model_plain: Jaccard
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.00012'
    title: 'Reliable Representations Make A Stronger Defender: Unsupervised Structure
      Refinement for Robust GNN'
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: https://github.com/likuanppd/STABLE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7364
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0035
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PairNorm
    model_plain: PairNorm
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.05767'
    title: Dirichlet Energy Enhancement of Graph Neural Networks by Framelet Augmentation
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.736
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.015
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DoG (GCN)
    model_plain: DoG (GCN)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: Mar 2025
    date_iso: 2025-03
    date_display: Mar 2025
    codebase_url: https://github.com/Statistical-Deep-Learning/DoG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.736
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CG3
    model_plain: CG3
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.10698'
    title: Towards Graph Self-Supervised Learning with Contrastive Adjusted Zooming
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.736
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SuperGAT
    model_plain: SuperGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.12055'
    title: Towards Self-Explainable Graph Neural Network
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/EnyanDai/SEGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.736
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Local-GCL
    model_plain: Local-GCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.04604'
    title: Localized Graph Contrastive Learning
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.736
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FLAG
    model_plain: FLAG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15792'
    title: 'IDEA: Invariant Defense for Graph Adversarial Robustness'
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.736
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: STGCN
    model_plain: STGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.07295'
    title: Adversarial Graph Disentanglement with Component-specific Aggregation
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/SsGood/ADGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.736
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN + PCL
    model_plain: GCN + PCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.09532'
    title: Pseudo Contrastive Learning for Graph-based Semi-supervised Learning
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.736
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0023
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CG^3
    model_plain: CG^3
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.09532'
    title: Pseudo Contrastive Learning for Graph-based Semi-supervised Learning
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.736
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Str-GCL
    model_plain: Str-GCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7358
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0084
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN + UDA*
    model_plain: GCN + UDA*
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7356
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0041
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Bt.FP
    model_plain: Bt.FP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1908.05081'
    title: 'AdaGCN: Adaboosting Graph Convolutional Networks into Deep Models'
    date: Aug 2019
    date_iso: 2019-08
    date_display: Aug 2019
    codebase_url: https://github.com/datake/AdaGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7355
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0057
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LDS
    model_plain: LDS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7355
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0054
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DSSL
    model_plain: DSSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.16026'
    title: 'MUSE: Multi-View Contrastive Learning for Heterophilic Graphs'
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7351
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0064
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NAFS-concat
    model_plain: NAFS-concat
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.08583'
    title: arXiv:2206.08583
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/PKU-DAIR/NAFS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.735
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PNA
    model_plain: PNA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1710.10321'
    title: arXiv:1710.10321
    date: Oct 2017
    date_iso: 2017-10
    date_display: Oct 2017
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.735
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CPGNN
    model_plain: CPGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.735
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphNAS
    model_plain: GraphNAS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15097'
    title: 'Policy-GNN: Aggregation Optimization for Graph Neural Networks'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.735
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MVGRL
    model_plain: MVGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.12063'
    title: 'HAT-GAE: Self-Supervised Graph Auto-encoders with Hierarchical Adaptive
      Masking and Trainable Corruption'
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7345
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphMAE
    model_plain: GraphMAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.12063'
    title: 'HAT-GAE: Self-Supervised Graph Auto-encoders with Hierarchical Adaptive
      Masking and Trainable Corruption'
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7341
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0041
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: BLEND-kNN
    model_plain: BLEND-kNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.09443'
    title: Beltrami Flow and Neural Diffusion on Graphs
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: https://github.com/twitter-research/graph-neural-pde
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.734
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGMLP
    model_plain: DGMLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.00955'
    title: Evaluating Deep Graph Neural Networks
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.734
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN+GDC
    model_plain: GCN+GDC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.13009'
    title: 'Iterative Deep Graph Learning for Graph Neural Networks: Better and Robust
      Node Embeddings'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/hugochan/IDGL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.734
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCNII
    model_plain: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.15454'
    title: 'GPNet: Simplifying Graph Neural Networks via Multi-channel Geometric Polynomials'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.734
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NAFS-max
    model_plain: NAFS-max
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.08583'
    title: arXiv:2206.08583
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/PKU-DAIR/NAFS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.734
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DisGNN
    model_plain: DisGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.07295'
    title: Adversarial Graph Disentanglement with Component-specific Aggregation
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/SsGood/ADGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.734
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: BGRL
    model_plain: BGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.13854'
    title: arXiv:2306.13854
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/yeonjun-in/torch-SP-AGCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.734
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN + GAug-M
    model_plain: GCN + GAug-M
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.733
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Pro-GNN
    model_plain: Pro-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.12055'
    title: Towards Self-Explainable Graph Neural Network
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/EnyanDai/SEGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.733
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HONGAT
    model_plain: HONGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.733
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AP-GCN
    model_plain: AP-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.07295'
    title: Adversarial Graph Disentanglement with Component-specific Aggregation
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/SsGood/ADGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.733
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: InfoGCL
    model_plain: InfoGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.12063'
    title: 'HAT-GAE: Self-Supervised Graph Auto-encoders with Hierarchical Adaptive
      Masking and Trainable Corruption'
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7329
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0026
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: notations and formally define the problem
    model_plain: notations and formally define the problem
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2005.10203'
    title: Graph Structure Learning for Robust Graph Neural Networks
    date: May 2020
    date_iso: 2020-05
    date_display: May 2020
    codebase_url: https://github.com/ChandlerBang/Pro-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7328
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0069
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Pro-GNN-fs
    model_plain: Pro-GNN-fs
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2005.10203'
    title: Graph Structure Learning for Robust Graph Neural Networks
    date: May 2020
    date_iso: 2020-05
    date_display: May 2020
    codebase_url: https://github.com/ChandlerBang/Pro-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7326
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0038
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT + UDA*
    model_plain: GAT + UDA*
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7324
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0048
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CAT-I-MF
    model_plain: CAT-I-MF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.03147'
    title: Learning Conjoint Attentions for Graph Neural Nets
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7324
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0021
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT + PCL
    model_plain: GAT + PCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.09532'
    title: Pseudo Contrastive Learning for Graph-based Semi-supervised Learning
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7322
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0044
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: g-U-Nets
    model_plain: g-U-Nets
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.05178'
    title: Graph U-Nets
    date: May 11, 2019
    date_iso: '2019-05-11'
    date_display: May 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.732
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
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
    - 0.732
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SubG-Con
    model_plain: SubG-Con
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.10698'
    title: Towards Graph Self-Supervised Learning with Contrastive Adjusted Zooming
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.732
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Graph U-Net
    model_plain: Graph U-Net
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.12578'
    title: Graph Convolutional Neural Networks with Node Transition Probability-based
      Message Passing and DropNode Regularization
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.732
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NAFS-mean
    model_plain: NAFS-mean
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.08583'
    title: arXiv:2206.08583
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/PKU-DAIR/NAFS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.732
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DisenGCN
    model_plain: DisenGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.11430'
    title: Independence Promoted Graph Disentangled Networks
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.732
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LINKX
    model_plain: LINKX
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.15454'
    title: 'GPNet: Simplifying Graph Neural Networks via Multi-channel Geometric Polynomials'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7319
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Sbert
    model_plain: Sbert
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14324'
    title: Large Language Models as Topological Structure Enhancers for Text-Attributed
      Graphs
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/sunshy-1/LLM4GraphTopology
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7317
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0175
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SLAPS
    model_plain: SLAPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15183'
    title: 'GraphEdit: Large Language Models for Graph Structure Learning'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/HKUDS/GraphEdit
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7317
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0087
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DeBERTa
    model_plain: DeBERTa
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14324'
    title: Large Language Models as Topological Structure Enhancers for Text-Attributed
      Graphs
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/sunshy-1/LLM4GraphTopology
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7313
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0194
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: RpHGNN
    model_plain: RpHGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.15920'
    title: 'ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order
      Neighboring Feature Fusion'
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/lx970414/ScaleGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7312
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TOP
    model_plain: TOP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.15920'
    title: 'ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order
      Neighboring Feature Fusion'
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/lx970414/ScaleGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7311
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: APPNP
    model_plain: APPNP
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
    - 0.731
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: H2GCN
    model_plain: H2GCN
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
    - 0.731
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSGAN
    model_plain: GraphSGAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1902.08226'
    title: 'Graph Adversarial Training: Dynamically Regularizing Based on Graph Structure'
    date: Feb 2019
    date_iso: 2019-02
    date_display: Feb 2019
    codebase_url: https://github.com/fulifeng/GraphAT
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.731
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GB-GNN KTA
    model_plain: GB-GNN KTA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.731
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Graph-MLP
    model_plain: Graph-MLP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.04051'
    title: 'Graph-MLP: Node Classification without Message Passing in Graph'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.731
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CCA-SSG
    model_plain: CCA-SSG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.04604'
    title: Localized Graph Contrastive Learning
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.731
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.08480'
    title: Eliciting Structural and Semantic Global Knowledge in Unsupervised Graph
      Contrastive Learning
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/kaize0409/S-3-CL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.731
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ARGVA
    model_plain: ARGVA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.02534'
    title: 'MGAE: Masked Autoencoders for Self-Supervised Learning on Graphs'
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.731
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0086
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT + GraphMix
    model_plain: GAT + GraphMix
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7308
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0023
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GREET
    model_plain: GREET
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.16026'
    title: 'MUSE: Multi-View Contrastive Learning for Heterophilic Graphs'
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7308
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0084
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PGD + HAO
    model_plain: PGD + HAO
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.08057'
    title: Understanding and Improving Graph Injection Attack by Promoting Unnoticeability
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/LFhase/GIA-HAO
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7304
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: OFA
    model_plain: OFA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7304
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: JK
    model_plain: JK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1908.05081'
    title: 'AdaGCN: Adaboosting Graph Convolutional Networks into Deep Models'
    date: Aug 2019
    date_iso: 2019-08
    date_display: Aug 2019
    codebase_url: https://github.com/datake/AdaGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7303
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0047
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: BGC (GCond)
    model_plain: BGC (GCond)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.11025'
    title: Backdoor Graph Condensation
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/JiahaoWuGit/BGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7303
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAGE
    model_plain: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.11025'
    title: Backdoor Graph Condensation
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/JiahaoWuGit/BGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7303
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CAT-I-SC
    model_plain: CAT-I-SC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.03147'
    title: Learning Conjoint Attentions for Graph Neural Nets
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7302
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0024
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NodeFormer
    model_plain: NodeFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.13148'
    title: Transformers over Directed Acyclic Graphs
    date: Oct 24, 2022
    date_iso: '2022-10-24'
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.73
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: S^2GC
    model_plain: S^2GC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.00955'
    title: Evaluating Deep Graph Neural Networks
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.73
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DMD-ACMP
    model_plain: DMD-ACMP
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
    - 0.73
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.021
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LGCN_sub
    model_plain: LGCN_sub
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1808.03965'
    title: Large-Scale Learnable Graph Convolutional Networks
    date: Aug 2018
    date_iso: 2018-08
    date_display: Aug 2018
    codebase_url: https://github.com/divelab/lgcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.73
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCA
    model_plain: GCA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: Mar 2025
    date_iso: 2025-03
    date_display: Mar 2025
    codebase_url: https://github.com/Statistical-Deep-Learning/DoG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.73
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GGD
    model_plain: GGD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: Mar 2025
    date_iso: 2025-03
    date_display: Mar 2025
    codebase_url: https://github.com/Statistical-Deep-Learning/DoG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.73
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GMI
    model_plain: GMI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.10698'
    title: Towards Graph Self-Supervised Learning with Contrastive Adjusted Zooming
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.73
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Jo-SRC
    model_plain: Jo-SRC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.73
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LGCN
    model_plain: LGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15097'
    title: 'Policy-GNN: Aggregation Optimization for Graph Neural Networks'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.73
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SUGRL
    model_plain: SUGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.08480'
    title: Eliciting Structural and Semantic Global Knowledge in Unsupervised Graph
      Contrastive Learning
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/kaize0409/S-3-CL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.73
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Shift-GAT
    model_plain: Shift-GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.73
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SPAGAN
    model_plain: SPAGAN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.03464'
    title: 'SPAGAN: Shortest Path Graph Attention Network'
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: https://github.com/ihollywhy/SPAGAN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.73
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: BAGCN
    model_plain: BAGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.02279'
    title: arXiv:2411.02279
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/huangJC0429/label-utilize-GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7296
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0075
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGSR
    model_plain: SGSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7296
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0025
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ScaleGNN_b
    model_plain: ScaleGNN_b
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.15920'
    title: 'ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order
      Neighboring Feature Fusion'
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/lx970414/ScaleGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7295
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN + SSL
    model_plain: GCN + SSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.02380'
    title: Self-supervised Training of Graph Convolutional Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7295
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0062
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LazyGNN
    model_plain: LazyGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.15920'
    title: 'ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order
      Neighboring Feature Fusion'
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/lx970414/ScaleGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7291
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GBP
    model_plain: GBP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.00955'
    title: Evaluating Deep Graph Neural Networks
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.729
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Exphormer
    model_plain: Exphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: Mar 2025
    date_iso: 2025-03
    date_display: Mar 2025
    codebase_url: https://github.com/Statistical-Deep-Learning/DoG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.729
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GMNN
    model_plain: GMNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.12578'
    title: Graph Convolutional Neural Networks with Node Transition Probability-based
      Message Passing and DropNode Regularization
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.729
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SeHGNN
    model_plain: SeHGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.15920'
    title: 'ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order
      Neighboring Feature Fusion'
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/lx970414/ScaleGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.729
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Snowball
    model_plain: Snowball
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.02174'
    title: 'Break the Ceiling: Stronger Multi-scale Deep Graph Convolutional Networks'
    date: Jun 2019
    date_iso: 2019-06
    date_display: Jun 2019
    codebase_url: https://github.com/PwnerHarry/Stronger_GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.728
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: H-GCN
    model_plain: H-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.13009'
    title: 'Iterative Deep Graph Learning for Graph Neural Networks: Better and Robust
      Node Embeddings'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/hugochan/IDGL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.728
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FMLP-S
    model_plain: FMLP-S
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.06631'
    title: Frameless Graph Knowledge Distillation
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: https://github.com/dshi3553usyd/Frameless_Graph_Distillation.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.728
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0122
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GADPN(GCN)
    model_plain: GADPN(GCN)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.08230'
    title: 'GADPN: Graph Adaptive Denoising and Perturbation Networks via Singular
      Value Decomposition'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.728
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CoGSL
    model_plain: CoGSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.02279'
    title: arXiv:2411.02279
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/huangJC0429/label-utilize-GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7279
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0042
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: S2GCN
    model_plain: S2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.15920'
    title: 'ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order
      Neighboring Feature Fusion'
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/lx970414/ScaleGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7278
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HINormer
    model_plain: HINormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.15920'
    title: 'ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order
      Neighboring Feature Fusion'
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/lx970414/ScaleGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7275
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PTDNet-GCN
    model_plain: PTDNet-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.02279'
    title: arXiv:2411.02279
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/huangJC0429/label-utilize-GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7273
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0018
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT + SSL
    model_plain: GAT + SSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.02380'
    title: Self-supervised Training of Graph Convolutional Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7273
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0072
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FAGCN
    model_plain: FAGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.00797'
    title: Beyond Low-frequency Information in Graph Convolutional Networks
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.727
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FMP ode
    model_plain: FMP ode
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.14806'
    title: Framelet Message Passing
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.727
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: UFGConv-S
    model_plain: UFGConv-S
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.06986'
    title: How Framelets Enhance Graph Neural Networks
    date: Feb 13, 2021
    date_iso: '2021-02-13'
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.727
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: UFG
    model_plain: UFG
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.05767'
    title: Dirichlet Energy Enhancement of Graph Neural Networks by Framelet Augmentation
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.727
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE + GAug-M
    model_plain: GraphSAGE + GAug-M
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.727
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: IncepGCN+DropEdge
    model_plain: IncepGCN+DropEdge
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.15454'
    title: 'GPNet: Simplifying Graph Neural Networks via Multi-channel Geometric Polynomials'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.727
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ARIEL
    model_plain: ARIEL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.727
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SimP-GCN
    model_plain: SimP-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.22299'
    title: 'CoATA: Effective Co-Augmentation of Topology and Attribute for Graph Neural
      Networks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7263
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0059
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
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
    - 0.726
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.013
    - null
    - null
    - null
    - null
    - null
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
    - 0.726
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGFormer
    model_plain: SGFormer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.10759'
    title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/qitianwu/SGFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.726
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MVGRL
    model_plain: MVGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.10698'
    title: Towards Graph Self-Supervised Learning with Contrastive Adjusted Zooming
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.726
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: JKNet+DropEdge
    model_plain: JKNet+DropEdge
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.15454'
    title: 'GPNet: Simplifying Graph Neural Networks via Multi-channel Geometric Polynomials'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.726
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN-LPA
    model_plain: GCN-LPA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.02279'
    title: arXiv:2411.02279
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/huangJC0429/label-utilize-GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.726
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TDGIA + HAO
    model_plain: TDGIA + HAO
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.08057'
    title: Understanding and Improving Graph Injection Attack by Promoting Unnoticeability
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/LFhase/GIA-HAO
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7251
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAMLP
    model_plain: GAMLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.15920'
    title: 'ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order
      Neighboring Feature Fusion'
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/lx970414/ScaleGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7251
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCDE-rk2
    model_plain: GCDE-rk2
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.07532'
    title: Graph Neural Ordinary Differential Equations
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.725
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Sel-Cl
    model_plain: Sel-Cl
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.725
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGC Paper
    model_plain: SGC Paper
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.725
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT-ppr
    model_plain: GAT-ppr
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.725
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GLR
    model_plain: GLR
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.725
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ARMA
    model_plain: ARMA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.07295'
    title: Adversarial Graph Disentanglement with Component-specific Aggregation
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/SsGood/ADGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.725
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphHeat
    model_plain: GraphHeat
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2007.16002'
    title: Graph Convolutional Networks using Heat Kernel for Semi-supervised Learning
    date: Jul 2020
    date_iso: 2020-07
    date_display: Jul 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.725
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Shift-GCN
    model_plain: Shift-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.725
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphCL
    model_plain: GraphCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2007.08025'
    title: 'GraphCL: Contrastive Self-Supervised Learning of Graph Representations'
    date: Jul 2020
    date_iso: 2020-07
    date_display: Jul 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.725
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CL
    model_plain: CL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7244
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRCN
    model_plain: GRCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7243
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0061
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NARS
    model_plain: NARS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.15920'
    title: 'ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order
      Neighboring Feature Fusion'
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/lx970414/ScaleGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7241
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7241
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0218
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SIGN
    model_plain: SIGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.00955'
    title: Evaluating Deep Graph Neural Networks
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.724
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPR
    model_plain: GPR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.11264'
    title: 'GraphGLOW: Open-World Graph Structure Learning for Cross-Graph Topology
      Refinement'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/WtaoZhao/GraphGLOW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.724
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GIANT
    model_plain: GIANT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14324'
    title: Large Language Models as Topological Structure Enhancers for Text-Attributed
      Graphs
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/sunshy-1/LLM4GraphTopology
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7238
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0083
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN + DropEdge
    model_plain: GCN + DropEdge
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.12578'
    title: Graph Convolutional Neural Networks with Node Transition Probability-based
      Message Passing and DropNode Regularization
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.723
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SUBLIME
    model_plain: SUBLIME
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.723
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0109
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE + BVAT
    model_plain: GraphSAGE + BVAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7223
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0046
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
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
    - 0.722
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.14806'
    title: Framelet Message Passing
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.722
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: linear Snowball
    model_plain: linear Snowball
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.02174'
    title: 'Break the Ceiling: Stronger Multi-scale Deep Graph Convolutional Networks'
    date: Jun 2019
    date_iso: 2019-06
    date_display: Jun 2019
    codebase_url: https://github.com/PwnerHarry/Stronger_GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.722
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: truncated Krylov
    model_plain: truncated Krylov
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.02174'
    title: 'Break the Ceiling: Stronger Multi-scale Deep Graph Convolutional Networks'
    date: Jun 2019
    date_iso: 2019-06
    date_display: Jun 2019
    codebase_url: https://github.com/PwnerHarry/Stronger_GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.722
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN-VN
    model_plain: GCN-VN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1802.08888'
    title: 'N-GCN: Multi-scale Graph Convolution for Semi-supervised Node Classification'
    date: Feb 2018
    date_iso: 2018-02
    date_display: Feb 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.722
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MixUp
    model_plain: MixUp
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.22299'
    title: 'CoATA: Effective Co-Augmentation of Topology and Attribute for Graph Neural
      Networks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.722
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0095
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: IDGL
    model_plain: IDGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.722
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0118
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FactorGCN
    model_plain: FactorGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.07295'
    title: Adversarial Graph Disentanglement with Component-specific Aggregation
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/SsGood/ADGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.722
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Ada-Ugnn
    model_plain: Ada-Ugnn
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.01777'
    title: A Unified View on Graph Neural Networks as Graph Signal Denoising
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: https://github.com/alge24/ADA-UGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7217
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT + DropEdge
    model_plain: GAT + DropEdge
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7216
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0091
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ENGINE
    model_plain: ENGINE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7215
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.12063'
    title: 'HAT-GAE: Self-Supervised Graph Auto-encoders with Hierarchical Adaptive
      Masking and Trainable Corruption'
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7212
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0029
    - null
    - null
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
    arxiv_id: '1312.6203'
    title: Spectral Networks and Locally Connected Networks on Graphs
    date: Dec 21, 2013
    date_iso: '2013-12-21'
    date_display: Dec 2013
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.721
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.015
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN-Jaccard
    model_plain: GCN-Jaccard
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2005.10203'
    title: Graph Structure Learning for Robust Graph Neural Networks
    date: May 2020
    date_iso: 2020-05
    date_display: May 2020
    codebase_url: https://github.com/ChandlerBang/Pro-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.721
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0063
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GSR
    model_plain: GSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.02279'
    title: arXiv:2411.02279
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/huangJC0429/label-utilize-GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.721
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0025
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCA
    model_plain: GCA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.04604'
    title: Localized Graph Contrastive Learning
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.721
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: JOAO
    model_plain: JOAO
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7209
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0017
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CPGNN
    model_plain: CPGNN
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
    - 0.7206
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TriCL
    model_plain: TriCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7202
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: IDGL-Anch
    model_plain: IDGL-Anch
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.13009'
    title: 'Iterative Deep Graph Learning for Graph Neural Networks: Better and Robust
      Node Embeddings'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/hugochan/IDGL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.72
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Vanilla PPRGo
    model_plain: Vanilla PPRGo
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.14038'
    title: Robustness of Graph Neural Networks at Scale
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.72
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AF-GCL
    model_plain: AF-GCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.04604'
    title: Localized Graph Contrastive Learning
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.72
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN + DHGR
    model_plain: GCN + DHGR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08264'
    title: 'Make Heterophily Graphs Better Fit GNN: A Graph Rewiring Approach'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7196
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0067
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN + DropEdge
    model_plain: GCN + DropEdge
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7193
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0031
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.00797'
    title: Beyond Low-frequency Information in Graph Convolutional Networks
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.719
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGCL
    model_plain: SGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: Mar 2025
    date_iso: 2025-03
    date_display: Mar 2025
    codebase_url: https://github.com/Statistical-Deep-Learning/DoG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.719
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphGLOW_cos
    model_plain: GraphGLOW_cos
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.11264'
    title: 'GraphGLOW: Open-World Graph Structure Learning for Cross-Graph Topology
      Refinement'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/WtaoZhao/GraphGLOW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.719
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GATNE
    model_plain: GATNE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.12063'
    title: 'HAT-GAE: Self-Supervised Graph Auto-encoders with Hierarchical Adaptive
      Masking and Trainable Corruption'
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.719
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0022
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SUGRL
    model_plain: SUGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7189
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0025
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SelfTask-GNN
    model_plain: SelfTask-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.02534'
    title: 'MGAE: Masked Autoencoders for Self-Supervised Learning on Graphs'
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7182
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0013
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ChebNet
    model_plain: ChebNet
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
    - 0.718
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.016
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GDE
    model_plain: GDE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.09443'
    title: Beltrami Flow and Neural Diffusion on Graphs
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: https://github.com/twitter-research/graph-neural-pde
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.718
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GIB-Bern
    model_plain: GIB-Bern
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.12811'
    title: Graph Information Bottleneck
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.718
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0503
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.15454'
    title: 'GPNet: Simplifying Graph Neural Networks via Multi-channel Geometric Polynomials'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.718
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.718
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGI Paper
    model_plain: DGI Paper
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.718
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TriCL-GM
    model_plain: TriCL-GM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7173
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN-BBGDC
    model_plain: GCN-BBGDC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.04064'
    title: Bayesian Graph Neural Networks with Adaptive Connection Sampling
    date: Jun 7, 2020
    date_iso: '2020-06-07'
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7172
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0048
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GWNN
    model_plain: GWNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.00797'
    title: Beyond Low-frequency Information in Graph Convolutional Networks
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.717
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FMP mlp
    model_plain: FMP mlp
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.14806'
    title: Framelet Message Passing
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.717
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphGLOW_dp
    model_plain: GraphGLOW_dp
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.11264'
    title: 'GraphGLOW: Open-World Graph Structure Learning for Cross-Graph Topology
      Refinement'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/WtaoZhao/GraphGLOW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.717
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRACE
    model_plain: GRACE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.10698'
    title: Towards Graph Self-Supervised Learning with Contrastive Adjusted Zooming
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.717
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Scattering GCN
    model_plain: Scattering GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.08414'
    title: 'Scattering GCN: Overcoming Oversmoothness in Graph Convolutional Networks'
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: http://github.com/dms-net/scatteringGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.717
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CNNs
    model_plain: CNNs
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.11689'
    title: Self-Supervised Graph Representation Learning via Topology Transformations
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/gyshgx868/topo-ter
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.717
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LLMs through graph neural networks
    model_plain: LLMs through graph neural networks
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08785'
    title: 'InstructGraph: Boosting Large Language Models via Graph-centric Instruction
      Tuning and Preference Alignment'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/wjn1996/InstructGraph
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7165
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN + Vanilla
    model_plain: GCN + Vanilla
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7164
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0031
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GS-mean
    model_plain: GS-mean
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.05868'
    title: Pitfalls of Graph Neural Network Evaluation
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.716
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.019
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LoopyNet
    model_plain: LoopyNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2001.05140'
    title: 'Graph-Bert: Only Attention is Needed for Learning Graph Representations'
    date: Jan 2020
    date_iso: 2020-01
    date_display: Jan 2020
    codebase_url: https://github.com/jwzhanggy/Graph-Bert
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.716
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CPGNN
    model_plain: CPGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.10759'
    title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/qitianwu/SGFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.716
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT + GAug-M
    model_plain: GAT + GAug-M
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.716
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: BGRL
    model_plain: BGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.08792'
    title: Unifying Graph Contrastive Learning with Flexible Contextual Scopes
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: https://github.com/zyzisastudyreallyhardguy/UGCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.716
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: APPNP + DHGR
    model_plain: APPNP + DHGR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08264'
    title: 'Make Heterophily Graphs Better Fit GNN: A Graph Rewiring Approach'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.716
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0035
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAuG-O
    model_plain: GAuG-O
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.716
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: N.S.-GCN
    model_plain: N.S.-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.02279'
    title: arXiv:2411.02279
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/huangJC0429/label-utilize-GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7155
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Logistic Reg.-X
    model_plain: Logistic Reg.-X
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7154
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphGLOW_knn
    model_plain: GraphGLOW_knn
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.11264'
    title: 'GraphGLOW: Open-World Graph Structure Learning for Cross-Graph Topology
      Refinement'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/WtaoZhao/GraphGLOW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.715
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TAGCN DGL PyTorch
    model_plain: TAGCN DGL PyTorch
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.715
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: APPNP DGL PyTorch
    model_plain: APPNP DGL PyTorch
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.715
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GADPN(SAGE)
    model_plain: GADPN(SAGE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.08230'
    title: 'GADPN: Graph Adaptive Denoising and Perturbation Networks via Singular
      Value Decomposition'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.715
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Pro-GNN
    model_plain: Pro-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.00064'
    title: 'SPGCL: Simple yet Powerful Graph Contrastive Learning via SVD-Guided Structural
      Perturbation'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.715
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRACE + PiNGDA
    model_plain: GRACE + PiNGDA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7147
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE + DropEdge
    model_plain: GraphSAGE + DropEdge
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7146
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0057
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN-BBDE
    model_plain: GCN-BBDE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.04064'
    title: Bayesian Graph Neural Networks with Adaptive Connection Sampling
    date: Jun 7, 2020
    date_iso: '2020-06-07'
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7146
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0055
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NWR-GAE full
    model_plain: NWR-GAE full
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.09025'
    title: Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/mtang724/NWR-GAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7145
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0241
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NWR-GAE
    model_plain: NWR-GAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.16026'
    title: 'MUSE: Multi-View Contrastive Learning for Heterophilic Graphs'
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7145
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0241
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE-pool
    model_plain: GraphSAGE-pool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.09532'
    title: Pseudo Contrastive Learning for Graph-based Semi-supervised Learning
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7144
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0134
    - null
    - null
    - null
    - null
    - null
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
    - 0.714
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.026
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN-K
    model_plain: GCN-K
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.12055'
    title: Towards Self-Explainable Graph Neural Network
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/EnyanDai/SEGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.714
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MixHop-learn
    model_plain: MixHop-learn
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.15454'
    title: 'GPNet: Simplifying Graph Neural Networks via Multi-channel Geometric Polynomials'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.714
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GB-GNN-II
    model_plain: GB-GNN-II
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.714
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TAGCN Paper
    model_plain: TAGCN Paper
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.714
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.03147'
    title: Learning Conjoint Attentions for Graph Neural Nets
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.714
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MixHop
    model_plain: MixHop
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.11689'
    title: Self-Supervised Graph Representation Learning via Topology Transformations
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/gyshgx868/topo-ter
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.714
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.11689'
    title: Self-Supervised Graph Representation Learning via Topology Transformations
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/gyshgx868/topo-ter
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.714
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GMI
    model_plain: GMI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.11689'
    title: Self-Supervised Graph Representation Learning via Topology Transformations
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/gyshgx868/topo-ter
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.714
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AGE
    model_plain: AGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.00219'
    title: 'Grain: Improving Data Efficiency of Graph Neural Networks via Diversified
      Influence Maximization'
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/zwt233/Grain
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.714
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TED-GCN
    model_plain: TED-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.714
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRACEIS
    model_plain: GRACEIS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.714
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0053
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PolyGCL
    model_plain: PolyGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7138
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0021
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT + Vanilla
    model_plain: GAT + Vanilla
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7137
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0093
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Simple-HGN
    model_plain: Simple-HGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.15920'
    title: 'ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order
      Neighboring Feature Fusion'
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/lx970414/ScaleGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7134
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NodeFormer
    model_plain: NodeFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.02279'
    title: arXiv:2411.02279
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/huangJC0429/label-utilize-GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7131
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0098
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AP-GCN
    model_plain: AP-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.00955'
    title: Evaluating Deep Graph Neural Networks
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.713
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN-DVAT
    model_plain: GCN-DVAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.02174'
    title: 'Break the Ceiling: Stronger Multi-scale Deep Graph Convolutional Networks'
    date: Jun 2019
    date_iso: 2019-06
    date_display: Jun 2019
    codebase_url: https://github.com/PwnerHarry/Stronger_GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.713
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphGLOW_at
    model_plain: GraphGLOW_at
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.11264'
    title: 'GraphGLOW: Open-World Graph Structure Learning for Cross-Graph Topology
      Refinement'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/WtaoZhao/GraphGLOW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.713
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
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
    arxiv_id: '2206.08583'
    title: arXiv:2206.08583
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/PKU-DAIR/NAFS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.713
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GB-GNN SAMME.R
    model_plain: GB-GNN SAMME.R
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.713
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.013
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GB-GNN SAMME.R + Fine Tuning
    model_plain: GB-GNN SAMME.R + Fine Tuning
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.713
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: APPNP DGL MXNet
    model_plain: APPNP DGL MXNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.713
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Random
    model_plain: Random
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.05057'
    title: Towards More Practical Adversarial Attacks on Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/Mark12Ding/GNN-Practical-Attack
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.713
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GARNET
    model_plain: GARNET
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15792'
    title: 'IDEA: Invariant Defense for Graph Adversarial Robustness'
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.713
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.08230'
    title: 'GADPN: Graph Adaptive Denoising and Perturbation Networks via Singular
      Value Decomposition'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.713
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MetaGIA + HAO
    model_plain: MetaGIA + HAO
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.08057'
    title: Understanding and Improving Graph Injection Attack by Promoting Unnoticeability
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/LFhase/GIA-HAO
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7125
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Cluster-GCN
    model_plain: Cluster-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.15920'
    title: 'ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order
      Neighboring Feature Fusion'
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/lx970414/ScaleGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7125
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AGIA + HAO
    model_plain: AGIA + HAO
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.08057'
    title: Understanding and Improving Graph Injection Attack by Promoting Unnoticeability
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/LFhase/GIA-HAO
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7122
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MGNN
    model_plain: MGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.15920'
    title: 'ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order
      Neighboring Feature Fusion'
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/lx970414/ScaleGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7122
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GLNN
    model_plain: GLNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2208.10010'
    title: 'NOSMOG: Learning Noise-robust and Structure-aware MLPs on Graphs'
    date: Aug 2022
    date_iso: 2022-08
    date_display: Aug 2022
    codebase_url: https://github.com/meettyj/NOSMOG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7122
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.015
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ChebNet + PCL
    model_plain: ChebNet + PCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.09532'
    title: Pseudo Contrastive Learning for Graph-based Semi-supervised Learning
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7121
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0134
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MoNet
    model_plain: MoNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.05868'
    title: Pitfalls of Graph Neural Network Evaluation
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.712
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.02
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Graph-Bert
    model_plain: Graph-Bert
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2001.05140'
    title: 'Graph-Bert: Only Attention is Needed for Learning Graph Representations'
    date: Jan 2020
    date_iso: 2020-01
    date_display: Jan 2020
    codebase_url: https://github.com/jwzhanggy/Graph-Bert
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.712
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Intersection
    model_plain: Intersection
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.02174'
    title: 'Break the Ceiling: Stronger Multi-scale Deep Graph Convolutional Networks'
    date: Jun 2019
    date_iso: 2019-06
    date_display: Jun 2019
    codebase_url: https://github.com/PwnerHarry/Stronger_GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.712
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: RGCN
    model_plain: RGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2005.10203'
    title: Graph Structure Learning for Robust Graph Neural Networks
    date: May 2020
    date_iso: 2020-05
    date_display: May 2020
    codebase_url: https://github.com/ChandlerBang/Pro-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.712
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0083
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCA
    model_plain: GCA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.08792'
    title: Unifying Graph Contrastive Learning with Flexible Contextual Scopes
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: https://github.com/zyzisastudyreallyhardguy/UGCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.712
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Soft Median PPRGo
    model_plain: Soft Median PPRGo
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.14038'
    title: Robustness of Graph Neural Networks at Scale
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.712
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1710.10321'
    title: arXiv:1710.10321
    date: Oct 2017
    date_iso: 2017-10
    date_display: Oct 2017
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.712
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.019
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Partially absorbing
    model_plain: Partially absorbing
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.08414'
    title: 'Scattering GCN: Overcoming Oversmoothness in Graph Convolutional Networks'
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: http://github.com/dms-net/scatteringGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.712
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PCNet
    model_plain: PCNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.712
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DNNs
    model_plain: DNNs
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.09755'
    title: Finding Heterophilic Neighbors via Confidence-based Subgraph Matching for
      Semi-supervised Node Classification
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.712
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PSAGNN
    model_plain: PSAGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.22299'
    title: 'CoATA: Effective Co-Augmentation of Topology and Attribute for Graph Neural
      Networks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7118
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0032
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT-k-Lap
    model_plain: GAT-k-Lap
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.03147'
    title: Learning Conjoint Attentions for Graph Neural Nets
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7118
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0052
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GLEM-GNN
    model_plain: GLEM-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7116
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MUSE
    model_plain: MUSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.16026'
    title: 'MUSE: Multi-View Contrastive Learning for Heterophilic Graphs'
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7114
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LDS
    model_plain: LDS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.00064'
    title: 'SPGCL: Simple yet Powerful Graph Contrastive Learning via SVD-Guided Structural
      Perturbation'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7112
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE + DHGR
    model_plain: GraphSAGE + DHGR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08264'
    title: 'Make Heterophily Graphs Better Fit GNN: A Graph Rewiring Approach'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7111
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0065
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DCNN (our implementation)
    model_plain: DCNN (our implementation)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1802.08888'
    title: 'N-GCN: Multi-scale Graph Convolution for Semi-supervised Node Classification'
    date: Feb 2018
    date_iso: 2018-02
    date_display: Feb 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.711
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HAN
    model_plain: HAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.15920'
    title: 'ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order
      Neighboring Feature Fusion'
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/lx970414/ScaleGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.711
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE DGL PyTorch
    model_plain: GraphSAGE DGL PyTorch
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.711
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AERO-GNN
    model_plain: AERO-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.711
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE + Vanilla
    model_plain: GraphSAGE + Vanilla
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7109
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0059
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Framelets
    model_plain: Framelets
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
    - 0.71
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Self-training
    model_plain: Self-training
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.02174'
    title: 'Break the Ceiling: Stronger Multi-scale Deep Graph Convolutional Networks'
    date: Jun 2019
    date_iso: 2019-06
    date_display: Jun 2019
    codebase_url: https://github.com/PwnerHarry/Stronger_GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.71
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DW
    model_plain: DW
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1805.07984'
    title: Adversarial Attacks on Neural Networks for Graph Data
    date: May 2018
    date_iso: 2018-05
    date_display: May 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.71
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRAPHITE
    model_plain: GRAPHITE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1803.10459'
    title: 'Graphite: Iterative Generative Modeling of Graphs'
    date: Mar 28, 2018
    date_iso: '2018-03-28'
    date_display: Mar 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.71
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NS-SAGE
    model_plain: NS-SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1802.08888'
    title: 'N-GCN: Multi-scale Graph Convolution for Semi-supervised Node Classification'
    date: Feb 2018
    date_iso: 2018-02
    date_display: Feb 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.71
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LLaGA
    model_plain: LLaGA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.04894'
    title: Adversarial Attacks and Defenses on Graph-aware Large Language Models (LLMs)
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.71
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.04
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: KCG
    model_plain: KCG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.00219'
    title: 'Grain: Improving Data Efficiency of Graph Neural Networks via Diversified
      Influence Maximization'
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/zwt233/Grain
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.71
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: EP-B
    model_plain: EP-B
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2007.08025'
    title: 'GraphCL: Contrastive Self-Supervised Learning of Graph Representations'
    date: Jul 2020
    date_iso: 2020-07
    date_display: Jul 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.71
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT-NetMF
    model_plain: GAT-NetMF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.03147'
    title: Learning Conjoint Attentions for Graph Neural Nets
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7094
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0016
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Variance Reduction
    model_plain: Variance Reduction
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1901.08150'
    title: Hypergraph Convolution and Hypergraph Attention
    date: Jan 2019
    date_iso: 2019-01
    date_display: Jan 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.709
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGC DGL
    model_plain: SGC DGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.709
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN DGL TensorFlow
    model_plain: GCN DGL TensorFlow
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.709
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT DGL PyTorch
    model_plain: GAT DGL PyTorch
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.709
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DropEdge
    model_plain: DropEdge
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.00064'
    title: 'SPGCL: Simple yet Powerful Graph Contrastive Learning via SVD-Guided Structural
      Perturbation'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.709
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CDC
    model_plain: CDC
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.03670'
    title: 'CDC: A Simple Framework for Complex Data Clustering This work was supported
      by the National Natural Science Foundation of China Grant 62276053. Corresponding
      author: Erlin Pan Z. Kang, X. Xie, B. Li, E. Pan are with the School of Computer
      Science and Engineering, University of Electronic Science and Technology of
      China, Chengdu, China (e-mail: zkang@uestc.edu.cn; x624361380@outlook.com; bingheng86,
      wujisixsix6@gmail.com).'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.709
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Degree
    model_plain: Degree
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.00219'
    title: 'Grain: Improving Data Efficiency of Graph Neural Networks via Diversified
      Influence Maximization'
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/zwt233/Grain
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.709
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Auto-HeG
    model_plain: Auto-HeG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.709
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Hyper-Atten.
    model_plain: Hyper-Atten.
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1901.08150'
    title: Hypergraph Convolution and Hypergraph Attention
    date: Jan 2019
    date_iso: 2019-01
    date_display: Jan 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7088
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRAND
    model_plain: GRAND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.14806'
    title: Framelet Message Passing
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.708
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ResGCN
    model_plain: ResGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.00955'
    title: Evaluating Deep Graph Neural Networks
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.708
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: C&S
    model_plain: C&S
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.08583'
    title: arXiv:2206.08583
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/PKU-DAIR/NAFS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.708
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GB-GNN Adj. + Fine Tuning
    model_plain: GB-GNN Adj. + Fine Tuning
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.708
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GB-GNN KTA + Fine Tuning
    model_plain: GB-GNN KTA + Fine Tuning
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.708
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GB-GNN-II + Fine Tuning L=1
    model_plain: GB-GNN-II + Fine Tuning L=1
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.708
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GB-GNN KTA + FT
    model_plain: GB-GNN KTA + FT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.708
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GB-GNN II + FT
    model_plain: GB-GNN II + FT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.708
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Random
    model_plain: Random
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.00219'
    title: 'Grain: Improving Data Efficiency of Graph Neural Networks via Diversified
      Influence Maximization'
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/zwt233/Grain
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.708
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.07754'
    title: On the Robustness of Graph Neural Diffusion to Topology Perturbations
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/zknus/Robustness-of-Graph-Neural-Diffusion
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7075
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0086
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGFormer
    model_plain: SGFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.07256'
    title: 'Graph homophily booster: Reimagining the role of discrete features in
      heterophilic graph learning'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/q-rz/ICLR26-GRAPHITE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7074
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0125
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN-DO-DE
    model_plain: GCN-DO-DE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.04064'
    title: Bayesian Graph Neural Networks with Adaptive Connection Sampling
    date: Jun 7, 2020
    date_iso: '2020-06-07'
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7074
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0123
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: RobustGCN
    model_plain: RobustGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.07754'
    title: On the Robustness of Graph Neural Diffusion to Topology Perturbations
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/zknus/Robustness-of-Graph-Neural-Diffusion
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7072
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0115
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: JK-Net
    model_plain: JK-Net
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.00955'
    title: Evaluating Deep Graph Neural Networks
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.707
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN-SVAT
    model_plain: GCN-SVAT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.02174'
    title: 'Break the Ceiling: Stronger Multi-scale Deep Graph Convolutional Networks'
    date: Jun 2019
    date_iso: 2019-06
    date_display: Jun 2019
    codebase_url: https://github.com/PwnerHarry/Stronger_GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.707
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ESC-GNN
    model_plain: ESC-GNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.707
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.017
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GZoom(DGI, l=2)
    model_plain: GZoom(DGI, l=2)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.707
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GB-GNN Adj. + FT
    model_plain: GB-GNN Adj. + FT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.707
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: N-GCN_a
    model_plain: N-GCN_a
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.08676'
    title: 'Redesigning graph filter-based GNNs to relax the homophily assumption
      This work was supported in part by the Spanish AEI Grants PID2022-136887NB-I00,
      PID2023-149457OB-I00, FPU20/05554, the Community of Madrid (Madrid ELLIS Unit),
      and the NSF under award CCF-2340481. Research was sponsored by the Army Research
      Office and was accomplished under Grant Number W911NF-17-S-0002. The views and
      conclusions contained in this document are those of the authors and should not
      be interpreted as representing the official policies, either expressed or implied,
      of the Army Research Office or the U.S. Army or the U.S. Government. The U.S.
      Government is authorized to reproduce and distribute reprints for Government
      purposes notwithstanding any copyright notation herein. Emails: samuel.rey.escudero@urjc.es,
      nav@rice.edu, victor.tenorio@urjc.es, segarra@rice.edu, antonio.garcia.marques@urjc.es'
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/reysam93/adaptive_agg_gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.707
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN-SVD
    model_plain: GCN-SVD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2005.10203'
    title: Graph Structure Learning for Robust Graph Neural Networks
    date: May 2020
    date_iso: 2020-05
    date_display: May 2020
    codebase_url: https://github.com/ChandlerBang/Pro-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7065
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0032
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PGCN_n
    model_plain: PGCN_n
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.12578'
    title: Graph Convolutional Neural Networks with Node Transition Probability-based
      Message Passing and DropNode Regularization
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.706
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: UnionNET
    model_plain: UnionNET
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.706
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GATv2
    model_plain: GATv2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.08230'
    title: 'GADPN: Graph Adaptive Denoising and Perturbation Networks via Singular
      Value Decomposition'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.706
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ANRMAB
    model_plain: ANRMAB
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.00219'
    title: 'Grain: Improving Data Efficiency of Graph Neural Networks via Diversified
      Influence Maximization'
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/zwt233/Grain
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.706
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HetGNN
    model_plain: HetGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.15920'
    title: 'ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order
      Neighboring Feature Fusion'
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/lx970414/ScaleGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7055
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN-DE
    model_plain: GCN-DE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.04064'
    title: Bayesian Graph Neural Networks with Adaptive Connection Sampling
    date: Jun 7, 2020
    date_iso: '2020-06-07'
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7052
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0075
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: M3S
    model_plain: M3S
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.02174'
    title: 'Break the Ceiling: Stronger Multi-scale Deep Graph Convolutional Networks'
    date: Jun 2019
    date_iso: 2019-06
    date_display: Jun 2019
    codebase_url: https://github.com/PwnerHarry/Stronger_GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.705
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GloGNN
    model_plain: GloGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.705
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.019
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Soft Median GDC
    model_plain: Soft Median GDC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.14038'
    title: Robustness of Graph Neural Networks at Scale
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.705
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Soft Medoid GDC
    model_plain: Soft Medoid GDC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.14038'
    title: Robustness of Graph Neural Networks at Scale
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.705
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCE
    model_plain: GCE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.705
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GB-GNN Adj.
    model_plain: GB-GNN Adj.
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.705
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAGE
    model_plain: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2208.10010'
    title: 'NOSMOG: Learning Noise-robust and Structure-aware MLPs on Graphs'
    date: Aug 2022
    date_iso: 2022-08
    date_display: Aug 2022
    codebase_url: https://github.com/meettyj/NOSMOG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7049
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: APPNP vanilla
    model_plain: APPNP vanilla
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08264'
    title: 'Make Heterophily Graphs Better Fit GNN: A Graph Rewiring Approach'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7046
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0031
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DoG (GCN)
    model_plain: DoG (GCN)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.04064'
    title: Bayesian Graph Neural Networks with Adaptive Connection Sampling
    date: Jun 7, 2020
    date_iso: '2020-06-07'
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7044
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0039
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT + DHGR
    model_plain: GAT + DHGR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08264'
    title: 'Make Heterophily Graphs Better Fit GNN: A Graph Rewiring Approach'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7043
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0065
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Beltrami
    model_plain: Beltrami
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.07754'
    title: On the Robustness of Graph Neural Diffusion to Topology Perturbations
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/zknus/Robustness-of-Graph-Neural-Diffusion
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7041
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0138
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: EGNN
    model_plain: EGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.05767'
    title: Dirichlet Energy Enhancement of Graph Neural Networks by Framelet Augmentation
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.704
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.028
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GZoom_F+MILE(DW)
    model_plain: GZoom_F+MILE(DW)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.704
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAM
    model_plain: GAM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.09755'
    title: Finding Heterophilic Neighbors via Confidence-based Subgraph Matching for
      Semi-supervised Node Classification
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.704
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.03147'
    title: Learning Conjoint Attentions for Graph Neural Nets
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7036
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0042
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Hyper-Conv.
    model_plain: Hyper-Conv.
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1901.08150'
    title: Hypergraph Convolution and Hypergraph Attention
    date: Jan 2019
    date_iso: 2019-01
    date_display: Jan 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7035
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.02907'
    title: Semi-Supervised Classification with Graph Convolutional Networks
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/tkipf/gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.703
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Renormalization trick
    model_plain: Renormalization trick
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.02907'
    title: Semi-Supervised Classification with Graph Convolutional Networks
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/tkipf/gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.703
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FAGCN
    model_plain: FAGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.703
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.016
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN Paper
    model_plain: GCN Paper
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.703
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MVGRL
    model_plain: MVGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.03670'
    title: 'CDC: A Simple Framework for Complex Data Clustering This work was supported
      by the National Natural Science Foundation of China Grant 62276053. Corresponding
      author: Erlin Pan Z. Kang, X. Xie, B. Li, E. Pan are with the School of Computer
      Science and Engineering, University of Electronic Science and Technology of
      China, Chengdu, China (e-mail: zkang@uestc.edu.cn; x624361380@outlook.com; bingheng86,
      wujisixsix6@gmail.com).'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.703
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: BGC (DC-Graph)
    model_plain: BGC (DC-Graph)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.11025'
    title: Backdoor Graph Condensation
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/JiahaoWuGit/BGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7027
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SUGRL
    model_plain: SUGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7026
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN-BBGDC-ARM
    model_plain: GCN-BBGDC-ARM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.04064'
    title: Bayesian Graph Neural Networks with Adaptive Connection Sampling
    date: Jun 7, 2020
    date_iso: '2020-06-07'
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7025
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GOUDA
    model_plain: GOUDA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7025
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: GraphTrans_UltrasSmall
    model_plain: GraphTrans_UltrasSmall
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.10759'
    title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/qitianwu/SGFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.702
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN DGL PyTorch
    model_plain: GCN DGL PyTorch
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.702
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TAGCN DGL MXNet
    model_plain: TAGCN DGL MXNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.702
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGI DGL TensorFlow
    model_plain: DGI DGL TensorFlow
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.702
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
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
    arxiv_id: '2602.00064'
    title: 'SPGCL: Simple yet Powerful Graph Contrastive Learning via SVD-Guided Structural
      Perturbation'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.702
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SNAG
    model_plain: SNAG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.12357'
    title: 'Auto-HeG: Automated Graph Neural Network on Heterophilic Graphs'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.024
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HANet
    model_plain: HANet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1907.04786'
    title: Fast Haar Transforms for Graph Neural Networks
    date: Jul 2019
    date_iso: 2019-07
    date_display: Jul 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.701
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NGNN
    model_plain: NGNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.04714'
    title: 'NRGNN: Learning a Label Noise-Resistant Graph Neural Network on Sparsely
      and Noisily Labeled Graphs'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/EnyanDai/NRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.701
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.013
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Pagerank
    model_plain: Pagerank
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.05057'
    title: Towards More Practical Adversarial Attacks on Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/Mark12Ding/GNN-Practical-Attack
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.701
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GNNGuard
    model_plain: GNNGuard
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.00012'
    title: 'Reliable Representations Make A Stronger Defender: Unsupervised Structure
      Refinement for Robust GNN'
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: https://github.com/likuanppd/STABLE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7007
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: Diffusion-A
    model_plain: Diffusion-A
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.015
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphPrompt
    model_plain: GraphPrompt
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.04894'
    title: Adversarial Attacks and Defenses on Graph-aware Large Language Models (LLMs)
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.03
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ARMA
    model_plain: ARMA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.03147'
    title: Learning Conjoint Attentions for Graph Neural Nets
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0066
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN + Vanilla
    model_plain: GCN + Vanilla
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.14038'
    title: Robustness of Graph Neural Networks at Scale
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.699
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: BeltramiGuard
    model_plain: BeltramiGuard
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.07754'
    title: On the Robustness of Graph Neural Diffusion to Topology Perturbations
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/zknus/Robustness-of-Graph-Neural-Diffusion
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.699
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0044
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE DGL MXNet
    model_plain: GraphSAGE DGL MXNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.699
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: RWCS
    model_plain: RWCS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.05057'
    title: Towards More Practical Adversarial Attacks on Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/Mark12Ding/GNN-Practical-Attack
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.699
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.08230'
    title: 'GADPN: Graph Adaptive Denoising and Perturbation Networks via Singular
      Value Decomposition'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.699
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AAGCN-N_H
    model_plain: AAGCN-N_H
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.08676'
    title: 'Redesigning graph filter-based GNNs to relax the homophily assumption
      This work was supported in part by the Spanish AEI Grants PID2022-136887NB-I00,
      PID2023-149457OB-I00, FPU20/05554, the Community of Madrid (Madrid ELLIS Unit),
      and the NSF under award CCF-2340481. Research was sponsored by the Army Research
      Office and was accomplished under Grant Number W911NF-17-S-0002. The views and
      conclusions contained in this document are those of the authors and should not
      be interpreted as representing the official policies, either expressed or implied,
      of the Army Research Office or the U.S. Army or the U.S. Government. The U.S.
      Government is authorized to reproduce and distribute reprints for Government
      purposes notwithstanding any copyright notation herein. Emails: samuel.rey.escudero@urjc.es,
      nav@rice.edu, victor.tenorio@urjc.es, segarra@rice.edu, antonio.garcia.marques@urjc.es'
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/reysam93/adaptive_agg_gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.699
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
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
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6984
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Virtual Node
    model_plain: Virtual Node
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.07256'
    title: 'Graph homophily booster: Reimagining the role of discrete features in
      heterophilic graph learning'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/q-rz/ICLR26-GRAPHITE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.698
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0689
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Chebyshev
    model_plain: Chebyshev
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1808.03965'
    title: Large-Scale Learnable Graph Convolutional Networks
    date: Aug 2018
    date_iso: 2018-08
    date_display: Aug 2018
    codebase_url: https://github.com/divelab/lgcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.698
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGCNN
    model_plain: DGCNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.12578'
    title: Graph Convolutional Neural Networks with Node Transition Probability-based
      Message Passing and DropNode Regularization
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.698
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: JK-Net
    model_plain: JK-Net
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.15454'
    title: 'GPNet: Simplifying Graph Neural Networks via Multi-channel Geometric Polynomials'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.698
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ChebNet
    model_plain: ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2007.16002'
    title: Graph Convolutional Networks using Heat Kernel for Semi-supervised Learning
    date: Jul 2020
    date_iso: 2020-07
    date_display: Jul 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.698
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CCGC
    model_plain: CCGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.03670'
    title: 'CDC: A Simple Framework for Complex Data Clustering This work was supported
      by the National Natural Science Foundation of China Grant 62276053. Corresponding
      author: Erlin Pan Z. Kang, X. Xie, B. Li, E. Pan are with the School of Computer
      Science and Engineering, University of Electronic Science and Technology of
      China, Chengdu, China (e-mail: zkang@uestc.edu.cn; x624361380@outlook.com; bingheng86,
      wujisixsix6@gmail.com).'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.698
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FB-GCN-N_A
    model_plain: FB-GCN-N_A
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.08676'
    title: 'Redesigning graph filter-based GNNs to relax the homophily assumption
      This work was supported in part by the Spanish AEI Grants PID2022-136887NB-I00,
      PID2023-149457OB-I00, FPU20/05554, the Community of Madrid (Madrid ELLIS Unit),
      and the NSF under award CCF-2340481. Research was sponsored by the Army Research
      Office and was accomplished under Grant Number W911NF-17-S-0002. The views and
      conclusions contained in this document are those of the authors and should not
      be interpreted as representing the official policies, either expressed or implied,
      of the Army Research Office or the U.S. Army or the U.S. Government. The U.S.
      Government is authorized to reproduce and distribute reprints for Government
      purposes notwithstanding any copyright notation herein. Emails: samuel.rey.escudero@urjc.es,
      nav@rice.edu, victor.tenorio@urjc.es, segarra@rice.edu, antonio.garcia.marques@urjc.es'
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/reysam93/adaptive_agg_gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.698
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Heat+
    model_plain: Heat+
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.07754'
    title: On the Robustness of Graph Neural Diffusion to Topology Perturbations
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/zknus/Robustness-of-Graph-Neural-Diffusion
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6978
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0095
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NeuralSparse
    model_plain: NeuralSparse
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.697
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.018
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN-LPA
    model_plain: GCN-LPA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.697
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.017
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GEN
    model_plain: GEN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.697
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.016
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GOAL
    model_plain: GOAL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.697
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.02
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN + AdaEdge
    model_plain: GCN + AdaEdge
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.697
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT-Deep
    model_plain: GAT-Deep
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.03147'
    title: Learning Conjoint Attentions for Graph Neural Nets
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.697
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0057
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE + GraphMix
    model_plain: GraphSAGE + GraphMix
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6962
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0036
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Chebyshev filter (K=3)
    model_plain: Chebyshev filter (K=3)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.02907'
    title: Semi-Supervised Classification with Graph Convolutional Networks
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/tkipf/gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.696
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
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
    arxiv_id: '1906.02174'
    title: 'Break the Ceiling: Stronger Multi-scale Deep Graph Convolutional Networks'
    date: Jun 2019
    date_iso: 2019-06
    date_display: Jun 2019
    codebase_url: https://github.com/PwnerHarry/Stronger_GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.696
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPR-GNN
    model_plain: GPR-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.696
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.017
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT + Vanilla
    model_plain: GAT + Vanilla
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08264'
    title: 'Make Heterophily Graphs Better Fit GNN: A Graph Rewiring Approach'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.696
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0063
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: JacobiConv
    model_plain: JacobiConv
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.696
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphAdapter
    model_plain: GraphAdapter
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6957
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LM
    model_plain: LM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6951
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GASSL
    model_plain: GASSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6951
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0084
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphTrans (small)
    model_plain: GraphTrans (small)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.10759'
    title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/qitianwu/SGFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.695
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGCL
    model_plain: SGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.695
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0082
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ChebNet
    model_plain: ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.11430'
    title: Independence Promoted Graph Disentangled Networks
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.695
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DFCN
    model_plain: DFCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.09600'
    title: Deep Fusion Clustering Network
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/WxTu/DFCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.695
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Ortho-GCN
    model_plain: Ortho-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.695
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN-BDE-ARM
    model_plain: GCN-BDE-ARM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.04064'
    title: Bayesian Graph Neural Networks with Adaptive Connection Sampling
    date: Jun 7, 2020
    date_iso: '2020-06-07'
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6943
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0045
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ACMGCN
    model_plain: ACMGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.694
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.017
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE + AdaEdge
    model_plain: GraphSAGE + AdaEdge
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.694
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGI DGL PyTorch
    model_plain: DGI DGL PyTorch
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.694
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DAGNN
    model_plain: DAGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.08230'
    title: 'GADPN: Graph Adaptive Denoising and Perturbation Networks via Singular
      Value Decomposition'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.694
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PTDNet
    model_plain: PTDNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.09755'
    title: Finding Heterophilic Neighbors via Confidence-based Subgraph Matching for
      Semi-supervised Node Classification
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.694
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Single parameter
    model_plain: Single parameter
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.02907'
    title: Semi-Supervised Classification with Graph Convolutional Networks
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/tkipf/gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.693
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Cheby
    model_plain: Cheby
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.02174'
    title: 'Break the Ceiling: Stronger Multi-scale Deep Graph Convolutional Networks'
    date: Jun 2019
    date_iso: 2019-06
    date_display: Jun 2019
    codebase_url: https://github.com/PwnerHarry/Stronger_GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.693
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
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
    arxiv_id: '1902.08226'
    title: 'Graph Adversarial Training: Dynamically Regularizing Based on Graph Structure'
    date: Feb 2019
    date_iso: 2019-02
    date_display: Feb 2019
    codebase_url: https://github.com/fulifeng/GraphAT
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.693
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DisenGCN
    model_plain: DisenGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.692
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.017
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: KP-GIN
    model_plain: KP-GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.12055'
    title: Towards Self-Explainable Graph Neural Network
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/EnyanDai/SEGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.692
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GMI
    model_plain: GMI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6911
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0107
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ICA
    model_plain: ICA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.02907'
    title: Semi-Supervised Classification with Graph Convolutional Networks
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/tkipf/gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.691
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: VEPM
    model_plain: VEPM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.691
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.019
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT + AdaEdge
    model_plain: GAT + AdaEdge
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.14082'
    title: Metropolis-Hastings Data Augmentation for Graph Neural Networks
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.691
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Iterative Classification Algorithm
    model_plain: Iterative Classification Algorithm
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1901.08150'
    title: Hypergraph Convolution and Hypergraph Attention
    date: Jan 2019
    date_iso: 2019-01
    date_display: Jan 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.691
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PS-GraphPart-W
    model_plain: PS-GraphPart-W
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6906
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0119
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FS-GCN
    model_plain: FS-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6905
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0026
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MultiStage
    model_plain: MultiStage
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.02174'
    title: 'Break the Ceiling: Stronger Multi-scale Deep Graph Convolutional Networks'
    date: Jun 2019
    date_iso: 2019-06
    date_display: Jun 2019
    codebase_url: https://github.com/PwnerHarry/Stronger_GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.69
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCNII
    model_plain: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.69
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DeepWalk
    model_plain: DeepWalk
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.09025'
    title: Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/mtang724/NWR-GAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6899
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0095
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: STABLE
    model_plain: STABLE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6891
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0101
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GIN + PCL
    model_plain: GIN + PCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.09532'
    title: Pseudo Contrastive Learning for Graph-based Semi-supervised Learning
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6891
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0119
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Betweenness
    model_plain: Betweenness
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.05057'
    title: Towards More Practical Adversarial Attacks on Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/Mark12Ding/GNN-Practical-Attack
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.689
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.00064'
    title: 'SPGCL: Simple yet Powerful Graph Contrastive Learning via SVD-Guided Structural
      Perturbation'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.689
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.689
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphNAS
    model_plain: GraphNAS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.12357'
    title: 'Auto-HeG: Automated Graph Neural Network on Heterophilic Graphs'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6883
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0209
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DA-GraphPart
    model_plain: DA-GraphPart
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6882
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0117
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6881
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.018
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: S^3GC
    model_plain: S^3GC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.03670'
    title: 'CDC: A Simple Framework for Complex Data Clustering This work was supported
      by the National Natural Science Foundation of China Grant 62276053. Corresponding
      author: Erlin Pan Z. Kang, X. Xie, B. Li, E. Pan are with the School of Computer
      Science and Engineering, University of Electronic Science and Technology of
      China, Chengdu, China (e-mail: zkang@uestc.edu.cn; x624361380@outlook.com; bingheng86,
      wujisixsix6@gmail.com).'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.688
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT^3
    model_plain: GAT^3
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.03464'
    title: 'SPAGAN: Shortest Path Graph Attention Network'
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: https://github.com/ihollywhy/SPAGAN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.688
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6878
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GLEM-LM
    model_plain: GLEM-LM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6878
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AD-GCL
    model_plain: AD-GCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6874
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0053
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: 1st-order term only
    model_plain: 1st-order term only
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.02907'
    title: Semi-Supervised Classification with Graph Convolutional Networks
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/tkipf/gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.687
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: H2GCN
    model_plain: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.687
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.02
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AdaLNet
    model_plain: AdaLNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.04051'
    title: 'Graph-MLP: Node Classification without Message Passing in Graph'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.687
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AFGRL
    model_plain: AFGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.04604'
    title: Localized Graph Contrastive Learning
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.687
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SBert + NA
    model_plain: SBert + NA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6866
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LM (appr.)
    model_plain: LM (appr.)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6866
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRACE
    model_plain: GRACE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6865
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.017
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PS-FeatProp
    model_plain: PS-FeatProp
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6864
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0071
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GS-meanpool
    model_plain: GS-meanpool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.05868'
    title: Pitfalls of Graph Neural Network Evaluation
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.686
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.024
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GIB-Cat
    model_plain: GIB-Cat
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.12811'
    title: Graph Information Bottleneck
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.686
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.049
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPRGNN
    model_plain: GPRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.02279'
    title: arXiv:2411.02279
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/huangJC0429/label-utilize-GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6857
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0122
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HGRL
    model_plain: HGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.16026'
    title: 'MUSE: Multi-View Contrastive Learning for Heterophilic Graphs'
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6856
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DinkNet + CMV-ND
    model_plain: DinkNet + CMV-ND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.13368'
    title: Scalable Attribute-Missing Graph Clustering via Neighborhood Differentiation
    date: Jul 9, 2025
    date_iso: '2025-07-09'
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6856
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0171
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ProtGNN
    model_plain: ProtGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6851
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0052
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPT-GNN
    model_plain: GPT-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.12063'
    title: 'HAT-GAE: Self-Supervised Graph Auto-encoders with Hierarchical Adaptive
      Masking and Trainable Corruption'
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6851
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0033
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HopFormer
    model_plain: HopFormer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.02268'
    title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.685
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0346
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT-ppr
    model_plain: GAT-ppr
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.09443'
    title: Beltrami Flow and Neural Diffusion on Graphs
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: https://github.com/twitter-research/graph-neural-pde
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.685
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DropEdge
    model_plain: DropEdge
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.09755'
    title: Finding Heterophilic Neighbors via Confidence-based Subgraph Matching for
      Semi-supervised Node Classification
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.684
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Sent-BERT
    model_plain: Sent-BERT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6839
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DC-Graph (Clean)
    model_plain: DC-Graph (Clean)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.11025'
    title: Backdoor Graph Condensation
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/JiahaoWuGit/BGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6837
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: RobustGCN
    model_plain: RobustGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.17185'
    title: 'Robustness in Text-Attributed Graph Learning: Insights, Trade-offs, and
      New Defenses'
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/Leirunlin/TGRB
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6834
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: 1st-order model
    model_plain: 1st-order model
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.02907'
    title: Semi-Supervised Classification with Graph Convolutional Networks
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/tkipf/gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.683
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCDE-dpr5
    model_plain: GCDE-dpr5
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.07532'
    title: Graph Neural Ordinary Differential Equations
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.683
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FOSSIL
    model_plain: FOSSIL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6824
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0034
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6823
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: S2-HHGR
    model_plain: S2-HHGR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6821
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.018
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Union
    model_plain: Union
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.02174'
    title: 'Break the Ceiling: Stronger Multi-scale Deep Graph Convolutional Networks'
    date: Jun 2019
    date_iso: 2019-06
    date_display: Jun 2019
    codebase_url: https://github.com/PwnerHarry/Stronger_GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.682
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphPart
    model_plain: GraphPart
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.682
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: Roberta
    model_plain: Roberta
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6819
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FOSSIL v2
    model_plain: FOSSIL v2
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6816
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0023
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GSC+Cheb
    model_plain: GSC+Cheb
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6811
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0026
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: RGCN
    model_plain: RGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.14038'
    title: Robustness of Graph Neural Networks at Scale
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.681
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FeatProp
    model_plain: FeatProp
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6804
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0069
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRACE-MLP
    model_plain: GRACE-MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.13854'
    title: arXiv:2306.13854
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/yeonjun-in/torch-SP-AGCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.68
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.68
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN (rand. splits)
    model_plain: GCN (rand. splits)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.02907'
    title: Semi-Supervised Classification with Graph Convolutional Networks
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/tkipf/gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.679
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MILE(DGI, l=1)
    model_plain: MILE(DGI, l=1)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.679
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AllSet
    model_plain: AllSet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6783
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.018
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LP
    model_plain: LP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.05868'
    title: Pitfalls of Graph Neural Network Evaluation
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.678
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.021
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Self-training
    model_plain: Self-training
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.04714'
    title: 'NRGNN: Learning a Label Noise-Resistant Graph Neural Network on Sparsely
      and Noisily Labeled Graphs'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/EnyanDai/NRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.678
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.6778
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0342
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Sbert
    model_plain: Sbert
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6777
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6751
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GS-maxpool
    model_plain: GS-maxpool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.05868'
    title: Pitfalls of Graph Neural Network Evaluation
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.675
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.023
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HoloNet+EDEN
    model_plain: HoloNet+EDEN
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
    - 0.675
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Graph scattering
    model_plain: Graph scattering
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.08414'
    title: 'Scattering GCN: Overcoming Oversmoothness in Graph Convolutional Networks'
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: http://github.com/dms-net/scatteringGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.675
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Degree
    model_plain: Degree
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.05057'
    title: Towards More Practical Adversarial Attacks on Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/Mark12Ding/GNN-Practical-Attack
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.675
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: BGRL
    model_plain: BGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.03670'
    title: 'CDC: A Simple Framework for Complex Data Clustering This work was supported
      by the National Natural Science Foundation of China Grant 62276053. Corresponding
      author: Erlin Pan Z. Kang, X. Xie, B. Li, E. Pan are with the School of Computer
      Science and Engineering, University of Electronic Science and Technology of
      China, Chengdu, China (e-mail: zkang@uestc.edu.cn; x624361380@outlook.com; bingheng86,
      wujisixsix6@gmail.com).'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.675
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
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
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.675
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: VGAE
    model_plain: VGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6746
    - null
    - null
    - null
    - 0.9706
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - 0.0022
    - null
    - null
    - null
  - model: KNN w/ sp.-X
    model_plain: KNN w/ sp.-X
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6735
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.021
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HNHN
    model_plain: HNHN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6728
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.022
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Sp2GCL + PiNGDA
    model_plain: Sp2GCL + PiNGDA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6721
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0063
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAGE
    model_plain: SAGE
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
    - 0.672
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Dir-GNN+EDEN
    model_plain: Dir-GNN+EDEN
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
    - 0.672
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PS-Random-W
    model_plain: PS-Random-W
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6718
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0092
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: S^3GC + CMV-ND
    model_plain: S^3GC + CMV-ND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.13368'
    title: Scalable Attribute-Missing Graph Clustering via Neighborhood Differentiation
    date: Jul 9, 2025
    date_iso: '2025-07-09'
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6717
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0147
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LLM2Vec
    model_plain: LLM2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6713
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.13009'
    title: 'Iterative Deep Graph Learning for Graph Neural Networks: Better and Robust
      Node Embeddings'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/hugochan/IDGL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.67
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AGC
    model_plain: AGC
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.01210'
    title: Attributed Graph Clustering via Adaptive Graph Convolution
    date: Jun 2019
    date_iso: 2019-06
    date_display: Jun 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.67
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0024
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FAGCN
    model_plain: FAGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.08230'
    title: 'GADPN: Graph Adaptive Denoising and Perturbation Networks via Singular
      Value Decomposition'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.67
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCNII
    model_plain: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.09755'
    title: Finding Heterophilic Neighbors via Confidence-based Subgraph Matching for
      Semi-supervised Node Classification
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.67
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Roberta
    model_plain: Roberta
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6695
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRAND
    model_plain: GRAND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.17185'
    title: 'Robustness in Text-Attributed Graph Learning: Insights, Trade-offs, and
      New Defenses'
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/Leirunlin/TGRB
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6693000000000001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.011200000000000002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CPGNN
    model_plain: CPGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.09443'
    title: Beltrami Flow and Neural Diffusion on Graphs
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: https://github.com/twitter-research/graph-neural-pde
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.669
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.018
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DIMPA+EDEN
    model_plain: DIMPA+EDEN
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
    - 0.669
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Cheby
    model_plain: Cheby
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.11025'
    title: Backdoor Graph Condensation
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/JiahaoWuGit/BGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.669
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.03147'
    title: Learning Conjoint Attentions for Graph Neural Nets
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.669
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0016
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPT-3.5-turbo
    model_plain: GPT-3.5-turbo
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6683
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: VGAE
    model_plain: VGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.08792'
    title: Unifying Graph Contrastive Learning with Flexible Contextual Scopes
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: https://github.com/zyzisastudyreallyhardguy/UGCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.668
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DSF-GPR-I
    model_plain: DSF-GPR-I
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.09041'
    title: Graph Neural Networks with Diverse Spectral Filtering
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/jingweio/DSF
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6677
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0034
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LabelProp NL
    model_plain: LabelProp NL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.05868'
    title: Pitfalls of Graph Neural Network Evaluation
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.667
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.022
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAE
    model_plain: GAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.11689'
    title: Self-Supervised Graph Representation Learning via Topology Transformations
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/gyshgx868/topo-ter
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.667
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Sbert
    model_plain: Sbert
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6669
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Coteaching+
    model_plain: Coteaching+
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.04714'
    title: 'NRGNN: Learning a Label Noise-Resistant Graph Neural Network on Sparsely
      and Noisily Labeled Graphs'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/EnyanDai/NRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.664
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.013
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: UniGCN
    model_plain: UniGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.664
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.019
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPT3.5
    model_plain: GPT3.5
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6639
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0862
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Text-Embedding-3-Large
    model_plain: Text-Embedding-3-Large
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6624
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LanczosNet
    model_plain: LanczosNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.06986'
    title: How Framelets Enhance Graph Neural Networks
    date: Feb 13, 2021
    date_iso: '2021-02-13'
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.662
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.019
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DisGNN
    model_plain: DisGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.662
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.022
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LNet
    model_plain: LNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.04051'
    title: 'Graph-MLP: Node Classification without Message Passing in Graph'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.662
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DHGNN
    model_plain: DHGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6616
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.023
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.00797'
    title: Beyond Low-frequency Information in Graph Convolutional Networks
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.661
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GC-RWCS
    model_plain: GC-RWCS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.05057'
    title: Towards More Practical Adversarial Attacks on Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/Mark12Ding/GNN-Practical-Attack
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.661
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TAPE
    model_plain: TAPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6606
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CP
    model_plain: CP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.04714'
    title: 'NRGNN: Learning a Label Noise-Resistant Graph Neural Network on Sparsely
      and Noisily Labeled Graphs'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/EnyanDai/NRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.66
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.016
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SDCN
    model_plain: SDCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.09600'
    title: Deep Fusion Clustering Network
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/WxTu/DFCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.66
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Random-W
    model_plain: Random-W
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6592
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0105
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: JK-Net
    model_plain: JK-Net
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.03147'
    title: Learning Conjoint Attentions for Graph Neural Nets
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6588
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0001
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.6588
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0141
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRACE
    model_plain: GRACE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6586
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GIANT
    model_plain: GIANT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6582
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAE
    model_plain: GAE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.12063'
    title: 'HAT-GAE: Self-Supervised Graph Auto-encoders with Hierarchical Adaptive
      Masking and Trainable Corruption'
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6582
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0011
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.658
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GOFA
    model_plain: GOFA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6572
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AMGC + CMV-ND
    model_plain: AMGC + CMV-ND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.13368'
    title: Scalable Attribute-Missing Graph Clustering via Neighborhood Differentiation
    date: Jul 9, 2025
    date_iso: '2025-07-09'
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6571
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0283
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.6563
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0169
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Graphormer_Small
    model_plain: Graphormer_Small
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.10759'
    title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/qitianwu/SGFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.656
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Random Policy
    model_plain: Random Policy
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15097'
    title: 'Policy-GNN: Aggregation Optimization for Graph Neural Networks'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.656
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.024
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GB-GNN-KTA L=0
    model_plain: GB-GNN-KTA L=0
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.656
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.017
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPT4
    model_plain: GPT4
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6556
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0929
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.08057'
    title: Understanding and Improving Graph Injection Attack by Promoting Unnoticeability
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/LFhase/GIA-HAO
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6555
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Sp2GCL
    model_plain: Sp2GCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6554
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0051
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Co-training
    model_plain: Co-training
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.02174'
    title: 'Break the Ceiling: Stronger Multi-scale Deep Graph Convolutional Networks'
    date: Jun 2019
    date_iso: 2019-06
    date_display: Jun 2019
    codebase_url: https://github.com/PwnerHarry/Stronger_GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.655
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MLP + PCL
    model_plain: MLP + PCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.09532'
    title: Pseudo Contrastive Learning for Graph-based Semi-supervised Learning
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6545
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0105
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGCNN
    model_plain: DGCNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.13970'
    title: Directed Graph Convolutional Network
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.654
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.023
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPR-GNN
    model_plain: GPR-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.09041'
    title: Graph Neural Networks with Diverse Spectral Filtering
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/jingweio/DSF
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6539
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0044
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: UnionGraphSNN
    model_plain: UnionGraphSNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6522
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0112
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAE
    model_plain: GAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.08792'
    title: Unifying Graph Contrastive Learning with Flexible Contextual Scopes
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: https://github.com/zyzisastudyreallyhardguy/UGCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.652
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Random
    model_plain: Random
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6511
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0112
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GB-GNN-II L=0
    model_plain: GB-GNN-II L=0
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.651
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.025
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.09755'
    title: Finding Heterophilic Neighbors via Confidence-based Subgraph Matching for
      Semi-supervised Node Classification
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.651
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: UnionSNN
    model_plain: UnionSNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6502
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0102
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.6501
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0229
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LADIES (64)
    model_plain: LADIES (64)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.07323'
    title: Layer-Dependent Importance Sampling for Training Deep and Large Graph Convolutional
      Networks
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/acbull/LADIES
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.65
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.65
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.036
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Forward
    model_plain: Forward
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.04714'
    title: 'NRGNN: Learning a Label Noise-Resistant Graph Neural Network on Sparsely
      and Noisily Labeled Graphs'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/EnyanDai/NRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.65
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.015
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ZeroG
    model_plain: ZeroG
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.11235'
    title: 'ZeroG: Investigating Cross-dataset Zero-shot Transferability in Graphs'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/NineAbyss/ZeroG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6494
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DS-GNN
    model_plain: DS-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.04714'
    title: 'NRGNN: Learning a Label Noise-Resistant Graph Neural Network on Sparsely
      and Noisily Labeled Graphs'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/EnyanDai/NRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.649
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.013
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NAG+EDEN
    model_plain: NAG+EDEN
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
    - 0.648
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.6478
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0105
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPT-4o
    model_plain: GPT-4o
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6477
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Planetoid*
    model_plain: Planetoid*
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.02907'
    title: Semi-Supervised Classification with Graph Convolutional Networks
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/tkipf/gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.647
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
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
    arxiv_id: '2004.13970'
    title: Directed Graph Convolutional Network
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.647
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.023
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSNN
    model_plain: GraphSNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6468
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0272
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: OptBG+EDEN
    model_plain: OptBG+EDEN
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
    - 0.646
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Node2Vec
    model_plain: Node2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.09025'
    title: Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/mtang724/NWR-GAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6456
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: RAWGNN+DiSRW
    model_plain: RAWGNN+DiSRW
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
    - 0.6454
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0075
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DAEGC
    model_plain: DAEGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.09600'
    title: Deep Fusion Clustering Network
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/WxTu/DFCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.645
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DC-Graph (Clean)
    model_plain: DC-Graph (Clean)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.13974'
    title: Are You Using Reliable Graph Prompts? Trojan Prompt Attacks on Graph Neural
      Networks
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/ventr1c/TPGA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.644
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.6436
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0035
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LADIES (512)
    model_plain: LADIES (512)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.07323'
    title: Layer-Dependent Importance Sampling for Training Deep and Large Graph Convolutional
      Networks
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/acbull/LADIES
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.643
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.024
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MoNet
    model_plain: MoNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.03147'
    title: Learning Conjoint Attentions for Graph Neural Nets
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6422
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0016
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HyperConv
    model_plain: HyperConv
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6412
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.026
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: WRGAT
    model_plain: WRGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.641
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.019
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.641
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: VGAE
    model_plain: VGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.11689'
    title: Self-Supervised Graph Representation Learning via Topology Transformations
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/gyshgx868/topo-ter
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.641
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TSVM
    model_plain: TSVM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1603.08861'
    title: Revisiting Semi-Supervised Learning with Graph Embeddings
    date: Mar 29, 2016
    date_iso: '2016-03-29'
    date_display: Mar 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.64
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MPNN
    model_plain: MPNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.06986'
    title: How Framelets Enhance Graph Neural Networks
    date: Feb 13, 2021
    date_iso: '2021-02-13'
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.64
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.019
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.64
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TriCL-N
    model_plain: TriCL-N
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6398
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.02
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.639
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SBA-P
    model_plain: SBA-P
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.13974'
    title: Are You Using Reliable Graph Prompts? Trojan Prompt Attacks on Graph Neural
      Networks
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/ventr1c/TPGA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.639
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.638
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGC+DGCN
    model_plain: SGC+DGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.13970'
    title: Directed Graph Convolutional Network
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.638
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.02
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.6374
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0087
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.13970'
    title: Directed Graph Convolutional Network
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.637
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.02
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: BL-Rand
    model_plain: BL-Rand
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.13974'
    title: Are You Using Reliable Graph Prompts? Trojan Prompt Attacks on Graph Neural
      Networks
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/ventr1c/TPGA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.637
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: UnionGCN
    model_plain: UnionGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6366
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0175
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Graphormer_UltrasSmall
    model_plain: Graphormer_UltrasSmall
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.10759'
    title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/qitianwu/SGFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.636
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Patton
    model_plain: Patton
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.636
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MGAE
    model_plain: MGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.01210'
    title: Attributed Graph Clustering via Adaptive Graph Convolution
    date: Jun 2019
    date_iso: 2019-06
    date_display: Jun 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6356
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FastGCN (1024)
    model_plain: FastGCN (1024)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.07323'
    title: Layer-Dependent Importance Sampling for Training Deep and Large Graph Convolutional
      Networks
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/acbull/LADIES
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.635
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.018
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAGE (our implementation)
    model_plain: SAGE (our implementation)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1802.08888'
    title: 'N-GCN: Multi-scale Graph Convolution for Semi-supervised Node Classification'
    date: Feb 2018
    date_iso: 2018-02
    date_display: Feb 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.635
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: RIM
    model_plain: RIM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6344
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0042
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ARGVA
    model_plain: ARGVA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.09025'
    title: Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/mtang724/NWR-GAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6336
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0208
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PS-Pagerank-W
    model_plain: PS-Pagerank-W
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6327
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0034
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CTGC
    model_plain: CTGC
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17063'
    title: 'Contrastive Graph Condensation: Advancing Data Versatility through Self-Supervised
      Learning'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/XYGaoG/CTGCcode
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.632
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.018
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRACE
    model_plain: GRACE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.03670'
    title: 'CDC: A Simple Framework for Complex Data Clustering This work was supported
      by the National Natural Science Foundation of China Grant 62276053. Corresponding
      author: Erlin Pan Z. Kang, X. Xie, B. Li, E. Pan are with the School of Computer
      Science and Engineering, University of Electronic Science and Technology of
      China, Chengdu, China (e-mail: zkang@uestc.edu.cn; x624361380@outlook.com; bingheng86,
      wujisixsix6@gmail.com).'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.631
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.6299
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0108
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DA-Density
    model_plain: DA-Density
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6298
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0077
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Planetoid*
    model_plain: Planetoid*
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1603.08861'
    title: Revisiting Semi-Supervised Learning with Graph Embeddings
    date: Mar 29, 2016
    date_iso: '2016-03-29'
    date_display: Mar 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.629
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.629
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: UGBA-P
    model_plain: UGBA-P
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.13974'
    title: Are You Using Reliable Graph Prompts? Trojan Prompt Attacks on Graph Neural
      Networks
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/ventr1c/TPGA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.629
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PS-RIM-W
    model_plain: PS-RIM-W
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6285
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0049
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.628
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.13970'
    title: Directed Graph Convolutional Network
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.628
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.021
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TGPA
    model_plain: TGPA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.13974'
    title: Are You Using Reliable Graph Prompts? Trojan Prompt Attacks on Graph Neural
      Networks
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/ventr1c/TPGA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.627
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PathNet+DiSRW
    model_plain: PathNet+DiSRW
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
    - 0.6266
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0089
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TGPA/R
    model_plain: TGPA/R
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.13974'
    title: Are You Using Reliable Graph Prompts? Trojan Prompt Attacks on Graph Neural
      Networks
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/ventr1c/TPGA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.626
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.625
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NAG
    model_plain: NAG
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
    - 0.625
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: OptBG
    model_plain: OptBG
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
    - 0.624
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.6238
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0028
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PS-Degree-W
    model_plain: PS-Degree-W
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6236
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0069
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Full-Batch
    model_plain: Full-Batch
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.07323'
    title: Layer-Dependent Importance Sampling for Training Deep and Large Graph Convolutional
      Networks
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/acbull/LADIES
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.623
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.031
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GTA-P
    model_plain: GTA-P
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.13974'
    title: Are You Using Reliable Graph Prompts? Trojan Prompt Attacks on Graph Neural
      Networks
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/ventr1c/TPGA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.622
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ProGCL + CMV-ND
    model_plain: ProGCL + CMV-ND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.13368'
    title: Scalable Attribute-Missing Graph Clustering via Neighborhood Differentiation
    date: Jul 9, 2025
    date_iso: '2025-07-09'
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6215
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0079
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CurvGN
    model_plain: CurvGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6208
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0085
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.6205
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0059
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GaLGuard
    model_plain: GaLGuard
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.04894'
    title: Adversarial Attacks and Defenses on Graph-aware Large Language Models (LLMs)
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.62
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.04
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Pagerank
    model_plain: Pagerank
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6197
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0019
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SDCN_Q
    model_plain: SDCN_Q
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.09600'
    title: Deep Fusion Clustering Network
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/WxTu/DFCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.617
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FactorGCN
    model_plain: FactorGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.616
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.02
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MLP-K
    model_plain: MLP-K
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.12055'
    title: Towards Self-Explainable Graph Neural Network
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/EnyanDai/SEGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.616
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.016
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.6141
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0193
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.13970'
    title: Directed Graph Convolutional Network
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.614
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.034
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAE
    model_plain: GAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.09600'
    title: Deep Fusion Clustering Network
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/WxTu/DFCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.614
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DA-Degree
    model_plain: DA-Degree
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6129
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0047
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DA-Pagerank
    model_plain: DA-Pagerank
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6125
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0045
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AMGC
    model_plain: AMGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.13368'
    title: Scalable Attribute-Missing Graph Clustering via Neighborhood Differentiation
    date: Jul 9, 2025
    date_iso: '2025-07-09'
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6123
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0187
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TLP
    model_plain: TLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.12140'
    title: Graph Few-Shot Learning via Adaptive Spectrum Experts and Cross-Set Distribution
      Calibration
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/KEAML-JLU/GRACE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6112
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.021
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Node features (SVM)
    model_plain: Node features (SVM)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.08414'
    title: 'Scattering GCN: Overcoming Oversmoothness in Graph Convolutional Networks'
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: http://github.com/dms-net/scatteringGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.611
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: C-Density
    model_plain: C-Density
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6106
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0095
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LogReg
    model_plain: LogReg
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.05868'
    title: Pitfalls of Graph Neural Network Evaluation
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.61
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.022
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PS-Density-W
    model_plain: PS-Density-W
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.61
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0055
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: VGAE
    model_plain: VGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.09600'
    title: Deep Fusion Clustering Network
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/WxTu/DFCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.61
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AAGCN
    model_plain: AAGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.08676'
    title: 'Redesigning graph filter-based GNNs to relax the homophily assumption
      This work was supported in part by the Spanish AEI Grants PID2022-136887NB-I00,
      PID2023-149457OB-I00, FPU20/05554, the Community of Madrid (Madrid ELLIS Unit),
      and the NSF under award CCF-2340481. Research was sponsored by the Army Research
      Office and was accomplished under Grant Number W911NF-17-S-0002. The views and
      conclusions contained in this document are those of the authors and should not
      be interpreted as representing the official policies, either expressed or implied,
      of the Army Research Office or the U.S. Army or the U.S. Government. The U.S.
      Government is authorized to reproduce and distribute reprints for Government
      purposes notwithstanding any copyright notation herein. Emails: samuel.rey.escudero@urjc.es,
      nav@rice.edu, victor.tenorio@urjc.es, segarra@rice.edu, antonio.garcia.marques@urjc.es'
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/reysam93/adaptive_agg_gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.61
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.036
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: COSMIC
    model_plain: COSMIC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.12140'
    title: Graph Few-Shot Learning via Adaptive Spectrum Experts and Cross-Set Distribution
      Calibration
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/KEAML-JLU/GRACE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6095
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0275
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.6088
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0108
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DA-RIM-W
    model_plain: DA-RIM-W
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.608
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0057
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GB-GNN-Adj L=0
    model_plain: GB-GNN-Adj L=0
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.607
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.017
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Clean GNN (GC-SNTK)
    model_plain: Clean GNN (GC-SNTK)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.11025'
    title: Backdoor Graph Condensation
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/JiahaoWuGit/BGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6068
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0104
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGI + CMV-ND
    model_plain: DGI + CMV-ND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.13368'
    title: Scalable Attribute-Missing Graph Clustering via Neighborhood Differentiation
    date: Jul 9, 2025
    date_iso: '2025-07-09'
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.606
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0147
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: IDEC
    model_plain: IDEC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.09600'
    title: Deep Fusion Clustering Network
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/WxTu/DFCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.605
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Logistic Reg.-A
    model_plain: Logistic Reg.-A
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6049
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Degree-W
    model_plain: Degree-W
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6047
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0049
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Random-Init
    model_plain: Random-Init
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6044
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.025
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Shift-MLP
    model_plain: Shift-MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.604
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DA-RIM
    model_plain: DA-RIM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6033
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Degree
    model_plain: Degree
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6023
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0054
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: BGC (GC-SNTK)
    model_plain: BGC (GC-SNTK)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.11025'
    title: Backdoor Graph Condensation
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/JiahaoWuGit/BGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.602
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0364
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Meta-BP
    model_plain: Meta-BP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.12140'
    title: Graph Few-Shot Learning via Adaptive Spectrum Experts and Cross-Set Distribution
      Calibration
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/KEAML-JLU/GRACE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6015
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0245
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ManiReg
    model_plain: ManiReg
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1603.08861'
    title: Revisiting Semi-Supervised Learning with Graph Embeddings
    date: Mar 29, 2016
    date_iso: '2016-03-29'
    date_display: Mar 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.601
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Manifold Regularization
    model_plain: Manifold Regularization
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1901.08150'
    title: Hypergraph Convolution and Hypergraph Attention
    date: Jan 2019
    date_iso: 2019-01
    date_display: Jan 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.601
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TENT
    model_plain: TENT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.12140'
    title: Graph Few-Shot Learning via Adaptive Spectrum Experts and Cross-Set Distribution
      Calibration
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/KEAML-JLU/GRACE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0311
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.5994
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0038
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DA-AGE
    model_plain: DA-AGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5992
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0042
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HyperGCN
    model_plain: HyperGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5992
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.096
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Density-W
    model_plain: Density-W
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5988
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0097
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: EvenNet
    model_plain: EvenNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.17185'
    title: 'Robustness in Text-Attributed Graph Learning: Insights, Trade-offs, and
      New Defenses'
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/Leirunlin/TGRB
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5977
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0027
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ChebNet
    model_plain: ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.13970'
    title: Directed Graph Convolutional Network
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.597
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.04
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TEG
    model_plain: TEG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.12140'
    title: Graph Few-Shot Learning via Adaptive Spectrum Experts and Cross-Set Distribution
      Calibration
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/KEAML-JLU/GRACE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.597
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0269
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SemiEmb
    model_plain: SemiEmb
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1603.08861'
    title: Revisiting Semi-Supervised Learning with Graph Embeddings
    date: Mar 29, 2016
    date_iso: '2016-03-29'
    date_display: Mar 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.596
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Semi-supervised Embedding
    model_plain: Semi-supervised Embedding
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1901.08150'
    title: Hypergraph Convolution and Hypergraph Attention
    date: Jan 2019
    date_iso: 2019-01
    date_display: Jan 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.596
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphText
    model_plain: GraphText
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.5943
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.07323'
    title: Layer-Dependent Importance Sampling for Training Deep and Large Graph Convolutional
      Networks
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/acbull/LADIES
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.594
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPT-3.5-turbo
    model_plain: GPT-3.5-turbo
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14324'
    title: Large Language Models as Topological Structure Enhancers for Text-Attributed
      Graphs
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/sunshy-1/LLM4GraphTopology
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.5929
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Geom-GCN
    model_plain: Geom-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.00064'
    title: 'SPGCL: Simple yet Powerful Graph Contrastive Learning via SVD-Guided Structural
      Perturbation'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5917
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.05868'
    title: Pitfalls of Graph Neural Network Evaluation
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.591
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.023
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Meta-GPS
    model_plain: Meta-GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.12140'
    title: Graph Few-Shot Learning via Adaptive Spectrum Experts and Cross-Set Distribution
      Calibration
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/KEAML-JLU/GRACE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5895
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0212
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Spectral
    model_plain: Spectral
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.06986'
    title: How Framelets Enhance Graph Neural Networks
    date: Feb 13, 2021
    date_iso: '2021-02-13'
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.589
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ProGCL
    model_plain: ProGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.13368'
    title: Scalable Attribute-Missing Graph Clustering via Neighborhood Differentiation
    date: Jul 9, 2025
    date_iso: '2025-07-09'
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5885
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0093
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DeepWalk
    model_plain: DeepWalk
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.08792'
    title: Unifying Graph Contrastive Learning with Flexible Contextual Scopes
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: https://github.com/zyzisastudyreallyhardguy/UGCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.588
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: X-FNC
    model_plain: X-FNC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.12140'
    title: Graph Few-Shot Learning via Adaptive Spectrum Experts and Cross-Set Distribution
      Calibration
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/KEAML-JLU/GRACE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5879
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0256
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DA-AGE-W
    model_plain: DA-AGE-W
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5841
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0045
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DinkNet
    model_plain: DinkNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.13368'
    title: Scalable Attribute-Missing Graph Clustering via Neighborhood Differentiation
    date: Jul 9, 2025
    date_iso: '2025-07-09'
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5834
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: Label Propagation
    model_plain: Label Propagation
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.08414'
    title: 'Scattering GCN: Overcoming Oversmoothness in Graph Convolutional Networks'
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: http://github.com/dms-net/scatteringGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.582
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MUSE
    model_plain: MUSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5805
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0042
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Raw features
    model_plain: Raw features
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.11996'
    title: Generative Subgraph Contrast for Self-Supervised Graph Representation Learning
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: https://github.com/yh-han/GSC.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.578
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: S^3GC
    model_plain: S^3GC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.13368'
    title: Scalable Attribute-Missing Graph Clustering via Neighborhood Differentiation
    date: Jul 9, 2025
    date_iso: '2025-07-09'
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5761
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0151
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AGE-W
    model_plain: AGE-W
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.576
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0035
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PS-AGE-W
    model_plain: PS-AGE-W
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5744
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0049
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AGC-DRR + CMV-ND
    model_plain: AGC-DRR + CMV-ND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.13368'
    title: Scalable Attribute-Missing Graph Clustering via Neighborhood Differentiation
    date: Jul 9, 2025
    date_iso: '2025-07-09'
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5741
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0151
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GeniePath
    model_plain: GeniePath
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.574
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0216
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPN
    model_plain: GPN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.12140'
    title: Graph Few-Shot Learning via Adaptive Spectrum Experts and Cross-Set Distribution
      Calibration
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/KEAML-JLU/GRACE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5736
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.022
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Feat
    model_plain: Feat
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1603.08861'
    title: Revisiting Semi-Supervised Learning with Graph Embeddings
    date: Mar 29, 2016
    date_iso: '2016-03-29'
    date_display: Mar 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.572
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Whole Dataset
    model_plain: Whole Dataset
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17063'
    title: 'Contrastive Graph Condensation: Advancing Data Versatility through Self-Supervised
      Learning'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/XYGaoG/CTGCcode
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.572
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.024
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MVGRL
    model_plain: MVGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.13368'
    title: Scalable Attribute-Missing Graph Clustering via Neighborhood Differentiation
    date: Jul 9, 2025
    date_iso: '2025-07-09'
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.572
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0058
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MVGRL + CMV-ND
    model_plain: MVGRL + CMV-ND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.13368'
    title: Scalable Attribute-Missing Graph Clustering via Neighborhood Differentiation
    date: Jul 9, 2025
    date_iso: '2025-07-09'
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.572
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0058
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAE
    model_plain: GAE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.09025'
    title: Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/mtang724/NWR-GAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.571
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: AE
    model_plain: AE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.09600'
    title: Deep Fusion Clustering Network
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/WxTu/DFCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.571
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ARGVA
    model_plain: ARGVA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.09600'
    title: Deep Fusion Clustering Network
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/WxTu/DFCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.569
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: KNN w/ sp.-A
    model_plain: KNN w/ sp.-A
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5678
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.013
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FB-GCN
    model_plain: FB-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.08676'
    title: 'Redesigning graph filter-based GNNs to relax the homophily assumption
      This work was supported in part by the Spanish AEI Grants PID2022-136887NB-I00,
      PID2023-149457OB-I00, FPU20/05554, the Community of Madrid (Madrid ELLIS Unit),
      and the NSF under award CCF-2340481. Research was sponsored by the Army Research
      Office and was accomplished under Grant Number W911NF-17-S-0002. The views and
      conclusions contained in this document are those of the authors and should not
      be interpreted as representing the official policies, either expressed or implied,
      of the Army Research Office or the U.S. Army or the U.S. Government. The U.S.
      Government is authorized to reproduce and distribute reprints for Government
      purposes notwithstanding any copyright notation herein. Emails: samuel.rey.escudero@urjc.es,
      nav@rice.edu, victor.tenorio@urjc.es, segarra@rice.edu, antonio.garcia.marques@urjc.es'
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/reysam93/adaptive_agg_gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.566
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.023
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FS-MLP
    model_plain: FS-MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5637
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0037
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCSR
    model_plain: GCSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17063'
    title: 'Contrastive Graph Condensation: Advancing Data Versatility through Self-Supervised
      Learning'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/XYGaoG/CTGCcode
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.563
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.017
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCOND
    model_plain: GCOND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17063'
    title: 'Contrastive Graph Condensation: Advancing Data Versatility through Self-Supervised
      Learning'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/XYGaoG/CTGCcode
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.559
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DEC
    model_plain: DEC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.09600'
    title: Deep Fusion Clustering Network
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/WxTu/DFCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.559
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCDM
    model_plain: GCDM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17063'
    title: 'Contrastive Graph Condensation: Advancing Data Versatility through Self-Supervised
      Learning'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/XYGaoG/CTGCcode
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.558
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LLaGA
    model_plain: LLaGA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.5573
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GDEM
    model_plain: GDEM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17063'
    title: 'Contrastive Graph Condensation: Advancing Data Versatility through Self-Supervised
      Learning'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/XYGaoG/CTGCcode
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.556
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.017
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Meta-GNN
    model_plain: Meta-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.12140'
    title: Graph Few-Shot Learning via Adaptive Spectrum Experts and Cross-Set Distribution
      Calibration
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/KEAML-JLU/GRACE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5545
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0215
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SimGC
    model_plain: SimGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17063'
    title: 'Contrastive Graph Condensation: Advancing Data Versatility through Self-Supervised
      Learning'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/XYGaoG/CTGCcode
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.554
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5502
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.034
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Coarsening
    model_plain: Coarsening
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17063'
    title: 'Contrastive Graph Condensation: Advancing Data Versatility through Self-Supervised
      Learning'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/XYGaoG/CTGCcode
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.547
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.046
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Node2Vec
    model_plain: Node2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15097'
    title: 'Policy-GNN: Aggregation Optimization for Graph Neural Networks'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.547
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MLP
    model_plain: MLP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.04051'
    title: 'Graph-MLP: Node Classification without Message Passing in Graph'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.547
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GSC
    model_plain: GSC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5456
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0074
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ARGE
    model_plain: ARGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1802.04407'
    title: Adversarially Regularized Graph Autoencoder for Graph Embedding
    date: Feb 2018
    date_iso: 2018-02
    date_display: Feb 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.544
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: G-Meta
    model_plain: G-Meta
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.12140'
    title: Graph Few-Shot Learning via Adaptive Spectrum Experts and Cross-Set Distribution
      Calibration
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/KEAML-JLU/GRACE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5439
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0219
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AGE
    model_plain: AGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5425
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0031
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DSSL
    model_plain: DSSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5416
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0064
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: K-means
    model_plain: K-means
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1802.04407'
    title: Adversarially Regularized Graph Autoencoder for Graph Embedding
    date: Feb 2018
    date_iso: 2018-02
    date_display: Feb 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.54
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CCGC + CMV-ND
    model_plain: CCGC + CMV-ND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.13368'
    title: Scalable Attribute-Missing Graph Clustering via Neighborhood Differentiation
    date: Jul 9, 2025
    date_iso: '2025-07-09'
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5398
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0193
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.12140'
    title: Graph Few-Shot Learning via Adaptive Spectrum Experts and Cross-Set Distribution
      Calibration
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/KEAML-JLU/GRACE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5372
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0255
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.13368'
    title: Scalable Attribute-Missing Graph Clustering via Neighborhood Differentiation
    date: Jul 9, 2025
    date_iso: '2025-07-09'
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.536
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: AGC-DRR
    model_plain: AGC-DRR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.13368'
    title: Scalable Attribute-Missing Graph Clustering via Neighborhood Differentiation
    date: Jul 9, 2025
    date_iso: '2025-07-09'
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.534
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0105
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NoisyGCN
    model_plain: NoisyGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.17185'
    title: 'Robustness in Text-Attributed Graph Learning: Insights, Trade-offs, and
      New Defenses'
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/Leirunlin/TGRB
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5324
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0109
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Herding
    model_plain: Herding
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17063'
    title: 'Contrastive Graph Condensation: Advancing Data Versatility through Self-Supervised
      Learning'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/XYGaoG/CTGCcode
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.527
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.026
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.08676'
    title: 'Redesigning graph filter-based GNNs to relax the homophily assumption
      This work was supported in part by the Spanish AEI Grants PID2022-136887NB-I00,
      PID2023-149457OB-I00, FPU20/05554, the Community of Madrid (Madrid ELLIS Unit),
      and the NSF under award CCF-2340481. Research was sponsored by the Army Research
      Office and was accomplished under Grant Number W911NF-17-S-0002. The views and
      conclusions contained in this document are those of the authors and should not
      be interpreted as representing the official policies, either expressed or implied,
      of the Army Research Office or the U.S. Army or the U.S. Government. The U.S.
      Government is authorized to reproduce and distribute reprints for Government
      purposes notwithstanding any copyright notation herein. Emails: samuel.rey.escudero@urjc.es,
      nav@rice.edu, victor.tenorio@urjc.es, segarra@rice.edu, antonio.garcia.marques@urjc.es'
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/reysam93/adaptive_agg_gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.527
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.043
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HyperSAGE
    model_plain: HyperSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5243
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.094
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.17185'
    title: 'Robustness in Text-Attributed Graph Learning: Insights, Trade-offs, and
      New Defenses'
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/Leirunlin/TGRB
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.524
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0167
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: UniGLM
    model_plain: UniGLM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.5226
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
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
    arxiv_id: '2510.12140'
    title: Graph Few-Shot Learning via Adaptive Spectrum Experts and Cross-Set Distribution
      Calibration
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/KEAML-JLU/GRACE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5195
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0245
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: InstructGLM
    model_plain: InstructGLM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.5187
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: training-free baseline
    model_plain: training-free baseline
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5175
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: struc2vec
    model_plain: struc2vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.09025'
    title: Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/mtang724/NWR-GAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.517
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0067
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DeepWalk
    model_plain: DeepWalk
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.04051'
    title: 'Graph-MLP: Node Classification without Message Passing in Graph'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.514
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DeepWalk + Features
    model_plain: DeepWalk + Features
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2007.08025'
    title: 'GraphCL: Contrastive Self-Supervised Learning of Graph Representations'
    date: Jul 2020
    date_iso: 2020-07
    date_display: Jul 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.514
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GZoom(N2V, l=1)
    model_plain: GZoom(N2V, l=1)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.507
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ZeroG
    model_plain: ZeroG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.5035
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT + CAR
    model_plain: GAT + CAR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.10946'
    title: Causally-guided Regularization of Graph Attention Improves Generalizability
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.06
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GZoom(DW, l=1)
    model_plain: GZoom(DW, l=1)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.495
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4931
    - null
    - null
    - null
    - 0.9445
    - null
    - null
    - null
    metric_stds:
    - 0.0026
    - null
    - null
    - null
    - 0.0032
    - null
    - null
    - null
  - model: Raw features
    model_plain: Raw features
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2007.08025'
    title: 'GraphCL: Contrastive Self-Supervised Learning of Graph Representations'
    date: Jul 2020
    date_iso: 2020-07
    date_display: Jul 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.493
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: K-means + CMV-ND
    model_plain: K-means + CMV-ND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.13368'
    title: Scalable Attribute-Missing Graph Clustering via Neighborhood Differentiation
    date: Jul 9, 2025
    date_iso: '2025-07-09'
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4927
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0132
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ProtoNet
    model_plain: ProtoNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.12140'
    title: Graph Few-Shot Learning via Adaptive Spectrum Experts and Cross-Set Distribution
      Calibration
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/KEAML-JLU/GRACE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4915
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0229
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MAML
    model_plain: MAML
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.12140'
    title: Graph Few-Shot Learning via Adaptive Spectrum Experts and Cross-Set Distribution
      Calibration
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/KEAML-JLU/GRACE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4915
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0225
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Kcenter
    model_plain: Kcenter
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17063'
    title: 'Contrastive Graph Condensation: Advancing Data Versatility through Self-Supervised
      Learning'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/XYGaoG/CTGCcode
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.49
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.052
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GZoom_F+MILE(N2V)
    model_plain: GZoom_F+MILE(N2V)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.483
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Node2Vec
    model_plain: Node2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.08792'
    title: Unifying Graph Contrastive Learning with Flexible Contextual Scopes
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: https://github.com/zyzisastudyreallyhardguy/UGCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.476
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Sent-BERT
    model_plain: Sent-BERT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.11235'
    title: 'ZeroG: Investigating Cross-dataset Zero-shot Transferability in Graphs'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/NineAbyss/ZeroG
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.4752
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LP
    model_plain: LP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.02174'
    title: 'Break the Ceiling: Stronger Multi-scale Deep Graph Convolutional Networks'
    date: Jun 2019
    date_iso: 2019-06
    date_display: Jun 2019
    codebase_url: https://github.com/PwnerHarry/Stronger_GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.473
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MILE(DW, l=1)
    model_plain: MILE(DW, l=1)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.471
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GATv2
    model_plain: GATv2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.10946'
    title: Causally-guided Regularization of Graph Attention Improves Generalizability
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.47
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.08
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Transformer + CAR
    model_plain: Transformer + CAR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.10946'
    title: Causally-guided Regularization of Graph Attention Improves Generalizability
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.47
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.09
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DeepWalk
    model_plain: DeepWalk
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.47
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE-SMGDC
    model_plain: GraphSAGE-SMGDC
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
    - 0.4667
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.036
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Multi-layer perceptron
    model_plain: Multi-layer perceptron
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.02907'
    title: Semi-Supervised Classification with Graph Convolutional Networks
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/tkipf/gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.465
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Multilayer Perceptron
    model_plain: Multilayer Perceptron
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1901.08150'
    title: Hypergraph Convolution and Hypergraph Attention
    date: Jan 2019
    date_iso: 2019-01
    date_display: Jan 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.465
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.11430'
    title: Independence Promoted Graph Disentangled Networks
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.465
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCoT
    model_plain: GCoT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.08092'
    title: 'GCoT: Chain-of-Thought Prompt Learning for Graphs'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.4621
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0878
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GNNGuard
    model_plain: GNNGuard
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.17185'
    title: 'Robustness in Text-Attributed Graph Learning: Insights, Trade-offs, and
      New Defenses'
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/Leirunlin/TGRB
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.46130000000000004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.013999999999999999
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.10946'
    title: Causally-guided Regularization of Graph Attention Improves Generalizability
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.46
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.09
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: E5
    model_plain: E5
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.11235'
    title: 'ZeroG: Investigating Cross-dataset Zero-shot Transferability in Graphs'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/NineAbyss/ZeroG
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.4589
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Node2Vec
    model_plain: Node2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.458
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TADW
    model_plain: TADW
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1802.04407'
    title: Adversarially Regularized Graph Autoencoder for Graph Embedding
    date: Feb 2018
    date_iso: 2018-02
    date_display: Feb 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.455
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphPrompt
    model_plain: GraphPrompt
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.08092'
    title: 'GCoT: Chain-of-Thought Prompt Learning for Graphs'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.4534
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.1053
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LP
    model_plain: LP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1603.08861'
    title: Revisiting Semi-Supervised Learning with Graph Embeddings
    date: Mar 29, 2016
    date_iso: '2016-03-29'
    date_display: Mar 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.453
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Label Propagation
    model_plain: Label Propagation
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1901.08150'
    title: Hypergraph Convolution and Hypergraph Attention
    date: Jan 2019
    date_iso: 2019-01
    date_display: Jan 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.453
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MILE(N2V, l=1)
    model_plain: MILE(N2V, l=1)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.452
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: RTM
    model_plain: RTM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1802.04407'
    title: Adversarially Regularized Graph Autoencoder for Graph Embedding
    date: Feb 2018
    date_iso: 2018-02
    date_display: Feb 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.451
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: 3D InfoGraph
    model_plain: 3D InfoGraph
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.08092'
    title: 'GCoT: Chain-of-Thought Prompt Learning for Graphs'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.45
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0919
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPRGNN
    model_plain: GPRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.17185'
    title: 'Robustness in Text-Attributed Graph Learning: Insights, Trade-offs, and
      New Defenses'
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/Leirunlin/TGRB
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4498
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0068000000000000005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HARP(N2V)
    model_plain: HARP(N2V)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.448
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CCGC
    model_plain: CCGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.13368'
    title: Scalable Attribute-Missing Graph Clustering via Neighborhood Differentiation
    date: Jul 9, 2025
    date_iso: '2025-07-09'
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.448
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0213
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FastGCN (512)
    model_plain: FastGCN (512)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.07323'
    title: Layer-Dependent Importance Sampling for Training Deep and Large Graph Convolutional
      Networks
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/acbull/LADIES
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.446
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.108
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: VGAE
    model_plain: VGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.01210'
    title: Attributed Graph Clustering via Adaptive Graph Convolution
    date: Jun 2019
    date_iso: 2019-06
    date_display: Jun 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4438
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SUBLIME
    model_plain: SUBLIME
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15183'
    title: 'GraphEdit: Large Language Models for Graph Structure Learning'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/HKUDS/GraphEdit
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4373
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0708
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.4333
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.036
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPF
    model_plain: GPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.08092'
    title: 'GCoT: Chain-of-Thought Prompt Learning for Graphs'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.4328
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0882
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DeepWalk
    model_plain: DeepWalk
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.02907'
    title: Semi-Supervised Classification with Graph Convolutional Networks
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/tkipf/gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.432
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphEmb
    model_plain: GraphEmb
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1603.08861'
    title: Revisiting Semi-Supervised Learning with Graph Embeddings
    date: Mar 29, 2016
    date_iso: '2016-03-29'
    date_display: Mar 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.432
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HARP(DW)
    model_plain: HARP(DW)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.432
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ProG
    model_plain: ProG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.08092'
    title: 'GCoT: Chain-of-Thought Prompt Learning for Graphs'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.4317
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0849
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphCL
    model_plain: GraphCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.08092'
    title: 'GCoT: Chain-of-Thought Prompt Learning for Graphs'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.4312
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0961
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Transformer
    model_plain: Transformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.10946'
    title: Causally-guided Regularization of Graph Attention Improves Generalizability
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.43
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.09
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Node2Vec
    model_plain: Node2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.03670'
    title: 'CDC: A Simple Framework for Complex Data Clustering This work was supported
      by the National Natural Science Foundation of China Grant 62276053. Corresponding
      author: Erlin Pan Z. Kang, X. Xie, B. Li, E. Pan are with the School of Computer
      Science and Engineering, University of Electronic Science and Technology of
      China, Chengdu, China (e-mail: zkang@uestc.edu.cn; x624361380@outlook.com; bingheng86,
      wujisixsix6@gmail.com).'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.421
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: BNLL
    model_plain: BNLL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4157
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0117
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: RAG-GFM
    model_plain: RAG-GFM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.15124'
    title: 'RAG-GFM: Overcoming In-Memory Bottlenecks in Graph Foundation Models via
      Retrieval-Augmented Generation'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: https://github.com/RingBDStack/RAG-GFM
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.415
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.03
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: OFA
    model_plain: OFA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4131
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: METIS
    model_plain: METIS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.03670'
    title: 'CDC: A Simple Framework for Complex Data Clustering This work was supported
      by the National Natural Science Foundation of China Grant 62276053. Corresponding
      author: Erlin Pan Z. Kang, X. Xie, B. Li, E. Pan are with the School of Computer
      Science and Engineering, University of Electronic Science and Technology of
      China, Chengdu, China (e-mail: zkang@uestc.edu.cn; x624361380@outlook.com; bingheng86,
      wujisixsix6@gmail.com).'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.413
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAE
    model_plain: GAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.01210'
    title: Attributed Graph Clustering via Adaptive Graph Convolution
    date: Jun 2019
    date_iso: 2019-06
    date_display: Jun 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4126
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAE
    model_plain: GAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1802.04407'
    title: Adversarially Regularized Graph Autoencoder for Graph Embedding
    date: Feb 2018
    date_iso: 2018-02
    date_display: Feb 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.408
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphCL SpikingGPF
    model_plain: GraphCL SpikingGPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4076
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0887
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: UniGraph
    model_plain: UniGraph
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.15124'
    title: 'RAG-GFM: Overcoming In-Memory Bottlenecks in Graph Foundation Models via
      Retrieval-Augmented Generation'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: https://github.com/RingBDStack/RAG-GFM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.405
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.031
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCOPE
    model_plain: GCOPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.15124'
    title: 'RAG-GFM: Overcoming In-Memory Bottlenecks in Graph Foundation Models via
      Retrieval-Augmented Generation'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: https://github.com/RingBDStack/RAG-GFM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.404
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.046
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphMAE SpikingGPF
    model_plain: GraphMAE SpikingGPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4035
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0854
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ZeroG
    model_plain: ZeroG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.15124'
    title: 'RAG-GFM: Overcoming In-Memory Bottlenecks in Graph Foundation Models via
      Retrieval-Augmented Generation'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: https://github.com/RingBDStack/RAG-GFM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.397
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.059
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DeepWalk
    model_plain: DeepWalk
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.12140'
    title: Graph Few-Shot Learning via Adaptive Spectrum Experts and Cross-Set Distribution
      Calibration
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/KEAML-JLU/GRACE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3956
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0279
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAMGPT
    model_plain: SAMGPT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.15124'
    title: 'RAG-GFM: Overcoming In-Memory Bottlenecks in Graph Foundation Models via
      Retrieval-Augmented Generation'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: https://github.com/RingBDStack/RAG-GFM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.387
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.064
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DMoN
    model_plain: DMoN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.03670'
    title: 'CDC: A Simple Framework for Complex Data Clustering This work was supported
      by the National Natural Science Foundation of China Grant 62276053. Corresponding
      author: Erlin Pan Z. Kang, X. Xie, B. Li, E. Pan are with the School of Computer
      Science and Engineering, University of Electronic Science and Technology of
      China, Chengdu, China (e-mail: zkang@uestc.edu.cn; x624361380@outlook.com; bingheng86,
      wujisixsix6@gmail.com).'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.385
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: K-means
    model_plain: K-means
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.01210'
    title: Attributed Graph Clustering via Adaptive Graph Convolution
    date: Jun 2019
    date_iso: 2019-06
    date_display: Jun 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3849
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SimGRACE SpikingGPF
    model_plain: SimGRACE SpikingGPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3828
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0566
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: EdgePred SpikingGPF
    model_plain: EdgePred SpikingGPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3813
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0838
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: BGRL
    model_plain: BGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3802
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0146
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: OFA
    model_plain: OFA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.11235'
    title: 'ZeroG: Investigating Cross-dataset Zero-shot Transferability in Graphs'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/NineAbyss/ZeroG
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.3792
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MDGPT
    model_plain: MDGPT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.15124'
    title: 'RAG-GFM: Overcoming In-Memory Bottlenecks in Graph Foundation Models via
      Retrieval-Augmented Generation'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: https://github.com/RingBDStack/RAG-GFM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.379
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.072
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CAL CausalGAT
    model_plain: CAL CausalGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.10946'
    title: Causally-guided Regularization of Graph Attention Improves Generalizability
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.37
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MDGFM
    model_plain: MDGFM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.15124'
    title: 'RAG-GFM: Overcoming In-Memory Bottlenecks in Graph Foundation Models via
      Retrieval-Augmented Generation'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: https://github.com/RingBDStack/RAG-GFM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.363
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.062
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DeepWalk
    model_plain: DeepWalk
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.01210'
    title: Attributed Graph Clustering via Adaptive Graph Convolution
    date: Jun 2019
    date_iso: 2019-06
    date_display: Jun 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3615
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphCL GPF
    model_plain: GraphCL GPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3477
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.1346
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphMAE
    model_plain: GraphMAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.11235'
    title: 'ZeroG: Investigating Cross-dataset Zero-shot Transferability in Graphs'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/NineAbyss/ZeroG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3462
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: VGAE
    model_plain: VGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1802.04407'
    title: Adversarially Regularized Graph Autoencoder for Graph Embedding
    date: Feb 2018
    date_iso: 2018-02
    date_display: Feb 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.344
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphMAE GPF
    model_plain: GraphMAE GPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3425
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.1338
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphMAE GPF-plus
    model_plain: GraphMAE GPF-plus
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.339
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.1305
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphCL GPF-plus
    model_plain: GraphCL GPF-plus
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3373
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.1174
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DeepWalk
    model_plain: DeepWalk
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1802.04407'
    title: Adversarially Regularized Graph Autoencoder for Graph Embedding
    date: Feb 2018
    date_iso: 2018-02
    date_display: Feb 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.337
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: EdgePred GPF-plus
    model_plain: EdgePred GPF-plus
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3315
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.1132
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: EdgePred GPF
    model_plain: EdgePred GPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3301
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.1051
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DNGR
    model_plain: DNGR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1802.04407'
    title: Adversarially Regularized Graph Autoencoder for Graph Embedding
    date: Feb 2018
    date_iso: 2018-02
    date_display: Feb 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.326
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DNGR
    model_plain: DNGR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.01210'
    title: Attributed Graph Clustering via Adaptive Graph Convolution
    date: Jun 2019
    date_iso: 2019-06
    date_display: Jun 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3259
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SimGRACE GPF-plus
    model_plain: SimGRACE GPF-plus
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3251
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.1175
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
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
    - 0.3167
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.1089
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphCL All-in-One
    model_plain: GraphCL All-in-One
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3144
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.074
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.15124'
    title: 'RAG-GFM: Overcoming In-Memory Bottlenecks in Graph Foundation Models via
      Retrieval-Augmented Generation'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: https://github.com/RingBDStack/RAG-GFM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.314
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.041
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: EdgePred Fine-Tuning
    model_plain: EdgePred Fine-Tuning
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3111
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.098
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Roberta
    model_plain: Roberta
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.11235'
    title: 'ZeroG: Investigating Cross-dataset Zero-shot Transferability in Graphs'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/NineAbyss/ZeroG
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.3095
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SimGRACE GPF
    model_plain: SimGRACE GPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3057
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0977
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphMAE Fine-Tuning
    model_plain: GraphMAE Fine-Tuning
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3057
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.108
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphCL Fine-Tuning
    model_plain: GraphCL Fine-Tuning
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3053
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.1063
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: EdgePred All-in-One
    model_plain: EdgePred All-in-One
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.301
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.067
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SubG-Con
    model_plain: SubG-Con
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0091
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: RMSC
    model_plain: RMSC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1802.04407'
    title: Adversarially Regularized Graph Autoencoder for Graph Embedding
    date: Feb 2018
    date_iso: 2018-02
    date_display: Feb 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.295
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SimGRACE Fine-Tuning
    model_plain: SimGRACE Fine-Tuning
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2865
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.1224
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SimGRACE All-in-One
    model_plain: SimGRACE All-in-One
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2856
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0662
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphMAE All-in-One
    model_plain: GraphMAE All-in-One
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2856
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0662
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.08092'
    title: 'GCoT: Chain-of-Thought Prompt Learning for Graphs'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2771
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0874
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: H2GCN
    model_plain: H2GCN
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
    - 0.2722
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0157
    - null
    - null
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
    arxiv_id: '2502.08092'
    title: 'GCoT: Chain-of-Thought Prompt Learning for Graphs'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2636
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0903
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Spectral
    model_plain: Spectral
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.01210'
    title: Attributed Graph Clustering via Adaptive Graph Convolution
    date: Jun 2019
    date_iso: 2019-06
    date_display: Jun 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2591
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPPT
    model_plain: GPPT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2553
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0348
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Spectral
    model_plain: Spectral
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1802.04407'
    title: Adversarially Regularized Graph Autoencoder for Graph Embedding
    date: Feb 2018
    date_iso: 2018-02
    date_display: Feb 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.239
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Sbert
    model_plain: Sbert
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.11235'
    title: 'ZeroG: Investigating Cross-dataset Zero-shot Transferability in Graphs'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/NineAbyss/ZeroG
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.2376
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphEncoder
    model_plain: GraphEncoder
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1802.04407'
    title: Adversarially Regularized Graph Autoencoder for Graph Embedding
    date: Feb 2018
    date_iso: 2018-02
    date_display: Feb 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.225
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FA
    model_plain: FA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2231
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0034
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.11235'
    title: 'ZeroG: Investigating Cross-dataset Zero-shot Transferability in Graphs'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/NineAbyss/ZeroG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2112
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: RolX
    model_plain: RolX
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.09025'
    title: Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/mtang724/NWR-GAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.209
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0072
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphWave
    model_plain: GraphWave
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.09025'
    title: Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/mtang724/NWR-GAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2079
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0159
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphCL
    model_plain: GraphCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.11235'
    title: 'ZeroG: Investigating Cross-dataset Zero-shot Transferability in Graphs'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/NineAbyss/ZeroG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2059
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LLaGA
    model_plain: LLaGA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1952
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FastGCN (64)
    model_plain: FastGCN (64)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.07323'
    title: Layer-Dependent Importance Sampling for Training Deep and Large Graph Convolutional
      Networks
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/acbull/LADIES
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.192
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.027
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1524
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphGPS
    model_plain: GraphGPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1393
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphMAE
    model_plain: GraphMAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0811
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AMEN
    model_plain: AMEN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.00113'
    title: Anomaly Detection on Attributed Networks via Contrastive Self-Supervised
      Learning
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.6154
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Radar
    model_plain: Radar
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.00113'
    title: Anomaly Detection on Attributed Networks via Contrastive Self-Supervised
      Learning
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.6709
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ANOMALOUS
    model_plain: ANOMALOUS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.00113'
    title: Anomaly Detection on Attributed Networks via Contrastive Self-Supervised
      Learning
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.6307
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DOMINANT
    model_plain: DOMINANT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.00113'
    title: Anomaly Detection on Attributed Networks via Contrastive Self-Supervised
      Learning
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.8251
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.00113'
    title: Anomaly Detection on Attributed Networks via Contrastive Self-Supervised
      Learning
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.8293
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CoLA
    model_plain: CoLA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.00113'
    title: Anomaly Detection on Attributed Networks via Contrastive Self-Supervised
      Learning
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.8968
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Adamic Adar
    model_plain: Adamic Adar
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1803.00816'
    title: arXiv:1803.00816
    date: Mar 2018
    date_iso: 2018-03
    date_display: Mar 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7782
    - null
    - 0.8869
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DC-SBM
    model_plain: DC-SBM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1803.00816'
    title: arXiv:1803.00816
    date: Mar 2018
    date_iso: 2018-03
    date_display: Mar 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9313
    - null
    - 0.9477
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Node2Vec
    model_plain: Node2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1803.00816'
    title: arXiv:1803.00816
    date: Mar 2018
    date_iso: 2018-03
    date_display: Mar 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9458
    - null
    - 0.9529
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: VGAE
    model_plain: VGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1803.00816'
    title: arXiv:1803.00816
    date: Mar 2018
    date_iso: 2018-03
    date_display: Mar 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9631
    - null
    - 0.9511
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NetGAN (500K)
    model_plain: NetGAN (500K)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1803.00816'
    title: arXiv:1803.00816
    date: Mar 2018
    date_iso: 2018-03
    date_display: Mar 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9193
    - null
    - 0.9518
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NetGAN (100M)
    model_plain: NetGAN (100M)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1803.00816'
    title: arXiv:1803.00816
    date: Mar 2018
    date_iso: 2018-03
    date_display: Mar 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9689
    - null
    - 0.963
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MF
    model_plain: MF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.7592
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.0325
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.9625
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.002
    - null
    - null
    - null
  - model: SAGE
    model_plain: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.9739
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.0015
    - null
    - null
    - null
  - model: SEAL
    model_plain: SEAL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.8852
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.014
    - null
    - null
    - null
  - model: BUDDY
    model_plain: BUDDY
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.9672
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.0026
    - null
    - null
    - null
  - model: Neo-GNN
    model_plain: Neo-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.9489
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.006
    - null
    - null
    - null
  - model: NCN
    model_plain: NCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.9704
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.0026
    - null
    - null
    - null
  - model: NCNC
    model_plain: NCNC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.9765
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.003
    - null
    - null
    - null
  - model: NBFNet
    model_plain: NBFNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.9106
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.0015
    - null
    - null
    - null
  - model: PEG
    model_plain: PEG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.9615
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.0041
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - 0.5923
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.007
    - null
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
    - null
    - null
    - null
    - null
    - null
    - 0.3351
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.007
    - null
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
    - null
    - null
    - null
    - null
    - null
    - 0.6842
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.006
    - null
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
    - null
    - null
    - null
    - null
    - null
    - 0.6892
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.006
    - null
  - model: JK-Net
    model_plain: JK-Net
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
    - null
    - null
    - null
    - null
    - null
    - 0.6811
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.007
    - null
  - model: MixHop
    model_plain: MixHop
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
    - null
    - null
    - null
    - null
    - null
    - 0.6774
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.013
    - null
  - model: GCNII
    model_plain: GCNII
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
    - null
    - null
    - null
    - null
    - null
    - 0.6811
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.017
    - null
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
    - null
    - null
    - null
    - null
    - null
    - 0.6464
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.009
    - null
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
    - null
    - null
    - null
    - null
    - null
    - 0.6868
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.011
    - null
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
    - null
    - null
    - null
    - null
    - null
    - 0.6914
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.016
    - null
  - model: Katz Index
    model_plain: Katz Index
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.12865'
    title: arXiv:2409.12865
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/jnanliu/KnowFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.81
    - null
    - null
    - null
    - 0.768
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Personalized PageRank
    model_plain: Personalized PageRank
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.12865'
    title: arXiv:2409.12865
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/jnanliu/KnowFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.814
    - null
    - null
    - null
    - 0.762
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SimRank
    model_plain: SimRank
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.12865'
    title: arXiv:2409.12865
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/jnanliu/KnowFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.805
    - null
    - null
    - null
    - 0.755
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DeepWalk
    model_plain: DeepWalk
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.12865'
    title: arXiv:2409.12865
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/jnanliu/KnowFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.836
    - null
    - null
    - null
    - 0.805
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LINE
    model_plain: LINE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.12865'
    title: arXiv:2409.12865
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/jnanliu/KnowFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.868
    - null
    - null
    - null
    - 0.838
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: VGAE
    model_plain: VGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.12865'
    title: arXiv:2409.12865
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/jnanliu/KnowFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.92
    - null
    - null
    - null
    - 0.908
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: S-VGAE
    model_plain: S-VGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.12865'
    title: arXiv:2409.12865
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/jnanliu/KnowFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.952
    - null
    - null
    - null
    - 0.947
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SEAL
    model_plain: SEAL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.12865'
    title: arXiv:2409.12865
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/jnanliu/KnowFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.924
    - null
    - null
    - null
    - 0.905
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TLC-GNN
    model_plain: TLC-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.12865'
    title: arXiv:2409.12865
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/jnanliu/KnowFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.916
    - null
    - null
    - null
    - 0.909
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NBFNet
    model_plain: NBFNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.12865'
    title: arXiv:2409.12865
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/jnanliu/KnowFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.936
    - null
    - null
    - null
    - 0.923
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: KnowFormer
    model_plain: KnowFormer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.12865'
    title: arXiv:2409.12865
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/jnanliu/KnowFormer
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.95
    - null
    - null
    - null
    - 0.941
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Diff
    model_plain: Diff
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.04236'
    title: Graph Pooling via Ricci Flow
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.24
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.12
  - model: Mincut
    model_plain: Mincut
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.04236'
    title: Graph Pooling via Ricci Flow
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.31
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.04
  - model: DMoN
    model_plain: DMoN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.04236'
    title: Graph Pooling via Ricci Flow
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.29
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.03
  - model: TV
    model_plain: TV
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.04236'
    title: Graph Pooling via Ricci Flow
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.3
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.05
  - model: ORC (us)
    model_plain: ORC (us)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.04236'
    title: Graph Pooling via Ricci Flow
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.35
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.04
  - model: DEC
    model_plain: DEC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.2812
    - null
    - null
    - null
    - null
    - 0.2834
    metric_stds:
    - null
    - null
    - 0.0036
    - null
    - null
    - null
    - null
    - 0.003
  - model: DCN
    model_plain: DCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.2931
    - null
    - null
    - null
    - null
    - 0.2764
    metric_stds:
    - null
    - null
    - 0.0014
    - null
    - null
    - null
    - null
    - 0.0008
  - model: IDEC
    model_plain: IDEC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.257
    - null
    - null
    - null
    - null
    - 0.2717
    metric_stds:
    - null
    - null
    - 0.0265
    - null
    - null
    - null
    - null
    - 0.024
  - model: AdaGAE
    model_plain: AdaGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.2419
    - null
    - null
    - null
    - null
    - 0.2779
    metric_stds:
    - null
    - null
    - 0.0085
    - null
    - null
    - null
    - null
    - 0.0047
  - model: MGAE
    model_plain: MGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.3355
    - null
    - null
    - null
    - null
    - 0.3463
    metric_stds:
    - null
    - null
    - 0.0118
    - null
    - null
    - null
    - null
    - 0.0065
  - model: DAEGC
    model_plain: DAEGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.3778
    - null
    - null
    - null
    - null
    - 0.3641
    metric_stds:
    - null
    - null
    - 0.0124
    - null
    - null
    - null
    - null
    - 0.0086
  - model: ARGVA
    model_plain: ARGVA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.3432
    - null
    - null
    - null
    - null
    - 0.344
    metric_stds:
    - null
    - null
    - 0.007
    - null
    - null
    - null
    - null
    - 0.0071
  - model: SDCN
    model_plain: SDCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.4017
    - null
    - null
    - null
    - null
    - 0.3871
    metric_stds:
    - null
    - null
    - 0.0043
    - null
    - null
    - null
    - null
    - 0.0032
  - model: AGE
    model_plain: AGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.4531
    - null
    - null
    - null
    - null
    - 0.4493
    metric_stds:
    - null
    - null
    - 0.0041
    - null
    - null
    - null
    - null
    - 0.0053
  - model: MVGRL
    model_plain: MVGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.3418
    - null
    - null
    - null
    - null
    - 0.4069
    metric_stds:
    - null
    - null
    - 0.0173
    - null
    - null
    - null
    - null
    - 0.0093
  - model: DFCN
    model_plain: DFCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.455
    - null
    - null
    - null
    - null
    - 0.439
    metric_stds:
    - null
    - null
    - 0.003
    - null
    - null
    - null
    - null
    - 0.002
  - model: GDCL
    model_plain: GDCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.4107
    - null
    - null
    - null
    - null
    - 0.3952
    metric_stds:
    - null
    - null
    - 0.0096
    - null
    - null
    - null
    - null
    - 0.0038
  - model: GCA
    model_plain: GCA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.352
    - null
    - null
    - null
    - null
    - 0.3615
    metric_stds:
    - null
    - null
    - 0.0096
    - null
    - null
    - null
    - null
    - 0.0078
  - model: MCGC
    model_plain: MCGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.3754
    - null
    - null
    - null
    - null
    - 0.3911
    metric_stds:
    - null
    - null
    - 0.0012
    - null
    - null
    - null
    - null
    - 0.0006
  - model: AutoSSL
    model_plain: AutoSSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.3873
    - null
    - null
    - null
    - null
    - 0.4067
    metric_stds:
    - null
    - null
    - 0.0055
    - null
    - null
    - null
    - null
    - 0.0084
  - model: AGC-DRR
    model_plain: AGC-DRR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.4534
    - null
    - null
    - null
    - null
    - 0.4328
    metric_stds:
    - null
    - null
    - 0.0233
    - null
    - null
    - null
    - null
    - 0.0141
  - model: DCRNN
    model_plain: DCRNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.4764
    - null
    - null
    - null
    - null
    - 0.4586
    metric_stds:
    - null
    - null
    - 0.003
    - null
    - null
    - null
    - null
    - 0.0035
  - model: AFGRL
    model_plain: AFGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.1432
    - null
    - null
    - null
    - null
    - 0.1517
    metric_stds:
    - null
    - null
    - 0.0078
    - null
    - null
    - null
    - null
    - 0.0047
  - model: ProGCL
    model_plain: ProGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.3616
    - null
    - null
    - null
    - null
    - 0.3959
    metric_stds:
    - null
    - null
    - 0.0111
    - null
    - null
    - null
    - null
    - 0.0039
  - model: SUBLIME
    model_plain: SUBLIME
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.4421
    - null
    - null
    - null
    - null
    - 0.4315
    metric_stds:
    - null
    - null
    - 0.0054
    - null
    - null
    - null
    - null
    - 0.0014
  - model: RGC
    model_plain: RGC
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.4617
    - null
    - null
    - null
    - null
    - 0.4506
    metric_stds:
    - null
    - null
    - 0.0146
    - null
    - null
    - null
    - null
    - 0.0093
  - model: K-means
    model_plain: K-means
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.1297
    - null
    - null
    - null
    - null
    - 0.347
    metric_stds:
    - null
    - null
    - 0.0332
    - null
    - null
    - null
    - null
    - 0.0066
  - model: GMM
    model_plain: GMM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.1503
    - null
    - null
    - null
    - null
    - 0.3416
    metric_stds:
    - null
    - null
    - 0.0102
    - null
    - null
    - null
    - null
    - 0.01
  - model: DBSCAN
    model_plain: DBSCAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.0737
    - null
    - null
    - null
    - null
    - 0.3846
    metric_stds:
    - null
    - null
    - 0.0107
    - null
    - null
    - null
    - null
    - 0.0037
  - model: DPCA
    model_plain: DPCA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.1242
    - null
    - null
    - null
    - null
    - 0.143
    metric_stds:
    - null
    - null
    - 0.0094
    - null
    - null
    - null
    - null
    - 0.004
  milestones:
  - value: 0.745
    std: 0.011
    model: CNNs
    arxiv_id: '1312.6203'
    title: Spectral Networks and Locally Connected Networks on Graphs
    date: '2013-12-21'
  - value: 0.756
    std: 0.011
    model: Graphormer
    arxiv_id: '1710.10321'
    title: arXiv:1710.10321
    date: 2017-10
  - value: 0.88
    std: null
    model: GCN
    arxiv_id: '1805.07984'
    title: Adversarial Attacks on Neural Networks for Graph Data
    date: 2018-05
  - value: 0.897
    std: 0.021
    model: Policy-GNN
    arxiv_id: '2006.15097'
    title: 'Policy-GNN: Aggregation Optimization for Graph Neural Networks'
    date: 2020-06
  - value: 0.952
    std: 0.002
    model: S-VAE/VGAE
    arxiv_id: '2407.09468'
    title: 'Beyond Euclid: An Illustrated Guide to Modern Machine Learning with Geometric,
      Topological, and Algebraic Structures'
    date: 2024-07
---

