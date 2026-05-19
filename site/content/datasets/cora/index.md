---
title: Cora
slug: cora
benchmark: Classic
task_type: node_classification
description: Citation network node classification (7 classes).
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.Planetoid.html
stats:
  num_graphs: null
  avg_nodes: 2708.0
  avg_edges: 10556.0
  num_classes: 7
result_count: 399
best_model:
  model: GPM
  value: 0.9285
  metric: Accuracy
variants:
- slug: random-10-fold
  name: Random 10-fold
  notes: 10-fold cross-validation; results not directly comparable to Planetoid.
  is_standard: false
  primary_metric: Accuracy
  higher_is_better: true
  metrics:
  - Accuracy
  - F1
  - NMI
  rows:
  - model: GPM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9285
    - null
    - null
    metric_stds:
    - 0.0054
    - null
    - null
  - model: TRIGON
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9170999999999999
    - null
    - null
    metric_stds:
    - 0.0029
    - null
    - null
  - model: DR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9139
    - null
    - null
    metric_stds:
    - 0.0024
    - null
    - null
  - model: LLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8995
    - null
    - null
    metric_stds:
    - 0.0201
    - null
    - null
  - model: ANS-GT + HDSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8967
    - null
    - null
    metric_stds:
    - 0.0039
    - null
    - null
  - model: GrokFormer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: '2024-11-26'
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8957
    - null
    - null
    metric_stds:
    - 0.0143
    - null
    - null
  - model: GAT+JK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8952
    - null
    - null
    metric_stds:
    - 0.0043
    - null
    - null
  - model: ACMII-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8947
    - null
    - null
    metric_stds:
    - 0.0108
    - null
    - null
  - model: ParaFormer_GPRGNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.894
    - null
    - null
    metric_stds:
    - 0.009000000000000001
    - null
    - null
  - model: ACMII-Snowball-3
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8936
    - null
    - null
    metric_stds:
    - 0.0126
    - null
    - null
  - model: Snowball-2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8933
    - null
    - null
    metric_stds:
    - 0.013
    - null
    - null
  - model: ACMGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8933
    - null
    - null
    metric_stds:
    - 0.0081
    - null
    - null
  - model: HiGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: '2024-11-26'
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8923
    - null
    - null
    metric_stds:
    - 0.0023
    - null
    - null
  - model: ACM-GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.89
    - null
    - null
    metric_stds:
    - 0.0135
    - null
    - null
  - model: JacobiConv
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: '2024-11-26'
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8898
    - null
    - null
    metric_stds:
    - 0.0046
    - null
    - null
  - model: GrokFilter
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: '2024-11-26'
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8898
    - null
    - null
    metric_stds:
    - 0.0125
    - null
    - null
  - model: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.492
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8893
    - null
    - null
    metric_stds:
    - 0.0137
    - null
    - null
  - model: GCN (LCP)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14864'
    title: Effective Structural Encodings via Local Curvature Profiles
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.889
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
  - model: FAGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8885
    - null
    - null
    metric_stds:
    - 0.0136
    - null
    - null
  - model: ACM-Snowball-2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8883
    - null
    - null
    metric_stds:
    - 0.0149
    - null
    - null
  - model: RUM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8874
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
  - model: NodeFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.887
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
  - model: ParaFormer_GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.887
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
  - model: ParaFormer (a)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.887
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: Coarformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8869
    - null
    - null
    metric_stds:
    - 0.0082
    - null
    - null
  - model: HopGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: '2024-11-26'
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8868
    - null
    - null
    metric_stds:
    - 0.0106
    - null
    - null
  - model: SpecFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: '2024-11-26'
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8857
    - null
    - null
    metric_stds:
    - 0.0101
    - null
    - null
  - model: HN-1
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.16767'
    title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed Graphs as
      Effectively as We Expected'
    date: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8856
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
  - model: BernNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8852
    - null
    - null
    metric_stds:
    - 0.0095
    - null
    - null
  - model: + DIGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8831
    - null
    - null
    metric_stds:
    - 0.0029
    - null
    - null
  - model: GLoGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.883
    - null
    - null
    metric_stds:
    - 0.011000000000000001
    - null
    - null
  - model: GPRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8827
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
  - model: ChebNet + NBA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8823
    - null
    - null
    metric_stds:
    - 0.0159
    - null
    - null
  - model: Nagphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.882
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
  - model: CoBFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.882
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
  - model: GCN (SUB)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14864'
    title: Effective Structural Encodings via Local Curvature Profiles
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.881
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
  - model: AFR-4
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.881
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
  - model: SGFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8809999999999999
    - null
    - null
    metric_stds:
    - 0.006999999999999999
    - null
    - null
  - model: ND
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.16767'
    title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed Graphs as
      Effectively as We Expected'
    date: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8807
    - null
    - null
    metric_stds:
    - 0.0074
    - null
    - null
  - model: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.88
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
  - model: GCN (LA)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14864'
    title: Effective Structural Encodings via Local Curvature Profiles
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.88
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
  - model: ChebNet + NBA+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8795
    - null
    - null
    metric_stds:
    - 0.0217
    - null
    - null
  - model: BORF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.879
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
  - model: GTR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8786
    - null
    - null
    metric_stds:
    - 0.0028000000000000004
    - null
    - null
  - model: H2GCN-2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16560'
    title: Algorithmic Graph Tasks
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: https://github.com/nec-research/Adaptive-Message-Passing
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8781
    - null
    - null
    metric_stds:
    - 0.013500000000000002
    - null
    - null
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8778
    - null
    - null
    metric_stds:
    - 0.0096
    - null
    - null
  - model: Base (GCN)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8773000000000001
    - null
    - null
    metric_stds:
    - 0.0025
    - null
    - null
  - model: SRDF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8773000000000001
    - null
    - null
    metric_stds:
    - 0.0031
    - null
    - null
  - model: EGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8769
    - null
    - null
    metric_stds:
    - 0.0125
    - null
    - null
  - model: Polynormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: '2024-11-26'
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8767
    - null
    - null
    metric_stds:
    - 0.0128
    - null
    - null
  - model: Base (GAT)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8765000000000001
    - null
    - null
    metric_stds:
    - 0.0024
    - null
    - null
  - model: Gophormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8765
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
  - model: ACM-SGC-1
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8764
    - null
    - null
    metric_stds:
    - 0.0099
    - null
    - null
  - model: MixHop
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16560'
    title: Algorithmic Graph Tasks
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: https://github.com/nec-research/Adaptive-Message-Passing
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8761
    - null
    - null
    metric_stds:
    - 0.0085
    - null
    - null
  - model: GCN (RW)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14864'
    title: Effective Structural Encodings via Local Curvature Profiles
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.876
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
  - model: Llama2-7B (ND)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.16767'
    title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed Graphs as
      Effectively as We Expected'
    date: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.8758
    - null
    - null
    metric_stds:
    - 0.0059
    - null
    - null
  - model: JDR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8754000000000001
    - null
    - null
    metric_stds:
    - 0.0025
    - null
    - null
  - model: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8752
    - null
    - null
    metric_stds:
    - 0.0061
    - null
    - null
  - model: AFR-3
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.875
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
  - model: Llama2-7B (HN-1)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.16767'
    title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed Graphs as
      Effectively as We Expected'
    date: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.8745
    - null
    - null
    metric_stds:
    - 0.0019
    - null
    - null
  - model: NodeFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: '2024-11-26'
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8732
    - null
    - null
    metric_stds:
    - 0.0092
    - null
    - null
  - model: NBA-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8722
    - null
    - null
    metric_stds:
    - 0.0095
    - null
    - null
  - model: GAT + NBA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8722
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
  - model: CPGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.872
    - null
    - null
    metric_stds:
    - 0.011000000000000001
    - null
    - null
  - model: NBA-GCN+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.872
    - null
    - null
    metric_stds:
    - 0.0129
    - null
    - null
  - model: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.16767'
    title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed Graphs as
      Effectively as We Expected'
    date: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8709
    - null
    - null
    metric_stds:
    - 0.0066
    - null
    - null
  - model: GraphSAGE + NBA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8702
    - null
    - null
    metric_stds:
    - 0.0083
    - null
    - null
  - model: JKNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.87
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
  - model: + PANDA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03671'
    title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    date: '2024-06-06'
    date_iso: '2024-06-06'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.87
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
  - model: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8694
    - null
    - null
    metric_stds:
    - 0.0119
    - null
    - null
  - model: H2GCN-1
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16560'
    title: Algorithmic Graph Tasks
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: https://github.com/nec-research/Adaptive-Message-Passing
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8692
    - null
    - null
    metric_stds:
    - 0.0137
    - null
    - null
  - model: GAT + NBA+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8692
    - null
    - null
    metric_stds:
    - 0.0098
    - null
    - null
  - model: GCN+JK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.869
    - null
    - null
    metric_stds:
    - 0.0151
    - null
    - null
  - model: FOSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.869
    - null
    - null
    metric_stds:
    - 0.02
    - null
    - null
  - model: GAT (LapPE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8686
    - null
    - null
    metric_stds:
    - 0.0152
    - null
    - null
  - model: GCN-Cheby
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16560'
    title: Algorithmic Graph Tasks
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: https://github.com/nec-research/Adaptive-Message-Passing
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8676
    - null
    - null
    metric_stds:
    - 0.0095
    - null
    - null
  - model: GraphTrans
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.867
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
  - model: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.866
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
  - model: GCN (NO)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14864'
    title: Effective Structural Encodings via Local Curvature Profiles
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.866
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
  - model: GAT (LCP, LA)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14864'
    title: Effective Structural Encodings via Local Curvature Profiles
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.866
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
  - model: None
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.866
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
  - model: GRPE-FFGT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.04653'
    title: Hybrid Focal and Full-Range Attention Based Graph Transformers -
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8659
    - null
    - null
    metric_stds:
    - 0.0083
    - null
    - null
  - model: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8658
    - null
    - null
    metric_stds:
    - 0.0026
    - null
    - null
  - model: SIGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.865
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
  - model: GraphSAGE + LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.865
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
  - model: CensNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8648
    - null
    - null
    metric_stds:
    - 0.0138
    - null
    - null
  - model: SDRF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.864
    - null
    - null
    metric_stds:
    - 0.021
    - null
    - null
  - model: HGODE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 1.0
    arxiv_id: '2604.24293'
    title: 'Latent-Hysteresis Graph ODEs: Modeling Coupled Topology-Feature Evolution
      via Continuous Phase Transitions'
    date: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8626
    - null
    - null
    metric_stds:
    - 0.0078
    - null
    - null
  - model: GAT (LCP, RW)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14864'
    title: Effective Structural Encodings via Local Curvature Profiles
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.861
    - null
    - null
    metric_stds:
    - 0.015
    - null
    - null
  - model: GraphSAGE+JK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16560'
    title: Algorithmic Graph Tasks
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: https://github.com/nec-research/Adaptive-Message-Passing
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8595999999999999
    - null
    - null
    metric_stds:
    - 0.0083
    - null
    - null
  - model: GCN+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.501066
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8592
    - null
    - null
    metric_stds:
    - 0.0083
    - null
    - null
  - model: Nagphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.04653'
    title: Hybrid Focal and Full-Range Attention Based Graph Transformers -
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8577
    - null
    - null
    metric_stds:
    - 0.0135
    - null
    - null
  - model: GAT (LCP)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14864'
    title: Effective Structural Encodings via Local Curvature Profiles
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.857
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
  - model: GAT (SUB, RW)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14864'
    title: Effective Structural Encodings via Local Curvature Profiles
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.857
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
  - model: AMP_GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16560'
    title: Algorithmic Graph Tasks
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: https://github.com/nec-research/Adaptive-Message-Passing
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8568000000000001
    - null
    - null
    metric_stds:
    - 0.0152
    - null
    - null
  - model: Cheby+JK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16560'
    title: Algorithmic Graph Tasks
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: https://github.com/nec-research/Adaptive-Message-Passing
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8549
    - null
    - null
    metric_stds:
    - 0.0127
    - null
    - null
  - model: SGC-2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8548
    - null
    - null
    metric_stds:
    - 0.0148
    - null
    - null
  - model: GENs
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8543000000000001
    - null
    - null
    metric_stds:
    - 0.0042
    - null
    - null
  - model: CO
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.16767'
    title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed Graphs as
      Effectively as We Expected'
    date: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8542
    - null
    - null
    metric_stds:
    - 0.0178
    - null
    - null
  - model: ChebNet + LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8531
    - null
    - null
    metric_stds:
    - 0.0139
    - null
    - null
  - model: GAT (SUB, LA)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14864'
    title: Effective Structural Encodings via Local Curvature Profiles
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.853
    - null
    - null
    metric_stds:
    - 0.013
    - null
    - null
  - model: Geom-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8527
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8523
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
  - model: SGC-1
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8512
    - null
    - null
    metric_stds:
    - 0.0164
    - null
    - null
  - model: CARIBOU
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.22727'
    title: Convergent Privacy Framework for Multi-layer GNNs through Contractive Message
      Passing
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.851
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: CaCoSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.27529'
    title: Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in
      GNNs
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.85
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GAT (SUB)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14864'
    title: Effective Structural Encodings via Local Curvature Profiles
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.85
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
  - model: DropSens
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.07364'
    title: Effects of Dropout on Performance in - Long-range Graph Learning Tasks
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8498
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8477
    - null
    - null
    metric_stds:
    - 0.0156
    - null
    - null
  - model: GAT (LA)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14864'
    title: Effective Structural Encodings via Local Curvature Profiles
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.847
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
  - model: SGFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.845
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
  - model: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8445999999999999
    - null
    - null
    metric_stds:
    - 0.0055000000000000005
    - null
    - null
  - model: TAPE (E (e5))
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8438
    - null
    - null
    metric_stds:
    - 0.0036
    - null
    - null
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2312.16560'
    title: Algorithmic Graph Tasks
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: https://github.com/nec-research/Adaptive-Message-Passing
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8423999999999999
    - null
    - null
    metric_stds:
    - 0.0144
    - null
    - null
  - model: EdgeGAT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.22259'
    title: Rotary Position Encodings for Graphs
    date: Sep 2025
    date_iso: 2025-09
    codebase_url: https://github.com/google-research/scenic
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.842
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
  - model: UniMP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.04653'
    title: Hybrid Focal and Full-Range Attention Based Graph Transformers -
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8418
    - null
    - null
    metric_stds:
    - 0.0139
    - null
    - null
  - model: DMD-SGC
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.841
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
  - model: GTR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.27529'
    title: Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in
      GNNs
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8406999999999999
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: SDRF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.27529'
    title: Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in
      GNNs
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8404
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GT + HDSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.839
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
  - model: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8388
    - null
    - null
    metric_stds:
    - 0.006500000000000001
    - null
    - null
  - model: IDGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8388
    - null
    - null
    metric_stds:
    - 0.0042
    - null
    - null
  - model: GraphGPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8387
    - null
    - null
    metric_stds:
    - 0.0096
    - null
    - null
  - model: GRCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8387
    - null
    - null
    metric_stds:
    - 0.0049
    - null
    - null
  - model: GAT (RW)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14864'
    title: Effective Structural Encodings via Local Curvature Profiles
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.838
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
  - model: BORF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.27529'
    title: Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in
      GNNs
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8368000000000001
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: FOSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.27529'
    title: Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in
      GNNs
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8366
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GPRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8366
    - null
    - null
    metric_stds:
    - 0.0077
    - null
    - null
  - model: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.27529'
    title: Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in
      GNNs
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.836
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: HSGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.836
    - null
    - null
    metric_stds:
    - 0.018
    - null
    - null
  - model: GATv2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.22259'
    title: Rotary Position Encodings for Graphs
    date: Sep 2025
    date_iso: 2025-09
    codebase_url: https://github.com/google-research/scenic
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.835
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
  - model: Gapformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.835
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
  - model: Polynormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8343
    - null
    - null
    metric_stds:
    - 0.009000000000000001
    - null
    - null
  - model: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.834
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
  - model: GAT (NO)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14864'
    title: Effective Structural Encodings via Local Curvature Profiles
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.834
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
  - model: SUBLIME
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.834
    - null
    - null
    metric_stds:
    - 0.0042
    - null
    - null
  - model: Framelets
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.833
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
  - model: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.833
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
  - model: Exphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8329000000000001
    - null
    - null
    metric_stds:
    - 0.013600000000000001
    - null
    - null
  - model: DIGL (PPR)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.07364'
    title: Effects of Dropout on Performance in - Long-range Graph Learning Tasks
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8321
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: + DIGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03671'
    title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    date: '2024-06-06'
    date_iso: '2024-06-06'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.832
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
  - model: PNA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.22259'
    title: Rotary Position Encodings for Graphs
    date: Sep 2025
    date_iso: 2025-09
    codebase_url: https://github.com/google-research/scenic
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.832
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
  - model: LDS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8301
    - null
    - null
    metric_stds:
    - 0.0041
    - null
    - null
  - model: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.83
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
  - model: GRAND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.829
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
  - model: DMD-ACMP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.829
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
  - model: SDRF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.07364'
    title: Effects of Dropout on Performance in - Long-range Graph Learning Tasks
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8276
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: text-ada-embedding-002
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8272
    - null
    - null
    metric_stds:
    - 0.0069
    - null
    - null
  - model: GOKU
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.27529'
    title: Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in
      GNNs
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8266
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: DMD-GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.826
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
  - model: e5-large
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8256
    - null
    - null
    metric_stds:
    - 0.0073
    - null
    - null
  - model: TAPE (TA + E (e5))
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8256
    - null
    - null
    metric_stds:
    - 0.0073
    - null
    - null
  - model: GRPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 46.2
    arxiv_id: '2311.04653'
    title: Hybrid Focal and Full-Range Attention Based Graph Transformers -
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8252
    - null
    - null
    metric_stds:
    - 0.013
    - null
    - null
  - model: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.22259'
    title: Rotary Position Encodings for Graphs
    date: Sep 2025
    date_iso: 2025-09
    codebase_url: https://github.com/google-research/scenic
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.825
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
  - model: GSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8248
    - null
    - null
    metric_stds:
    - 0.0043
    - null
    - null
  - model: \modelname{}
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04082'
    title: 'Curve Your Attention: Mixed-Curvature Transformers for Graph Representation
      Learning'
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8232
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
  - model: DMD++
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.823
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
  - model: NodeFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.822
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
  - model: Sentence-BERT(MiniLM)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.822
    - null
    - null
    metric_stds:
    - 0.0049
    - null
    - null
  - model: SIGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.821
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
  - model: GOAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.821
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
  - model: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05697'
    title: 'Diffusing to the Top: Boost Graph Neural Networks with Minimal Hyperparameter
      Tuning'
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8205
    - null
    - null
    metric_stds:
    - 0.0081
    - null
    - null
  - model: TF-IDF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8199
    - null
    - null
    metric_stds:
    - 0.0063
    - null
    - null
  - model: SAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.04653'
    title: Hybrid Focal and Full-Range Attention Based Graph Transformers -
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8191
    - null
    - null
    metric_stds:
    - 0.0342
    - null
    - null
  - model: HC-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.819
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
  - model: None
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.07364'
    title: Effects of Dropout on Performance in - Long-range Graph Learning Tasks
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8189
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05697'
    title: 'Diffusing to the Top: Boost Graph Neural Networks with Minimal Hyperparameter
      Tuning'
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8189
    - null
    - null
    metric_stds:
    - 0.0094
    - null
    - null
  - model: ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05697'
    title: 'Diffusing to the Top: Boost Graph Neural Networks with Minimal Hyperparameter
      Tuning'
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8183
    - null
    - null
    metric_stds:
    - 0.0046
    - null
    - null
  - model: JKNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.818
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
  - model: CoGSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8176
    - null
    - null
    metric_stds:
    - 0.0024
    - null
    - null
  - model: AGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.817
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
  - model: FA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.07364'
    title: Effects of Dropout on Performance in - Long-range Graph Learning Tasks
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8165
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.816
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
  - model: TokenGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04082'
    title: 'Curve Your Attention: Mixed-Curvature Transformers for Graph Representation
      Learning'
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8142
    - null
    - null
    metric_stds:
    - 0.0079
    - null
    - null
  - model: GCN-SSM (eig(Lambda)=1)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.10818'
    title: 'On Vanishing Gradients, Over-Smoothing, and Over-Squashing in GNNs: -
      Bridging Recurrent and Graph Learning'
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.813
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: Full Graph
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17404'
    title: Spectral Greedy Coresets for Graph Neural Networks
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.812
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
  - model: Google Palm Cortex 001
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8115
    - null
    - null
    metric_stds:
    - 0.0101
    - null
    - null
  - model: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.22259'
    title: Rotary Position Encodings for Graphs
    date: Sep 2025
    date_iso: 2025-09
    codebase_url: https://github.com/google-research/scenic
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.811
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
  - model: GPRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05697'
    title: 'Diffusing to the Top: Boost Graph Neural Networks with Minimal Hyperparameter
      Tuning'
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8103
    - null
    - null
    metric_stds:
    - 0.0065
    - null
    - null
  - model: Nagphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8092
    - null
    - null
    metric_stds:
    - 0.011699999999999999
    - null
    - null
  - model: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01618'
    title: 'Operator Learning Meets Numerical Analysis: Improving Neural Networks
      through Iterative Methods'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.804
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2309.04082'
    title: 'Curve Your Attention: Mixed-Curvature Transformers for Graph Representation
      Learning'
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.804
    - null
    - null
    metric_stds:
    - 0.0053
    - null
    - null
  - model: ProGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.803
    - null
    - null
    metric_stds:
    - 0.0057
    - null
    - null
  - model: NodeFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8028
    - null
    - null
    metric_stds:
    - 0.0082
    - null
    - null
  - model: GEN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8021
    - null
    - null
    metric_stds:
    - 0.0172
    - null
    - null
  - model: STABLE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.802
    - null
    - null
    metric_stds:
    - 0.0068
    - null
    - null
  - model: GIN (LA)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14864'
    title: Effective Structural Encodings via Local Curvature Profiles
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.801
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
  - model: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.801
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
  - model: MixHop
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05697'
    title: 'Diffusing to the Top: Boost Graph Neural Networks with Minimal Hyperparameter
      Tuning'
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8008
    - null
    - null
    metric_stds:
    - 0.0143
    - null
    - null
  - model: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04082'
    title: 'Curve Your Attention: Mixed-Curvature Transformers for Graph Representation
      Learning'
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8
    - null
    - null
    metric_stds:
    - 0.0085
    - null
    - null
  - model: HAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04082'
    title: 'Curve Your Attention: Mixed-Curvature Transformers for Graph Representation
      Learning'
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7981
    - null
    - null
    metric_stds:
    - 0.0058
    - null
    - null
  - model: GIN (LCP)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14864'
    title: Effective Structural Encodings via Local Curvature Profiles
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.798
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
  - model: \mathcal{Q}-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04082'
    title: 'Curve Your Attention: Mixed-Curvature Transformers for Graph Representation
      Learning'
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7963
    - null
    - null
    metric_stds:
    - 0.0057
    - null
    - null
  - model: GPRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7951
    - null
    - null
    metric_stds:
    - 0.0036
    - null
    - null
  - model: TAPE (E (PLM))
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7946
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
  - model: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7941
    - null
    - null
    metric_stds:
    - 0.0038
    - null
    - null
  - model: ANS-GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.794
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
  - model: RWPT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.14098'
    title: 'Toward a Graph Foundation Model: - Pre-Training Transformers With Random
      Walks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.793
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: RWPT (Pre-Train w/ all)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.14098'
    title: 'Toward a Graph Foundation Model: - Pre-Training Transformers With Random
      Walks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.793
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GIN (SUB)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14864'
    title: Effective Structural Encodings via Local Curvature Profiles
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.793
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
  - model: HGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04082'
    title: 'Curve Your Attention: Mixed-Curvature Transformers for Graph Representation
      Learning'
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.793
    - null
    - null
    metric_stds:
    - 0.0051
    - null
    - null
  - model: PIGN with GAT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01618'
    title: 'Operator Learning Meets Numerical Analysis: Improving Neural Networks
      through Iterative Methods'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.792
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
  - model: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04082'
    title: 'Curve Your Attention: Mixed-Curvature Transformers for Graph Representation
      Learning'
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7888
    - null
    - null
    metric_stds:
    - 0.0087
    - null
    - null
  - model: RWPT (Pre-Train w/ Arxiv + FB15k237 + ChEMBL)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.14098'
    title: 'Toward a Graph Foundation Model: - Pre-Training Transformers With Random
      Walks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7869
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GFT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.14098'
    title: 'Toward a Graph Foundation Model: - Pre-Training Transformers With Random
      Walks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7862
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: SGGC
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17404'
    title: Spectral Greedy Coresets for Graph Neural Networks
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.786
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
  - model: G2-GCN (GraphSAGE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.07419'
    title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    date: Jan 2026
    date_iso: 2026-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7859999999999999
    - null
    - null
    metric_stds:
    - 0.05
    - null
    - null
  - model: G2-GCN (GATv2)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.07419'
    title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    date: Jan 2026
    date_iso: 2026-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.785
    - null
    - null
    metric_stds:
    - 0.06
    - null
    - null
  - model: BS-KAGAT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.18380'
    title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: https://github.com/RomanBresson/KAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7828
    - null
    - null
    metric_stds:
    - 0.0083
    - null
    - null
  - model: RWPT (+ Token reconstruction)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.14098'
    title: 'Toward a Graph Foundation Model: - Pre-Training Transformers With Random
      Walks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7818
    - null
    - null
    metric_stds:
    - 0.0052
    - null
    - null
  - model: GIN (RW)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14864'
    title: Effective Structural Encodings via Local Curvature Profiles
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.781
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
  - model: RWPT (Context loss)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.14098'
    title: 'Toward a Graph Foundation Model: - Pre-Training Transformers With Random
      Walks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7802
    - null
    - null
    metric_stds:
    - 0.0037
    - null
    - null
  - model: RWPT (Context prediction)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.14098'
    title: 'Toward a Graph Foundation Model: - Pre-Training Transformers With Random
      Walks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7802
    - null
    - null
    metric_stds:
    - 0.0037
    - null
    - null
  - model: GCN-SSM (With B)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.10818'
    title: 'On Vanishing Gradients, Over-Smoothing, and Over-Squashing in GNNs: -
      Bridging Recurrent and Graph Learning'
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.778
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GCN (LCP, LA)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14864'
    title: Effective Structural Encodings via Local Curvature Profiles
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.778
    - null
    - null
    metric_stds:
    - 0.015
    - null
    - null
  - model: MaskGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.14098'
    title: 'Toward a Graph Foundation Model: - Pre-Training Transformers With Random
      Walks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7751
    - null
    - null
    metric_stds:
    - 0.0028
    - null
    - null
  - model: '*-w/o-GrokFilter'
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: '2024-11-26'
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7742
    - null
    - null
    metric_stds:
    - 0.0177
    - null
    - null
  - model: GCN (SUB, LA)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14864'
    title: Effective Structural Encodings via Local Curvature Profiles
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.774
    - null
    - null
    metric_stds:
    - 0.013
    - null
    - null
  - model: GAP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.22727'
    title: Convergent Privacy Framework for Multi-layer GNNs through Contractive Message
      Passing
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.771
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.767
    - null
    - null
    metric_stds:
    - 0.0042
    - null
    - null
  - model: SCGIGA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17404'
    title: Spectral Greedy Coresets for Graph Neural Networks
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.767
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
  - model: PIGN with GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01618'
    title: 'Operator Learning Meets Numerical Analysis: Improving Neural Networks
      through Iterative Methods'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.767
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
  - model: RWPT (Pre-Train w/ Arxiv)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.14098'
    title: 'Toward a Graph Foundation Model: - Pre-Training Transformers With Random
      Walks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7663
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: RWPT (+ Position reconstruction)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.14098'
    title: 'Toward a Graph Foundation Model: - Pre-Training Transformers With Random
      Walks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7661
    - null
    - null
    metric_stds:
    - 0.0044
    - null
    - null
  - model: GraphGPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.765
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
  - model: MLP-2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7644
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
  - model: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.492
    arxiv_id: '2601.07419'
    title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    date: Jan 2026
    date_iso: 2026-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.763
    - null
    - null
    metric_stds:
    - 0.023
    - null
    - null
  - model: GIN (NO)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14864'
    title: Effective Structural Encodings via Local Curvature Profiles
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.763
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
  - model: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.14098'
    title: 'Toward a Graph Foundation Model: - Pre-Training Transformers With Random
      Walks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7624
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GCN (LCP, RW)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14864'
    title: Effective Structural Encodings via Local Curvature Profiles
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.761
    - null
    - null
    metric_stds:
    - 0.016
    - null
    - null
  - model: GCN (SUB, RW)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14864'
    title: Effective Structural Encodings via Local Curvature Profiles
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.758
    - null
    - null
    metric_stds:
    - 0.016
    - null
    - null
  - model: Graphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.758
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
  - model: LASER
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.27529'
    title: Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in
      GNNs
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7576999999999999
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2506.14098'
    title: 'Toward a Graph Foundation Model: - Pre-Training Transformers With Random
      Walks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7565
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: G2-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.07419'
    title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    date: Jan 2026
    date_iso: 2026-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7559999999999999
    - null
    - null
    metric_stds:
    - 0.011000000000000001
    - null
    - null
  - model: GATv2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.07419'
    title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    date: Jan 2026
    date_iso: 2026-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.755
    - null
    - null
    metric_stds:
    - 0.027999999999999997
    - null
    - null
  - model: DPDGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.22727'
    title: Convergent Privacy Framework for Multi-layer GNNs through Contractive Message
      Passing
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.755
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GIANT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.14098'
    title: 'Toward a Graph Foundation Model: - Pre-Training Transformers With Random
      Walks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7513
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: HealHGNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7506
    - null
    - null
    metric_stds:
    - 0.0116
    - null
    - null
  - model: GraphPrompt
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.14098'
    title: 'Toward a Graph Foundation Model: - Pre-Training Transformers With Random
      Walks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7497
    - null
    - null
    metric_stds:
    - 0.0035
    - null
    - null
  - model: HGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.748
    - null
    - null
    metric_stds:
    - 0.011000000000000001
    - null
    - null
  - model: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16560'
    title: Algorithmic Graph Tasks
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: https://github.com/nec-research/Adaptive-Message-Passing
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7475
    - null
    - null
    metric_stds:
    - 0.0222
    - null
    - null
  - model: FrameHGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7472
    - null
    - null
    metric_stds:
    - 0.021
    - null
    - null
  - model: SheafHyperGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7471
    - null
    - null
    metric_stds:
    - 0.0123
    - null
    - null
  - model: TAPE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7456
    - null
    - null
    metric_stds:
    - 0.0203
    - null
    - null
  - model: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.745
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
  - model: PhenomNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7445
    - null
    - null
    metric_stds:
    - 0.0096
    - null
    - null
  - model: Deep-HGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7406999999999999
    - null
    - null
    metric_stds:
    - 0.016399999999999998
    - null
    - null
  - model: SAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7402
    - null
    - null
    metric_stds:
    - 0.0101
    - null
    - null
  - model: Word2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7401
    - null
    - null
    metric_stds:
    - 0.0124
    - null
    - null
  - model: RWPT (Pre-Train w/ FB15k237)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.14098'
    title: 'Toward a Graph Foundation Model: - Pre-Training Transformers With Random
      Walks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7371
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: ED-HNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.737
    - null
    - null
    metric_stds:
    - 0.0138
    - null
    - null
  - model: \kappa-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04082'
    title: 'Curve Your Attention: Mixed-Curvature Transformers for Graph Representation
      Learning'
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.737
    - null
    - null
    metric_stds:
    - 0.0069
    - null
    - null
  - model: HES-GSL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7368
    - null
    - null
    metric_stds:
    - 0.0104
    - null
    - null
  - model: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.14098'
    title: 'Toward a Graph Foundation Model: - Pre-Training Transformers With Random
      Walks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7359
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GraphSAGE + Pairnorm
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.07419'
    title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    date: Jan 2026
    date_iso: 2026-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.735
    - null
    - null
    metric_stds:
    - 0.049
    - null
    - null
  - model: GraphMAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.14098'
    title: 'Toward a Graph Foundation Model: - Pre-Training Transformers With Random
      Walks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.731
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: AllSetTransformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7308
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
  - model: UniGCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7304999999999999
    - null
    - null
    metric_stds:
    - 0.022099999999999998
    - null
    - null
  - model: Graphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7290000000000001
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
  - model: RBF-KAGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.18380'
    title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: https://github.com/RomanBresson/KAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7277
    - null
    - null
    metric_stds:
    - 0.013500000000000002
    - null
    - null
  - model: HyperGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7276
    - null
    - null
    metric_stds:
    - 0.011200000000000002
    - null
    - null
  - model: CRAIG-Linear
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17404'
    title: Spectral Greedy Coresets for Graph Neural Networks
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.727
    - null
    - null
    metric_stds:
    - 0.029
    - null
    - null
  - model: UniGCNII (Norm. H-20-LAPE depth 2)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7268
    - null
    - null
    metric_stds:
    - 0.0136
    - null
    - null
  - model: UniGCNII (H-19-RWPEE WE depth 8)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7265
    - null
    - null
    metric_stds:
    - 0.0127
    - null
    - null
  - model: HNHN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7264
    - null
    - null
    metric_stds:
    - 0.015700000000000002
    - null
    - null
  - model: UniGCNII (no encodings depth 2)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7264
    - null
    - null
    metric_stds:
    - 0.0106
    - null
    - null
  - model: RBF-KAGAT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.18380'
    title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: https://github.com/RomanBresson/KAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7262000000000001
    - null
    - null
    metric_stds:
    - 0.016399999999999998
    - null
    - null
  - model: UniGCNII (H-19-RWPEE EE depth 2)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7259
    - null
    - null
    metric_stds:
    - 0.0125
    - null
    - null
  - model: UniGCNII (Hodge H-20-LAPE depth 2)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7252
    - null
    - null
    metric_stds:
    - 0.0138
    - null
    - null
  - model: HCHA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7242000000000001
    - null
    - null
    metric_stds:
    - 0.014199999999999999
    - null
    - null
  - model: SAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.724
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
  - model: SLAPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7228
    - null
    - null
    metric_stds:
    - 0.0097
    - null
    - null
  - model: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.14098'
    title: 'Toward a Graph Foundation Model: - Pre-Training Transformers With Random
      Walks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.721
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GCN (eig(W)=1)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.10818'
    title: 'On Vanishing Gradients, Over-Smoothing, and Over-Squashing in GNNs: -
      Bridging Recurrent and Graph Learning'
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.719
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7184
    - null
    - null
    metric_stds:
    - 0.0062
    - null
    - null
  - model: Transformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: '2024-11-26'
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7183
    - null
    - null
    metric_stds:
    - 0.0168
    - null
    - null
  - model: GQT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.13798'
    title: Learning Graph Quantized Tokenizers
    date: '2024-10-17'
    date_iso: '2024-10-17'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7181
    - null
    - null
    metric_stds:
    - 0.0021
    - null
    - null
  - model: VCR-Graphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.13798'
    title: Learning Graph Quantized Tokenizers
    date: '2024-10-17'
    date_iso: '2024-10-17'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7167
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
  - model: Nagphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.13798'
    title: Learning Graph Quantized Tokenizers
    date: '2024-10-17'
    date_iso: '2024-10-17'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7151
    - null
    - null
    metric_stds:
    - 0.0013
    - null
    - null
  - model: GRAND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.13798'
    title: Learning Graph Quantized Tokenizers
    date: '2024-10-17'
    date_iso: '2024-10-17'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7137
    - null
    - null
    metric_stds:
    - 0.0011
    - null
    - null
  - model: BGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.14098'
    title: 'Toward a Graph Foundation Model: - Pre-Training Transformers With Random
      Walks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.712
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: UniGAT (no encodings nlayer2)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7116
    - null
    - null
    metric_stds:
    - 0.0155
    - null
    - null
  - model: LRGB
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.27529'
    title: Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in
      GNNs
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7101999999999999
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.18380'
    title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: https://github.com/RomanBresson/KAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7084999999999999
    - null
    - null
    metric_stds:
    - 0.0175
    - null
    - null
  - model: AllDeepSets
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7082999999999999
    - null
    - null
    metric_stds:
    - 0.0163
    - null
    - null
  - model: GCond
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17404'
    title: Spectral Greedy Coresets for Graph Neural Networks
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.706
    - null
    - null
    metric_stds:
    - 0.037
    - null
    - null
  - model: RWPT (Pre-Train w/ ChEMBL)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.14098'
    title: 'Toward a Graph Foundation Model: - Pre-Training Transformers With Random
      Walks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7034
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: UniGCNII (LDP depth 2)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6985
    - null
    - null
    metric_stds:
    - 0.0165
    - null
    - null
  - model: GatedGraph
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6985
    - null
    - null
    metric_stds:
    - 0.0274
    - null
    - null
  - model: IDGL_knn
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6974
    - null
    - null
    metric_stds:
    - 0.0057
    - null
    - null
  - model: GATv2 + Pairnorm
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.07419'
    title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    date: Jan 2026
    date_iso: 2026-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6970000000000001
    - null
    - null
    metric_stds:
    - 0.015
    - null
    - null
  - model: SGFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.697
    - null
    - null
    metric_stds:
    - 0.0054
    - null
    - null
  - model: GCN + Pairnorm
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.07419'
    title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    date: Jan 2026
    date_iso: 2026-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.696
    - null
    - null
    metric_stds:
    - 0.055
    - null
    - null
  - model: GCN-kNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6948
    - null
    - null
    metric_stds:
    - 0.0066
    - null
    - null
  - model: UniGAT (LDP)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6931
    - null
    - null
    metric_stds:
    - 0.0223
    - null
    - null
  - model: GPRGNN_knn
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6927
    - null
    - null
    metric_stds:
    - 0.0062
    - null
    - null
  - model: OrderedGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6921
    - null
    - null
    metric_stds:
    - 0.0023
    - null
    - null
  - model: M
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6914
    - null
    - null
    metric_stds:
    - 0.0078
    - null
    - null
  - model: Exphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.13798'
    title: Learning Graph Quantized Tokenizers
    date: '2024-10-17'
    date_iso: '2024-10-17'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6909
    - null
    - null
    metric_stds:
    - 0.0072
    - null
    - null
  - model: VCR-Graphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6878
    - null
    - null
    metric_stds:
    - 0.0029
    - null
    - null
  - model: RAW-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6864
    - null
    - null
    metric_stds:
    - 0.0055
    - null
    - null
  - model: GOAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6855
    - null
    - null
    metric_stds:
    - 0.0034
    - null
    - null
  - model: DEFT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6801
    - null
    - null
    metric_stds:
    - 0.0086
    - null
    - null
  - model: 1-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.68
    - null
    - null
    metric_stds:
    - 0.0245
    - null
    - null
  - model: UniGAT (Norm. H-20-LAPE)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6789
    - null
    - null
    metric_stds:
    - 0.0237
    - null
    - null
  - model: UniGCN (H-19-RWPEE EN)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6786
    - null
    - null
    metric_stds:
    - 0.0215
    - null
    - null
  - model: GraphSAINT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.13798'
    title: Learning Graph Quantized Tokenizers
    date: '2024-10-17'
    date_iso: '2024-10-17'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6785
    - null
    - null
    metric_stds:
    - 0.0021
    - null
    - null
  - model: UniGAT (H-19-RWPEE WE)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6782
    - null
    - null
    metric_stds:
    - 0.0218
    - null
    - null
  - model: UniGAT (Hodge H-20-LAPE)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.678
    - null
    - null
    metric_stds:
    - 0.0227
    - null
    - null
  - model: UniSAGE (no encodings)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.678
    - null
    - null
    metric_stds:
    - 0.0233
    - null
    - null
  - model: UniGAT (H-19-RWPEE EE)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6776
    - null
    - null
    metric_stds:
    - 0.0191
    - null
    - null
  - model: Graphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.04653'
    title: Hybrid Focal and Full-Range Attention Based Graph Transformers -
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6771
    - null
    - null
    metric_stds:
    - 0.0078
    - null
    - null
  - model: UniGCN (no encodings)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.677
    - null
    - null
    metric_stds:
    - 0.0233
    - null
    - null
  - model: GPRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.13798'
    title: Learning Graph Quantized Tokenizers
    date: '2024-10-17'
    date_iso: '2024-10-17'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6712
    - null
    - null
    metric_stds:
    - 0.0031
    - null
    - null
  - model: ProGNN_knn
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6711
    - null
    - null
    metric_stds:
    - 0.0056
    - null
    - null
  - model: GEN_knn
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6695
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
  - model: BNPool
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.668
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
  - model: LLama 7B
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.668
    - null
    - null
    metric_stds:
    - 0.022
    - null
    - null
  - model: SEA-GWNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6674
    - null
    - null
    metric_stds:
    - 0.0079
    - null
    - null
  - model: CoGSL_knn
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6665
    - null
    - null
    metric_stds:
    - 0.0037
    - null
    - null
  - model: GSR_knn
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6628
    - null
    - null
    metric_stds:
    - 0.0059
    - null
    - null
  - model: UniGAT (HCP-FRC)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6595
    - null
    - null
    metric_stds:
    - 0.0324
    - null
    - null
  - model: BS-KAGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.18380'
    title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: https://github.com/RomanBresson/KAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6578
    - null
    - null
    metric_stds:
    - 0.0168
    - null
    - null
  - model: MixHop
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6565
    - null
    - null
    metric_stds:
    - 0.1131
    - null
    - null
  - model: UniGCNII (HCP-FRC depth 2)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6554
    - null
    - null
    metric_stds:
    - 0.0193
    - null
    - null
  - model: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6516
    - null
    - null
    metric_stds:
    - 0.0028
    - null
    - null
  - model: GAT-kNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6462
    - null
    - null
    metric_stds:
    - 0.0104
    - null
    - null
  - model: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6447
    - null
    - null
    metric_stds:
    - 0.0018
    - null
    - null
  - model: GWNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6419
    - null
    - null
    metric_stds:
    - 0.0079
    - null
    - null
  - model: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6397
    - null
    - null
    metric_stds:
    - 0.018
    - null
    - null
  - model: PPRGo
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.13798'
    title: Learning Graph Quantized Tokenizers
    date: '2024-10-17'
    date_iso: '2024-10-17'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6354
    - null
    - null
    metric_stds:
    - 0.0025
    - null
    - null
  - model: UniSAGE (LDP)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6308
    - null
    - null
    metric_stds:
    - 0.0268
    - null
    - null
  - model: GATv2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6305
    - null
    - null
    metric_stds:
    - 0.0221
    - null
    - null
  - model: UniGCN (LDP)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6296
    - null
    - null
    metric_stds:
    - 0.0289
    - null
    - null
  - model: Transformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6289
    - null
    - null
    metric_stds:
    - 0.0175
    - null
    - null
  - model: UFGConvS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6243
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6176
    - null
    - null
    metric_stds:
    - 0.0014
    - null
    - null
  - model: Scattering GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6114
    - null
    - null
    metric_stds:
    - 0.0113
    - null
    - null
  - model: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6109
    - null
    - null
    metric_stds:
    - 0.0371
    - null
    - null
  - model: GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.13798'
    title: Learning Graph Quantized Tokenizers
    date: '2024-10-17'
    date_iso: '2024-10-17'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6105
    - null
    - null
    metric_stds:
    - 0.0038
    - null
    - null
  - model: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6098
    - null
    - null
    metric_stds:
    - 0.0294
    - null
    - null
  - model: Cheb
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6054
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
  - model: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.492
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6054
    - null
    - null
    metric_stds:
    - 0.0273
    - null
    - null
  - model: IterGNN with GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01618'
    title: 'Operator Learning Meets Numerical Analysis: Improving Neural Networks
      through Iterative Methods'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.605
    - null
    - null
    metric_stds:
    - 0.175
    - null
    - null
  - model: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6033
    - null
    - null
    metric_stds:
    - 0.0226
    - null
    - null
  - model: PertGraph
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.22727'
    title: Convergent Privacy Framework for Multi-layer GNNs through Contractive Message
      Passing
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: Fine-tuned Deberta-base
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5923
    - null
    - null
    metric_stds:
    - 0.0116
    - null
    - null
  - model: GLEM-LM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5923
    - null
    - null
    metric_stds:
    - 0.0116
    - null
    - null
  - model: TAPE (TA + E (PLM))
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5923
    - null
    - null
    metric_stds:
    - 0.0116
    - null
    - null
  - model: SAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.13798'
    title: Learning Graph Quantized Tokenizers
    date: '2024-10-17'
    date_iso: '2024-10-17'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5901
    - null
    - null
    metric_stds:
    - 0.0034
    - null
    - null
  - model: WaveShrink-ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5898
    - null
    - null
    metric_stds:
    - 0.0069
    - null
    - null
  - model: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5855
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
  - model: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5823
    - null
    - null
    metric_stds:
    - 0.0099
    - null
    - null
  - model: DMON
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.579
    - null
    - null
    metric_stds:
    - 0.038
    - null
    - null
  - model: UniGCN (HCP-FRC)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5777
    - null
    - null
    metric_stds:
    - 0.031
    - null
    - null
  - model: Scattering
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5765
    - null
    - null
    metric_stds:
    - 0.0084
    - null
    - null
  - model: WaveNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5765
    - null
    - null
    metric_stds:
    - 0.0105
    - null
    - null
  - model: UniSAGE (HCP-FRC)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5735
    - null
    - null
    metric_stds:
    - 0.0315
    - null
    - null
  - model: MinCut
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.57
    - null
    - null
    metric_stds:
    - 0.021
    - null
    - null
  - model: GraphGPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.13798'
    title: Learning Graph Quantized Tokenizers
    date: '2024-10-17'
    date_iso: '2024-10-17'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5576
    - null
    - null
    metric_stds:
    - 0.0023
    - null
    - null
  - model: JBGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.554
    - null
    - null
    metric_stds:
    - 0.024
    - null
    - null
  - model: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.551
    - null
    - null
    metric_stds:
    - 0.013
    - null
    - null
  - model: SGWT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5504
    - null
    - null
    metric_stds:
    - 0.0112
    - null
    - null
  - model: FA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5488
    - null
    - null
    metric_stds:
    - 0.0282
    - null
    - null
  - model: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5426
    - null
    - null
    metric_stds:
    - 0.018
    - null
    - null
  - model: TAPE (P)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5279
    - null
    - null
    metric_stds:
    - 0.0147
    - null
    - null
  - model: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04082'
    title: 'Curve Your Attention: Mixed-Curvature Transformers for Graph Representation
      Learning'
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5244
    - null
    - null
    metric_stds:
    - 0.0108
    - null
    - null
  - model: DiffPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.504
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
  - model: Deberta-base
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4849
    - null
    - null
    metric_stds:
    - 0.0186
    - null
    - null
  - model: GLEM-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4849
    - null
    - null
    metric_stds:
    - 0.0186
    - null
    - null
  - model: DR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.27529'
    title: Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in
      GNNs
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4435
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: FA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2986
    - null
    - null
    metric_stds:
    - 0.0028000000000000004
    - null
    - null
  - model: DAEGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.58
    - null
    metric_stds:
    - null
    - 0.08
    - null
  - model: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.61
    - null
    metric_stds:
    - null
    - 0.04
    - null
  - model: DMON
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.48
    - null
    metric_stds:
    - null
    - 0.06
    - null
  - model: GRACE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.54
    - null
    metric_stds:
    - null
    - 0.03
    - null
  - model: MVGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.54
    - null
    metric_stds:
    - null
    - 0.03
    - null
  - model: SUBLIME
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.39
    - null
    metric_stds:
    - null
    - 0.05
    - null
  - model: BGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.38
    - null
    metric_stds:
    - null
    - 0.06
    - null
  - model: VGAER
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.54
    - null
    metric_stds:
    - null
    - 0.14
    - null
  - model: uAGNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.48
    - null
    metric_stds:
    - null
    - 0.08
    - null
  - model: Diff
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.04236'
    title: Graph Pooling via Ricci Flow
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.2
    metric_stds:
    - null
    - null
    - 0.04
  - model: MinCut
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.04236'
    title: Graph Pooling via Ricci Flow
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.43
    metric_stds:
    - null
    - null
    - 0.03
  - model: DMON
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.04236'
    title: Graph Pooling via Ricci Flow
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.37
    metric_stds:
    - null
    - null
    - 0.05
  - model: TV
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.04236'
    title: Graph Pooling via Ricci Flow
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.33
    metric_stds:
    - null
    - null
    - 0.05
  - model: ORC (us)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.04236'
    title: Graph Pooling via Ricci Flow
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.47
    metric_stds:
    - null
    - null
    - 0.04
  - model: EMD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.04236'
    title: Graph Pooling via Ricci Flow
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.47
    metric_stds:
    - null
    - null
    - 0.04
  - model: Sinkhorn
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.04236'
    title: Graph Pooling via Ricci Flow
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.45
    metric_stds:
    - null
    - null
    - 0.03
  - model: ORC-approx
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.04236'
    title: Graph Pooling via Ricci Flow
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.45
    metric_stds:
    - null
    - null
    - 0.03
  - model: ORC (us) [2 iters]
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.04236'
    title: Graph Pooling via Ricci Flow
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.44
    metric_stds:
    - null
    - null
    - 0.05
  - model: CurvPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.04236'
    title: Graph Pooling via Ricci Flow
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.35
    metric_stds:
    - null
    - null
    - null
  - model: DyGFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: '2024-06-04'
    date_iso: '2024-06-04'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.0845
    - null
    metric_stds:
    - null
    - 0.0013
    - null
  - model: DyRep
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: '2024-06-04'
    date_iso: '2024-06-04'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.0529
    - null
    metric_stds:
    - null
    - 0.0047
    - null
  - model: GraphMixer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: '2024-06-04'
    date_iso: '2024-06-04'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.066
    - null
    metric_stds:
    - null
    - 0.0011
    - null
  - model: JODIE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: '2024-06-04'
    date_iso: '2024-06-04'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.0633
    - null
    metric_stds:
    - null
    - 0.0041
    - null
  - model: TGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: '2024-06-04'
    date_iso: '2024-06-04'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.0539
    - null
    metric_stds:
    - null
    - 0.0019
    - null
  - model: TGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: '2024-06-04'
    date_iso: '2024-06-04'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.0604
    - null
    metric_stds:
    - null
    - 0.0027
    - null
  - model: Our
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: '2024-06-04'
    date_iso: '2024-06-04'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.0789
    - null
    metric_stds:
    - null
    - 0.0033
    - null
  milestones:
  - value: 0.8952
    std: 0.0043
    model: GAT+JK
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: 2022-10
  - value: 0.8967
    std: 0.0039
    model: ANS-GT + HDSE
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: 2023-08
  - value: 0.9285
    std: 0.0054
    model: GPM
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
---

