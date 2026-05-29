---
title: ogbl-collab
slug: ogbl-collab
benchmark: OGB
task_type: link_prediction
description: Link prediction on academic collaboration network (author co-authorship).
primary_metric: Hits@50
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.OGBLinkPropPredDataset.html
stats:
  num_graphs: 235868
  avg_nodes: 1285465.0
  avg_edges: null
  num_classes: null
result_count: 68
best_model:
  model: ILLS
  value: 0.785
  metric: Hits@50
  arxiv_id: '2305.17589'
  paper_title: Graph Inductive Biases in Transformers without Message Passing
variants:
- slug: standard-split
  name: Standard split
  notes: 'Time-based split. Metric: Hits@50.'
  is_standard: true
  primary_metric: Hits@50
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - Hits@50
  rows:
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
    is_best: true
    metric_values:
    - 0.785
    metric_stds:
    - 0.002
  - model: Graphtransformer
    model_plain: Graphtransformer
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
    metric_stds:
    - 0.003
  - model: PNA
    model_plain: PNA
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
    metric_stds:
    - 0.002
  - model: GIN
    model_plain: GIN
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
    - 0.758
    metric_stds:
    - 0.003
  - model: GAT
    model_plain: GAT
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
    - 0.751
    metric_stds:
    - 0.004
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
    - 0.745
    metric_stds:
    - 0.003
  - model: GCN
    model_plain: GCN
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
    - 0.736
    metric_stds:
    - 0.002
  - model: MPLP
    model_plain: MPLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.00976'
    title: Pure Message Passing Can Estimate Common Neighbor for Link Prediction
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/Barcavin/efficient-node-labelling
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6699
    metric_stds:
    - 0.004
  - model: BUDDY-SIGN (MLP Decoder)
    model_plain: BUDDY-SIGN (MLP Decoder)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.17475'
    title: On the Impact of Feature Heterophily on Link Prediction with Graph Neural
      Networks
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/tensor-gales/HeteLinkPred
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6664
    metric_stds:
    - 0.0064
  - model: NCNC
    model_plain: NCNC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.00976'
    title: Pure Message Passing Can Estimate Common Neighbor for Link Prediction
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/Barcavin/efficient-node-labelling
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6661
    metric_stds:
    - 0.0071
  - model: BUDDY-GCN (MLP Decoder)
    model_plain: BUDDY-GCN (MLP Decoder)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.17475'
    title: On the Impact of Feature Heterophily on Link Prediction with Graph Neural
      Networks
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/tensor-gales/HeteLinkPred
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6621
    metric_stds:
    - 0.0033
  - model: BUDDY-NoFeat (MLP Decoder)
    model_plain: BUDDY-NoFeat (MLP Decoder)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.17475'
    title: On the Impact of Feature Heterophily on Link Prediction with Graph Neural
      Networks
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/tensor-gales/HeteLinkPred
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6606
    metric_stds:
    - 0.0022
  - model: ELPH
    model_plain: ELPH
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.00976'
    title: Pure Message Passing Can Estimate Common Neighbor for Link Prediction
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/Barcavin/efficient-node-labelling
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6594
    metric_stds:
    - 0.0058
  - model: SEAL-PS2
    model_plain: SEAL-PS2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.12488'
    title: 'Bring Your Own View: Graph Neural Networks for Link Prediction with Personalized
      Subgraph Selection'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/qiaoyu-tan/PS2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6483
    metric_stds:
    - 0.0054
  - model: AA
    model_plain: AA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.00976'
    title: Pure Message Passing Can Estimate Common Neighbor for Link Prediction
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/Barcavin/efficient-node-labelling
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6435
    metric_stds:
    - 0.0
  - model: RA
    model_plain: RA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.00976'
    title: Pure Message Passing Can Estimate Common Neighbor for Link Prediction
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/Barcavin/efficient-node-labelling
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.64
    metric_stds:
    - 0.0
  - model: SEAL
    model_plain: SEAL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.12488'
    title: 'Bring Your Own View: Graph Neural Networks for Link Prediction with Personalized
      Subgraph Selection'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/qiaoyu-tan/PS2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6364
    metric_stds:
    - 0.0071
  - model: CN
    model_plain: CN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.00976'
    title: Pure Message Passing Can Estimate Common Neighbor for Link Prediction
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/Barcavin/efficient-node-labelling
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6137
    metric_stds:
    - 0.0
  - model: DE-GNN
    model_plain: DE-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.00170'
    title: Asymmetric Learning for Graph Neural Network based Link Prediction
    date: Mar 2023
    date_iso: 2023-03
    date_display: Mar 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5787
    metric_stds:
    - 0.0079
  - model: AML (G)
    model_plain: AML (G)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.00170'
    title: Asymmetric Learning for Graph Neural Network based Link Prediction
    date: Mar 2023
    date_iso: 2023-03
    date_display: Mar 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.576
    metric_stds:
    - 0.0071
  - model: SEAL
    model_plain: SEAL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.00170'
    title: Asymmetric Learning for Graph Neural Network based Link Prediction
    date: Mar 2023
    date_iso: 2023-03
    date_display: Mar 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5755
    metric_stds:
    - 0.0072
  - model: Neo-GNN
    model_plain: Neo-GNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04216'
    title: 'Neo-GNNs: Neighborhood Overlap-aware Graph Neural Networks for Link Prediction'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seongjunyun/Neo_GNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5752
    metric_stds:
    - 0.0037
  - model: AML (S)
    model_plain: AML (S)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.00170'
    title: Asymmetric Learning for Graph Neural Network based Link Prediction
    date: Mar 2023
    date_iso: 2023-03
    date_display: Mar 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5726
    metric_stds:
    - 0.0125
  - model: AML
    model_plain: AML
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.00170'
    title: Asymmetric Learning for Graph Neural Network based Link Prediction
    date: Mar 2023
    date_iso: 2023-03
    date_display: Mar 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5726
    metric_stds:
    - 0.0125
  - model: AML-R (S)
    model_plain: AML-R (S)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.00170'
    title: Asymmetric Learning for Graph Neural Network based Link Prediction
    date: Mar 2023
    date_iso: 2023-03
    date_display: Mar 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5715
    metric_stds:
    - 0.0032
  - model: AML-R (G)
    model_plain: AML-R (G)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.00170'
    title: Asymmetric Learning for Graph Neural Network based Link Prediction
    date: Mar 2023
    date_iso: 2023-03
    date_display: Mar 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5708
    metric_stds:
    - 0.0119
  - model: AA
    model_plain: AA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.00170'
    title: Asymmetric Learning for Graph Neural Network based Link Prediction
    date: Mar 2023
    date_iso: 2023-03
    date_display: Mar 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5649
    metric_stds:
    - 0.0
  - model: CN
    model_plain: CN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.17475'
    title: On the Impact of Feature Heterophily on Link Prediction with Graph Neural
      Networks
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/tensor-gales/HeteLinkPred
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5644
    metric_stds:
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.00170'
    title: Asymmetric Learning for Graph Neural Network based Link Prediction
    date: Mar 2023
    date_iso: 2023-03
    date_display: Mar 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5643
    metric_stds:
    - 0.0086
  - model: GraphSage-PS2
    model_plain: GraphSage-PS2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.12488'
    title: 'Bring Your Own View: Graph Neural Networks for Link Prediction with Personalized
      Subgraph Selection'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/qiaoyu-tan/PS2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5571
    metric_stds:
    - 0.0093
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.12488'
    title: 'Bring Your Own View: Graph Neural Networks for Link Prediction with Personalized
      Subgraph Selection'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/qiaoyu-tan/PS2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5463
    metric_stds:
    - 0.0112
  - model: SAGE
    model_plain: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.00170'
    title: Asymmetric Learning for Graph Neural Network based Link Prediction
    date: Mar 2023
    date_iso: 2023-03
    date_display: Mar 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5457
    metric_stds:
    - 0.0082
  - model: SEAL
    model_plain: SEAL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04216'
    title: 'Neo-GNNs: Neighborhood Overlap-aware Graph Neural Networks for Link Prediction'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seongjunyun/Neo_GNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5437
    metric_stds:
    - 0.0002
  - model: Adamic Adar
    model_plain: Adamic Adar
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04216'
    title: 'Neo-GNNs: Neighborhood Overlap-aware Graph Neural Networks for Link Prediction'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seongjunyun/Neo_GNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.53
    metric_stds:
    - 0.0
  - model: Resource Allocation
    model_plain: Resource Allocation
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04216'
    title: 'Neo-GNNs: Neighborhood Overlap-aware Graph Neural Networks for Link Prediction'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seongjunyun/Neo_GNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5289
    metric_stds:
    - 0.0
  - model: GAE-PS2
    model_plain: GAE-PS2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.12488'
    title: 'Bring Your Own View: Graph Neural Networks for Link Prediction with Personalized
      Subgraph Selection'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/qiaoyu-tan/PS2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5026
    metric_stds:
    - 0.0032
  - model: Common Neighbors
    model_plain: Common Neighbors
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04216'
    title: 'Neo-GNNs: Neighborhood Overlap-aware Graph Neural Networks for Link Prediction'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seongjunyun/Neo_GNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5006
    metric_stds:
    - 0.0
  - model: CN
    model_plain: CN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.00170'
    title: Asymmetric Learning for Graph Neural Network based Link Prediction
    date: Mar 2023
    date_iso: 2023-03
    date_display: Mar 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4996
    metric_stds:
    - 0.0
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
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.497
    metric_stds:
    - 0.0059
  - model: Node2Vec
    model_plain: Node2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.00170'
    title: Asymmetric Learning for Graph Neural Network based Link Prediction
    date: Mar 2023
    date_iso: 2023-03
    date_display: Mar 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4929
    metric_stds:
    - 0.0064
  - model: LLP
    model_plain: LLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.491
    metric_stds:
    - 0.0057
  - model: JK-Net
    model_plain: JK-Net
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04216'
    title: 'Neo-GNNs: Neighborhood Overlap-aware Graph Neural Networks for Link Prediction'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seongjunyun/Neo_GNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4884
    metric_stds:
    - 0.0083
  - model: SAGE (MLP Decoder)
    model_plain: SAGE (MLP Decoder)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.17475'
    title: On the Impact of Feature Heterophily on Link Prediction with Graph Neural
      Networks
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/tensor-gales/HeteLinkPred
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4864
    metric_stds:
    - 0.0039
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04216'
    title: 'Neo-GNNs: Neighborhood Overlap-aware Graph Neural Networks for Link Prediction'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seongjunyun/Neo_GNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.486
    metric_stds:
    - 0.0046
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
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4819
    metric_stds:
    - 0.0094
  - model: NAGphormer
    model_plain: NAGphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4756
    metric_stds:
    - 0.0052
  - model: SMLP
    model_plain: SMLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.00170'
    title: Asymmetric Learning for Graph Neural Network based Link Prediction
    date: Mar 2023
    date_iso: 2023-03
    date_display: Mar 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4725
    metric_stds:
    - 0.0089
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04216'
    title: 'Neo-GNNs: Neighborhood Overlap-aware Graph Neural Networks for Link Prediction'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seongjunyun/Neo_GNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4701
    metric_stds:
    - 0.0079
  - model: NodeFormer
    model_plain: NodeFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4656
    metric_stds:
    - 0.0062
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04216'
    title: 'Neo-GNNs: Neighborhood Overlap-aware Graph Neural Networks for Link Prediction'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seongjunyun/Neo_GNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4489
    metric_stds:
    - 0.0123
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4475
    metric_stds:
    - 0.0107
  - model: GAE
    model_plain: GAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.12488'
    title: 'Bring Your Own View: Graph Neural Networks for Link Prediction with Personalized
      Subgraph Selection'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/qiaoyu-tan/PS2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4475
    metric_stds:
    - 0.0107
  - model: SEAL-RS
    model_plain: SEAL-RS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.12488'
    title: 'Bring Your Own View: Graph Neural Networks for Link Prediction with Personalized
      Subgraph Selection'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/qiaoyu-tan/PS2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4356
    metric_stds:
    - 0.013
  - model: Node2Vec
    model_plain: Node2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04216'
    title: 'Neo-GNNs: Neighborhood Overlap-aware Graph Neural Networks for Link Prediction'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seongjunyun/Neo_GNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4136
    metric_stds:
    - 0.0069
  - model: GPRGNN (MLP Decoder)
    model_plain: GPRGNN (MLP Decoder)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.17475'
    title: On the Impact of Feature Heterophily on Link Prediction with Graph Neural
      Networks
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/tensor-gales/HeteLinkPred
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3952
    metric_stds:
    - 0.0128
  - model: Matrix Factorization
    model_plain: Matrix Factorization
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04216'
    title: 'Neo-GNNs: Neighborhood Overlap-aware Graph Neural Networks for Link Prediction'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seongjunyun/Neo_GNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3874
    metric_stds:
    - 0.003
  - model: MF
    model_plain: MF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.00170'
    title: Asymmetric Learning for Graph Neural Network based Link Prediction
    date: Mar 2023
    date_iso: 2023-03
    date_display: Mar 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3793
    metric_stds:
    - 0.0076
  - model: GraphSAGE + HR
    model_plain: GraphSAGE + HR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.12488'
    title: 'Bring Your Own View: Graph Neural Networks for Link Prediction with Personalized
      Subgraph Selection'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/qiaoyu-tan/PS2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3754
    metric_stds:
    - 0.0037
  - model: SAGE
    model_plain: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.00976'
    title: Pure Message Passing Can Estimate Common Neighbor for Link Prediction
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/Barcavin/efficient-node-labelling
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3682
    metric_stds:
    - 0.0741
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.00976'
    title: Pure Message Passing Can Estimate Common Neighbor for Link Prediction
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/Barcavin/efficient-node-labelling
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3553
    metric_stds:
    - 0.0239
  - model: GAE-RS
    model_plain: GAE-RS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.12488'
    title: 'Bring Your Own View: Graph Neural Networks for Link Prediction with Personalized
      Subgraph Selection'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/qiaoyu-tan/PS2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3451
    metric_stds:
    - 0.0068
  - model: GCN (MLP Decoder)
    model_plain: GCN (MLP Decoder)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.17475'
    title: On the Impact of Feature Heterophily on Link Prediction with Graph Neural
      Networks
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/tensor-gales/HeteLinkPred
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3017
    metric_stds:
    - 0.029
  - model: GCN (DistMult Decoder)
    model_plain: GCN (DistMult Decoder)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.17475'
    title: On the Impact of Feature Heterophily on Link Prediction with Graph Neural
      Networks
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/tensor-gales/HeteLinkPred
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2842
    metric_stds:
    - 0.0422
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04216'
    title: 'Neo-GNNs: Neighborhood Overlap-aware Graph Neural Networks for Link Prediction'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seongjunyun/Neo_GNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1998
    metric_stds:
    - 0.0096
  - model: SAGE (DOT Decoder)
    model_plain: SAGE (DOT Decoder)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.17475'
    title: On the Impact of Feature Heterophily on Link Prediction with Graph Neural
      Networks
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/tensor-gales/HeteLinkPred
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1971
    metric_stds:
    - 0.0052
  - model: GPRGNN (DOT Decoder)
    model_plain: GPRGNN (DOT Decoder)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.17475'
    title: On the Impact of Feature Heterophily on Link Prediction with Graph Neural
      Networks
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/tensor-gales/HeteLinkPred
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1428
    metric_stds:
    - 0.0252
  - model: GCN (DOT Decoder)
    model_plain: GCN (DOT Decoder)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.17475'
    title: On the Impact of Feature Heterophily on Link Prediction with Graph Neural
      Networks
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/tensor-gales/HeteLinkPred
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1064
    metric_stds:
    - 0.0042
  - model: NoGNN (MLP Decoder)
    model_plain: NoGNN (MLP Decoder)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.17475'
    title: On the Impact of Feature Heterophily on Link Prediction with Graph Neural
      Networks
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/tensor-gales/HeteLinkPred
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0607
    metric_stds:
    - 0.0018
  milestones:
  - value: 0.5752
    std: 0.0037
    model: Neo-GNN
    arxiv_id: '2206.04216'
    title: 'Neo-GNNs: Neighborhood Overlap-aware Graph Neural Networks for Link Prediction'
    date: 2022-06
  - value: 0.6483
    std: 0.0054
    model: SEAL-PS2
    arxiv_id: '2212.12488'
    title: 'Bring Your Own View: Graph Neural Networks for Link Prediction with Personalized
      Subgraph Selection'
    date: 2022-12
  - value: 0.785
    std: 0.002
    model: ILLS
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: '2023-05-27'
---

