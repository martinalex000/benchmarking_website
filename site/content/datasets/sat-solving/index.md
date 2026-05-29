---
title: SAT Solving
slug: sat-solving
benchmark: GraphBench
task_type: node_classification
description: 'SAT problem instances represented as graphs. Multi-level node/edge/graph-level
  tasks across 11 solvers and 3 instance-size scales.

  '
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://graphbench.github.io/website/datasets.html
stats:
  num_graphs: 208788
  avg_nodes: 10400.5
  avg_edges: 2054969.0
  num_classes: null
result_count: 20
best_model:
  model: Threshold-based pooling with supervised attention
  value: 1.0
  metric: Accuracy
  arxiv_id: '1905.02850'
  paper_title: Understanding Attention and Generalization in Graph Neural Networks
variants:
- slug: large
  name: Large
  notes: SAT solving performance prediction on large-scale instances.
  is_standard: false
  primary_metric: Accuracy
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - Accuracy
  - Recall@20
  - Time
  rows:
  - model: Threshold-based pooling with supervised attention
    model_plain: Threshold-based pooling with supervised attention
    is_baseline: false
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
    is_best: true
    metric_values:
    - 1.0
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: ChebyGIN with supervised top-k pooling
    model_plain: ChebyGIN with supervised top-k pooling
    is_baseline: false
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
    - 0.8
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.13522'
    title: 'IGB: Addressing The Gaps In Labeling, Features, Heterogeneity, and Size
      of Public Graph Datasets for Deep Learning Research'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/IllinoisGraphBenchmark/IGB-Datasets
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6489
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
    arxiv_id: '2302.13522'
    title: 'IGB: Addressing The Gaps In Labeling, Features, Heterogeneity, and Size
      of Public Graph Datasets for Deep Learning Research'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/IllinoisGraphBenchmark/IGB-Datasets
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6459
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.13522'
    title: 'IGB: Addressing The Gaps In Labeling, Features, Heterogeneity, and Size
      of Public Graph Datasets for Deep Learning Research'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/IllinoisGraphBenchmark/IGB-Datasets
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5029
    - null
    - null
    metric_stds:
    - null
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
    - 0.31
    - null
    - null
    metric_stds:
    - 0.15
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
    - 0.28
    - null
    - null
    metric_stds:
    - 0.08
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
    - 0.26
    - null
    - null
    metric_stds:
    - 0.11
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
    - 0.2
    - null
    - null
    metric_stds:
    - 0.03
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
    - 0.15
    - null
    - null
    metric_stds:
    - 0.07
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
    - 0.11
    - null
    - null
    metric_stds:
    - 0.06
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
    - 0.11
    - null
    - null
    metric_stds:
    - 0.06
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
    - 0.09
    - null
    - null
    metric_stds:
    - 0.03
    - null
    - null
  - model: AliGraph
    model_plain: AliGraph
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1902.08730'
    title: 'AliGraph: A Comprehensive Graph Neural Network Platform'
    date: Feb 2019
    date_iso: 2019-02
    date_display: Feb 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 300.0
    metric_stds:
    - null
    - null
    - null
  - model: MF
    model_plain: MF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.13973'
    title: Linear-Time Graph Neural Networks for Scalable Recommendations
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/QwQ2000/TheWebConf24-LTGNN-PyTorch
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.02752
    - null
    metric_stds:
    - null
    - null
    - null
  - model: NCF
    model_plain: NCF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.13973'
    title: Linear-Time Graph Neural Networks for Scalable Recommendations
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/QwQ2000/TheWebConf24-LTGNN-PyTorch
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.02785
    - null
    metric_stds:
    - null
    - null
    - null
  - model: PinSage
    model_plain: PinSage
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.13973'
    title: Linear-Time Graph Neural Networks for Scalable Recommendations
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/QwQ2000/TheWebConf24-LTGNN-PyTorch
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.02809
    - null
    metric_stds:
    - null
    - null
    - null
  - model: LightGCN
    model_plain: LightGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.13973'
    title: Linear-Time Graph Neural Networks for Scalable Recommendations
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/QwQ2000/TheWebConf24-LTGNN-PyTorch
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.02903
    - null
    metric_stds:
    - null
    - null
    - null
  - model: LightGCN-GAS
    model_plain: LightGCN-GAS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.13973'
    title: Linear-Time Graph Neural Networks for Scalable Recommendations
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/QwQ2000/TheWebConf24-LTGNN-PyTorch
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.02886
    - null
    metric_stds:
    - null
    - null
    - null
  - model: LTGNN
    model_plain: LTGNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.13973'
    title: Linear-Time Graph Neural Networks for Scalable Recommendations
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/QwQ2000/TheWebConf24-LTGNN-PyTorch
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.02942
    - null
    metric_stds:
    - null
    - null
    - null
  milestones:
  - value: 1.0
    std: null
    model: Threshold-based pooling with supervised attention
    arxiv_id: '1905.02850'
    title: Understanding Attention and Generalization in Graph Neural Networks
    date: 2019-05
