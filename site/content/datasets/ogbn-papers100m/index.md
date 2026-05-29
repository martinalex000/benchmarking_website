---
title: ogbn-papers100M
slug: ogbn-papers100m
benchmark: OGB
task_type: node_classification
description: Node classification on 111M academic paper citation network (172 subjects).
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.OGBNodePropPredDataset.html
stats:
  num_graphs: 111059956
  avg_nodes: 1615685872.0
  avg_edges: null
  num_classes: 172
result_count: 105
best_model:
  model: ILSS
  value: 0.782
  metric: Accuracy
  arxiv_id: '2305.17589'
  paper_title: Graph Inductive Biases in Transformers without Message Passing
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
  - Macro-F1
  - Micro-F1
  - Node-C
  rows:
  - model: ILSS
    model_plain: ILSS
    is_baseline: true
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
    is_best: true
    metric_values:
    - 0.782
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
  - model: Graver
    model_plain: Graver
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.05592'
    title: 'Graver: Generative Graph Vocabularies for Robust Graph Foundation Models
      Fine-tuning'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: https://github.com/RingBDStack/GRAVER
    uses_external_data: true
    is_best: true
    metric_values:
    - 0.7762
    - null
    - null
    - null
    metric_stds:
    - 0.0294
    - null
    - null
    - null
  - model: GraphSAINT + RWSE
    model_plain: GraphSAINT + RWSE
    is_baseline: true
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
    - 0.775
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
  - model: Neighbor Sampling (NS)
    model_plain: Neighbor Sampling (NS)
    is_baseline: true
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
    - 0.773
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
  - model: LADIES
    model_plain: LADIES
    is_baseline: true
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
    - 0.771
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
  - model: GraphSAINT
    model_plain: GraphSAINT
    is_baseline: true
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
    - 0.768
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
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
    - 0.765
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
  - model: Cluster-GCN
    model_plain: Cluster-GCN
    is_baseline: true
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
    - 0.762
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06443'
    title: How Wide and How Deep? Mitigating Over-Squashing of GNNs via Channel Capacity
      Constrained Estimation
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: https://github.com/pixelhero98/C3E
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.76
    - null
    - null
    - null
    metric_stds:
    - 0.0
    - null
    - null
    - null
  - model: FastGCN
    model_plain: FastGCN
    is_baseline: true
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
    - 0.759
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
  - model: JacobiConv
    model_plain: JacobiConv
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06443'
    title: How Wide and How Deep? Mitigating Over-Squashing of GNNs via Channel Capacity
      Constrained Estimation
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: https://github.com/pixelhero98/C3E
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.759
    - null
    - null
    - null
    metric_stds:
    - 0.0
    - null
    - null
    - null
  - model: S2GCN
    model_plain: S2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06443'
    title: How Wide and How Deep? Mitigating Over-Squashing of GNNs via Channel Capacity
      Constrained Estimation
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: https://github.com/pixelhero98/C3E
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.753
    - null
    - null
    - null
    metric_stds:
    - 0.0
    - null
    - null
    - null
  - model: SAMGPT
    model_plain: SAMGPT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.05592'
    title: 'Graver: Generative Graph Vocabularies for Robust Graph Foundation Models
      Fine-tuning'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: https://github.com/RingBDStack/GRAVER
    uses_external_data: true
    is_best: true
    metric_values:
    - 0.736
    - null
    - null
    - null
    metric_stds:
    - 0.0755
    - null
    - null
    - null
  - model: ProNoG
    model_plain: ProNoG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.05592'
    title: 'Graver: Generative Graph Vocabularies for Robust Graph Foundation Models
      Fine-tuning'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: https://github.com/RingBDStack/GRAVER
    uses_external_data: true
    is_best: true
    metric_values:
    - 0.7349
    - null
    - null
    - null
    metric_stds:
    - 0.0734
    - null
    - null
    - null
  - model: MDGPT
    model_plain: MDGPT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.05592'
    title: 'Graver: Generative Graph Vocabularies for Robust Graph Foundation Models
      Fine-tuning'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: https://github.com/RingBDStack/GRAVER
    uses_external_data: true
    is_best: true
    metric_values:
    - 0.721
    - null
    - null
    - null
    metric_stds:
    - 0.0712
    - null
    - null
    - null
  - model: GCOPE
    model_plain: GCOPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.05592'
    title: 'Graver: Generative Graph Vocabularies for Robust Graph Foundation Models
      Fine-tuning'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: https://github.com/RingBDStack/GRAVER
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7126
    - null
    - null
    - null
    metric_stds:
    - 0.0595
    - null
    - null
    - null
  - model: GLEM-GNN
    model_plain: GLEM-GNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.14709'
    title: Learning on Large-scale Text-attributed Graphs via Variational Inference
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: https://github.com/AndyJZhao/GLEM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7036
    - null
    - null
    - null
    metric_stds:
    - 0.0002
    - null
    - null
    - null
  - model: GraphPrompt
    model_plain: GraphPrompt
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.05592'
    title: 'Graver: Generative Graph Vocabularies for Robust Graph Foundation Models
      Fine-tuning'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: https://github.com/RingBDStack/GRAVER
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7011
    - null
    - null
    - null
    metric_stds:
    - 0.0662
    - null
    - null
    - null
  - model: GPF
    model_plain: GPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.05592'
    title: 'Graver: Generative Graph Vocabularies for Robust Graph Foundation Models
      Fine-tuning'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: https://github.com/RingBDStack/GRAVER
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7007
    - null
    - null
    - null
    metric_stds:
    - 0.0655
    - null
    - null
    - null
  - model: ChebNet
    model_plain: ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06443'
    title: How Wide and How Deep? Mitigating Over-Squashing of GNNs via Channel Capacity
      Constrained Estimation
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: https://github.com/pixelhero98/C3E
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.691
    - null
    - null
    - null
    metric_stds:
    - 0.0
    - null
    - null
    - null
  - model: GDC_PPR
    model_plain: GDC_PPR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06443'
    title: How Wide and How Deep? Mitigating Over-Squashing of GNNs via Channel Capacity
      Constrained Estimation
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: https://github.com/pixelhero98/C3E
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.688
    - null
    - null
    - null
    metric_stds:
    - 0.0
    - null
    - null
    - null
  - model: RLU+SCR
    model_plain: RLU+SCR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2112.04319'
    title: 'SCR: Training Graph Neural Networks with Consistency Regularization'
    date: Dec 2021
    date_iso: 2021-12
    date_display: Dec 2021
    codebase_url: https://github.com/THUDM/SCR
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6842
    - null
    - null
    - null
    metric_stds:
    - 0.0015
    - null
    - null
    - null
  - model: GAMLP
    model_plain: GAMLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.14709'
    title: Learning on Large-scale Text-attributed Graphs via Variational Inference
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: https://github.com/AndyJZhao/GLEM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6825
    - null
    - null
    - null
    metric_stds:
    - 0.0011
    - null
    - null
    - null
  - model: GAMLP+RLU
    model_plain: GAMLP+RLU
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.10097'
    title: Graph Attention MLP with Reliable Label Utilization
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6825
    - null
    - null
    - null
    metric_stds:
    - 0.0011
    - null
    - null
    - null
  - model: RLU
    model_plain: RLU
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2112.04319'
    title: 'SCR: Training Graph Neural Networks with Consistency Regularization'
    date: Dec 2021
    date_iso: 2021-12
    date_display: Dec 2021
    codebase_url: https://github.com/THUDM/SCR
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6825
    - null
    - null
    - null
    metric_stds:
    - 0.0011
    - null
    - null
    - null
  - model: SCR-m
    model_plain: SCR-m
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2112.04319'
    title: 'SCR: Training Graph Neural Networks with Consistency Regularization'
    date: Dec 2021
    date_iso: 2021-12
    date_display: Dec 2021
    codebase_url: https://github.com/THUDM/SCR
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6816
    - null
    - null
    - null
    metric_stds:
    - 0.0012
    - null
    - null
    - null
  - model: SCR
    model_plain: SCR
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2112.04319'
    title: 'SCR: Training Graph Neural Networks with Consistency Regularization'
    date: Dec 2021
    date_iso: 2021-12
    date_display: Dec 2021
    codebase_url: https://github.com/THUDM/SCR
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6814
    - null
    - null
    - null
    metric_stds:
    - 0.0008
    - null
    - null
    - null
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06443'
    title: How Wide and How Deep? Mitigating Over-Squashing of GNNs via Channel Capacity
      Constrained Estimation
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: https://github.com/pixelhero98/C3E
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.681
    - null
    - null
    - null
    metric_stds:
    - 0.0
    - null
    - null
    - null
  - model: SAGN+0-SLE
    model_plain: SAGN+0-SLE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.10097'
    title: Graph Attention MLP with Reliable Label Utilization
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.68
    - null
    - null
    - null
    metric_stds:
    - 0.0015
    - null
    - null
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06443'
    title: How Wide and How Deep? Mitigating Over-Squashing of GNNs via Channel Capacity
      Constrained Estimation
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: https://github.com/pixelhero98/C3E
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.679
    - null
    - null
    - null
    metric_stds:
    - 0.0
    - null
    - null
    - null
  - model: GAMLP
    model_plain: GAMLP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.10097'
    title: Graph Attention MLP with Reliable Label Utilization
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6771
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
  - model: TOP-GCNII
    model_plain: TOP-GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.19693'
    title: Accurate and Scalable Graph Neural Networks via Message Invariance
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/MIRALab-USTC/TOP
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6721
    - null
    - null
    - null
    metric_stds:
    - 0.0012
    - null
    - null
    - null
  - model: simple GNN model
    model_plain: simple GNN model
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
    - 0.6717
    - null
    - null
    - null
    metric_stds:
    - 0.0014
    - null
    - null
    - null
  - model: GDC_HK
    model_plain: GDC_HK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06443'
    title: How Wide and How Deep? Mitigating Over-Squashing of GNNs via Channel Capacity
      Constrained Estimation
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: https://github.com/pixelhero98/C3E
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.671
    - null
    - null
    - null
    metric_stds:
    - 0.0
    - null
    - null
    - null
  - model: SHADOW-GAT
    model_plain: SHADOW-GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.19693'
    title: Accurate and Scalable Graph Neural Networks via Message Invariance
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/MIRALab-USTC/TOP
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6708
    - null
    - null
    - null
    metric_stds:
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
    arxiv_id: '2502.19693'
    title: Accurate and Scalable Graph Neural Networks via Message Invariance
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/MIRALab-USTC/TOP
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6706
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: SIGN-XL
    model_plain: SIGN-XL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2112.04319'
    title: 'SCR: Training Graph Neural Networks with Consistency Regularization'
    date: Dec 2021
    date_iso: 2021-12
    date_display: Dec 2021
    codebase_url: https://github.com/THUDM/SCR
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6706
    - null
    - null
    - null
    metric_stds:
    - 0.0017
    - null
    - null
    - null
  - model: GPRGNN
    model_plain: GPRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06443'
    title: How Wide and How Deep? Mitigating Over-Squashing of GNNs via Channel Capacity
      Constrained Estimation
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: https://github.com/pixelhero98/C3E
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.668
    - null
    - null
    - null
    metric_stds:
    - 0.0
    - null
    - null
    - null
  - model: SAGN
    model_plain: SAGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2112.04319'
    title: 'SCR: Training Graph Neural Networks with Consistency Regularization'
    date: Dec 2021
    date_iso: 2021-12
    date_display: Dec 2021
    codebase_url: https://github.com/THUDM/SCR
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6675
    - null
    - null
    - null
    metric_stds:
    - 0.0084
    - null
    - null
    - null
  - model: GraphCL
    model_plain: GraphCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.05592'
    title: 'Graver: Generative Graph Vocabularies for Robust Graph Foundation Models
      Fine-tuning'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: https://github.com/RingBDStack/GRAVER
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.667
    - null
    - null
    - null
    metric_stds:
    - 0.0429
    - null
    - null
    - null
  - model: HSIC-C-GraphSAGE
    model_plain: HSIC-C-GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.06483'
    title: arXiv:2111.06483
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.663
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: SIGN-XL
    model_plain: SIGN-XL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.10097'
    title: Graph Attention MLP with Reliable Label Utilization
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6606
    - null
    - null
    - null
    metric_stds:
    - 0.0019
    - null
    - null
    - null
  - model: SIGN
    model_plain: SIGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.19693'
    title: Accurate and Scalable Graph Neural Networks via Message Invariance
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/MIRALab-USTC/TOP
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6606
    - null
    - null
    - null
    metric_stds:
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
    - 0.6601
    - null
    - null
    - null
    metric_stds:
    - 0.0037
    - null
    - null
    - null
  - model: GPPT
    model_plain: GPPT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.05592'
    title: 'Graver: Generative Graph Vocabularies for Robust Graph Foundation Models
      Fine-tuning'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: https://github.com/RingBDStack/GRAVER
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6581
    - null
    - null
    - null
    metric_stds:
    - 0.0656
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.06483'
    title: arXiv:2111.06483
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.658
    - null
    - null
    - null
    metric_stds:
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
    - 0.657
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
  - model: SIGN
    model_plain: SIGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.10097'
    title: Graph Attention MLP with Reliable Label Utilization
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6568
    - null
    - null
    - null
    metric_stds:
    - 0.0006
    - null
    - null
    - null
  - model: Neighbor2Seq+Conv
    model_plain: Neighbor2Seq+Conv
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.03341'
    title: 'Neighbor2Seq: Deep Learning on Massive Graphs by Transforming Neighbors
      to Sequences'
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/divelab/Neighbor2Seq
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6562
    - null
    - null
    - null
    metric_stds:
    - 0.0032
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
    - 0.652
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
  - model: SIGN(3,3,3)
    model_plain: SIGN(3,3,3)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.11198'
    title: 'SIGN: Scalable Inception Graph Neural Networks'
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6511
    - null
    - null
    - null
    metric_stds:
    - 0.0014
    - null
    - null
    - null
  - model: SIGN
    model_plain: SIGN
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
    - 0.6511
    - null
    - null
    - null
    metric_stds:
    - 0.0014
    - null
    - null
    - null
  - model: Neighbor2Seq+Attn
    model_plain: Neighbor2Seq+Attn
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.03341'
    title: 'Neighbor2Seq: Deep Learning on Massive Graphs by Transforming Neighbors
      to Sequences'
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/divelab/Neighbor2Seq
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6504
    - null
    - null
    - null
    metric_stds:
    - 0.0024
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: false
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
    - 0.648
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
  - model: GCC
    model_plain: GCC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.05592'
    title: 'Graver: Generative Graph Vocabularies for Robust Graph Foundation Models
      Fine-tuning'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: https://github.com/RingBDStack/GRAVER
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6474
    - null
    - null
    - null
    metric_stds:
    - 0.0378
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
    - 0.647
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
  - model: GAT + C&S
    model_plain: GAT + C&S
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.06483'
    title: arXiv:2111.06483
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.645
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: SIGN(3,1,1)
    model_plain: SIGN(3,1,1)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.11198'
    title: 'SIGN: Scalable Inception Graph Neural Networks'
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6439
    - null
    - null
    - null
    metric_stds:
    - 0.0018
    - null
    - null
    - null
  - model: SIGN(3,0,0)
    model_plain: SIGN(3,0,0)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.11198'
    title: 'SIGN: Scalable Inception Graph Neural Networks'
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6428
    - null
    - null
    - null
    metric_stds:
    - 0.0014
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
    - 0.642
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.05592'
    title: 'Graver: Generative Graph Vocabularies for Robust Graph Foundation Models
      Fine-tuning'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: https://github.com/RingBDStack/GRAVER
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6376
    - null
    - null
    - null
    metric_stds:
    - 0.0377
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.06483'
    title: arXiv:2111.06483
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.637
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: LM-Ft
    model_plain: LM-Ft
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.14709'
    title: Learning on Large-scale Text-attributed Graphs via Variational Inference
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: https://github.com/AndyJZhao/GLEM
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6352
    - null
    - null
    - null
    metric_stds:
    - 0.0006
    - null
    - null
    - null
  - model: GAT-NSampler
    model_plain: GAT-NSampler
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
    - 0.6347
    - null
    - null
    - null
    metric_stds:
    - 0.0039
    - null
    - null
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2005.00687'
    title: 'Open Graph Benchmark: Datasets for Machine Learning on Graphs'
    date: May 2020
    date_iso: 2020-05
    date_display: May 2020
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6329
    - null
    - null
    - null
    metric_stds:
    - 0.0019
    - null
    - null
    - null
  - model: S-GCN
    model_plain: S-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.11198'
    title: 'SIGN: Scalable Inception Graph Neural Networks'
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6329
    - null
    - null
    - null
    metric_stds:
    - 0.0019
    - null
    - null
    - null
  - model: GCN-NSampler
    model_plain: GCN-NSampler
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
    - 0.6204
    - null
    - null
    - null
    metric_stds:
    - 0.0027
    - null
    - null
    - null
  - model: GCN (bb.)
    model_plain: GCN (bb.)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.05592'
    title: 'Graver: Generative Graph Vocabularies for Robust Graph Foundation Models
      Fine-tuning'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: https://github.com/RingBDStack/GRAVER
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6159
    - null
    - null
    - null
    metric_stds:
    - 0.0513
    - null
    - null
    - null
  - model: DSSL
    model_plain: DSSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.05592'
    title: 'Graver: Generative Graph Vocabularies for Robust Graph Foundation Models
      Fine-tuning'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: https://github.com/RingBDStack/GRAVER
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6127
    - null
    - null
    - null
    metric_stds:
    - 0.0521
    - null
    - null
    - null
  - model: Node2Vec
    model_plain: Node2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.11198'
    title: 'SIGN: Scalable Inception Graph Neural Networks'
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.5807
    - null
    - null
    - null
    metric_stds:
    - 0.0028
    - null
    - null
    - null
  - model: Node2Vec
    model_plain: Node2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.03341'
    title: 'Neighbor2Seq: Deep Learning on Massive Graphs by Transforming Neighbors
      to Sequences'
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/divelab/Neighbor2Seq
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.556
    - null
    - null
    - null
    metric_stds:
    - 0.0023
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
    - 0.529
    - null
    - null
    - null
    metric_stds:
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
    - 0.526
    - null
    - null
    - null
    metric_stds:
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
    arxiv_id: '2502.19693'
    title: Accurate and Scalable Graph Neural Networks via Message Invariance
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/MIRALab-USTC/TOP
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5173
    - null
    - null
    - null
    metric_stds:
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
    - 0.516
    - null
    - null
    - null
    metric_stds:
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
    - 0.515
    - null
    - null
    - null
    metric_stds:
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
    - 0.512
    - null
    - null
    - null
    metric_stds:
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
    arxiv_id: '2004.11198'
    title: 'SIGN: Scalable Inception Graph Neural Networks'
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4724
    - null
    - null
    - null
    metric_stds:
    - 0.0031
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.175
    - null
    - null
    - null
    metric_stds:
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
    - 0.174
    - null
    - null
    - null
    metric_stds:
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.173
    - null
    - null
    - null
    metric_stds:
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.151
    - null
    - null
    - null
    metric_stds:
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.144
    - null
    - null
    - null
    metric_stds:
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
    - null
    - 0.3112
    - 0.4231
    - null
    metric_stds:
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
    - null
    - 0.5402
    - 0.6234
    - null
    metric_stds:
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
    - null
    - 0.5359
    - 0.6232
    - null
    metric_stds:
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
    - null
    - 0.538
    - 0.6263
    - null
    metric_stds:
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
    - null
    - 0.5397
    - 0.6266
    - null
    metric_stds:
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
    - null
    - 0.5379
    - 0.6253
    - null
    metric_stds:
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
    - null
    - 0.5349
    - 0.6185
    - null
    metric_stds:
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
    - null
    - 0.5355
    - 0.6197
    - null
    metric_stds:
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
    - null
    - 0.5363
    - 0.6252
    - null
    metric_stds:
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
    - null
    - 0.5474
    - 0.6375
    - null
    metric_stds:
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
    - null
    - 0.555
    - 0.6395
    - null
    metric_stds:
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
    - null
    - 0.5548
    - 0.6395
    - null
    metric_stds:
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
    - null
    - 0.5742
    - 0.6569
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: LightDiC
    model_plain: LightDiC
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.11772'
    title: 'LightDiC: A Simple yet Effective Approach for Large-scale Digraph Representation
      Learning'
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: https://github.com/xkLi-Allen/LightDiC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.654
    metric_stds:
    - null
    - null
    - null
    - 0.002
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.11772'
    title: 'LightDiC: A Simple yet Effective Approach for Large-scale Digraph Representation
      Learning'
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: https://github.com/xkLi-Allen/LightDiC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.472
    metric_stds:
    - null
    - null
    - null
    - 0.003
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.11772'
    title: 'LightDiC: A Simple yet Effective Approach for Large-scale Digraph Representation
      Learning'
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: https://github.com/xkLi-Allen/LightDiC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.458
    metric_stds:
    - null
    - null
    - null
    - 0.001
  - model: GBP
    model_plain: GBP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.11772'
    title: 'LightDiC: A Simple yet Effective Approach for Large-scale Digraph Representation
      Learning'
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: https://github.com/xkLi-Allen/LightDiC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.483
    metric_stds:
    - null
    - null
    - null
    - 0.002
  - model: SIGN
    model_plain: SIGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.11772'
    title: 'LightDiC: A Simple yet Effective Approach for Large-scale Digraph Representation
      Learning'
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: https://github.com/xkLi-Allen/LightDiC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.525
    metric_stds:
    - null
    - null
    - null
    - 0.002
  - model: S^2GC
    model_plain: S^2GC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.11772'
    title: 'LightDiC: A Simple yet Effective Approach for Large-scale Digraph Representation
      Learning'
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: https://github.com/xkLi-Allen/LightDiC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.506
    metric_stds:
    - null
    - null
    - null
    - 0.001
  - model: SAGE
    model_plain: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.11772'
    title: 'LightDiC: A Simple yet Effective Approach for Large-scale Digraph Representation
      Learning'
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: https://github.com/xkLi-Allen/LightDiC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.552
    metric_stds:
    - null
    - null
    - null
    - 0.002
  - model: UniMP
    model_plain: UniMP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.11772'
    title: 'LightDiC: A Simple yet Effective Approach for Large-scale Digraph Representation
      Learning'
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: https://github.com/xkLi-Allen/LightDiC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.547
    metric_stds:
    - null
    - null
    - null
    - 0.003
  - model: GAMLP
    model_plain: GAMLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.11772'
    title: 'LightDiC: A Simple yet Effective Approach for Large-scale Digraph Representation
      Learning'
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: https://github.com/xkLi-Allen/LightDiC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.568
    metric_stds:
    - null
    - null
    - null
    - 0.003
  milestones:
  - value: 0.6511
    std: 0.0014
    model: SIGN(3,3,3)
    arxiv_id: '2004.11198'
    title: 'SIGN: Scalable Inception Graph Neural Networks'
    date: 2020-04
  - value: 0.6717
    std: 0.0014
    model: simple GNN model
    arxiv_id: '2105.07634'
    title: Improving Graph Neural Networks with Simple Architecture Design
    date: 2021-05
  - value: 0.6825
    std: 0.0011
    model: GAMLP+RLU
    arxiv_id: '2108.10097'
    title: Graph Attention MLP with Reliable Label Utilization
    date: 2021-08
  - value: 0.6842
    std: 0.0015
    model: RLU+SCR
    arxiv_id: '2112.04319'
    title: 'SCR: Training Graph Neural Networks with Consistency Regularization'
    date: 2021-12
  - value: 0.7036
    std: 0.0002
    model: GLEM-GNN
    arxiv_id: '2210.14709'
    title: Learning on Large-scale Text-attributed Graphs via Variational Inference
    date: 2022-10
  - value: 0.782
    std: 0.001
    model: ILSS
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: '2023-05-27'
---