- slug: small
  name: Small
  notes: SAT solving performance prediction on small instances.
  is_standard: false
  primary_metric: Accuracy
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - Accuracy
  - Deg.
  - Degree
  - F1
  - MMD
  - MMD Clus
  - MMD Deg
  - MMD Orb
  - MMD Spect
  rows:
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.13522'
    title: 'IGB: Addressing The Gaps In Labeling, Features, Heterogeneity, and Size
      of Public Graph Datasets for Deep Learning Research'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/IllinoisGraphBenchmark/IGB-Datasets
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.7549
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
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
    arxiv_id: '2302.13522'
    title: 'IGB: Addressing The Gaps In Labeling, Features, Heterogeneity, and Size
      of Public Graph Datasets for Deep Learning Research'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/IllinoisGraphBenchmark/IGB-Datasets
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7093
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
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
    arxiv_id: '2302.13522'
    title: 'IGB: Addressing The Gaps In Labeling, Features, Heterogeneity, and Size
      of Public Graph Datasets for Deep Learning Research'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/IllinoisGraphBenchmark/IGB-Datasets
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
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HEP
    model_plain: HEP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1902.08730'
    title: 'AliGraph: A Comprehensive Graph Neural Network Platform'
    date: Feb 2019
    date_iso: 2019-02
    date_display: Feb 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.5793
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AHEP
    model_plain: AHEP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1902.08730'
    title: 'AliGraph: A Comprehensive Graph Neural Network Platform'
    date: Feb 2019
    date_iso: 2019-02
    date_display: Feb 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.5097
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
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
    arxiv_id: '1902.08730'
    title: 'AliGraph: A Comprehensive Graph Neural Network Platform'
    date: Feb 2019
    date_iso: 2019-02
    date_display: Feb 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.7014
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MVE
    model_plain: MVE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1902.08730'
    title: 'AliGraph: A Comprehensive Graph Neural Network Platform'
    date: Feb 2019
    date_iso: 2019-02
    date_display: Feb 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.7214
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MNE
    model_plain: MNE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1902.08730'
    title: 'AliGraph: A Comprehensive Graph Neural Network Platform'
    date: Feb 2019
    date_iso: 2019-02
    date_display: Feb 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.8486
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
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
    arxiv_id: '1902.08730'
    title: 'AliGraph: A Comprehensive Graph Neural Network Platform'
    date: Feb 2019
    date_iso: 2019-02
    date_display: Feb 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.8994
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
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
    arxiv_id: '2502.04308'
    title: 'HOG-Diff: Higher-Order Guided Diffusion for Graph Generation'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.09
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphAF
    model_plain: GraphAF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.04308'
    title: 'HOG-Diff: Higher-Order Guided Diffusion for Graph Generation'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.03
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphDF
    model_plain: GraphDF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.04308'
    title: 'HOG-Diff: Higher-Order Guided Diffusion for Graph Generation'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.04
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
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
    arxiv_id: '2502.04308'
    title: 'HOG-Diff: Higher-Order Guided Diffusion for Graph Generation'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.13
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GNF
    model_plain: GNF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.04308'
    title: 'HOG-Diff: Higher-Order Guided Diffusion for Graph Generation'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.03
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: EDP-GNN
    model_plain: EDP-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.04308'
    title: 'HOG-Diff: Higher-Order Guided Diffusion for Graph Generation'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.052
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPrinFlowNet
    model_plain: GPrinFlowNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.04308'
    title: 'HOG-Diff: Higher-Order Guided Diffusion for Graph Generation'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.021
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SPECTRE
    model_plain: SPECTRE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.04308'
    title: 'HOG-Diff: Higher-Order Guided Diffusion for Graph Generation'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.078
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GDSS
    model_plain: GDSS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.04308'
    title: 'HOG-Diff: Higher-Order Guided Diffusion for Graph Generation'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.021
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DiGress
    model_plain: DiGress
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.04308'
    title: 'HOG-Diff: Higher-Order Guided Diffusion for Graph Generation'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.015
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HOG-Diff
    model_plain: HOG-Diff
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.04308'
    title: 'HOG-Diff: Higher-Order Guided Diffusion for Graph Generation'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.015
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGAE
    model_plain: DGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.07735'
    title: Discrete Graph Auto-Encoder
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.032
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.019
    - null
    - null
    - null
    - null
  - model: GDSS
    model_plain: GDSS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.07735'
    title: Discrete Graph Auto-Encoder
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.045
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.028
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
    arxiv_id: '2211.10794'
    title: DDGM
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.09
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphDF
    model_plain: GraphDF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.10794'
    title: DDGM
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.04
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphNF
    model_plain: GraphNF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.10794'
    title: DDGM
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: EDP-GNN
    model_plain: EDP-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.10794'
    title: DDGM
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.052
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GDSS
    model_plain: GDSS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.10794'
    title: DDGM
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.021
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphLSGM
    model_plain: GraphLSGM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.10794'
    title: DDGM
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
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
    arxiv_id: '2402.18974'
    title: Generating Graphs via Spectral Diffusion
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/lcosmo/GGSD
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.1072
    - 0.0271
    - 0.1469
    - 0.052
    metric_stds:
    - null
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
    arxiv_id: '2402.18974'
    title: Generating Graphs via Spectral Diffusion
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/lcosmo/GGSD
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.0843
    - 0.0013
    - 0.0201
    - 0.0282
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DiGress
    model_plain: DiGress
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.18974'
    title: Generating Graphs via Spectral Diffusion
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/lcosmo/GGSD
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.1035
    - 0.0096
    - 0.0372
    - 0.0506
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GSDM
    model_plain: GSDM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.18974'
    title: Generating Graphs via Spectral Diffusion
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/lcosmo/GGSD
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.0446
    - 0.0099
    - 0.0155
    - 0.0131
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GDSS
    model_plain: GDSS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.18974'
    title: Generating Graphs via Spectral Diffusion
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/lcosmo/GGSD
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.106
    - 0.0107
    - 0.0356
    - 0.045
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SPECTRE
    model_plain: SPECTRE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.18974'
    title: Generating Graphs via Spectral Diffusion
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/lcosmo/GGSD
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.1067
    - 0.0079
    - 0.025
    - 0.046
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GGSD
    model_plain: GGSD
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.18974'
    title: Generating Graphs via Spectral Diffusion
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/lcosmo/GGSD
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.059
    - 0.0016
    - 0.0142
    - 0.0153
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSNN
    model_plain: GraphSNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.03687'
    title: 'Pard: Permutation-invariant Autoregressive Diffusion for Graph Generation'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LingxiaoShawn/Pard
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.08
    - null
    - null
    - null
    - null
    metric_stds:
    - null
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
    arxiv_id: '2402.03687'
    title: 'Pard: Permutation-invariant Autoregressive Diffusion for Graph Generation'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LingxiaoShawn/Pard
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.06
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: EDP-GNN
    model_plain: EDP-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.03687'
    title: 'Pard: Permutation-invariant Autoregressive Diffusion for Graph Generation'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LingxiaoShawn/Pard
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.053
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GDSS
    model_plain: GDSS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.03687'
    title: 'Pard: Permutation-invariant Autoregressive Diffusion for Graph Generation'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LingxiaoShawn/Pard
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.045
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphArm
    model_plain: GraphArm
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.03687'
    title: 'Pard: Permutation-invariant Autoregressive Diffusion for Graph Generation'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LingxiaoShawn/Pard
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.034
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DiGress
    model_plain: DiGress
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.03687'
    title: 'Pard: Permutation-invariant Autoregressive Diffusion for Graph Generation'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LingxiaoShawn/Pard
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.047
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: higher-order graph transformer
    model_plain: higher-order graph transformer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.03687'
    title: 'Pard: Permutation-invariant Autoregressive Diffusion for Graph Generation'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LingxiaoShawn/Pard
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.023
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SDE
    model_plain: SDE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.08892'
    title: Fast Graph Generation via Spectral Diffusion
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.009
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DeepGMG
    model_plain: DeepGMG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.08892'
    title: Fast Graph Generation via Spectral Diffusion
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.523
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
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
    arxiv_id: '2211.08892'
    title: Fast Graph Generation via Spectral Diffusion
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.08
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphAF
    model_plain: GraphAF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.08892'
    title: Fast Graph Generation via Spectral Diffusion
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.133
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphDF
    model_plain: GraphDF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.08892'
    title: Fast Graph Generation via Spectral Diffusion
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.07
    - null
    - null
    - null
    - null
    metric_stds:
    - null
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
    arxiv_id: '2211.08892'
    title: Fast Graph Generation via Spectral Diffusion
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.623
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GNF
    model_plain: GNF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.08892'
    title: Fast Graph Generation via Spectral Diffusion
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.17
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: EDP-GNN
    model_plain: EDP-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.08892'
    title: Fast Graph Generation via Spectral Diffusion
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.074
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GDSS
    model_plain: GDSS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.08892'
    title: Fast Graph Generation via Spectral Diffusion
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.046
    - null
    - null
    - null
    - null
    metric_stds:
    - null
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
    arxiv_id: '2406.04843'
    title: Variational Flow Matching for Graph Generation
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.35
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GNF
    model_plain: GNF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.04843'
    title: Variational Flow Matching for Graph Generation
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.2
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: EDP-GNN
    model_plain: EDP-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.04843'
    title: Variational Flow Matching for Graph Generation
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.053
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GDSS
    model_plain: GDSS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.04843'
    title: Variational Flow Matching for Graph Generation
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.045
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CatFlow
    model_plain: CatFlow
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.04843'
    title: Variational Flow Matching for Graph Generation
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.018
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  milestones:
  - value: 0.7549
    std: null
    model: GraphSAGE
    arxiv_id: '2302.13522'
    title: 'IGB: Addressing The Gaps In Labeling, Features, Heterogeneity, and Size
      of Public Graph Datasets for Deep Learning Research'
    date: 2023-02
---

